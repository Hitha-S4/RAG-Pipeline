# -*- coding: utf-8 -*-
"""
Extraction prompt set — v3. Product-agnostic.

WHAT CHANGED FROM v2
    v2 hardcoded one product's vocabulary into the prompts and the regexes.
    That is wrong twice over:
      1. it does not generalize to other documentation sets, and
      2. priming a model with product X's terms invites it to inject those
         terms into product Y's documentation — a hallucination vector.
    v3 describes identifiers by SHAPE, never by name, and derives the actual
    domain vocabulary from the corpus at runtime via build_domain_profile().

WHY SPLIT INTO SIX PASSES
    A single mega-prompt forces the model to weigh six competing content specs
    at once. Typical failure modes: windows silently returning nothing, exact
    identifiers replaced by vague paraphrase, and a fallback sub-type absorbing
    most blocks. Root cause: models compress by default, and a preservation
    rule buried deep in a long prompt loses to that instinct.

ARCHITECTURE (do not run the six passes blindly in parallel)
    PASS 0  ROUTER  -> one cheap call. Inventories every fact in the window and
                       assigns each to exactly ONE type. Preserves ONE HOME,
                       which six independent passes would destroy.
    PASS 1..6 TYPED -> run only for the types the router found. Each pass sees
                       the router manifest, so it knows what it owns and what
                       to merely cross-reference.
    PASS 7  AUDIT   -> mechanical + LLM check that every identifier and every
                       manifest item survived. Re-run failures.

USAGE
    profile = build_domain_profile(all_source_text)      # once per corpus
    sys_msg = TYPE_PROMPTS["keywords"].format(domain_terms=profile)
    usr_msg = TYPED_USER.format(doc_name=..., index=..., total=...,
                                type_name="keywords", manifest=..., text=...)
"""

from __future__ import annotations

import re
from collections import Counter

# ═══════════════════════════════════════════════════════════════════════════
# SHARED GROUNDING CONTRACT — prepended to every pass
# Identifier classes are defined by SHAPE. No product names appear anywhere.
# ═══════════════════════════════════════════════════════════════════════════

GROUNDING_CONTRACT = """\
Rules:
- Use ONLY facts present in the input window.
- Do NOT add commentary, markdown, or text outside the required block schema.
- Preserve identifiers, commands, paths, versions, ports, flags, file names, and limits verbatim.
- Content MUST reproduce the relevant source passage in full — copy every sentence from the
  source window that belongs to this block verbatim or near-verbatim. Do NOT paraphrase,
  condense, summarise, or omit any sentence. A block's Content should be 450–600 tokens;
  if you find yourself writing fewer than 200 tokens, you have under-copied — go back and
  include the missing source sentences.
- Keep Summary concise and answer-first (1–2 sentences; this is the ONLY field that should
  be condensed — Content must not be).
- If a detail is not stated, write exactly: not stated.
- If ownership is unclear, emit the fact as knowledge rather than dropping it.
- Record negative and limiting facts exactly as written.
"""

DOMAIN_SLOT = """\
━━━ DOMAIN VOCABULARY OBSERVED IN THIS CORPUS ━━━
The tokens below were extracted mechanically from the source documents. They
are lookup keys: if one appears in your window, carry it verbatim. This list is
descriptive, not exhaustive — a token absent from it is still an identifier if
it matches a G3 shape. Never introduce a token from this list into a block
whose window does not contain it.
{domain_terms}
"""

SUBTYPE_VOCAB = """\
━━━ SUB-TYPE — choose exactly one; "other" is a last resort ━━━
  install       installing / deploying / setting up
  uninstall     removing / decommissioning
  upgrade       upgrading / patching / migrating versions
  configure     configuring / enabling / tuning settings and parameters
  integrate     connecting to other systems / APIs / connectors
  administer    users, roles, permissions, backups, schedules
  monitor       monitoring, auditing, alerting, reporting, dashboards
  troubleshoot  diagnosing errors, known issues, workarounds
  use           running / operating / day-to-day usage and examples
  reference     command / parameter reference, syntax, glossary
  overview      conceptual overview, introduction, architecture
  other         ONLY if none of the above can be defended
"""

