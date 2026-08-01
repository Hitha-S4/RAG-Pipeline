"""
Centralised application settings — types only.

All values must be supplied via .env (copy .env.example → .env).
pydantic-settings resolves: .env file → environment variables.

The only exception is ``milvus_lite_path``, which is ``Optional[str]``
because it is only required when ``MILVUS_MODE=lite`` (commented-out in
.env.example by design — uncomment it when switching to lite mode).
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Literal, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, DotEnvSettingsSource, SettingsConfigDict


class _DotEnvSource(DotEnvSettingsSource):
    """DotEnvSettingsSource that strips inline ``# comments`` from .env values.

    pydantic-settings does not strip inline comments from value lines, so::

        MILVUS_MODE=standalone   # standalone | lite

    would be read as ``'standalone   # standalone | lite'`` and fail Literal
    validation.  This subclass post-processes every raw string value returned
    by the parent to remove anything after an unquoted ``#``.

    Note: the .env file itself must not have inline comments on value lines —
    use the script in scripts/strip_env_comments.py to clean it if needed.
    The parent DotEnvSettingsSource reads the file before this class sees the
    values, so this acts as a safety net for any remaining edge cases.
    """

    def __call__(self) -> dict[str, Any]:
        raw = super().__call__()
        cleaned: dict[str, Any] = {}
        for key, value in raw.items():
            if isinstance(value, str):
                # Strip inline comment: everything from ' #' onwards.
                # Quoted values are already handled by the parent loader.
                stripped = value.split(" #")[0].strip()
                cleaned[key] = stripped
            else:
                cleaned[key] = value
        return cleaned


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):  # type: ignore[override]
        """Replace the default dotenv source with our comment-stripping one."""
        sources = super().settings_customise_sources(settings_cls, **kwargs)
        # sources is a tuple: (init_settings, env_settings, dotenv_settings, ...)
        # Replace DotEnvSettingsSource with our comment-stripping subclass.
        patched = []
        for src in sources:
            if isinstance(src, DotEnvSettingsSource):
                patched.append(
                    _DotEnvSource(
                        settings_cls,
                        env_file=cls.model_config.get("env_file", ".env"),
                        env_file_encoding=cls.model_config.get("env_file_encoding", "utf-8"),
                        case_sensitive=cls.model_config.get("case_sensitive", False),
                        env_ignore_empty=cls.model_config.get("env_ignore_empty", False),
                        env_nested_delimiter=cls.model_config.get("env_nested_delimiter"),
                    )
                )
            else:
                patched.append(src)
        return tuple(patched)

    # ── App ───────────────────────────────────────────────────────────────────
    app_name:  str
    app_env:   Literal["development", "staging", "production"]
    log_level: str

    # Name of the product the ingested documentation describes.  Prompts are
    # data-source independent; this is the ONLY place a product is named.
    # Set PRODUCT_NAME in .env (e.g. "IBM Guardium Data Protection (GDP)").
    product_name: str = "the product"

    # ── Milvus ────────────────────────────────────────────────────────────────
    milvus_mode:       Literal["lite", "standalone"]
    milvus_lite_path:  Optional[str] = None   # required only when milvus_mode=lite
    milvus_host:       str
    milvus_port:       int
    milvus_user:       str
    milvus_password:   str
    milvus_collection: str
    milvus_dimension:  int

    # ── Embedding ─────────────────────────────────────────────────────────────
    # multi-qa-MiniLM-L6-cos-v1 is an ASYMMETRIC Q→passage model (same 384-dim
    # as all-MiniLM-L6-v2, no Milvus schema change).  It shifts the relevant-pair
    # cosine band from 0.55–0.75 → 0.75–0.95, which is the single largest lever
    # on retrieval quality.
    #
    # IMPORTANT: changing embedding_model_name invalidates ALL stored vectors.
    #   1. Drop the Milvus collection (POST /api/v1/admin/drop-collection)
    #   2. Re-ingest every document
    #   3. Re-run tests/calibrate_cosine.py and update cos_floor / cos_ceil below
    embedding_provider:   str   = "local"   # local | aim
    embedding_model_name: str   = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
    embedding_batch_size: int   = 64
    embedding_delay:      float = 0.0       # only used for aim provider

    # ── Provider (IBM AIM) ────────────────────────────────────────────────────
    llm_base_url: str
    llm_api_key:  str = Field(repr=False)

    # ── LLM ───────────────────────────────────────────────────────────────────
    llm_enabled:     bool
    llm_model:          str

    # ── Token budget ──────────────────────────────────────────────────────────
    # The model's TOTAL context is shared by input + output:
    #
    #     llm_input_window_tokens  +  llm_max_output_tokens  +  safety
    #                                                  <=  llm_context_window
    #
    # CRITICAL INSIGHT — keep INPUT window SMALL, raise OUTPUT independently:
    #
    #   LLM_INPUT_WINDOW_TOKENS controls window SIZE (chars of PDF fed per call).
    #   LLM_MAX_OUTPUT_TOKENS   controls how many tokens the LLM can emit.
    #
    #   DO NOT raise both together. Raising input to 32k causes 30× chunk regression:
    #     8,000 input tokens (24k chars) → ~241 windows → ~4,120 chunks   ✅
    #    32,000 input tokens (96k chars) → ~13 windows  →   ~132 chunks   ❌
    #
    # CONFIRMED LIMITS (aim.dev03, granite-4-h-small, 2026-07-15):
    #   - Watsonx hard new-token cap : 100,000  (110k → WatsonxException)
    #   - AIM proxy ceiling          : 100,000  (passes cleanly up to 100k)
    #   - Model total context        : 131,072
    #
    # RECOMMENDED (current .env):
    #     LLM_INPUT_WINDOW_TOKENS=8000    # 24k chars/window → ~241 windows for gdp-12.x
    #     LLM_MAX_OUTPUT_TOKENS=32000     # 4× more output budget → less truncation
    #     LLM_MAX_TOKENS=8000             # legacy alias for input window
    #     Total/window ≈ 41,000 ≪ 131,072 ✓  headroom × 3
    #
    llm_context_window:      int = 131_072   # model's total context (informational)
    llm_input_window_tokens: int = 8_000     # input tokens per window — keep small!
    # max_tokens sent in every API request body.
    # Real ceiling: 100,000 (Watsonx hard cap).  _safe_max_tokens() in providers.py
    # enforces min(this, _MAX_NEW_TOKENS_HARD_CAP=100k, context_budget).
    llm_max_output_tokens:   int = 32_000

    # Legacy alias — some callers still read llm_max_tokens. Kept as the INPUT
    # window budget so old .env files keep working; prefer llm_input_window_tokens.
    llm_max_tokens:  int

    # llm_clean_enabled: LLM cleaning pass on each window before extraction.
    # DISABLED: the cleaner must reproduce the full window (~24 k chars) but at
    # 8 k output tokens the model can emit far less → every window falls back,
    # wasting ~563 extra LLM calls with zero quality gain. Leave false.
    llm_clean_enabled: bool = False
    llm_timeout:     int
    llm_concurrency: int
    llm_max_entries: int
    llm_request_delay: float = 0.5   # seconds between concurrency windows (rate-limit guard)
    llm_thinking: str = ""           # reasoning effort: "low" | "medium" | "high" | "" (disabled)

    # llm_stream: request `stream: true` and consume the SSE response.
    #
    #   DEFAULT FALSE — THIS GATEWAY'S SSE IS BROKEN FOR gpt-oss-120b.
    #   Verified with scripts/probe_aim.sh against an identical prompt:
    #     stream=true   → ONE chunk, no finish_reason, no [DONE], 237 B
    #     stream=false  → full JSON, finish_reason=stop, usage present, 810 B
    #   The streamed response carries only the first few tokens and the stream
    #   then closes cleanly (curl exits 0 — so it is not a reset, a timeout, or
    #   a WAF). It is the gateway emitting a partial stream and calling it done.
    #   Non-streamed returns complete responses in 0.7-1.2 s, so streaming buys
    #   nothing here.
    #   MUST stay true for large models (gpt-oss-120b).  A non-streamed request
    #   with a multi-thousand-token output holds the connection idle for minutes;
    #   the CDN/ingress in front of AIM kills it and returns an HTML error page,
    #   which the old code mislabelled as a "WAF block".  Streaming keeps bytes
    #   flowing so the idle timer never fires.
    llm_stream: bool = False

    # llm_user_agent: sent as the User-Agent header.  curl's default
    # ("curl/8.x") is a common trigger for CDN bot rules; set something
    # identifiable for your service.
    llm_user_agent: str = "ragpipeline/1.0"

    # llm_stream_require_done: treat a stream with no `data: [DONE]` sentinel
    #   AND no finish_reason as a failure.
    #   LEAVE FALSE. [DONE] is an OpenAI convention, not part of SSE, and the
    #   watsonx/vLLM gateway does not send it — requiring it caused every one of
    #   389 windows to fail four times with "truncated" on complete responses.
    llm_stream_require_done: bool = True   # only consulted when llm_stream=true

    # llm_debug_raw_dir: directory for raw dumps of responses that fail to
    #   parse (first 5 per process). Empty string disables. Invaluable — it is
    #   the difference between reading the failure and guessing at it.
    llm_debug_raw_dir: str = "./debug/llm_raw"

    # llm_debug_min_chars: responses shorter than this are logged at WARNING
    #   with their exact content and dumped raw. They pass every transport
    #   check (HTTP 200, finish_reason=stop) but carry no extraction output —
    #   without this they are invisible until you notice total_chunks=6.
    llm_debug_min_chars: int = 50

    # llm_http_version: "1.1" | "2" | "auto".
    #   Default 1.1. HTTP/2 multiplexing behind a CDN/ingress can produce a
    #   mid-stream RST_STREAM that truncates an SSE response after the first
    #   frame — the observed failure. HTTP/1.1 has no stream-reset path.
    llm_http_version: str = "1.1"

    # llm_compact_schema: use the 5-field extraction schema instead of 11.
    #   Cuts completion tokens ~40%, which cuts wall-clock time ~40% since
    #   decode is the bottleneck. COST: no Evidence spans, no cross-type
    #   references (these feed graph_traversal.py). A data-model tradeoff,
    #   not a bug fix — verify your retrieval path before enabling.
    llm_compact_schema: bool = False
    # Extraction mode:
    #   "all_types"   — one LLM call per window extracts all six types (default, fastest)
    #   "sequential"  — ROUTER call per window, then one typed pass per category found,
    #                   processed as 6 serial full-window batches (highest fidelity, slowest)
    #   "parallel"    — ROUTER call per window (same as sequential), then ALL 6 typed passes
    #                   for ALL windows are dispatched into ONE combined LLM pool and run
    #                   concurrently (bounded by LLM_CONCURRENCY). Same call count as
    #                   sequential but wall-clock ≈ all_types because no inter-pass waiting.
    #                   Recommended when per-type prompt quality matters and speed must match
    #                   all_types. Requires LLM_CONCURRENCY >= 2 to be meaningful.
    #   "independent" — NO ROUTER. 6 direct per-category LLM passes in parallel, one pass
    #                   per (window, category) pair. Each pass uses only its own
    #                   TYPE_PROMPTS[category] system prompt + DIRECT_USER message so
    #                   the LLM extracts ONLY its assigned category from the raw window.
    #                   Implements the exact independent-lane schema:
    #                     stage2_cleaned → [Chunk] → LLM(knowledge prompt) → [Knowledge]
    #                       → {chunk_id, chunk_type, sub_type, depth, is_leaf,
    #                          parent_id, children_ids, content_hash,
    #                          summary, content, embedding, summary_embedding}
    #                   Same LLM call count as parallel but no ROUTER overhead.
    #                   Set LLM_EXTRACTION_MODE=independent in .env to activate.
    llm_extraction_mode: str = "all_types"

    # ── Chunking ──────────────────────────────────────────────────────────────
    chunk_strategy:        str  = "recursive"
    chunk_target_tokens:   int
    chunk_ceiling_tokens:  int
    chunk_overlap_tokens:  int
    chunk_leaf_min_tokens: int
    chars_per_token:       float

    # ── Summarization ─────────────────────────────────────────────────────────
    summarize_enabled: bool
    embed_summaries:   bool
    embed_all_nodes:   bool

    # ── Retrieval ─────────────────────────────────────────────────────────────
    # Match queries against the SUMMARY vector (abstractive gist) rather than the
    # raw CONTENT vector.  Summaries are brief, denoised, and category-focused, so
    # summary-space ANN is more precise for this taxonomy-driven pipeline.
    search_on_summary: bool = True

    # Summary→content fallback threshold.
    # When the best summary-cosine for a query is BELOW this value, the retrieval
    # service runs a second ANN pass against the raw content embedding and merges
    # the results (keeping the higher score per chunk).  This rescues chunks whose
    # summary is poorly worded but whose content is a strong match.
    # Set to 0.0 to disable fallback entirely; 1.0 to always run both passes.
    # Default 0.72 — triggers for the ~35% of queries that score below "Good".
    content_fallback_threshold: float = 0.85

    # ── Relevance scoring ─────────────────────────────────────────────────────
    # Composite = w_summary*norm(cos_summary) + w_content*norm(cos_content)
    # facet_match is excluded (weight 0.00) — lexical metadata fields are not
    # reliably populated, so the facet term was suppressing correct scores.
    score_w_summary: float = 0.75
    score_w_content: float = 0.25
    score_w_facet:   float = 0.00

    # Calibration band for the embedding model's cosine.
    # norm() linearly rescales [cos_floor, cos_ceil] → [0, 1] so the displayed
    # relevance score matches user expectations.
    #
    # Values below are set for multi-qa-MiniLM-L6-cos-v1 (asymmetric Q→passage):
    #   relevant pair band  : ~0.65 – 0.92   (vs 0.55–0.75 for symmetric MiniLM)
    #   irrelevant pair band: ~0.10 – 0.45
    #   → floor=0.40, ceil=0.90 is a reasonable starting point for this model.
    #
    # Run tests/calibrate_cosine.py after re-ingesting to get exact values from
    # your own corpus. Paste the printed floor/ceil here and restart the server.
    cos_floor: float = 0.40   # was 0.25 for all-MiniLM-L6-v2 (symmetric)
    cos_ceil:  float = 0.85   # was 0.75 for all-MiniLM-L6-v2 (symmetric)

    # ── Retrieval threshold ───────────────────────────────────────────────────
    # Hard minimum RAW cosine (NOT the rescaled norm()) a summary vector must
    # reach against the query for the chunk to be returned. Summaries are written
    # answer-first specifically so real questions clear this bar on the
    # multi-qa-MiniLM Q→passage model. Retrieval must apply this against the RAW
    # cosine, before norm() rescaling.
    retrieval_min_cosine: float = 0.90
    # If a query returns nothing above the threshold, optionally fall back to the
    # best available hit so the user still gets an answer (logged as low-conf).
    retrieval_fallback_to_best: bool = True

    # ── Cleaning ──────────────────────────────────────────────────────────────
    # Strip CLI / REST command-reference dumps (generic, shape-based) after load.
    strip_command_reference: bool  = True
    command_ref_density:     float = 0.6   # min command-line density to drop a block
    command_ref_min_lines:   int   = 3     # min lines a block needs before dropping

    # ── Storage ───────────────────────────────────────────────────────────────
    upload_dir: str
    max_upload_size_mb: int
    jsonl_output_dir: str
    md_output_dir: str  = "output"           # directory where *.md files are written
    summary_dir:  str  = "uploads/summary"  # flat dir for concise *.md summaries


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached singleton Settings instance."""
    return Settings()


def reload_settings() -> Settings:
    """Clear the settings cache and return a fresh Settings instance."""
    get_settings.cache_clear()
    return get_settings()
