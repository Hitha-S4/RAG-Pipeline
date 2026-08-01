"""
LLM prompt templates — generic technical-documentation pipeline.

DATA-SOURCE INDEPENDENT: nothing below hardcodes any product. The product name
arrives via {doc_name}; every rule is phrased generically.

Public API
──────────
    SYSTEM_PROMPTS        – dict[category -> system prompt]  (concise MD builder)
    USER_PROMPTS          – dict[category -> user prompt template]
    SYSTEM_NOTES_PROMPTS  – dict[category -> system prompt]  (RAW-MD notes)
    USER_NOTES_PROMPTS    – dict[category -> user prompt template]
    CLASSIFY_SYSTEM       – system prompt for the one-shot classify+summarize call
    VALID_CATEGORIES      – frozenset of the six valid category names
    OVERVIEW_SYSTEM       – system prompt for the one-shot doc-overview call
    DEPENDENCY_ORDER      – generation order (list[str])
    CONTEXT_DEPS          – dict[category -> list of categories whose MD feeds in]
    build_context()       – helper: assemble the {context} string from prior MDs

User prompt placeholders (all user prompts share the same four)
───────────────────────────────────────────────────────────────
    {doc_name}      – display name of the source document
    {export_date}   – ISO date of this run
    {chunks}        – serialised entry text
    {context}       – dependency context (may be "" for root categories)

Package layout
──────────────
    _shared.py    – _ROLE, _G, DEPENDENCY_ORDER, CONTEXT_DEPS,
                    build_context(), OVERVIEW_SYSTEM
    classify.py   – CLASSIFY_SYSTEM, VALID_CATEGORIES         (step-4 prompt)
    knowledge.py  – SYSTEM_KNOWLEDGE_NOTES / SYSTEM_KNOWLEDGE + USER_*
    features.py   – SYSTEM_FEATURES_NOTES  / SYSTEM_FEATURES  + USER_*
    workflows.py  – SYSTEM_WORKFLOWS_NOTES / SYSTEM_WORKFLOWS + USER_*
    entities.py   – SYSTEM_ENTITIES_NOTES  / SYSTEM_ENTITIES  + USER_*
    keywords.py   – SYSTEM_KEYWORDS_NOTES  / SYSTEM_KEYWORDS  + USER_*
    personas.py   – SYSTEM_PERSONAS_NOTES  / SYSTEM_PERSONAS  + USER_*
"""
from __future__ import annotations

from src.enums import ChunkCategory

# ── Shared infrastructure ─────────────────────────────────────────────────────
from ._shared import (
    DEPENDENCY_ORDER,
    CONTEXT_DEPS,
    build_context,
    OVERVIEW_SYSTEM,
    COMPRESS_SYSTEM,
)

# ── Classify prompt ───────────────────────────────────────────────────────────
from .classify import CLASSIFY_SYSTEM, VALID_CATEGORIES

# ── Per-category notes prompts (RAW-MD builder) ───────────────────────────────
from .knowledge import SYSTEM_KNOWLEDGE_NOTES, USER_KNOWLEDGE_NOTES
from .features  import SYSTEM_FEATURES_NOTES,  USER_FEATURES_NOTES
from .workflows import SYSTEM_WORKFLOWS_NOTES, USER_WORKFLOWS_NOTES
from .entities  import SYSTEM_ENTITIES_NOTES,  USER_ENTITIES_NOTES
from .keywords  import SYSTEM_KEYWORDS_NOTES,  USER_KEYWORDS_NOTES
from .personas  import SYSTEM_PERSONAS_NOTES,  USER_PERSONAS_NOTES

# ── Per-category concise MD prompts (MD builder) ──────────────────────────────
from .knowledge import SYSTEM_KNOWLEDGE, USER_KNOWLEDGE
from .features  import SYSTEM_FEATURES,  USER_FEATURES
from .workflows import SYSTEM_WORKFLOWS, USER_WORKFLOWS
from .entities  import SYSTEM_ENTITIES,  USER_ENTITIES
from .keywords  import SYSTEM_KEYWORDS,  USER_KEYWORDS
from .personas  import SYSTEM_PERSONAS,  USER_PERSONAS

