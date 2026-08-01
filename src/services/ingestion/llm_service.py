"""
LLM service — fast, token-efficient notes for MD generation.

PROVIDER
────────
  IBM AIM /inference/chat/completions via curl subprocess.
  No Python HTTP client, no WAF fingerprinting issues.

CONCURRENCY & BATCHING
──────────────────────
- Each ingestion run may have up to 6 categories × N batches.
- Batches within a single generate_notes() call are fired with asyncio.gather()
  so they run concurrently against the endpoint (bounded by LLM_CONCURRENCY).
- MAX_ENTRIES controls chunks per batch; increase it if the model's context
  window supports larger payloads.

SETTINGS (env vars / .env)
──────────────────────────
  LLM_ENABLED=true
  LLM_BASE_URL=https://...
  LLM_API_KEY=sk-...
  LLM_MODEL=<model-path>
  LLM_MAX_TOKENS=4000
  LLM_TIMEOUT=60
  LLM_CONCURRENCY=4             (max parallel requests)
  LLM_MAX_ENTRIES=15            (chunks per batch)
"""
from __future__ import annotations

import asyncio
import logging
from typing import Optional

from src.services.ingestion.prompts import (
    OVERVIEW_SYSTEM      as _OVERVIEW_SYSTEM,
    SYSTEM_NOTES_PROMPTS as _SYSTEM,
)
from src.utils.llm_helpers import _is_placeholder, _make_snippet, _parse_blocks
from src.utils.providers import _LLMProvider

logger = logging.getLogger(__name__)


# ── Public service ────────────────────────────────────────────────────────────

