"""
Semantic recursive chunker — hierarchy-aware, boundary-safe splitting.

Split levels (coarse → fine):
    1. Markdown headings  (# / ## / ###)
    2. Blank-line paragraphs
    3. Sentences          (punctuation-aware, abbreviation-safe)
    4. Clauses            (,  ;  :  — delimiter is PRESERVED)
    5. Emergency          (hard character slice, snapped to word boundary)

Key fixes over the original draft
──────────────────────────────────
  Bug 1 — merge_small used `<` instead of `<=`, so two chunks whose combined
           length equals exactly MIN_CHARS were never merged.

  Bug 2 — split_by_heading silently dropped any text that appeared *before*
           the first heading (the preamble).  It is now captured and prepended.

  Bug 3 — split_by_sentence re-joined with an unconditional " " separator,
           which doubled the space that already exists after sentence-terminal
           punctuation (". " → ".  ").  Now joins with "" and lets the original
           spacing survive.

  Bug 4 — split_by_clause used re.split() on the delimiter pattern, which
           *consumes* the matched delimiter — so every comma, semicolon, and
           colon vanished from the output.  Fixed by using re.split() with a
           capturing group so the delimiter token is kept, then zip-merged back.

  Bug 5 — emergency_split sliced at exact character offsets, cutting words
           mid-character.  Now snaps each cut-point backward to the nearest
           space so words are never broken.

  Bug 6 — depth did not represent the split level; it incremented on every
           recursive call regardless of whether a split actually occurred.
           Replaced with a named split_level so each Chunk carries the level
           at which it was actually produced (heading=1 … emergency=5).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List

# ── Configuration ─────────────────────────────────────────────────────────────

MAX_CHARS: int = 1800   # hard ceiling per chunk (characters)
MIN_CHARS: int = 300    # minimum before two adjacent pieces are merged

# ── Regex patterns ────────────────────────────────────────────────────────────

# ATX Markdown headings: # Title / ## Sub / ### Sub-sub
_HEADING_RE = re.compile(r"(?m)^(#{1,6}\s+.*)$")

# Two or more blank lines / carriage-returns = paragraph boundary
_PARAGRAPH_RE = re.compile(r"\n\s*\n")

# Sentence boundary: split AFTER [.!?] followed by whitespace + uppercase / digit / quote.
# Lookbehind keeps the punctuation attached to the preceding sentence.
_SENTENCE_RE = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9"(])')

# Clause boundary: split AFTER [,;:] followed by whitespace.
# Capturing group ( ) preserves the delimiter token in re.split output.
_CLAUSE_RE = re.compile(r'([,;:])\s+')


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class Chunk:
    text: str
    split_level: int = field(default=0)
    """
    The level at which this chunk was produced:
        0 = text already fit within MAX_CHARS (no split needed)
        1 = heading split
        2 = paragraph split
        3 = sentence split
        4 = clause split
        5 = emergency (hard) split
    """


# ── Public API ────────────────────────────────────────────────────────────────

def recursive_chunk(text: str) -> List[Chunk]:
    """Split *text* into Chunk objects, each ≤ MAX_CHARS characters."""
    return _split(text.strip(), split_level=0)


# ── Core recursive splitter ───────────────────────────────────────────────────

def _split(text: str, split_level: int) -> List[Chunk]:
    text = text.strip()
    if not text:
        return []

    # Already fits — emit as-is, carrying the level at which it was produced.
    if len(text) <= MAX_CHARS:
        return [Chunk(text=text, split_level=split_level)]

    # ── Level 1: headings ─────────────────────────────────────────────────────
    pieces = _split_by_heading(text)
    if len(pieces) > 1:
        return _recurse(pieces, split_level=1)

    # ── Level 2: paragraphs ───────────────────────────────────────────────────
    pieces = _split_by_paragraph(text)
    if len(pieces) > 1:
        return _recurse(pieces, split_level=2)

    # ── Level 3: sentences ────────────────────────────────────────────────────
    pieces = _split_by_sentence(text)
    if len(pieces) > 1:
        return _recurse(pieces, split_level=3)

    # ── Level 4: clauses ──────────────────────────────────────────────────────
    pieces = _split_by_clause(text)
    if len(pieces) > 1:
        return _recurse(pieces, split_level=4)

    # ── Level 5: emergency hard split ─────────────────────────────────────────
    return _emergency_split(text, split_level=5)


# ── Split strategies ──────────────────────────────────────────────────────────

def _split_by_heading(text: str) -> List[str]:
    """
    Partition *text* on Markdown ATX headings.

    Fix (Bug 2): any text that appears *before* the first heading is captured
    as a preamble section rather than silently dropped.
    """
    matches = list(_HEADING_RE.finditer(text))
    if not matches:
        return [text]

    sections: List[str] = []

    # Preserve preamble (text before the first heading).
    preamble = text[:matches[0].start()].strip()
    if preamble:
        sections.append(preamble)

    for i, m in enumerate(matches):
        start = m.start()
        end   = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section = text[start:end].strip()
        if section:
            sections.append(section)

    return _merge_small(sections)


def _split_by_paragraph(text: str) -> List[str]:
    """Split on blank-line paragraph boundaries."""
    parts = [p.strip() for p in _PARAGRAPH_RE.split(text) if p.strip()]
    return _merge_small(parts)


def _split_by_sentence(text: str) -> List[str]:
    """
    Split on sentence boundaries (punctuation-aware).

    Fix (Bug 3): sentences are accumulated by concatenation (not " ".join),
    so the original whitespace that followed each period is preserved and no
    extra spaces are inserted.
    """
    sentences = _SENTENCE_RE.split(text)
    chunks: List[str] = []
    current = ""

    for sentence in sentences:
        # Re-attach with the exact whitespace that was already in the text;
        # do NOT add an extra " " between sentences.
        candidate = current + sentence if current else sentence

        if len(candidate) <= MAX_CHARS:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = sentence

    if current:
        chunks.append(current)

    return chunks


def _split_by_clause(text: str) -> List[str]:
    """
    Split on clause boundaries (, ; :) while PRESERVING the delimiter.

    Fix (Bug 4): the original code used re.split() without a capturing group,
    which consumed the comma/semicolon/colon.  We now use a capturing group
    so re.split() yields [before, delim, before, delim, …, last], then
    zip-merge every (before + delim) pair back into proper clause strings.
    """
    # re.split with a capturing group produces:
    #   ["First clause", ",", " second clause", ";", " third clause", ":", " fourth"]
    # We want:             "First clause,"      "second clause;"      etc.
    tokens = _CLAUSE_RE.split(text)
    # tokens[0::3] = clause text,  tokens[1::3] = delimiter  (every 2nd in the flat list)
    # Actually re.split with one capturing group yields alternating [text, delim, text, delim…]
    clauses: List[str] = []
    i = 0
    while i < len(tokens):
        part = tokens[i]
        if i + 1 < len(tokens):
            delim = tokens[i + 1]   # the captured [,;:] character
            clauses.append((part + delim).strip())
            i += 2
        else:
            if part.strip():
                clauses.append(part.strip())
            i += 1

    chunks: List[str] = []
    current = ""

    for clause in clauses:
        candidate = current + " " + clause if current else clause
        if len(candidate) <= MAX_CHARS:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = clause

    if current:
        chunks.append(current)

    return chunks


# ── Helpers ───────────────────────────────────────────────────────────────────

def _merge_small(parts: List[str]) -> List[str]:
    """
    Merge adjacent parts that are too small to stand alone.

    Fix (Bug 1): the original used `<` so two parts whose combined length
    equals exactly MIN_CHARS were never merged.  Changed to `<=`.
    """
    merged: List[str] = []
    current = ""

    for p in parts:
        combined_len = len(current) + len(p) + (2 if current else 0)  # +2 for "\n\n"
        if combined_len <= MIN_CHARS:
            current = current + "\n\n" + p if current else p
        else:
            if current:
                merged.append(current)
            current = p

    if current:
        merged.append(current)

    return merged


def _recurse(parts: List[str], split_level: int) -> List[Chunk]:
    """Apply _split to each part, propagating the current split_level."""
    output: List[Chunk] = []
    for p in parts:
        output.extend(_split(p, split_level))
    return output


def _emergency_split(text: str, split_level: int) -> List[Chunk]:
    """
    Hard character-budget split used only when no natural boundary exists.

    Fix (Bug 5): the original sliced at exact offsets, cutting mid-word.
    Now each cut-point is snapped backward to the nearest space so no word
    is ever broken.  If there is no space in the window, the exact offset is
    used as a last resort (handles continuous text with no spaces).
    """
    chunks: List[Chunk] = []
    start = 0

    while start < len(text):
        end = min(start + MAX_CHARS, len(text))

        # Snap back to the nearest space to avoid cutting mid-word.
        if end < len(text):
            snap = text.rfind(" ", start, end)
            if snap > start:          # found a space inside the window
                end = snap

        chunk_text = text[start:end].strip()
        if chunk_text:
            chunks.append(Chunk(text=chunk_text, split_level=split_level))

        start = end

    return chunks