OUTPUT_FORMAT = """\
Return ONLY blocks in this exact schema:
===1===
- Type: <the single type this pass extracts>
- SubType: <one value from the sub-type vocabulary>
- Name: <short noun phrase; preserve exact identifier verbatim>
- Content: <full verbatim or near-verbatim source passage for this block — do NOT condense>
- Summary: <1–2 sentence concise answer-first summary>
- Keywords: <comma-separated names or none>
- Features: <comma-separated names or none>
- Workflows: <comma-separated names or none>
- Personas: <comma-separated names or none>
- Entities: <comma-separated names or none>
===2===
...

If the window contains no items of this type, reply exactly:
NONE FOR THIS TYPE
"""

SUMMARY_RULES = """\
Summary rules:
- Start with the exact Name in the first three words.
- Keep Summary to one or two dense sentences.
- Use the same identifiers and key terms found in the input.
- No filler, commentary, or marketing language.
"""

ROUTER_SYSTEM = f"""\
You are the routing stage of a documentation extraction pipeline. You do not
write blocks. You inventory the window and assign ownership, so that later
passes never duplicate or drop a fact.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
━━━ YOUR TASK ━━━
1. Walk the window top to bottom and list EVERY distinct item it documents.
   An item is anything a reader could ask a question about: a defined term, a
   role, a procedure, a capability, a named object, a concept, a table row, a
   list entry, a release-note line.
2. Assign each item exactly ONE owning type, first match wins:
     1. a bare term / acronym being DEFINED (X = ...)              -> keywords
     2. a human role, job title, or set of responsibilities        -> personas
     3. an ordered procedure / how-to / configuration task         -> workflows
     4. a named capability with limits/benefits/prerequisites      -> features
     5. a named deployable or configurable system object           -> entities
     6. anything else: concept, overview, architecture, background -> knowledge
3. One item per LIST ENTRY and one per TABLE ROW. Never collapse a list or a
   table into a single item.
4. Skip ONLY: bare page numbers, running headers, tables of contents.

━━━ COVERAGE CHECK BEFORE YOU ANSWER ━━━
Re-read the window and confirm every sentence is represented by some item. Any
sentence not covered must become a knowledge item. Then list every G3-shaped
identifier appearing anywhere in the window and name the item that will carry it.

━━━ OUTPUT ━━━
ITEMS
- <name> :: <type> :: <one-line scope: what this item owns>
IDENTIFIERS
- <identifier> :: <owning item name>
UNCOVERED
- <any sentence you could not place, verbatim; or "none">
"""

ROUTER_USER = """\
SOURCE: {doc_name} | WINDOW {index} of {total}

{text}

Inventory every item now. Assign exactly one owning type to each. List every
identifier and its owner. Report anything you could not place.\
"""

KEYWORDS_SYSTEM = f"""\
Extract only keywords blocks: domain-specific terms, acronyms, component names,
and standards named or defined in the window.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
A keyword is a lookup term. Emit one block for each distinct term the window
names as a thing.

Content rules:
- Keep the exact term or acronym verbatim.
- Expand an acronym only if the source explicitly expands it.
- State what it is and any distinguishing detail the source gives.
- Do not duplicate the same term across multiple blocks.

{SUBTYPE_VOCAB}
Prefer these subtypes for keywords: reference, overview.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

PERSONAS_SYSTEM = f"""\
Extract only personas blocks: human roles that operate or use the product.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
A persona is a named human role, job title, or account role described in the window.

Content rules:
- Keep the role name exactly as written.
- State what the role uses the product for.
- Include only responsibilities, permissions, and access stated in the source.
- Do not transfer tasks between roles or merge similar roles.

{SUBTYPE_VOCAB}
Prefer these subtypes for personas: administer, use, overview.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

FEATURES_SYSTEM = f"""\
Extract only features blocks: named product capabilities or functions.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
A feature is a named capability the window describes.

Content rules:
- Reproduce ALL relevant source sentences verbatim; do not condense or paraphrase.
- State what the capability does, its prerequisites, limits, and numeric caps.
- Preserve platforms, systems, versions, and version floors verbatim.
- Aim for 450–600 tokens in Content; fewer than 200 tokens means under-copied.

{SUBTYPE_VOCAB}
Prefer these subtypes for features: configure, integrate, monitor, use, overview.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

WORKFLOWS_SYSTEM = f"""\
Extract only workflows blocks: step-by-step procedures and operational or configuration tasks.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
A workflow is a named task or procedure described in the window.

