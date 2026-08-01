#!/usr/bin/env bash
# Ground-truth probe for the AIM endpoint.
#
# Run this BEFORE tuning anything else. It prints the real HTTP status and wall
# time for one streamed and one non-streamed request, which is the single fact
# the old pipeline could not observe (it only knew "the body starts with '<'").
#
#   HTTP 403 → genuine WAF deny        → headers/UA/body-size problem
#   HTTP 429 → rate limit              → lower LLM_CONCURRENCY
#   HTTP 504 → gateway idle timeout    → keep LLM_STREAM=true, lower LLM_MAX_OUTPUT_TOKENS
#   HTTP 400 → rejected parameter      → read the body, it names the bad field
#
# Usage:  set -a; source .env; set +a; ./scripts/probe_aim.sh

set -uo pipefail
: "${LLM_BASE_URL:?set LLM_BASE_URL}"
: "${LLM_API_KEY:?set LLM_API_KEY}"
: "${LLM_MODEL:?set LLM_MODEL}"

URL="${LLM_BASE_URL%/}/inference/chat/completions"
PROMPT="${1:-Reply with the single word OK.}"

probe () {
  local label="$1" stream="$2" max_tokens="$3"
  echo "── ${label} (stream=${stream}, max_tokens=${max_tokens}) ─────────────"
  local body
  body=$(mktemp)
  cat > "$body" <<JSON
{
  "model": "${LLM_MODEL}",
  "messages": [
    {"role": "system", "content": "You are terse."},
    {"role": "user",   "content": "${PROMPT}"}
  ],
  "max_tokens": ${max_tokens},
  "stream": ${stream},
  "reasoning_effort": "low"
}
JSON
  curl -sS -N -X POST "$URL" \
    -H "Authorization: Bearer ${LLM_API_KEY}" \
    -H "Content-Type: application/json" \
    -H "Accept: $([ "$stream" = true ] && echo text/event-stream || echo application/json)" \
    -H "Expect:" \
    -H "User-Agent: ${LLM_USER_AGENT:-ragpipeline/1.0}" \
    --compressed \
    --connect-timeout 15 \
    --max-time "${LLM_TIMEOUT:-300}" \
    -d "@${body}" \
    -w '\n>>> http_code=%{http_code}  time_total=%{time_total}s  size=%{size_download}B\n' \
    | tail -c 1200
  rm -f "$body"
  echo
}

probe "streamed, small budget"      true  256
probe "non-streamed, small budget"  false 256
probe "non-streamed, LARGE budget"  false "${LLM_MAX_OUTPUT_TOKENS:-6000}"
