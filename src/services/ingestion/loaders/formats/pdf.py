"""PDF loader — extracts text via pdfplumber.

Uses font-size metadata to derive real heading levels (H1–H4), emitting
Markdown ``##`` markers so heading_tree.py parses unambiguous structure
instead of guessing from indentation.

Font-level heuristic (product-agnostic):
  • Collect all distinct font sizes from the page.
  • Body size = the most-frequent size (floor-rounded to 1 dp).
  • Any line whose max font size exceeds body_size is a heading candidate;
    sizes are ranked descending and mapped to levels 1–4.
  • Running headers/footers (a line that appears verbatim on > 10 % of pages)
    are suppressed by frequency, never by matching a product name.
"""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)

# Minimum number of pages a line must appear on before it is considered a
# running header/footer and suppressed.  10 % of the document is the threshold;
# we enforce a floor of 3 so a 5-page PDF doesn't lose legitimate headings.
_RUNNING_HDR_MIN_PAGES = 3
_RUNNING_HDR_RATIO     = 0.10

# How many distinct heading levels to emit (H1 … H_MAX_LEVELS).
_MAX_HEADING_LEVELS = 4

# A heading line is short and title-ish: no trailing sentence punctuation,
# not too many words.
_MAX_HEADING_WORDS = 12
_TERMINAL_PUNCT_RE = re.compile(r"[.!?,;]\s*$")


def _round1(v: float) -> float:
    return round(v, 1)


def _table_to_markdown(table: list[list[str | None]]) -> str:
    """Convert a pdfplumber table (list of rows, each a list of cell strings)
    into a Markdown table string.  Skips tables with fewer than 2 columns or
    rows, and rows that are entirely empty."""
    # Normalise cells: None → ""
    rows = [[str(c).strip() if c is not None else "" for c in row]
            for row in table if any(c for c in row)]
    if len(rows) < 2:
        return ""
    n_cols = max(len(r) for r in rows)
    # Pad rows to uniform width
    rows = [r + [""] * (n_cols - len(r)) for r in rows]
    header = "| " + " | ".join(rows[0]) + " |"
    sep    = "| " + " | ".join(["---"] * n_cols) + " |"
    body   = "\n".join("| " + " | ".join(r) + " |" for r in rows[1:])
    return "\n".join([header, sep, body])