Content rules:
- Reproduce the full procedure verbatim from the source; do not condense or drop steps.
- Keep steps in source order; do not merge, reorder, or invent steps.
- Preserve commands, APIs, tools, flags, menu paths, and variants verbatim.
- If the task is named but steps are absent, write exactly: Steps: not stated.
- Aim for 450–600 tokens in Content; fewer than 200 tokens means under-copied.

Add one workflow qualifier to the Name when present:
- navigation
- configuration
- action

{SUBTYPE_VOCAB}
Prefer these subtypes for workflows: install, uninstall, upgrade, configure, integrate, administer, troubleshoot, use.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

ENTITIES_SYSTEM = f"""\
Extract only entities blocks: named system objects.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
An entity is a named deployable or configurable object such as an agent, service,
process, node, policy, rule, connector, component, data source, credential,
certificate, keystore, port, group, or queue.

Content rules:
- Reproduce ALL source sentences that describe this entity verbatim.
- State what it does, its purpose, and its relationships to other components.
- Preserve parameters, ports, files, and configuration surface verbatim.
- Do not infer roles or relationships that the source does not state.
- Record denied or unsupported capabilities exactly.
- Aim for 450–600 tokens in Content; fewer than 200 tokens means under-copied.

{SUBTYPE_VOCAB}
Prefer these subtypes for entities: configure, integrate, administer, reference, overview.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

KNOWLEDGE_SYSTEM = f"""\
Extract only knowledge blocks: overview, architecture, concepts, background,
and any fact not owned by keywords, personas, features, workflows, or entities.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}
Knowledge is the fallback type: if a fact is real and type ownership is unclear,
use knowledge instead of dropping it.

Content rules:
- Reproduce ALL relevant source sentences verbatim for this concept or background fact.
- State what it is, why it matters, and how it fits, using only source facts.
- One meaningful table row or list entry may become one block.
- Use exactly one primary type per block; merge nearby duplicate facts.
- Aim for 450–600 tokens in Content; fewer than 200 tokens means under-copied.

{SUBTYPE_VOCAB}
Prefer these subtypes for knowledge: overview, reference, monitor, troubleshoot.

{SUMMARY_RULES}
{OUTPUT_FORMAT}
"""

TYPED_USER = """\
SOURCE: {doc_name} | WINDOW {index} of {total}
EXTRACTING TYPE: {type_name}

ROUTER MANIFEST — items assigned to you, and identifiers you must carry:
{manifest}

WINDOW TEXT:
{text}

Emit one block for every manifest item of type {type_name}. Preserve every fact
and every identifier verbatim. If the window truly
contains no items of this type, reply exactly: NONE FOR THIS TYPE\
"""

AUDIT_SYSTEM = """\
You audit an extraction for LOSS and for INVENTION. You do not rewrite blocks.
You have no knowledge of this product beyond the source window given to you.

Given the source window and the blocks extracted from it, report:

LOST — facts, sentences, numbers, limits, or variants present in the source that
       appear in NO block. Quote each verbatim from the source.
DROPPED IDENTIFIERS — every component name, acronym, cipher, protocol, version,
       port, command, flag, file, parameter, or role name in the source that
       appears in no block.
INVENTED — every claim in a block NOT supported by the source, including
       invented acronym expansions, invented steps, invented role names, and
       invented relationships between components. Quote the offending text.
BAD EVIDENCE — any Evidence span that is not a literal substring of the source.
OVER-COMPRESSED — any block whose Content replaces a specific source value with
       a category word.
CONTRADICTED — any block that asserts something the source denies or limits.

Be exhaustive and literal. Report counts even when zero. Do not praise, do not
summarize, do not suggest rewrites.

OUTPUT
LOST (n)
- "<verbatim source span>"
DROPPED IDENTIFIERS (n)
- <identifier>
INVENTED (n)
- <block name> :: "<offending text>"
BAD EVIDENCE (n)
- <block name> :: "<span>"
OVER-COMPRESSED (n)
- <block name> :: source "<specific>" -> block "<vague>"
CONTRADICTED (n)
- <block name> :: source "<statement>" -> block "<contradiction>"
"""

AUDIT_USER = """\
SOURCE WINDOW:
{text}

