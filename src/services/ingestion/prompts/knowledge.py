"""KNOWLEDGE prompt — generated LAST; synthesises all other category outputs."""
from ._shared import _ROLE, _G

# ── RAW-MD notes prompt (used by generate_notes / classify pass) ──────────────

SYSTEM_KNOWLEDGE_NOTES = (
    _ROLE
    + "Synthesize a knowledge topic from each excerpt.\n"
    "Fix OCR artefacts in headings (e.g. rejoin split words like 'Data base' → 'Database'; strip page numbers).\n\n"
    "For EACH numbered excerpt output EXACTLY this block:\n\n"
    "===1===\n"
    "- Topic: <clean concept name — no page numbers, no raw OCR>\n"
    "- Summary: <2-4 complete sentences: what it is, how it works, why it matters>\n"
    "- Keywords: <6-10 product-specific terms, comma-separated>\n\n"
    "===2===\n"
    "- Topic: ...\n"
    "- Summary: ...\n"
    "- Keywords: ...\n\n"
    "Output ONLY the ===number=== blocks. Nothing else."
)

USER_KNOWLEDGE_NOTES = """SOURCE: {doc_name} | DATE: {export_date}
{context}
ENTRIES:
{chunks}

Write the knowledge note blocks now."""

# ── Master knowledge MD prompt (generated last, with all category context) ────

SYSTEM_KNOWLEDGE = _G + """Write the MASTER knowledge document for this source.
It has two parts:

PART 1 — Document Overview (the first ## section):
  A high-level summary of the entire source document:
  - What product / subsystem it covers
  - Its primary purpose and capabilities
  - Key personas, entities, and workflows addressed
  Then four overview sub-sections — each a brief bullet list:
  - Features Overview
  - Workflows Overview
  - Personas Overview
  - Entities Overview

PART 2 — Knowledge Sections:
  Detailed knowledge entries — one ## section per distinct concept area.

Output EXACTLY this shape:

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring
and security platform. It provides real-time monitoring, policy enforcement,
vulnerability assessment, and compliance reporting across structured and
unstructured data stores, both on-premises and in the cloud.

### Features Overview
- **Datasource Connectivity:** Dynamic port detection, multi-driver support, CyberArk credential vault integration
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation
- **Compliance & Reporting:** PCI-DSS, GDPR, HIPAA, SOX report templates; automated audit trails

### Workflows Overview
- **Configuration:** Add datasource, deploy S-TAP via GIM, configure FGAC policies
- **Navigation:** Review activity reports, run vulnerability assessments, audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents

### Personas Overview
- **Administration:** Administrator (platform config, user management), Security Administrator (FGAC, policies)
- **Data & Database Mgmt:** Database Administrator (datasources, S-TAP), Data Analyst (dashboards, queries)
- **Compliance & Audit:** Compliance Officer (regulatory reports), Security Analyst (threat investigation)

### Entities Overview
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector

---

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases,
including native drivers for optimized performance and generic drivers for broad
compatibility. A browser service resolves instance names to current ports dynamically.

**Key Concepts:** JDBC, Native Driver, Browser Service, Dynamic Port Detection

---

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents and evaluates it in
real time against configured security policies. Violations trigger alerts, reports,
or blocking via S-GATE. Policies can target specific users, objects, operations,
and time windows.

**Key Concepts:** S-TAP, S-GATE, Security Policy, Real-Time Monitoring, Audit Trail

---

RULES:
0. The worked example above is ILLUSTRATIVE ONLY (it happens to use a database
   security product). Write about whatever product the CONTEXT and ENTRIES
   actually describe — never copy names, components, or facts from the example.
1. PART 1 Document Overview is ALWAYS the first ## section.
   Use the CONTEXT (other category files) to populate all four overview sub-sections.
   Each overview sub-section: 3-6 bullet items, each a "**Topic:** brief phrase" line.
2. PART 2 Knowledge Sections: one ## per DISTINCT concept area.
   MERGE all entries about the same area (G4).
   Body: 2-3 complete sentences (G1). No parameter tables (G5).
3. **Key Concepts:** line ends every knowledge section.
4. Section titles: clean noun phrases (G2/G3); no page numbers, no OCR artifacts.
5. End every section with a line containing only: ---"""

USER_KNOWLEDGE = """SOURCE: {doc_name} | DATE: {export_date}
CONTEXT (summaries from FEATURES, WORKFLOWS, PERSONAS, ENTITIES, KEYWORDS already generated):
{context}

ENTRIES:
{chunks}

Write the master knowledge document now — Document Overview first, then knowledge sections."""
