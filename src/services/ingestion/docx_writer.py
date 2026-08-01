"""
DOCX writer — renders the extracted knowledge base as a Word deliverable.

Completely product-independent: it reads whatever the LLM extracted (six
categories, sub-types, relations, summaries) and lays it out. No document,
product, or vendor is referenced anywhere in this module.

Layout
──────
    Title            <product_name> — Knowledge Base
    Overview         block counts per category / sub-type
    Per category     KNOWLEDGE, FEATURES, WORKFLOWS, ENTITIES, KEYWORDS, PERSONAS
      ## Name        (Heading 2)
      summary        (italic)
      content        (body; numbered steps and bullets preserved)
      Related:       relation names, so the reader can follow the graph

Keywords render as a two-column table (Term | Definition) since they are
one-liners; every other category renders as prose sections.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document as DocxDocument
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

from src.enums import ChunkCategory
from src.models import Chunk
from src.utils.logging import get_logger

logger = get_logger(__name__)

# Presentation order — overview first, then capability, then procedure, then reference.
_ORDER = [
    ChunkCategory.KNOWLEDGE,
    ChunkCategory.FEATURES,
    ChunkCategory.WORKFLOWS,
    ChunkCategory.ENTITIES,
    ChunkCategory.KEYWORDS,
    ChunkCategory.PERSONAS,
]

_BULLET_RE = re.compile(r"^\s*[-*+]\s+(.*)$")
_NUMBER_RE = re.compile(r"^\s*(\d+)[.)]\s+(.*)$")
_HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.*)$")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def _add_rich(doc: DocxDocument, text: str, style: str | None = None) -> None:
    """Add a paragraph, rendering **bold** spans as real bold runs."""
    p = doc.add_paragraph(style=style)
    for i, part in enumerate(_BOLD_RE.split(text)):
        if not part:
            continue
        run = p.add_run(part)
        run.bold = i % 2 == 1          # odd indices are the captured bold groups
    return p


def _render_markdown_body(doc: DocxDocument, body: str) -> None:
    """Render a markdown content body into Word paragraphs.

    Handles headings, bullets, numbered steps and plain paragraphs. Anything
    unrecognised falls through as body text — never dropped.
    """
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if (m := _HEADING_RE.match(line)):
            _add_rich(doc, m.group(1), style="Heading 3")
        elif (m := _NUMBER_RE.match(line)):
            _add_rich(doc, m.group(2), style="List Number")
        elif (m := _BULLET_RE.match(line)):
            _add_rich(doc, m.group(1), style="List Bullet")
        else:
            _add_rich(doc, line)


def _relations(chunk: Chunk) -> str:
    """Flatten a chunk's relation facets into a single 'Related:' line."""
    pairs = (
        ("Keywords", chunk.keywords), ("Features", chunk.features),
        ("Workflows", chunk.workflows), ("Personas", chunk.personas),
        ("Entities", chunk.entities),
    )
    parts = [f"{label}: {', '.join(vals)}" for label, vals in pairs if vals]
    return " · ".join(parts)


def _blocks_only(chunks: list[Chunk]) -> list[Chunk]:
    """Keep the LLM-extracted blocks; drop the recursive leaf pieces.

    Recursive pieces are splits of a parent block's content — including them
    would duplicate every long section in the document.
    """
    return [c for c in chunks if not _is_recursive_piece(c)]


def _is_recursive_piece(c: Chunk) -> bool:
    heads = c.metadata.headings or []
    return bool(heads) and heads[-1].startswith("part-")


def write_docx(chunks: list[Chunk], out_path: Path, product_name: str) -> Path:
    """Render the extracted knowledge base to `out_path` and return it."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    blocks = _blocks_only(chunks)

    by_cat: dict[ChunkCategory, list[Chunk]] = defaultdict(list)
    for c in blocks:
        by_cat[c.metadata.chunk_type].append(c)

    doc = DocxDocument()
    doc.styles["Normal"].font.size = Pt(10.5)

    title = doc.add_heading(f"{product_name} — Knowledge Base", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Overview ────────────────────────────────────────────────────────────
    doc.add_heading("Overview", level=1)
    doc.add_paragraph(
        f"Extracted {len(blocks)} blocks across {len(by_cat)} categories."
    )
    table = doc.add_table(rows=1, cols=2)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    hdr[0].text, hdr[1].text = "Category", "Blocks"
    for cat in _ORDER:
        if by_cat.get(cat):
            row = table.add_row().cells
            row[0].text = cat.value.title()
            row[1].text = str(len(by_cat[cat]))

    subs = Counter(c.metadata.sub_type for c in blocks if c.metadata.sub_type)
    if subs:
        doc.add_paragraph()
        _add_rich(doc, "**Sub-types:** " + ", ".join(
            f"{k} ({v})" for k, v in subs.most_common()))

    # ── One section per category ────────────────────────────────────────────
    for cat in _ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        doc.add_page_break()
        doc.add_heading(cat.value.title(), level=1)

        items.sort(key=lambda c: (c.metadata.headings or [""])[0].lower())

        # Keywords are one-liners — a glossary table reads far better than prose.
        if cat is ChunkCategory.KEYWORDS:
            kt = doc.add_table(rows=1, cols=2)
            kt.style = "Light Grid Accent 1"
            head = kt.rows[0].cells
            head[0].text, head[1].text = "Term", "Definition"
            for c in items:
                cells = kt.add_row().cells
                cells[0].text = (c.metadata.headings or ["—"])[0]
                cells[1].text = (c.summary or c.content).strip()
            continue

        for c in items:
            name = (c.metadata.headings or ["Untitled"])[0]
            doc.add_heading(name, level=2)

            if c.metadata.sub_type:
                p = doc.add_paragraph()
                r = p.add_run(c.metadata.sub_type)
                r.italic = True
                r.font.size = Pt(9)

            if c.summary:
                p = _add_rich(doc, c.summary)
                for r in p.runs:
                    r.italic = True

            if c.content and c.content.strip() != (c.summary or "").strip():
                _render_markdown_body(doc, c.content)

            if (rel := _relations(c)):
                p = _add_rich(doc, f"**Related** — {rel}")
                for r in p.runs:
                    r.font.size = Pt(9)

    doc.save(str(out_path))
    logger.info("DOCX written: %s (%d blocks)", out_path, len(blocks))
    return out_path