EXTRACTED BLOCKS:
{blocks}

Audit now. Be exhaustive and literal.\
"""

TYPE_PROMPTS = {
    "keywords": KEYWORDS_SYSTEM,
    "personas": PERSONAS_SYSTEM,
    "features": FEATURES_SYSTEM,
    "workflows": WORKFLOWS_SYSTEM,
    "entities": ENTITIES_SYSTEM,
    "knowledge": KNOWLEDGE_SYSTEM,
}

EXTRACTION_ORDER = [
    "keywords",
    "entities",
    "workflows",
    "features",
    "personas",
    "knowledge",
]

# ═══════════════════════════════════════════════════════════════════════════
# DIRECT (INDEPENDENT) USER MESSAGE — no router manifest required.
#
# Used by the "independent" extraction mode in EntityPipeline.
# Each category gets its own dedicated TYPE_PROMPTS[category] system prompt
# AND its own DIRECT_USER message with just the window text.
#
# Difference from TYPED_USER:
#   TYPED_USER  — requires {manifest} from a prior ROUTER call.
#   DIRECT_USER — no ROUTER; the system prompt already scopes the category.
#                 The LLM extracts only its category from the raw window.
#
# Usage:
#   system = TYPE_PROMPTS[category].format(domain_terms=domain_terms)
#   user   = DIRECT_USER.format(doc_name=..., index=..., total=...,
#                                type_name=category, text=window_text)
# ═══════════════════════════════════════════════════════════════════════════

DIRECT_USER = """\
SOURCE: {doc_name} | WINDOW {index} of {total}
EXTRACTING TYPE: {type_name}

WINDOW TEXT:
{text}

Emit one block for every {type_name} item in the window. Preserve every fact \
and every identifier verbatim. If the window truly contains no items of this \
type, reply exactly: NONE FOR THIS TYPE\
"""

# ═══════════════════════════════════════════════════════════════════════════
# ALL-TYPES SINGLE-CALL PROMPT
# One LLM call per window; emits all six types in one reply.
# This is the production path used by entity_pipeline.py.
# ═══════════════════════════════════════════════════════════════════════════

# Separate output format for the all-types prompt: Type field lists all valid
# values instead of "the single type this pass extracts", and the NONE FOR THIS
# TYPE fallback is removed (it only applies to single-type passes).
_ALL_TYPES_OUTPUT_FORMAT = """\
Return ONLY blocks in the schema below.

NOTE ON THE TRAILING "..." — REMOVED DELIBERATELY.
The previous version of this template ended with a literal ellipsis to mean
"and so on for further blocks". Instruction-following models read "Return ONLY
blocks in this exact schema" plus a schema ending in "..." and returned exactly
that: three characters. 383 of 389 windows came back as "..." and the run
produced 6 chunks from an 8 MB document. Never end a strict-format template
with a continuation marker — state the repetition rule in words instead.

Emit one block per item, numbered sequentially from 1, using this structure for
every block. There is no upper limit on the number of blocks; a dense window
should produce many.

===1===
- Type: <one of: keywords | personas | workflows | features | entities | knowledge>
- SubType: <one value from the sub-type vocabulary>
- Name: <short noun phrase; preserve exact identifier verbatim>
- Content: <full verbatim or near-verbatim source passage for this block — reproduce every
  relevant sentence from the window; do NOT paraphrase, condense, or summarise; aim for
  450–600 tokens; fewer than 200 tokens means you under-copied>
- Summary: <1–2 sentence concise answer-first summary — this is the ONLY field to condense>
- Keywords: <comma-separated names or none>
- Features: <comma-separated names or none>
- Workflows: <comma-separated names or none>
- Personas: <comma-separated names or none>
- Entities: <comma-separated names or none>

The next block repeats the same ten fields under a ===2=== marker, then
===3===, and so on until every item in the window has been emitted.

Your reply must begin with the characters ===1=== and contain nothing else
before it. Never reply with an ellipsis, a placeholder, or a restatement of
this schema.
"""

ALL_TYPES_SYSTEM = f"""\
You are a documentation extraction engine. Given one window of technical
documentation, extract EVERY fact into typed blocks covering all six categories
in a SINGLE reply.

