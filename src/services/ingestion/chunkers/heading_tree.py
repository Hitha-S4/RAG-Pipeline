"""
Heading-tree parser — pure-Python, dependency-free.

Builds a properly nested N-level tree of headings from a document.

────────────────────────────────────────────────────────────────────────────────
WHY THIS WAS REWRITTEN  (the bug that wrecked retrieval quality)
────────────────────────────────────────────────────────────────────────────────
The previous version used a naive ATX rule and STRICT PRECEDENCE:
"markdown headings win; only if there are none, fall back to structure".

On PDF-derived text that is catastrophic, because '#' constantly appears in
content that is NOT a heading:

    # Verify API key exists                  <- a shell comment
    # Skips registry certificate install...  <- a YAML comment
    ##### Report Title #####                 <- literal sample output
    # Number sign                            <- the docs DESCRIBING the '#' char
    # of Licenses  This value indicates ...  <- '#' used as "number of"

Measured on the real corpus this produced **173 distinct "headings" for 6,437
chunks**, the most common being "Number sign" (1,918 chunks). Worse: those few
junk '#' matches satisfied the "markdown found" test, so the structural fallback
NEVER RAN and the ~800 genuine chapter titles ("Configuring the alerter",
"Managing correlation alerts") were lost entirely.

Every chunk then carried a wrong breadcrumb, poisoning parent context, the
summaries built from it, and ultimately retrieval.

THE FIX — three layers
  1. MASK CODE first  — fenced/indented/shell/YAML lines are blanked before any
     heading matching happens.
  2. VALIDATE candidates — a heading is short, title-ish, has no trailing
     sentence punctuation, no shell metacharacters, no key=value, and is not a
     TOC/table row (column gaps, trailing page number).
  3. ADAPTIVE SOURCE SELECTION, not blind precedence — each detector is SCORED
     on how plausible its output is (count x distinctness), and the best wins.
     A doc with 5 markdown hits and 800 title-case hits is a title-case doc.

All rules are shape-based and product-agnostic (no product nouns anywhere).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_MAX_LEVEL = 6
_MAX_HEADING_CHARS = 90


# ── Layer 1: mask code so it can never be mistaken for structure ──────────────

_FENCE_RE = re.compile(r"^\s*(?:```|~~~)")

_CODE_ISH_RE = re.compile(
    r"""
      [|;{}<>]                       # shell pipes, redirects, braces
    | \$\w                           # $VAR
    | \w+\s*=\s*\S                   # key=value
    | ^\s*(?:sudo|cd|ls|ps|grep|awk|sed|cat|echo|export|chmod|chown|kubectl|docker|helm|curl|wget|systemctl)\b
    | ^\s*/                          # absolute path
    | \.(?:sh|py|ini|yaml|yml|conf|log|jar|tgz|crt|pem)\b
    """,
    re.VERBOSE | re.IGNORECASE,
)


def mask_code_lines(text: str) -> list[str]:
    """Return lines with code-ish lines blanked (offsets preserved)."""
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        if re.match(r"^(?: {4,}|\t)\S", line) and _CODE_ISH_RE.search(line):
            out.append("")
            continue
        out.append(line)
    return out


# ── Layer 2: validate a heading candidate ────────────────────────────────────

_TOC_ROW_RE          = re.compile(r"\S\s{2,}\S")
# A TOC page number is separated by a COLUMN GAP ("Installing patches      1058").
# Requiring the gap means a legitimate heading that merely ends in a digit
# ("Rule 11", "Configuring feature 2") is NOT thrown away.
_TRAILING_PAGENO_RE  = re.compile(r"\s{2,}\d{1,4}\s*$")
_COMMENT_VERB_RE = re.compile(
    r"^\s*(?:verify|skips?|hook|pass|define|set|use|run|optional|required|note|"
    r"should|must|add|remove|create|delete|enable|disable|check)\b",
    re.IGNORECASE,
)


def is_valid_heading(title: str, *, from_markdown: bool = False) -> bool:
    """Shape-check a heading candidate. Product-agnostic."""
    s = title.strip().strip("#").strip()
    if not s or not (3 <= len(s) <= _MAX_HEADING_CHARS):
        return False
    if s.endswith((".", ":", ";", "!", "?", ",")):
        return False
    if _CODE_ISH_RE.search(s):
        return False
    if _TOC_ROW_RE.search(s) or _TRAILING_PAGENO_RE.search(s):
        return False
    letters = sum(c.isalpha() for c in s)
    if letters < 3 or letters / len(s) < 0.5:
        return False
    if len(s.split()) > 12:
        return False
    if from_markdown and _COMMENT_VERB_RE.match(s):
        # '#' is heavily abused in code comments; demand non-imperative phrasing.
        return False
    return True


# ── Layer 3: detectors ───────────────────────────────────────────────────────

_MD_RE        = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$")
_NUMBERED_RE  = re.compile(r"^(\d+(?:\.\d+)+)\.?\s+(.+)$")
_TITLECASE_RE = re.compile(r"^([A-Z][\w\-/&()']*(?:\s+[\w\-/&()',]+){1,10})$")


@dataclass
class HeadingHit:
    line:  int
    title: str
    level: int


@dataclass
class HeadingNode:
    title:    str
    level:    int
    body:     str = ""
    children: list["HeadingNode"] = field(default_factory=list)

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


def _detect_markdown(lines: list[str]) -> list[HeadingHit]:
    hits = []
    for i, ln in enumerate(lines):
        m = _MD_RE.match(ln)
        if m and is_valid_heading(m.group(2), from_markdown=True):
            hits.append(HeadingHit(i, m.group(2).strip(), min(len(m.group(1)), _MAX_LEVEL)))
    return hits


def _detect_numbered(lines: list[str]) -> list[HeadingHit]:
    hits = []
    for i, ln in enumerate(lines):
        m = _NUMBERED_RE.match(ln)
        if m and is_valid_heading(m.group(2)):
            hits.append(HeadingHit(i, m.group(2).strip(),
                                   min(m.group(1).count(".") + 1, _MAX_LEVEL)))
    return hits


def _detect_titlecase(lines: list[str]) -> list[HeadingHit]:
    """
    Standalone Title-Case lines — the dominant structure in PDF-derived text.

    LEVEL INFERENCE: PDF-to-text keeps the visual indent of each heading, and the
    indent encodes the outline depth. We collect every heading's indent, rank the
    distinct indent values, and map rank -> level. This is fully generic (no font
    metrics, no product knowledge) and is what turns a FLAT list of 9k headings
    into a real nested tree.
    """
    raw_hits: list[tuple[int, str, int]] = []   # (line, title, indent)
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            continue
        if not _TITLECASE_RE.match(s) or not is_valid_heading(s):
            continue
        prev_blank = i == 0 or not lines[i - 1].strip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        # Isolation: a heading sits above its paragraph, not inside one.
        if prev_blank or (nxt and len(s) < len(nxt) * 0.6):
            raw_hits.append((i, s, len(ln) - len(ln.lstrip())))

    if not raw_hits:
        return []

    # Rank distinct indents -> levels. Indents within 2 columns are the same
    # level (PDF text extraction jitters by a space or two).
    indents = sorted({ind for _, _, ind in raw_hits})
    buckets: list[int] = []
    for ind in indents:
        if not buckets or ind - buckets[-1] > 2:
            buckets.append(ind)

    def level_for(indent: int) -> int:
        lvl = 1
        for b in buckets:
            if indent >= b:
                lvl = buckets.index(b) + 1
        return min(lvl, _MAX_LEVEL)

    return [HeadingHit(line, title, level_for(ind)) for line, title, ind in raw_hits]


def _plausibility(hits: list[HeadingHit], n_lines: int) -> float:
    """
    Score a detector's output: many DISTINCT headings, not absurdly dense.

    The distinctness term is what kills the old failure mode — a detector that
    emits "Number sign" 1,918 times scores near zero however many hits it has.

    The density guard only applies to reasonably large documents: on a tiny doc
    a high headings-per-line ratio is normal (a short outline is mostly
    headings), so we skip the guard under a few hundred lines to avoid throwing
    away correct structure.
    """
    if not hits or n_lines == 0:
        return 0.0
    if n_lines >= 300 and len(hits) / n_lines > 0.25:   # dense across a big doc → nonsense
        return 0.0
    distinct_ratio = len({h.title for h in hits}) / len(hits)
    return len(hits) * (distinct_ratio ** 2)


def find_headings(text: str) -> list[HeadingHit]:
    """Locate headings using the most plausible detector FOR THIS DOCUMENT."""
    lines = mask_code_lines(text)
    n = len(lines)

    candidates = (
        ("markdown",  _detect_markdown(lines)),
        ("numbered",  _detect_numbered(lines)),
        ("titlecase", _detect_titlecase(lines)),
    )
    scored = sorted(
        ((_plausibility(h, n), name, h) for name, h in candidates),
        key=lambda t: t[0], reverse=True,
    )
    best_score, _, best = scored[0]
    if best_score <= 0:
        return []

    merged = list(best)
    for score, _, hits in scored[1:]:
        if score >= best_score * 0.5 and hits is not best:
            merged.extend(hits)          # e.g. markdown doc w/ numbered sub-sections

    merged.sort(key=lambda h: h.line)
    seen, out = set(), []
    for h in merged:
        if h.line not in seen:
            seen.add(h.line)
            out.append(h)
    return out


def build_tree(text: str) -> tuple[str, list[HeadingNode]]:
    """Parse *text* into ``(preamble, roots)`` — an N-level nested heading tree."""
    hits = find_headings(text)
    if not hits:
        return text.strip(), []

    raw = text.splitlines()
    n = len(hits)
    roots: list[HeadingNode] = []
    stack: list[HeadingNode] = []

    for i, h in enumerate(hits):
        start = h.line + 1
        end   = hits[i + 1].line if i + 1 < n else len(raw)
        node  = HeadingNode(title=h.title, level=h.level,
                            body="\n".join(raw[start:end]).strip())
        while stack and stack[-1].level >= h.level:
            stack.pop()
        (stack[-1].children if stack else roots).append(node)
        stack.append(node)

    preamble = "\n".join(raw[: hits[0].line]).strip()
    return preamble, roots
