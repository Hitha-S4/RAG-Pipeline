# IBM Guardium Data Protection — PERSONAS

**Category:** personas  |  **Generated:** 2026-07-13  |  **Source:** gdp-12.x-documentation 2.pdf

---

## Data & Database Management

### Database Administrator
- **Components:**
  - **Roles:** DBA, DB Admin, Data Admin, GIM User
  - **Responsibilities:**
    - Configure and maintain datasources, database connections, and S‑TAP agents
    - Monitor database performance, apply patches, and manage K‑TAP/KAU
    - Manage GIM installations and updates from the GIM UI or CLI
- **Links:**
  - **Features:** Datasource Configuration, S‑TAP Management, K‑TAP/KAU Management, GIM UI, GIM CLI
  - **Workflows:** Add Datasource, Configure S‑TAP, Apply GIM Patch, Discover Databases, Manage GIM Modules
  - **Knowledge:** Database Connection Architecture, Agent Deployment, GIM Architecture, JDBC, K‑TAP, KAU
  - **Keywords:** GIM, K‑TAP, KAU, JDBC, Datasource, Patch Management

## Compliance & Audit

### Compliance Officer
- **Components:**
  - **Roles:** Compliance Manager, Risk Officer, Audit Manager
  - **Responsibilities:**
    - Define and enforce compliance policies
    - Generate audit reports and verify policy adherence
    - Manage secrets, API keys, and credentials securely
- **Links:**
  - **Features:** Policy Definition, Audit Reporting, Credential Management
  - **Workflows:** Create Compliance Policy, Generate Audit Report, Manage Secrets
  - **Knowledge:** Compliance Standards, Audit Reporting Framework, Secrets Management
  - **Keywords:** Compliance, Audit, RBAC, Secrets, encryption

### Security Analyst
- **Components:**
  - **Roles:** SOC Analyst, Threat Analyst, Incident Responder
  - **Responsibilities:**
    - Investigate security incidents and account takeover attempts
    - Analyze application events and connection profiling data
    - Configure alerts and notifications for risky user activities
- **Links:**
  - **Features:** Incident Management, Application Events, Connection Profiling, Portfolio Risks
  - **Workflows:** Investigate Incident, Create Alert Rule, Analyze Application Events, Review Connection Profiles
  - **Knowledge:** Incident Response Process, Application Event Analysis, Connection Profiling Insights, Account Takeover Detection
  - **Keywords:** Account Takeover, Application Events Entity, Connection Profiling List, Risky Users

## Security Incidents Overview
Security incidents require knowledge of Security Policy Architecture, Certificate Management, and familiarity with FGAC, IAM, LDAP, SSL, and TLS.

---

## Database Administration
### Database Administrator
- **Roles:** DBA, DB Admin, Data Admin, Database Administrator  
- **Responsibilities:** Configure and maintain datasource connections, monitor performance, apply patches, and manage S‑TAP agents.  
- **Links:** Datasource Configuration, Performance Monitoring, S‑TAP Management  
- **Knowledge:** Database Connection Architecture, Agent Deployment  
- **Keywords:** S‑TAP, K‑TAP, GIM, JDBC, Datasource  

---

## Compliance & Audit  

### Compliance Officer  
- **Roles:** Compliance Manager, Risk Officer, Audit Manager, Compliance Officer  
- **Responsibilities:** Ensure compliance with regulatory standards, configure compliance reporting and audits, and monitor risky users/SQL errors.  
- **Links:** Access Control, Risk Assessment, Vulnerability Management  
- **Knowledge:** Regulatory Frameworks, Risk Management, Audit Trails  
- **Keywords:** SOX, GDPR, HIPAA, PCI‑DSS, Audit, Risk  

### Security Analyst  
- **Roles:** SOC Analyst, Threat Analyst, Incident Responder, Security Analyst  
- **Responsibilities:** Investigate incidents (e.g., brute‑force attacks), analyze Guardium VA alerts, and respond to policy violations.  
- **Links:** Alert Management, Vulnerability Assessment, Incident Response  
- **Knowledge:** Threat Detection, Risk Scoring, Security Operations  
- **Keywords:** Brute force attack, Vulnerability Assessment, Incident Response  

---

## Engineering  

### DevOps Engineer  
- **Roles:** Platform Engineer, SRE, Infrastructure Engineer, DevOps Engineer  
- **Responsibilities:** Deploy Guardium components via GIM bundles, perform rollbacks/live upgrades, and monitor Edge Gateway performance.  
- **Links:** GIM Bundle Management, Live Upgrade Recovery, Edge Gateway Management  
- **Knowledge:** Software Deployment, High Availability, Monitoring  
- **Keywords:** GIM, Live Upgrade, Edge Gateway, Monitoring  

### Application Developer  
- **Roles:** Software Engineer, Integration Developer, Application Developer  
- **Responsibilities:** Use Guardium APIs, connect to Guardium Caches, and configure Java or ABAP/Java stacks for data discovery.  
- **Links:** GuardAPI, Cache Access, Data Source Configuration  
- **Knowledge:** API Integration, Data Access Patterns, Stack Configurations  
- **Keywords:** GuardAPI, Revocation API, Cache, ABAP, Java Stack  

---

## Administration  

### Administrator  
- **Roles:** Super Administrator, Platform Admin, Global Administrator, Security Administrator  
- **Responsibilities:** Manage users, roles, and platform configuration; define FGAC policies; control feature access; monitor violations; customize navigation; configure datasources; assign minimal roles; handle patching, certificates, incident monitoring, reporting, provisioning, password changes, license management, audit logs, custom partitioning, GIM bundle cleanup, REST API operations, and custom user roles.  
- **Links:** Role Management, Access Control, FGAC Policy Management, Dashboard Customization, Datasource Configuration, Policy Violations, REST API, Custom Partitioning, License Management, Audit Logs  
- **Workflows:** Create/Assign Roles, User & Navigation Customization, Patch Management, Certificate Configuration, Incident Monitoring, Report Generation, User Provisioning, Password Reset, License Application, Audit Review, Partition Configuration, GIM Cleanup, API Operations, Role Definition  
- **Knowledge:** Access Control Architecture, FGAC Policies, Platform Configuration, Security Monitoring, Data Source Management, License Types, Audit Process, Custom Partitioning Guidelines  
- **Keywords:** Super Admin, IAM, FGAC, RBAC, ANCHOR, REST API, Setup, GIM, S-TAP, FGAC, Custom Roles  

### Security Administrator  
- **Roles:** Security Admin, FGAC Admin, IAM Administrator  
- **Responsibilities:** Define/enforce FGAC policies, configure certificates/IAM for least‑privilege access, monitor violations, approve S‑TAP connections, manage log ingestion roles, remove unused GIM bundles, apply license keys, perform security assessments, create integration users/roles, configure risk‑spotter via API, and access user comments on Guardium components.  
- **Links:** FGAC Policy Management, Certificate Configuration, S-TAP Approval, Log Ingestion Role, GIM Bundle Management, License Management, VA Tests, Comments, Integration Roles, REST API, Custom Part

## Partitioning
- **Workflows:** Custom Partitioning Planning
- **Knowledge:** Custom Partitioning Guidelines

## Compliance & Audit
### Compliance Officer
- **Roles:** Audit Manager, Compliance Manager, Risk Officer
- **Responsibilities:** Manage and track audit tasks, ensure policies documented and enforced
- **Links:** Features: Audit Process To-Do List, Policy Management
- **Knowledge:** Audit Process Architecture, Policy Documentation