"""
Command / API-reference stripper — generic and data-source independent.

Problem (requirement 7)
───────────────────────
Product manuals bury huge CLI / REST *command-reference* chapters inside the
prose (in the GDP docs this is the "GuardAPI and REST API commands" chapter with
~850 ``grdapi <cmd> param=value`` lines).  These command dumps are noise for a
persona / feature / workflow knowledge base: they wreck chunking, dominate the
vocabulary, and pollute retrieval.

Approach (requirement 8 — NOT data-source specific)
───────────────────────────────────────────────────
We never look for the word "grdapi" or any product name.  Instead we detect the
*shape* of command-reference content:

    • CLI invocation lines — a leading command token followed by two or more
      ``key=value`` assignments               e.g.  ``foo create x=1 y=2``
    • REST request lines   — an HTTP verb + path e.g.  ``POST /api/v1/things``
    • assignment-dense lines — mostly ``key=value`` pairs

Then two independent, individually-toggleable passes run:

    1. BLOCK pass  — split the text into blank-line-delimited blocks; drop any
      block whose command-line density ≥ ``density_threshold`` and which has at
      least ``min_block_lines`` lines.  This removes whole reference sections
      (the heading line riding just above such a block is dropped too when it
      looks like a reference heading — "… commands", "… API", "CLI", "syntax").

    2. LINE pass   — drop any remaining standalone command lines scattered
      through otherwise-prose blocks.

Both passes are conservative: a paragraph that merely *mentions* a command in
running prose stays, because a single command token inside a sentence does not
reach the density bar.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from src.services.ingestion.cleaners.command_patterns import (
    REST_CALL, SYNTAX_SECTION, is_command_line as _is_command_line,
)

# ── Line-shape detectors ──────────────────────────────────────────────────────

# key=value assignment (value may be quoted / contain most non-space chars)
_ASSIGN_RE = re.compile(r"""[A-Za-z_][\w.\-]*=(?:"[^"]*"|'[^']*'|\S+)""")

# REST request line:  VERB /path...
_REST_RE = re.compile(r"^\s*(?:GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s+/\S+", re.IGNORECASE)

# CLI invocation:  a leading lowercase-ish command token, then the rest of the line.
# Kept generic — any single leading token made of letters/digits/_/-  (no spaces).
_LEADING_TOKEN_RE = re.compile(r"^\s*([A-Za-z][\w\-]*)\b(.*)$")

# Reference-style heading hint (used only to also drop the heading above a dump).
_REF_HEADING_RE = re.compile(
    r"(?:command(?:s|\s+reference)?|rest\s*api|\bapi\b|\bcli\b|syntax|parameter\s+list|reference)\s*$",
    re.IGNORECASE,
)

_MIN_ASSIGNMENTS = 2   # a CLI line needs at least this many key=value pairs


def is_command_line(line: str) -> bool:
    """
    True when *line* looks like a CLI invocation or a REST request — the shapes
    that make up a command-reference dump. Generic: no product tokens involved.
    """
    s = line.strip()
    if not s:
        return False

    if _REST_RE.match(s):
        return True

    assignments = _ASSIGN_RE.findall(s)
    if len(assignments) >= _MIN_ASSIGNMENTS:
        # Prose rarely stacks 2+ key=value pairs; a command line almost always does.
        # Extra guard: require a leading command-like token (no sentence
        # punctuation before the first assignment) to avoid nuking prose that
        # happens to contain "a=1 and b=2".
        m = _LEADING_TOKEN_RE.match(s)
        if m and "." not in m.group(1) and "," not in s.split("=")[0]:
            return True

    return False


def _is_reference_heading(line: str) -> bool:
    s = line.strip().strip("#").strip()
    # Headings are short; a full sentence ending in "API." is not a heading.
    if not s or len(s) > 80 or s.endswith((".", "!", "?")):
        return False
    return bool(_REF_HEADING_RE.search(s))


# ── Stats container ───────────────────────────────────────────────────────────

@dataclass
class CommandReferenceStats:
    total_lines:          int = 0
    command_lines:        int = 0
    blocks_total:         int = 0
    blocks_dropped:       int = 0
    lines_dropped_block:  int = 0
    lines_dropped_single: int = 0
    headings_dropped:     int = 0

    @property
    def lines_dropped(self) -> int:
        return self.lines_dropped_block + self.lines_dropped_single