def _extract_with_pdfplumber(path: Path) -> str:
    """
    Extract text from *path* using pdfplumber, annotating headings with
    Markdown ``#`` markers derived from font-size rank, and converting
    tables to Markdown table syntax so the LLM receives structured row data.

    Returns a single string ready for DocumentProcessor.
    """
    import pdfplumber  # type: ignore

    all_lines: list[str]            = []      # final output lines
    page_line_sets: list[set[str]]  = []      # for running-header detection

    # ── Pass 1: collect all words with their font sizes ───────────────────────
    raw_pages: list[list[dict]]      = []     # per-page list of word dicts
    raw_tables: list[list[str]]      = []     # per-page Markdown table blocks
    size_counter: Counter[float]     = Counter()

    with pdfplumber.open(str(path)) as pdf:
        for page in pdf.pages:
            words = page.extract_words(
                x_tolerance=3,
                y_tolerance=3,
                keep_blank_chars=False,
                use_text_flow=True,
                extra_attrs=["size"],
            )
            raw_pages.append(words)
            for w in words:
                sz = _round1(float(w.get("size") or 0))
                if sz > 0:
                    size_counter[sz] += 1

            # Extract tables for this page
            page_md_tables: list[str] = []
            try:
                tables = page.extract_tables()
                for tbl in (tables or []):
                    md = _table_to_markdown(tbl)
                    if md:
                        page_md_tables.append(md)
            except Exception:
                pass  # table extraction failure is non-fatal
            raw_tables.append(page_md_tables)

    if not size_counter:
        # No font-size data — fall back to plain pdfplumber text extraction
        with pdfplumber.open(str(path)) as pdf:
            pages_text = []
            for i, page in enumerate(pdf.pages):
                parts = [page.extract_text() or ""]
                if i < len(raw_tables):
                    parts.extend(raw_tables[i])
                pages_text.append("\n\n".join(p for p in parts if p))
            return "\n\n".join(pages_text)

    # Body size = most frequent size (floor-rounded)
    body_size = size_counter.most_common(1)[0][0]

    # Heading sizes: larger than body, sorted descending → level 1, 2, 3, 4
    heading_sizes = sorted(
        {sz for sz in size_counter if sz > body_size},
        reverse=True,
    )[:_MAX_HEADING_LEVELS]
    size_to_level: dict[float, int] = {
        sz: lvl + 1 for lvl, sz in enumerate(heading_sizes)
    }

    # ── Pass 2: group words into lines, tag headings ───────────────────────────
    structured_pages: list[list[str]] = []

    for i, words in enumerate(raw_pages):
        if not words:
            structured_pages.append([])
            page_line_sets.append(set())
            continue

        # Group by rounded top-y coordinate (same baseline = same line)
        line_map: dict[float, list[dict]] = {}
        for w in words:
            key = round(float(w.get("top") or 0), 0)
            line_map.setdefault(key, []).append(w)

        page_lines: list[str] = []
        for _, line_words in sorted(line_map.items()):
            text = " ".join(w["text"] for w in line_words).strip()
            if not text:
                continue
            max_sz = _round1(max(
                float(w.get("size") or 0) for w in line_words
            ))
            level = size_to_level.get(max_sz)
            if level and _is_heading_candidate(text):
                page_lines.append(f"{'#' * level} {text}")
            else:
                page_lines.append(text)

        structured_pages.append(page_lines)
        page_line_sets.append({ln.lstrip("#").strip() for ln in page_lines})
        # Attach this page's Markdown tables at the end of the page
        if i < len(raw_tables) and raw_tables[i]:
            for md_tbl in raw_tables[i]:
                structured_pages[-1].append("")
                structured_pages[-1].append(md_tbl)

    # ── Pass 3: suppress running headers/footers ──────────────────────────────
    n_pages   = len(structured_pages)
    min_pages = max(_RUNNING_HDR_MIN_PAGES, int(n_pages * _RUNNING_HDR_RATIO))

    line_freq: Counter[str] = Counter()
    for line_set in page_line_sets:
        for ln in line_set:
            line_freq[ln] += 1

    boilerplate: set[str] = {ln for ln, cnt in line_freq.items() if cnt >= min_pages}

    # ── Assemble final output ─────────────────────────────────────────────────
    for page_lines in structured_pages:
        filtered = [
            ln for ln in page_lines
            if ln.lstrip("#").strip() not in boilerplate
        ]
        if filtered:
            all_lines.extend(filtered)
            all_lines.append("")   # blank line between pages

    return "\n".join(all_lines)


def _is_heading_candidate(text: str) -> bool:
    """Shape check: short, no trailing punctuation, not too many words."""
    if _TERMINAL_PUNCT_RE.search(text):
        return False
    if len(text.split()) > _MAX_HEADING_WORDS:
        return False
    letters = sum(c.isalpha() for c in text)
    if letters < 3:
        return False
    return True


class PDFLoader(BaseLoader):
    """
    Extracts structured text from a PDF using pdfplumber.

    Font-size metadata is used to emit Markdown heading markers (# / ## / ###)
    so the heading tree parser receives unambiguous structure signals rather
    than having to guess from indentation (which DocumentProcessor collapses).

    Falls back to plain pdfplumber text extraction if font-size data is absent.
    Raises ImportError if pdfplumber is not installed.
    """

    def get_supported_extensions(self) -> list[str]:
        return [".pdf"]

    def load(self, source: str, **kwargs) -> Document:
        self.validate_file(source)
        path = Path(source)

        try:
            content = _extract_with_pdfplumber(path)
            logger.info("PDF loaded via pdfplumber: %s", path.name)
        except ImportError:
            raise RuntimeError(
                "pdfplumber is required for PDF loading. "
                "Run: pip install pdfplumber"
            )

        # Strip generic CLI/REST command-reference dumps.
        try:
            from src.config.settings import get_settings
            from src.services.ingestion.cleaners import analyze_command_reference
            s = get_settings()
            if getattr(s, "strip_command_reference", True):
                content, stats = analyze_command_reference(
                    content,
                    density_threshold=getattr(s, "command_ref_density", 0.6),
                    min_block_lines=getattr(s, "command_ref_min_lines", 3),
                )
                if stats.blocks_dropped or stats.lines_dropped:
                    logger.info(
                        "PDF command-reference stripped: %s  blocks=%d  lines=%d",
                        path.name, stats.blocks_dropped, stats.lines_dropped,
                    )
        except Exception as exc:
            logger.warning("command-reference stripping skipped for %s: %s", path.name, exc)

        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=path.stem,
                source_type=SourceType.PDF,
                original_filename=path.name,
            ),
        )
