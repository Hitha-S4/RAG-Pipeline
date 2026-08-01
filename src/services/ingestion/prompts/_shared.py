"""
Shared infrastructure for all prompt modules.

Exported
────────
    _ROLE             – grounding + output-format prefix (prepended to every SYSTEM_*)
    _G                – quality-gates prefix (used by the concise-MD builder prompts)
    DEPENDENCY_ORDER  – generation order list
    CONTEXT_DEPS      – dict[category -> upstream categories]
    build_context()   – assembles the {context} string from prior MD files
    OVERVIEW_SYSTEM   – system prompt for the one-shot doc-overview call
"""
from __future__ import annotations
from pathlib import Path

from src.enums import ChunkCategory

# ── Dependency graph ──────────────────────────────────────────────────────────

_K = ChunkCategory.KNOWLEDGE.value
_F = ChunkCategory.FEATURES.value
_W = ChunkCategory.WORKFLOWS.value
_E = ChunkCategory.ENTITIES.value
_KW = ChunkCategory.KEYWORDS.value
_P = ChunkCategory.PERSONAS.value

DEPENDENCY_ORDER: list[str] = [_K, _F, _W, _E, _KW, _P]

CONTEXT_DEPS: dict[str, list[str]] = {
    _K:  [],
    _F:  [_K],
    _W:  [_K, _F],
    _E:  [_K],
    _KW: [_K, _F, _E],
    _P:  [_K, _F, _E],
}

# Per-dependency char budget inside {context}; caller may override.
_CTX_BUDGET_PER_DEP = 1400


def build_context(category: str, out_dir: str | Path,
                  budget_per_dep: int = _CTX_BUDGET_PER_DEP) -> str:
    """
    Assemble the {context} string for `category` from previously generated
    files in out_dir. For each dependency, includes an excerpt of the
    processed MD (<CAT>.md) AND, when present, the RAW MD (<CAT>_RAW.md).
    Returns "" for root categories or when nothing exists yet.
    """
    out_dir = Path(out_dir)
    parts: list[str] = []
    for dep in CONTEXT_DEPS.get(category, []):
        for suffix, label in ((".md", "processed"), ("_RAW.md", "raw")):
            p = out_dir / f"{dep.upper()}{suffix}"
            if p.exists():
                text = p.read_text(encoding="utf-8", errors="ignore")
                # skip the file header (everything up to first ---)
                i = text.find("\n---\n")
                body = text[i + 5:] if i >= 0 else text
                parts.append(f"[{dep} / {label}]\n{body[:budget_per_dep].strip()}")
    return "\n\n".join(parts)


# ── Shared role header (used by generate_notes / RAW-MD prompts) ──────────────

_ROLE = (
    "You are a precise technical documentation analyst. "
    "Extract structured fields from the provided excerpts. "
    "Ground every statement in the excerpt text — never invent facts. "
    "A CONTEXT block may appear before the excerpts; use it only for grounding, "
    "do not copy it verbatim. "
    "Output ONLY the ===N=== blocks specified. No prose, no headings, no extra text.\n\n"
)


# ── Quality-gates prefix (used by concise-MD builder prompts) ─────────────────
# G1 truncation  — "…from multiple IP addre" mid-word cutoffs
# G2 page noise  — titles like "<Product Name> 873" (page artifacts)
# G3 fragments   — sentence fragments used as names ("You do not need to…")
# G4 duplicates  — the same topic emitted as many entries
# G5 tables      — parameter-table rows mistaken for content

_G = """You are a technical documentation analyst. Ground every statement in the
provided entries; never invent facts, names, versions, or steps. Preserve exact
terminology and command syntax. Output Markdown only — no preamble, no fences.

QUALITY GATES (apply to every entry you write):
G1 COMPLETE SENTENCES ONLY. Source excerpts may be cut off mid-sentence.
   Never copy a cut-off fragment. Either finish the thought as a complete,
   faithful sentence, or stop at the last complete sentence in the excerpt.
   A description must never end mid-word or mid-clause.
G2 CLEAN TITLES. Never use a title that is a document/page artifact — e.g.
   a product name followed by a number ("<Product> 873"), a running header,
   or table column labels ("Parameter Description", "Name Description").
   Derive a real topic/task name from the entry's content instead.
G3 NAMES ARE NOUN PHRASES. A name/title is a short noun phrase or task name,
   never a sentence fragment ("You do not need to restart…" is NOT a name).
   If the heading is a fragment, name the thing the text is actually about.
G4 NO DUPLICATES. If several entries cover the same topic (same cleaned name),
   MERGE them into one block combining their information. Never emit two
   blocks with the same title.
G5 SKIP NOISE. If an entry is only a parameter-table fragment, a page header,
   or has no meaningful content, skip it silently — output nothing for it.
   It is always better to write fewer, complete blocks than many broken ones.

"""

# ── Doc-overview system prompt ────────────────────────────────────────────────

OVERVIEW_SYSTEM = (
    _G
    + "Below are representative excerpts from one document. Write a concise "
    "overview (3-5 complete sentences) covering: (1) what product or subsystem "
    "the document describes, (2) its primary purpose and capabilities, and "
    "(3) the main user roles, objects, or procedures addressed. Output ONLY "
    "the overview paragraph."
)

# ── Layer-2 compression prompt ────────────────────────────────────────────────
# Receives the full layer-1 structured output for a category and compresses it
# into the most concise, high-level summary possible — no new facts, no loss
# of distinct concepts, aggressive deduplication.

COMPRESS_SYSTEM = (
    _G
    + "You are given a structured Markdown reference for ONE category extracted "
    "from technical documentation. Your job is to COMPRESS it into the most "
    "concise, high-level version possible while keeping every distinct concept.\n\n"
    "COMPRESSION RULES:\n"
    "C1 MERGE similar items. If two sections or entries describe the same thing "
    "   from different angles, merge them into one. Never repeat the same concept twice.\n"
    "C2 KEEP structure. Preserve ## group headings and ### item headings. "
    "   Remove sub-headings that add no new information.\n"
    "C3 SHORTEN descriptions. Each item gets at most 1-2 sentences. "
    "   Cut every word that does not add meaning.\n"
    "C4 DROP noise. Remove entries that are page artifacts, parameter-table "
    "   fragments, or header-only placeholders with no real content.\n"
    "C5 NO new facts. Never add information not present in the input.\n"
    "Output ONLY the compressed Markdown. No preamble, no fences."
)