{GROUNDING_CONTRACT}
{DOMAIN_SLOT}

━━━ SIX BLOCK TYPES — emit blocks of ALL types found in this window ━━━

  keywords  — a term, acronym, abbreviation, standard, or protocol being named
              or defined. One block per distinct term.
              Prefer sub-types: reference, overview.

  personas  — a human role, job title, or account role that operates or uses
              the product. State responsibilities and access from the source.
              Prefer sub-types: administer, use, overview.

  workflows — a named step-by-step procedure, how-to, or configuration task.
              Keep steps in source order. Preserve commands, flags, menu paths
              verbatim. If steps are absent write: Steps: not stated.
              Prefer sub-types: install, configure, integrate, administer,
              troubleshoot, use.

  features  — a named product capability, function, or mode. State what it does,
              its prerequisites, limits, and numeric caps verbatim.
              Prefer sub-types: configure, integrate, monitor, use, overview.

  entities  — a named deployable or configurable system object: agent, service,
              process, node, policy, rule, connector, component, data source,
              credential, certificate, port, group, or queue. Preserve parameters,
              ports, files, and configuration surface verbatim.
              Prefer sub-types: configure, integrate, administer, reference, overview.

  knowledge — overview, architecture, concepts, background, and ANY fact not
              clearly owned by the five types above. This is the FALLBACK type:
              never drop a fact; emit it as knowledge if unsure.
              Prefer sub-types: overview, reference, monitor, troubleshoot.

━━━ TYPE ASSIGNMENT RULES (first match wins) ━━━
  1. A bare term / acronym being DEFINED                -> keywords
  2. A human role or set of responsibilities            -> personas
  3. An ordered procedure / how-to / configuration task -> workflows
  4. A named capability with limits or benefits         -> features
  5. A named deployable or configurable system object   -> entities
  6. Anything else: concept, overview, architecture     -> knowledge

━━━ COVERAGE RULES ━━━
- Every sentence must land in exactly one block.
- One list entry or table row = one block (never collapse a list into one block).
- Merge ONLY byte-identical duplicate facts.
- Skip ONLY: bare page numbers, running headers, tables of contents.
- When a window truly contains nothing for a type, emit NO blocks of that type.

{SUBTYPE_VOCAB}

{SUMMARY_RULES}

{_ALL_TYPES_OUTPUT_FORMAT}
"""

ALL_TYPES_USER = """\
SOURCE: {doc_name} | WINDOW {index} of {total}

{text}

Extract every block now. Emit blocks for ALL six types found in this window in
one reply. Preserve every fact and identifier verbatim.\
"""

IDENTIFIER_PATTERNS = [
    r"\b[A-Z][A-Z0-9]{1,}(?:-[A-Z0-9]+)*\b",
    r"\b[A-Za-z]{2,}-\d{2,4}(?:-[A-Za-z]{2,4})?\b",
    r"\b\d{3,4}-bit\b",
    r"\b[A-Za-z]{2,10} \d+\.\d+(?:\.\d+)?\b",
    r"\bv?\d+\.\d+(?:\.\d+)+\b",
    r"\bport \d{2,5}\b",
    r"\b(?:no more than|up to|maximum of|at least|minimum of) \d+\b",
    r"\b[\w.-]+\.(?:[a-z]{2,5})\b",
    r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){1,4}\b",
    r"\b[a-z]+(?:[A-Z][a-z0-9]+){1,3}\b",
    r"(?<!\w)--?[a-zA-Z][\w-]{1,}\b",
    r"\b[A-Z][\w ]{1,24}(?: > [A-Z][\w ]{1,24}){1,4}\b",
]

_STOPWORD_SHAPES = re.compile(
    r"^(?:The|This|That|These|Those|When|Where|What|Which|With|From|Into|"
    r"NOTE|WARNING|IMPORTANT|TABLE|FIGURE|CHAPTER|SECTION|AND|OR|NOT|ALL|ANY)$",
    re.I,
)


def find_identifiers(text: str) -> set[str]:
    """Every identifier-shaped token in a string. Purely structural."""
    out: set[str] = set()
    for pat in IDENTIFIER_PATTERNS:
        for m in re.finditer(pat, text):
            tok = m.group(0).strip()
            if len(tok) > 1 and not _STOPWORD_SHAPES.match(tok):
                out.add(tok)
    return out


def build_domain_profile(corpus_text: str, min_count: int = 3, top_n: int = 250) -> str:
    """Derive this corpus's vocabulary instead of hardcoding one."""
    counts: Counter[str] = Counter()
    for pat in IDENTIFIER_PATTERNS:
        for m in re.finditer(pat, corpus_text):
            tok = m.group(0).strip()
            if len(tok) > 1 and not _STOPWORD_SHAPES.match(tok):
                counts[tok] += 1
    kept = [(t, c) for t, c in counts.most_common(top_n) if c >= min_count]
    if not kept:
        return "  (none detected)"
    return "\n".join(f"  {t}   (x{c})" for t, c in kept)


