"""
ClassifyService — single LLM pass that assigns categories + sub-type + summary
to every chunk.

This is the step-4 concern extracted from LLMService / MarkdownService so all
classify logic lives in one place.

Flow
────
    svc = ClassifyService()
    classified = svc.classify(chunks)   # list[Chunk] → list[dict]

Each output dict:
    {
        "chunk_id":    str,
        "categories":  list[str],   # one or more of the six category names
        "sub_type":    str,         # one lifecycle action (or "")
        "summary":     str,
        "headings":    list[str],
        "content":     str,
        "depth":       int,
        "is_leaf":     bool,
        "parent_id":   str | None,
        "token_count": int,
    }
"""
from __future__ import annotations

import asyncio
import re

from src.enums import ChunkCategory, ChunkSubType
from src.models import Chunk
from src.services.ingestion.classifiers.taxonomy import classify_sub_type as _heuristic_sub_type
from src.services.ingestion.prompts import CLASSIFY_SYSTEM as _CLASSIFY_SYSTEM
from src.utils.llm_helpers import _is_placeholder, _make_snippet, _parse_blocks
from src.utils.logging import get_logger

logger = get_logger(__name__)

_VALID_SUB_TYPES: frozenset[str] = frozenset(e.value for e in ChunkSubType)


_FACET_KEYS = ("keywords", "features", "workflows", "personas", "entities")


def _parse_facets(block: str) -> dict[str, list[str]]:
    """
    Pull the facet lines out of a ===N=== block.

    These drive two things:
      • cross-category links (persona -> feature -> workflow -> knowledge)
      • the facet term of the relevance score (lexical anchor on rare terms)
    "none"/empty is normalised to an empty list.
    """
    out: dict[str, list[str]] = {k: [] for k in _FACET_KEYS}
    for key in _FACET_KEYS:
        m = re.search(rf"^-\s*{key}\s*:\s*(.+)$", block, re.MULTILINE | re.IGNORECASE)
        if not m:
            continue
        raw = m.group(1).strip()
        if raw.lower() in {"none", "n/a", "-", ""}:
            continue
        vals = [v.strip() for v in raw.split(",")]
        out[key] = [v for v in vals if v and v.lower() != "none"][:8]
    return out


def _parse_classify_block(block: str) -> tuple[list[str], str, str]:
    """Parse a single ===N=== block into (categories, sub_type, summary)."""
    VALID = frozenset(e.value for e in ChunkCategory)

    cats_raw = ""
    m = re.search(r"^-\s*[Cc]ategories?:\s*(.+)", block, re.MULTILINE)
    if m:
        cats_raw = m.group(1).strip()

    sub_type = ""
    ms = re.search(r"^-\s*[Ss]ub[\s_-]?[Tt]ype:\s*([A-Za-z]+)", block, re.MULTILINE)
    if ms:
        cand = ms.group(1).strip().lower()
        if cand in _VALID_SUB_TYPES:
            sub_type = cand

    summ = ""
    m2 = re.search(r"^-\s*[Ss]ummary:\s*(.+)", block, re.MULTILINE | re.DOTALL)
    if m2:
        raw = m2.group(1).strip()
        raw = re.split(r"\n-\s+\w+:", raw)[0].strip()
        summ = re.sub(r"\s+", " ", raw)

    cats = [c.strip().lower() for c in re.split(r"[,/;]+", cats_raw) if c.strip()]
    cats = [c for c in cats if c in VALID]
    if not cats:
        cats = [ChunkCategory.KNOWLEDGE.value]

    return cats, sub_type, summ, _parse_facets(block)


# ── Service ───────────────────────────────────────────────────────────────────

