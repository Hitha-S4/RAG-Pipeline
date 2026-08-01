"""
Taxonomy helpers — pure-Python, dependency-free.

This module owns two orthogonal classification axes and the small amount of
logic that maps between them.  It deliberately imports nothing from pydantic,
Milvus, or the LLM so it can be unit-tested in isolation and reused on both the
ingestion side (label every chunk) and the retrieval side (scope a query).

Axis 1 — CATEGORY  (``src.enums.ChunkCategory``)
    What *kind* of information a chunk is:
        knowledge · features · workflows · entities · keywords · personas
    A chunk may carry several categories; :func:`primary_category` collapses a
    multi-label list down to the single most specific one for storage/filtering.

Axis 2 — SUB-TYPE  (``src.enums.ChunkSubType``)
    Which *lifecycle action* the chunk is about:
        install · uninstall · upgrade · configure · integrate · administer ·
        monitor · troubleshoot · use · reference · overview · other
    Requirement (1): "classify as install, uninstall, configure, uses etc".
    This is what lets a query like *"how to configure a collector?"* fetch the
    ``configure`` slice of personas / features / workflows (requirement 3).

Everything here is heuristic and data-source independent (requirement 8): it
keys off generic verbs and doc-structure signals, never a product name.
"""
from __future__ import annotations

import re
from typing import Iterable

from src.enums import ChunkCategory
from src.enums.chunk_sub_type import ChunkSubType

# ──────────────────────────────────────────────────────────────────────────────
# Category priority — collapse a multi-label list to one primary category.
#
# Ordered most-specific → least-specific.  A chunk that is BOTH a workflow and a
# feature is stored as a workflow, because the workflow label is the one a
# retrieval filter benefits from most.  "knowledge" is the catch-all and always
# ranks last.
# ──────────────────────────────────────────────────────────────────────────────

_CATEGORY_PRIORITY: tuple[ChunkCategory, ...] = (
    ChunkCategory.WORKFLOWS,
    ChunkCategory.FEATURES,
    ChunkCategory.PERSONAS,
    ChunkCategory.ENTITIES,
    ChunkCategory.KEYWORDS,
    ChunkCategory.KNOWLEDGE,
)

_PRIORITY_INDEX: dict[str, int] = {
    cat.value: i for i, cat in enumerate(_CATEGORY_PRIORITY)
}


def primary_category(categories: Iterable[str]) -> ChunkCategory:
    """
    Collapse a list of category names to the single most-specific one.

    Unknown / empty inputs fall back to ``knowledge`` so this never raises and
    always returns a storable value.
    """
    best: ChunkCategory = ChunkCategory.KNOWLEDGE
    best_rank = len(_CATEGORY_PRIORITY)  # worse than anything real
    for name in categories or ():
        key = str(name).strip().lower()
        rank = _PRIORITY_INDEX.get(key)
        if rank is not None and rank < best_rank:
            best_rank = rank
            best = ChunkCategory(key)
    return best


# ──────────────────────────────────────────────────────────────────────────────
# Sub-type keyword vocabulary.
#
# Each sub-type maps to a set of regex word-patterns.  Patterns are matched
# whole-word (``\b`` boundaries) and case-insensitively.  Ordering in
# ``_SUBTYPE_ORDER`` breaks ties: the earliest matching sub-type with the
# highest hit-count wins.  Headings are weighted more heavily than body text
# because a section titled "Installing X" is a strong signal.
# ──────────────────────────────────────────────────────────────────────────────

_SUBTYPE_PATTERNS: dict[ChunkSubType, tuple[str, ...]] = {
    ChunkSubType.UNINSTALL: (
        r"uninstall(?:ing|ation)?", r"remov(?:e|al|ing)", r"delet(?:e|ion|ing)",
        r"decommission", r"tear[\s-]?down", r"deregister",
    ),
    ChunkSubType.INSTALL: (
        r"install(?:ing|ation)?", r"deploy(?:ing|ment)?", r"provision(?:ing)?",
        r"set[\s-]?up", r"onboard(?:ing)?", r"bootstrap",
    ),
    ChunkSubType.UPGRADE: (
        r"upgrad(?:e|ing)", r"updat(?:e|ing)", r"patch(?:ing)?", r"migrat(?:e|ion|ing)",
        r"roll[\s-]?back", r"version",
    ),
    ChunkSubType.CONFIGURE: (
        r"configur(?:e|ing|ation)", r"config", r"enabl(?:e|ing)", r"disabl(?:e|ing)",
        r"set(?:ting)?s?", r"tun(?:e|ing)", r"parameter", r"custom(?:ize|ise|ization)",
        r"defin(?:e|ing)", r"specify",
    ),
    ChunkSubType.INTEGRATE: (
        r"integrat(?:e|ion|ing)", r"connect(?:ing|ivity|or)?", r"federat(?:e|ion)",
        r"sync(?:hroniz(?:e|ation))?", r"import", r"export", r"api",
    ),
    ChunkSubType.ADMINISTER: (
        r"administ(?:er|ration|rative)", r"manag(?:e|ing|ement)", r"grant",
        r"revok(?:e|ing)", r"permission", r"role", r"access[\s-]?control",
        r"rotat(?:e|ion)", r"credential", r"backup", r"restore", r"schedul(?:e|ing)",
    ),
    ChunkSubType.MONITOR: (
        r"monitor(?:ing)?", r"audit(?:ing)?", r"alert(?:ing)?", r"report(?:ing)?",
        r"dashboard", r"metric", r"log(?:ging)?", r"observ(?:e|ability)",
    ),
    ChunkSubType.TROUBLESHOOT: (
        r"troubleshoot(?:ing)?", r"debug(?:ging)?", r"diagnos(?:e|is|tic)",
        r"error", r"fail(?:ure|ed|ing)?", r"resolv(?:e|ing)", r"fix(?:ing)?",
        r"known[\s-]?issue", r"workaround",
    ),
    ChunkSubType.USAGE: (
        r"us(?:e|ing|age)", r"run(?:ning)?", r"execut(?:e|ing|ion)",
        r"perform(?:ing)?", r"operat(?:e|ing|ion)", r"how[\s-]?to", r"example",
    ),
    ChunkSubType.REFERENCE: (
        r"reference", r"command(?:s)?", r"syntax", r"parameter[\s-]?list",
        r"glossary", r"appendix", r"cli", r"rest[\s-]?api",
    ),
    ChunkSubType.OVERVIEW: (
        r"overview", r"introduction", r"about", r"concept", r"architecture",
        r"what[\s-]?is", r"background", r"summary",
    ),
}

