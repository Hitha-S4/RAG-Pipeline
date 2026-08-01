"""
Summary distillation prompts — turn raw per-chunk summaries into ONE clean,
merged, retrieval-optimised document per category.

Data-source independent: uses the same per-category SYSTEM_PROMPTS and
USER_PROMPTS that the main ingestion pipeline uses, so the distilled output
is in the exact same schema that retrieval and reporting expect.

Two goals, both required:
  1. FORMAT  — output matches the per-category concise MD schema exactly.
  2. RETRIEVAL — entries are answer-first (name/term stated first), matching
     the design of SYSTEM_PROMPTS / USER_PROMPTS.
"""
from __future__ import annotations

from datetime import date

# Re-use the production concise MD prompts — data-source independent,
# well-tested, and they produce the exact schema retrieval expects.
# Use relative imports (we're inside the prompts package) to avoid any
# chance of a circular import through the package __init__.
from .features  import SYSTEM_FEATURES,  USER_FEATURES
from .workflows import SYSTEM_WORKFLOWS, USER_WORKFLOWS
from .entities  import SYSTEM_ENTITIES,  USER_ENTITIES
from .keywords  import SYSTEM_KEYWORDS,  USER_KEYWORDS
from .personas  import SYSTEM_PERSONAS,  USER_PERSONAS
from .knowledge import SYSTEM_KNOWLEDGE, USER_KNOWLEDGE
from src.enums import ChunkCategory

_K  = ChunkCategory.KNOWLEDGE.value
_F  = ChunkCategory.FEATURES.value
_W  = ChunkCategory.WORKFLOWS.value
_E  = ChunkCategory.ENTITIES.value
_KW = ChunkCategory.KEYWORDS.value
_P  = ChunkCategory.PERSONAS.value

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

# ── Public API ────────────────────────────────────────────────────────────────

DISTILL_CATEGORIES = list(SYSTEM_PROMPTS)


def get_distill_prompts(category: str, product_name: str) -> dict[str, str]:
    """Return {"system": ..., "task": ...} for one category.

    ``system``  — the concise MD builder system prompt for this category.
    ``task``    — the user message template; caller substitutes {notes}.
                  Uses USER_PROMPTS[category] with:
                    {doc_name}     ← product_name
                    {export_date}  ← today's ISO date
                    {context}      ← "" (no dependency context at distill time)
                    {chunks}       ← the raw notes block
    """
    system = SYSTEM_PROMPTS[category]
    user_tpl = USER_PROMPTS[category]
    # Pre-fill the stable placeholders; leave {chunks} for the merge loop.
    task_prefix = user_tpl.format(
        doc_name=product_name,
        export_date=date.today().isoformat(),
        context="",
        chunks="{notes}",
    )
    return {"system": system, "task": task_prefix}


# Backward-compat alias used by SummaryDistiller._merge ─────────────────────
# The old API was:
#   spec = DISTILL_PROMPTS[category]
#   system = spec["system"].format(product_name=...)
#   user   = spec["task"].format(category=..., notes=...)
#
# The new helper is called directly from SummaryDistiller; DISTILL_PROMPTS is
# kept as an empty sentinel so any stale import doesn't crash.
DISTILL_PROMPTS: dict[str, dict[str, str]] = {}