class LLMService:
    """
    Issues batched, concurrent AIM calls per category (≤6 total per ingestion run).
    Each category's chunks are split into batches of _MAX_ENTRIES; all batches for
    that category are fired in parallel via asyncio.gather.
    Fast path: placeholder chunks skip the LLM; static fallback renders them.
    """

    # Max chunks per batch
    _MAX_ENTRIES = 15

    def __init__(self, settings=None):
        if settings is None:
            from src.config.settings import get_settings
            settings = get_settings()
        self._enabled       = getattr(settings, "llm_enabled", False)
        self._max_entries   = getattr(settings, "llm_max_entries", self._MAX_ENTRIES)
        self._request_delay = getattr(settings, "llm_request_delay", 1.0)
        self._provider: Optional[_LLMProvider] = None
        if self._enabled:
            self._provider = _LLMProvider(
                base_url           = settings.llm_base_url,
                api_key            = settings.llm_api_key,
                model              = settings.llm_model,
                max_output_tokens  = getattr(settings, "llm_max_output_tokens", 4000),
                timeout            = settings.llm_timeout,
                concurrency        = getattr(settings, "llm_concurrency", 4),
                total_context      = getattr(settings, "llm_context_window", 131_072),
                thinking_effort    = getattr(settings, "llm_thinking", ""),
                stream             = getattr(settings, "llm_stream", True),
                user_agent         = getattr(settings, "llm_user_agent", "ragpipeline/1.0"),
                require_done       = getattr(settings, "llm_stream_require_done", False),
                debug_raw_dir      = getattr(settings, "llm_debug_raw_dir", "./debug/llm_raw"),
                min_expected_chars = getattr(settings, "llm_debug_min_chars", 50),
                http_version       = getattr(settings, "llm_http_version", "1.1"),
            )
        logger.info(
            "LLMService  enabled=%s  max_entries=%d  request_delay=%.1fs",
            self._enabled, self._max_entries, self._request_delay,
        )

    @property
    def enabled(self) -> bool:
        return self._enabled and self._provider is not None

    def complete_batch(
        self,
        requests: list[tuple[str, str]],
        on_result: "Callable[[int, str], None] | None" = None,
    ) -> list[str]:
        """Fire ALL requests via sub-batched asyncio.run().

        Passes _request_delay to complete_many() so the provider paces
        requests in groups of _concurrency with an inter-batch sleep.
        This prevents AIM rate-limit storms on large extraction runs
        (e.g. 389 windows → without pacing, 8.5% of windows fail).

        The _dead flag is reset at the top of every new batch.  A permanent
        error or fail-fast during one document must not poison subsequent
        documents processed by the same IngestionService instance (which
        reuses this LLMService singleton across calls).

        ``on_result(idx, raw)`` — forwarded to complete_many(); fires
        immediately as each window completes so callers can write incremental
        output without waiting for the entire batch to finish.
        """
        if not self.enabled or not requests:
            return [""] * len(requests)

        # Reset dead flag — each top-level batch is a fresh attempt.
        # Fail-fast from a previous document must not poison subsequent
        # documents processed by the same IngestionService instance (which
        # reuses this LLMService singleton across calls).
        if getattr(self._provider, "_dead", False):
            logger.warning(
                "AIM provider was marked dead from a previous run — resetting for new batch (%d requests)",
                len(requests),
            )
            self._provider._dead = False          # type: ignore[union-attr]
            self._provider._had_success = False   # type: ignore[union-attr]
            self._provider._success_count = 0     # type: ignore[union-attr]

        logger.debug("complete_batch  total=%d  concurrency=%s  delay=%.1fs",
                     len(requests),
                     getattr(self._provider, "_concurrency", "?"),
                     self._request_delay)

        results = asyncio.run(
            self._provider.complete_many(  # type: ignore[union-attr]
                requests,
                inter_batch_delay=self._request_delay,
                on_result=on_result,
            )
        )
        filled = sum(1 for r in results if r)
        logger.info("complete_batch done  total=%d  filled=%d", len(requests), filled)
        return results

    def complete_batch_sequential(self, requests: list[tuple[str, str]]) -> list[str]:
        """Re-run requests one at a time — no concurrency, no burst pressure.

        Intended as a last-resort fallback. Prefer complete_batch_retry()
        for normal retry passes.
        """
        if not self.enabled or not requests:
            return [""] * len(requests)

        if getattr(self._provider, "_dead", False):
            logger.warning("AIM provider dead — skipping %d sequential request(s)", len(requests))
            return [""] * len(requests)

        logger.debug("complete_batch_sequential  total=%d  delay=5s", len(requests))

        results = asyncio.run(
            self._provider.complete_many(  # type: ignore[union-attr]
                requests,
                inter_batch_delay=5.0,
                concurrency=1,
            )
        )
        filled = sum(1 for r in results if r)
        logger.info("complete_batch_sequential done  total=%d  filled=%d", len(requests), filled)
        return results

    def complete_batch_retry(self, requests: list[tuple[str, str]],
                             concurrency: int = 3,
                             delay: float = 3.0) -> list[str]:
        """Retry pass with reduced concurrency (default 3) and a moderate delay.

        Sits between complete_batch() (full concurrency) and
        complete_batch_sequential() (concurrency=1).  Used for all retry
        passes in the extraction pipeline so failed windows get another
        attempt without hammering the endpoint.

        concurrency: parallel slots (default 3; pass 1 for fully sequential)
        delay: seconds between requests within each worker (default 3.0)
        """
        if not self.enabled or not requests:
            return [""] * len(requests)

        if getattr(self._provider, "_dead", False):
            logger.warning(
                "AIM provider was marked dead — resetting for retry batch (%d requests)",
                len(requests),
            )
            self._provider._dead = False          # type: ignore[union-attr]
            self._provider._had_success = False   # type: ignore[union-attr]
            self._provider._success_count = 0     # type: ignore[union-attr]

        logger.debug(
            "complete_batch_retry  total=%d  concurrency=%d  delay=%.1fs",
            len(requests), concurrency, delay,
        )

        results = asyncio.run(
            self._provider.complete_many(  # type: ignore[union-attr]
                requests,
                inter_batch_delay=delay,
                concurrency=concurrency,
            )
        )
        filled = sum(1 for r in results if r)
        logger.info(
            "complete_batch_retry done  total=%d  filled=%d  concurrency=%d",
            len(requests), filled, concurrency,
        )
        return results

    def generate_notes(
        self,
        category: str,
        entries: list[dict],
        context: str = "",
    ) -> list[str]:
        """
        Concurrent batched AIM calls for up to _MAX_ENTRIES non-placeholder chunks
        per batch.  All batches for this category are fired in parallel.
        Returns list[str] parallel to entries; empty string → static fallback.

        context: optional extra text prepended to each user message — used by
                 the personas category to supply PERSONAS_RAW + KNOWLEDGE_RAW
                 content so the model has richer grounding.
        """
        results = [""] * len(entries)
        if not self.enabled or not entries:
            return results

        # Fast path: skip placeholder chunks
        real_idx = [
            i for i, c in enumerate(entries)
            if not _is_placeholder(c.get("content", ""))
        ]
        if not real_idx:
            return results

        system = _SYSTEM.get(category, _SYSTEM["knowledge"])

        # Split real entries into batches of _MAX_ENTRIES
        batches: list[list[int]] = [
            real_idx[start : start + self._max_entries]
            for start in range(0, len(real_idx), self._max_entries)
        ]

        # Build one (system, user_msg) pair per batch
        requests: list[tuple[str, str]] = []
        for batch in batches:
            lines = []
            for seq, i in enumerate(batch, 1):
                lines.append(f"--- Excerpt {seq} ---\n{_make_snippet(entries[i])}")
            excerpts = "\n\n".join(lines)
            if context:
                user_msg = (
                    f"CONTEXT (use for grounding — do not copy verbatim):\n"
                    f"{context[:2000]}\n\n---\n\n{excerpts}"
                )
            else:
                user_msg = excerpts
            requests.append((system, user_msg))

        logger.info(
            "LLM call  cat=%s  batches=%d  real_chunks=%d  total=%d",
            category, len(batches), len(real_idx), len(entries),
        )

        # Fire all batches concurrently (generate_notes batches are already small
        # — _MAX_ENTRIES chunks each — so no inter-batch delay needed here)
        raw_responses = asyncio.run(self._provider.complete_many(requests))  # type: ignore[union-attr]

        # Map parsed results back to original indices
        for batch, raw in zip(batches, raw_responses):
            if not raw:
                continue
            parsed = _parse_blocks(raw, len(batch))
            for seq_i, orig_i in enumerate(batch):
                results[orig_i] = parsed[seq_i]

        filled = sum(1 for r in results if r)
        logger.info("LLM done  cat=%s  filled=%d/%d", category, filled, len(entries))
        return results

    def generate_doc_overview(
        self,
        doc_name: str,
        pdf_name: str,
        entries: list[dict],
        max_excerpts: int = 6,
    ) -> str:
        """
        Return a short prose overview of the document.
        Picks the richest non-placeholder chunks as excerpts.
        Returns empty string on failure or when LLM disabled — caller uses static fallback.
        """
        if not self.enabled or not entries:
            return ""

        sample = [
            c for c in sorted(entries, key=lambda x: -x.get("token_count", 0))
            if not _is_placeholder(c.get("content", ""))
        ][:max_excerpts]
        if not sample:
            return ""

        lines = [
            f"--- Excerpt {i} ---\n{_make_snippet(c)}"
            for i, c in enumerate(sample, 1)
        ]
        user_msg = f"Document: {doc_name} ({pdf_name})\n\n" + "\n\n".join(lines)

        logger.info("LLM overview  doc=%s  excerpts=%d", doc_name, len(sample))
        try:
            return self._provider.complete(_OVERVIEW_SYSTEM, user_msg)  # type: ignore[union-attr]
        except Exception as exc:
            logger.warning("LLM overview failed  doc=%s  error=%s", doc_name, exc)
            return ""
