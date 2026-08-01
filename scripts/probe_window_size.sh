#!/usr/bin/env bash
# Find the largest window that completes inside the gateway's ~30 s deadline.
#
# The gateway returns HTTP 504 at a fixed ~30.5 s for non-streamed requests, and
# its SSE mode ends the response after the first delta. So the only remaining
# lever is per-request work: shrink the window until generation finishes in time.
#
# This sends REAL text from your cleaned document at several sizes and reports
# status + wall time + completion_tokens for each. Pick the largest size that
# returns 200 with comfortable margin (aim for <20 s, not <30 s).
#
# Usage:
#   set -a; source .env; set +a
#   ./scripts/probe_window_size.sh uploads/<doc_id>/stage2_cleaned.txt

set -uo pipefail
: "${LLM_BASE_URL:?}"; : "${LLM_API_KEY:?}"; : "${LLM_MODEL:?}"
SRC="${1:?usage: probe_window_size.sh <path-to-stage2_cleaned.txt>}"
[ -f "$SRC" ] || { echo "no such file: $SRC"; exit 1; }

URL="${LLM_BASE_URL%/}/inference/chat/completions"
OFFSET="${OFFSET:-200000}"   # skip front matter; override if you like

for CHARS in 24000 12000 6000 3000 1500; do
  TEXT=$(tail -c +${OFFSET} "$SRC" | head -c "$CHARS" \
         | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read())[1:-1])')
  BODY=$(mktemp)
  cat > "$BODY" <<JSON
{
  "model": "${LLM_MODEL}",
  "messages": [
    {"role":"system","content":"Extract every distinct fact from the documentation window into numbered blocks. Begin your reply with ===1=== and use the fields Type, Name, Content, Summary."},
    {"role":"user","content":"${TEXT}"}
  ],
  "max_tokens": ${LLM_MAX_OUTPUT_TOKENS:-6000},
  "stream": false,
  "reasoning_effort": "${LLM_THINKING:-low}"
}
JSON
  printf "%-7s chars  " "$CHARS"
  RESP=$(curl -sS -X POST "$URL" \
    -H "Authorization: Bearer ${LLM_API_KEY}" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "Expect:" \
    -H "User-Agent: ${LLM_USER_AGENT:-ragpipeline/1.0}" \
    --http1.1 --connect-timeout 15 --max-time 120 \
    -d "@${BODY}" \
    -w '\n__M__%{http_code}__%{time_total}')
  rm -f "$BODY"
  CODE=$(echo "$RESP" | tail -1 | cut -d_ -f5)
  SECS=$(echo "$RESP" | tail -1 | awk -F'__' '{print $4}')
  TOKS=$(echo "$RESP" | python3 -c '
import sys,json,re
raw=sys.stdin.read().rsplit("\n__M__",1)[0]
try:
    d=json.loads(raw); u=d.get("usage",{})
    c=(d["choices"][0]["message"]["content"] or "")
    print(f"completion={u.get(\"completion_tokens\")} content_chars={len(c)} finish={d[\"choices\"][0].get(\"finish_reason\")}")
except Exception:
    print("(no parseable body)")' 2>/dev/null)
  printf "http=%s  %6.1fs  %s\n" "${CODE:-?}" "${SECS:-0}" "$TOKS"
done

echo
echo "Pick the largest size returning http=200 in well under 30 s."
echo "Then set:  LLM_INPUT_WINDOW_TOKENS = <chars> / 3     (chars-per-token = 3.0)"
