"""PERSONAS prompt — depends on: knowledge, features, entities."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes / classify pass) ──────────────

SYSTEM_PERSONAS_NOTES = (
    _ROLE
    + "Identify the user persona implied by each excerpt.\n\n"
    "Map to EXACTLY one canonical archetype — never invent names, never output 'User':\n"
    "  Administrator, Security Administrator, Database Administrator,\n"
    "  Compliance Officer, DevOps Engineer, Data Analyst, Security Analyst,\n"
    "  Application Developer, IT Manager, Operator.\n\n"
    "MERGE RULE: same archetype in multiple excerpts → same persona name always.\n\n"
    "For EACH numbered excerpt output EXACTLY this block:\n\n"
    "===1===\n"
    "- Persona: Administrator\n"
    "- Roles: Super Administrator, Platform Admin\n"
    "- Responsibilities: Manage user accounts; assign roles; configure platform settings\n"
    "- Features used: Role Management, Access Control, User Menu Customization\n"
    "- Workflows run: Create User, Assign Role, Configure Navigation\n\n"
    "===2===\n"
    "- Persona: <canonical archetype>\n"
    "- Roles: <comma-separated product role names — exact names from text>\n"
    "- Responsibilities: <semicolon-separated action phrases from excerpt>\n"
    "- Features used: <comma-separated feature names>\n"
    "- Workflows run: <comma-separated workflow names>\n\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_PERSONAS_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the persona note blocks now."""

# ── Concise MD builder prompt ─────────────────────────────────────────────────

SYSTEM_PERSONAS = _G + """Write a structured persona reference matching this EXACT schema.
Each persona must have: Components (Roles, Responsibilities) and Links
(Features, Workflows, Knowledge, Keywords). Group by domain.

Output EXACTLY this shape:

## Administration

### Administrator
- **Components:**
  - **Roles:** Super Administrator, Platform Admin, Global Administrator
  - **Responsibilities:**
    - Manage user accounts, roles, and platform-wide configuration
    - Control access to features and tools via Setup Tools and Views
    - Customize navigation menus per user or role
- **Links:**
  - **Features:** Role Management, User Menu Customization, Access Control
  - **Workflows:** Create User, Assign Role, Configure Navigation Menu
  - **Knowledge:** Access Control Architecture, Platform Configuration
  - **Keywords:** RBAC, FGAC, Setup Tools

### Security Administrator
- **Components:**
  - **Roles:** Security Admin, FGAC Admin, IAM Administrator
  - **Responsibilities:**
    - Define and enforce fine-grained access control policies
    - Configure certificates and IAM policies for least-privilege access
    - Monitor and respond to security policy violations
- **Links:**
  - **Features:** FGAC Policy Management, Certificate Configuration
  - **Workflows:** Configure IAM Policy, Enable FGAC, Review Security Incidents
  - **Knowledge:** Security Policy Architecture, Certificate Management
  - **Keywords:** FGAC, IAM, LDAP, SSL, TLS

---

## Data & Database Management

### Database Administrator
- **Components:**
  - **Roles:** DBA, DB Admin, Data Admin
  - **Responsibilities:**
    - Configure and maintain datasources and database connections
    - Monitor database performance and apply patches
    - Manage S-TAP agents on database servers
- **Links:**
  - **Features:** Datasource Configuration, Performance Monitoring, S-TAP Management
  - **Workflows:** Add Datasource, Configure S-TAP, Apply GIM Patch
  - **Knowledge:** Database Connection Architecture, Agent Deployment
  - **Keywords:** S-TAP, K-TAP, GIM, JDBC, Datasource

---

ROLE NORMALISATION — map variants to canonical archetypes:
  Administrator         ← Super Administrator, Super Admin, Platform Admin, Global Administrator
  Security Administrator ← Security Admin, FGAC Admin, IAM Administrator, Permission Manager
  Database Administrator ← DB Admin, DBA, Database Manager, Data Admin
  Compliance Officer    ← Compliance Manager, Risk Officer, Audit Manager, Privacy Officer
  DevOps Engineer       ← Platform Engineer, SRE, Infrastructure Engineer, Deployment Engineer
  Data Analyst          ← Business Analyst, Reporting Analyst, BI Analyst
  Security Analyst      ← SOC Analyst, Threat Analyst, Incident Responder
  Application Developer ← Developer, API Consumer, Software Engineer, Integration Developer
  IT Manager            ← IT Director, Operations Manager, Service Manager
  Operator              ← System Operator, Tier-1 Support, Service Desk

GROUPING — assign to these domain sections:
  Administration        → Administrator, Security Administrator
  Data & Database Mgmt  → Database Administrator, Data Analyst
  Compliance & Audit    → Compliance Officer, Security Analyst
  Engineering           → DevOps Engineer, Application Developer
  Operations            → IT Manager, Operator

RULES:
1. ONE block per canonical archetype — MERGE all variants (G4).
2. Components > Roles: list exact source role names absorbed into this archetype.
3. Components > Responsibilities: bullet phrases, 3-6 items max, no duplication.
4. Links > Features/Workflows/Knowledge/Keywords from entries + CONTEXT — no invention.
5. Omit a domain group if none of its archetypes appear in the entries.
6. End every domain group with a line containing only: ---"""

USER_PERSONAS = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT:
{context}

ENTRIES:
{chunks}

Write the structured persona reference now."""
