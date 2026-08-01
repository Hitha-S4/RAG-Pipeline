from __future__ import annotations

import asyncio
import json
import logging
import os
import random
import subprocess
import tempfile
import time
from dataclasses import dataclass

logger = logging.getLogger(__name__)


# ── Error sentinels ───────────────────────────────────────────────────────────

class _PermanentError(RuntimeError):
    """Endpoint returned an unrecoverable error (401/403, bad model name).

    Must not be retried — it will never succeed within this run.
    """
    pass


class _TransientError(RuntimeError):
    """Endpoint returned a retryable error (429, 5xx, timeout, truncated SSE)."""

    def __init__(self, message: str, status: int = 0):
        super().__init__(message)
        self.status = status


# ── IBM AIM provider ──────────────────────────────────────────────────────────

# Default total context window (tokens) when settings don't supply one.
_DEFAULT_CONTEXT = 131_072

# Hard ceiling on max_tokens sent in any single request.  Watsonx enforces a
# per-request new-token limit of 100,000 regardless of the model's total context
# window.  Above this: "The number of new tokens N exceeds the limit of 100000".
_MAX_NEW_TOKENS_HARD_CAP = 100_000

# Safety headroom subtracted from the computed output budget (tokenizer
# overhead, message framing, estimation error).
_CONTEXT_SAFETY = 1_000

# Chars-per-token for estimating input size from raw prompt length.  Technical
# PDF text is denser than average English (~3.5 c/t); 3.0 is conservative so we
# never UNDER-estimate input tokens.
_EST_CHARS_PER_TOKEN = 3.0

# Sentinel curl writes after the body so we can recover the HTTP status even
# when the body itself is HTML or a truncated SSE stream.
_WRITE_OUT = "\n__HTTP__%{http_code}__%{time_total}"
_WRITE_OUT_MARKER = "\n__HTTP__"

# Abort a batch if this many opening requests fail without a single success.
_FAILFAST_AFTER = 20

# Max number of raw failed responses written to disk per process.
_MAX_RAW_DUMPS = 5

# Responses shorter than this are almost certainly degenerate (a template
# fragment, an ellipsis, a refusal) rather than real extraction output. They
# succeed at the transport layer, so nothing else flags them.
_SUSPICIOUS_CHARS = 50


@dataclass
class _SSEResult:
    """Everything the caller needs to judge whether a stream was usable."""
    text: str
    reasoning_chars: int
    finish_reason: str | None
    saw_done: bool
    usage: dict | None
    frames: int

    @property
    def complete(self) -> bool:
        """A [DONE] sentinel OR a finish_reason both mean the model stopped
        deliberately.  [DONE] is optional in SSE — do not require it."""
        return self.saw_done or self.finish_reason is not None


# Models that use the OpenAI/harmony `reasoning_effort` parameter rather than
# the Anthropic-style `thinking` block.  Matched as substrings of the model id.
_REASONING_EFFORT_MODELS = ("gpt-oss", "gpt-4", "gpt-5", "o1", "o3", "o4")


