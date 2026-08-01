"""ENTITIES prompt — depends on: knowledge."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes) ──────────────────────────────

SYSTEM_ENTITIES_NOTES = (
    _ROLE
    + "The CONTEXT block (if present) contains knowledge summaries — use them "
    "to correctly type and describe entities.\n\n"
    "Extract named system objects the product manages (NOT features or workflows).\n"
    "Examples: agents, policies, nodes, services, credentials, databases.\n\n"
    "For EACH numbered excerpt output EXACTLY this block, replacing N:\n\n"
    "===1===\n"
    "- Name: <entity name — exact terminology>\n"
    "- Type: <policy | agent | node | service | database | api | "
    "configuration | credential | tool | report | component | other>\n"
    "- Description: <COMPLETE 2-3 sentences: what this object is and what it "
    "does in the product — never truncate>\n\n"
    "===2===\n"
    "- Name: ...\n"
    "- Type: ...\n"
    "- Description: ...\n\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_ENTITIES_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT (known concepts — helps you name objects correctly; no fact import):
{context}

ENTRIES:
{chunks}

Write the entity note blocks now."""

# ── Concise MD builder prompt (used by _build_concise_from_raw) ───────────────

SYSTEM_ENTITIES = _G + """Write a high-level entity reference grouped by system domain.
Merge entries about the same object into one block.

Output EXACTLY this shape:

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Type:** appliance
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

---

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

---

RULES:
0. Any product names in the examples above are ILLUSTRATIVE ONLY. Extract from the actual input text - never copy example content.
1. "## Category" headings group related entities (Agents & Collectors,
   Policies & Rules, Databases & Datasources, Credentials & Certificates,
   APIs & Tools, Infrastructure, Cloud Services).
   MERGE all entries about the same object into ONE block (G4).
2. ENTITY TEST — only include named system objects (noun phrases):
   * Sentences or instructions ("You do not need to restart…") → SKIP.
   * Page artifacts ("<Product> 899") or table labels → SKIP (G2/G5).
3. "**Type:**" one word: agent | appliance | policy | service | database |
   api | configuration | credential | certificate | tool | report | connector.
4. **Description:** 1-2 COMPLETE sentences (G1). For header-only entries:
   *Named entity identified in source; detailed content not extracted.*
5. End every category section with a line containing only: ---"""

USER_ENTITIES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT (known concepts — helps you name objects correctly; no fact import):
{context}

ENTRIES:
{chunks}

Write the grouped entity reference now."""
