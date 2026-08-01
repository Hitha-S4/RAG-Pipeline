"""
Output writer — persists chunk data to disk after classify_and_summarize.

Writes to output/<source_name>/:
    chunks_<category>.jsonl   — one file per category; a chunk appearing in
                                multiple categories is written to each of them.
    chunks.report.txt         — summary statistics

JSONL record schema (per row) — full independent-lane schema:
    chunk_id        — UUID primary key
    chunk_type      — extraction category (knowledge | keywords | personas |
                      workflows | features | entities)
    sub_type        — lifecycle axis (install | configure | monitor | … | other)
    depth           — tree depth (1 = window root, 2 = extracted block,
                      3 = recursive piece)
    is_leaf         — True when this chunk is embeddable (no children)
    parent_id       — chunk_id of parent, or null for roots
    children_ids    — list[chunk_id] of direct children
    content_hash    — SHA-256 of content (dedup / change detection)
    headings        — heading path extracted from the LLM Name field
    content         — extracted content text (embedded as content_embedding)
    summary         — abstractive gist (embedded as summary_embedding)
    token_count     — approximate token count of content
    categories      — list[str] category assignment(s)

Milvus additionally stores:
    embedding         — content vector (FLOAT_VECTOR)
    summary_embedding — summary vector (FLOAT_VECTOR)
"""
from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from src.config.settings import get_settings
from src.models import Chunk
from src.utils.logging import get_logger

logger = get_logger(__name__)

CATEGORIES = ("features", "workflows", "personas", "knowledge", "keywords", "entities")


def _base_dict(c: Chunk) -> dict[str, Any]:
    """Fields written to every JSONL row — matches the full independent-lane schema.

    chunk_type and sub_type are now included so every row carries the complete
    per-category identity required by the independent extraction lane design:
        {chunk_id, chunk_type, sub_type, depth, is_leaf, parent_id,
         children_ids, content_hash, headings, content, summary, token_count}
    """
    return {
        "chunk_id":     c.chunk_id,
        "chunk_type":   c.metadata.chunk_type.value,   # e.g. "knowledge", "keywords"
        "sub_type":     c.metadata.sub_type or "other", # e.g. "configure", "overview"
        "depth":        c.metadata.depth,
        "is_leaf":      c.metadata.is_leaf,
        "parent_id":    c.metadata.parent_id,
        "children_ids": c.metadata.children_ids,
        "content_hash": c.content_hash,
        "headings":     c.metadata.headings,
        "content":      c.content,
        "summary":      c.summary,
        "token_count":  c.token_count,
    }


class OutputWriterService:
    def __init__(self):
        self._settings = get_settings()

    def _out_dir(self, source_name: str) -> Path:
        base = Path(self._settings.jsonl_output_dir) / source_name
        base.mkdir(parents=True, exist_ok=True)
        return base

    def write(
        self,
        chunks: list[Chunk],
        source_name: str,
        classified: list[dict] | None = None,
    ) -> Path:
        """
        Write per-category JSONL files + report.

        Parameters
        ----------
        chunks:
            All Chunk objects from the chunker.
        source_name:
            Output directory name under jsonl_output_dir.
        classified:
            Optional list parallel to *chunks*. Each entry has ``categories``
            (list[str]) and optionally ``summary`` (str). When None, falls back
            to the chunk_type already stored on each Chunk object.

        Each row written to JSONL now contains the full independent-lane schema:
            chunk_id, chunk_type, sub_type, depth, is_leaf, parent_id,
            children_ids, content_hash, headings, content, summary,
            token_count, categories
        (embedding and summary_embedding are only in Milvus — vectors are not
        written to JSONL to keep file sizes manageable.)
        """
        out = self._out_dir(source_name)

        # Build chunk_id → classified record map for fast lookup
        clf_by_id: dict[str, dict] = {}
        if classified:
            for rec in classified:
                clf_by_id[rec["chunk_id"]] = rec

        # Group base dicts by every category they belong to.
        # _base_dict() already includes chunk_type, sub_type, and summary from
        # the Chunk object. The classified record only supplements categories
        # and may override summary when a later pass produced a better one.
        by_cat: dict[str, list[dict]] = defaultdict(list)
        for c in chunks:
            rec = clf_by_id.get(c.chunk_id)
            base = _base_dict(c)
            if rec:
                base["categories"] = rec["categories"]
                # Override summary only when classified record has a non-empty one.
                if rec.get("summary"):
                    base["summary"] = rec["summary"]
                for cat in rec["categories"]:
                    if cat in set(CATEGORIES):
                        by_cat[cat].append(base)
            else:
                # Fallback: use the chunk_type already on the Chunk object.
                cat = c.metadata.chunk_type.value
                base["categories"] = [cat]
                # summary is already in base from _base_dict(c) — do not blank it.
                if cat in set(CATEGORIES):
                    by_cat[cat].append(base)

        for cat in CATEGORIES:
            path = out / f"chunks_{cat}.jsonl"
            rows = by_cat.get(cat, [])
            with path.open("w", encoding="utf-8") as f:
                for row in rows:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
            logger.info("Wrote %d chunks → %s", len(rows), path.name)

        self._write_report(chunks, by_cat, out / "chunks.report.txt")
        logger.info("Output written to: %s", out)
        return out

    def _write_report(
        self,
        chunks: list[Chunk],
        by_cat: dict[str, list[dict]],
        path: Path,
    ) -> None:
        depths: Counter = Counter(c.metadata.depth for c in chunks)
        leaves  = sum(1 for c in chunks if c.is_leaf)
        tok: dict[int, list[int]] = defaultdict(list)
        for c in chunks:
            tok[c.metadata.depth].append(c.token_count)

        lines = [
            " Chunk Report",
            "=" * 60,
            f"Generated  : {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"Total      : {len(chunks)}",
            f"Leaves     : {leaves}  ({100 * leaves // max(len(chunks), 1)}%)",
            f"Branches   : {len(chunks) - leaves}",
            "",
            "By depth:",
            *[
                f"  L{d}: {depths[d]:6d}  "
                f"avg={int(statistics.mean(tok[d])) if tok[d] else 0:4d} tok  "
                f"min={min(tok[d]) if tok[d] else 0}  "
                f"max={max(tok[d]) if tok[d] else 0}"
                for d in sorted(depths)
            ],
            "",
            "By category (after LLM classification):",
            *[f"  {cat:12s}: {len(by_cat.get(cat, []))} chunks" for cat in CATEGORIES],
        ]
        path.write_text("\n".join(lines), encoding="utf-8")
        logger.info("Report written → %s", path.name)
