# Permissionstodynamicrolesandcredsfordifferentpaths — KNOWLEDGE

**Category:** knowledge  |  **Generated:** 2026-07-09  |  **Source:** gdp-12.x-documentation.pdf

---
## Configure Datasource Connectivity
Add data sources to Guardium using the management interface. Supply connection details relevant to the database type, including hostname, port, database name, user credentials, and optional SSL/TLS parameters. For cloud databases, provide the service endpoint and credentials.

## Manage Threat Detection Policies
Define security policies using the GUI to monitor database activities. Configure rule sets to detect SQL injection, privilege abuse, and data exfiltration. Use Guardium’s rule builder to add conditions based on users, objects, commands, and data values; assign severity levels and blocking actions for detected violations. Create audit trails and configure automatic incident generation upon rule hits.

## Implement and Maintain Inspection Engines
Deploy and configure Linux-UNIX inspection engines through Guardium’s GIM agent. Set audit parameters like log file locations, retention periods, and privileged user logging. Utilize cockroachDB and Couchbase support for NoSQL auditing. Periodically update inspection rules to cover new application requirements and regulatory changes.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection (GDP) provides comprehensive database security and compliance across heterogeneous environments. It supports real-time monitoring, policy enforcement, vulnerability assessments, and integrates with AWS Secrets Manager for credential management.

### Key Features
- **DataSource Connectivity:** JDBC, native drivers, and dynamic port detection.
- **Threat Detection:** Real-time S-TAP monitoring, S-GATE blocking, and incident response.
- **Compliance Reporting:** Pre-built templates for PCI-DSS, GDPR, HIPAA, SOX.
- **Secrets Management:** Integration with AWS Secrets Manager for secure credential handling.

### Main Workflows
- **Configuration:** Adding datasources, deploying S-TAP agents via GIM, defining FGAC policies.
- **Monitoring:** Using dashboards, reports, and alerts for real-time visibility.
- **Remediation:** Blocking unauthorized access and rotating credentials.

**IBM Guardium Data Protection Overview**

IBM Guardium Data Protection is a comprehensive platform that safeguards structured and unstructured data across on‑premise and cloud environments. It continuously monitors database activity, identifies threats in real time, supports regulatory compliance, and delivers actionable insights for security and data governance teams.

### Key Features
- Data source connectivity: Dynamic port detection, multi-driver support, CyberArk vault integration
- Threat prevention: S‑GATE real‑time blocking, rule‑based policy enforcement
- Compliance reporting: PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit logging
- Cost insight analysis: Visualizes financial impact of data risks in customizable units

### Primary Workflows
1. **Data Source Connectivity**
   - JDBC connectors with native and generic drivers
   - Dynamic resolution of hostnames to ports
   - Credential retrieval from AWS Secrets Manager or CyberArk vaults
2. **Threat Prevention & Blocking**
   - Define FGAC policies, manage compliance reports, and block unauthorized queries
   - Rotate credentials automatically and trigger incident response actions
3. **Compliance & Reporting**
   - Generate audit reports, modify datasource custom properties, and run discovery scenarios
   - View Process Run Log for verification and data analysis
4. **Cost Insight Analysis**
   - Customize reporting units (U.S. dollars or person‑hours) to assess risk financial impact

## Guardium High‑Level Overview

### Configuration, Monitoring, Threat Response, Cost Governance
- **Configuration:** add data sources, deploy S‑TAP agents via Guardium Installation Manager (GIM) or API, define FGAC policies  
- **Monitoring:** view activity reports, run vulnerability scans, navigate audit dashboards  
- **Threat Response:** block illegitimate queries, rotate credentials, generate security incidents  
- **Cost Governance:** configure and review cost‑impact visualizations in dollars or labor‑hours  

### Personas  
- **Security Administrator:** manages policies, access control, incident response  
- **Compliance Officer:** runs regulatory templates, maintains audit artifacts, generates compliance reports  
- **Data Analyst:** consumes dashboards, runs ad‑hoc queries, creates custom cost‑impact views  
- **Operations Engineer:** handles deployment, patching, HA setup of Guardium components  

### Key Entities  
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregators, Central Manager  
- **Policy Entities:** Security Policies, Audit Policies, Classification Rules, Access Rules  
- **Infrastructure:** GIM, Managed Units, S‑GATE blocking gateway, Universal Connectors  
- **Reporting:** Dashboards, Audits, Cost‑Governance Views, Policy Exception Lists  

### Dual‑Unit Cost Display  
Enables executives to view financial impact of data‑risk mitigation in either U.S. dollars or person‑hours, improving communication of security ROI.

### Aggregator Appliance  
Acts as a central management node, providing federated management of multiple collectors/aggregators, unified credential management, automated patch distribution, and metadata storage for reporting.

### Adding Custom MSSQL Properties via GRDAPI  
```json
{
  "command": "add_datasource_custom_property",
  "parameters": {"dataSourceName":"MyMSSQL","propertyName":"TRANSACTION-ISOLATION-LEVEL","value":"SNAPSHOT"}
}
{
  "command": "add_datasource_custom_property",
  "parameters": {"dataSourceName":"MyMSSQL","propertyName":"MAXDOP","value":"4"}
}
```
See Guardium *Custom Properties Documentation* for full list.

### Apache Cassandra Configuration  
- RPM: `/home/cassandra/apache-cassandra-4.x/conf`  
- .tar: `$INSTALLPATH/conf`  
Refer to *Cassandra Datasource Guide* and *Aster Data Source Configuration* for troubleshooting.

### Log and SSL Parameters for MySQL  
- `log_error` – error log path  
- `general_log_file` – general query log path  
- `relay_log_basename` – relay log base name  
- `ssl_dir` – SSL certificate directory  

### Typical Datasource Definition  
- **Host Name/IP** (required)  
Additional parameters see vendor‑specific documentation.  

### Kubernetes Deployments  
- **Pods:** containerized Guardium instances  
- **Aggregator:** central management pod  
- **UI Banner:** user web interface  
- **Scanner:** scheduled vulnerability scans  

Common issues: TLS certificate hostname mismatches, resource constraints, network connectivity, scanner misconfiguration. See *Guardium Deployment Guide* for remediation.

### Neo4j Data Source Setup  
1. Verify authentication support: local user (yes), LDAP (no), Kerberos (no), SSL (yes, yes for mutual).  
2. Configure mandatory fields: *Host* (IP/hostname).  
Full parameter list in *Neo4j Datasource Configuration*.

### AWS Secrets Manager / Database Authentication  
Guardium can use temporary credentials from AWS Secrets Manager, providing automatic rotation and eliminating long‑term key storage for AWS databases.

## ## Introduction to IBM Guardium Data Protection
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### ## Feature Overview
- **Database Connectivity:** Supports multiple JDBC driver families, native and generic drivers, dynamic port detection via browser service  
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation, Active Threat Analytics  
- **Compliance & Reporting:** PCI-DSS, GDPR, HIPAA, SOX report templates, automated audit trails  
- **Image Management:** REST API for downloading Edge Gateway images in single tar archive  

### ## Workflows Overview
- **Configuration:** Add datasources, deploy S-TAP via GIM, configure FGAC policies  
- **Activity Monitoring:** Real-time traffic capture via S-TAP agents, policy evaluation, alerting/blocking via S-GATE  
- **Upgrade Management:** Installation and upgrade procedures through appliance management interface  
- **Agent Updates:** Installation/release notes for S-TAP, GIM, and CAS agents  

### ## Personas Overview
- **Administration:** Administrators manage platform configuration and user access  
- **Data Security:** Security Administrators configure policies, manage threats  
- **Database Management:** DBAs handle datasources and S-TAP deployment  
- **Compliance:** Compliance Officers generate regulatory reports, manage audit trails  

### ## Entities Overview
- **Agents:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager  
- **Policies:** Security Policies, Audit Policies, Classification Rules, Access Rules  
- **Infrastructure:** Managed Unit, S-GATE, Universal Connector  

### ## Database Connection Architecture
IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

### ## Activity Monitoring & Policy Enforcement
IBM Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

### ## Threat Detection & Advanced Analytics
IBM Guardium's Active Threat Analytics feature identifies potential security breaches by analyzing outlier mining results and symptoms of attacks. It provides dashboards for viewing and investigating breach cases, illustrating advanced threat detection and response capabilities.

### ## Policy Management
IBM Guardium policies include rules that define conditions and actions for monitoring database activities. Multiple policies can be installed simultaneously, and actions are triggered based on rule matches, highlighting a core feature for database activity control and monitoring.

### ## Agent Management & Updates
IBM Guardium supports various agents including S-TAP, A-TAP, K-TAP, Collector, Aggregator, and Central Manager, which capture and transmit database activity data. Release notes for these agents detail new features and enhancements.

### ## Atlas Service Integration
IBM Guardium integrates with Hortonworks and Cloudera 7 platforms, specifically supporting the Atlas service in Ranger HDFS. This integration enhances data governance and security capabilities within big data environments.

IBM Guardium Data Protection: Enterprise Database Activity Monitoring and Security Overview

### Features
- **Datasource Connectivity:** Supports native and generic JDBC drivers with dynamic port detection; integrates with CyberArk credential vault.
- **Threat Detection:** Real-time monitoring and S-GATE policy enforcement; generates security incidents.
- **Compliance & Reporting:** Provides PCI-DSS, GDPR, HIPAA, and SOX report templates; automates audit trails.

### Workflows
- **Configuration:** Add datasources, deploy S-TAP agents via GIM, configure FGAC policies.
- **Navigation:** Review activity reports, run vulnerability assessments, use audit dashboard.
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents.

### Personas
- **Administration:** Administrator (platform config, user management) and Security Administrator (FGAC, policies).
- **Data & Database Management:** Database Administrator (datasources, S-TAP) and Data Analyst (dashboards, queries).
- **Compliance & Audit:** Compliance Officer (regulatory reports) and Security Analyst (threat investigation).

### Core Components
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule.
- **Infrastructure:** Installation Manager (GIM), Managed Units, S-GATE, Universal Connector.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise security platform for safeguarding structured and unstructured data across on-premises and cloud environments. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Key Features
- **Compliance Reporting:** Generates PCI-DSS, GDPR, HIPAA, and SOX audit reports
- **Data Discovery & Classification:** Automatically identifies and classifies sensitive data
- **Policy Management:** Creates granular security policies and access rules
- **Threat Detection:** Employs real-time monitoring and anomaly detection
- **Credential & Identity Management:** Defines permissions for roles and secrets

### Core Components
- **Datasource Connectivity:** Supports JDBC, native drivers, and dynamic port detection
- **Threat Detection:** Uses S-TAP agents and S-GATE for real-time policy enforcement
- **Compliance & Reporting:** Offers PCI-DSS, GDPR, HIPAA, and SOX report templates
- **Admin:** Central Manager for managing agents, collectors, and connectors

### Guardium Overview
IBM Guardium Data Protection offers enterprise-level database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data stores across hybrid environments.  

### Features
- Dynamic database connectivity with automatic port detection and driver selection  
- Real-time monitoring, immediate policy enforcement, and S-GATE blocking capabilities  
- Comprehensive compliance reporting for PCI-DSS, GDPR, HIPAA, and SOX  
- Risk scoring, user behavior analytics, and privileged session management  

### Personas
- **Administration:** Global Admin, Auditee Admin  
- **Security:** Security Architect, SOC Analyst  
- **Data Operations:** DBA, Application Owner  
- **Compliance:** Compliance Manager, GRC Analyst  

### Core Entities
- Agents/collectors: S-TAP, A-TAP, K-TAP, Central Manager  
- Policy constructs: Guardium Groups, Exception Rules, Assessment Schedules  
- Infrastructure: Aggregators, S-GATE appliances, Universal Connectors  

## Certificate Fingerprint Format
Guardium supports SHA-256 for robust certificate validation, enabling secure communications and data integrity verification.  

## Database Connection Architecture
Guardium uses JDBC drivers optimized for performance, with generic drivers for broader compatibility. Dynamic port detection managed via browser service resolves instance names to current port assignments, enhancing flexibility and security in database connectivity.

## Key Sections

### Audit Logger Configuration
- Determines log format, retention, rotation, and destination
- Critical for compliance and security monitoring

### Certificate Display
- Shows certificates in PEM format with metadata and SAN entries

### Firewall Chain Management
- Uses custom chains for modular rule application
- Chains are cleaned before use

### Database Connection Architecture
- Supports JDBC with native and generic drivers
- Dynamic port detection via browser service

### Activity Monitoring & Policy Enforcement
- Captures database traffic via S-TAP
- Enforces real-time policies through S-GATE

### Personas Overview
- **Administration:** Platform config, user management
- **Security:** FGAC policies, security administration
- **Database Management:** Datasource config, S-TAP deployment
- **Compliance:** Regulatory reports, audit trails

### Entities Overview
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, collectors
- **Policies & Rules:** Security, audit, classification, access
- **Infrastructure:** GIM, managed units, S-GATE, universal connectors

## API parameters

