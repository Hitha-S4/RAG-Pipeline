"""
Document processor — cleans and normalises raw document content before chunking.

Steps performed:
    1. Unicode normalisation (NFKC)
    2. Whitespace / control-character cleanup
    3. Strip isolated page-number lines (common in PDF extracts)
    4. Paragraph de-duplication
    5. Strip Table-of-Contents sections (TOC entries are noise for retrieval)
    6. Populates Document.cleaned_content
"""
from __future__ import annotations

import re
import unicodedata
from collections import OrderedDict

from src.models import Document
from src.services.ingestion.cleaners import non_ascii_ratio, to_ascii
from src.utils.logging import get_logger

logger = get_logger(__name__)

_RE_PAGE_NUM   = re.compile(r"(?m)^\s*\d{1,4}\s*$")
_RE_MULTI_NL   = re.compile(r"\n{3,}")
_RE_HORIZ_RULE = re.compile(r"^[-=_]{4,}\s*$", re.MULTILINE)
_RE_CTRL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

# Matches a heading line that declares a table of contents section.
_RE_TOC_HEADING = re.compile(
    r"^#+\s*(?:tables?\s+of\s+contents?|contents?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def _normalise(text: str) -> str:
    """Unicode NFKC normalisation + control-char removal."""
    text = unicodedata.normalize("NFKC", text)
    text = _RE_CTRL_CHARS.sub("", text)
    return text


def _clean_whitespace(text: str) -> str:
    # RC2 fix: collapse inline whitespace LINE BY LINE so leading indentation
    # is preserved.  The old single-pass `re.sub(r"[ \t]+", " ", text)`
    # collapsed every multi-space run including the leading indent that
    # heading_tree._detect_titlecase uses to infer heading depth, producing
    # a document where every heading appeared at indent 1 and the tree had
    # zero edges.
    lines = []
    for line in text.splitlines():
        stripped_leading = len(line) - len(line.lstrip(" \t"))
        indent = line[:stripped_leading]           # preserve original indent
        body   = re.sub(r"[ \t]+", " ", line[stripped_leading:])  # collapse body only
        lines.append(indent + body)
    text = "\n".join(lines)
    text = _RE_PAGE_NUM.sub("", text)             # drop bare page numbers
    text = _RE_HORIZ_RULE.sub("", text)           # drop decorative rules
    text = _RE_MULTI_NL.sub("\n\n", text)         # collapse blank lines
    return text.strip()


def _dedup_paragraphs(text: str) -> str:
    """Remove exact duplicate paragraphs (common in PDF header/footer repeats)."""
    paragraphs = re.split(r"\n\n+", text)
    seen: OrderedDict[str, None] = OrderedDict()
    for p in paragraphs:
        key = p.strip()
        if key:
            seen[key] = None
    return "\n\n".join(seen.keys())


def _strip_toc_sections(text: str) -> str:
    """Remove Table-of-Contents sections from PDF-extracted text.

    Strategy: scan for a heading that names a TOC section (e.g. "# Tables of
    Contents").  Once found, consume ALL lines until the next heading (any line
    starting with '#') is reached.  The TOC heading line itself is also dropped.

    This handles PDFs where the TOC entries may be:
      • "Title words  42"   (with space-padded page number)
      • "Title words"       (page number collapsed away after whitespace normalisation)
    Both forms produce short, valueless chunks after recursive chunking, so the
    safest rule is: drop the entire block.

    Multiple TOC sections (some PDFs have one per chapter) are all removed.
    """
    lines   = text.split("\n")
    out     = []
    in_toc  = False
    dropped = 0

    for line in lines:
        stripped = line.strip()
        # Entering a TOC section: suppress the heading line itself.
        if _RE_TOC_HEADING.match(stripped):
            in_toc = True
            dropped += 1
            continue
        if in_toc:
            # The next non-blank heading ends the TOC section — emit it.
            if stripped.startswith("#"):
                in_toc = False
                out.append(line)
            else:
                dropped += 1
            continue
        out.append(line)

    if dropped:
        logger.info("Stripped %d TOC lines from document", dropped)
    return "\n".join(out)


class DocumentProcessor:
    """
    Stateless processor that cleans a Document's content and returns it
    with Document.cleaned_content populated.
    """

    def process(self, document: Document) -> Document:
        raw = document.content
        ratio = non_ascii_ratio(raw)
        text = to_ascii(raw)               # step 0: clean unwanted non-ASCII data
        if ratio > 0:
            logger.info("doc_id=%s non-ASCII ratio=%.4f cleaned to ASCII",
                        document.doc_id, ratio)
        text = _normalise(text)
        text = _clean_whitespace(text)
        text = _dedup_paragraphs(text)
        text = _strip_toc_sections(text)   # remove TOC noise before chunking

        document.cleaned_content = text
        logger.info(
            "Processed doc_id=%s  raw_chars=%d  clean_chars=%d",
            document.doc_id, len(raw), len(text),
        )
        return document