def check_window(source_text: str, blocks_text: str) -> dict:
    """Mechanical loss check. Run per window; re-extract on failure."""
    src = find_identifiers(source_text)
    out = find_identifiers(blocks_text)
    dropped = sorted(src - out)
    return {
        "identifiers_in_source": len(src),
        "identifiers_in_output": len(src & out),
        "dropped": dropped,
        "empty_output": (not blocks_text.strip() or blocks_text.strip() == "NONE FOR THIS TYPE"),
        "passed": not dropped,
    }


def check_evidence(source_text: str, evidence_spans: list[str]) -> list[str]:
    """Return spans that are NOT literal substrings of the source (G4 breach)."""
    norm = " ".join(source_text.split())
    bad = []
    for span in evidence_spans:
        s = " ".join(span.strip().strip('"').split())
        if s and s not in norm:
            bad.append(span)
    return bad


def check_injection(window_text: str, blocks_text: str) -> list[str]:
    """Guard against cross-document contamination."""
    in_window = find_identifiers(window_text)
    in_blocks = find_identifiers(blocks_text)
    return sorted(in_blocks - in_window)


# ═══════════════════════════════════════════════════════════════════════════
# COMPACT OUTPUT FORMAT — opt-in via LLM_COMPACT_SCHEMA=true
#
# WHY THIS EXISTS
#   Wall-clock time on this pipeline is dominated by DECODE, not prefill:
#   ~11 M output tokens at ~90 tok/s per stream. Anything that shrinks the
#   reply shrinks the run proportionally.
#
#   Measured on a 1,500-char window: completions averaged ~1,750 tokens.
#   `Evidence` (verbatim quotes, up to 3 spans per block) and the five
#   cross-reference lines account for roughly 40% of that.
#
# WHAT YOU GIVE UP — read before enabling
#   * Evidence: the verbatim-span audit trail. If you use it to verify that a
#     block is grounded in the source, you lose that check.
#   * Keywords/Features/Workflows/Personas/Entities cross-refs: these feed
#     graph_traversal.py. Retrieval that walks between block types will
#     degrade. Check whether your retrieval path actually uses them.
#
#   This is a DATA-MODEL tradeoff, not a bug fix. It is off by default.
# ═══════════════════════════════════════════════════════════════════════════

_ALL_TYPES_OUTPUT_FORMAT_COMPACT = """\
Return ONLY blocks in the schema below.

Emit one block per item, numbered sequentially from 1. There is no upper limit
on the number of blocks; a dense window should produce many.

===1===
- Type: <one of: keywords | personas | workflows | features | entities | knowledge>
- SubType: <one value from the sub-type vocabulary>
- Name: <short noun phrase; preserve exact identifier verbatim>
- Content: <verbatim or near-verbatim source passage for this block; preserve identifiers, commands, paths, versions, ports, flags and limits verbatim; do not paraphrase or condense>
- Summary: <one dense answer-first sentence>

The next block repeats the same five fields under a ===2=== marker, then
===3===, and so on until every item in the window has been emitted.

Be terse. Do not restate the same fact in Content and Summary. Do not add
commentary, headings, or any text outside the block schema.

Your reply must begin with the characters ===1=== and contain nothing else
before it. Never reply with an ellipsis, a placeholder, or a restatement of
this schema.
"""

ALL_TYPES_SYSTEM_COMPACT = ALL_TYPES_SYSTEM.replace(
    _ALL_TYPES_OUTPUT_FORMAT, _ALL_TYPES_OUTPUT_FORMAT_COMPACT
)