In Guardium APIs, a number sign (#) preceding a parameter indicates that the parameter is optional and not required for successful execution.

## Central manager

The Guardium Central Manager displays CPU usage statistics for all managed units and collectors in the deployment.

## Configuration comments

Guardium's configuration files support comments, which allow administrators to add descriptive text about specific settings.

## CPU monitoring

For optimal performance, monitor CPU utilization in relation to activity levels in Guardium systems.

## API versioning

API endpoint descriptions in Guardium include version numbers at the top, indicating compatibility with specific Guardium releases.

## S-TAP agents

Guardium's management console shows the hostnames of connected S-TAP agents.

## A-TAP agents

In Kubernetes, Guardium supports deploying multiple A-TAP agents to monitor different application pods.

## pod autoscaling

Monitor Horizontal Pod Autoscaler status when configuring K-TAP agents in Kubernetes environments.

## Policy syntax

In Guardium policy definitions, the number sign (#) marks the beginning of a clause or condition.

## Performance tuning

Review CPU usage along with disk I/O performance for optimization in high-volume database monitoring.

## Custom reports

Use the `#include` directive in custom reports to incorporate predefined report templates.

## Oracle reports

Guardium provides Oracle-specific reports that utilize Oracle auditing for relevant security analysis.

## Ingest examples

Guardium's Ingest configuration examples are marked with `#Example` comments for proper formatting guidance.

## Connectivity issues

Verify hostnames in the Guardium central manager match actual server names when troubleshooting.

## Kubernetes monitoring

Use `kubectl get pods` to list all pods for comprehensive Guardium agent deployment.

## HPA metrics

Refer to Guardium documentation for interpreting HPA metrics and ensuring proper K-TAP agent scaling.

## Classification rules

The number sign (#) in classification rules introduces optional conditions that allow continued evaluation.

## Performance scheduling

Schedule resource-intensive Guardium tasks during low CPU usage periods to minimize impact.

## GIM client

Guardium GIM client examples use `#Example` comments to demonstrate proper parameter value syntax.

## Data export metadata

Exported Guardium data includes the exporting agent's hostname in the metadata for tracking.

## Kubernetes deployment

Guardium agents can be deployed as DaemonSets in Kubernetes to ensure agent presence on each node.

## HPA status Overview

Guardium's implementation of Horizontal Pod Autoscaling (HPA) for K-TAP agents enhances their operational efficiency. Custom metrics, in addition to standard CPU and memory metrics, are utilized to accurately reflect the workload of K-TAP agents. This ensures optimal scaling based on database-specific indicators, improving the overall monitoring capability of the platform.

## Number Sign Feature

In Guardium's workflow definitions, the `#` symbol denotes a commented-out step within the workflow. This feature serves as a temporary disabling mechanism for specific steps, allowing administrators to exclude them from execution during testing or maintenance. The commented steps are not removed from the definition but remain available for reactivation, providing flexibility in managing workflow processes.

## Oracle Example for Classification

Guardium's classification system for Oracle databases includes the capability to examine application contexts set during database sessions. This classification aids in identifying sensitive operations by analyzing how data is accessed based on the application context. It provides insights into data usage within Oracle applications, enhancing the ability to monitor and protect sensitive information effectively.

## Advanced Audit Logging Options

The advanced options section for Guardium's audit logging includes commented examples (`#Example`) that demonstrate how to configure settings like log compression and encryption. These examples provide guidance on enhancing data protection for audit logs by implementing secure storage practices. Developers and administrators can use these examples as a reference to configure audit logging according to their security requirements.

## Oracle Monitoring Example

The Oracle example section offers a step-by-step guide for setting up monitoring of Oracle databases using Guardium. It covers prerequisites, required privileges, and necessary configuration settings. This example serves as a valuable resource for administrators who are implementing Guardium in Oracle environments, ensuring they can effectively monitor and protect their Oracle database activities.

## Policy Rule Definition

When defining policy rules in Guardium, the `#` symbol is used to start a new rule clause. Each clause specifies a condition that, when met, triggers the corresponding actions outlined in the rule. Multiple clauses can be combined to create complex rule definitions. This structure allows administrators to set up detailed and precise policies to enforce security and compliance within the Guardium environment.

oncepts:** CAS Template, Continuous Audit, Audit Type, Flexibility, Automation

---

## REST API: create_assessment Command

Use `POST /restAPI/create_assessment` to initiate a new security assessment in Guardium. The request body must include JSON fields `description` (assessment name), `definition` (policy or test definitions), and optional `type` (e.g., compliance, vulnerability). The API responds with the assessment's ID, confirming creation. This CLI-equivalent endpoint aids automation by allowing scripted or programmatic assessment provisioning, essential for CI/CD pipelines or large-scale deployments.

**Key Concepts:** Security Assessment, API Creation, JSON Payload, Automation

---

## Disable Threat Finder (CLI)

The CLI command `disable_threat_finder` immediately stops threat detection on a specified Guardium managed unit. It requires no options but may be followed by `-G <group_name>` to apply to a managed unit group. This command supports rapid response to maintenance needs or testing scenarios where threat analytics could impact system performance. Re-enable with `enable_threat_finder`.

**Key Concepts:** Threat Finder, Managed Unit, CLI, Maintenance Mode

## IBM Guardium Data Protection Overview
IBM Guardium Data Protection is a comprehensive enterprise solution for database activity monitoring, data security, and compliance reporting across structured and unstructured data sources, both on-premises and in the cloud.

### Features
- **Database Activity Monitoring:** Real-time tracking of database transactions and user actions
- **Policy Enforcement:** Prevention of unauthorized access and data exfiltration through granular security policies
- **Vulnerability Assessment:** Periodic scans for database vulnerabilities and configuration weaknesses
- **Compliance Reporting:** Built-in templates for PCI-DSS, GDPR, HIPAA, SOX, and other regulatory standards
- **Identity and Access Management:** Integration with LDAP, Active Directory, and other identity providers

### Workflows
- **Deployment:** Install S-TAP agents, configure collectors and aggregators, connect to Central Manager
- **Policy Management:** Create and apply security policies to monitor and block risky activities
- **Monitoring:** Continuous monitoring of database activity, generating alerts and reports
- **Incident Response:** Automate response actions such as alerting, blocking, credential rotation

### Personas
- **Security Admin:** Define policies, review alerts, manage compliance reports
- **Database Admin:** Install S-TAP agents, manage datasource configurations
- **Compliance Officer:** Monitor compliance status, generate audit evidence
- **Data Analyst:** Access activity reports while respecting data access controls

---

## Guardium API: get_debug_level

The `get_debug_level` Guardium API command retrieves the current debugging level configuration for the Guardium system.

**Parameters:**
- `api_target_host` (required): Specifies where the command should execute. Supported values include:
  - `all_managed`: Execute on all managed units except the central manager
  - `group:<group name>`: Execute on all managed units in the specified group

**Concepts:**
- `Debug Level`: Current debugging level configuration
- `Guardium`: IBM's data security platform
- `api_target_host`: Parameter to specify execution target for API commands

uring the Guardium web server to require client certificate authentication. The steps ensure secure, authenticated access to the Guardium web interface.

Key Concepts: Client Certificate, Certificate Trust Store, SSL Configuration, Guardium Web Server

---

## Configure for client web certificates

**Prerequisites**
- Valid CA-signed client certificates
- Administrative access to Guardium appliance

**Process**
1. Import the CA certificate into Guardium's trust store to establish trust.
2. Upload each client certificate to the Guardium system.
3. Configure the Guardium web server to require client certificate authentication.
4. Restart Guardium services to apply changes.

**Verification**
- Access Guardium web interface using a configured client certificate.
- Verify successful authentication and access.

**Key Concepts:** CA Certificate, Client Certificate, Trust Store, SSL Authentication

## Certificate-Based Authentication for Web Interface

### Enabling Certificate Authentication

1. **Import Certificates**
   Upload PEM-formatted certificates and private keys to the Guardium appliance.
   Ensure certificates are signed by a trusted CA and private keys are encrypted.

2. **Configure Trust Store**
   Add the CA certificate that signed your server certificates to the appliance's
   trust store. This allows Guardium to validate client certificates presented during
   TLS handshakes.

3. **Activate Authentication**
   In the Guardium web interface, navigate to *Admin > Managed Systems > Authentication*.
   Select *Certificate* as the authentication method for web clients. Apply changes.

4. **Restrict Access**
   Optionally configure allowed certificates by adding them under *Admin > Managed Systems > Authorized Certificates*.

### Key Concepts

- **Certificate Import**: Process of adding PEM-encoded X.509 certificates and RSA private keys to the Guardium trust chain.
- **Trust Store Management**: Configuring which CA certificates Guardium trusts to validate client certificates.
- **Web Interface Security**: Hardening measures for Guardium's web management console.
- **Certificate-Based Authentication**: Verifying client identities via TLS client certificate exchange rather than passwords.

## Manage Custom Datasource Properties

The `grdapi` command allows creation, listing, and querying of custom properties for datasources in Guardium. It supports derived properties that join tables to enrich metadata. Available from v11.0.

Key Concepts: DataSource Management, Custom Attributes, Metadata Enrichment

## Oracle SQL Commands Report

Generates reports on SQL operations, including runtime parameters and key entities like Access SQL and Full SQL. Provides insights into database usage and optimization.

Key Concepts: SQL Activity Analysis, User Behavior, Database Performance

## Create Role API

Creates roles with specific privileges on Guardium systems via CLI or REST API. Applicable to standalone collectors and central managers. Available from v10.1.4.

Key Concepts: Role Management, Privilege Assignment, Security Configuration

## Change Tracker Parameter Settings

Configures Change Tracker settings such as file change tracking, certificate expiration alerts, and process intervals. Available from v12.1.

Key Concepts: Change Management, Security Configuration, Monitoring

## Configure for client web certificates

This procedure outlines steps to configure client web certificates for secure interactions with IBM Guardium Data Protection, as described in the entry `157b359f-807f-43f5-a4c0-68557f7392b4`.

Key Concepts: Client Authentication, Certificate Configuration

## Skips registry certificate installation on cluster nodes

In cluster configurations, registry certificate installation may be skipped on specific nodes, as detailed in `f13f1388-1697-4fad-8dd6-5b4ab7f3ea23`, affecting audit process synchronization.

Key Concepts: Cluster Configuration, Certificate Management

## Number sign

Reiterates the process for registering a unit with the central manager, emphasizing the use of either IPv4 or IPv6 and the independence of hostname from IP mode selection (`d376ef9b-fec8-4c16-aeab-54b859b8a0ee`).

Key Concepts: Unit Registration, IP Mode Selection

## Number sign

Details the REST API endpoint for disabling entitlement optimization in Guardium (`0c924af1-bdd2-48f6-aa3b-eb0449e6b054`).

Key Concepts: API Usage, Entitlement Management

## Number sign

Explains the `datamart_copy_file_bundle` action for adding data marts to bundles (`0fb7049e-84a1-4662-a316-0427f227edf6`).

Key Concepts: Data Mart Management, Bundle Configuration

## Number sign

Details the `execute_incidentGenProcess` REST API syntax for incident generation (`c27e921b-e3e1-48fe-934e-c9d4ffe481e3`).

Key Concepts: API Integration, Incident Handling

## Number sign

Iterative refinement process for refining policies, running procedures, and assessing results to optimize configuration for client web certificates (`32a6851d-fc7a-4c2d-b1b4-6714e857e67e`).

Key Concepts: Policy Optimization, Iterative Configuration

## Number sign

Describes special handling of response length thresholds in extrusion rules within Guardium, including calculation methods and the exclusive "Revoke" function (`70819170-e68b-44c0-8005-c9ad8f5574e2`).

Key Concepts: Extrusion Rules, Response Handling

## Number sign

Addresses detection of credential stuffing attacks using policies and the importance of robust policy management (`6cfd90aa-04bf-4bcf-9e2d-a533fd4a5ac2`).

Key Concepts: Credential Stuffing, Policy Management

## Number sign

Provides an Oracle configuration example related to database procedures (`aa69895f-81b6-466d-aa7e-aa4e97ed3ca5`).

Key Concepts: Oracle Database Configuration

## Document Overview

IBM Guardium Data Protection secures databases with monitoring, policy enforcement, compliance reporting, and UEBA.

### Features

- Real-time activity monitoring
- Policy-based alerts and automatic blocking
- Anomaly detection and risk scoring
- Audit reports for major compliance standards
- Transparent encryption, tokenization, and dynamic masking

### Personas

- Security Administrator: configures policies and responds to incidents
- Database Administrator: installs S‑TAP agents and helps with compliance
- Compliance Officer: generates audit reports
- Data Analyst: uses activity data for operational insights

---

## KILL Commands Execution Activity Stream

Logs `KILL` statements from client apps, capturing client IP, server IP, service name, and issuing user. Provides audit trails for session terminations, supporting security policies around critical session management.

---

## Oracle Timestamp Aggregation Across Time Zones

Converting timestamps to a common zone (e.g., UTC) before aggregation prevents incorrect totals and skewed analytics caused by duplicate local times in different offsets.

---

## Enterprise Load Balancing Configuration

Integrates Guardium collectors with enterprise load balancers:

1. Associate load‑balancer entities to Guardium managed units.  
2. Point S‑TAP instances to the correct collector based on routing.  
3. Verify mappings and test failover in the Guardium UI.

---

## Guardium S‑TAP Character Redaction

S‑TAP uses regex patterns to redact sensitive data characters on‑the‑fly. Regex rules match and replace characters in captured data streams. Not available for certain null‑terminated Windows data types.

**Example:** `.{10}` – redacts any 10‑character sequence.

---

## db2_exit_health_check Script Usage

```bash
/usr/local/guardium/guard_stap/guardctl db_instance=db2inst1 deactivate
```

Validates Guardium‑DB2 exit integration, checks IE parameters, and reports issues without changing configurations.

*Personas:* DB2 Administrators, Security Administrators

---

## Configuring IBM Guardium S‑TAP Debug Logging

`WINSTAP_DEBUG_FILE_NAME` determines S‑TAP debug log location. Default:

```
%ProgramData%\IBM\guardium\debug\guardium_<YYYYMMDD>.log
```

Change the path or filename to troubleshoot S‑TAP issues on Windows.

---

## Controlling DB2 Exit Audit Logging

Enabling audit logging creates detailed exit logs for compliance. Disabling reduces storage use but limits traceability.

configurable rules  
- **Audit Logging:** Centralized log collection, retention policies, and integration with SIEM systems  
- **Compliance & Reporting:** Built‑in PCI‑DSS, GDPR, HIPAA, and SOX report templates; customizable audit trails

## **IBM Guardium Data Protection Overview**

### **Features**
- **Data Discovery & Classification:** Detect sensitive data and apply tags.  
- **Policy Management:** Configure policies for access control, data masking, and SQL protection.  
- **Activity Monitoring:** Capture and analyze database and file activities (SQL statements, file operations).  
- **Threat Detection:** Identify anomalies and violations using machine learning and rule‑based analysis.  
- **Compliance Reporting:** Provide pre‑built reports for PCI‑DSS, GDPR, HIPAA, SOX, etc.  

### **Workflows**
- **Data Source Discovery:** Catalog all enterprise data sources.  
- **Policy Deployment:** Distribute and enforce Guardium policies.  
- **Alert Investigation:** Examine alerts via audit trails and session replay.  
- **Reporting & Dashboards:** Visualize security metrics and compliance status.  

### **Personas**
- **Security Administrator:** Configures policies and incident response.  
- **Compliance Officer:** Reviews compliance reports and regulatory adherence.  
- **Database Administrator:** Manages data sources and Guardium agent installation.  

### **Key Entities**
- **Guardium Aggregators:** Normalize data from collectors.  
- **Guardium Collectors:** Host S‑TAP agents to capture database activities.  

*(Document emphasizes Guardium’s capabilities for real‑time monitoring, enforcement, threat detection, and regulatory compliance.)*

## IBM Guardium Data Protection Overview
IBM Guardium is an enterprise platform for monitoring database activity, enforcing security policies, assessing vulnerabilities, and generating compliance reports across on-premises and cloud data stores.

### Key Features
- Real-time policy enforcement
- S-GATE traffic blocking
- Automated incident generation
- PCI-DSS, GDPR, HIPAA compliance reporting
- CyberArk credential integration

### Workflows
- Centralized policy distribution
- Automated agent lifecycle management
- Vulnerability assessment execution
- Incident response coordination

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is IBM's enterprise-class solution for database activity monitoring, security, and compliance across structured and unstructured data stores, both on-premises and in cloud environments.

## Key Features

### Entities and Access Control
- Database Objects
- Privileged Commands
- Groups
- Classification
- Access Rules

### Monitoring & Alerting
- API Keys
- Access Tokens
- API Calls
- Central Manager
- Managed Units

### Infrastructure Components
- S-TAP
- K-TAP
- Aggregator
- Collector
- Shared Secret
- Logger Queue

### Compliance and Reporting
- Audit Rules
- Scheduler
- Reporter
- Regulatory Standards: PCI-DSS, GDPR, HIPAA, SOX

## Core Workflows

### Data Object Protection
1. Create database objects (tables, views)
2. Apply Access Rules to control who can access what
3. Monitor data access and change activity in real-time
4. Generate audit reports and alerts for policy violations

### Token Management
1. Obtain Access Tokens via REST API for authentication 
2. Include token in Authorization header of API requests
3. Verify tokens are valid and have not expired

## Guardium API Operations

Perform desired operations securely using the authenticated session.

### Key Concepts
- Access Token
- REST API
- Authorization Header
- Central Manager
- Standalone Appliance
- Managed Unit

## Unauthorized Access Detection

Guardium detects and blocks API calls lacking valid access tokens. Requests missing a valid token in the Authorization header receive an authentication failure error, preventing unauthorized access.

### Key Concepts
- Access Token Validation
- API Authentication
- Unauthorized Access Prevention
- Error Response

## Database Connection Architecture

Guardium supports JDBC drivers for SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to ports dynamically.

### Key Concepts
- JDBC
- Native Driver
- Browser Service
- Dynamic Port Detection

## Activity Monitoring & Policy Enforcement

Guardium captures database traffic via S-TAP agents and evaluates it against security policies in real time. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target users, objects, operations, and time windows.

### Key Concepts
- S-TAP
- S-GATE
- Security Policy
- Real-Time Monitoring
- Audit Trail

## API Authentication Configuration

Kerberos authentication for database connections requires specifying a username/password or a Kerberos keytab file. Upload the Kerberos configuration file to Guardium to enable secure authentication.

### Key Concepts
- Kerberos
- Authentication
- Keytab
- Secure Connections

## High Availability and Traffic Management

A system component monitors load on managed units and network traffic to balance connections for optimal performance and high availability, ensuring efficient resource utilization and continuity.

### Key Concepts
- Load Balancing
- Traffic Management
- Managed Units
- High Availability

## Guardium System Control Configuration

The `WINSTAP_ALL_CAN_CONTROL` parameter specifies which Guardium systems can manage an S-TAP agent. Value 0 restricts control to the primary Guardium system, while 1 allows any system to manage it. Versions 12.2+ add external load balancer support.

### Key Concepts
- S-TAP Management
- Centralized Control
- Guardium System Roles

## Transport Security for S-TAP

The `WINSTAP_USE_TLS` parameter configures encryption for S-TAP-to-Guardium communication. Value 0 disables encryption (not recommended), while 1 enables SSL encryption for secure data transmission.

### Key Concepts
- TLS Encryption
- Data Security
- S-TAP Communication
- Secure Transmission

## Guardium System Port Configuration

The `PRIMARY` parameter determines if an S-TAP agent is the primary (1) or secondary (0) connection point to Guardium. The read-only `TAP_GUARD_TCP_PORT` specifies the port used for S-TAP-to-Guardium communication, typically 9500 or 9800.

### Key Concepts
- Primary/Secondary Agents
- Port Configuration
- Data Transmission
- Security

## Network Traffic Monitoring Configuration

The `PORT_RANGE_START` parameter in `guard_tap.ini` sets the lowest port number for S-TAP to listen for database traffic in network monitoring mode. Valid protocols include typical database ports like 7, 8, and 808, with MSSQLSERVER as the default.

### Key Concepts
- Network Monitoring
- Port Configuration
- Database Traffic
- S-TAP Setup

## K-TAP Management for Database Instances

To deactivate K-TAP monitoring for a specific database instance (e.g., `db2inst1`), run `/usr/local/guardium/guard_stap/guardctl db_instance=db2inst1` on the associated host.

## Get Hadoop Cluster Status

Retrieves monitoring data for Hadoop ecosystem components.

**Required parameters:** `serverHostName`, `serverPort`, `userName`, `password`, optional `clusterName`.

**Result:** Status of services such as HBASE, HIVE, etc.

---

## API Target Host Parameter

Accepts a host name or IP address.  
- On a managed unit, the command runs on the central manager.  
- Example IP: `10.0.1.123`.  
IP must match the network's IP mode.

---

## Host Name for Central Management

A hostname for registration with the central manager can be IPv4 or IPv6, regardless of IP mode settings, enabling flexible connectivity.

## Manage Threat Analytics in Guardium

**The Active Threat Analytics** feature in IBM Guardium allows administrators to manage threat detection processes. It provides tools to enable, disable, and filter threat analytics items, ensuring effective threat detection and response. Proper configuration is crucial for maintaining a strong security posture and protecting sensitive data.

---

## IBM Guardium Data Protection Overview

**IBM Guardium** is a comprehensive database security platform that monitors activity in relational and non-relational data sources. It ensures ongoing compliance by enforcing security policies, detecting vulnerabilities, and providing detailed compliance reports.

### Core Features
- **Database Monitoring:** Continuous surveillance of authorized and unauthorized database access using database-agnostic agents.
- **Policy Enforcement:** Real-time blocking of unauthorized activities with Guardium's S-GATE functionality.
- **Vulnerability Assessment:** Automated scans to identify security configuration gaps and policy violations.
- **Compliance Reporting:** Ready-made templates for PCI-DSS, GDPR, HIPAA, SOX, and other regulatory frameworks.
- **Threat Analytics:** Advanced detection and response capabilities to identify and mitigate threats in real-time.
- **Cloud Compatibility:** Support for major cloud database services including AWS RDS, Azure SQL, and Google Cloud SQL.

### Workflow Steps
- **Policy Setup:** Define access controls, audit policies, and compliance requirements tailored to organizational needs.
- **Incident Response:** Analyze alerts, audit trails, and system behavior to respond to security incidents.
- **Vulnerability Management:** Schedule routine vulnerability scans, remediate findings, and confirm compliance status.
- **Performance Tuning:** Monitor system performance, troubleshoot issues, and optimize configurations for efficiency.

### User Roles
- **Security Administrators:** Implement policies, manage data sources, and investigate security incidents.
- **Compliance Officers:** Generate compliance reports, verify controls, and align processes with regulatory standards.
- **Data Analysts:** Review audit logs, create performance dashboards, and conduct investigative queries.
- **IT Administrators:** Oversee Guardium deployments, configure infrastructure, and ensure system stability.

### Key Components
- **Managed Units:** Groups of Guardium systems for centralized management and control.
- **Collectors and Agents:** Components that capture database transactions and relay them to collectors.
- **Aggregators:** Collect normalized audit data from multiple sources for unified analysis.
- **Central Managers:** Serve as unified control points for comprehensive reporting across all Guardium deployments.

---

## Guardium Data Protection Overview

IBM Guardium provides enterprise database activity monitoring, security policy enforcement, vulnerability assessment, and compliance reporting across data stores.

### Key Features
- Real-time monitoring of database activity
- Policy enforcement with S-TAP agents
- Compliance templates for PCI-DSS, GDPR, HIPAA, and SOX
- Incident response capabilities
- Support for on-premises and cloud data stores

### Core Workflows
- **Configuration:** Add datasources, deploy S-TAP agents, define policies
- **Monitoring:** Review activity reports, run assessments, use audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents
- **Upgrade:** Coordinate updates through Central Manager

### Personas and Roles
- **Administrators:** Platform management and operations
- **Security Administrators:** Configure fine-grained access control and blocking
- **Database Administrators:** Manage S-TAP deployment and parameters
- **Compliance Officers:** Generate and distribute regulatory reports
- **Security Analysts:** Investigate threats and handle policy exceptions

### Technical Components
- **Agents:** Kernel-TAP (K-TAP), User-TAP (U-TAP), Activation-TAP (A-TAP)
- **Managed Units:** Collectors, Aggregators, Central Manager
- **Policies:** Security, Audit, Classification
- **Credentials:** Integration with CyberArk vault

---

## Verify API Key Existence

For firewall configuration in Guardium, `firewall_force_unwatch` defines network/mask of IPs exempt from firewall blocking when `firewall_default_state` is enabled. This ensures specific traffic remains unaffected by default firewall settings.

**Key Concepts:** firewall_default_state, firewall_force_unwatch, network, mask

---

## Verify API Key Existence

The `DB_IGNORE_RESPONSE` parameter configures which database response packets Guardium should ignore. Setting it to `ALL` or specific database types (e.g., MSSQL, DB2) optimizes traffic monitoring by filtering unnecessary responses.

**Key Concepts:** DB_IGNORE_RESPONSE, response packets, database types, filtering

```markdown
## IBM Guardium Data Protection Overview

### Database Connection Architecture
- Supports JDBC drivers: native for performance, generic for compatibility
- Browser service resolves instance names to dynamic ports

### Activity Monitoring & Policy Enforcement
- Captures database traffic via S-TAP
- Real-time policy evaluation and enforcement
- Triggers alerts, reports, or blocking

### Internal Rule Processing
- Rules engine evaluates transactions
- Supports complex logic with AND/OR, wildcards, regex

### Logging & Auditing
- Extensive security and system logging
- Centralized forwarding to SIEM systems

### Configuration Management
- Central Manager interface for multi-appliance management
- Version control, change auditing, templated deployments
```

## Guardium: Comprehensive Data Protection Platform

IBM Guardium Data Protection offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores in on-premises and cloud environments.

### Core Features
- Dynamic datasource connectivity, multi-driver support, and CyberArk integration
- Real-time policy enforcement, S-GATE blocking, and security incident generation
- PCI-DSS, GDPR, HIPAA, SOX report templates, and automated audit trails
- REST APIs, SDKs, SAML SSO, and FIPS 140-2 compliance

### Operational Workflows
- **Configuration:** Deploy S-TAP agents, configure FGAC policies, and manage policies via export/import
- **Navigation:** Review activity reports, run vulnerability assessments, and perform investigative drill-downs
- **Action:** Block queries, rotate credentials, investigate incidents, and revoke privileges

### User Personas
- Administrators manage platform configuration and user access
- Security Administrators define FGAC policies and handle incident responses
- Auditors generate compliance reports
- Database Administrators manage datasources and S-TAP deployments
- Data Owners configure data classifications and masking policies
- Developers perform code analysis and manage test data

### Technical Entities
- Agents and collectors: S-TAP, A-TAP, K-TAP, Log File Agent, Collector, Aggregator, Central Manager
- Policies and rules: Security Policy, Audit Policy, Classification Rule, Access Rule, FGAC Rule, S-GATE Rule
- Infrastructure components: GIM, Managed Unit, S-GATE Device, Universal Connector, On-Prem/Cloud Datastores

## Guardium Data Protection Overview

IBM Guardium Data Protection secures enterprise databases with real-time monitoring, compliance reporting, vulnerability assessment, and incident management.

### Features
- Real-time monitoring of data access and transactions
- Automated vulnerability scans prioritizing weaknesses
- Compliance reports for PCI-DSS, GDPR, HIPAA, and SOX
- Automated alerts and response workflows for security incidents

### Workflows
- Configuration and deployment of datasources and agents
- Monitoring activity and generating compliance reports
- Setting up threat detection policies and response mechanisms

### Entities
- Guardium Servers: Central Manager, Managed Units, Collectors, Aggregators
- Data Sources: Monitored databases, file systems, applications
- Users and Groups: Roles, distribution lists for reports and notifications
- Reports and Dashboards: Configurable templates and real-time data visualizations

# Compressed Guardium Technical Reference

## Personas Overview
- Security Administrators manage policies, monitor threats, conduct investigations.
- Compliance Officers generate and review compliance reports, ensure regulatory adherence.
- Database Administrators configure datasources, maintain agent health, optimize performance.
- IT Auditors conduct audits, verify configurations, assess security controls.

## Entities Overview
- Data Sources: Databases, data warehouses, files, and applications protected by Guardium.
- Agents & Collectors: S-TAP, A-TAP, and other components responsible for data collection and monitoring.
- Policies & Rules: Security policies, audit policies, classification rules, and access rules governing data access and usage.
- Infrastructure Components: Central Manager, aggregators, S-GATE, and managed units forming the Guardium architecture.

## Registry Certificate Installation on Cluster Nodes
Each node in a Guardium cluster requires a unique X.509 certificate signed by the cluster's Certificate Authority. The process:
1. Generate a private key and CSR on the node. 
2. Submit the CSR to the Guardium CA for signing.
3. Distribute the signed certificate to the node.
4. Install it in the Java KeyStore of Guardium components (Collector, Aggregator, Central Manager).
5. Restart Guardium services for the new certificate to take effect.
Proper installation ensures authenticated and encrypted inter-node communication for multi-node deployments.

## Managing Bundle Versions in GIM
Global Installation Manager (GIM) displays only the latest bundle versions by default, but administrators can view all versions to select a specific one suited to a target platform or client:
1. Open the GIM console.
2. Navigate to **Manage → Bundles**.
3. Check "Show All Versions" to list historic releases alongside current ones.
4. Select the desired version for installation on managed units.
5. Apply the changes to make the bundle available for deployment.

ique wildcard (`*.example.com`) to ensure proper routing and security. The entry details steps to generate certificate signing requests, import signed certificates, and specify those in ingress annotations for cloud deployments.

## Optional, annotations to specify for ingress

The *2283c7a7-f4be-4419-992a-04c47e894b8f* entity specifies that TLS certificates for inbound traffic (ingress) to Guardium must include a unique common name. This identifier allows external systems to validate the Guardium instance and establish secure connections.

## Date Time Type Exe Term Host AUID Event

The *3ab6dbce-2b2c-4459-9e90-a8eba19ec618* features entity describes methods for resolving VMware kernel panics. It outlines software updates or configuration changes required to address stability issues, emphasizing Guardium's capabilities for diagnosing and fixing system problems in managed environments.

## Date Time Type Exe Term Host AUID Event

The *0e75d0c5-a4ac-4eb2-a975-a9dc6db46af9* entities category lists relevant terms for understanding disk space management on Guardium aggregators and collectors. Key terms include "disk space reservation," "CLI command," "default percentages," and "warning message," essential for administrators managing storage and system performance.

## Date Time Type Exe Term Host AUID Event

The *3ab6dbce-2b2c-4459-9e90-a8eba19ec618* knowledge entry provides instructions for troubleshooting a VMware kernel panic issue. It outlines steps such as applying specific software updates to the ESX system or adjusting configuration settings to resolve the stability problem, highlighting Guardium's role in system management and kernel health monitoring.

## Document Overview

IBM Guardium for OcrNet is a security solution designed to detect and prevent threats in database environments. It intercepts and inspects all SQL traffic in real-time, providing comprehensive visibility into database activities.

### Capture Process
SQL traffic data captured by S-TAP agents on database servers is sent to the Guardium collector for analysis. The Guardium aggregator further processes and stores data for reporting and analysis.

### Analysis Module
The Guardium threat intelligence engine analyzes captured traffic against predefined and customizable policies to detect anomalies and potential threats.

### Reporting and Alerts
Guardium provides real-time alerts and reports on suspicious activities, including unauthorized access attempts, policy violations, and data exfiltration attempts.

### Compliance and Auditing
Guardium helps organizations meet compliance requirements by generating detailed audit trails and reports on database activities, ensuring transparency and accountability.

## Oracle Data Type Support for Discovery & Classification
IBM Guardium for Oracle supports numeric, character, date, and timestamp data types for data discovery and classification. It provides regex patterns and type-based criteria, automatically identifying regulated data like SSNs and credit card numbers.

## Error Criteria Evaluation in Session Policies for Oracle
Session-level policies in Guardium for Oracle trigger on most SQL errors, except LOGIN_FAILED. This behavior is equivalent to the Exception type criteria (SQL_ERROR) in Data Security Policies.

## Default Behavior of SQL Logging in Oracle Guardium
By default, Guardium for Oracle does not log insert values in SQL statements to protect sensitive data. This behavior can be overridden for specific auditing or debugging needs.

## Special Handling of TRANSFORM Actions for Oracle
TRANSFORM actions in Guardium for Oracle automatically populate Instance name, Server name, and Service name based on database type. This dynamic modification enhances real-time data protection.

## Oracle Alert Management and Programming Considerations
Guardium for Oracle uses java.util.Date and String for alert management, employing standard Java practices within Oracle workflows to handle audit messages effectively.

## **Compressed Guardium Reference**

### **IBM Guardium Overview**
IBM Guardium is an enterprise database activity monitoring and security platform that monitors, reports on, and protects structured and unstructured data across on‑premises and cloud environments. It enforces policies, detects threats, assesses vulnerabilities, and supports compliance reporting.

### **Key Areas**
- **Data Source Connectivity:** Connects to Oracle, SQL Server, DB2, Sybase, Informix and other databases using native drivers and generic JDBC; auto‑detects dynamic ports.  
- **Threat Detection:** Real‑time policy enforcement, S‑GATE query blocking, incident creation, statistical anomaly detection.  
- **Compliance & Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX; automated audit trails and data classification.  
- **Privileged Session Management:** Session recording, privileged user monitoring, password vault integration.  

### **Core Workflows**
- **Configuration:** Add data sources, deploy S‑TAP agents, define FGAC policies, set classification rules.  
- **Monitoring:** View alerts, anomaly reports, CAS status, archived query results.  
- **Mitigation:** Block queries, rotate credentials, revoke privileges, generate compliance reports.  
- **Maintenance:** Schedule archival tasks, manage system backups, update Guardium components.  

### **Personas**
- **Security Administrator:** Configures policies, oversees threat detection, ensures compliance.  
- **Database Administrator:** Installs S‑TAP agents, defines repositories, tunes performance.  
- **Compliance Officer:** Generates audit reports, validates regulatory adherence.  
- **Data Analyst:** Produces usage reports, visualizes access patterns.  

### **Guardium Entities**
- **Agents & Collectors:** S‑TAP (kernel‑level), A‑TAP (user‑level), K‑TAP (kernel tap), Collector, Aggregator, Central Manager.  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, FGAC.  
- **Infrastructure:** Managed Unit, S‑GATE, Universal Connector, Data Classification Engine.  

---

### **Oracle Integration – Report Merging**
Guardium merges Oracle report data internally for a default **14‑day window** shown at the top of each interactive report. The merged view enables trend analysis across intervals; the window can be customized per report definition. Merging is transparent to users and powers statistical calculations such as averages and standard deviations.

**Key Concepts:** Merged Data, Merge Period, Interactive Reports, Oracle Integration  

---

### **Statistical Metrics for Temporary Object Usage**
Three Guardium metrics evaluate temporary object activity:
- **Temporary Objects Average** – mean count per session.  
- **Temporary Objects Score** – anomaly score versus baseline.  
- **Temporary Objects SD** – standard deviation, showing variability.  

These metrics flag excessive or unusual temporary‑object creation, often a sign of misuse or attack.

**Key Concepts:** Temporary Objects, Anomaly Detection, Statistical Metrics, Database Security  

---

### **Dynamic Query Building for Reporting**
Guardium dynamically selects the appropriate column for reporting queries:
- **Client/Server** option → uses `ATTRIBUTE_ID`.  
- **Client/Server By Session** option → uses `MAIN_ATTRIBUTE_ID`.  

This automatic column choice lets the same query adapt to transaction‑level or session‑level granularity.

**Key Concepts:** Query Customization, Attribute Filtering, Reporting Granularity, FGAC  

---

### **User Hierarchy Management via CLI**
Example CLI command to set up a user hierarchy:
```
grdapi create_user_hierarchy userName=ADAMS parentUserName=SCOTT
```
ADAMS inherits SCOTT’s permissions, simplifying privilege management.

**Key Concepts:** User Hierarchy, Role Inheritance, Access Control, CLI  

---

### **Auditing – Applicable Entities**
The **Timestamp** attribute is the only temporal field for **Data Set** entities. Attributes that **are not** applicable to Data Sets:
- **Records Affected**  
- **Returned Data**  
- **Full SQL**  

For audit context, use session‑level fields such as **Session ID** and **User ID**.

**Key Concepts:** Data Sets Domain, Audit Attributes, Entity Mapping, Auditing Best Practices  

---

### **Archive Task Scheduling**
If an archive task runs later in the day, any skipped executions are automatically processed during the next run. No manual rerun is needed as long as the archive finishes **within the same calendar day**.

**Key Concepts:** Archive Scheduling, Task Continuity, Automated Processing, Backup Workflow  

---

### **System Credential & Archive Configuration**
1. **Choose a storage method** (e.g., S3, FTP, database).  
2. **Enter credentials** (keys, usernames, passwords).  
3. **Specify endpoints** (server addresses, ports).  

These steps ensure secure and reliable backup and archival operations.  

---

## Key Concepts
- Backup Configuration
- Credential Management
- Endpoint Specification
- Version Compatibility

## Smart Card Authentication Login Workflow
Navigate to `https://<central_manager>/gui/`, enter smart card PIN, access Guardium features.

## Enterprise Load Balancing and S-TAP Configuration
Enable load balancer on Central Manager, configure S-TAP to point to load balancer IP/port, set `load_balancer_port`. Distributes traffic across collector units.

## Document Overview
- **Features:** Unified database visibility, policy-based protection, advanced threat detection, compliance reports, endpoint integration, data classification.
- **Workflows:** Deployment, policy management, reporting, investigation.
- **Personas:** Security administrators, database administrators, compliance officers, security analysts.
- **Entities:** Sensors (S-TAP), collectors, aggregators, policy definitions, audit trails, reporting engine.

e level only supports basic regular expressions without advanced features like backreferences or lookaheads. For basic matching, the limited regex syntax is sufficient, but for more complex patterns, external processing may be required.

**Key Concepts:** Redaction, Regular Expressions, Database Security, Pattern Matching

## Group Membership in Guardium Policies

A Guardium policy rule is triggered when any member of a group like DB_TABLES_PROD matches the rule conditions. All members do not need to match.

**Key Concepts:** Group-Based Policies, Rule Triggering, Policy Flexibility

---

## Ad Hoc Policy Analysis

The Guardium policy analyzer lets users run ad hoc assessments of policy activity. To use it:
1. Navigate to the policy analyzer menu
2. Confirm that policy monitoring is active
3. Run the analysis to review changes and security trends

**Key Concepts:** Policy Analysis, Security Trend Monitoring, Ad Hoc Reporting

---

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise platform for database activity monitoring and security. It:
- Monitors structured and unstructured data on-premises and in the cloud
- Enforces policies and blocks threats in real time
- Provides compliance reporting for PCI-DSS, GDPR, HIPAA, SOX
- Supports datasource connectivity, threat detection, and compliance features

**Key Concepts:** Database Activity Monitoring, Data Security, Compliance Reporting

---

## Special Handling for TRANSFORM Actions

TRANSFORM actions transform data into usable formats while maintaining integrity. They require a unique identifier to categorize the transformation and ensure proper data management.

**Key Concepts:** Data Transformation, Data Integrity, Transformation Categories

---

## Special Handling for TRANSFORM Actions

The Guardium DLP feature maps regulatory requirements to Guardium definitions for compliance monitoring. It is disabled by default and helps organizations adhere to data protection regulations.

**Key Concepts:** Data Compliance, Regulatory Requirements, DLP, Data Protection

---

## Special Handling for TRANSFORM Actions

When configuring audit schedules, the Sync QUERY_FROM_DATE option aligns the start date of the next run with the end date of the previous run to avoid data gaps. This requires at least one prior execution of the audit process.

**Key Concepts:** Audit Synchronization, Data Consistency, QUERY_FROM_DATE

---

## Special Handling for TRANSFORM Actions

Guardium lets users create custom tables to integrate enterprise data with internal data. These tables can be queried alongside predefined tables, supporting flexible data analysis.

**Key Concepts:** Custom Tables, Data Integration, Query Flexibility

---

## Special Handling for TRANSFORM Actions

The provided table lists supported and unsupported data types for custom tables, focusing on Oracle databases. Types like RAW, LONG RAW, and XMLTYPE are unsupported in Oracle custom tables.

**Key Concepts:** Oracle Data Types, Custom Tables, Database Compatibility

---

## Oracle Example

Periodic entitlement reviews validate user privileges against database resources, enforcing least privilege access. Database administrators manage these privileges to maintain security and functionality.

**Key Concepts:** Entitlement Reviews, Least Privilege Access, Database Privileges

---

## Oracle Example

Shared database user accounts hinder individual activity tracking. Guardium features enable effective user monitoring even in shared account environments, supporting robust user activity tracking.

**Key Concepts:** Shared User Accounts, User Activity Tracking, Database Monitoring

ises and in the cloud.

### Features Overview

- **Dynamic Port Detection:** Automatic discovery of database ports using browser services
- **Multi-Driver Support:** Native JDBC, ODBC, CLI drivers plus generic for broad coverage
- **CyberArk Integration:** Secure credential retrieval for S-TAP configuration
- **Real-Time Policy Enforcement:** S-GATE blocking of unauthorized queries
- **Compliance Reporting:** PCI-DSS, GDPR, HIPAA, SOX templates with automated audit trails

### Workflows Overview

- **Datasource Onboarding:** Add system, deploy S-TAP via GIM, configure connectivity
- **Policy Creation:** Define FGAC/Audit rules, classification, access controls
- **Monitoring:** Review activity reports, run vulnerability assessments, analyze alerts
- **Incident Response:** Block sessions, rotate credentials, investigate anomalies

### Personas Overview

- **Security Administrator:** Manages FGAC policies, security rules, compliance settings
- **Database Administrator:** Configures datasources, S-TAP installation, performance tuning
- **Compliance Officer:** Generates regulatory reports, reviews audit evidence
- **Analyst:** Performs threat investigations, uses dashboards and ad-hoc analysis

### Entities Overview

- **Agents:** S-TAP (On-prem), A-TAP (Audit), K-TAP (VIA)
- **Collectors:** Central data aggregation and storage
- **Policies:** Security, Audit, Classification, Access control rules
- **Infrastructure:** Managed Units, S-GATE, Universal Connector

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

Key Concepts: JDBC, Native Driver, Browser Service, Dynamic Port Detection

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

Key Concepts: S-TAP, S-GATE, Security Policy, Real-Time Monitoring, Audit Trail

## Oracle Specific Entity: Analytic Case

The "Analytic Case" entity in Guardium represents a single analytic investigation. It includes:
- **Case ID:** Unique identifier for the case
- **Anomaly Score:** Statistical rating of the anomaly severity
- **Database Name:** Target DB involved in the case
- **Timestamp:** When the case was created

## SQL Audit Key Concepts

- **SQL Verb:** Captured operation type (e.g., SELECT, INSERT, UPDATE, DELETE)
- **Error Codes:** Standard SQL states (e.g., -557 for invalid grant/revoke)
- **Transactional Status:** Rolled back vs. committed changes
- **Cascading Effects:** Related objects affected by DDL statements

## GuardAPI: User Hierarchies

The `create_user_hierarchy` GuardAPI command establishes reporting relationships between users. Example: `grdapi create_user_hierarchy userName=ADAMS parentUserName=SCOTT` defines ADAMS as reporting to SCOTT. This enables hierarchical access to user activity data.

## Keywords - SQL Error Heartbeat

SQL error codes and their meanings:
- **-557:** Inconsistent grant/revoke keywords
- **-559:** Disabled authorization functions
- **Heartbeat:** Periodic background process status indicator

## Sentry Services Requirements

For Hadoop data protection:
1. Install Sentry Services on Hadoop clusters
2. Configure Sentry with appropriate roles/privileges
3. Enable Sentry auditing for Guardium capture
4. Add Sentry-supported systems as Guardium datasources

## 549. Skips registry certificate installation on cluster nodes

This passage outlines the Guardium support for various Hive configurations, including Hive 1 and Hive 2, with and without Sentry. It describes the need for specific taggers and credentials when Sentry is not enabled, noting that Data Lake uses the All-Schema tagger by default. The passage also mentions the deprecation of older Guardium Hive versions. It guides users for performance testing and provides instructions for optional tagger configurations.

Key Concepts: Hive, Sentry, Tagger, Data Lake, Tag Data, Hive Configuration

urity scans, manage policies.
- **Incident Response:** Alert investigation, session replay, activity drill-down.
- **Maintenance:** Installation updates, patching, performance tuning.

### Personas Overview
- **Guardium Admin:** Platform configuration, user provisioning, cluster setup.
- **Security Analyst:** Policy authoring, incident investigation, UEBA tuning.
- **DB Admin:** Data source registration, S-TAP diagnostics, performance tuning.

### Entities Overview
- **S-TAP:** Kernel-mode sensor collecting SQL traffic.
- **Collector Aggregator:** Event aggregation, pre-filtering, forwarding to Central Manager.
- **Policies:** FGAC, UEBA, Classification, Discovery, Masking, S-GATE.
- **GIM:** Grid Installation & Management tool for deploying agents.
- **UEBA:** User and Entity Behavior Analytics for anomaly detection.
- **S-GATE:** Real-time blocking of risky SQL statements.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection provides comprehensive database security, real-time monitoring, policy enforcement, vulnerability assessments, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- Dynamic port detection and multi-driver support for datasource connectivity
- Real-time threat detection with S-GATE blocking and security incident generation
- Compliance reporting for PCI-DSS, GDPR, HIPAA, SOX, and automated audit trails

### Standard Workflows
- Add datasources and deploy S-TAP agents via Guardium Installation Manager (GIM)
- Configure Fine-Grained Access Control (FGAC) policies

nst configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

Key Concepts: S-TAP, S-GATE, Security Policy, Real-Time Monitoring, Audit Trail

---

## Environment Variable Configuration in Kubernetes

To use a truststore bundle for PostgreSQL in a Kubernetes environment, set the `TRUSTSTORE_PATH` environment variable in the deployment spec to point to the location of the bundle. Ensure the path is accessible by the PostgreSQL container process.

---

## External S-TAP Group Management

The External S-TAP group feature allows grouping and managing multiple External S-TAPs for efficient administration. View and edit group properties through the provided interface, using the ability to centrally manage several S-TAP instances.

---

## Ingress Annotations for Network Configuration

Use the `network.cloud-sql-proxy.executor.enabled` annotation to specify default router and DNS server IP addresses for appliance ingress. Configure these values via CLI commands, ensuring the first resolver is required while others are optional for the desired network setup.

---

## Guardium VM Installation (RIP)

Navigate to the VirtualCenter Server inventory to install the Guardium VM. This step follows logging in and displaying the inventory of managed hosts or clusters, indicating the next substantial action after initial setup steps.

---

## Solr Search Time Control

Configure the `time_allowed` parameter for Solr search operations to limit execution time. Set an integer value within the allowed range, with Deep Search using ten times this specified value to control the depth and duration of search operations.

---

## API Call Pagination with `indexFrom`

Utilize the `indexFrom` parameter when fetching data to specify the starting index for the first record. For sequential retrieval of subsequent data, increment the offset parameter to paginate through results effectively in API calls.

---

## Target Host Specification in APIs

The `api_target_host` parameter in IBM Guardium APIs specifies where the API executes. Choices include all managed units, the central manager, a specific group, or an individual host, allowing control over execution scope within the Guardium environment.

## Guardium Security Policies

Providers protect data by enforcing rules that trigger alerts, reports, or blocking. Policies apply to users, objects, operations, and time windows.

## Configuring Client Web Certificates

To enable mutual SSL authentication for Guardium UI access, install client certificates and their CA certificates in the appliance's certificate store. Only clients with valid certificates gain access.

## Configuring Client Web Certificates Workflow

1. Create a CSR, obtain a signed certificate from a CA, and import it with the CA certificate into Guardium
2. Enable mutual SSL in Administration > Settings > SSL Settings
3. Configure client machines to present the certificate during HTTPS connections
4. Test the setup with and without a valid certificate

## Configuring Client Web Certificates Entities

- Client Certificate: X.509 certificate for authentication
- Certificate Authority: Trusted CA that signs client certificates
- Trust Store: Repository within Guardium that holds CA certificates
- SSL/TLS Protocol: Enables encrypted communication with client certificates

## Oracle Database Monitoring

- Define monitored procedures and parameter values in Guardium policies
- Create data classifications for sensitive data patterns
- Set up audit trails for procedure executions and parameter values
- Configure anomaly detection for unusual execution patterns
- Analyze data in Guardium reports to identify unauthorized usage

## Oracle Database Configuration

1. Ensure Oracle instance is accessible via TCP/IP
2. Install and deploy Guardium's S-TAP agent on the server
3. Define auditing requirements for sensitive data and procedures
4. Create policies that capture required database activities
5. Verify Oracle appears in Guardium's inventory and activity is recorded

## Policy Builder TRANSFORM Actions

Special handling applies to TRANSFORM actions in Guardium's Policy Builder:

- Define transformation logic with regular expressions and masking characters
- Ensure transformations occur before data leaves the collector
- Validate session termination before S-TAP upgrades affect TRANSFORM actions
- Test thoroughly in non-production environments
- Document transformation logic and maintain update procedures

## Real-Time S-GATE Configuration

When modifying S-GATE policy rules in real-time:

1. Use Guardium's administrative interface to modify parameters
2. Adjust platform-specific firewall configurations (iptables/nftables for Linux, appropriate tools for Windows)
3. Apply changes immediately
4. Monitor policy logs and system messages
5. Create audit trails documenting all changes

## Data Masking with TRANSFORM Actions

For advanced masking scenarios:

1. Create precise regular expressions for sensitive data elements
2. Apply masking transformations before data leaves the collector
3. Maintain a list of transformation rules and matched patterns
4. Regularly test masked outputs
5. Coordinate with application development teams for functional queries after masking

## Secure Email Alert Configuration

To secure SMTP email alerting in Guardium, perform the following steps:
1. Add trusted email recipients to the Guardium keystore using the `store_ssl_cert` command.
2. Enable S/MIME encryption for alerts via the `modify_guard_param` command.
3. Configure the alerter to use secure mode without authentication or STARTTLS.
These steps ensure that alerts are encrypted from the Guardium appliance to the email server, preventing interception of sensitive notification content. This security measure complements Guardium's real-time monitoring by safeguarding incident communications during policy violation events.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features

- Monitors structured data from relational databases, unstructured data from file systems, and semi-structured data from NoSQL databases
- Collects transaction logs, query activities, user interactions in real-time
- Captures metadata such as user identities, roles, permissions
- Supports JDBC connectivity with native and generic drivers
- Real-time S-TAP monitoring, S-GATE blocking
- GDPR, HIPAA, PCI-DSS compliance templates

### User Personas

- Security Administrator
- Data Engineer
- Compliance Officer

### Core Workflows

- Configuration: Deploy agents, configure policies
- Monitoring: Review activity reports, investigate incidents
- Response: Block queries, manage risk, ensure compliance

### Important Entities

- S-TAP (database monitoring agent)
- S-GATE (inline blocking agent)
- GIM (agent deployment infrastructure)
- Policies: Security, Audit, Classification, Access

Period Start Date‑Time** and **Period End Date‑Time** attributes to delimit reporting windows for audit and analysis. These timestamps are used by Schedule, Review, and Report entities to restrict data retrieval to the specified time frame.

## Date Components Extraction
`Period_End_Date` and `Period_Start_Date` extract date-only components from a datetime value. Similarly, `Period_End_Time` and `Period_Start_Time` provide time-only components. `Period_End_Weekday` and `Period_Start_Weekday` return the weekday of the respective datetime endpoint. These attributes enable filtering, reporting, and calculations on datetime values without modifying the original timestamps.

## License Remaining Indicator
The **Licenses Remaining** field reports the number of additional license seats available on a Guardium appliance. This read‑only metric supports capacity planning by indicating when new entitlement purchases are required to prevent service disruptions.

## Recovery Strategy Overview
When recovering a Guardium system, separate procedures apply depending on deployment type:
- **Standalone Appliance** – Use local backup and restore mechanisms, leveraging the built‑in snapshot feature.
- **Managed Unit Integration** – Synchronize backups across the central manager and managed units, coordinating recovery through GIM for consistency.

Specific steps vary according to whether the appliance operates autonomously or as part of a managed ecosystem.

## Classification Scans

Guardium's classification feature scans databases to identify regulated data using predefined classifications or custom patterns.

## Auditing & Reporting

Guardium generates comprehensive audit trails and customizable reports, visualizing activity trends through dashboards.

## Integration & Extensibility

Guardium integrates with external systems via APIs, feeds, and connectors, extending functionality through custom plugins.

## x_tds_response_packets Command

Displays the maximum number of response packets Guardium captures per query on the TDS protocol analyzer.

## Event Timestamp Management (664)
Guardium's logging framework uses **Timestamp Created** (immutable) and **Event Date** (mutable) to track event timing, enabling precise monitoring while allowing adjustments.

## Oracle CAS Installation (665)
To install CAS on UNIX:
1. Set `JAVA_HOME` with a supported Java version.
2. Verify OS compatibility.
These steps ensure successful CAS deployment for monitoring.

## CAS Script Templates (666)
CAS agents use OS scripts with positional parameters (`%3` DB username, `%4` DB password, `%5` instance name) to dynamically adapt to various database environments.

## License Management (667/668)
Guardium's license management UI displays:
- Current license count
- Actions for baseline editing/deleting/adding
Unregistered baselines stay active until explicitly disabled, ensuring continuous compliance.

## Guardium Overview (Document)
IBM Guardium Data Protection secures enterprise data by:
- Monitoring activity in real time
- Enforcing policies and detecting threats
- Providing compliance reports (PCI-DSS, GDPR, etc.)

### Key Components
- **Connectivity:** Native/JDBC drivers, browser service for dynamic ports
- **Threat Detection:** Real-time S-GATE blocking, anomaly detection
- **Compliance:** Automated audit trails, report templates

### Workflows
- Add data sources, deploy S-TAPs, disable insecure protocols
- Monitor activities, detect anomalies, enforce policies
- Manage patches, upgrades, and API keys securely

### User Personas
- **Administration:** System and security admins configure and manage
- **DB Administrators:** Manage datasources and patches
- **Compliance:** Generate reports, manage licenses

## IBM Guardium Data Protection Overview

IBM Guardium is an enterprise security platform that monitors, enforces policies, assesses vulnerabilities, and reports on compliance for structured and unstructured data across on-premises and cloud environments.

### Key Features
- **Database Activity Monitoring:** Real-time tap on database transactions using S-TAP, A-TAP, and K-TAP agents that forward activity to collectors for analysis.
- **Policy Enforcement:** Centralized creation of FGAC, SQL Guard, and classification policies enforced by the Secure Guard Engine (S-GATE) which can block, alert, or modify transactions.
- **Data Discovery & Classification:** Automated scanning for sensitive data (PII, PCI) using dictionary and pattern matching, with results used in policy building.
- **Vulnerability Assessment:** Predefined scans for configuration weaknesses and missing patches across database systems, generating risk scores and remediation reports.
- **Compliance Reporting:** Pre-built templates for regulations (PCI-DSS, GDPR, HIPAA, SOX) and customizable audit cubes for audit readiness.
- **Unified Policy Management:** Single pane for policy creation, deployment, and management across all monitored data sources.
- **Anomaly Detection:** Machine learning for user behavior analytics and insider threat detection.

### Architecture Components
- **Guardium Units:** Central Manager, Aggregators, Collectors, and Managed Units forming a hierarchical deployment model.
- **Interception Technologies:** S-TAP (kernel tap), A-TAP (application tap), K-TAP (UNIX kernel module) capturing database traffic.
- **Data Flow:** S-TAP agents on database servers forward traffic to Collectors, which aggregate and send it to the Central Manager for policy evaluation and reporting.
- **Policy Distribution:** Master policies managed centrally and distributed to managed units via encrypted SSL channels.

### Monitoring Workflows
1. **Discovery & Assessment:** Automated scans identify data stores and classify sensitive information.
2. **Policy Enforcement:** Real-time evaluation of transactions against security policies with possible blocking via S-GATE.
3. **Incident Response:** Alerts, audit logging, and session management for detected violations.
4. **Compliance Automation:** Generation of audit logs, reports, and remediation tickets.

### Roles & Personas
- **Data Protection Admin:** Manages datasources, policies, and incidents.
- **Security Analyst:** Conducts investigations and threat hunting.
- **Compliance Officer:** Ensures audit readiness and verifies compliance.
- **DBA/Data Admin:** Installs agents and monitors performance impact.

### Integration
- **Security Infrastructure:** LDAP/Active Directory, HSM, Kerberos for secure credential vaulting.
- **Data Sources:** Supports structured databases (Oracle, MSSQL, DB2) and unstructured files/cloud buckets.
- **Third-Party Tools:** Integration with SIEMs, ticketing systems, and other security tools via APIs for broader security orchestration.

### Vulnerability Management
- Proactive identification of database vulnerabilities with automated scanning and remediation tracking.

### Data Protection
- Secure handling of credentials and keys using HSM and LDAP integration.

### Secure Communication
- Encrypted connections between all Guardium components and agents for data in transit protection.

## Contents

### Encrypt Network Traffic for Security  
Encrypt communication between S-TAP and the Guardium collector for all environments except when performance is critical. Use Guardium's Installation Manager (GIM) to configure multiple servers.

### Import Db2 for i Data to Guardium  
Verify the datasource availability, run the import once, then analyze the data with Custom Query-Report Builder.

### Retrieve Certificate Alias  
Use `show certificate external_stap` to retrieve the unknown alias when needed.

### Configure Google BigQuery Ingress  
Specify `db_type=bigquery` and `port=443`. Traﬃc can be intercepted with proxies or connectors.

### Manage GIM Server and Clients  
GIM manages installation, conﬁguration, certiﬁcates, and diagnostics. Understand failover between primary and standby servers using GUI and CLI.

### Upgrade Database Software  
Upgrade operational databases without OS upgrades to maintain S‑TAP monitoring capabilities.

### Manage Deprecated Parameters  
`shared_memory_allocation_threshold` and similar parameters have been deprecated. Use modern dynamic allocation thresholds.

### License and Patch Management  
Install license keys using CLI or GUI. Install maintenance patches regularly to keep the system updated and secure.

Legacy Database Connection
- **Supported Databases:** Oracle, SQL Server, DB2, Sybase, MySQL, PostgreSQL, Teradata, SAP HANA
- **Connection Types:** ODBC, JDBC, Native API
- **Configuration:** Defined in Guardium policy as data source objects
- **Monitoring:** Real-time activity capture via S-TAP or A-TAP agents
- **Management:** Centralized via Guardium UI or CLI

---
### Skip Service Access Setup
No further details provided.

## Database Connection Architecture

IBM Guardium supports JDBC drivers for SQL databases:

* **Native drivers** – Optimized for specific database vendors.
* **Generic drivers** – Broad compatibility across many systems.
* A **Browser Service** resolves logical instance names to current port numbers, removing static connections.

---

## Activity Monitoring & Policy Enforcement

Guardium captures all database traffic via **S‑TAP** agents and evaluates it in real‑time against **security policies** defined by the user. Policy violations generate **alerts**, **audit reports**, or can be blocked by **S‑GATE**. Policies can be scoped by user, object, operation, and time window.

---

## IMS Transaction Monitoring

This section logs IMS transactions. It records:

* **DL/I calls**
* **SMF records**
* Database accesses performed by IMS applications

Logging modes determine how IMS activity contributes to monitoring database access patterns and transaction‑level visibility.

---

## Guardium .tgz Deployment

Instructions for deploying a Guardium system from a packaged **.tgz** file located in the `releases/` directory. The file contains the full Guardium software bundle but does not detail the specific features installed.

## Cluster Node Registration

Managed units excluded from alerts automatically generate system exclusion groups per alert when the alerts are activated on those units.

**Key Concepts:** Alert Exclusions, Managed Units, System Groups, Activation

## Central Management Configuration Profiles

Edit or add configuration profiles for distribution from Central Management, optionally assigning a security role.

**Key Concepts:** Configuration Profiles, Distribution, Security Roles, Central Management

## Document Overview

IBM Guardium Data Protection monitors and secures structured and unstructured data across on‑premises and cloud data stores. It offers real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

**Features**
- Dynamic port detection and multi‑driver support for datasource connectivity
- Real‑time threat detection with S‑GATE blocking and incident generation
- Pre‑built report templates for PCI‑DSS, GDPR, HIPAA, SOX; automated audit trails

**Workflows**
- **Configuration:** Add datasources, deploy S‑TAP via GIM, configure FGAC policies
- **Navigation:** Review activity reports, run vulnerability assessments, use audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents

**Personas**
- **Administration:** Platform setup, user management
- **Security Administrator:** FGAC policies, audit policies
- **Database Administrator:** Datasource management, S‑TAP deployment
- **Data Analyst:** Dashboard usage, query execution
- **Compliance Officer:** Regulatory report generation
- **Security Analyst:** Threat investigation

**Entities**
- Agents/Collectors: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- Policies/Rules: Security Policy, Audit Policy, Classification Rule, Access Rule
- Infrastructure: GIM, Managed Unit, S‑GATE, Universal Connector

## Exception View Attribute Definitions

An exception view customizes audit result displays by assigning compatible data types (Date, VARCHAR, numeric) to selected attributes. Proper type assignment ensures correct formatting, filtering, and analysis of exception records.

**Key Concepts:** Exception View, Attribute Definition, Data Type Specification, Audit Result Customization

## Document Overview

IBM Guardium External S‑TAP enables real‑time database activity monitoring for databases in DMZs, private clouds, Kubernetes, or managed services where a native S‑TAP cannot be installed. It captures encrypted traffic transparently on a dedicated host or container and forwards it to a Guardium collector for analysis, blocking, and reporting.

**Features**
- Flexible deployment on Linux hosts or containers in various environments
- Transparent traffic capture using network sniffing
- Automatic TLS/SSL decryption when keys are supplied
- Scalable, high‑availability active‑active deployment

**Workflows**
1. **Provisioning:** Deploy External S‑TAP image on a host with network access to the database.
2. **Configuration:** Provide database IP/port, TLS certificates (if encrypted), and collector endpoint via Guardium UI or API.
3. **Activation:** Start S‑TAP service; traffic intercepted and forwarded in real time.
4. **Monitoring & Management:** Use Guardium dashboards, reports, and alerts to monitor activity, generate alerts, and enforce blocking.

**Personas**
- **Security Administrator:** Deploys, configures, manages certificates, defines FGAC rules.
- **Database Administrator:** Provides network/credential info; ensures performance impact is minimal.
- **Compliance Officer:** Reviews audit reports, verifies regulatory compliance.
- **Ops Engineer:** Monitors health, scales, troubleshoots External S‑TAP hosts.

**Entities**
- External S‑TAP Instance: Host/container running the External S‑TAP service.
- Collector / Aggregator: Guardium collector receiving and processing traffic.
- Certificates & Keys: TLS certificates and private keys for decryption.
- Network Interfaces: Network adapters used to tap traffic.

## Compressed Reference

## External S‑TAP Overview
Guardium External S‑TAP (Software Tap) captures live database traffic for on‑premises, private‑cloud, Kubernetes, and managed‑service environments without installing agents on the database host. It runs on a separate Linux host or container, optionally decrypts TLS traffic, and forwards clear‑text payloads to a Guardium collector for real‑time policy evaluation and logging.

### Supported Deployment Scenarios
- **On‑Premises DMZ** – Deploy on a bastion host with network routes to the database.  
- **Private‑Cloud VM** – Run as a VM in a private‑cloud VPC, attached to the database subnet.  
- **Kubernetes Pod** – Deploy as a privileged pod using host‑network mode.  
- **Managed‑Service Proxy** – Use where OS‑level access is restricted (e.g., Amazon RDS, Azure Database for PostgreSQL, Google Cloud SQL).

### Key Benefits
- No kernel modules or agents on the database host.  
- Insight into encrypted traffic when TLS keys are supplied.  
- Uniform monitoring across on‑prem and cloud assets.  
- Compliance with PCI‑DSS, HIPAA, GDPR, etc.

### Operational Workflow
1. Provision a Linux VM/container with NIC access.  
2. Pull the Guardium External S‑TAP Docker image or boot the VM image.  
3. Define source IP ranges, destination DB IP/port, and DNS resolution.  
4. Upload server certificate, private key, and optionally client certificates for mutual TLS.  
5. Register the S‑TAP with Guardium via GuardAPI (`add_external_s_tap`) or UI.  
6. Activate monitoring; traffic is mirrored to the collector for policy/audit processing.  
7. Maintain certificates, policies, or scale the S‑TAP cluster as traffic changes.

### Architectural Components
- **Linux Host / Container** – Provides network tap (tcpdump/pcap) and runs the S‑TAP service.  
- **TLS Decryption Keys** – Optional, securely stored for decrypting sessions.  
- **Forwarder Daemon** – Encapsulates packets into TCP streams sent to the Guardium collector over TLS.  
- **Guardium Collector** – Assembles queries, applies FGAC/AVC policies, and logs activity.

## Guardium Data Protection Overview
IBM Guardium Data Protection is an enterprise platform for real‑time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Features Overview
- **Datasource Connectivity** – JDBC & native drivers, generic drivers, dynamic port detection, CyberArk credential vault.  
- **Threat Detection** – Real‑time policy enforcement, S‑GATE blocking, security incidents, anomaly detection, threat analytics.  
- **Compliance & Reporting** – PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit trails; data discovery and classification.  
- **Unified Data Protection** – Encryption at rest & in motion, tokenization, encrypted file transfers.

### Workflows Overview
- **Configuration** – Add datasource, deploy S‑TAP via GIM, configure FGAC policies, enable anomaly detection, set up client web certificates.  
- **Navigation** – Activity explorer, session explorer, audit dashboard, anomaly detection console, policy manager.  
- **Action** – Block unauthorized queries, rotate credentials, respond to incidents, manage data masking, repair security issues.

### Personas Overview
- **Administration** – Platform configuration, user management.  
- **Security Administrator** – FGAC, policies, anomaly detection.  
- **Database Administrator** – Datasource setup, S‑TAP deployment.  
- **Data Analyst** – Dashboards, queries, data masking.  
- **Compliance Officer** – Regulatory reports, data discovery.  
- **Security Analyst** – Threat investigation, response actions.

### Entities Overview
- **Agents & Collectors** – S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager, browser service.  
- **Policies & Rules** – Security policy, audit policy, classification rule, access rule, FGAC, anomaly detection rules.  
- **Infrastructure** – GIM (Guardium Installation Manager), Managed Unit, S‑GATE, Universal Connector, GuardAppEvent.  

## Client Web Certificates
Supports configuration of client web certificates to authenticate and encrypt SSL/TLS communications between Guardium components and external web interfaces.

## Activity Monitoring & Policy Enforcement
Captures database traffic via S‑TAP agents, evaluates it against real‑time policies, and triggers alerts, reports, or S‑GATE blocking based on user, object, operation, and time criteria.

## Special Handling for TRANSFORM Actions
TRANSFORM actions modify captured data for masking or compliance. Ensure proper configuration to avoid undownloadable audit files when blob bind variables are unsupported, and guarantee accurate classification and reporting of sensitive data.

## IBM Guardium Overview

IBM Guardium Data Protection centrally monitors, enforces policies, and generates compliance reports for structured and unstructured databases across on-premises and cloud environments. It prevents unauthorized access, detects malicious activity, and provides audit-ready evidence for regulatory controls.

### Core Features
- **Dynamic Datasource Discovery:** Automatically identifies database ports and supports native and generic JDBC/ODBC drivers, integrating with CyberArk for credential management.
- **Real‑Time Threat Prevention:** Uses S-TAP agents and S-GATE appliances to block violations, enforces FGAC policies, and evaluates policies continuously.
- **Compliance Reporting:** Includes built‑in templates for PCI-DSS, GDPR, HIPAA, SOX, and automates evidence collection and audit trails.

### Key Concepts
- **S-TAP:** In-process agent capturing database traffic.
- **S-GATE:** Appliance that enforces blocking actions.
- **FGAC Policies:** Fine‑grained access control rules for data sensitivity.

## Database Connection Architecture

Guardium ingests database traffic through S-TAP agents that capture packets at the host level and forward them to collectors for analysis. Dynamic port detection using browser services and support for native and generic JDBC/ODBC drivers ensure broad compatibility. Real-time policy evaluation can trigger immediate blocking via S-GATE appliances.

## Activity Monitoring & Policy Enforcement

Guardium captures complete SQL streams from S-TAP agents and matches statements against active security policies. Violations result in alerts, audit‑log storage, or immediate S-GATE blocking. Policies can be scoped by user, object, operation, time window, and data sensitivity, enabling granular, least‑privilege enforcement.

## Verify Classification API Key Exists

An API key (`cadb51e0-d93a-4e1a-956c-bc62304d6cda`) must exist to use the API for extracting and downloading profile templates during data classification. This key ensures secure access to the classification feature.

**Key Concepts:** API Key, Data Classification, Profile Template

---

## S-TAP Upgrade Continuity

During an S-TAP upgrade, database traffic is still monitored, with the database using the previous version of the exit library, ensuring no interruption in monitoring or service.

**Key Concepts:** S-TAP Upgrade, Database Monitoring, Exit Library

---

## K-TAP Enablement After Installation

If K-TAP was automatically installed using P-CAP, instructions are provided for enabling it, including ensuring kernel compatibility, as the S-TAP process checks the kernel to determine if K-TAP is required.

**Key Concepts:** K-TAP, Kernel Compatibility, S-TAP Installation

---

## Guardium Gateway Process Information

To redirect the S-TAP debug log to a larger partition, use the command `ps -ef | grep gtwgateway` to identify the process for troubleshooting and log management.

**Key Concepts:** S-TAP Debug Log, Process Management, Log Partitioning

---

## SessionLossesMetadata Parameter

The `SessionLossesMetadata` parameter allows sending metadata when packet losses occur in a session, aiding in monitoring network reliability and issues. Setting it to `1` enables this feature.

**Key Concepts:** Metadata Transmission, Packet Loss, Network Reliability

---

## DataStax Cassandra Auditing Parameters

Parameters and their descriptions for configuring DataStax Cassandra auditing include connection details, memory settings, database information, and encryption options, essential for setting up auditing.

**Key Concepts:** Auditing Parameters, DataStax, Cassandra

---

## HDFS Audit Processing Error

When HDFS audits are not processed, a `CannotObtainBlockLengthException` is logged, referencing a `LocatedBlock` object with properties related to block length issues in HDFS auditing.

**Key Concepts:** HDFS Auditing, Block Length Exception, Log Analysis

---

## Guardium Audit Logging Options

Configurations for audit logging in DataStax Cassandra include connection settings, memory allocation, database specifics, and encryption preferences to ensure comprehensive logging and monitoring.

**Key Concepts:** Audit Logging, Configuration, DataStax Cassandra

---

## Custom Certificate Import and Mutual Authentication

To configure mutual authentication with External S-TAP, import the custom certificate. This ensures that both the data store server and client verify each other's certificates, enhancing security in database connections.

**Key Concepts:** Mutual Authentication, Certificate Import, External S-TAP

```markdown
## GuardAPI Parameters for Scheduling Policy Analysis

Key Concepts: GuardAPI, Policy Analysis, Command Parameters

## show db-top-tables Command

Lists all tables in a database or filters by name pattern to identify large tables affecting performance.

Key Concepts: Database Management, Large Tables, Performance Analysis

## Guardium Data Protection Overview

### Features

- Supports native protocols for Oracle, SQL Server, MySQL, PostgreSQL, Teradata, MongoDB, etc.
- Rule‑based access control, session inspection, data masking, alerting
- Distributed architecture with collectors, aggregators, and a central manager
- Real‑time anomaly detection and machine‑learning profiling
- Modern data classification rules for personal data, credit‑card numbers, and regulatory identifiers

### Workflows

1. Add datasources & deploy agents (register databases, install/verify S‑TAP agents, configure GIM lifecycle)
2. Create FGAC policies (define groups, objects, operations, time windows for blocking/monitoring)
3. Run compliance assessments (schedule scans, generate audit reports, export evidence)
4. Incident response (investigate alerts, block sessions, rotate credentials, generate forensic evidence)

### Personas

- Security Administrator – manages policies, reviews alerts, audits activity
- Compliance Officer – produces regulatory reports, monitors coverage
- Database Administrator – installs S‑TAPs, configures data sources, troubleshoots
- Data Analyst – consumes dashboards, runs ad‑hoc queries, verifies discovery results

### Entities

- Managed Units – collections of collectors/aggregators communicating with the central manager
- Agents & Appliances – S‑TAP (in‑process), A‑TAP (network), K‑TAP (kernel‑level), database‑specific collectors
- Policy Components – security policies, audit policies, FGAC rules, classification rules, access‑control rules
- Infrastructure – central manager, managed units, GIM (Guardium Installation Manager), S‑GATE (blocking gateway)

## api_target_host Parameter

Defines where a REST API request executes.

| Value | Effect | Scope |
|---|---|---|
| **`central_manager`** | Executes on the central manager only; changes are synchronized across all managed units. | Controlled actions (install agents, modify configuration). |
| **`all`** | Executes on every managed unit **and** the central manager; useful for system‑wide operations. | System‑wide restarts, health checks, bulk data collection; aggregates results from all endpoints. |
| **Specific hostname/IP** | Executes on the named managed unit only; target‑ed actions affect a single unit. | Precise actions (e.g., add/remove a unit) requiring exact spelling or IP; case‑insensitive match. |

**Validation** – The host is validated against the system’s inventory; invalid hosts return HTTP 400 (Invalid parameter).  

**Cross‑Unit Behavior** – Each unit processes the request independently; failures on one unit do not block others. The response indicates per‑host success or failure.

**Typical Use Cases**

- Deploy a new S‑TAP version across all units (`api_target_host=all`)
- Retrieve the central manager’s configuration (`api_target_host=central_manager`)
- Disable S‑GATE blocking on a single collector (`api_target_host=collector123.local`)
```

## Overview

IBM Guardium provides enterprise-grade database activity monitoring and protection for structured and unstructured data across on-premises and cloud environments. It continuously monitors database traffic, enforces security policies, detects threats, and generates compliance reports.

### Key Features
- Real-time monitoring with S-TAP agents at the kernel level for low overhead
- Policy enforcement via S-GATE to block illegal operations and alert on violations
- Threat detection through behavior analytics, vulnerability assessments, and rule sets
- Compliance reporting with templates and audit trails for frameworks like PCI-DSS, GDPR, HIPAA, and SOX

### Monitoring Workflow
- Datasource discovery to detect new databases automatically or manually
- Policy configuration using the policy builder for security, audit, and classification
- Incident response to investigate alerts, export findings, and orchestrate remediation
- Data masking to prevent unauthorized exposure through redaction or tokenization

### Roles
- Security officer: configures policies, reviews incidents, and generates evidence
- DBA: monitors database health, resolves performance issues, and manages S-TAP
- Compliance manager: uses built-in reports to demonstrate regulatory adherence
- Data steward: performs classification and verifies masking rules

### Entities
- Data sources
- Policies
- Rules
- Alerts
- Violations
- Assessments
- Reports
- Distributions

## Central Guardian Services Overview

### Key Components
- **Agents & Collectors:** S-TAP (network), A-TAP (process), K-TAP (live memory), Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Data Masking Rule.
- **Infrastructure:** GIM, Managed Unit, S-GATE, Central Manager, Universal Connector, Portal.

### Features
- **SAML Reconfiguration:** After restoring a backup with a new hostname/IP, re-download/upload SAML SP metadata to the IdP for uninterrupted SSO.

### Capabilities
- **Real-Time Monitoring:** S-TAP, S-GATE, Security Policy for live database traffic analysis.
- **Compliance Reporting:** PCI-DSS, GDPR, HIPAA, SOX templates with automated audit trails.
- **Central Management:** Unified control via GIM for on-premises and cloud data sources.

### Workflows
- **S-TAP Management:** Installation, verification, uninstallation, and debugging.
- **Activity Monitoring:** Dynamic policy enforcement, alerts, and logging.
- **Load Balancing:** Thread configuration for S-TAP-Guardium data handling.
- **Status Verification:** Post-ATAP and S-TAP installation checks using GIM.

### Personas
- **Database Administrators:** Manage S-TAP, ensure policy compliance.
- **Security Administrators:** Define and enforce security policies, monitor security logs.
- **Compliance Officers:** Generate and review compliance reports.
- **Security Analysts:** Investigate incidents, analyze activity logs.

## Configuring Client Web Certificates

To configure client web certificates in Guardium, follow these steps:

1. Upload the client web certificate files to the Guardium system.
2. Configure the Guardium system to use the uploaded certificates for secure communication.
3. Define which client certificates are authorized to access Guardium resources by setting up authentication policies.
4. Test the configuration by accessing Guardium resources using client web certificates.

## Decrypting Traffic Through Two Proxies

To decrypt database traffic routed through two proxies, follow these steps:

1. Configure the first proxy to intercept and forward database traffic to the second proxy.
2. Configure the second proxy to decrypt the intercepted traffic and forward it to the database server on a non-SSL port.
3. Ensure the database server does not listen on the port used by the first proxy.
4. Verify the end-to-end decryption process by checking logs and connection status.

## Disabling Teradata Exit Library

To disable the Teradata exit library on Linux-UNIX systems, follow these steps:

1. Review the Linux-UNIX documentation for disabling Teradata's exit library.
2. Execute the documented commands or procedures to disable the exit library.
3. Verify that the monitoring library is fully disabled by checking system logs and configuration files.
4. Test the system to ensure no unintended monitoring conflicts occur.

## Supporting HDFS Audits with Ranger Integration

To enable HDFS audits with SSL, Kerberos, and Ranger integration, follow these steps:

1. Configure HDFS services to use SSL encryption and Kerberos authentication.
2. Ensure all HDFS clients are configured to authenticate using Kerberos tickets.
3. Deploy the Guardium S-TAP agent on HDFS nodes to monitor traffic.
4. Integrate Ranger with Guardium to provide comprehensive audit and access control for HDFS resources.
5. Verify the configuration by performing test audits and checking Ranger policies.

**CLI Network Reset Procedure**

Log in as `guardcli` and execute `guard-config-update --network-reset` to purge stored settings, then reboot to start the network configuration wizard.  

**Precaution:** Ensure physical access to the appliance during the reset to supply new network parameters.

## Manage Security Policies

Guardium policies enforce real-time data security through a flexible, rule-based framework.  

### Building Policies
- Use the **Policy Builder** wizard or manual rule editor to construct security, audit, classification, and access policies.  
- Define rule conditions based on database objects, user identities, query contents, and session attributes.  
- Specify enforcement actions (log, alert, block, or terminate) and combine multiple rules into logical groups.  

### Deployment
- Deploy policies instantly to managed Collector units; changes take effect without Collector restarts.  
- Verify enforcement by querying the **MAS Table** for real-time rule status updates.  

### Monitoring & Tuning
- Review **Enforcement Reports** to track rule hits, false positives, and performance impact.  
- Refine rules iteratively, leveraging the **Rule-based Tuning** suggestions for optimal coverage.  

### Advanced Responses
- Combine standard actions with conditional flows (if/else logic) to create dynamic, context-aware responses.  
- Leverage the **Query Language** to script multi-step remediation workflows triggered by policy violations.

## Connection String Verification
Verify a client can establish a secure connection to a Guardium server using the connection string.

## Anchor S-GATE
Configure S-GATE in Guardium Data Protection to block or modify SQL statements.

### Steps
1. Enable S-GATE: `store sgated enabled true`
2. Define security policies
3. Adjust operational limits: `store sgated_limits`
4. Enable caching: `store sgated_cached`
5. Configure auditing: `store sgated_audit`
6. Monitor status: `view sgated_status`, `view sgated_stats`

## Document Overview
IBM Guardium Data Protection platform features, workflows, personas, and entities.

### Features
- Datasource connectivity
- Threat detection
- Compliance & reporting

### Workflows
- Configuration
- Navigation
- Action

### Personas
- Administration
- Data & Database Management
- Compliance & Audit

### Entities
- Agents & collectors
- Policies & rules
- Infrastructure

## Policy Rule Elements
Attributes "App. User" and "Category" create conditional logic in Guardium policy rules.

## Query Rewrite and Access Policy
Guardium query rewrite transformations enforce access policies dynamically.

### Activation
1. Activate security policy
2. Define query rewrite definitions

## Monitoring Database Usage Across Systems

Guardium automatically tracks databases accessed via network traffic, data source definitions, and compliance monitoring, even if they aren't pre-configured.

- Guardium's detection capability extends to monitoring all databases connected through registered sources or monitored for compliance, ensuring comprehensive security coverage.

This automatic recognition enables Guardium to protect all relevant databases within an organization reliably.

---

## Exploitation Risks of Stored Procedures

Stored procedures can be misused to carry out attacks, as demonstrated by a malicious administrator's two-step process targeting sensitive data.

1. **Initial Step:** Creation of a stored procedure followed by granting temporary elevated privileges.
2. **Execution Phase:** After a set period, the procedure is altered to delete or corrupt critical data without immediate detection.

Identifying the involvement of stored procedures, user accounts, and privilege changes aids in securing databases against such threats.

---

## License Management for Continuous Protection

Monitoring the "Of Licenses" value in IBM Guardium ensures that all security and compliance components remain fully licensed and operational.

- Regular license checks prevent any service disruptions that could compromise the integrity of database protection mechanisms.

An adequate license count maintains full functionality across all monitored systems and data sources.

---

## Assessing Transaction Exposure in Disaster Scenarios

Testing the resiliency of database systems against various failure modes is essential to ensure they can withstand operational disruptions without significant data loss.

- Scenario-based testing focuses on the directionality of transaction processing and the robustness of data handling methods to identify potential vulnerabilities.
- Evaluation includes user behaviors and error conditions to cover all possible failure sources comprehensively.

Regular exposure assessments help strengthen system designs against both technical and human-induced risks.

---

## Centralized Recovery for Managed Aggregators

Restoring a centrally managed aggregator in IBM Guardium utilizes configuration data stored on the central manager, streamlining the recovery process.

- **No Local Data Restoration Required:** Since all configuration data resides centrally, only the aggregator's status needs to be restored, minimizing downtime and complexity.
- **Centralized Control:** The aggregator, as a pivotal system component, benefits from centralized management, reducing the need for individual node recovery efforts.

This approach simplifies disaster recovery and enhances system resilience.

---

## System Health Checks for Aggregator and Collectors

Regular health monitoring of aggregator and collector units ensures the reliability and performance of the IBM Guardium deployment.

- **Status Indicators:** Registering a unit takes about 15 minutes to reflect in health views; configuration changes may take up to 2 hours to update.
- **Operational Overviews:** Deployment health views provide essential insights into system status, helping identify and address issues promptly.

Consistent health monitoring maintains the security posture and efficiency of Guardium's surveillance systems.

---

## Enhanced MustGather Command Organization

In version 12.1, IBM Guardium reorganized its MustGather commands by component, facilitating more targeted troubleshooting efforts.

- **Component-Specific Commands:** Grouping commands by system component allows administrators to quickly access the relevant diagnostics tools, improving issue resolution efficiency.

## Guardium Data Protection Overview

IBM Guardium Data Protection provides comprehensive monitoring, policy enforcement, threat detection, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- **Universal Connector**: Collects native logs using custom plug-ins without requiring S-TAP agents
- **Path Verification**: Ensures correct database server installations through db2 path utilities
- **Plugin Configuration**: Provides custom values for Hook main rules to manage monitoring chains

### Essential Workflows
- **S-TAP Activation/Deactivation**: Manage K-TAP switching and validate K-TAP modules
- **Linux Compatibility Checks**: Verify K-TAP versions before upgrading the operating system
- **Policy Hooking**: Integrate S-TAP rules with security chains for enhanced monitoring

### User Personas
- **Administrators**: Manage S-TAP installations, switch to K-TAP, configure plugins
- **Security Analysts**: Verify API keys, inspect plugin dependencies, trace hook rules
- **Compliance Officers**: Ensure configurations align with security policies

### Core Entities
- **Agents & Collectors**: S-TAP, K-TAP, Universal Connector plug-ins
- **Configuration Paths**: db2 path utilities, Guardium installation directories
- **Policy Hooks**: Main rules, security chains, Ranger log4j integrations

## Guardium Data Protection: Overview 

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features

- **Datasource Connectivity:** Supports JDBC drivers, native drivers, dynamic port detection
- **Anomaly Detection:** Identifies repeated failed logins, unusual session behavior, policy violations  
- **Compliance & Reporting:** Generates PCI-DSS, GDPR, HIPAA, SOX reports with customizable condition attributes
- **Audit & Visibility:** Covers terminated users, session details, report customization options

### Workflows

- **Environment Setup:** Enables datasource connection, applies TRANSFORM actions, uses packaged tooling
- **Policy Configuration:** Defines SQL parsers, model queries, audit policy details 
- **Monitoring & Response:** Tracks failed logins, security incidents, session activity
- **Report Generation:** Produces compliance reports, activity summaries, identifies potential threats

### Personas

- **Security Administrators:** Configure policies, monitor anomalies, respond to incidents
- **Database Administrators:** Manage datasources, review query activities, handle permissions
- **Compliance Officers:** Generate regulatory reports, ensure data protection standards
- **Analysts:** Investigate anomalies, use visualization tools, trace user activities

### Entities

- **Agents & Collectors:** S-TAP, A-TAP, K-TAP for traffic capture 
- **Policy Components:** Security Policy, Audit Policy, Classification Rule, Access Rule
- **Data Identity:** Terminated DB Users, application users, session attributes
- **Reporting Tools:** Report builder, packaged tooling, visualization components

## Managing S-TAP with `guard-config-update`

Administrators can install and manage S-TAP agents across different installation methods (GIM, RPM, shell) using the `guard-config-update` utility. This simplifies the S-TAP lifecycle without needing to know the underlying installation method.

**Basic usage:**

```bash
# Install S-TAP (detects current method)
guard-config-update --install-s-tap

# Start S-TAP
guard-config-update --start-s-tap

# Stop S-TAP
guard-config-update --stop-s-tap

# Check S-TAP status
guard-config-update --status-s-tap
```

## Document Overview

IBM Guardium Data Protection secures enterprise data across databases and big data stores through real-time activity monitoring, policy enforcement, compliance reporting, and vulnerability assessment. It employs S-TAP agents for capturing database traffic, evaluates it against security policies, and triggers alerts or blocking. Key features include real-time monitoring, compliance reporting, vulnerability assessment, and access governance.

### Features Overview
- Real-Time Monitoring via S-TAP agents
- Compliance Reporting with audit trails and templated reports
- Vulnerability Assessment for configuration weaknesses
- Access Governance to control user privileges and monitor data access

### Workflows Overview
- Configuration of agents (S-TAP, GIM), defining policies, and setting up user roles
- Incident Response by investigating alerts, blocking unauthorized queries, and rotating credentials
- Administration of datasource connections, monitoring dashboards, and generating reports

### Personas Overview
- Security Administrators define policies and oversee threat detection
- Compliance Officers access regulatory reports and ensure data protection
- Security Analysts investigate alerts and analyze activity reports
- Database Administrators configure datasources and maintain system performance

### Entities Overview
- Agents: S-TAP, GIM, K-TAP, A-TAP
- Infrastructure: Central Manager, Aggregator, Managed Units
- Policies: Security Policy, Audit Policy, Access Rule, Classification Rule
- Audit Artifacts: Reports, Alerts, Logs, Dashboards

---

## CAS Execution Environment Variables

Environment variables (`$UCAS`, `$PCAS`, `$ICAS`) provide the DB username, password, and instance name for script execution, enabling dynamic script execution in the CAS run environment.

---

## Oracle Kerberos Authentication Configuration

SQLNET parameters for Oracle Kerberos authentication configuration include `SQLNET.authentication_services`, `SQLNET.KERBEROS5_REALMS`, `SQLNET.KERBEROS5_KEYTAB`, and `SQLNET.KERBEROS5_CONF`.

## External S-TAP Image Deployment

Use `skopeo list-tags docker://icr.io/ibm-guardium/external_stap:<signing_token>` to list available image tags. Retrieve `<signing_token>` with `show certificate external_stap_signing`.

## Comprehensive Tool Overview

IBM Guardium Data Protection provides end-to-end database security solutions. Core
components include S-TAP agents for real-time traffic monitoring, policy definitions
for access control, and centralized management through GIM. It supports compliance
automation, vulnerability assessment, and incident response across hybrid environments.

## Key Features

- **Real-Time Monitoring:** S-TAP and A-TAP agents capture database activity
- **Policy Enforcement:** FGAC policies, data classification, and access controls
- **Compliance Reporting:** Pre-built and custom templates for regulatory needs
- **Incident Response:** Alert investigation, session blocking, and automated remediation

## Common Workflows

1. **Agent Deployment:** Install via GIM, configure network settings, and register with Central Manager
2. **Policy Creation:** Define FGAC rules, assign to managed units, and enable enforcement
3. **Compliance Auditing:** Generate reports, audit user privileges, and schedule exports
4. **Threat Investigation:** Analyze alerts, quarantine sessions, and automate responses

## User Personas

- **Security Administrators:** Manage policies, monitor alerts, and configure infrastructure
- **Database Administrators:** Deploy agents, tune performance, and review access patterns
- **Compliance Officers:** Access audit logs, generate compliance reports, and manage policy changes
- **Incident Responders:** Investigate incidents, block sessions, and orchestrate remediation

## System Architecture

- **Deploy Agents:** Use GIM to install S-TAP on all monitored systems
- **Define Policies:** Create FGAC rules, classification rules, and access masks
- **Configure Infrastructure:** Set up aggregators, central managers, and failover clusters
- **Integrate Systems:** Connect databases, file systems, and cloud services to Guardium

## Feature Details

- **FGAC Policies:** Granular access controls based on user, data, and context
- **Classification Rules:** Automatically categorize sensitive data based on patterns
- **Access Rules:** Control data access through predefined conditions
- **K-TAP and A-TAP:** Alternative capture methods for environments where S-TAP is unsuitable
- **GIM Integration:** Centralized agent management and configuration

## Configuring CSV Export Size

Set global profile parameters to manage CSV export behavior:
- `csv_fetch_size`: Number of rows fetched per database call (default: 100)
- `csv_max_size`: Maximum file size before rotation (default: 50 MB)

Adjust these values via the Guardium CLI using `store csv_fetch_size` and `store csv_max_size`. Changes require a Guardium service restart to take effect. For large exports, gradually increase `csv_fetch_size` while monitoring system memory usage.
Back to [Configuration Workflows](#configuration-workflows)

---

## Managing Central Units

Central Manager (CM) is the primary Guardium appliance that coordinates activities across multiple Managed Units (MUs). Key responsibilities include:
- Centralized configuration management
- Policy distribution to Managed Units
- Aggregation of audit data from collector units

When configuring a Central Manager:
1. Ensure sufficient hardware resources (CPU, memory, storage)
2. Configure proper network connectivity to all Managed Units
3. Set up SSL certificates for secure communications
4. Define database connections for audit data collection

Regularly monitor Central Manager health and capacity to prevent bottlenecks in audit data collection and reporting.
Back to [Configuration Management](#configuration-management)

---

## Guardium API Basic Authentication

To interact with Guardium using REST APIs:
1. Obtain an API key from the Guardium UI under Administration > Users > API Keys
2. Set the `Authorization` header as `Bearer <your_api_key>`
3. Include `api_target_host` parameter if calling from a Managed Unit

Example API call using curl:
```bash
curl -k -X GET \
  -H "Authorization: Bearer your_api_key_here" \
  -H "Content-Type: application/json" \
  "https://your-guardium-host:8443/restAPI/policy?api_target_host=central_manager_address"
```
The `api_target_host` parameter specifies where the API should be executed - typically set to the Central Manager's address.

Authentication tokens expire after 30 minutes by default. For persistent sessions, periodically refresh the token using the `/restAPI/session` endpoint.
Back to [Configuration Workflows](#configuration-workflows)

---

## Deploying Guardium S-TAP

To deploy S-TAP agents:
1. Download the appropriate S-TAP package from the IBM Support site
2. Extract the agent on a local machine or directly on the target database server
3. Run the installation script with root privileges

Post-installation configuration includes:
- Defining monitoring parameters in the Guardium UI
- Establishing connection between S-TAP and Central Manager
- Configuring data collection options (full SQL, partial SQL, etc.)

For Linux systems, verify that necessary kernel headers are installed and that the Guardium kernel module was properly loaded:
```bash
lsmod | grep stap
```

Back to [Configuration Workflows](#configuration-workflows)

## Running Security Assessments

IBM Guardium enables running vulnerability assessments through the VA Scanner application. The scanner must be installed on a Linux system with access to the Guardium Central Manager. The scan process involves creating a new scan, selecting appropriate scan templates or tests, and scheduling or manually initiating the scan. To execute a guardium vulnerability assessment, follow these steps: identify the systems and databases to be scanned, choose a standard assessment template or create a custom one, configure the scan parameters including target hosts and credentials, schedule or start the assessment scan immediately, and review and analyze the assessment results and generated reports. Key procedures include running the `create_vulnerability_assessment_template.grdapi` script, creating a datasource connection to the target database, and initiating the security assessment with the desired test selections through the Guardium UI or API.

**Key Concepts:** VA Scanner, Custom Assessment, Scan Template, Grdapi Script

## Running File Scanning Jobs

IBM Guardium's File Activity Monitoring (FAM) schedules automated discovery jobs that periodically scan defined file system targets, apply classification policies, and surface findings in real time. To configure a scanning job, select agents, define scanning frequency, set target paths, run discovery jobs, review discovered data objects, apply classification rules, enable alerts and remediation actions, and export findings and generate compliance reports. Key concepts include scanning jobs, data discovery, classification policies, and scan schedules.

**Key Concepts:** Scanning Jobs, Data Discovery, Classification Policies, Scan Schedules

## Comprehensive IBM Guardium Summary

IBM Guardium Data Protection is an enterprise-grade platform for monitoring, protecting, and reporting on database activity across heterogeneous environments. It supports multiple connection types, including JDBC and native drivers, and offers conditional access controls (FGAC) to enforce fine-grained security policies. The system enables archival management for long-term audit data retention, compliance reporting, and threat detection through real-time policy enforcement and security incident generation.

Key components include S-TAP agents for real-time traffic capture, central management via the Collector-Aggregator architecture, and various personas (Administrators, Data Analysts, Compliance Officers) for tailored access and operations. Guardium also integrates with external services like CyberArk for credential management and supports virtual deployment on platforms such as Hyper-V.

The platform provides REST API capabilities for automated management tasks, such as creating database groups, and includes advanced features like behavioral analytics to assess user risk profiles and detailed alert categorization for actionable insights. Proper certificate management for external S-TAP verification and configurations for virtual environments ensure secure and scalable operations.

## Configuration Auditing System (CAS) Overview

The Configuration Auditing System (CAS) is a stand-alone process in Guardium that monitors configuration changes independently of the Tomcat application server. It consists of a CAS server on the Guardium system and a CAS client on the database server, enabling comprehensive configuration auditing.

## 1029. Create user hierarchy via grdapi

The `grdapi create_user_hierarchy` command adds a parent-child relationship between users in a Guardium environment. It requires the `userName` of the child user and the `parentUserName` of the existing parent user. The `userID` for each user must already be defined, and the parent user must be in a higher hierarchy level than the child.

**Key Concepts:** User Hierarchy, Security, Access Control

## Skip Registry Certificates

In a thin Guardium environment, registry certificates can be omitted during specific operations, streamlining setup while maintaining system integrity.

## Enterprise Load Balancing Monitoring

Monitor and analyze enterprise Guardium load balancing activity using the provided UI sections and reports for insights into load distribution and system performance.

## IBM Guardium Data Protection

**Features:**
- Supports JDBC drivers for Oracle with dynamic port detection
- Captures traffic via S-TAP agents and Db2 Exit library
- Real-time FGAC, S-GATE blocking, and policy enforcement
- PCI-DSS, GDPR, HIPAA, SOX compliance templates
- Automated audits and email notifications

**Workflows:**
- Configure datasources, agents, FGAC/audit policies, SMTP alerts
- Review activity reports, threat alerts, S-GATE blocks, system status
- Perform vulnerability assessments, agent updates, credential vault integration

**Personas:**
- System admin configures Guardium platform and user management
- Policy admin defines FGAC/access rules and S-GATE blocks
- DBAs add datasources and adjust Oracle/Db2 parameters for Guardium
- Auditors generate reports and receive alerts

**Components:**
- Agents & Collectors: S-TAP, A-TAP, K-TAP, aggregators, central manager
- Policies & Rules: Security policies, audit policies, FGAC/access rules, policy groups
- Infrastructure: Guardium Infrastructure Manager (GIM), managed units, S-GATE, Db2 Exit library

### Features Overview
- **Datasource Connectivity:** Dynamic port detection, multi-driver support, IBM Informix support
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation
- **Compliance & Reporting:** PCI-DSS, GDPR, HIPAA, SOX report templates, automated audit trails for Informix

### Workflows Overview
- **Configuration:** Add datasource, deploy S-TAP via GIM, configure FGAC policies for database engines
- **Navigation:** Review activity reports, run vulnerability assessments, audit dashboard for Informix
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents across data sources

### Personas Overview
- **Administration:** Administrator (platform config, user management), Security Administrator (FGAC, policies for databases)
- **Data & Database Management:** Database Administrator (datasources, S-TAP deployment for engines like Informix), Data Analyst (dashboards, queries)
- **Compliance & Audit:** Compliance Officer (regulatory reports), Security Analyst (threat investigation across data sources)

### Entities Overview
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule for various data stores
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector for Informix and other databases

ystematically integrates database instances, ensuring seamless interaction across different Guardium components. This integration establishes a secure, encrypted connection, vital for safeguarding data transmitted through web-based applications.

### Configure for Client Web Certificates
To enable client web certificate authentication in Guardium, configure the application to trust client certificates. This requires setting up a trust store with CA certificates and configuring the web server to require client certificates for authentication.

### Special Handling for TRANSFORM Actions: Incident Exceptions
Defines a custom exception for a specific incident type (PLAIN_PASSWORD) using an IF condition to match incidents and the THROW_EXCEPTION action to specify exception details like type and message.

### Special Handling for TRANSFORM Actions: Incident Exception Management
Incident management functions are accessible through incident management report drill-down menus, varying by user security roles. Role-based access control determines specific incident management capabilities accessible to individual users, ensuring proper access to incident management functions.

### Special Handling for TRANSFORM Actions: Regulatory Compliance Features
Lists regulatory requirements like CCPA and SOX, indicating Guardium provides templates for these compliance types. Certain features are available in version 12.2 and later, highlighting specific entities and contextual knowledge about compliance features.

### Special Handling for TRANSFORM Actions: Archival Management
Explains managing archived audit files by specifying retention periods in days or runs. After a new file is added, the oldest file is automatically removed, ensuring efficient storage resource use and a fundamental administrative task.

### Special Handling for TRANSFORM Actions: Custom Table SQL Definition
Explains defining the SQL query used to populate a custom table. The query should be entered directly (excluding newline characters), with all columns explicitly named and aliasing allowed if needed. Discusses key aspects of custom table population related to SQL syntax and keywords used in user-defined queries.

### Oracle Example: Custom Table Configuration
Discusses setting up user-related statements and the necessity of two Application User Translation entries. Provides insight into a workflow for configuring user information in Guardium and highlights the roles involved in database administration.

### Oracle Example: Conditional Grouping in Reports
Defines two condition types in Oracle reports where a group operator is active. "GROUPMember" and "IN GROUP" appear in parameter columns, providing members of a group selected from a dropdown. Clarifies the meaning and usage of these specific keyword entities within query building.

### Oracle Example: Client IP Handling for IPv6 and SSL
Explains handling of client IP addresses for IPv6 and SSL connections in Guardium, requiring specific configurations to ensure accurate logging and policy enforcement for secure and modern network environments.

### Document Overview
IBM Guardium Data Protection is a comprehensive platform for protecting structured and unstructured data across enterprise environments, both on-premises and in the cloud.

### Features Overview
- Secure Authentication Management: Supports password policies, LDAP/Active Directory integration, MFA, and API key lifecycle management.

## Configure for Client Web Certificates

### Requirements
- Minimum 2 GB of free disk space is required for audit logs and temporary files.
- File Activity Monitoring (FAM) discovery agent (crawler) does **not** support TLS encryption.

### Configuration Steps
1. **Prepare Certificate Files**
   - Obtain a valid TLS certificate and private key for the Guardium instance.
   - Ensure the certificate is signed by a trusted Certificate Authority (CA).

2. **Install Certificates**
   - Copy the certificate (`guardium.crt`) and private key (`guardium.key`) to the Guardium server.
   - Place them in a secure directory with restricted access (e.g., `/guardium/certs`).

3. **Configure Guardium to Use Client Web Certificates**
   - Navigate to **Administration → Security → TLS/SSL Settings**.
   - Enable **Client Web Certificate Validation**.
   - Specify the path to the CA certificate (`ca.crt`) that signed the client certificates.

4. **Validate Configuration**
   - Restart the Guardium services to apply the new TLS settings.
   - Verify connectivity by accessing the Guardium web interface using HTTPS.

5. **File Activity Monitoring (FAM) Crawler**
   - The FAM crawler operates **without** TLS encryption.
   - Ensure the crawler has read access to the monitored file systems.

### Notes
- Other components, such as S-TAP connections, must continue to use secured TLS connections.
- Regularly rotate certificates to maintain security posture.

### IBM Guardium Data Protection

**Comprehensive platform** securing structured and unstructured data across databases, files, and big data environments. Real‑time monitoring, policy enforcement, compliance reporting, and threat analytics protect sensitive information from unauthorized access and threats.

#### Features
- **Data Sources:** On‑premises and cloud repositories
- **Monitoring:** Real‑time activity monitoring, unified reporting
- **Compliance:** Automated compliance reporting for regulatory frameworks
- **Threat Detection:** Machine‑learning and anomaly‑based threat detection

#### Workflows
- **Deployment:** Install S‑TAP agents on database servers
- **Configuration:** Define policies, risk assessments, protection groups
- **Investigation:** Create/manage investigations, generate reports
- **Response:** Automatic blocking, alerts, remediation actions

#### Personas
- **Security Administrator**
- **Compliance Officer**
- **Data Analyst**
- **Incident Responder**

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- **Datasource Connectivity:** Supports JDBC drivers (native and generic), dynamic port detection, and CyberArk credential vault integration.
- **Threat Detection:** Enables real-time policy enforcement, S-GATE blocking, security incident generation, and automated alerting.
- **Compliance & Reporting:** Offers built-in reporting templates for common compliance frameworks.

### Components
- **Agents:** S-TAP, A-TAP, Log File Monitor, Log Agent
- **Servers:** Guardium Aggregator, Central Manager, Collectors
- **Policies:** Data Access Policy, User Behavior Policy, Data Protection Policy
- **Reports:** Audit Reports, Vulnerability Assessment Reports, Compliance Reports

## Database Connection Architecture

IBM Guardium supports JDBC connectivity to SQL databases using native drivers for optimized performance and generic drivers for broad compatibility. The platform includes a browser service that dynamically resolves database instance names to current ports. During S-TAP installation, an initial discovery process configures connection information which can be subsequently modified, requiring reconfiguration if network parameters change. Optional components such as credential vaults may be integrated for specific authentication requirements. Configuration involves setting up JDBC connection strings and verifying driver compatibility.

**Key Concepts:** JDBC, native drivers, dynamic port resolution, credential vaults

## Activity Monitoring & Policy Enforcement

Guardium's S-TAP agents monitor database traffic in real-time, evaluating it against configured security policies and generating alerts for violations. Policies may specify user identities, object names, operation types, and time windows. Upon detecting unauthorized access or suspicious behavior, the S-GATE module can dynamically block specific queries while allowing other legitimate traffic to continue. Violations are recorded in the Guardium audit repository, supporting both immediate incident response and historical compliance reporting. The system supports fine-grained control through FGAC (Fine Grained Access Control) policies that apply to specific databases, schemas, or tables.

**Key Concepts:** S-TAP, real-time monitoring, S-GATE, FGAC

## Database Instance Activation

The `guardctl` utility manages S-TAP instances associated with specific database installations. `guardctl db_instance=db2inst1 deactivate` temporarily disables monitoring for the DB2 instance while preserving configuration. Re-activation uses `guardctl db_instance=db2inst1` without the deactivate flag. This allows administrators to control monitoring at the instance level without reinstalling the S-TAP agent, facilitating maintenance operations. Activation state persists across restarts, ensuring persistent control over monitoring scope.

## SELinux Configuration for S-TAP

Proper SELinux configuration requires:
1. Installing `policycoreutils-python`
2. Generating allow rules with `audit2allow`
3. Applying custom modules with `semodule`
4. Restarting the audit service

Validation involves checking Guardium-specific SELinux contexts and permissions. This ensures S-TAP operates without triggering denials that could impair functionality.

**Key Concepts:** SELinux, audit2allow, semodule, customized policy modules

## S-TAP Verification

Guardium implements periodic verification of S-TAP installations and inspection engines according to a configured schedule. The process checks process statuses, connectivity to Guardium collectors, and inspection engine functionality. Failure notifications are generated through the Guardium interface or GRDAPI commands for external system integration. This supports proactive maintenance by identifying issues before they impact security coverage.

**Key Concepts:** automated validation, continuous monitoring, failure alerts

## Group Configuration for HDFS Integration

To integrate HDFS with Guardium, the HDFS user must be granted read access to Ranger audit directories. This involves:
```bash
chown ranger:hadoop /var/log/ranger/audit
```
Verifying access:
```bash
ls -ld /var/log/ranger/audit
```
This configuration allows Guardium to collect HDFS audit data through S-TAP agents, providing comprehensive monitoring across the data ecosystem.

**Key Concepts:** HDFS permissions, user grouping, audit data collection

## API Endpoint for Module Management

The Guardium API provides the endpoint `PUT https://[Guardium hostname or IP address]:8443/restAPI/gim_unassign_client_module` for unassigning modules from GIM clients. This operation requires specifying the client IP address and module name. It demonstrates Guardium's extensive API functionality for managing security configurations programmatically.

**Key Concepts:** REST API, module management, GIM client interaction

## Flexible Module Management for Administrators

Administrators can dynamically adjust client configurations using Guardium's flexible module management through REST API interactions.

## Web Certificate Configuration Workflow

To configure client web certificates for Guardium:

1. Run `guardium stop tap` to disable S-TAP as part of the upgrade procedure
2. Complete certificate configuration using standard Guardium procedures
3. Restart S-TAP with `guardium start tap`

## Daily Volume Estimation for Threat Analytics

Estimate the daily volume of threat analytics cases during the planning phase to ensure proper system sizing and resource allocation. Consider factors such as monitored databases, transaction volumes, and expected threat pattern complexity to prevent performance bottlenecks and ensure timely threat detection.

## Oracle Session Data Collection

For Oracle databases, Guardium uses the FGA_TRAIL data format type to collect session-level audit information, capturing comprehensive monitoring data despite not exposing client/server OS details directly.

## Comprehensive Enterprise Data Protection

IBM Guardium Data Protection provides unified visibility, dynamic adaptation, integrated threat management, and compliance automation for database activity monitoring across heterogeneous data sources, both on-premises and in cloud environments.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection offers real-time database activity monitoring, security policy enforcement, and compliance reporting across structured and unstructured data sources on-premises and in the cloud.

### Features
- Real-time inspection of SQL and NoSQL traffic via S-TAP, A-TAP, and K-TAP agents.
- Agentless collection from Windows, UNIX, and Linux file systems.
- FGAC, S-GATE, and access control lists for granular enforcement.
- Automated tagging of sensitive data across the enterprise.

### Workflows
- **Deployment:** Install S-TAP agents, configure collectors, and activate policies.
- **Monitoring:** Review dashboards, investigate alerts, generate compliance reports.
- **Remediation:** Block queries, rotate credentials, revoke excessive privileges.

### Personas
- **Security Administrator:** Manage policies, roles, and certifications.
- **Database Administrator:** Install agents and tune for performance.
- **Compliance Officer:** Validate adherence to standards (PCI, GDPR, HIPAA).

### Entities
- **Agents:** S-TAP, A-TAP, K-TAP (traffic collectors).
- **Collectors:** Central manager, aggregator (traffic processors).
- **Policies:** FGAC, audit, classification, access control.
- **Infrastructure:** Managed units, S-GATE, Guardium API.

## Document Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security solution that offers real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for both structured and unstructured data across on‑premises and cloud environments.

### Features Overview
- **Guardium Installation Manager (GIM):** Centralized deployment and patch management of agents.
- **Patch Management:** Installation and rollback of patches for S‑TAP, Guardium modules, and related components.
- **API Key Verification:** Secure access to Guardium APIs through validated API keys.
- **Multi‑Zone Installation Support:** Correct handling of primary/secondary zones for components such as S‑TAP.
- **Ingress Annotations:** Optional settings for Kubernetes NGINX ingress controllers.

### Workflows Overview
- **Patch Installation Workflow:** Steps to install, verify, and troubleshoot patches.
- **Service Restart Workflow:** Restarting specific services (e.g., GUI, inspection cores) after updates.
- **Backup/Restore Workflow:** Pre‑upgrade backups to protect against potential upgrade issues.
- **Installation Workflow:** Procedures for agent deployment, including considerations for multi‑zone environments.
- **Troubleshooting Workflow:** Collection of logs and diagnostic data to diagnose and resolve issues.

### Personas Overview
- **Database Administrator:** Manages database configurations, data access, and performance.
- **Security Administrator:** Defines and enforces security policies, audits, and compliance controls.
- **Application Developer:** Integrates Guardium APIs and services into application workflows.
- **Compliance Officer:** Oversees adherence to regulatory requirements and generates compliance reports.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures databases in on-premises and cloud deployments through real-time monitoring, policy enforcement, vulnerability assessments, and compliance reporting.

### Key Features
- **Policy Enforcement:** S-GATE blocking, Fine-Grained Access Control (FGAC), and query rewriting
- **Threat Detection:** Real-time activity analysis, outliers, risk scoring, and SQL injection detection
- **Assessment & Reporting:** Vulnerability scans, Data Source Version History, and compliance templates for PCI-DSS, GDPR, HIPAA, and SOX

### Core Workflows
- **Deployment:** Install S-TAP agents on database hosts, configure Central Manager, and define policies
- **Monitoring:** Enable real-time alerts, generate audit reports, and conduct on-demand vulnerability assessments
- **Enforcement:** Dynamically adjust policy rules, apply adaptive blocking, and perform query rewrites
- **Compliance Management:** Automate regulatory reporting, verify policy adherence, and maintain audit trails

### Personas
- **Security Administrator:** Defines and manages data classification, access rules, and compliance policies
- **Database Administrator:** Installs/configures S-TAP agents, administers Guardium components, and manages backups
- **Compliance Officer:** Reviews compliance reports, generates regulatory audits, and ensures data protection standards
- **Security Analyst:** Investigates security incidents, conducts forensic analyses, and audits user activities

### Architecture Components
- **Agents:** S-TAP (host), A-TAP (appliance), K-TAP (kernel-level), Inspection Engines (database connectors)
- **Management Components:** Collectors, Aggregators, and Central Managers for data processing and storage
- **Policy Engine:** S-GATE, FGAC, and query rewrite capabilities for real-time enforcement
- **Infrastructure Integrations:** Universal Connectors for heterogeneous environments, Ingress Controllers

### Configuration Parameters
- `WINSTAP_CMD_LINE`: Defines command-line options for Windows S-TAP
- `api_target_host`: Specifies target hosts for API calls
- `annotations`: Ingress configuration overrides in K8s deployments

### Operational Tasks
- **API Key Management:** Generate, distribute, and rotate secure API keys for automated integrations
- **Backup/Restore:** Manage Guardium application and configuration data
- **Multi-Zone Installations:** Deploy components across primary and secondary zones for redundancy
- **SnifDb2Exit Configuration:** Activate extended DB2 monitoring on 64-bit systems
- **Guard_STAP Dynamic Configuration:** Use guardctl to adjust specific database instance settings
- **Certificate Management:** CLI-driven keystore administration for secure communications

# IBM Guardium Data Protection Overview

IBM Guardium Data Protection provides enterprise‑grade database activity monitoring, vulnerability assessment, and compliance reporting for structured and unstructured data on‑premises and in the cloud.

## Key Features
- Database connectivity via native drivers and generic JDBC, with dynamic port detection and a multi‑driver architecture.
- Real‑time policy enforcement, S‑GATE blocking, and immediate alerting on security incidents.
- Built‑in compliance reports for PCI‑DSS, GDPR, HIPAA, SOX, and flexible audit trails.
- Deployment flexibility across physical, virtual, and cloud environments, including Kubernetes and containers.

## Core Workflows
1. **Setup & Deployment** – Perform datasource discovery, deploy S‑TAP/S‑GATE agents, and configure them through the Guardium Installation Manager (GIM).
2. **Monitoring & Alerts** – Collect traffic continuously, evaluate policies, and generate incidents.
3. **Response & Remediation** – Automatically block malicious queries, rotate credentials, and investigate incidents.
4. **Compliance Management** – Collect audit data, generate regulatory reports, and prepare for audits.

## Personas
- **Guardium Administrators** – Configure the platform, manage users, and oversee central management.
- **Security Analysts** – Investigate alerts, run vulnerability scans, and fine‑tune policies.
- **Database Administrators** – Register databases, deploy agents, and maintain data‑source health.
- **Compliance Officers** – Generate regulatory reports, track audit readiness, and verify policy adherence.

## Entities
- **Agents** – S‑TAP (kernel‑based), A‑TAP (user‑space), K‑TAP (alternative kernel mode), Collectors, and Aggregators.
- **Policies & Rules** – Guardium policies, audit policies, FGAC rules, and access rules.
- **Infrastructure** – GIM, Managed Units, and S‑GATE modules.

```markdown
## Quality Gates

**Policy Constructs**: Security Policy, Audit Policy, Classification Rules, Access Rules, FGAC.  
**Infrastructure**: Managed Units, Guardium Infrastructure Manager (GIM), S‑GATE Blocking Engine, Universal Connectors.

## Guardium Model & Version Management
Guardium stores hardware (model) and software (version) metadata in system attributes. Additional attributes include Import Selected Manager IP and Purge at Age.

## Oracle Session Time Zone Handling
Oracle stores session timestamps in UTC with the client's original time‑zone offset, so two sessions that appear to start at the same local time may actually be hours apart.

## CAS API Access Restrictions
Only users with the **admin** role or the **CAS** role may invoke GuardAPIs or REST APIs for managing CAS hosts, templates, and template sets.

## Guardium License Monitoring
The **Licenses Remaining** metric shows unused Guardium licenses available for activating S‑TAP agents or other components.

## Invalid vs. Inactive S‑TAPs
Invalid S‑TAPs fail health checks (e.g., missing binary, wrong version) and appear in deployment health dashboards. The `remove_invalid_stap` command cleans them up.

## K‑TAP Configuration Parameters
- **KTAP_LIVE_UPDATE** (default **Y**) enables live kernel driver updates without reboot.  
- **GIM_ALLOW_CUSTOM_BUNDLES=0** prevents non‑standard K‑TAP bundles, enforcing strict version control.

## K‑TAP Checkpoint & Failover Settings
Checkpoint attributes: Client Checkpoint File, Checkpoint Period.  
Failover attribute: Failover File. These ensure continuous traffic capture during disruptions.

## Kas Configured Ingress Annotations
Use Kubernetes annotations (e.g., `kubernetes.io/ingress.class`, `nginx.ingress.kubernetes.io/rewrite-target`) to configure Kas ingress behavior.

## Guardium System Time Zone CLI
`store time_zone <value>` sets the system clock to a new time zone, restarting services and temporarily disabling monitoring.

## Language Configuration Workflow
`store language <locale>` switches the Guardium UI language, restarting services briefly.

## Guardium System Clock Adjustment
`store time_zone` also adjusts the system clock, essential after moving an appliance to a new geographic location.

## Date‑Time, Exe, Term, Host, AUID, Event Fields
Guardium logs contain: Date Time (UTC with offset), Exe (command/query), Term (termination reason), Host (origin IP/hostname), AUID (audit user ID), Event (Guardium event type).

## REST API for System Backup (v11.4+)
`POST /api/system/backups` schedules or triggers backups, specifying scopes (metadata, config, audit) and storage location.
```

## Edge External Registry Deletion
The `delete_edge_external_registry` API removes external registry entries linked to Guardium Edge components, cleaning outdated data to maintain Edge‑to‑Central Manager communication integrity.  

## Features Overview
IBM Guardium Data Protection monitors, protects, and reports on database activity across on‑premises and cloud data stores, enforcing security policies, assessing vulnerabilities, and generating compliance reports.

## GuardAPI Function: get_ip_restriction_config
`get_ip_restriction_config` returns the system's IP restriction settings. The mandatory parameter `api_target_host` defines where the API runs:
- `all_managed` – all managed units (no central manager)
- `all` – all managed units plus central manager
- `<group name>` – all units in a specific group
- `<host name>` – a single central manager, managed unit or standalone unit

## GuardAPI Function: delete_edge_external_registry
`delete_edge_external_registry` (REST DELETE) cleans F5 data from Guardium, requiring `bigIP` and `appsIP` to identify target F5 devices.  

## NetApp Data ONTAP 7-Mode Share Enumeration
File System Scans need the data source account to have read (and possibly modify) permissions on NetApp Data ONTAP 7-Mode shares, enabling Guardium to discover and catalog file system resources.  

## Outliers and Symptom Timelines
Outliers—Activity anomalies spanning different threat categories within the same hour—trigger an Activity chart and incident timeline showing event chronology, aiding case investigation and response.  

## SQL Report Structure
Guardium SQL reports display each statement as a vertical list field‑by‑field; each field must occupy its own line, dictating report layout for multi‑line statements.  

## User Hierarchy Management
`create_user_hierarchy` builds role‑based permission structures. Example:  
```text
create_user_hierarchy userName=ADAMS parentUserName=SCOTT
```  
assigns user **ADAMS** under **SCOTT** in the hierarchy.

## Guardium Database Connection Guidelines

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

---

## Real-Time Database Activity Monitoring

IBM Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

---

## TLS 1.2 Encryption Enforcement

IBM Guardium enforces encrypted connections using TLS 1.2 for all network traffic, including database traffic monitored by S-TAP and communication between Guardium components. Administrators can check TLS configuration status and apply necessary updates to ensure compliance.

---

## IBM Guardium Feature Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

---

## Guardium Personas and Their Roles

- **Security Admin:** Policy definition, enforcement tuning, incident response
- **DB Admin:** Install/configure S-TAP, datasources, agent lifecycle
- **Compliance Officer:** Run reports, maintain audit evidence
- **Auditor:** Review policies, perform audits, validate controls
- **Analyst:** Query activity data, investigate incidents, produce insights

---

## Guardium Entity and Deployment Overview

- **Guardium System:** Central Manager, Managed Units, Aggregators
- **Plugins:** Universal Connectors, Cloud Access Security Broker
- **Security Objects:** Policies, Rules, Actions, Groups, Users/Roles
- **Data Objects:** Databases, Tables/Fields, Objects, Resources
- **Network Entities:** Firewalls, Load balancers, Ingress controllers
- **Authentication:** LDAP, Kerberos, Vault AppRole, API keys

**Deployment Workflow:** Install S-TAP → Configure datasources → Define policies → Monitor activity, run vulnerability assessments, generate compliance reports

## Guardium Error Resolution

### Windows Start Error 1192
When Guardium S-TAP fails on Windows with error "The application was unable to start correctly (0x000007b)":
- Check Application Event Log for faulting application "guardium_stapr.exe"
- Verify required Microsoft Visual C++ runtime DLLs in %WINDIR%\system32
- Ensure correct S-TAP version for installed Guardium release
- Confirm firewall rules allow S-TAP-port communication

**Key Concepts:** S-TAP, Windows, DLL, Event Log, Error Resolution

## Universal Connector Vault Integration

To secure Universal Connector credential storage:
- Configure HashiCorp Vault AppRole authentication
- Reference role ID and secret ID in Connector configuration
- Dynamic credential retrieval at runtime

**Key Concepts:** Universal Connector, Vault, AppRole, Credential Management, Security

## S-TAP Firewall Configuration

Deploying S-TAP agents behind firewalls requires:
- Opening port 16016 (TCP) for heartbeat and data
- Opening port 16017 (TCP) for blocking commands
- Opening port 16018 (TCP) for GIM software distribution
- Opening port 16019 (TCP) for API access
- Verifying open ports and creating necessary firewall rules

**Key Concepts:** Firewall, Port Requirements, S-TAP Communication, Connectivity

## API and REST Interfaces

Guardium provides programmatic access via:
- RESTful API endpoints over HTTPS
- GuardAPI commands from command line
- Scripting integrations with other tools
- Building custom dashboards

**Key Concepts:** REST API, GuardAPI, HTTPS, Integration, Automation

## IBM Guardium Data Protection Overview

IBM Guardium provides comprehensive database activity monitoring, threat detection, and compliance reporting for on-premises and cloud data environments. Key features include:

- **Real-Time Monitoring**: Continuous capture of database traffic via S-TAP agents for immediate visibility.
- **Policy Enforcement**: Automated policy application to enforce security and compliance across structured and unstructured data stores.
- **Risk and Threat Detection**: Advanced analytics and machine learning to identify and respond to anomalies and threats.
- **Compliance Reporting**: Built-in reporting templates and tools to meet regulatory requirements efficiently.

### Deployment Scenarios
- **On-Premises**: Direct integration with existing infrastructure for deep visibility into database activity.
- **Cloud Environments**: Support for major cloud platforms to extend monitoring capabilities seamlessly.

### Management and Reporting
- Web-based console for centralized management, configuration, and reporting.
- Integration with third-party tools for extended analytics and workflow automation.

### Benefits
- **Enhanced Security**: Real-time threat detection and automated response mechanisms.
- **Operational Efficiency**: Streamlined compliance processes and reduced administrative overhead.
- **Scalability**: Designed to scale with organizational needs, supporting diverse data environments.

**Note**: For detailed usage instructions, refer to specific Guardium documentation modules covering installation, configuration, and advanced features.

## IBM Guardium Data Protection Overview

IBM Security Guardium Data Protection offers a unified platform for securing enterprise databases and big data environments through continuous monitoring, threat detection, and compliance automation.

### Key Features
- **Real-time Activity Monitoring:** S-TAP agents capture database transactions continuously.
- **Policy-Driven Security:** FGAC policies enforce access control, encryption, and data masking.
- **Compliance Automation:** Pre-built audit templates for PCI-DSS, GDPR, HIPAA, SOX.
- **Threat Protection:** S-GATE blocking, anomaly detection, SIEM integration.
- **Scalable Architecture:** Agents (S-TAP, A-TAP, K-TAP), collectors, aggregators, central managers.

### Core Workflows
- **Deployment & Discovery:** Inventory data sources, deploy agents, run classification.
- **Policy Configuration:** Define security, audit, classification, and access controls.
- **Monitoring & Reporting:** Review traffic, generate audit reports, investigate incidents.
- **Incident Response:** Block suspicious activity, generate alerts, remediate vulnerabilities.

### User Personas
- **Security Administrators:** Manage policies, oversee compliance, handle incidents.
- **Database Administrators:** Install agents, configure data sources, manage encryption keys.
- **Compliance Officers:** Access audit trails, generate regulatory reports.
- **Data Scientists/Auditors:** Query sanitized data, use dashboards for trend analysis.

### Main Entities
- **Agents:** S-TAP (kernel-level), A-TAP (user-space), K-TAP (alternative kernel module).
- **Policy Types:** FGAC, Audit, Classification, Access Rules.
- **Infrastructure Components:** Collectors, Aggregators, Central Manager.

## External S-TAP TLS Mutual Authentication
Configure an External S-TAP proxy to enforce TLS mutual authentication with the database server. The proxy validates the database's certificate using its CA and can require client certificates, ensuring end-to-end encrypted connections independent of source and target versions.

## IBM Guardium Overview
IBM Guardium safeguards databases through real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across on-prem and cloud data stores.

### Features
- Continuous activity tracking via S-TAP agents
- Configurable security policies for alerting and blocking
- Built-in compliance templates for PCI-DSS, GDPR, HIPAA, etc.
- Automated sensitive data discovery with InfoSphere integration
- Flexible deployment across JDBC driver families and dynamic ports

### Workflows
- Deploy agents, define datasources, create policies, and set up classification
- Monitor activity, view violations, and generate compliance reports
- Respond with S-GATE blocking, credential rotation, and incident management
- Maintain rules, evaluate policy effectiveness, and manage entities

### Personas
- **Security Administrator:** Manages policies and ensures compliance
- **Database Administrator:** Configures datasources and monitors S-TAP
- **Compliance Officer:** Coordinates regulatory requirements and reporting
- **Data Analyst:** Leverages data discovery for risk management

### Entities
- **Agents:** S-TAP, A-TAP, K-TAP for data capture
- **Reports:** Timestamps, Group Members, Counters
- **Policies:** Security, Audit, Classification, Access rules
- **Infrastructure:** Managed Units, S-GATE, Universal Connectors, Central Manager

## Managing Security Policy Installations in Edge Clusters
Guardium administrators can monitor security policy installations across edge clusters. The interface displays installation status for policies like ‘IBM Security Guardium Standard Activation’ per cluster. Links provide guidelines for creating and deploying these policies, enhancing oversight in distributed environments.

## Configuring Data Streams in Guardium
Security professionals and administrators configure data streams within IBM Security Guardium to direct monitored activity data to specified destinations. Although Guardium stores data internally by default, configurations allow streaming to other systems. Through the Guardium interface, administrators define these configurations, specifying data types and destinations to align with organizational policies and requirements.

## Reverting Keystore to Last Saved or Default State

### Reverting to Last Saved State
```bash
grdapi revert_keystore_to_last_saved
```

### Reverting to Default State
```bash
grdapi revert_keystore_to_default
```

## Inspection Engine Verification After Database Upgrade
Verify that the Guardium inspection engine paths remain correct after upgrading a database to ensure traffic capture continues uninterrupted. Update the installation path in Guardium if necessary.

## Kerberos Plugin Configuration File Structure
A valid Kerberos configuration file includes comment lines (ignored by the parser) and plugin entries. Required plugin values:
- `plugin_name`
- `realm`
- `keytab`
- `principal`

## Teradata Exit Setup
Teradata Exit enables communication between the Teradata database and S-TAP through a shared library, allowing monitoring without K-TAP if only Teradata is being monitored.

## Multi-threading in S-TAP and K-TAP
S-TAP and K-TAP utilize multi-threading to efficiently handle high data volumes by creating extra threads and buffers, increasing data collection speed, balancing traffic across threads, and storing packets for a single session in one buffer.

## VirtualCenter Server Overview
The VirtualCenter Server serves as a central management point for ESX Server hosts in a VMware infrastructure, allowing single control point management, optional SQL database usage for configuration data, and flexibility with documented hardware configurations.

## IBM Guardium Overview

IBM Guardium secures enterprise databases through comprehensive monitoring, vulnerability assessment, and policy enforcement. Core features include:

- **Database Activity Monitoring:** Real-time auditing of data access and usage.
- **Vulnerability Assessment:** Automated discovery of database weaknesses.
- **Policy Management:** Enforcement of security policies to protect sensitive data.
- **Threat Analytics:** Machine learning-based detection of suspicious activities.

### Installation and Monitoring
Deploy Guardium by installing agents and collectors, then configure data sources. Continuous real-time monitoring ensures prompt detection of anomalies, while periodic vulnerability scans keep systems secure.

## Guardium Features and Operations

### Features Overview
- **Datasource Connectivity:** Supports dynamic port detection and multi-driver configurations; integrates with CyberArk credential vault.
- **Threat Detection:** Provides real-time policy monitoring and automated alerts for suspicious activities.

```markdown
### Verify an API Key Exists
The `c8ec6965-8d25-4a28-b730-fbc9304a00b8` command sequence checks if an API key is valid by making a request to Guardium's API with authentication headers. It parses the JSON response and confirms the HTTP status code is 200 to verify the key exists. This process automates API key validation in workflows for security and access control.

### Number Sign Function
Parameters `hashicorpChildNamespaceString` and `hashicorpPath` define the location of datasource credentials in HashiCorp Vault. Discover valid values via `create_datasource --help=true`. `hashicorpPath` specifies a custom credential location.

### API Target Host Parameter
The `api_target_host` parameter in GuardAPI specifies target hosts using hostnames or IP addresses. Commands executed on a managed unit go to the central manager. Use `api_target_host=10.0.1.123` as an example. The parameter respects network IP mode, offering flexibility across deployments.

### Group Type Description Filtering
The `groupTypeDescLikeString` parameter filters group aliases by description. For instance, `%1` retrieves all aliases ending with '1' in objects like client or server IPs, aiding targeted group searches.

### Aliases in Report Views
Enabling aliases in report views improves column readability with user-friendly names instead of raw identifiers. This feature enhances user experience in security or compliance monitoring by presenting interpretable formats alongside raw data.

### Cancel Module Installation
The `PUT` API endpoint cancels pending installations of Guardium modules or bundles prior to processing. Introduced in 9.5, this endpoint follows REST syntax and is used in enterprise module management workflows to manage installations efficiently.

### Protect Data with Two-Step Validation
Introduced in V12.2, the `delete_data_params` API includes two parameters:
- `fips_go`: Automates service restarts when FIPS mode changes.
- `compatibility_check`: Ensures Guardium version compatibility across managed units.

This API is essential for maintaining security and stability during FIPS mode transitions.

### Number Sign Usage
The `api_target_host` parameter in GuardAPI allows specifying target hosts via IP or hostname, directing operations across network configurations effectively.

### External S-TAP IP Filtering Configuration
The Guardium CLI and configuration files enable filtering traffic from specific IP addresses to a MongoDB S-TAP, enhancing security by restricting access based on IP address.
```

## B container through an External S-TAP interface

Key commands and configurations:
- `iptables -I INPUT -p tcp -m tcp -s 172.17.0.3 -d 172.17.0.4 --dport 5432 -j ACCEPT`
- `iptables -I INPUT -p tcp -m tcp -s 172.17.0.4 -d 172.17.0.4 --dport 5432 -j ACCEPT`
- Ensure the IP addresses match the MongoDB container's IP for proper filtering

## Guardium Incident Resolution – MongoDB Example

Starting the S-TAP agent services on a Guardium appliance is required to begin monitoring databases such as MongoDB. CLI commands manage the S-TAP processes.

To start S-TAP:
```
/etc/rc.d/init.d/guard_stap start
```
Expected output on success:
```
Starting IBM Guardium S-TAP...                                         [  OK  ]
```

This step-by-step process enables administrators to programmatically control Guardium's activity monitoring for MongoDB and other databases, ensuring real-time security insights.

## Assessment Creation Constraints

When creating assessments through the Guardium API, each assessment must have a unique description to prevent conflicts and errors. The API rejects entries with duplicate descriptions.

Important considerations:
- The `assessmentDescription` parameter must be distinct for each assessment entry
- Attempting to create an assessment with a non-unique description results in an error
- Administrators should enforce unique descriptive text to avoid processing issues

## S-TAP Service Management

Proper initiation of the IBM Guardium S-TAP service ensures that database monitoring is active. The S-TAP agent must be running on all hosts where database activity needs to be observed.

Key CLI command and expected result:
```
/etc/rc.d/init.d/guard_stap start
Starting IBM Guardium S-TAP...                                         [  OK  ]
```
This command initializes the monitoring process, allowing Guardium to capture real-time database activity and security events.

## Audit Rule Join Example

The query filters Oracle audit records, joins them with system information and database definitions, and groups by command to count occurrences.

Key components of the query:
- Filters for `DB_USER`, `['ORACLE']`, and `MODULE` starting with `'TOOL%'`
- Joins across `RESULTSET`, `SYSINFO`, and `DB_DEFINITIONS`
- Groups by `COMMAND` with a count alias `volume`

## Certificate Validation and Policy Enforcement

Before processing data, Guardium can be configured to validate client web certificates to ensure secure connections. Additionally, policies can be set to disconnect sessions if certificates become invalid.

Key points:
- `client_web_cert_validation` must be set to `true` for validation
- `Disconnect if Cert Revoked` policy allows termination of sessions if a certificate is revoked, enhancing security measures

## API Target Host Specification

When calling Guardium APIs, the `api_target_host` parameter specifies which managed unit or Central Manager should execute the command. This ensures commands are directed to the correct appliance within the Guardium ecosystem.

Usage example:
```
api_target_host=192.168.1.100
```
Special considerations:
- In systems with dual IP addressing, the target host must match the registration protocol of the Central Manager for proper routing.

## Document Overview

### IBM Guardium Data Protection
IBM Guardium Data Protection is the enterprise-grade solution for real-time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, supporting both on-premises and cloud environments.

#### Features Overview
- **Datasource Connectivity:** Supports multiple JDBC driver families, including native drivers for optimized performance and generic drivers for broad compatibility, with dynamic port detection via a browser service.
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking capabilities, and security incident generation from captured activity.
- **Compliance & Reporting:** Pre-built report templates for regulatory frameworks such as PCI‑DSS, GDPR, HIPAA, and SOX, along with automated audit trail generation.

#### Workflows Overview
- **Configuration:** Add datasources, deploy S-TAP agents through Guardium Installation Manager (GIM), and configure Fine-Grained Access Control (FGAC) policies.
- **Navigation:** Review activity/search results, run vulnerability assessments via the VAM wizard, and use the audit dashboard for operational visibility.
- **Action:** Initiate S-GATE blocks on unauthorized queries, rotate credentials, and respond to generated security incidents.

#### Personas Overview
- **Administration:** System Administrator (platform configuration, user lifecycle), Security Administrator (FGAC policy authoring, policy enforcement).
- **Data & Database Management:** Database Administrator (datasource registration, S-TAP deployment), Data Analyst (dashboard consumption, ad-hoc queries).
- **Compliance & Audit:** Compliance Officer (regulatory reporting, audit readiness), Security Analyst (threat investigation, incident response).

#### Entities Overview
- **Agents & Collectors:** S-TAP (database activity capture), A-TAP/K-TAP (kernel-level monitoring), Collectors/Aggregators/CM (data aggregation).
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Group-Based FGAC.
- **Infrastructure:** GIM (deployment & patching), Managed Units (data collection units), S-GATE (blocking enforcement), Universal Connector (link to external ticketing systems).

```markdown
## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Concepts
- Database activity monitoring
- Policy enforcement
- Vulnerability assessment
- Compliance reporting

---

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. Dynamic port detection resolves instance names to current ports.

**Key Concepts:**
- JDBC driver families
- Native drivers
- Generic drivers
- Dynamic port detection

---

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents. Real-time policy evaluation triggers alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

**Key Concepts:**
- S-TAP agents
- Real-time policy evaluation
- S-GATE blocking
- Alert generation
- Policy targeting

---

## Plugin Configuration Values

Certain Guardium plugin values must be set correctly for proper operation, including `db_base`, `db_bits`, `db_tcp_intercepted_ports`, and encrypted session support.

**Key Concepts:**
- `db_base` path configuration
- `db_bits` architecture specification
- `db_tcp_intercepted_ports` definition
- Encrypted session support

---

## FAM Activity and Di Metrics

Key metrics for monitoring File Access Monitor (FAM) activities include `Di Rate`, `Di Queue Length`, `Di Total`, `Total Buffer Init`, `Bytes Dropped`, `Bytes Ignored`, and `Bytes Captured`.

**Key Concepts:**
- `Di Rate`
- `Di Queue Length`
- `Di Total`
- K-TAP collector metrics

---

## Central Manager Sync Workflow

Synchronizing user status between the Central Manager and managed units is achieved through executing a Portal user sync command, ensuring consistent user access control policies across the Guardium environment.

**Key Concepts:**
- Portal user sync command
- Consistent user access control
- Distributed deployment synchronization

---

## Guardium SQL Parsing Attributes

Guardium's SQL parsing extracts components from database queries, including `Parent`, `SQL Verb`, `Object`, and `Object/Command` attributes for detailed audit reports and policy rules based on granular SQL activity.

**Key Concepts:**
- SQL parsing components
- `Parent` identification
- `SQL Verb` classification
- `Object` specification
- `Object/Command` attributes

---

## Guardium API Target Host Parameter

The `api_target_host` parameter in Guardium's API framework defines API execution targets, including all managed units, the central manager, specific groups, or individual hosts.

**Key Concepts:**
- `api_target_host` parameter
- Execution targets
- Managed units
- Central manager
- Group targeting

---

## DELETE Member from Group API Syntax

Guardium's API supports removing members from group associations using the DELETE method on the `delete_member_from_group` endpoint, requiring a `member` parameter and allowing `api_target_host` to target all managed units, the central manager, a specific group, or an individual host.

**Key Concepts:**
- DELETE method
- `delete_member_from_group` endpoint
- `member` parameter
- Targeting options
```

## Guardium Overview

IBM Guardium is a unified data security platform that monitors and protects structured and unstructured data across on-premises, cloud, and hybrid environments.

### Features
- **Data Activity Monitoring**
- **Policy & Configuration Management**
- **Identity & Access Controls**
- **Encryption & Tokenization**
- **Compliance Support**
- **Automation & Orchestration**

### Workflows
- **Deployment & Provisioning**
- **Policy Management**
- **Monitoring & Reporting**
- **Orchestration**

### Personas
- **Security Administrator**
- **Database Security Analyst**
- **Compliance Officer**
- **Application Owner**

### Managed Unit Overview
A managed unit is a standalone Guardium appliance that can collect, monitor, and manage datasources, featuring collector, aggregator, and central manager roles.

### Collector Functionality
The collector analyzes session and audit data, applies policies, and stores results in the Guardium repository.

### Aggregator Capabilities
Aggregators centralize collector data, perform correlation analysis, and store aggregated results in a centralized database.

### Central Manager Role
The central manager oversees the fleet of Guardium appliances, provides single authentication, and aggregates data for enterprise-wide reporting.

### Datasource Definition
A datasource encompasses any database, data warehouse, file system, or SaaS service monitored and protected by Guardium, including configuration of instance, schema, and tables.

### Security Policy Elements
Security policies define rules for data access, specifying who can do what to which data in a given context, enabling blocking, alerting, and data masking.

### Audit Policy Details
Audit policies add context information to activity data, store it in the repository, and enable drill-down investigation.

## GuardCTL Command

The `guardctl` command-line utility activates or deactivates a DB2 instance within the Guardium environment. Specify `-db_instance db2inst1` to control the `db2inst1` instance, integrating Guardium with database services.

**Key Concepts:** GuardCTL, DB2, Instance Management, Command-Line Utility, Activation, Deactivation

## GDP Server Configuration

Configure the GDP server hostname with a valid DNS name for SSL certificates. Ensure hostname consistency and verify certificates using OpenSSL tools.

**Key Concepts:** GDP Server Hostname Configuration, SSL Certificate, OpenSSL

## I-TAP Configuration Retrieval

Retrieve I-TAP configuration settings via REST API. The mandatory `datasourceName` parameter returns configuration details for managing I-TAP agents.

**Key Concepts:** REST API, get_istap_config, datasourceName, Configuration Retrieval

## iptables Configuration

Manage iptables rules to control network traffic in a Couchbase environment. Accept connections on the local loopback interface for the Couchbase process and reject on other reserved loopback ports.

**Key Concepts:** iptables, Chain Management, Network Traffic Control, Port Management

## Kerberos Authentication Setup

Configure Kerberos authentication across database systems using the `setup_kerberos.sh` script. Specify `db_instance=db2inst1` for the target DB2 instance.

**Key Concepts:** Kerberos, Authentication, Database, setup_kerberos.sh

## GDP Server Hostname Verification

Configure the GDP server hostname to match the SSL certificate's CN. Use OpenSSL commands to verify hostname matches the certificate's CN, preventing security risks.

**Key Concepts:** GDP Server Hostname, SSL Certificate, CN, OpenSSL

## Backup Central Manager Identification

Use the `backup_cm_list_candidates` command in Guardium to identify potential backup central managers from registered units, aiding in high availability and failover management.

**Key Concepts:** Backup Central Manager, High Availability, Failover

## Guardium Agent Configuration Workflow

Configure IBM Guardium Data Protection by installing and activating S-TAP agents on database host machines. Use `guardctl` to manage A-TAP installations, requiring database instance credentials.

## Overview

IBM Guardium Data Protection is a comprehensive database activity monitoring and vulnerability assessment platform. It secures sensitive data in on-premises and cloud environments across a wide range of database technologies, providing real-time monitoring, automated policy enforcement, and detailed compliance reporting.

### Key Features
- **Real-Time Monitoring:** Continuous tracking of database transactions and user activities.
- **Policy Enforcement:** Automated rule-based control over data access and operations.
- **Vulnerability Assessment:** Built-in tests for configuration weaknesses and missing patches.
- **Compliance Reporting:** Templates for PCI-DSS, HIPAA, GDPR, and more.
- **Sensitive Data Discovery:** Automatic identification of sensitive data across all monitored systems.

### Primary Workflows
- **Deployment:** Installation of Guardium components including Central Manager and S-TAP agents using GIM.
- **Policy Management:** Creation, editing, and deployment of security and audit policies.
- **Post-Deployment Validation:** Verifying agent connectivity and proper functioning.
- **Core Operations:** Ongoing monitoring, alerting, reporting, and response to incidents.

## IBM Guardium Data Protection Overview
Centralized compliance monitoring and database security solution.
Real-time activity monitoring, threat detection, automated reporting.
Key Personas: Security Administrators, Data Analysts, Compliance Officers.
Entities: Databases, Agents (S-TAP, A-TAP, K-TAP), Audit Policies.

## API Endpoint for Testing Connectivity
Verify appliance reachability with REST API connectivity endpoint.

## Listing Data Source References by Name
Use `list_datasource_groupRef_by_name` GuardAPI with `application` and `objName` string parameters.

## Store SQL Credentials
Securely store credentials using `store_sql_credentials` GuardAPI, specifying `password` and `stapHost`.

## Calling Guardium REST API with curl
Interact with REST APIs using `curl` to test connectivity, authorize requests, and process JSON responses.

## Show Logstash Plugins API
Retrieve configured Logstash plugins via `showLogstashPlugins` endpoint at `https://<appliance>:8443/restAPI/showLogstashPlugins`.

## Managing Custom Data via REST API
Post custom data to Guardium with REST POST, specifying URL and `tableName`.

## Flat Log Process API
Process flat logs via REST POST, introduced in version 11.3, for efficient log data handling.

## REST API for Query Running
Execute queries using GET method with `START` and `COUNT` parameters, requiring Authorization token.

## Guardium REST API Syntax and Workflows
Follow modern web standards using GET method for data retrieval, essential for security analytics.

## Required API Parameters for Database Connection
Connecting to an Oracle Autonomous Database requires the following essential parameters via the API:
- **Wallet Configuration File Path:** Full path to the database wallet file
- **User Credentials:** Username and password or token for database authentication
- **Additional Password Requirements:** May include secret keys or vault references as required by the security policy

These parameters ensure secure and authenticated connections to managed databases through IBM Guardium.

## Query Rewrite Optimization APIs
Guardium provides specialized APIs for optimizing and customizing database query workflows. These APIs enable users to automatically rewrite complex queries, automate test case scenarios for performance tuning, and overcome limitations of the user interface by scripting advanced query modifications. These features are crucial for database administrators and developers aiming to enhance query performance and security.

## Oracle Autonomous Database Connection Parameters
To establish a connection to an Oracle Autonomous Database, the following parameters are typically required:
- **Database Wallet File:** Contains encryption keys and certificates for secure connections
- **User Name:** Database user credential for authentication
- **Password:** Secure password associated with the user account

These parameters ensure encrypted and authenticated access to Oracle's autonomous cloud databases using Guardium APIs.

## Documentation Overview
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features Overview
- **Vulnerability Scanning:** Automated scanning for database weaknesses
- **Audit Reporting:** Customizable audit and data mapping APIs
- **Access Control:** Populating members for groups via API
- **Command Management:** Remove query rewrite actions
- **Custom Integration:** API endpoints for data handling and F5 load balancer
- **Monitoring:** Executed DMLs on sensitive objects chart
- **User Management:** Reset utilization data, list database user mappings, list parameter mappings for functions

### Workflows Overview
- **Security Management:** Vulnerability scanning, audit reporting
- **Access Management:** Populate group members, manage command actions
- **Development Integration:** Use APIs for custom integrations
- **System Maintenance:** Reset utilization data, list mappings

### Personas Overview
- **Security Professionals:** Vulnerability assessments, risk management
- **Database Administrators:** Security management, user management
- **Developers:** Integrate custom applications via APIs
- **Compliance Officers:** Generate audit reports
- **Network Engineers:** Configure F5 load balancers

### Entities Overview
- **API Endpoints:** Various endpoints for custom data handling, table distribution, discovered instances
- **Commands:** remove_qr_action, list_db_user_mapping, reset_unit_utilization_data, list_param_mapping_for_function
- **Charts:** Executed DMLs on sensitive objects
- **Infrastructure:** Guardium system components
- **Network Devices:** F5 load balancer

configuration file includes valid paths for `guardium_home` and `java_home`.  
3. Confirm that the required ports (default 8080 for the web UI and 8443 for HTTPS) are not already in use.  
4. Review the `gsm.log` file in `guardium_home/logs` for specific error messages.  
5. Validate that the system meets the minimum memory and disk space requirements (minimum 4 GB RAM and 20 GB free disk).  
6. Restart the host machine if recent changes were made to system services or firewall rules.

## Compressed Guardium Reference

### Guard Installation Verification
The `guardfmt.jar` library resides in `$GUARD_HOME/lib`. Check the `$GUARD_HOME/log/guardfmt.log` file for CLASSPATH errors and ensure `GUARD_HOME` points to the correct installation path. If needed, run `guardadm test connect` to verify connectivity to the Guardium aggregation server.

### Key Concepts
Guard Sender Monitor, JVM, Java Runtime, Classpath, Log Files

## Removing Ranger Services

Guardium provides two methods to remove Ranger services:
1. **CLI Command**  
   `remove_ranger_config --host <host_name> --username <user_name>`
2. **REST API**  
   `DELETE /stap/rangerService?service_name=<service_name>&host_name=<host_name>`

Both require administrative authority in Ambari.

## REST API Deleting Ranger Service

To remove a Ranger service via Guardium's REST API, use the `DELETE /stap/rangerService` endpoint with:
- `service_name=<service_name>`
- `host_name=<host_name>`

Requires Ambari admin permissions.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures structured and unstructured data on-premises and in the cloud. It captures database activity in real-time, enforces policies, detects vulnerabilities, automates compliance checks, and manages encryption.

### Core Features
- Real-time activity monitoring via S-TAP agents
- Policy enforcement, blocking, and alerting
- Vulnerability assessment scanning
- Compliance reporting templates
- Centralized encryption management

### Main Workflows
- **Configuration:** Deploy agents, configure datasources, define policies
- **Monitoring:** Review activity, investigate incidents
- **Response:** Block threats, rotate credentials
- **Automation:** Integrate with SOAR platforms via REST APIs

### Primary Personas
- Security Administrators: Define policies, manage incidents
- Database Administrators: Deploy agents, maintain datasources
- Compliance Officers: Generate audit reports, ensure regulatory adherence
- Security Analysts: Investigate threats, correlate data

### Key Entities
- Agents & Collectors: S-TAP, A-TAP, K-TAP
- Policies & Rules: Security, Audit, Classification
- Infrastructure: Central Manager, Managed Units, Audit Repositories

## REST API Target Host Parameter

The `api_target_host` parameter in Guardium REST API calls specifies where the API executes. It accepts:
- Specific IP or hostname
- `all_managed`: All managed units except Central Manager
- `all`: All managed units including Central Manager
- `group:<group_name>`: Hosts in a specified managed group

The value must match the Guardium network's IP mode (IPv4/IPv6).

## Retrieve Policy Rule Details via REST

Guardium provides a REST API endpoint to retrieve details for rules in a policy:
```
GET /api/policy_rule?policies=<policy_name>
```
Returns for each rule:
- Rule type, objects, and conditions
- Creation and modification timestamps
- Owner and modification history

Minimum required version: 11.3

e Central Manager must consistently match the hostname or IP address used for the `api_target_host` parameter in API calls. If the unit was registered using its IP address, subsequent API calls must use the same IP address; mixing IPs and hostnames will cause authentication failures. This ensures proper communication and authorization between managed units and the Central Manager.

## Monitor Cross-CM Health View Hostname

Defines the Central Manager hostname for cross-cluster health reporting in IBM Guardium.

## Example API Response Fields

Includes DB2 IDs, timestamps, IPs, and shard details for database activity monitoring.

## IBM Guardium Data Protection

Enterprise platform for real-time database monitoring, threat detection, and compliance reporting.

### Features
- Supports native and generic drivers for DB2, Oracle, SQL Server, etc.
- Real-time policy enforcement, automated alerting, and audit trails
- Built-in compliance templates for PCI-DSS, GDPR, HIPAA, SOX

### Workflows
- Activate S-TAP agents, define security policies, manage groups via CLI/GUI
- Continuous traffic inspection, incident generation, automated blocking
- Real-time query blocking, credential rotation, forensic analysis

### Personas
- Guardium Administrator: platform configuration, user provisioning
- Security Administrator: policy management
- Database Administrator: datasource configuration, agent deployment
- Data Analyst: dashboards, custom reports
- Compliance Officer: regulatory reporting
- Auditor: control validation, evidence extraction

### Components
- S-TAP, K-TAP, A-TAP agents for traffic capture
- Collectors, aggregators, Central Manager roles
- Security, Audit, Access, Classification policies and rules
- Managed units, Guardscope appliances, Universal Connector for cloud sources

## 1573. HashiCorp Vault Configuration
Specify the vault port number to ensure secure communication with HashiCorp Vault. This parameter configures the specific port used for integrating Guardium with Vault for secret management.

## 1574. API Target Host Parameter
The `api_target_host` parameter designates execution targets for API requests within Guardium. It accepts values like `all_managed`, `central_manager`, or specific host names/IP addresses, enabling precise control over where API calls are directed.

## 1575. Db2 Admin Challenges and Compliance
Db2 administrators must balance stringent compliance monitoring with maintaining database performance. Key responsibilities include ensuring compliance with regulations and effectively overseeing privileged activities to prevent data breaches.

## 1576. User Information API Endpoint
The `grdapi list_users` command retrieves detailed user information, including username, first name, last name, email, and account status. This functionality supports system administration and security management by facilitating efficient handling of user data in Guardium.

## 1577. Offline Help Configuration Workflow
Set the offline help hostname using `set offline_help_hostname = 'newHostname'` via GuardAPI. This workflow manages help documentation access efficiently, enhancing user support within the Guardium system.

## 1578. api_target_host Parameter Reiteration
The `api_target_host` parameter directs API execution to specified targets in Guardium, including the central manager or managed units. Correct configuration is essential for maintaining network compliance and security.

## 1579. Overview of api_target_host
The `api_target_host` parameter allows directing API calls to all managed units, the central manager, or a specific host in Guardium. This feature is crucial for directing security protocols and maintaining operational control over Guardium functionalities.

## 1480. Logging Configuration with set_ztap_logging_config
Use the `set_ztap_logging_config --param log_level=DEBUG` command to control logging parameters in Guardium. Accessible as a REST API from Guardium V9.5, this method enhances system monitoring and troubleshooting through detailed logging options.

## 1481. Database Retrieval API Endpoint
This API provides access to database details, essential for data management and security in Guardium. Administrators can retrieve database information to support auditing, reporting, and compliance tasks within the system.

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. The Guardium Browser Service resolves instance names to current ports dynamically.

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents and evaluates it against configured security policies. Guardium generates alerts, and S-GATE can block unauthorized activity if policies are violated. Policies target specific users, objects, operations, and time windows, with real-time streaming analysis and event correlation. 

## Secure Data Source Management

To add a secured datasource to Guardium Insights, use the GUI to obtain the HTTPS certificate. Use the REST API endpoint `/api/datasource/add`. Follow the S-TAP configuration guide for preparation steps prior to integration.

## Screen Catalog Maintenance

Use the `update_catalog_entries` command to update host paths in archive catalog entries. Two modes are supported:
1) Single-entry update using `file_name`.
2) Path-based update using `path` and `hostname`.

## Query Rewrite Condition Management

Use the `update_qr_condition` API to create Query Rewrite conditions. Register the service at `<base_url>/api/queries/queryrewriteconditions`.

## Filtered Database Access Control

Use the `filter_rdb` parameter to specify filtered relational databases for Guardium operations. Accept up to 10 case-sensitive, comma-separated database names.

## Managing Guardium Configuration and Security

### External Feed Mapping
The `list_ef_mapping` command lists user-created external feed mappings in Guardium. These mappings correlate external data with Guardium's internal structures for auditing and investigative purposes.

### IPv6 Unit Registration
When using IPv6, register Guardium units with the central manager using their hostname to ensure proper communication. Maintain consistent hostname usage across configurations.

### Query Rewrite Condition Management
Use the `remove_qr_condition` command (available in Guardium 10.1.4+) to delete outdated query rewrite conditions via the DELETE REST API method, maintaining current and accurate policies.

### Secure Guardium Communication
The `SharedSecret` parameter secures communication between the central manager and managed units. It is distinct from password rules and enhances security by ensuring only authorized units can communicate.

### Unified Discovery and Classification Updates
Version 1.1 of the Unified Discovery and Classification feature includes refinements in installation, new features, enhancements, and issue resolutions. Upgrade guidance ensures a smooth transition from version 1.0.

### MongoDB Database Integration
The `load_mongodb` command integrates MongoDB databases with Guardium, requiring `collectionName`, `database`, `host`, `password`, `port`, and `user` parameters. Available from Guardium version 9.5 and later.

### API Execution Host Specification
The `api_target_host` parameter directs API commands to either the central manager or specific managed units, specified by IP address or hostname, ensuring accurate command execution.

### Data Compliance Status
The `show_data_compliance_status` API, available from Guardium version 12.2, checks if data compliance features are enabled via a POST REST service request, critical for regulatory compliance enforcement.

### Data Source Custom Property Updates
Use the `update_datasource_custom_property` API (available from Guardium version 11.4) to modify custom properties of data sources through REST or GuardAPI, adapting data source configurations to evolving security needs.

## Enterprise Data Security with IBM Guardium

### Guardium Overview
IBM Guardium is a solution providing real-time visibility into database and file activity, controlling, analyzing, and protecting sensitive information through various features and compliance capabilities.

### Key Features
- **Datasource Management:** Centralized setup of various data sources with custom properties, IP sharing, and role management.
- **Security Policies & Rules:** Offers fine-grained access control, monitoring, and alerts for policy violations.
- **Compliance Reporting:** Provides pre-built and customizable reports for major compliance standards and audits.

### Workflow Highlights
- **Configuration:** Start by adding datasources for monitoring and management within Guardium.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection secures databases and files by monitoring activity, enforcing policies, assessing vulnerabilities, and simplifying compliance.

### Key Features
- Monitor database and file activity in real time; create alerts and incidents.
- Enforce security policies and block unauthorized SQL queries.
- Generate automated compliance reports (PCI-DSS, GDPR, HIPAA, SOX).
- Discover and classify sensitive data across on-premises and cloud stores.

### Workflows
- **Configuration:** Add datasources; deploy S-TAP, A-TAP, K-TAP agents; configure policies.
- **Navigation:** Review activity reports; run vulnerability scans; use audit dashboards.
- **Action:** Block queries; rotate credentials; respond to incidents.
- **Classification:** Continuously discover and reclassify data; use external services.

### Personas
- **Administration:** Platform setup; user and role management.
- **Database Management:** Datasource configuration; agent deployment; policy enforcement.
- **Compliance:** Generate and manage regulatory reports; oversee audits.
- **Data Stewardship:** Ensure data accuracy and integrity; manage data lifecycle.

## Compact IBM Guardium Reference

### Database Connectivity
- Supports JDBC drivers: native for performance, generic for compatibility
- Browser Service resolves instance names to ports dynamically

### Real-Time Monitoring & Enforcement
- S-TAP agents capture traffic
- S-GATE evaluates against policies
- Supports alerts, reports, query blocking

### Session Management APIs
- GuardAPI and REST API for session inference rules
- Available from version 11.0
- Uses PUT method for configuration

### Host Identification
- `api_target_host` specifies central manager IP/host
- Managed units execute tasks on CM
- Requires IP mode compatibility

### Component Configuration
- `main_analyzer_address` aligns with main analyzer
- No environment specification needed

### Managed Unit Execution
- Commands executed via central manager
- Managed unit hostname/IP required
- Conforms to IP mode configuration

### SSL Verification
- `--ssl_ca_cert_file` specifies CA cert for validation
- `-h` or `--help` displays installation options

### Data Protection Features
- Sensitive data discovery & classification
- Anomaly detection
- Policy enforcement across DB/file systems

### Document Overview
- Enterprise database activity monitoring platform
- Real-time monitoring, policy enforcement, compliance reporting
- Supports structured/unstructured data in cloud/on-premise

### Key Workflows
1. **Configuration:**
   - Add datasources
   - Deploy S-TAP agents
   - Configure FGAC policies
2. **Monitoring:**
   - Review activity reports
   - Run vulnerability assessments
   - Use audit dashboard
3. **Management:**
   - Reset VA summary data
   - Manage security policies
   - Rotate credentials
4. **Remediation:**
   - Block unauthorized queries
   - Audit violations
   - Incident response

### Personas
- **Security Analysts:** Threat Detection dashboards, investigations
- **Compliance Officers:** Generate reports, manage policies
- **DBAs:** Datasource configuration, agent deployment, inventory
- **Administrators:** Component installation/upgrades, target host config, API token management

### Entities
- **Agents:** S-TAP, A-TAP, K-TAP
- **Compute Nodes:** Collector, Aggregator, Central Manager
- **Policy Objects:** Security Policy, Audit Policy, FGAC rules
- **Infrastructure:** GIM, Managed Units, S-GATE, Universal Connector, Asset inventory

### Code to Column Mapping
- REST API: `getFieldsTitles`
- POST requests with query parameters
- Converts codes to human-readable column names

### Solr Query Usage
- Full-text search capabilities
- Wildcards, comparisons, grouping, wildcards, ranges
- Faceted search, highlighting, spelling suggestions

## VA Summary Data Reset API

Reset vulnerability assessment summary data via REST or GuardAPI, using parameters like datasourceName, hostName, and port.

**Key Concepts:** REST API, GuardAPI, Vulnerability Assessment Reset, Datasource Key

---

## API Execution Target Hosts

The `api_target_host` parameter defines where the API executes: managed units, central manager, or a host group.

**Valid formats:** IP address, hostname, `<group_name>`, `all_managed`, `all`

**Key Concepts:** API Execution, Target Hosts, Managed Units, Central Manager

---

## grdapi push_insights_trust

Use `grdapi push_insights_trust` to add the Guardium Insights certificate. Include the target host and the entire PEM-encoded certificate.

**Key Concepts:** grdapi, Certificate Management, PEM Format, Security

---

## REST API for Universal Connector Configuration

Base URL: `https://<guardium_host>:8443/api/connector/configuration`

### Parameters
- `enable_metrics`: `0` (false) or `1` (true), default `0`
- `api_target_host`: can be `all_managed`, `all`, or `<group_name>`

### Example
```
GET https://<guardium_host>:8443/api/connector/configuration?enable_metrics=1&api_target_host=all_managed
```

---

## Guardium Overview

Comprehensive database security platform with real-time threat detection, compliance reporting, file monitoring, and vulnerability assessment.

### Key Features
- Real-time monitoring
- Compliance templates
- File activity monitoring
- Integrated vulnerability assessment

### Workflows
- Policy management
- Incident response
- Automated reporting
- User behavior analytics

### Personas
- Security administrators
- Database administrators
- Compliance officers
- Data analysts

### Entities
- Managed units
- Central manager
- Security policies
- S-TAP agents

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection offers real-time database activity monitoring, policy enforcement, and compliance reporting for structured and unstructured data across on-premises and cloud environments. It supports multiple deployment models and integrates with identity and secret management systems.

### Key Capabilities
- Database monitoring via S-TAP agents, centralized analysis by collectors
- Policy management with FGAC, OA, and query classification
- Data classification with built-in and custom sensitivity categories
- Dynamic dashboards for compliance reporting (PCI-DSS, GDPR, HIPAA, SOX)

### Personas
- Security admin: policy configuration and incident response
- DB admin: agent installation and data source integration
- Compliance officer: regulatory report generation
- Analyst: forensic investigations and policy validation

## Policy Management Workflow

Guardium allows administrators to define, assign, and modify security policies that enforce access controls and compliance rules. The system provides a graphical interface and API access for creating policies that include actions, conditions, and evaluation criteria.

Key components:
- Policy editor with drag-and-drop rule creation
- Policy assignment to data sources or user groups
- Real-time policy evaluation against activities
- Version tracking with rollback capabilities

## Data Classification and Sensitivity

Guardium includes a built-in data classification engine that automatically tags sensitive information. The system supports predefined categories like Secrets (e.g., medical license numbers, national IDs) and allows custom classifications to meet organizational needs.

Features:
- Automatic sensitivity detection in data fields
- Sensitivity tagging (Public, Internal, Restricted)
- Custom classification rules based on conditions
- Compliance reporting based on classified data

## S-TAP Debug Levels and Logging

S-TAP provides debug levels 0-11 for troubleshooting. Levels 0-10 log detailed information to both the S-TAP log and db2_exit (db2diag.log), while level 11 logs only to db2_exit. Proper log configuration aids in diagnosing issues and ensuring system stability.

Key points:
- Range of debug levels from minimal (0) to maximum (11) verbosity
- Logs written to S-TAP log and db2_exit (db2diag.log)
- Higher levels essential for detailed issue resolution
- Configuration via Guardium UI or CLI commands

## Query Condition and Action Management API

The `unassign_qr_condition_from_action` API allows removal of specific query conditions from actions via a DELETE REST service. This capability supports dynamic policy management and customization of query rule enforcement.

API details:
- Endpoint: `DELETE /guardium/guardrails/api/v1/qr/unassign_condition_from_action`
- Available from Guardium 10.1.4 onwards
- Useful for refining policy enforcement and updating security postures

## Update Classifier Rule API

The `update_classifier_rule` API enables modification of existing classification rules through a PUT REST service. It supports calculating a confidence score for rule matches, enhancing data classification accuracy.

API details:
- Endpoint: `PUT /api/flat/log/records`
- Parameter `calculateConfidenceScore` computes match confidence
- Available in all supported Guardium releases
- Automates and refines data classification tasks programmatically

# Guardium Data Protection Overview

## Features
- Real-time monitoring, policy enforcement, and vulnerability assessment
- Compliance reporting for regulatory standards (e.g., PCI-DSS, GDPR, HIPAA, SOX)

## Workflows
- Add datasources, deploy S-TAP agents, and configure FGAC policies
- Review activity reports, run assessments, and use audit dashboards
- Block unauthorized queries, rotate credentials, and respond to incidents

## Personas
- Administration: Platform configuration and user management
- Security: Policy definition and incident investigation
- Database: Manage datasources and S-TAP deployment
- Compliance: Regulatory reporting and audit readiness

## Entities
- Agents/Collectors: S-TAP (local), A-TAP/K-TAP (network), Collector, Aggregator, Central Manager
- Policies/Controls: Security policies, audit policies, classification rules, access controls
- Infrastructure: Central Manager, Managed Units, GIM, S-GATE

## Report Approval REST API
The `store_stap_approval` GuardAPI command approves STAP configurations via HTTPS POST, requiring a mandatory "isNeeded" boolean parameter indicating feature activation status. Involves the STAP approval process and security configuration workflows.

Key Concepts: GuardAPI, HTTPS, POST, STAP Approval, Feature Activation

## Hostname Registration Flexibility
The hostname used during Guardium unit registration is independent of IP mode selection, supporting both IPv4 and IPv6 addresses regardless of registration mode. Must explicitly specify an IPv6 address when registering via IPv6.

Key Concepts: Hostname, Registration, IPv4, IPv6, IP Mode, Unit Registration

## Unit Hostname IP Mode Independence
The unit hostname's independence from IP mode ensures Guardium's capability to manage IP addressing transparently, allowing consistent hostname usage across different network protocols, simplifying configuration.

Key Concepts: Unit Hostname, IP Mode Independence, Network Protocol Flexibility

## API Target Host Usage
The `api_target_host` parameter in GuardAPI commands specifies the central manager or managed unit hostname/IP address for executing API calls, enabling centralized management within the Guardium system architecture.

Key Concepts: api_target_host Parameter, Central Manager, Managed Unit, IP Address Handling

## User Hierarchy API Functionality
GuardAPI's `list_user_hierarchy_by_parent_user` command with `create=true` demonstrates user hierarchy functionality for data security and management, generating detailed user relationships illustrating hierarchical data organization within Guardium's security framework.

Key Concepts: User Hierarchy, GuardAPI, Data Security, User Management

## Charting Table-Level Privileges
The Db2 Table Level Privs chart provides insights into table-level permissions within IBM Db2 databases, detailing user and group assignments, role memberships, and privilege types, supporting security audits and compliance efforts.

Key Concepts: Table-Level Privileges, User Assignments, Role Memberships, Access Monitoring

## Document Overview
**IBM Guardium Data Protection** provides enterprise database activity monitoring and security, including real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for standards like PCI-DSS, GDPR, HIPAA, and SOX.

### Features Overview
- Datasource Connectivity: Dynamic port detection, multi-driver support, CyberArk credential vault integration
- Threat Detection: Real-time policy enforcement, S-GATE blocking, incident generation
- Compliance & Reporting: Built-in report templates, automated audit trails

### Workflows Overview
- Configuration: Add datasources, deploy S-TAP agents via GIM, configure FGAC policies
- Navigation: Review activity reports, run assessments, use audit dashboards
- Action: Block unauthorized queries, rotate credentials, respond to incidents

### Personas Overview
- **Administration**: Platform configuration, user/certificate management
- **Security**: Policy definition, incident investigation
- **Database**: Manage datasources, S-TAP deployment
- **Compliance**: Regulatory reporting, audit readiness

### Entities Overview
- Agents/Collectors: S-TAP (local database monitor), A-TAP/K-TAP (network/agentless monitors), Collector (traffic aggregate), Aggregator (distributed processing)
- Policies/Controls: Security Policies (FGAC), Audit Policies, Classification Rules, Access Controls
- Infrastructure: Central Manager, Managed Units, GIM (installation manager), S-GATE (proxy blocker)

## Central Manager Registration Requirements

To enable centralized management, every IBM Guardium agent must be registered with a central manager instance. Registration involves providing the managed unit's hostname or IP address to the central manager, establishing a secure connection for command execution, status monitoring, and result aggregation.

## Central Manager Registration

### IPv6 Compatibility

During registration, specify a hostname independent of IP mode to ensure compatibility with both IPv4 and IPv6 configurations.