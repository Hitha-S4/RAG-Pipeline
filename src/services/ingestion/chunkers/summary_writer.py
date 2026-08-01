"""
Summary writer — persists the summary layer produced by SummarizerService.

Files written to output/<source_name>/summaries/:

    <CATEGORY>_SUMMARY.md     one entry per chunk: heading path + gist summary,
                              ordered by depth (roots first) — this is the
                              "raw file with all summaries of the respective type".
    OVERVIEW.md               the summary-of-summaries: per-category overview
                              followed by the single document-level overview.
    summaries.jsonl           machine-readable: {chunk_id, type, depth, is_leaf,
                              parent_id, headings, summary} for every chunk.

This complements the existing MarkdownService (which emits the schema-shaped
*.md and verbatim *_RAW.md). Here the RAW-equivalent carries *summaries*, and
OVERVIEW.md carries the rolled-up gist, exactly per the ingestion design.
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from src.enums import ChunkCategory
from src.models import Chunk
from src.utils.logging import get_logger

logger = get_logger(__name__)

CATEGORIES = tuple(c.value for c in ChunkCategory)


def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _heading_path(c: Chunk) -> str:
    hs = c.metadata.headings or []
    return " > ".join(h.replace("\n", " ").strip() for h in hs if h.strip())


class SummaryWriterService:
    def __init__(self, settings=None):
        if settings is None:
            from src.config.settings import get_settings
            settings = get_settings()
        self._settings = settings

    def _out_dir(self, source_name: str) -> Path:
        base = Path(self._settings.jsonl_output_dir) / source_name / "summaries"
        base.mkdir(parents=True, exist_ok=True)
        return base

    def write(
        self,
        chunks: list[Chunk],
        overviews: dict[str, str],
        source_name: str,
        pdf_name: str,
    ) -> Path:
        out = self._out_dir(source_name)

        by_cat: dict[str, list[Chunk]] = defaultdict(list)
        for c in chunks:
            by_cat[str(c.metadata.chunk_type)].append(c)

        # ── Per-category summary collections ──────────────────────────────────
        for cat in CATEGORIES:
            cs = sorted(
                by_cat.get(cat, []),
                key=lambda c: (c.metadata.depth, not c.metadata.is_leaf),
            )
            lines = [
                f"# {source_name} — {cat.upper()} Summaries",
                "",
                f"**Source:** {pdf_name}",
                f"**Category:** {cat}",
                f"**Total nodes:** {len(cs)}",
                f"**Export Date:** {_today()}",
                "",
                "---",
                "",
            ]
            for c in cs:
                if not c.summary:
                    continue
                kind = "leaf" if c.metadata.is_leaf else "rollup"
                lines += [
                    f"## L{c.metadata.depth} · {kind} · {_heading_path(c) or '(no heading)'}",
                    "",
                    f"`{c.chunk_id}`  parent=`{c.metadata.parent_id or '—'}`",
                    "",
                    c.summary,
                    "",
                    "---",
                    "",
                ]
            (out / f"{cat.upper()}_SUMMARY.md").write_text("\n".join(lines), encoding="utf-8")

        # ── Overview (summary of summaries) ───────────────────────────────────
        ov_lines = [
            f"# {source_name} — Overview",
            "",
            f"**Source:** {pdf_name}",
            f"**Export Date:** {_today()}",
            "",
            "---",
            "",
            "## Document Overview",
            "",
            overviews.get("_document", "(no document overview generated)"),
            "",
        ]
        for cat in CATEGORIES:
            if overviews.get(cat):
                ov_lines += [f"## {cat.capitalize()} Overview", "", overviews[cat], ""]
        (out / "OVERVIEW.md").write_text("\n".join(ov_lines), encoding="utf-8")

        # ── Machine-readable dump ─────────────────────────────────────────────
        with (out / "summaries.jsonl").open("w", encoding="utf-8") as f:
            for c in chunks:
                if not c.summary:
                    continue
                f.write(json.dumps({
                    "chunk_id":  c.chunk_id,
                    "type":      str(c.metadata.chunk_type),
                    "depth":     c.metadata.depth,
                    "is_leaf":   c.metadata.is_leaf,
                    "parent_id": c.metadata.parent_id,
                    "headings":  c.metadata.headings,
                    "summary":   c.summary,
                }, ensure_ascii=False) + "\n")

        logger.info("Summary files written → %s", out)
        return out