# Tie-break order: more specific / action-oriented sub-types first so that, on an
# equal hit count, "configure" beats the generic "use", and "uninstall" (checked
# before "install") is not shadowed by the "install" substring inside it.
_SUBTYPE_ORDER: tuple[ChunkSubType, ...] = (
    ChunkSubType.UNINSTALL,
    ChunkSubType.INSTALL,
    ChunkSubType.UPGRADE,
    ChunkSubType.CONFIGURE,
    ChunkSubType.INTEGRATE,
    ChunkSubType.ADMINISTER,
    ChunkSubType.MONITOR,
    ChunkSubType.TROUBLESHOOT,
    ChunkSubType.REFERENCE,
    ChunkSubType.USAGE,
    ChunkSubType.OVERVIEW,
)

# Pre-compile every pattern once at import time.
_COMPILED: dict[ChunkSubType, list[re.Pattern[str]]] = {
    st: [re.compile(rf"\b{pat}\b", re.IGNORECASE) for pat in pats]
    for st, pats in _SUBTYPE_PATTERNS.items()
}

_HEADING_WEIGHT = 3   # a match in a heading counts this many body matches


def _count_hits(text: str, sub_type: ChunkSubType) -> int:
    if not text:
        return 0
    return sum(1 for rx in _COMPILED[sub_type] if rx.search(text))


def score_sub_types(text: str, headings: Iterable[str] | None = None) -> dict[ChunkSubType, int]:
    """
    Return a ``{ChunkSubType: weighted_hit_count}`` map for *text* + *headings*.

    Headings are weighted ``_HEADING_WEIGHT``× body matches.  Exposed publicly so
    callers (and tests) can inspect the full distribution, not just the winner.
    """
    heading_text = " ".join(headings or [])
    scores: dict[ChunkSubType, int] = {}
    for st in _SUBTYPE_ORDER:
        body_hits    = _count_hits(text, st)
        heading_hits = _count_hits(heading_text, st)
        total = body_hits + _HEADING_WEIGHT * heading_hits
        if total:
            scores[st] = total
    return scores


def classify_sub_type(
    text: str,
    headings: Iterable[str] | None = None,
    default: ChunkSubType = ChunkSubType.OTHER,
) -> ChunkSubType:
    """
    Best-guess lifecycle sub-type for a chunk of documentation.

    Returns *default* (``other``) when no vocabulary matches — callers can then
    leave the LLM-provided value in place if they have one.
    """
    scores = score_sub_types(text, headings)
    if not scores:
        return default
    # Highest weighted count wins; ties broken by _SUBTYPE_ORDER (dict preserves
    # insertion order, which follows _SUBTYPE_ORDER in score_sub_types).
    best_st = max(scores, key=lambda st: (scores[st], -_SUBTYPE_ORDER.index(st)))
    return best_st


# ──────────────────────────────────────────────────────────────────────────────
# Query-side detection — the retrieval counterpart.
# ──────────────────────────────────────────────────────────────────────────────

def detect_query_sub_type(query: str) -> ChunkSubType | None:
    """
    Infer the lifecycle sub-type a *question* is about.

    Returns ``None`` (rather than ``other``) when nothing matches, so the caller
    can choose to skip sub-type scoping entirely instead of forcing a filter.

    Example (requirement 3):
        "how to configure a collector?"  → ChunkSubType.CONFIGURE
    """
    scores = score_sub_types(query, headings=None)
    if not scores:
        return None
    return max(scores, key=lambda st: (scores[st], -_SUBTYPE_ORDER.index(st)))


def valid_sub_type(value: str) -> ChunkSubType:
    """Coerce an arbitrary string to a ChunkSubType, defaulting to ``other``."""
    key = str(value).strip().lower()
    try:
        return ChunkSubType(key)
    except ValueError:
        return ChunkSubType.OTHER
