"""
MarkdownService — two-phase per-category Markdown generation pipeline.

Flow
────
  Step 1 — classify (via ClassifyService, already done by caller in normal flow):
      Each chunk gets categories[] + summary.

  Step 2 — *_RAW.md per category:
      Records grouped by category → <CATEGORY>_RAW.md (summaries only).

  Step 3a — concise *.md for non-knowledge categories (batched concurrently):
      Layer-1: RAW → structured grouped Markdown (4 000-char segments)
      Layer-2: structured → compressed final (6 000-char windows)
      KEYWORDS special case: Layer-2 is replaced by _filter_keywords_output()
      which strips all prose/headings and enforces strict one-line-per-term format.

  Step 3b — KNOWLEDGE.md (generated last, uses all other *.md as context):
      Same two-layer approach, but reads already-written *.md files first.

12 files written per run:
    KNOWLEDGE_RAW.md / KNOWLEDGE.md
    FEATURES_RAW.md  / FEATURES.md
    WORKFLOWS_RAW.md / WORKFLOWS.md
    ENTITIES_RAW.md  / ENTITIES.md
    KEYWORDS_RAW.md  / KEYWORDS.md
    PERSONAS_RAW.md  / PERSONAS.md
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from src.enums import ChunkCategory
from src.models import Chunk
from src.services.ingestion.prompts import (
    SYSTEM_PROMPTS  as _L1_SYS,
    COMPRESS_SYSTEM as _L2_SYS,
)
from src.utils.logging import get_logger

from .helpers import DOC_NAME_FALLBACK, _clean_title, _today
from .pipeline import _build_concise_from_raw, _build_knowledge_context, _build_raw_md

logger = get_logger(__name__)

# ── KEYWORDS post-filter ──────────────────────────────────────────────────────
# Regex: a valid keyword line is  TERM(Full Name): sentence
# It must have a parenthesised full-name and end with a sentence (has a colon
# followed by at least 10 chars of text ending in a word character or period).
_KW_TERM_RE = re.compile(
    r'^[A-Za-z0-9][^\n(]{0,80}'   # term identifier (no newlines, no parens)
    r'\([^)]{2,100}\)'             # (Full Name)
    r':\s*.{10,}$'                 # : description (≥10 chars)
)

# Prose/section noise patterns to drop entirely — these are the "## Overview…"
# and "## Key Modules…" style headings and their paragraph text.
_KW_NOISE_RE = re.compile(
    r'^(#{1,6}\s|[-*]\s|\d+\.\s|>|`{3}|NOTE:|RULES?:|SOURCE:|CONTEXT:|ENTRIES:|---+\s*$)',
    re.IGNORECASE,
)


def _filter_keywords_output(raw: str) -> str:
    """
    Post-process the Layer-1 KEYWORDS LLM output into the strict format:

        TERM(Full Name): One complete sentence.

    Rules applied deterministically (no LLM needed):
    - Keep only lines that match the TERM(Full Name): description pattern.
    - Drop all ## headings, bullet lists, numbered lists, prose paragraphs,
      code fences, separator lines, and any line that begins with a noise marker.
    - Deduplicate by the normalised term key (lowercased, strip non-alphanumeric).
    - Sort A→Z by the term identifier (part before the first `(`).
    """
    seen: dict[str, str] = {}  # normalised_key → full line (first-wins dedup)
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        # Drop obvious noise lines first (fast path)
        if _KW_NOISE_RE.match(line):
            continue
        # Strip leading bullet/dash markers that the LLM sometimes adds
        line = re.sub(r'^[-*]\s+', '', line)
        # Validate the term-line pattern
        if not _KW_TERM_RE.match(line):
            continue
        # Normalise the term key for deduplication
        m = re.match(r'^([^(]+)', line)
        if not m:
            continue
        key = re.sub(r'[^a-z0-9]', '', m.group(1).lower())
        if key and key not in seen:
            seen[key] = line

    # Sort A→Z by the raw term identifier (case-insensitive)
    sorted_lines = sorted(seen.values(), key=lambda l: l.split('(')[0].strip().lower())
    return "\n".join(sorted_lines)


class MarkdownService:
    """
    Output layout per ingestion run
    ────────────────────────────────
    output/<source_name>/
        <CATEGORY>_RAW.md    ← summaries only (intermediate, no verbatim content)

    uploads/summary/
        KNOWLEDGE.md          ← concise high-level *.md  (the final outputs)
        FEATURES.md
        WORKFLOWS.md
        ENTITIES.md
        KEYWORDS.md
        PERSONAS.md
    """

    def __init__(self):
        from src.config.settings import get_settings
        from src.services.ingestion.llm_service import LLMService
        self._settings = get_settings()
        self._llm      = LLMService(self._settings)
        if self._llm.enabled:
            logger.info("LLM enrichment enabled  model=%s", self._settings.llm_model)
        else:
            logger.info("LLM enrichment disabled — set LLM_ENABLED=true to activate")

    def _out_dir(self, source_name: str) -> Path:
        """output/<source_name>/ — RAW.md + JSONL live here."""
        base = Path(self._settings.jsonl_output_dir) / source_name
        base.mkdir(parents=True, exist_ok=True)
        return base

    def _summary_dir(self) -> Path:
        """uploads/summary/ — concise *.md files go here (flat, always overwritten)."""
        base = Path(self._settings.upload_dir) / "summary"
        base.mkdir(parents=True, exist_ok=True)
        return base

    def generate(
        self,
        chunks: list[Chunk],
        source_name: str,
        pdf_name: str,
        classified: list[dict] | None = None,
    ) -> Path:
        """
        Full two-phase pipeline.

        Parameters
        ----------
        chunks:
            All Chunk objects from the chunker.
        source_name, pdf_name:
            Used for file naming and markdown headers.
        classified:
            Pre-computed output of ClassifyService.classify().  When None,
            ClassifyService is called internally (avoids running the LLM twice
            when the caller already has it).

        Returns the output directory (RAW.md location).
        Concise *.md files are written to uploads/summary/ (flat, overwritten on each run).

        Generation order:
            1. features, workflows, entities, keywords, personas  — all in parallel
               (each writes RAW.md then 2-layer concise *.md concurrently)
            2. knowledge — generated LAST using all other *.md files as context
               so KNOWLEDGE.md becomes the master overview document.
        """
        out     = self._out_dir(source_name)
        summary = self._summary_dir()

        # Step 1 — classify + summarize (if not already done by caller)
        if classified is None:
            from src.services.ingestion.classifiers import ClassifyService
            logger.info("[MD] Step1: classify_and_summarize %d chunks", len(chunks))
            classified = ClassifyService(self._settings).classify(chunks)

        # Infer doc name from first non-empty heading
        doc_name = DOC_NAME_FALLBACK
        for c in chunks:
            h = (c.metadata.headings or [""])[0].replace("\n", " ").strip()
            if h:
                doc_name = _clean_title(h)
                break

        display_pdf = re.sub(r"^[0-9a-f]{32}_", "", pdf_name)

        # Step 2 — group classified records by category
        _K  = ChunkCategory.KNOWLEDGE.value
        _KW = ChunkCategory.KEYWORDS.value
        CATS_FIRST = (
            ChunkCategory.FEATURES.value,
            ChunkCategory.WORKFLOWS.value,
            ChunkCategory.ENTITIES.value,
            _KW,
            ChunkCategory.PERSONAS.value,
        )
        _VALID_CATS = frozenset(e.value for e in ChunkCategory)
        by_cat: dict[str, list[dict]] = defaultdict(list)
        for rec in classified:
            for cat in rec.get("categories", [_K]):
                if cat in _VALID_CATS:
                    by_cat[cat].append(rec)
        # KEYWORDS gets every record so the glossary covers the full vocabulary
        by_cat[_KW] = classified

        # ── Step 3a: non-knowledge categories — fire all LLM batches concurrently ──
        raw_texts: dict[str, str] = {}
        for cat in CATS_FIRST:
            records = by_cat.get(cat, [])
            if not records:
                logger.info("[MD] %s  no records — skipping", cat.upper())
                continue
            raw_text = _build_raw_md(records, cat, doc_name, display_pdf)
            raw_path = out / f"{cat.upper()}_RAW.md"
            raw_path.write_text(raw_text, encoding="utf-8")
            filled = sum(1 for r in records if r.get("summary"))
            logger.info(
                "[MD] %s  RAW written → %s  entries=%d  with_summary=%d",
                cat.upper(), raw_path.name, len(records), filled,
            )
            raw_texts[cat] = raw_text

        # Build all layer-1 + layer-2 LLM requests for non-knowledge cats in one shot
        # KEYWORDS bypasses layer-2 (COMPRESS_SYSTEM) — uses _filter_keywords_output() instead.
        seg_size = 4000
        cat_segments: dict[str, list[str]] = {}
        for cat, raw_text in raw_texts.items():
            segs = [raw_text[i : i + seg_size] for i in range(0, len(raw_text), seg_size)]
            cat_segments[cat] = segs

        # Layer-1 requests
        l1_requests: list[tuple[str, str]] = []
        l1_meta: list[tuple[str, int]] = []
        for cat, segs in cat_segments.items():
            sys_p = _L1_SYS.get(cat) or "Produce well-structured Markdown. Group items under ## headings. Output ONLY Markdown."
            for i, seg in enumerate(segs):
                l1_requests.append((sys_p, seg))
                l1_meta.append((cat, i))

        logger.info("[MD] Layer-1 LLM batch  total_requests=%d", len(l1_requests))
        l1_responses = self._llm.complete_batch(l1_requests)

        l1_bodies: dict[str, str] = {}
        for (cat, _seg_idx), resp in zip(l1_meta, l1_responses):
            l1_bodies[cat] = l1_bodies.get(cat, "") + ("\n\n" if l1_bodies.get(cat) else "") + resp.strip()

        # Layer-2 requests — KEYWORDS is excluded; it gets the post-filter below instead
        win_size = 6000
        l2_requests: list[tuple[str, str]] = []
        l2_meta: list[tuple[str, int]] = []
        for cat, body in l1_bodies.items():
            if not body or cat == _KW:
                continue
            wins = [body[i : i + win_size] for i in range(0, len(body), win_size)]
            for i, w in enumerate(wins):
                l2_requests.append((_L2_SYS, w))
                l2_meta.append((cat, i))

        logger.info("[MD] Layer-2 LLM batch  total_requests=%d", len(l2_requests))
        l2_responses = self._llm.complete_batch(l2_requests)

        l2_bodies: dict[str, str] = {}
        for (cat, _win_idx), resp in zip(l2_meta, l2_responses):
            l2_bodies[cat] = l2_bodies.get(cat, "") + ("\n\n" if l2_bodies.get(cat) else "") + resp.strip()

        # KEYWORDS layer-2: deterministic post-filter instead of COMPRESS_SYSTEM
        if _KW in l1_bodies:
            l2_bodies[_KW] = _filter_keywords_output(l1_bodies[_KW])
            logger.info("[MD] KEYWORDS  post-filter applied  lines=%d",
                        l2_bodies[_KW].count("\n") + 1)

        header_tpl = (
            "# {doc_name} — {cat}\n\n"
            "**Category:** {cat_lower}  |  **Generated:** {date}  |  **Source:** {pdf}\n\n---\n\n"
        )
        for cat in CATS_FIRST:
            if cat not in raw_texts:
                continue
            body   = l2_bodies.get(cat) or l1_bodies.get(cat) or raw_texts[cat][:8000]
            header = header_tpl.format(
                doc_name=doc_name, cat=cat.upper(), cat_lower=cat,
                date=_today(), pdf=display_pdf,
            )
            md_path = summary / f"{cat.upper()}.md"
            md_path.write_text(header + body, encoding="utf-8")
            logger.info("[MD] %s  concise done → %s", cat.upper(), md_path)

        # ── Step 3b: KNOWLEDGE — generated last, reads all other *.md as context ──
        kn_records = by_cat.get(_K, classified)
        if kn_records:
            kn_raw = _build_raw_md(kn_records, _K, doc_name, display_pdf)
            (out / "KNOWLEDGE_RAW.md").write_text(kn_raw, encoding="utf-8")
            logger.info("[MD] KNOWLEDGE  RAW written  entries=%d", len(kn_records))

            kn_context = _build_knowledge_context(summary)
            kn_concise = _build_concise_from_raw(
                kn_raw, _K, doc_name, display_pdf, self._llm,
                extra_context=kn_context,
            )
            (summary / "KNOWLEDGE.md").write_text(kn_concise, encoding="utf-8")
            logger.info("[MD] KNOWLEDGE  master doc done → %s", summary / "KNOWLEDGE.md")

        logger.info("Markdown generation complete  raw=%s  summary=%s", out, summary)
        return out