# ── Core ──────────────────────────────────────────────────────────────────────

def _block_density(block_lines: list[str]) -> float:
    non_empty = [ln for ln in block_lines if ln.strip()]
    if not non_empty:
        return 0.0
    cmd = sum(1 for ln in non_empty if is_command_line(ln))
    return cmd / len(non_empty)


def analyze_command_reference(
    text: str,
    *,
    density_threshold: float = 0.6,
    min_block_lines: int = 3,
    drop_command_blocks: bool = True,
    drop_command_lines: bool = True,
    drop_reference_headings: bool = True,
) -> tuple[str, CommandReferenceStats]:
    """
    Strip command-reference content from *text* and return ``(cleaned, stats)``.

    Parameters mirror :func:`strip_command_reference`; this variant also returns
    a :class:`CommandReferenceStats` so callers can log how much was removed.
    """
    stats = CommandReferenceStats()
    if not text:
        return text, stats

    lines = text.splitlines()
    stats.total_lines   = len(lines)
    stats.command_lines = sum(1 for ln in lines if is_command_line(ln))

    # Partition into blank-line-delimited blocks, remembering separators so we
    # can rebuild the text faithfully.
    blocks: list[list[str]] = []
    current: list[str] = []
    for ln in lines:
        if ln.strip() == "":
            blocks.append(current)
            current = []
        else:
            current.append(ln)
    blocks.append(current)
    stats.blocks_total = sum(1 for b in blocks if b)

    kept_blocks: list[list[str]] = []
    prev_was_ref_heading_index: int | None = None

    for block in blocks:
        if not block:
            kept_blocks.append(block)
            continue

        is_dense = (
            drop_command_blocks
            and len(block) >= min_block_lines
            and _block_density(block) >= density_threshold
        )

        if is_dense:
            stats.blocks_dropped += 1
            stats.lines_dropped_block += len([ln for ln in block if ln.strip()])
            # Drop a reference-style heading sitting immediately above this dump.
            if (
                drop_reference_headings
                and kept_blocks
                and len(kept_blocks[-1]) == 1
                and _is_reference_heading(kept_blocks[-1][0])
            ):
                kept_blocks.pop()
                stats.headings_dropped += 1
            continue

        # Not a dense dump — optionally scrub individual stray command lines.
        if drop_command_lines:
            scrubbed = [ln for ln in block if not is_command_line(ln)]
            stats.lines_dropped_single += len(block) - len(scrubbed)
            block = scrubbed

        if block:
            kept_blocks.append(block)

    # Rebuild, collapsing runs of >2 blank lines that dropping may have created.
    out_lines: list[str] = []
    for i, block in enumerate(kept_blocks):
        if block:
            out_lines.extend(block)
            out_lines.append("")  # block separator
    cleaned = "\n".join(out_lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned, stats


def strip_command_reference(text: str, **kwargs) -> str:
    """Convenience wrapper returning only the cleaned text (see analyze_*)."""
    cleaned, _ = analyze_command_reference(text, **kwargs)
    return cleaned


# ── Reference-entry removal (requirement 7), data-source independent ─────────

def is_reference_block(block: list[str]) -> bool:
    """
    A block belongs to a command/API REFERENCE entry.

    Evidence required is deliberately strong — a syntax heading ("GuardAPI
    syntax", "REST API syntax") or a REST call line. A single inline command is
    NOT enough, because prose blocks often embed one worked example and we must
    not delete the surrounding workflow text.

    Shape-based only: no product nouns, so this works on any vendor's manual.
    """
    return any(SYNTAX_SECTION.match(l) or REST_CALL.search(l) for l in block)


def strip_reference_entries(text: str) -> tuple[str, int]:
    """Drop every blank-line-delimited block that is a reference entry."""
    blocks, cur = [], []
    for line in text.splitlines():
        if line.strip():
            cur.append(line)
        else:
            blocks.append(cur); cur = []
    blocks.append(cur)

    kept, dropped = [], 0
    for b in blocks:
        if b and is_reference_block(b):
            dropped += 1
        else:
            kept.append(b)
    out = "\n\n".join("\n".join(b) for b in kept if b)
    return out, dropped
