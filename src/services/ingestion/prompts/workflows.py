"""WORKFLOWS prompt — depends on: knowledge, features."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes / classify pass) ──────────────

SYSTEM_WORKFLOWS_NOTES = (
    _ROLE
    + "Extract workflow information from each excerpt.\n\n"
    "Classify type as: Navigation | Configuration | Action.\n"
    "  Navigation    → view, monitor, report, audit, dashboard\n"
    "  Configuration → setup, install, configure, enable, deploy, upgrade\n"
    "  Action        → protect, enforce, rotate, revoke, block, detect\n\n"
    "For EACH numbered excerpt output EXACTLY this block:\n\n"
    "===1===\n"
    "- Name: <workflow name — leaf heading, no page numbers>\n"
    "- Type: <Navigation | Configuration | Action>\n"
    "- Pre-requisites: <required conditions from text; omit if none>\n"
    "- Step 1: <first action>\n"
    "- Step 2: <second action>\n"
    "- Step 3: <third action; add more if present>\n"
    "- APIs/Tools: <commands, APIs, tools named; omit if none>\n\n"
    "===2===\n"
    "- Name: ...\n"
    "- Type: ...\n"
    "- Pre-requisites: ...\n"
    "- Step 1: ...\n"
    "- Step 2: ...\n"
    "- Step 3: ...\n"
    "- APIs/Tools: ...\n\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_WORKFLOWS_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the workflow note blocks now."""

# ── Concise MD builder prompt ─────────────────────────────────────────────────

SYSTEM_WORKFLOWS = _G + """Write a structured workflow reference matching this EXACT schema.

INPUT NOTE FORMAT — each entry arrives as:
  - Workflow Name [sub_type]:
    <content: steps, prerequisites, API commands, navigation paths>
Extract the workflow name verbatim, map the sub_type to a Type
(install/upgrade → Configuration; configure/administer → Configuration;
use → Action; monitor/reference → Navigation), and derive steps from the content.

Each workflow must have: Components (Pre-requisites, Execution Steps, APIs/Tools),
Types (Navigation | Configuration | Action), and optionally Customization (User workflows).

Output EXACTLY this shape:

## Datasource Configuration

### Configure MS SQL Server Datasource
- **Components:**
  - **Pre-requisites:** SQL Server installed and running; network connectivity verified
  - **Execution Steps:**
    1. Gather SQL Server hostname, port, and authentication method
    2. Navigate to **Datasources > Add Datasource** and select connection type
    3. Enter connection details and click **Test Connection**
    4. Save the datasource configuration
  - **APIs/Tools:** GuardAPI, grdapi add_datasource
- **Types:** Configuration
- **Customization:**
  - **User workflows:** Clone datasource template for faster repeated setup

---

## Access Control

### Configure Fine-Grained Access Control
- **Components:**
  - **Pre-requisites:** Administrator role assigned; security policy defined
  - **Execution Steps:**
    1. Navigate to **Setup > Access Control > FGAC**
    2. Define roles and object-level permissions
    3. Assign roles to user accounts
    4. Test access with a restricted user account
  - **APIs/Tools:** grdapi set_access_rule
- **Types:** Configuration

---

RULES:
1. Group workflows under "## Category" headings (adapt to source domain).
   MERGE workflows for the same task into ONE entry (G4).
2. Workflow name = clean task name (G2/G3). No page numbers or fragments.
3. Components > Pre-requisites: state exactly what is required before starting.
4. Components > Execution Steps: numbered list, each a COMPLETE action (G1).
   If entry is header-only write: *Detailed steps in source documentation.*
5. Components > APIs/Tools: exact command names and GUI paths — omit if none.
6. Types: one of Navigation | Configuration | Action.
7. Customization > User workflows: only when entry describes user-specific variants.
8. End every category with a line containing only: ---"""

USER_WORKFLOWS = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the structured workflow reference now."""
