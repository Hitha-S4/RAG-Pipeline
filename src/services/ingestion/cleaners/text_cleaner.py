"""
Text cleaner — removes/normalises unwanted non-ASCII data.

Strategy (lossless-first):
    1. NFKC normalisation (folds ligatures ﬁ→fi, full-width chars, etc.)
    2. Transliterate common typographic Unicode to ASCII equivalents
       (smart quotes, dashes, bullets, arrows, ellipsis, NBSP …)
    3. NFKD accent stripping for Latin letters (é→e, ü→u)
    4. Drop any byte still outside printable ASCII (replaced with ' ')

Pure function, format-agnostic — runs for PDF, HTML, or Markdown alike.
"""
from __future__ import annotations

import re
import unicodedata

# Typographic Unicode → ASCII transliteration map.
# Applied BEFORE the final strip so meaning is preserved, not deleted.
_TRANSLITERATE: dict[int, str] = {ord(k): v for k, v in {
    # quotes / apostrophes
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u201f": '"',
    "\u2032": "'", "\u2033": '"', "\u00ab": '"', "\u00bb": '"',
    # dashes / hyphens / minus
    "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-",
    "\u2014": "-", "\u2015": "-", "\u2212": "-",
    # spaces
    "\u00a0": " ", "\u2002": " ", "\u2003": " ", "\u2007": " ",
    "\u2009": " ", "\u200a": " ", "\u202f": " ", "\u3000": " ",
    # invisible / zero-width — delete outright
    "\u200b": "", "\u200c": "", "\u200d": "", "\ufeff": "",
    "\u00ad": "",                       # soft hyphen (PDF line-break artefact)
    # bullets / list markers
    "\u2022": "-", "\u2023": "-", "\u25aa": "-", "\u25cf": "-",
    "\u25e6": "-", "\u2043": "-", "\u00b7": "-",
    # ellipsis, arrows, misc symbols
    "\u2026": "...",
    "\u2192": "->", "\u2190": "<-", "\u21d2": "=>", "\u21d0": "<=",
    "\u00d7": "x",  "\u00f7": "/",
    "\u00a9": "(c)", "\u00ae": "(R)", "\u2122": "(TM)",
    "\u00b0": " deg", "\u2264": "<=", "\u2265": ">=", "\u2260": "!=",
    "\u2713": "[x]", "\u2714": "[x]", "\u2717": "[ ]",
}.items()}

# Anything left outside printable ASCII + \n \t after transliteration
_RE_NON_ASCII = re.compile(r"[^\x20-\x7e\n\t]")
_RE_MULTI_SP  = re.compile(r"[ \t]{2,}")


def to_ascii(text: str) -> str:
    """
    Clean unwanted non-ASCII data from `text`, preserving meaning where a
    safe ASCII equivalent exists and dropping the rest.
    """
    # 1. compatibility normalisation (ligatures, full-width forms)
    text = unicodedata.normalize("NFKC", text)
    # 2. transliterate known typographic characters
    text = text.translate(_TRANSLITERATE)
    # 3. strip accents from Latin letters (é → e)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    # 4. hard-drop anything still non-ASCII (CJK, emoji, control leftovers)
    text = _RE_NON_ASCII.sub(" ", text)
    # do NOT collapse leading indentation (heading_tree depends on it) —
    # only collapse runs that appear after a non-space character
    lines = []
    for line in text.splitlines():
        n = len(line) - len(line.lstrip(" \t"))
        lines.append(line[:n] + _RE_MULTI_SP.sub(" ", line[n:]))
    return "\n".join(lines)


def non_ascii_ratio(text: str) -> float:
    """Diagnostic: fraction of characters that are non-ASCII (before cleaning)."""
    if not text:
        return 0.0
    return sum(1 for ch in text if ord(ch) > 126) / len(text)