class ClassifyService:
    """
    Wraps LLMService.classify_and_summarize with Chunk → dict conversion.

    Owned entirely by the classifiers package so the classify concern lives in
    one place, separate from the MD-generation logic in MarkdownService.
    """

    def __init__(self, settings=None):
        from src.services.ingestion.llm_service import LLMService
        self._llm = LLMService(settings)

    def _chunk_to_raw(self, c: Chunk) -> dict:
        return {
            "chunk_id":    c.chunk_id,
            "chunk_type":  str(c.metadata.chunk_type),
            "depth":       c.metadata.depth,
            "is_leaf":     c.metadata.is_leaf,
            "headings":    c.metadata.headings,
            "parent_id":   c.metadata.parent_id,
            "content":     c.content,
            "token_count": c.token_count,
        }

    def classify_and_summarize(self, chunks: list[dict]) -> list[dict]:
        """
        Single LLM pass over all chunks. For each chunk the model returns:
          - categories : list[str]  — one or more of the six category names
          - sub_type   : str        — one lifecycle action (or "")
          - summary    : str        — 1-2 sentence extractive/abstractive summary

        Returns a list parallel to *chunks*. Placeholders and LLM failures fall
        back to an extractive summary and the pre-assigned chunk_type.
        """
        VALID = frozenset(e.value for e in ChunkCategory)

        def _extractive(c: dict) -> str:
            body = re.sub(r"^\[Parent[^\]]*\]\n\n", "", c.get("content", ""), flags=re.DOTALL)
            body = re.sub(r"\s+", " ", body).strip()
            sents = re.split(r"(?<=[.!?])\s+", body)
            return " ".join(s for s in sents[:2] if s)[:280]

        # Build output records with extractive fallbacks.
        # RC3 fix: run heuristic classify_sub_type() immediately so sub_type is
        # never empty — the LLM pass below will override it if it returns a
        # valid value, but at minimum every chunk leaves with a real sub_type.
        results: list[dict] = []
        for c in chunks:
            fallback_cat = str(c.get("chunk_type", ChunkCategory.KNOWLEDGE.value))
            if fallback_cat not in VALID:
                fallback_cat = ChunkCategory.KNOWLEDGE.value
            heuristic_st = _heuristic_sub_type(
                c.get("content", ""),
                headings=c.get("headings") or [],
            ).value
            results.append({
                "chunk_id":    c.get("chunk_id", ""),
                "categories":  [fallback_cat],
                "sub_type":    heuristic_st,
                "summary":     _extractive(c),
                "keywords":    [],
                "features":    [],
                "workflows":   [],
                "personas":    [],
                "entities":    [],
                "headings":    c.get("headings") or [],
                "content":     c.get("content", ""),
                "depth":       c.get("depth", 1),
                "is_leaf":     c.get("is_leaf", True),
                "parent_id":   c.get("parent_id"),
                "token_count": c.get("token_count", 0),
            })

        if not self._llm.enabled or not chunks:
            return results

        real_idx = [
            i for i, c in enumerate(chunks)
            if not _is_placeholder(c.get("content", ""))
        ]
        if not real_idx:
            return results

        batches: list[list[int]] = [
            real_idx[s : s + self._llm._max_entries]
            for s in range(0, len(real_idx), self._llm._max_entries)
        ]

        requests: list[tuple[str, str]] = []
        for batch in batches:
            lines = [
                f"--- Excerpt {seq} ---\n{_make_snippet(chunks[i])}"
                for seq, i in enumerate(batch, 1)
            ]
            requests.append((_CLASSIFY_SYSTEM, "\n\n".join(lines)))

        logger.info(
            "classify_and_summarize  chunks=%d  batches=%d  real=%d",
            len(chunks), len(batches), len(real_idx),
        )

        raw_responses = self._llm.complete_batch(requests)

        for batch, raw in zip(batches, raw_responses):
            if not raw:
                continue
            parsed_blocks = _parse_blocks(raw, len(batch))
            for seq_i, orig_i in enumerate(batch):
                block = parsed_blocks[seq_i]
                if not block:
                    continue
                cats, sub_type, summ, facets = _parse_classify_block(block)
                if cats:
                    results[orig_i]["categories"] = cats
                if sub_type:
                    results[orig_i]["sub_type"] = sub_type
                if summ:
                    results[orig_i]["summary"] = summ
                for _k, _v in facets.items():
                    if _v:
                        results[orig_i][_k] = _v

        filled = sum(1 for r in results if r["summary"])
        logger.info("classify_and_summarize done  filled=%d/%d", filled, len(chunks))
        return results

    def classify(self, chunks: list[Chunk]) -> list[dict]:
        """
        Convert Chunks to raw dicts and run classify_and_summarize.
        Callers pass the result to both OutputWriterService.write() and
        MarkdownService.generate() to avoid running the LLM twice.
        """
        raw = [self._chunk_to_raw(c) for c in chunks]
        return self.classify_and_summarize(raw)
