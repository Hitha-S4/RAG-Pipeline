"""
Embedding service — converts text chunks into dense vector embeddings.

Providers
─────────
    local  → sentence-transformers running on-device (MPS/CPU) — no network calls,
             no WAF, no rate limits. Default and recommended.
    remote → LLM provider embeddings endpoint via curl subprocess — fallback for
             when the local model is unavailable.

EMBEDDING_PROVIDER=local is set by default. Switch to remote in .env if needed.
"""
from __future__ import annotations

import json
import logging
import os
import subprocess
import tempfile
import time

from src.config.settings import get_settings
from src.models import Chunk
from src.utils.logging import get_logger

logger = get_logger(__name__)


# ── Local (HuggingFace sentence-transformers) provider ────────────────────────

class _LocalProvider:
    """Runs sentence-transformers on-device (MPS on Apple Silicon, CPU otherwise).
    Zero network calls — immune to WAF blocks and rate limits."""

    def __init__(self, model_name: str, batch_size: int):
        try:
            from sentence_transformers import SentenceTransformer  # type: ignore
        except ImportError:
            raise RuntimeError(
                "sentence-transformers is required: pip install sentence-transformers"
            )
        logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
        logger.info("Loading local embedding model: %s", model_name)
        self._model      = SentenceTransformer(model_name)
        self._batch_size = batch_size
        logger.info(
            "EmbeddingService ready  provider=local  model=%s  dim=%d",
            model_name, self._model.get_sentence_embedding_dimension(),
        )

    def embed(self, texts: list[str]) -> list[list[float]]:
        vectors = self._model.encode(
            texts,
            batch_size=self._batch_size,
            show_progress_bar=False,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
        return [v.tolist() for v in vectors]


# ── Remote (curl) provider ─────────────────────────────────────────────────────

class _RemoteProvider:
    """Calls the configured remote embeddings endpoint via curl. Fallback when local
    model is unavailable."""

    _TOKEN_LIMIT = 500

    def __init__(self, url: str, api_key: str, model: str, timeout: int = 120):
        self._url     = url
        self._api_key = api_key
        self._model   = model
        self._timeout = timeout
        try:
            from transformers import AutoTokenizer  # type: ignore
            logging.getLogger("transformers.tokenization_utils_base").setLevel(logging.ERROR)
            self._tokenizer = AutoTokenizer.from_pretrained(
                "sentence-transformers/all-MiniLM-L6-v2"
            )
        except Exception:
            self._tokenizer = None
        logger.info("EmbeddingService ready  provider=aim  url=%s  model=%s", url, model)

    def _truncate(self, text: str) -> str:
        if self._tokenizer is not None:
            ids = self._tokenizer.encode(text, add_special_tokens=True)
            if len(ids) <= self._TOKEN_LIMIT:
                return text
            return self._tokenizer.decode(
                ids[: self._TOKEN_LIMIT],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True,
            ).strip()
        max_chars = self._TOKEN_LIMIT * 2
        if len(text) <= max_chars:
            return text
        cut  = text[:max_chars]
        last = max(cut.rfind(". "), cut.rfind("\n"))
        return (text[:last + 1] if last > max_chars // 2 else cut).strip()

    def embed(self, texts: list[str]) -> list[list[float]]:
        truncated = [self._truncate(t) for t in texts]
        body      = json.dumps({"model": self._model, "input": truncated})

        last_exc: Exception = RuntimeError("no attempts made")
        for attempt in range(3):
            if attempt:
                time.sleep(2 ** attempt)
            with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
                tmp.write(body)
                tmp_path = tmp.name
            try:
                result = subprocess.run(
                    [
                        "/usr/bin/curl", "-s", "-X", "POST", self._url,
                        "-H", f"Authorization: Bearer {self._api_key}",
                        "-H", "Content-Type: application/json",
                        "-H", "Accept: application/json",
                        "-d", f"@{tmp_path}",
                        "--max-time", str(self._timeout),
                    ],
                    capture_output=True, text=True, timeout=self._timeout + 5,
                )
            finally:
                os.unlink(tmp_path)

            if result.returncode != 0:
                last_exc = RuntimeError(f"curl failed (rc={result.returncode}): {result.stderr[:300]}")
                logger.debug("AIM embed attempt %d: curl error", attempt + 1)
                continue
            raw = result.stdout.strip()
            if raw.lstrip().startswith("<"):
                last_exc = RuntimeError(f"AIM embed: WAF block: {raw[:120]}")
                logger.warning("AIM embed attempt %d: WAF HTML block", attempt + 1)
                continue
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                last_exc = RuntimeError(f"AIM embed: invalid JSON: {raw[:300]}")
                logger.debug("AIM embed attempt %d: invalid JSON", attempt + 1)
                continue
            if "error" in data or "data" not in data:
                last_exc = RuntimeError(f"AIM embed: error response: {raw[:300]}")
                logger.debug("AIM embed attempt %d: error body", attempt + 1)
                continue
            items = sorted(data["data"], key=lambda x: x.get("index", 0))
            return [item["embedding"] for item in items]

        logger.error("AIM embed failed after 3 attempts: %s", last_exc)
        raise last_exc


# ── Public service ────────────────────────────────────────────────────────────

class EmbeddingService:
    """Batched embedding service. Provider selected by EMBEDDING_PROVIDER setting."""

    def __init__(self):
        self._settings   = get_settings()
        self._batch_size = self._settings.embedding_batch_size
        self._batch_delay = self._settings.embedding_delay
        provider = getattr(self._settings, "embedding_provider", "local")

        if provider == "local":
            hf_model = getattr(
                self._settings, "embedding_model_name",
                "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
            )
            self._provider = _LocalProvider(hf_model, self._batch_size)
        elif provider == "aim":
            url = self._settings.llm_base_url.rstrip("/") + "/inference/embeddings"
            self._provider = _AIMProvider(
                url=url,
                api_key=self._settings.llm_api_key,
                model=self._settings.embedding_model_name,
            )
        else:
            raise ValueError(f"Unknown EMBEDDING_PROVIDER: {provider!r}. Use 'local' or 'aim'.")

    def _embed(self, texts: list[str]) -> list[list[float]]:
        return self._provider.embed(texts)

    def embed_chunks(self, chunks: list[Chunk]) -> list[Chunk]:
        """Embed all chunks in batches, populating Chunk.embedding in-place."""
        total   = len(chunks)
        batches = [chunks[i:i + self._batch_size] for i in range(0, total, self._batch_size)]
        logger.info("Embedding %d chunks in %d batches  provider=%s",
                    total, len(batches), type(self._provider).__name__)
        t0 = time.perf_counter()
        for idx, batch in enumerate(batches, start=1):
            if idx > 1 and self._batch_delay > 0:
                time.sleep(self._batch_delay)
            vectors = self._embed([c.content for c in batch])
            for chunk, vec in zip(batch, vectors):
                chunk.embedding = vec
            logger.debug("Embedded batch %d/%d", idx, len(batches))
        logger.info("Embedding complete  chunks=%d  elapsed=%.2fs", total, time.perf_counter() - t0)
        return chunks

    @staticmethod
    def _embed_text(c: Chunk) -> str:
        """Text actually embedded for retrieval: the section name prepended to
        the summary, so a question naming the item ('What is S-TAP?') matches
        even when the summary phrasing differs. The stored chunk.summary is left
        unchanged for display; only the embedded string carries the prefix."""
        name = ""
        headings = getattr(c.metadata, "headings", None) or []
        for h in headings:                       # first heading that isn't a part-N marker
            if h and not h.startswith("part-") and not h.startswith("window-"):
                name = h.strip()
                break
        summary = c.summary.strip()
        if name and not summary.lower().startswith(name.lower()):
            return f"{name}: {summary}"
        return summary

    def embed_summaries(self, chunks: list[Chunk]) -> list[Chunk]:
        """Embed chunk.summary into chunk.summary_embedding in-place.

        The embedded text is name-prefixed (see _embed_text); chunk.summary
        itself is not modified.
        """
        targets = [c for c in chunks if c.summary.strip()]
        if targets:
            batches = [targets[i:i + self._batch_size]
                       for i in range(0, len(targets), self._batch_size)]
            for idx, batch in enumerate(batches, 1):
                if idx > 1 and self._batch_delay > 0:
                    time.sleep(self._batch_delay)
                vectors = self._embed([self._embed_text(c) for c in batch])
                for c, v in zip(batch, vectors):
                    c.summary_embedding = v
        dim = self._settings.milvus_dimension
        for c in chunks:
            if not c.summary_embedding:
                c.summary_embedding = [0.0] * dim
        return chunks

    def embed_query(self, query: str) -> list[float]:
        """Return the embedding vector for a single query string."""
        return self._embed([query])[0]