# ── Unified dicts — callers iterate by category key ──────────────────────────

_K  = ChunkCategory.KNOWLEDGE.value
_F  = ChunkCategory.FEATURES.value
_W  = ChunkCategory.WORKFLOWS.value
_E  = ChunkCategory.ENTITIES.value
_KW = ChunkCategory.KEYWORDS.value
_P  = ChunkCategory.PERSONAS.value

# Notes prompts (generate_notes / RAW-MD pass)
SYSTEM_NOTES_PROMPTS: dict[str, str] = {
    _K:  SYSTEM_KNOWLEDGE_NOTES,
    _F:  SYSTEM_FEATURES_NOTES,
    _W:  SYSTEM_WORKFLOWS_NOTES,
    _E:  SYSTEM_ENTITIES_NOTES,
    _KW: SYSTEM_KEYWORDS_NOTES,
    _P:  SYSTEM_PERSONAS_NOTES,
}

USER_NOTES_PROMPTS: dict[str, str] = {
    _K:  USER_KNOWLEDGE_NOTES,
    _F:  USER_FEATURES_NOTES,
    _W:  USER_WORKFLOWS_NOTES,
    _E:  USER_ENTITIES_NOTES,
    _KW: USER_KEYWORDS_NOTES,
    _P:  USER_PERSONAS_NOTES,
}

# Concise MD prompts (MD builder pass)
SYSTEM_PROMPTS: dict[str, str] = {
    _K:  SYSTEM_KNOWLEDGE,
    _F:  SYSTEM_FEATURES,
    _W:  SYSTEM_WORKFLOWS,
    _E:  SYSTEM_ENTITIES,
    _KW: SYSTEM_KEYWORDS,
    _P:  SYSTEM_PERSONAS,
}

USER_PROMPTS: dict[str, str] = {
    _K:  USER_KNOWLEDGE,
    _F:  USER_FEATURES,
    _W:  USER_WORKFLOWS,
    _E:  USER_ENTITIES,
    _KW: USER_KEYWORDS,
    _P:  USER_PERSONAS,
}

__all__ = [
    # classify
    "CLASSIFY_SYSTEM",
    "VALID_CATEGORIES",
    # compression
    "COMPRESS_SYSTEM",
    # unified dicts
    "SYSTEM_NOTES_PROMPTS",
    "USER_NOTES_PROMPTS",
    "SYSTEM_PROMPTS",
    "USER_PROMPTS",
    # individual notes system prompts
    "SYSTEM_KNOWLEDGE_NOTES",
    "SYSTEM_FEATURES_NOTES",
    "SYSTEM_WORKFLOWS_NOTES",
    "SYSTEM_ENTITIES_NOTES",
    "SYSTEM_KEYWORDS_NOTES",
    "SYSTEM_PERSONAS_NOTES",
    # individual concise system prompts
    "SYSTEM_KNOWLEDGE",
    "SYSTEM_FEATURES",
    "SYSTEM_WORKFLOWS",
    "SYSTEM_ENTITIES",
    "SYSTEM_KEYWORDS",
    "SYSTEM_PERSONAS",
    # user prompts
    "USER_KNOWLEDGE_NOTES",
    "USER_FEATURES_NOTES",
    "USER_WORKFLOWS_NOTES",
    "USER_ENTITIES_NOTES",
    "USER_KEYWORDS_NOTES",
    "USER_PERSONAS_NOTES",
    "USER_KNOWLEDGE",
    "USER_FEATURES",
    "USER_WORKFLOWS",
    "USER_ENTITIES",
    "USER_KEYWORDS",
    "USER_PERSONAS",
    # shared infrastructure
    "OVERVIEW_SYSTEM",
    "COMPRESS_SYSTEM",
    "DEPENDENCY_ORDER",
    "CONTEXT_DEPS",
    "build_context",
]
