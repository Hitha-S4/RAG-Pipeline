"""
SummaryDistiller — Layer-3 distillation.

Turns the raw, per-chunk summaries (one messy entry per recursive chunk) into
ONE clean, merged, retrieval-optimised document per category, matching the
distilled reference layout exactly.

    raw per-chunk summaries        (many fragments, duplicates, chunk-ids)
            │
            ├─ group by category
            │
            ├─ hierarchical LLM merge per category   (lossless: nothing dropped)
            │     groups sized to the input window; repeat until one document
            │
            └─ <CATEGORY>.md   with the reference header:
                   # <product> — <CATEGORY>
                   **Category:** x  |  **Generated:** <date>  |  **Source:** <file>

Data-source independent: the product label comes only from settings.product_name;
the source label comes from the file name passed in. No product is named in code.

Retrieval note: the distilled entries are answer-first (name/term stated first),
which is what lets a user question match the entry above the cosine threshold.
The distilled text of each entry becomes the summary that gets embedded.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from src.config.settings import get_settings
from src.enums import ChunkCategory
from src.models import Chunk
from src.services.ingestion.entity_pipeline import make_windows, window_char_budget
from src.services.ingestion.prompts.distill import DISTILL_CATEGORIES, get_distill_prompts
from src.utils.logging import get_logger

logger = get_logger(__name__)

CATEGORIES = tuple(c.value for c in ChunkCategory)


def _header(product: str, category: str, source: str) -> str:
    return (f"# {product} — {category.upper()}\n\n"
            f"**Category:** {category}  |  **Generated:** {date.today().isoformat()}"
            f"  |  **Source:** {source}\n\n---\n")


class SummaryDistiller:
    """Distills raw per-chunk summaries into merged per-category documents."""

    def __init__(self, llm, settings=None):
        self.llm = llm
        self.settings = settings or get_settings()

    # ── collect raw notes per category ───────────────────────────────────────
    @staticmethod
    def _raw_notes(chunks: list[Chunk], category: str) -> list[str]:
        """One raw note per chunk of this category.

        Content strategy per category:
          keywords  — emit the term name verbatim on its own header line, then
                      the full content so the distill LLM can build
                      "TERM(Full Name): sentence" from the actual definition,
                      not from a paraphrased summary.
          workflows — emit full content (steps, commands) not just the 1-2
                      sentence summary; the distill prompt restructures it into
                      Pre-requisites + Execution Steps + APIs/Tools.
          features  — emit full content (support matrix, limits, description)
                      not just the summary; the distill prompt builds the
                      Components/Links schema from it.
          all others — name + summary (summary is already answer-first prose).
        """
        # Categories where we want full content, not the condensed summary.
        _CONTENT_CATS = {"keywords", "workflows", "features"}

        notes: list[str] = []
        for c in chunks:
            if c.metadata.chunk_type.value != category:
                continue
            name = (c.metadata.headings or ["(unnamed)"])[0]

            if category in _CONTENT_CATS:
                # Full content gives the distill LLM enough structure to work with.
                text = (c.content or c.summary or "").strip()
                if not text:
                    continue
                if category == "keywords":
                    # Format: "TERM:\n<content>" — preserves the exact term name
                    # so SYSTEM_KEYWORDS can re-emit it as "TERM(Full Name): sentence."
                    notes.append(f"- {name}:\n  {text}")
                else:
                    # workflows / features: include sub_type as a type hint.
                    sub = c.metadata.sub_type or "other"
                    notes.append(f"- {name} [{sub}]:\n  {text}")
            else:
                text = (c.summary or c.content or "").strip()
                if not text:
                    continue
                notes.append(f"- {name}: {text}")

        return notes

    # ── hierarchical merge (lossless) ────────────────────────────────────────
    def _merge(self, category: str, notes: list[str]) -> str:
        """Merge raw notes into one document, in window-sized groups, repeating
        until a single document remains. Nothing is dropped: a group too large
        to merge is passed through rather than truncated."""
        if not notes:
            return ""
        spec   = get_distill_prompts(category, self.settings.product_name)
        system = spec["system"]
        task   = spec["task"]   # already has {doc_name}/{export_date}/{context} filled;
                                # still contains {notes} placeholder for the notes block
        budget = window_char_budget()

        # A "unit" starts as one raw note; after each round it is a merged doc.
        units = notes
        rnd = 0
        while True:
            rnd += 1
            groups: list[list[str]] = []
            cur: list[str] = []
            size = 0
            for u in units:
                if size + len(u) > budget and cur:
                    groups.append(cur)
                    cur, size = [], 0
                cur.append(u)
                size += len(u) + 2
            if cur:
                groups.append(cur)

            logger.info("[distill:%s] round %d: %d unit(s) → %d group(s)",
                        category, rnd, len(units), len(groups))

            tasks = [(system, task.format(notes="\n".join(g))) for g in groups]
            merged = self.llm.complete_batch(tasks)
            units = [m.strip() for m in merged if m and m.strip()]

            if not units:
                logger.error("[distill:%s] merge round %d produced nothing",
                             category, rnd)
                return ""
            if len(units) == 1:
                return units[0]
            if len(groups) == len(units) and rnd > 1:
                # No further reduction possible — concatenate losslessly.
                logger.warning("[distill:%s] cannot reduce further — concatenating",
                               category)
                return "\n\n".join(units)

    # ── build all six ────────────────────────────────────────────────────────
    def distill(self, chunks: list[Chunk], out_dir: Path, source_name: str) -> dict[str, str]:
        """Write <CATEGORY>.md for every category. Returns {category: markdown}.

        Existing files are removed before each run so the LLM merge always
        reflects the current chunks. The old resume-skip guard caused stale
        files to persist silently across ingestion runs.
        """
        out_dir.mkdir(parents=True, exist_ok=True)
        product = self.settings.product_name
        docs: dict[str, str] = {}

        for category in CATEGORIES:
            final = out_dir / f"{category.upper()}.md"
            if final.exists():
                logger.info("[distill:%s] removing stale file to rebuild", category)
                final.unlink()

            notes = self._raw_notes(chunks, category)
            if not notes:
                body = f"_No {category} content found._"
                logger.warning("[distill:%s] no raw notes", category)
            else:
                body = self._merge(category, notes)
                logger.info("[distill:%s] %d note(s) → %d chars",
                            category, len(notes), len(body))

            md = _header(product, category, source_name) + "\n" + body + "\n"
            final.write_text(md, encoding="utf-8")
            docs[category] = md

        return docs