class _LLMProvider:
    """
    Chat-completions provider — uses /usr/bin/curl subprocess to avoid CDN
    TLS-fingerprint blocking that affects Python HTTP clients.
    Requests run concurrently via asyncio + ThreadPoolExecutor, bounded by a
    worker pool of size `concurrency`.
    """

    # Anthropic-style thinking budgets (granite / claude-family endpoints).
    _THINKING_BUDGETS: dict[str, int] = {
        "low":    1_024,
        "medium": 5_000,
        "high":  10_000,
    }

    # Valid values for OpenAI-style reasoning_effort.
    _REASONING_EFFORTS = ("low", "medium", "high")

    # ── Status-aware back-off ────────────────────────────────────────────────
    # The old fixed ladder (45/60/90 s) assumed every failure was a sustained
    # Akamai block.  In practice the dominant failure on gpt-oss is a gateway
    # timeout (502/503/504) caused by a long non-streamed generation — waiting
    # 90 s for that accomplishes nothing except turning a 40-minute run into a
    # multi-day one.  Delays are now chosen by what actually went wrong.
    #
    #   429 (rate limit)      → long, escalating: the limiter needs real time
    #   403 (WAF deny)        → permanent, no retry at all
    #   502/503/504 (gateway) → short: reconnect promptly
    #   000 (curl timeout)    → short-medium: usually our own --max-time
    #   other                 → moderate default
    _BACKOFF_RATE_LIMIT = (0, 30, 60, 120)
    # A gateway DEADLINE (as opposed to a transient blip) is deterministic:
    # the same window will take the same too-long time on every attempt. Four
    # attempts at ~30 s each plus sleeps burns ~150 s per window to learn what
    # attempt 2 already told us. Capped at 2 attempts via _MAX_ATTEMPTS_504.
    _BACKOFF_GATEWAY    = (0,  3,  8,  20)
    _BACKOFF_TIMEOUT    = (0,  5, 15,  30)
    _BACKOFF_DEFAULT    = (0, 10, 25,  50)

    _MAX_ATTEMPTS = 4        # 1 initial + 3 retries
    _MAX_ATTEMPTS_504 = 2    # gateway deadlines are deterministic — fail fast

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str,
        max_output_tokens: int,
        timeout: int,
        concurrency: int,
        total_context: int = _DEFAULT_CONTEXT,
        thinking_effort: str = "",
        stream: bool = True,
        user_agent: str = "",
        require_done: bool = True,
        debug_raw_dir: str = "",
        min_expected_chars: int = _SUSPICIOUS_CHARS,
        http_version: str = "1.1",
    ):
        # AIM endpoints expose /inference/chat/completions under the host root.
        # OpenAI-compatible endpoints (Ollama, vLLM, …) use /v1/chat/completions
        # and the caller passes the base_url as e.g. http://localhost:11434/v1 —
        # those already contain the path; appending the AIM suffix gives a 404.
        _base = base_url.rstrip("/")
        if _base.endswith("/chat/completions"):
            self._url = _base
        elif _base.endswith(("/v1", "/inference")):
            self._url = _base + "/chat/completions"
        else:
            # IBM AIM host root — preserve original behaviour.
            self._url = _base + "/inference/chat/completions"
        self._api_key           = api_key
        self._model             = model
        self._max_output_tokens = max_output_tokens
        self._total_context     = total_context
        self._timeout           = timeout
        self._concurrency       = max(1, concurrency)
        self._thinking_effort   = thinking_effort.lower().strip()
        self._stream            = stream
        self._user_agent        = user_agent or "ragpipeline/1.0"
        self._require_done      = require_done
        self._debug_raw_dir     = debug_raw_dir
        self._min_expected      = min_expected_chars
        self._http_version      = http_version
        self._raw_dumps         = 0
        self._had_success       = False
        self._success_count     = 0
        self._dead              = False   # set True on first permanent error
        self._uses_reasoning_effort = any(
            tag in model.lower() for tag in _REASONING_EFFORT_MODELS
        )
        logger.info(
            "LLMProvider ready  url=%s  model=%s  concurrency=%d  "
            "max_output_tokens=%d  context=%d  reasoning=%s (%s)  stream=%s",
            self._url, model, self._concurrency, max_output_tokens, total_context,
            self._thinking_effort or "disabled",
            "reasoning_effort" if self._uses_reasoning_effort else "thinking",
            self._stream,
        )

    # ── Token budgeting ──────────────────────────────────────────────────────

    def _safe_max_tokens(self, body_chars: int) -> int:
        """Compute a safe max_tokens for this specific request.

        Constraints (most restrictive wins):
          1. input + output + safety <= total_ctx   context overflow guard
          2. output <= _MAX_NEW_TOKENS_HARD_CAP     Watsonx per-request limit

        NOTE: this only ever CAPS `self._max_output_tokens`; it never raises it.
        If you set LLM_MAX_OUTPUT_TOKENS=16000 you really are telling a 120B
        model it may generate 16k tokens (~4–9 min of decode).  Set that value
        to what extraction actually needs — check `usage.completion_tokens` on a
        successful run — not to the theoretical ceiling.
        """
        estimated_input = int(body_chars / _EST_CHARS_PER_TOKEN)
        context_budget  = self._total_context - estimated_input - _CONTEXT_SAFETY
        capped = min(self._max_output_tokens,
                     _MAX_NEW_TOKENS_HARD_CAP,
                     max(context_budget, 256))
        if capped < self._max_output_tokens:
            logger.debug(
                "_safe_max_tokens: body=%d chars → est_input=%d tok → capped=%d "
                "(context_budget=%d)",
                body_chars, estimated_input, capped, context_budget,
            )
        return capped

    # ── Payload construction ─────────────────────────────────────────────────

    def _build_payload(self, system: str, user: str) -> dict:
        messages = [
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ]
        prompt_chars = sum(len(m["content"]) for m in messages)
        safe_tokens  = self._safe_max_tokens(prompt_chars)

        payload: dict = {
            "model": self._model,
            "messages": messages,
            "max_tokens": safe_tokens,
        }
        if self._stream:
            payload["stream"] = True

        # Reasoning parameter — SHAPE DEPENDS ON THE MODEL FAMILY.
        if self._thinking_effort:
            if self._uses_reasoning_effort:
                if self._thinking_effort in self._REASONING_EFFORTS:
                    payload["reasoning_effort"] = self._thinking_effort
            elif self._thinking_effort in self._THINKING_BUDGETS:
                payload["thinking"] = {
                    "type": "enabled",
                    "budget_tokens": self._THINKING_BUDGETS[self._thinking_effort],
                }

        logger.debug(
            "AIM request: prompt=%d chars (~%d tok)  max_tokens=%d  stream=%s",
            prompt_chars, int(prompt_chars / _EST_CHARS_PER_TOKEN),
            safe_tokens, self._stream,
        )
        return payload

    # ── Response parsing ─────────────────────────────────────────────────────

    @staticmethod
    def _split_status(raw: str) -> tuple[str, int, float]:
        """Split curl output into (body, http_status, seconds).

        Returns status 0 when the marker is missing (curl died before writing).
        """
        idx = raw.rfind(_WRITE_OUT_MARKER)
        if idx == -1:
            return raw, 0, 0.0
        body = raw[:idx]
        tail = raw[idx + len(_WRITE_OUT_MARKER):]
        parts = tail.strip().split("__")
        try:
            status = int(parts[0])
        except (ValueError, IndexError):
            status = 0
        try:
            elapsed = float(parts[1])
        except (ValueError, IndexError):
            elapsed = 0.0
        return body, status, elapsed

    @staticmethod
    def _parse_sse(body: str) -> "_SSEResult":
        """Accumulate content deltas from an OpenAI-style SSE stream.

        Returns an _SSEResult rather than a bare string, because the CALLER —
        not this parser — must decide whether an unterminated stream is fatal.

        WHY THIS CHANGED
        ────────────────
        The first version required a literal `data: [DONE]` frame and raised
        "truncated" without it.  That was wrong.  Plenty of OpenAI-compatible
        gateways (vLLM behind watsonx among them) close the stream immediately
        after the final chunk — the one carrying `finish_reason` — and never
        emit the `[DONE]` sentinel, which is optional in the SSE spec and only
        conventional in OpenAI's own implementation.  The result was a complete,
        perfectly good response being thrown away and retried four times on
        every one of 389 windows.

        A stream is now considered COMPLETE if either:
          * a `[DONE]` sentinel arrived, OR
          * the last chunk carried a non-null `finish_reason`.
        Only when neither is present is it genuinely suspect.
        """
        stripped = body.lstrip()

        # Gateway ignored stream:true and sent a normal completion object.
        if stripped.startswith("{"):
            data = json.loads(stripped)
            if "choices" not in data:
                raise ValueError(f"no choices in non-stream response: {stripped[:300]}")
            choice = data["choices"][0]
            msg = choice.get("message") or {}
            return _SSEResult(
                text=(msg.get("content") or "").strip(),
                reasoning_chars=len(msg.get("reasoning_content") or ""),
                finish_reason=choice.get("finish_reason"),
                saw_done=True,
                usage=data.get("usage"),
                frames=1,
            )

        parts: list[str] = []
        reasoning_chars = 0
        finish_reason: str | None = None
        usage: dict | None = None
        saw_done = False
        frames = 0

        for line in body.splitlines():
            line = line.strip()
            if not line or not line.startswith("data:"):
                continue
            chunk = line[5:].strip()
            if chunk == "[DONE]":
                saw_done = True
                break
            try:
                obj = json.loads(chunk)
            except json.JSONDecodeError:
                continue   # partial frame at the tail of a cut stream
            frames += 1
            if obj.get("usage"):
                usage = obj["usage"]
            choices = obj.get("choices") or []
            if not choices:
                continue
            choice = choices[0]
            if choice.get("finish_reason"):
                finish_reason = choice["finish_reason"]
            delta = choice.get("delta") or {}
            # `content` is the visible answer.  `reasoning_content` (gpt-oss
            # harmony analysis channel) is chain-of-thought — counted for
            # diagnostics but deliberately NOT accumulated into the result.
            reasoning_chars += len(delta.get("reasoning_content") or "")
            piece = delta.get("content")
            if piece:
                parts.append(piece)

        return _SSEResult(
            text="".join(parts).strip(),
            reasoning_chars=reasoning_chars,
            finish_reason=finish_reason,
            saw_done=saw_done,
            usage=usage,
            frames=frames,
        )

    def _dump_raw(self, body: str, status: int, elapsed: float) -> str:
        """Persist a failed raw response so the failure can be read, not guessed.

        Capped at _MAX_RAW_DUMPS per process — enough to diagnose, not enough to
        fill the disk on a 389-window run.
        """
        if not self._debug_raw_dir or self._raw_dumps >= _MAX_RAW_DUMPS:
            return ""
        try:
            os.makedirs(self._debug_raw_dir, exist_ok=True)
            path = os.path.join(
                self._debug_raw_dir,
                f"llm_raw_{int(time.time())}_{self._raw_dumps}_http{status}.txt",
            )
            with open(path, "w", encoding="utf-8", errors="replace") as fh:
                fh.write(f"# status={status} elapsed={elapsed:.2f}s bytes={len(body)}\n")
                fh.write(f"# model={self._model} stream={self._stream}\n\n")
                fh.write(body)
            self._raw_dumps += 1
            return path
        except OSError as exc:
            logger.debug("_dump_raw failed: %s", exc)
            return ""

    # ── Back-off selection ───────────────────────────────────────────────────

    def _backoff_for(self, status: int, attempt: int) -> float:
        if status in (429, 403):
            table = self._BACKOFF_RATE_LIMIT
        elif status in (502, 503, 504):
            table = self._BACKOFF_GATEWAY
        elif status == 0:
            table = self._BACKOFF_TIMEOUT
        else:
            table = self._BACKOFF_DEFAULT
        base   = table[min(attempt, len(table) - 1)]
        jitter = base * 0.25 * (2 * random.random() - 1)   # ±25 %
        return max(0.0, base + jitter)

    # ── The call itself ──────────────────────────────────────────────────────

    def _curl_complete(self, system: str, user: str) -> str:
        """Synchronous curl call with status-aware, jittered back-off."""
        if self._dead:
            raise _PermanentError("AIM provider is disabled for this run")

        body = json.dumps(self._build_payload(system, user))

        last_exc: Exception = RuntimeError("no attempts made")
        for attempt in range(self._MAX_ATTEMPTS):
            # Stop early on a repeated gateway deadline: it is a property of the
            # request size, not of luck, so further attempts cost 30 s each and
            # cannot succeed.
            if (attempt >= self._MAX_ATTEMPTS_504
                    and getattr(last_exc, "status", 0) in (502, 503, 504)):
                logger.warning(
                    "_curl_complete: giving up after %d gateway timeouts — "
                    "the request is too large to finish inside the deadline",
                    attempt,
                )
                break

            if attempt:
                delay = self._backoff_for(getattr(last_exc, "status", 0), attempt)
                logger.info(
                    "_curl_complete: retry %d/%d in %.1fs (last=%s)",
                    attempt + 1, self._MAX_ATTEMPTS, delay, last_exc,
                )
                time.sleep(delay)

            with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
                tmp.write(body)
                tmp_path = tmp.name
            try:
                cmd = [
                    "/usr/bin/curl", "-sS", "-X", "POST", self._url,
                    "-H", f"Authorization: Bearer {self._api_key}",
                    "-H", "Content-Type: application/json",
                    "-H", f"Accept: {'text/event-stream' if self._stream else 'application/json'}",
                    # Suppress curl's automatic Expect: 100-continue on bodies
                    # >1 KB — some proxies stall a full second waiting on it.
                    "-H", "Expect:",
                    "-H", f"User-Agent: {self._user_agent}",
                    "-w", _WRITE_OUT,
                    "-d", f"@{tmp_path}",
                    "--connect-timeout", "15",
                    "--max-time", str(self._timeout),
                ]
                # HTTP/2 multiplexing is a common source of mid-stream
                # RST_STREAM behind CDN/ingress layers; forcing 1.1 gives one
                # TCP connection per request with no stream-level reset path.
                if self._http_version == "1.1":
                    cmd.append("--http1.1")
                elif self._http_version == "2":
                    cmd.append("--http2")
                # NOTE: --compressed was REMOVED. gzip over a Server-Sent-Events
                # stream buffers at flush boundaries and interacts badly with
                # incremental delivery. SSE is small; the compression saves
                # nothing worth this risk.
                if self._stream:
                    cmd.insert(1, "-N")   # unbuffered — keeps the socket alive
                result = subprocess.run(
                    cmd, capture_output=True, text=True,
                    timeout=self._timeout + 15,
                )
            except subprocess.TimeoutExpired:
                last_exc = _TransientError("curl subprocess timed out", 0)
                logger.warning("_curl_complete attempt %d/%d: subprocess timeout",
                               attempt + 1, self._MAX_ATTEMPTS)
                continue
            finally:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

            raw = result.stdout
            body_text, status, elapsed = self._split_status(raw)
            body_text = body_text.strip()

            # curl itself failed (DNS, TLS, mid-stream abort, HTTP/2 reset).
            #
            # THIS USED TO READ `if returncode != 0 AND NOT body_text`, which
            # silently accepted every partial transfer: curl exits 18/56/92,
            # hands back the bytes it managed to read, and the old condition
            # evaluated False because body_text was non-empty. That is exactly
            # what a stream aborted after one frame looks like. The curl exit
            # code naming the real fault was discarded on every one of 389
            # windows. A non-zero exit is now ALWAYS a failure, and stderr is
            # always logged.
            #   18 CURLE_PARTIAL_FILE       — transfer ended early
            #   56 CURLE_RECV_ERROR         — failure receiving network data
            #   92 CURLE_HTTP2_STREAM       — HTTP/2 stream not closed cleanly
            #   28 CURLE_OPERATION_TIMEDOUT — --max-time hit
            if result.returncode != 0:
                last_exc = _TransientError(
                    f"curl rc={result.returncode} after {elapsed:.1f}s "
                    f"({len(body_text)} bytes received): "
                    f"{result.stderr.strip()[:300] or '(no stderr)'}",
                    status,
                )
                logger.warning("_curl_complete attempt %d/%d: %s",
                               attempt + 1, self._MAX_ATTEMPTS, last_exc)
                continue

            # ── Status classification ────────────────────────────────────────
            if status == 401:
                snippet = body_text[:200].replace("\n", " ")
                raise _PermanentError(
                    f"HTTP 401 — credentials rejected (not retryable). body={snippet}"
                )
            if status == 403:
                # 403 is NOT automatically permanent. If earlier requests in this
                # run succeeded, the credentials are fine and this is a rate or
                # abuse response to a concurrency burst — exactly what happens
                # when LLM_CONCURRENCY is raised. Treating it as permanent set
                # _dead and silently returned "" for every remaining window:
                # 6,450 empty responses, 0 chunks, and a "success" at the end.
                snippet = body_text[:200].replace("\n", " ")
                if self._had_success:
                    last_exc = _TransientError(
                        f"HTTP 403 after {self._success_count} successful requests "
                        f"— treating as a concurrency/rate response, not auth. "
                        f"Lower LLM_CONCURRENCY if it persists. body={snippet}",
                        403,
                    )
                    logger.warning("_curl_complete attempt %d/%d: %s",
                                   attempt + 1, self._MAX_ATTEMPTS, last_exc)
                    continue
                raise _PermanentError(
                    f"HTTP 403 with no prior success — auth or WAF deny. "
                    f"body={snippet}"
                )
            if status == 413:
                raise _PermanentError(
                    f"HTTP 413 — request body too large ({len(body)} bytes). "
                    "Lower LLM_INPUT_WINDOW_TOKENS / LLM_MAX_ENTRIES."
                )
            if status == 400:
                # Almost always a rejected parameter (e.g. sending `thinking` to
                # a model that wants `reasoning_effort`).  Surfacing the body is
                # the whole point — do not bury it behind a generic retry.
                raise _PermanentError(f"HTTP 400 — bad request: {body_text[:400]}")
            if status == 429:
                last_exc = _TransientError("HTTP 429 — rate limited", 429)
                logger.warning("_curl_complete attempt %d/%d: 429 rate limited (%.1fs)",
                               attempt + 1, self._MAX_ATTEMPTS, elapsed)
                continue
            if status in (502, 503, 504):
                last_exc = _TransientError(
                    f"HTTP {status} — gateway deadline hit after {elapsed:.1f}s. "
                    "This gateway kills non-streamed requests at ~30 s and its "
                    "SSE mode ends after the first delta, so the only lever is "
                    "less work per request: lower LLM_INPUT_WINDOW_TOKENS (see "
                    "scripts/probe_window_size.sh) or switch LLM_MODEL to "
                    "granite-4-h-small, which decodes fast enough to finish.",
                    status,
                )
                logger.warning("_curl_complete attempt %d/%d: HTTP %d after %.1fs",
                               attempt + 1, self._MAX_ATTEMPTS, status, elapsed)
                continue
            if status == 0:
                last_exc = _TransientError(
                    f"no HTTP status — connection dropped after {elapsed:.1f}s", 0
                )
                logger.warning("_curl_complete attempt %d/%d: connection dropped",
                               attempt + 1, self._MAX_ATTEMPTS)
                continue
            if status >= 400:
                last_exc = _TransientError(
                    f"HTTP {status}: {body_text[:300]}", status
                )
                logger.warning("_curl_complete attempt %d/%d: HTTP %d",
                               attempt + 1, self._MAX_ATTEMPTS, status)
                continue

            if not body_text:
                last_exc = _TransientError(f"HTTP {status} but empty body", status)
                logger.warning("_curl_complete attempt %d/%d: empty body",
                               attempt + 1, self._MAX_ATTEMPTS)
                continue

            # HTML with a 2xx — rare, but means something in the path replaced
            # the response.  Retryable, with the real status now recorded.
            if body_text.lstrip().startswith("<"):
                last_exc = _TransientError(
                    f"HTTP {status} returned HTML: {body_text[:120]}", status
                )
                logger.warning("_curl_complete attempt %d/%d: HTML body on HTTP %d",
                               attempt + 1, self._MAX_ATTEMPTS, status)
                continue

            # ── Success path ─────────────────────────────────────────────────
            try:
                if self._stream:
                    res = self._parse_sse(body_text)
                else:
                    data = json.loads(body_text)
                    if "error" in data or "choices" not in data:
                        raise ValueError(f"error response: {body_text[:300]}")
                    choice = data["choices"][0]
                    msg = choice.get("message") or {}
                    res = _SSEResult(
                        text=(msg.get("content") or "").strip(),
                        reasoning_chars=len(msg.get("reasoning_content") or ""),
                        finish_reason=choice.get("finish_reason"),
                        saw_done=True,
                        usage=data.get("usage"),
                        frames=1,
                    )
            except Exception as exc:
                dump = self._dump_raw(body_text, status, elapsed)
                last_exc = _TransientError(f"unparseable response: {exc}", status)
                logger.warning(
                    "_curl_complete attempt %d/%d: %s  bytes=%d  %.1fs%s",
                    attempt + 1, self._MAX_ATTEMPTS, last_exc, len(body_text),
                    elapsed, f"  raw={dump}" if dump else "",
                )
                continue

            # ── Judge the parsed stream ──────────────────────────────────────
            # A truncation check belongs HERE, with all the evidence, not inside
            # the parser.  Three distinct failure shapes are separated:
            if not res.text:
                if res.reasoning_chars:
                    # Model spent its whole budget in the analysis channel and
                    # never opened the final channel.  Almost always max_tokens
                    # being consumed by reasoning.
                    dump = self._dump_raw(body_text, status, elapsed)
                    last_exc = _TransientError(
                        f"model emitted {res.reasoning_chars} chars of reasoning "
                        f"but no content (finish={res.finish_reason}). Lower "
                        f"LLM_THINKING or raise LLM_MAX_OUTPUT_TOKENS."
                        + (f" raw={dump}" if dump else ""),
                        status,
                    )
                else:
                    dump = self._dump_raw(body_text, status, elapsed)
                    last_exc = _TransientError(
                        f"empty content in {res.frames} SSE frame(s), "
                        f"finish={res.finish_reason}"
                        + (f" raw={dump}" if dump else ""),
                        status,
                    )
                logger.warning("_curl_complete attempt %d/%d: %s",
                               attempt + 1, self._MAX_ATTEMPTS, last_exc)
                continue

            if res.finish_reason == "length":
                # Not an error — the response is real, just cut at the budget.
                # Callers parsing structured output will likely reject it, so
                # make the cause loud instead of letting it look like a WAF fault.
                logger.warning(
                    "LLM output hit max_tokens (finish_reason=length, %d chars). "
                    "Raise LLM_MAX_OUTPUT_TOKENS.", len(res.text),
                )

            # An incomplete stream is TRUNCATION, not a gateway convention.
            #
            # I previously defaulted this off, reasoning that [DONE] is an
            # OpenAI convention some gateways omit. That reasoning was wrong
            # here: finish_reason was ALSO absent, which no complete response
            # ever does. Accepting these converted one loud failure into 389
            # silent ones. Default is back on.
            if not res.complete and self._require_done:
                # Only reachable when LLM_STREAM_REQUIRE_DONE=true. Off by
                # default: many gateways never send [DONE].
                dump = self._dump_raw(body_text, status, elapsed)
                last_exc = _TransientError(
                    f"stream ended with no [DONE] and no finish_reason "
                    f"({len(res.text)} chars, {res.frames} frames)"
                    + (f" raw={dump}" if dump else ""),
                    status,
                )
                logger.warning("_curl_complete attempt %d/%d: %s",
                               attempt + 1, self._MAX_ATTEMPTS, last_exc)
                continue

            if not res.complete:
                logger.debug(
                    "stream had no [DONE]/finish_reason but returned %d chars — "
                    "accepting (gateway convention)", len(res.text),
                )

            # ── Degenerate-but-successful response ───────────────────────────
            # HTTP 200, finish_reason=stop, valid SSE — and three characters of
            # content. Nothing downstream will flag this: the batch counts it as
            # a success and the window parses to zero blocks. Surface it here.
            if 0 < len(res.text) < self._min_expected:
                dump = self._dump_raw(body_text, status, elapsed)
                logger.warning(
                    "SUSPICIOUSLY SHORT RESPONSE  %d chars  finish=%s  "
                    "reasoning_chars=%d  content=%r%s",
                    len(res.text), res.finish_reason, res.reasoning_chars,
                    res.text[:120], f"  raw={dump}" if dump else "",
                )

            if res.usage:
                # THIS is the number to tune LLM_MAX_OUTPUT_TOKENS against.
                logger.info(
                    "LLM usage  prompt=%s  completion=%s  total=%s",
                    res.usage.get("prompt_tokens"),
                    res.usage.get("completion_tokens"),
                    res.usage.get("total_tokens"),
                )

            self._had_success = True
            self._success_count += 1
            logger.debug(
                "_curl_complete ok  status=%d  %.1fs  chars=%d  frames=%d  "
                "reasoning_chars=%d  finish=%s",
                status, elapsed, len(res.text), res.frames,
                res.reasoning_chars, res.finish_reason,
            )
            return res.text

        raise last_exc

    # ── Async orchestration ──────────────────────────────────────────────────

    async def _complete_one(
        self,
        system: str,
        user: str,
        request_label: str,
    ) -> str:
        loop = asyncio.get_running_loop()
        logger.info("LLM request start  %s", request_label)
        started = time.monotonic()
        try:
            result = await loop.run_in_executor(None, self._curl_complete, system, user)
        except Exception as exc:
            logger.warning("LLM request failed  %s  after=%.1fs  error=%s",
                           request_label, time.monotonic() - started, exc)
            raise
        logger.info("LLM request done  %s  %.1fs  resp_chars=%d",
                    request_label, time.monotonic() - started, len(result))
        return result

    async def complete_many(
        self,
        requests: list[tuple[str, str]],
        inter_batch_delay: float = 0.0,
        concurrency: int | None = None,
        on_result: "Callable[[int, str], None] | None" = None,
    ) -> list[str]:
        """Run all (system, user) pairs through a worker pool; results in order.

        `concurrency` workers pull from a shared index queue, so a slow request
        never idles the other slots (the old fixed-batch gather did exactly
        that).  `inter_batch_delay` is applied as a small per-request pause
        inside each worker to pace the endpoint.

        Pass ``concurrency=1`` for a fully sequential retry pass.
        Failures become "" in the output so callers keep positional alignment.

        ``on_result(idx, raw)`` — optional callback invoked immediately after
        each request completes (inside the worker, before the next request is
        pulled).  ``raw`` is the response string ("" on failure).  Use this to
        write incremental output without waiting for the whole batch.
        """
        total = len(requests)
        if not total:
            return []

        effective = concurrency if concurrency is not None else self._concurrency
        effective = max(1, min(effective, total))
        results: list[object] = [None] * total
        queue: asyncio.Queue[int] = asyncio.Queue()
        for i in range(total):
            queue.put_nowait(i)

        logger.info(
            "LLM batch start  requests=%d  concurrency=%d  pace=%.1fs",
            total, effective, inter_batch_delay,
        )
        started = time.monotonic()
        completed = 0
        failures = 0

        async def worker(worker_id: int) -> None:
            nonlocal completed, failures
            while True:
                try:
                    idx = queue.get_nowait()
                except asyncio.QueueEmpty:
                    return
                if self._dead:
                    results[idx] = _PermanentError("provider dead")
                    queue.task_done()
                    continue
                system, user = requests[idx]
                label = f"request={idx + 1}/{total} w{worker_id}"
                try:
                    results[idx] = await self._complete_one(system, user, label)
                except _PermanentError as exc:
                    # Short-circuit the whole run — nothing else will succeed.
                    self._dead = True
                    logger.error(
                        "AIM PERMANENT ERROR — every remaining window will return "
                        "EMPTY and the pipeline will write 0 chunks. Cause: %s", exc,
                    )
                    results[idx] = exc
                except Exception as exc:
                    results[idx] = exc
                else:
                    # Fire the per-result callback immediately so callers can
                    # write incremental output without waiting for the whole batch.
                    if on_result is not None:
                        raw = results[idx] if isinstance(results[idx], str) else ""
                        try:
                            on_result(idx, raw)
                        except Exception as cb_exc:  # noqa: BLE001
                            logger.warning("on_result callback raised: %s", cb_exc)
                finally:
                    completed += 1
                    failures = sum(1 for r in results if isinstance(r, Exception))
                    # Nothing is worth 6,450 no-op iterations. If the opening
                    # requests fail wholesale, the configuration is wrong; stop
                    # and say so rather than "succeeding" with an empty result.
                    if (not self._dead
                            and completed >= _FAILFAST_AFTER
                            and failures == completed
                            and total > _FAILFAST_AFTER):
                        self._dead = True
                        logger.error(
                            "ABORTING BATCH — first %d/%d requests ALL failed. "
                            "Check LLM_CONCURRENCY, the model name, and "
                            "./debug/llm_raw/. Not burning the remaining %d.",
                            completed, total, total - completed,
                        )
                    if completed % 10 == 0 or completed == total:
                        logger.info(
                            "LLM progress  %d/%d  failures=%d  elapsed=%.0fs",
                            completed, total, failures, time.monotonic() - started,
                        )
                    queue.task_done()
                if inter_batch_delay > 0:
                    await asyncio.sleep(inter_batch_delay)

        await asyncio.gather(*(worker(w) for w in range(effective)))

        output: list[str] = ["" if isinstance(r, (Exception, type(None))) else r  # type: ignore[misc]
                             for r in results]
        logger.info(
            "LLM batch done  requests=%d  succeeded=%d  failed=%d  elapsed=%.0fs",
            total,
            sum(1 for r in output if r),
            sum(1 for r in output if not r),
            time.monotonic() - started,
        )
        return output

    def complete(self, system: str, user: str) -> str:
        """Synchronous single-call wrapper (used by generate_doc_overview)."""
        return asyncio.run(self.complete_many([(system, user)]))[0]