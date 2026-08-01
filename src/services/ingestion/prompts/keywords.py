"""KEYWORDS prompt — depends on: knowledge, features, entities."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes / classify pass) ──────────────

SYSTEM_KEYWORDS_NOTES = (
    _ROLE
    + "Extract ONLY project-specific terms and acronyms — NO generic English words.\n"
    "Include: component names, agent names, protocol names, named technologies,\n"
    "compliance standards, product-specific parameters, configuration objects.\n"
    "EXCLUDE: generic words like 'user', 'policy', 'data', 'system', 'server'.\n\n"
    "Each ===N=== block may contain MULTIPLE Term lines — one per distinct term.\n\n"
    "===1===\n"
    "- Term: S-TAP(Software TAP): IBM Guardium software agent that captures and forwards database traffic from monitored servers to a Guardium Collector.\n"
    "- Term: Collector(Collector): Guardium appliance that receives activity data from S-TAP agents, applies policies, and stores audit records.\n\n"
    "===2===\n"
    "- Term: GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.\n\n"
    "FORMAT: - Term: ACRONYM(Full Name): One complete sentence — what it IS and what it does.\n"
    "If not an acronym: TermName(TermName): definition.\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_KEYWORDS_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Extract project-specific keywords only — be thorough, no generic words."""

# ── Concise MD builder prompt (Layer-1 pass) ─────────────────────────────────
# Receives RAW-MD summaries; outputs a flat, deduplicated term list.
# NOTE: KEYWORDS intentionally bypasses the generic Layer-2 COMPRESS_SYSTEM.
#       A dedicated _compress_keywords() post-filter in service.py enforces
#       the final one-line-per-term format instead.

SYSTEM_KEYWORDS = _G + """Build a project-specific keyword glossary.

INPUT NOTE FORMAT — each entry arrives as:
  - TERM:
    <content describing what the term is or does>
Use the TERM name verbatim. Extract the full-name expansion and definition from
the content. If the content contains no definition (e.g. it's a release-note
enhancement paragraph), write a one-sentence definition from what the content says.

STRICT OUTPUT FORMAT — every output line must follow this pattern exactly:
  TERM(Full Name): One complete sentence describing what it IS and what it DOES.

Examples:
  A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.
  Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.
  CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.
  Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.
  FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
  GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.
  GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
  K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.
  S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.
  S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

STRICT RULES — violating any rule makes the output unusable:
0. Any product names in the examples above are ILLUSTRATIVE ONLY. Extract from the actual input text - never copy example content.
1. ONE term per line. No bullets (- or *), no ## headings, no category labels,
   no blank lines between terms, no prose paragraphs, no numbered lists.
2. Format: TERM(Full Name): sentence.
   Acronym  → ACRONYM(Full Expansion): sentence.
   Not an acronym → TermName(TermName): sentence.
3. ONE complete sentence per term — never truncate mid-word or mid-clause (G1).
4. ONLY product-specific terms: component names, agent names, protocol names,
   named technologies, compliance standards, product-specific parameters.
   EXCLUDE generic words: user, policy, data, server, system, configuration,
   management, database, file, report, application, service, network, security,
   access, control, feature, module, component, process, tool, type, mode.
5. DEDUPLICATE — each term appears exactly once; merge variant definitions (G4).
6. Sort A→Z by the term identifier (the part before the first parenthesis).
7. Aim for 60-120 terms from the provided entries and context combined.
8. NO section headers, NO overview paragraphs, NO prose of any kind.
   If the input contains a section like "## Overview of Guardium Architecture"
   or "## Key Modules and Components" — IGNORE it entirely, do not copy it."""

USER_KEYWORDS = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the project-specific keyword glossary — alphabetical A→Z, one term per line, \
no headings, no bullets, no prose."""
