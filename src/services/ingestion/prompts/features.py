"""FEATURES prompt — depends on: knowledge."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes / classify pass) ──────────────

SYSTEM_FEATURES_NOTES = (
    _ROLE
    + "Extract feature information from each excerpt.\n\n"
    "For EACH numbered excerpt output EXACTLY this block:\n\n"
    "===1===\n"
    "- Name: <exact feature name from excerpt>\n"
    "- Description: <1-2 complete sentences: what it does and its benefit>\n"
    "- Support matrix: <platforms/databases/versions — comma-separated; omit if absent>\n"
    "- Limitations: <constraints or unsupported cases — comma-separated; omit if absent>\n"
    "- Workflow types: <Navigation | Configuration | Action — comma-separated>\n"
    "- Related knowledge: <2-3 concept names from excerpt or CONTEXT>\n"
    "- Keywords: <4-6 product-specific terms, comma-separated>\n\n"
    "===2===\n"
    "- Name: ...\n"
    "- Description: ...\n"
    "- Support matrix: ...\n"
    "- Limitations: ...\n"
    "- Workflow types: ...\n"
    "- Related knowledge: ...\n"
    "- Keywords: ...\n\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_FEATURES_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the feature note blocks now."""

# ── Concise MD builder prompt ─────────────────────────────────────────────────

SYSTEM_FEATURES = _G + """Write a structured feature reference matching this EXACT schema.

INPUT NOTE FORMAT — each entry arrives as:
  - Feature Name [sub_type]:
    <content: what the feature does, supported platforms, constraints, limits>
Extract the feature name verbatim. Use the content to populate Support Matrix
(platforms/databases/versions stated), Limitations/Constraints (restrictions stated),
and derive relevant Workflow types from the sub_type and content.

Each feature must have: Components (Support Matrix, Limitations/Constraints,
Workflow types) and Links (Knowledge, Keywords).

Output EXACTLY this shape:

## Datasource Connectivity

### Dynamic Port Detection
- **Components:**
  - **Support Matrix:** SQL Server, Oracle, Db2, MySQL
  - **Limitations/Constraints:** Requires browser service running; not supported on z/OS
  - **Workflows with different types:** Configuration — Add Datasource; Navigation — View Ports
- **Links:**
  - **Knowledge:** Database Connection Architecture, Browser Service
  - **Keywords:** S-TAP, Collector, JDBC, Browser Service

### CyberArk Integration
- **Components:**
  - **Support Matrix:** All Guardium-supported databases
  - **Limitations/Constraints:** CyberArk SDK export restrictions apply in some regions
  - **Workflows with different types:** Configuration — Install CyberArk SDK
- **Links:**
  - **Knowledge:** Credential Management, Dynamic Secrets
  - **Keywords:** CyberArk SDK, Credential Vault

---

RULES:
0. Any product names in the examples above are ILLUSTRATIVE ONLY. Extract from the actual input text - never copy example content.
1. Group features under "## Category" headings (adapt to source domain).
   MERGE features about the same capability into ONE entry (G4).
2. Feature name = clean noun phrase (G2/G3).
3. Components > Support Matrix: list supported platforms/databases/versions.
4. Components > Limitations/Constraints: documented constraints only — omit if none.
5. Components > Workflows with different types: list as "Type — Workflow Name" pairs.
6. Links > Knowledge: 2-4 related knowledge concept names.
7. Links > Keywords: 4-8 product-specific terms (no generic words).
8. All bullet values: complete phrases, never truncated (G1).
9. End every category with a line containing only: ---"""

USER_FEATURES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the structured feature reference now."""
