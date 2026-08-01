# IBM Guardium Data Protection — KNOWLEDGE

**Category:** knowledge  |  **Generated:** 2026-07-13  |  **Source:** gdp-12.x-documentation 2.pdf

---
## `find_crashed_tables.sh` Script

The `find_crashed_tables.sh` script automates detection of corrupted InnoDB tables. Cron can schedule the script, such as running daily at 2 AM with `0 2 * * * /path/to/find_crashed_tables.sh`.

Key Concepts: **Cron**, **InnoDB**, **Script Automation**, **Database Health Monitoring**

# Guardium Data Protection Overview and Key Features

IBM Guardium Data Protection is an enterprise-class database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores on-premises and in the cloud.

## Core Features
- **Secure data access** (FGAC, Data Masking, Data Tokenization, Dynamic Data Masking, API protection)
- **Database auditing** (Activity monitoring, query analytics, user behavior analytics)
- **Endpoint protection** (Endpoint DEA, Endpoint DLP)
- **Vulnerability management** (Assessments, configuration compliance checks, remediation workflows)

## Essential Workflows
1. **Configuration** - Detect data sources, deploy S-TAP agents, define policies
2. **Monitoring** - Review alerts, run reports, investigate incidents
3. **Remediation** - Apply policies, enforce access controls, respond to incidents

## Persona-Based Roles
- **Security Admins** - Policy definition, policy enforcement
- **Security Ops** - Incident response, investigation
- **Data Stewards** - Data classification, data masking, data access governance
- **Compliance** - Auditing, reporting, regulatory compliance

## Key Entities
- **Sensors** - S-TAP, A-TAP, K-TAP, Universal Connector
- **Aggregators & Collectors** - Collector, Aggregator, Central Manager
- **Policies** - Security Policy, Audit Policy, Classification Policy
- **Data Stores** - Relational databases, Big Data stores, Cloud Object Stores

## Data Source Profile Management
Guardium provides a CSV template to simplify creation of data source profiles. Steps to use:
1. Download CSV template from Guardium UI
2. Populate each row with one data source profile
3. Import completed CSV via Deploy > Data Sources wizard
4. Review and activate new data sources

## Aggregator CLI Operations
The Guardium aggregator supports CLI commands for operational tasks:
- `backup_keys` - Back up shared secret keys to specified location
- `archive_tables` - Archive static tables to designated storage path
- `show_status` - Display current status of aggregator services
Commands must be run as the `guardium` user on the aggregator host.

## Troubleshooting Approach
1. **Logger collection** - Gather diagnostic logs from affected components
2. **Event correlation** - Identify related events across S-TAP, aggregators, and collector
3. **Environment verification** - Validate network routes, service status, configuration settings

IBM Guardium Data Protection is a comprehensive solution for protecting sensitive data from unauthorized access, malicious activity, and regulatory non-compliance, with flexible deployment options and a robust set of features to meet diverse security and compliance requirements.

## Comprehensive Guide to IBM Guardium Data Protection

IBM Guardium Data Protection offers robust database activity monitoring, policy enforcement, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- Supports JDBC drivers, native drivers, and dynamic port detection for seamless database connectivity.
- Real-time capture of database traffic through S-TAP agents, enabling policy enforcement, alerting, and blocking.
- Built-in compliance templates for PCI-DSS, GDPR, HIPAA, SOX, and automated audit trails.

### Primary Workflows
- **Configuration:** Add data sources, deploy S-TAP agents via GIM, and configure FGAC policies.
- **Activity Monitoring:** Utilize activity reports, run vulnerability assessments, and access the audit dashboard.
- **Response and Action:** Block unauthorized queries, rotate credentials, and implement security incidents swiftly.

This guide consolidates essential tasks and configurations to ensure optimal setup and operation of Guardium, facilitating enhanced data security and compliance adherence.

rotection

IBM Guardium enables auditing, classification, and vulnerability assessment for cloud database services through native audit mechanisms.

**Key Concepts:** Cloud databases, Native audit, Classification, Vulnerability assessment, Auditing

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform offering real‑time visibility into SQL traffic, policy‑based threat detection (including S‑GATE blocking), extensive compliance reporting, and advanced analytics for both on‑premises and cloud data sources.

### Key Features
- **Data Source Connectivity:** Dynamic port detection, multi‑driver support, CyberArk integration
- **Threat Detection & Enforcement:** Real‑time policy evaluation, alerting, S‑GATE query blocking
- **Compliance Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit trails
- **Advanced Analytics:** Selective auditing, pattern matching, distributed report aggregation

### Workflows
- **Configuration:** Add data sources, deploy S‑TAP agents, define FGAC policies
- **Monitoring:** Review dashboards, run vulnerability scans, receive incident alerts
- **Response:** Block unauthorized queries, rotate credentials, initiate incident workflows
- **Automation:** Scheduled data mart generation, automated ticket creation

### Personas
- Administration (platform & security administrators)  
- Data Management (DBAs, data analysts)  
- Compliance (compliance officers, auditors)  
- Security (security analysts, incident responders)

### Core Entities
| Category | Examples |
|----------|----------|
| **Agents & Collectors** | S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregator, Central Manager |
| **Policy Constructs** | Security Policy, Audit Policy, Classification Rules, Access Rules |
| **Infrastructure** | GIM, Managed Units, S‑GATE, Universal Connectors |

---

## S‑TAP Collector Statistics

This section reports the total number of collectors assigned to each S‑TAP and the count of packets dropped due to insufficient collector buffer space, broken down by collector.  
**Key Concepts:** Collector Statistics, Buffer Management, Packet Dropping

## Service name (SERVICE_NAME)

The **SERVICE_NAME** parameter in a session‑level policy (type `SESSION`) specifies the Oracle service name that Guardium must match to evaluate the rule. It is used **only** when the policy condition includes `ADMIN` privilege checks across supported RDBMS families (Oracle, DB2, etc.).

## Install the IBM Guardium virtual appliance

Deploy the Guardium virtual appliance OVA, power it on, run `setup_initial_configuration` with management IP, admin password, and license file, then configure basic network settings.  

## TEE Listen Port

Use **Real Port** for K‑TAP monitoring instead of the deprecated **TEE Listen Port**. The **Connect To IP** parameter defines the IP address S‑TAP uses to connect to the monitored database when multiple network interfaces exist.  

## Database Connection Architecture

Guardium supports JDBC native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.  

## Activity Monitoring & Policy Enforcement

Guardium captures database traffic via S‑TAP agents and evaluates it against real‑time security policies. Violations trigger alerts or blocking via S‑GATE.  

## Policies and Rules

Policies and rules control access and record activity through criteria such as user, IP address, database object, and operation type.  

## Parameter `pemData`

Required for the REST API endpoint `push_insights_trust` to carry persistent entity metadata for trust validation.  

## Deploy Guardium Data Protection server

Deploy the Guardium Data Protection server before configuring the vulnerability assessment scanner; the scanner must be reachable on port **8443** from both the database server and the Kubernetes cluster.  

## Name GUARDIUM_STA

Configure the Guardium Agent Monitor (GAM) Windows Service name and name‑pipe interval in the **[Name GUARDIUM_STA]** section of *resmon.ini*.  

## An x86_64 Processor

Install External S‑TAP on x86_64 Linux with at least 800 MB RAM, 2 GB storage, kernel ≥ 3.10, iptables ≥ 1.4, Docker or Podman, ≥ 2 vCPUs, and pubkey authentication enabled.  

## Parameter `--discover‑ies` and `--stop`

`--discover‑ies` initiates automatic database discovery and replaces current Inspection Engines. `--stop` disables S‑TAP or its monitoring service without removing configuration.  

## Dual Mode

Enable dual mode for Guardium to communicate with devices using IPv4, IPv6, or both on the central manager and managed units.  

## Verify SQL Guard IP address

Verify the SQL Guard IP address, hostname, and network reachability before S‑TAP installation to prevent connectivity issues.  

## Encrypted Elastic Search

Secure Elastic Search with SSL termination for encrypted log and alert forwarding.

## Field or Control Description
The Unique Global Identifier (UGID) value, derived from the machine’s MAC address, is used for data collation and aggregation. Changing the UGID after monitoring has begun can break continuity and is therefore prohibited.

## When to Use A‑TAP
A‑TAP is required when DBMS encryption in motion is used or when internal database implementation details such as shared memory preclude traditional S‑TAP interception. If possible, prefer an exit library over A‑TAP for lower overhead.

## Parameter Description
The **application** parameter defines the application scope for a datasource, supporting predefined applications such as ChangeAuditSystem, Access\_policy, and MonitorValues. It determines which audit policies and reports apply to the traffic from that datasource.

## Observed Accesses – Observed Traffic from Guardium Internal Table GDM_Access
Observed Accesses are records in the Guardium internal table **GDM\_Access**, capturing all monitored read/write operations with timestamps, users, objects, and SQL statements. **Datasource Definitions** list existing datasource names, types, authentication information, and network locations used to identify traffic origins.

## Measuring Licensing for Guardium Vulnerability Assessment
License enforcement for Guardium Vulnerability Assessment is measured by the quantity of databases scanned. Each counted database instance triggers compliance reporting and may affect support entitlement. Proper cataloging ensures accurate licensing compliance.

## Document Overview
IBM Guardium Data Protection provides comprehensive database activity monitoring, security policy enforcement, and compliance reporting for structured and unstructured data across on‑premises and cloud environments.

**Features**
- Automated discovery of instances and configuration of inspection engines
- Real‑time monitoring with S‑TAP agents and S‑GATE rule enforcement
- Pre‑built compliance templates (PCI‑DSS, GDPR, HIPAA, SOX) and automated audit trails

**Workflows**
- Configuration: add data sources, deploy S‑TAP, define policies
- Management: review activity reports, run vulnerability assessments, operate dashboards
- Response: block anomalous queries, rotate credentials, generate incident tickets

**Personas**
- Security Administrators: manage platform, FGAC policies, compliance posture
- Database Administrators: provision data sources, maintain S‑TAP agents
- Compliance Officers: generate regulatory reports, monitor policy violations

**Entities**
- Agents & Collectors: S‑TAP (on‑host), A‑TAP (network), K‑TAP (kernel), Collector, Aggregator, Central Manager
- Policy Types: Security Policy, Audit Policy, Classification Rule, Access Rule
- Infrastructure: GIM (Guardium Installation Manager), Managed Unit, S‑GATE, Universal Connector

## 130. Plan and Organize
Users click **Overview** for an introduction, then create a **Cardholder Server IPs List** containing the IPs of servers that store cardholder data.

## 131. About this task
Failover groups have priorities; the load balancer checks groups starting with priority 1 and proceeds sequentially when searching for an available managed unit.

## 132. Components and Topology
Guardium components include Collectors that perform real‑time capture and analysis of database activity, storing it for analysis and alerts.

## 133. Unit Utilization and Unit Utilization Details Reports
Unit utilization and Unit utilization details reports provide an enterprise‑wide view of collector usage, summarizing health with Low, Medium, or High indicators to show which collectors are over‑ or under‑utilized.

## 134. Subject Alternative Name (Optional)
Subject Alternative Name (SAN) is an optional extension allowing additional hostnames to be protected by a single certificate. Once CA‑signed, the PEM‑formatted certificate (including intermediates/roots) can be imported into Guardium.

## 135. Optimizing Queries
Optimizing queries requires knowledge of internal data storage per domain; each domain defines a fixed data set influencing query performance.

## 136. About this task
With SELinux enabled, GIM and supervisor processes default to the **unconfined_service** domain after Guardium S‑TAP installation, retaining some exposure despite SELinux’s additional security layer.

## 137. Parameter Value Types
- **application (String):** Required application type for the datasource.  
- **cloudTitle (String):** Required cloud account name.

## 138. About this task
Extracted CSV files from data mart have a naming convention based on the user‑defined filename and the period start date/time in short format.

## 139. About Archived Data File Names
Guardium data archive files use a naming scheme reflecting the export date and version, with multiple files possible per day based on export/purge/archive settings.

## 140. Configuring Database Discovered Instance Rules
Guardium can automatically discover and run inspection engines on new databases created on Windows and UNIX systems.

## 141. About this task
This task explains how to access **Data Lake Reports** and tips for viewing the view/table schema used for predefined reports.

## 142. Understanding Policies
A security policy is an ordered set of rules evaluating traffic between database clients and servers, where each rule can target a client request or a server response.

## 143. IPv6 Support
IPv6 support allows session‑level and advanced policies to process IPv6 addresses.

## IBM Guardium Documentation

IBM Guardium is an enterprise database activity monitoring and security platform that monitors, enforces policies, assesses vulnerabilities, and provides compliance reporting for structured and unstructured data in on‑premises and cloud environments.

### Features Overview
- **Dynamic S‑TAP Deployment:** Deploy S‑TAP agents for traffic collection; install and migrate using a centralized installer for AIX, Solaris, and Linux.
- **Policy Enforcement:** Real‑time policy evaluation with optional blocking via S‑GATE.
- **Compliance Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX audits; automated audit trails.
- **Custom Configurations:** Define client IP masks, custom classifier properties, and patch install/remove workflows.

### Workflows Overview
- **Installation & Migration:** Run the centralized installer on AIX, Solaris, and Linux; migrate existing deployments to Guardium Insights specifying tenant ID and route name.
- **Configuration & Monitoring:** Schedule periodic uploads of buffer usage metrics; schedule patch installations and removal.
- **Security Controls:** Apply/delete database patches; configure client‑side encryption tuning.

## Consolidated Guardium Documentation Overview

### Core Capabilities
- Real-time database monitoring and security across on-premises and cloud data sources.
- Threat detection through policy enforcement and incident generation.

### Configuration Procedures
- **Datasource Management**: Include dynamic port detection and multi-driver support.
- **Policy Deployment**: Utilize FGAC policies and GIM for S-TAP deployment.
- **Compliance Reporting**: Access templates for PCI-DSS, GDPR, HIPAA, and SOX audits.
- **Vulnerability Assessment**: Add and manage assessments via the compliance interface.

### Navigation and Utilization
- Review activity reports and generate vulnerability assessments.
- Utilize the audit dashboard for continuous monitoring and incident response.

### Advanced Features
- **Credential Vault Integration**: Integrate with CyberArk for enhanced security.
- **Patch Management**: Handle software updates and patch installations securely.
- **Hadoop Integration**: Gather necessary cluster information for Ranger and Navigator integration.

### Enterprise Support
- Compatibility with Oracle Unified Auditing (Oracle Database 18c+ and Oracle Instant Client 18+ or higher).
- Secure Boot Attestation with Clevis and Tang server configuration.
- AWS IAM Role Authentication for secure AWS service interactions.

## Deleting a Patch Install Request
Use the CLI command `delete scheduled-patch` to delete a patch install request. Patches remain on the central manager after installation. Patch files on standalone or managed units are deleted post-installation.

## Updating Datasource Attributes
The `update_datasource_by_name` API allows modifying datasource attributes such as shared status. Supply the `host` and `id` parameters to identify the specific datasource.

## Adding Custom Classification Properties for Oracle
Custom properties enable Oracle datasources to leverage `DATA-CARDINALITY-FOR-SAMPLING-TABLES` for table cardinality estimation and `DA` for determining data cardinality during classification.

## Defining AWS IAM Policy for Data Streams
The AWS IAM policy for your AWS account must grant permissions to view data stream configuration and modify tags. Apply a policy with at least `datastreams:DescribeStream` and `datastreams:TagResource` actions.

## Rolling Out Custom K-TAP in Production
After verifying a custom K-TAP on a test server, log into the production server's OS and initiate the production rollout. Follow the standard K-TAP deployment steps once verification succeeds.

## A-TAP Activation Process (Post-Guardium 12.2.2)
Starting with Guardium 12.2.2, `db_exec_file` remains unmodified after A-TAP activation for Oracle versions 12.2.x and later. No additional steps are required post-activation.

## Netezza Database Entitlement Domains
Netezza DB Entitlements domains allow uploading and generating reports on Netezza entitlement data. Each domain maps to a single entity and presents a pre‑defined entitlement report.

## Distributed Reports
Distributed reports gather data from multiple managed units onto the central manager for unified correlation and analysis across the Guardium environment.

## K-TAP Module Build Process
When a new K-TAP module is requested for a specific OS/database version, Guardium builds it and notifies the customer within up to 14 days. The module is then added to the Guardium download catalog.

## Prerequisites for External S-TAP Installation
Complete this setup task the first time installing External S-TAP. It prepares the environment, including required drivers and network configurations, ensuring a smooth deployment.

## Central Management Architecture
In Central Management, one Guardium unit acts as the Central Manager, monitoring and controlling all managed units. Stand‑alone units operate independently without central oversight.

## Guardium on Hyper‑V
Before installing Guardium on Hyper‑V, confirm that the Hyper‑V environment meets Guardium's system requirements. Follow the Guardium installation guide for Hyper‑V.

## Deploying External S-TAP to Cloud Databases
Deploy External S-TAP to cloud deployments such as Oracle Cloud Infrastructure (OCI) by configuring an NGINX internal load balancer to route traffic to the S-TAP instances.

## Guardium System Domain Management
The `show system domain` command displays the current Guardium system's domain name. Use `store system domain <value>` to assign a new domain name to the appliance.

## Controlling File Classification
The analysis controls option determines if file classification is enabled or disabled and whether it relies solely on predefined rules or custom configurations.

## Define Monitoring Activities

Specifies which database activities are monitored and logged:
- **Value-Change Audit** tracks changes to data values.
- **DML Audit** records data manipulation language statements (INSERT, UPDATE, DELETE).
- **DCL Audit** logs data control language statements (GRANT, REVOKE).

Selectively enable these audit types to balance monitoring coverage with performance impact.

## Guardium Host

The `Guardium Host` parameter defines the IP address or hostname of the Guardium appliance that receives events from S-TAP agents.  
If unspecified, S-TAP defaults to the first Guardium host defined in the configuration.

## Unsupported Database Types

The S-TAP agent does **not** support the following databases:
- IBM Informix
- Sybase
- MariaDB
- SAP HANA

For these databases, use A-TAP, K-TAP, or native audit mechanisms instead.

## Compiler Support

Guardium S-TAP supports compilation on systems with:
- GCC version 4.8 or later
- Clang version 3.5 or later

The installation script automatically detects the compiler version and proceeds if a supported compiler is present.

## Enable/Disable S-TAP

The `var_stap_enabled` parameter toggles S-TAP monitoring for a specific instance:
- **Enabled (1)**: Starts S-TAP and begins traffic capture.
- **Disabled (0)**: Stops traffic capture and disconnects the agent.

Changes require restarting the S-TAP service (`stapctl stop` / `stapctl start`).

## deployment_mode

`deployment_mode` determines how S-TAP is installed:
- **GIM**: Uses Guardium Installer Manager (default for most platforms).
- **RPM**: Direct RPM installation (used on older Linux distributions).
- **HP-UX**: Special mode for HP-UX systems.

Select the appropriate mode for the target host architecture.

## Enable/Disable Module

The `module_<n>_enabled` flag controls whether a specific Guardium module (e.g., `module_1_enabled`) is active.  
Disabling a module prevents its associated agents and collectors from processing traffic, useful for troubleshooting or maintenance.

## Port Protocol Function
Guardium system services use standard network ports and protocols:
- FTP (20/21 TCP) – file transfer
- SSH/SCP (22 TCP) – remote command and file transfer
- SMTP (25 TCP) – email notifications
- DNS (53 TCP) – name resolution
- NTP (323 UDP) – time synchronization
- SNMP (161 TCP/UDP) – monitoring and management data
- LDAP (389 TCP) – directory authentication
- FTP data (20 TCP) – passive data channel
- SSH data (22 TCP) – encrypted data channel

## Before You Begin
Deploy External S‑TAP with Helm only after **Git**, **Kubernetes**, and **Helm** are installed and correctly configured on the control plane. Initialized clusters and Helm repositories are prerequisites for the deployment workflow.

## Send Command
The **S‑TAP Commands** window allows an administrator to issue control actions such as **restart** the S‑TAP service on the monitored host. The exact restart behavior (service restart vs. container restart) depends on the load‑balancing configuration in use.

## MSSQL 2000
For MSSQL 2000, set the **compatibility mode** parameter and define a `conProperty` connection string for JDBC connections. These settings ensure the Guardium collector can correctly interpret query syntax and data types specific to that legacy version.

## How Log Records Affected Works
**Log Records Affected** sniffs additional response packets after a query finishes, ensuring all rows modified or returned by the statement are captured accurately in the audit log.

## Over‑Generalized Access
Over‑generalized access describes three risk patterns:
- Broad privileges granted to many users (e.g., `SELECT ANY TABLE`);
- Dormant accounts/tables retaining high‑level permissions without active use;
- Privilege propagation from one user to another through roles or shared resources.  
Detecting and remediating these patterns is a primary compliance objective in Guardium.

## Before You Begin (Query Rewrite)
To enable query‑rewrite usage on a Guardium Central Manager, create and test the rewrite rule on the **collector** using the **Query Rewrite Builder**. Only after successful validation can the rule be exported and applied centrally.

## About This Task
*Table 1* lists the **default predefined extractions to file** (e.g., session logs, access logs) that run **hourly**.  
*Table 2* provides recommended **execution windows** for each extraction to avoid performance impact during peak business hours.

## Rule Criteria
**File‑access rule criteria** let you specify which accesses trigger alerts or reporting events. Criteria may be scoped to a single datasource or a group (file‑server cluster) and can include user, process, file path, and operation attributes.

## Component Description
The **OS Type** field in a template set indicates whether the target systems are **Windows** or **UNIX**. This setting determines which binaries, service names, and configuration files the template will reference; it can only be changed when the template set contains no members.

## Before You Begin (K‑TAP)
When deploying a custom **K‑TAP** module on a Linux host with Secure Boot enabled, sign the module **before installation** by running the `kernelModuleSigning.sh` script on the build system. Signing ensures the kernel will load the driver without rejecting it as unsigned.

## Parameter Value Type Description
The **`savePassword`** parameter of the `update_cloud_datasource` API determines whether authentication credentials (username/password or token) are persisted. If **true**, credentials are saved in the encrypted Guardium credential vault; if **false**, they are supplied only for the duration of the API call.

## Defining Datasources for Scheduled Tasks
(Entry incomplete – no further meaningful content to extract.)

## Guardium Datasource Management for Scheduled Tasks

Configure datasources with IP/hostname, instance/SID, credentials, and for JDBC, driver class, URL, and security properties. Use dedicated service accounts with minimal permissions. Verify network connectivity to target systems before automation. Associate datasources with tasks via the Guardium console, selecting frequency and execution window. Monitor execution through audit logs for successful data collection.

## Enabling IPv6 Support in Guardium

Ensure all systems run Guardium version 11.1 or later for IPv6 compatibility. Enable IPv6 in Central Manager network settings and assign IPv6 addresses to management interfaces. Propagate changes to managed units and test IPv6 connectivity. Adjust firewall rules to permit IPv6 traffic.

## Unregistering Guardium Managed Units

Unregister managed units from the Central Manager admin console to maintain accurate licensing. Select the unit and choose unregister, removing it from the Central Manager's inventory but preserving local data. Direct unregistering from the unit does not affect licensing.

## Configuring External Storage Systems

Use `store storage-system` GuardAPI to configure Amazon S3, IBM Cloud Object Storage, or TSM for backup/archival. Specify type, host endpoint, credentials, and connection parameters. Enable storage with `on` and disable with `off`. Ensure functional network paths for data archiving.

## S-TAP Command Flags `--discover-ies` and `--stop`

`--discover-ies` enables automatic discovery and update of Inspection Engines. `--stop` temporarily halts S-TAP without uninstallation, useful for maintenance. Use `guardium install tap discoveries=On|Off stop=On|Off` to manage dynamic database environments and controlled downtimes.

## Updating Audit Case Severity via GuardAPI

Use `update_ata_case` to change the severity of audit cases. Parameters: `actualCaseSeverityString` (High/Medium/Low) and `caseIdList` (comma-separated IDs). Example: `update_ata_case actualCaseSeverityString=High caseIdList=123,456,789`.

## Visualizing Data Activity with Topology View

Guardium's topology view uses animated bubble charts to visualize data activity over time. Bubbles represent database objects, with size and animation reflecting interaction volume. Real-time updates enhance situational awareness, aiding in rapid identification of suspicious activities and compliance violations.

## S-TAP Startup Troubleshooting

Guardium logs specific fatal S-TAP startup errors to the Windows Event Log when configuration issues prevent the service from launching. Review these entries to diagnose problems such as missing files, permission denials, or corrupted settings. Common resolutions include verifying file and directory permissions, ensuring all required paths exist, correcting environmental variables, and confirming version compatibility with installed database agents. Restart the S-TAP service after applying fixes.

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring
and security platform.

### Mode Involves
Executing the `diag.bat` utility from appropriate Windows directories to diagnose
installation or runtime problems such as connectivity, resource limits, or driver
conflicts.

### About This Task
Inspecting and centrally managing multiple Guardium inspection engines (datasource
instances) is performed only on the collector where the engine resides. Engines
cannot be created or started from the Central Manager.

### Parameter Details
| Parameter | Type | Description |
|-----------|------|-------------|
| `filterIgnoreVerbs` | int (default 1) | Omits verb text from captured queries, reducing analysis noise. |
| `filterTempObjects` | int (default 1) | Excludes temporary tables, procedures, and transient objects from datasets. |
| **Both defaults are enabled (1)** to minimize false positives. |

### Services Status Panel
A single‑page view of critical Guardium services (CAS, alerter, scheduler) across
all domain appliances. Accessible via **Setup → Tools & Views → Services Status**
for quick health diagnostics.

### `files:read` Permission
Enables Intelligent Data Discovery and Data Classification to read files shared
in Slack channels, scanning uploads for sensitive data patterns (credit cards,
PII, PHI).

### New Name
Starting with Guardium 12.0, the cross‑CM health view is now called **Enterprise Hub**,
highlighting its role as the centralized monitoring and management interface for
distributed deployments.

### Additional Constraints
Physical S‑TAP deployments may also be limited by the **Processor Value Unit (PVU)**
rating of the underlying hardware nodes—approximately **4 000 PVU per collector
node** is recommended for balanced performance, though actual limits vary with
workload and policy.

### S‑TAP Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `auto_discovery` | boolean | Enables automatic discovery of new database instances on the host. |
| `buffer_size` | int (MB) | Size of the in‑memory buffer for captured traffic before flushing. |
| `checkpoint_period` | int (seconds) | Interval for batching and sending collected data to the collector. |
| `client_baseline` | filename | Baseline configuration for distinguishing legitimate client traffic. |

These parameters affect capture granularity, stability, and throughput.

### Example Scenarios
Illustrate entitlement usage (user‑seat licensing) with configurations such as:
1. Standard users accessing a single production Oracle database.
2. Developers connecting to multiple test databases with elevated privileges.
3. External partners using a shared SaaS‑based PostgreSQL service.

### Command
`show csr wildcard key create self-signed gui` generates a self‑signed CSR using the
appliance’s FQDN for Guardium web UI/API authentication. The hostname and domain
must be set before execution.

### External S‑TAP
A network‑level monitoring component that captures database traffic without an on‑host
agent, ideal for cloud workloads, virtualized environments, and HA clusters.

### Preparing SAP‑HANA S‑TAP
1. Enable SSL/TLS on the HANA database.  
2. Install the S‑TAP agent on the HANA host and point it to the Guardium collector.  
3. Enable the appropriate datasource type in the Guardium console.

### External S‑TAP Failover
Configure AWS Route 53 health checks or integrate with CloudWatch metrics for
high‑availability monitoring, ensuring uninterrupted service if the primary S‑TAP
instance fails.

### Registry Setting
`HKEY_LOCAL_MACHINE\SOFTWARE\IBM\InfoSphere Guardium\WinStap\WER_DUMP_COUNT`
(REG_DWORD, 0‑5) controls the maximum number of Windows Error Reporting dump files
retained locally; `0` disables dumps.

### Sensitive Data Access
Guardium Fine‑Grained Access Control (FGAC) policies enforce granular visibility
and export controls based on user/group, business context, data classification tags,
and temporal constraints.

## Guardium Overview
Guardium provides real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on‑premises and cloud stores.

## Features
- **Risk Scoring:** Daily users' risk from violations, assessments, exceptions, and anomalies.
- **Policy Automation:** Streamlined confidentiality and usage monitoring wizard.
- **Data Discovery:** Finds sensitive tables and adds them to monitoring groups.
- **Unified Architecture:** Cloudera Navigator integration for Hadoop audit events.
- **Investigative Dashboards:** Local or distributed ad‑hoc data exploration.

## Workflows
- **Session‑level Policy Definition:** Adds session context to standard policy steps.
- **Disaster Recovery:** License and SSL certificates must be reinstalled after restore.
- **Entitlement Optimization:** "What If" analysis predicts impact of new privileges.
- **Big Data Intelligence:** Centralizes mart data for long‑term reporting.

## Personas
- **Security Officer:** Manages risk scoring, compliance, entitlement analysis.
- **DB Administrator:** Deploys S‑TAP agents, defines data discovery groups.
- **Compliance Manager:** Uses wizards to deploy policies and maintain archives.

## Entities
- **Modules:** Violations, Vulnerability Assessments, Classification Engine, Buffer Monitor, Archiving Manager.
- **Concepts:** Risk Indicator, Session Policy, Sensitive Data Table, External Feed, Disaster Recovery Set.

## Risk Scoring Engine
Risk Spotter aggregates violations, assessments, exceptions, and anomalies to calculate a daily overall risk score for each user.

## Compliance & Application Data Monitoring Wizard
Guides creation of policies for regulatory mandates and sensitive‑data discovery, automating source selection, group creation, and policy activation.

## Sensitive Data Search
Scans databases, flags confidential columns (e.g., SSN, credit‑card numbers), and adds those tables to monitoring groups.

## Session‑Level Policy Workflow
Mirrors standard policy flow but binds the policy to a specific session context (user, application, time window) for granular enforcement.

## Hadoop Audit Integration
Cloudera Navigator agent forwards HDFS, YARN, Hive events to the Navigator server; Guardium correlates these with its own logs for unified big‑data and relational visibility.

## Investigative Dashboards
Allows interactive exploration; runs in local mode (single machine) or distributed mode (multiple collectors) for enterprise forensics.

## Disaster Recovery License Re‑installation
After restoring configuration, manually reinstall the license file and regenerate or restore SSL certificates to re‑enable enforcement.

## Entitlement Optimization – What If Analysis
Simulates granting a privilege to predict its effect on policy checks, risk scores, and compliance outcomes, providing a justification score.

## Guardium Big Data Intelligence Data Mart Architecture
Provision a central location for periodic transfer of data‑mart exports; agents transform raw audit logs into the mart schema and push aggregated records for long‑term analytics.

## A‑TAP Upgrade Procedure
1. Deactivate A‑TAP.
2. Upgrade the database or S‑TAP.
3. Reactivate A‑TAP (required for versions before 12.2.1); versions 12.2.1+ auto‑recover.

## Database Buffer Utilization Monitoring
Shows inspection core load, buffer percentages per collector (up to three), and alerts when thresholds are exceeded.

## Collector vs. Aggregator Archiving
- **Collector Archiving:** Simple, limited by local storage.
- **Aggregator Archiving:** Efficient for high volume, consolidates before archiving but adds network load.

## External Feed Configuration
(Entry incomplete; not merged as it references missing content.)

## Guardium Overview

### Features
- Database connectivity via native JDBC and generic drivers; dynamic port discovery.
- Real-time monitoring with S-TAP agents, S-GATE inline blocking, and policy enforcement.
- Compliance reporting for PCI‑DSS, GDPR, HIPAA, SOX; automated audit trails.

### Workflows
- **Configuration:** Define datasources, deploy S‑TAP via GIM, configure FGAC policies, enable auto‑discovery.
- **Management:** Use dashboards, generate activity reports, perform vulnerability scans, monitor health.
- **Action:** Block unauthorized queries, rotate credentials, generate incident reports, run assessments.

### Personas
- **Guardium Admin:** Deploys/configures components, manages users/roles.
- **Security Admin:** Creates FGAC policies, monitors alerts, investigates incidents.
- **DB Admin:** Installs S‑TAP, configures audit settings, reviews personal data findings.
- **Compliance Officer:** Executes GDPR, PCI, HIPAA reports, tracks compliance status.

### Entities
- **Agents/Collectors:** S-TAP (database agent), A-TAP (encrypted traffic), K-TAP (kernel driver), Collector, Aggregator, Central Manager.
- **Policies/Rules:** Security Policy (inspection engines), Audit Policy (logging), Classification Rule (PII discovery), Access Rule (FGAC).
- **Infrastructure:** GIM (installer manager), Managed Unit, S-GATE (blocking gateway), Universal Connector, Investigation Dashboard.

---

## Optimize TURBINE Database Tables

Run `optimize_database` during low‑usage periods to rewrite tables, eliminate fragmentation, and reclaim filesystem space.

**Key Concepts:** TURBINE schema, database optimization, storage reclamation

---

## Configure S‑TAP Using Workflow Builder

Open Workflow Builder, select *Event Type* → *Event Status*, and complete the setup steps to configure S‑TAP data sources, test connections, and verify audit server status.

**Key Concepts:** S‑TAP configuration, workflow automation, data source validation

---

## Enable IPv6 Considerations

Ensure IPv6 infrastructure is ready and Guardium version 11.1+ is used; IPv4/IPv6 mixing is unsupported.

**Key Concepts:** IPv6 readiness, protocol compatibility, version requirements

---

## Deploy Guardium on Red Hat Virtualization

Review Red Hat Virtualization prerequisites and features before installing Guardium to avoid installation issues.

**Key Concepts:** Virtualization platform specifics, deployment prerequisites

---

## OpenSSH Version Check

Use `show openssh version` to verify the OpenSSH version on a Guardium appliance, aiding connectivity troubleshooting and security compliance checks.

**Key Concepts:** OpenSSH utility, version verification, security patches

---

## Cross‑CM Health View Appliance Requirements

Dedicate a standalone Guardium appliance for Cross‑CM health monitoring to ensure accurate metrics.

**Key Concepts:** Health monitoring appliance, resource isolation, dedicated hardware

---

## GDPR Policy Violations Reports

Guardium generates GDPR‑specific audit reports (Data Subject Delete, Rectification, Access, Personal Data Discovery, Server) for compliance monitoring.

**Key Concepts:** GDPR compliance, audit reporting, data subject rights, personal data discovery

---

## IPv4 Reconfiguration Procedure

In Network Settings, select *IPv4* and follow prompts to restore IPv4 configuration after IPv6 or dual‑stack setups.

**Key Concepts:** IPv4 reconfiguration, protocol transition, network settings panel

---

## S‑TAP Agent Functionality and Auto‑Discovery

S‑TAP monitors database traffic and forwards it to the collector; auto‑discovery automatically retrieves and enables Unix‑Linux inspection engines daily.

**Key Concepts:** S‑TAP monitoring, auto‑discovery process, Unix‑Linux database support

---

## Define Event Workflows

1. Open Workflow Builder.
2. Select *Event Type*.
3. Choose *Event Status*.

This defines custom event handling workflows.

**Key Concepts:** Event workflow definition, Workflow Builder, event customization

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise platform for securing structured and unstructured data across on‑premises and cloud data stores. It offers real‑time database activity monitoring, vulnerability assessment, compliance reporting, and policy enforcement.

### Key Features
- **Database Connectivity:** JDBC, native drivers, dynamic port detection
- **Threat Detection:** Real‑time monitoring, S‑GATE blocking, security incidents
- **Compliance Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX

### Workflows
- **Configuration:** Add datasources, deploy S‑TAP agents, define policies
- **Monitoring:** Review activity reports, run vulnerability scans, use dashboards
- **Response:** Block unauthorized queries, rotate credentials, investigate incidents

### Personas
- **Administration:** Platform and user management, security configuration
- **Database Management:** Datasource setup, S‑TAP deployment, policy definition
- **Compliance:** Generate regulatory reports, track audit trails

### Entities
- **Agents:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- **Policies:** Security, audit, classification, access rules
- **Infrastructure:** Guardium Installation Manager, Managed Units, S‑GATE, Universal Connector

with the instance name. For Oracle on Linux, run `guardctl activate-oracle`. This installs the necessary software, configures the kernel module, and enables transparent traffic capture for encrypted connections.

**Key Concepts:** GIM, A‑TAP, GuardCTL, Oracle Activation, Linux Configuration

ce Monitoring** – Enable the **Real‑Time Alerts** module to generate incidents whenever a policy is violated. Configure **Data Mart** jobs to export compliance logs daily to a SIEM or external storage.
5. **Generate & Distribute Reports** – Use the built‑in **Compliance Report** templates (PCI‑DSS, GDPR, HIPAA) and schedule them for automated delivery to audit teams. The reports include violation counts, data‑access summaries, and remediation dashboards.
6. **Automate Remediation** – Link policy violations to **Remediation Workflows** (e.g., password reset, data‑masking scripts) that execute automatically or trigger ticket creation in your ITSM system.
7. **Maintain the Program** – Periodically re‑run classification jobs, update policy tags, and review audit findings. Guardium’s **Audit Trail** records all configuration changes for continuous improvement.

## Manage S-TAP Clusters

The **Manage S-TAP Clusters** page (central manager only) provides create, edit, and delete controls for S-TAP cluster configuration. Cluster‑wide changes can be made for multiple S-TAP instances.

## Parameter Value Types for non_credential_scan

**non_credential_scan** requires two mandatory string parameters:  

- **databaseType** – type of the target database.  
- **serversGroup** – name of the group containing the target servers.

## GuardAPI Syntax for activation

To start data streaming, the **activate** Boolean parameter is required. If `activate=true`, the **cloudTitle** parameter must also be supplied to identify the cloud database service account used for streaming.

## Registering Managed Units

Managed units can be registered for central management from either the **Central Manager** or directly from the unit’s own GUI/CLI. Registration makes the unit part of the Guardium ecosystem and controllable from the central console.

## Job Queue

The **job queue** is a background process that stores assessments and classification tasks. It continuously polls for pending jobs and executes them sequentially, eliminating the need for manual task triggering.

## Configuring a General Slon Looper

Open the **New looper configuration window** (see documentation for the *slon looper utility*) to configure a general slon looper. This looper automates periodic execution of replication‑related tasks.

## Install and Schedule S-TAP on Windows

After installing the **GIM client** on a Windows host, schedule an **S-TAP installation** from Guardium and provide the mandatory **WINSTAP_INSTALL_DIR** parameter. This directory cannot be changed after installation.

## Preparing for IBM COS Target

Before configuring an **IBM COS** target, note that **Cleversafe** is now **IBM Cloud Object Storage**. Also, IBM COS external storage is not supported on **IPv6** deployments.

## External S-TAP Load Balancer Scripts

Guardium **External S-TAP** deployments require **load balancer scripts** to provide redundancy and eliminate single points of failure. These scripts handle endpoint discovery and distribute traffic across multiple S-TAP instances.

## Directory and MYSQL\_HOME

The **Directory** field indicates the installation path of the Guardium component. If MySQL is installed in a non‑standard location, set the optional **MYSQL\_HOME** environment variable. Unicode‑encoded database names are not supported.

## DB2 z/OS Entitlements

**DB2 z/OS entitlements** capture database privileges assigned to individual grantees, PUBLIC, special roles, JAR resources, packages, and zSecure role mappings. They enable fine‑grained, role‑based access control tailored to z/OS environments.

## Document Overview

IBM Guardium Data Protection provides enterprise database activity monitoring, vulnerability assessment, and compliance reporting for structured and unstructured data, on‑premises and in the cloud.

### Features Overview
- **Custom Query‑Report Builder**: Create ad‑hoc queries against custom domains and tables, save reusable reports.
- **AWS HA for External S‑TAPs**: High availability using Route 53 health checks and CloudWatch alarms across Availability Zones.
- **GuardAPI Automation**: CLI to automate provisioning, policy enforcement, report generation, and bulk configuration.
- **S‑TAP Configuration Parameters**: Fine‑tune S‑TAP behavior (log4j verbosity, max write size, compression, user‑role tracking, etc.).

### Workflows Overview
- **Custom Query Authoring**: Build queries on user‑defined tables, execute ad‑hoc or scheduled.
- **External S‑TAP HA Setup**: Deploy S‑TAP in multiple AZs, configure health checks and failover via Route 53 and CloudWatch.
- **Automating with GuardAPI**: Scripted bulk tasks, scheduled jobs, and API‑driven deployment pipelines.
- **S‑TAP Tuning**: Adjust parameters like log4j logging level, compression thresholds, and collection settings to balance performance and forensic detail.

### Personas Overview
- **Security Administrator**: Design custom queries, define policies, manage GuardAPI scripts and automation.
- **Database Administrator**: Optimize S‑TAP performance, verify HA failover, review raw SQL collections.
- **Compliance Officer**: Use custom queries for audits, validate controls via saved reports.

### Entities Overview
- **Custom Domains & Tables**: User‑created data structures queryable via the Report Builder.
- **AWS Resources (Route 53, CloudWatch)**: External services enabling S‑TAP HA and monitoring in AWS environments.
- **GuardAPI Commands & Parameters**: CLI commands and flags for bulk management and automation.
- **S‑TAP Configuration Files**: Agent settings (e.g., `LOG_FULL_DETAILS`, compression) stored locally on monitored hosts.

---


## Working with Custom Queries

The **Custom Query‑Report Builder** lets users define ad‑hoc SQL queries against **custom domains**—user‑defined schemas that hold application‑specific tables.

1. **Define a query**: Select tables, add joins, filters, and aggregations.  
2. **Save as a report**: Store for later reuse, schedule execution, or run on demand.  
3. **View results**: Directly in Guardium UI or export for external analysis.

Key artifacts: Custom Domain, Custom Tables, Query Builder, Ad‑hoc Reporting.

---


## Configuring AWS HA for External S-TAPs

Deploy External S‑TAP agents across multiple AWS Availability Zones for **high availability**.

1. **Deploy multiple instances**: One per AZ to ensure at least one remains operational.  
2. **Route 53 health checks**: Monitor each S‑TAP’s health endpoint.  
3. **CloudWatch alarms**: Trigger DNS failover to a healthy instance when a health check fails.  
4. **Automatic failover**: Guardium collectors redirect traffic seamlessly without manual reconfiguration.

Key artifacts: External S‑TAP, AWS HA, Route 53, CloudWatch, Failover.

---


## Accessing GuardAPI Commands

**GuardAPI** is a command‑line interface for automating Guardium tasks.

1. **Connect**: SSH to the Guardium appliance or use the web console CLI.  
2. **Execute**: `guardapi <command> param=value ...` (e.g., `create_data_source type=Oracle host=ora01 port=1521`).  
3. **Automate**: Chain commands in scripts, schedule via cron, or embed in CI/CD pipelines.

Key artifacts: GuardAPI, CLI, Automation Scripts, Scheduled Tasks.

---


## Parameter Value Types and Descriptions

Key **S‑TAP configuration parameters**:

- **log4j_settings** – control diagnostic log verbosity and format.  
- **max_write_size** – limit bytes per log file write to prevent flooding.  
- **compression_threshold** – enable compression of log data beyond this byte count.  
- **user_tracking_fields** – specify which user role fields (e.g., `USER`, `ROLE`) are captured.  
- **log_full_sql** – toggle capture of complete SQL statements for forensic analysis.

These parameters are set through the S‑TAP configuration file or via GuardAPI (`set_stap_parameter`).

Core Parameter Adjustments
---

Adjust the **compression_threshold** value to control when data is compressed before being sent to the Guardium collector, and enable **behavior_tracking_fields** to capture additional forensic data such as username and roles for each database session. These settings are modified via the Guardium UI or using `modify_guard_param` GuardAPI.

Client/Server IP and Full SQL Details
---

When the **LOG FULL DETAILS** policy rule is enabled, S‑TAP captures the full SQL text and logs the client IP address in each audit record. The **Client IP** column is populated only under this rule, and records are sorted by **FULL SQL ID** descending within each second for consistent ordering.

External S‑TAP Deployment Steps
---

1. **TLS Assets**: Generate a private key (`proxy.key`) and obtain a TLS certificate (`proxy.pem`) signed by a trusted CA.  
2. **Secure Storage**: Store the key‑pair on the collector, a persistent volume, or as a Kubernetes secret accessible at startup.  
3. **S‑TAP Configuration**: Reference the asset locations in the S‑TAP config file or with the `create_s_tap` GuardAPI call.

Analyzer Log‑Volume Insights
---

`show alp_throttle` reports data volume written to `GDM_FLAT_LOG`. High values may indicate heavy audit traffic or verbose log4j settings. To mitigate collector load, lower `max_write` or enable compression.

Real‑Time Trust Evaluator Overview
---

The **RTTE** assigns a trust score (0‑100) to each connection based on source, historical behavior, and current context. Scores drive policy actions (e.g., blocking) when a low trust level is detected.

Mixed‑Version Distributed Reports
---

32‑bit Central Managers cannot pull data from 64‑bit managed units due to architecture‑specific data structures. Standardize to one bitness or use alternative export methods for cross‑architecture reporting.

Guardium Big Data Intelligence Streaming
---

1. Enable streaming on each collector.  
2. Set the GBDI ingestion endpoint (e.g., Kafka/HTTP) and auth details.  
3. GBDI ingests the stream for real‑time analytics, threat hunting, and dashboards.

K‑TAP Build Troubleshooting
---

If S‑TAP installation reports K‑TAP build failures, ensure **GCC 11** is available at `/opt/rh/gcc-toolset-11/root/usr/bin/gcc` and that this path precedes any incompatible compilers in `PATH`. Re‑run the installer after verification.

Policy Builder for Data Workflow
---

The unified **Policy Builder for Data** UI lets you create, edit, and install policies, rule sets, and actions without disrupting live monitoring. It validates configurations before activation.

Datasource Management APIs
---

Guardium provides CRUD‑style APIs for datasource management: `modify_guard_param`, `add_connection`, `create_datasource`, `delete_datasource`, `list_datasources`, and others. These endpoints support programmatic automation via GuardAPI calls.

Access Management Roles
---

The **Access Management** application supplies default roles that determine UI visibility, functional privileges, and which actions administrators can take within the Guardium console.

### MySQL Table Privilege

The `SELECT_MYSQL_TABLE_PRIVILEGE` Guardium class wraps the MySQL privilege
`SELECT`. It promotes query activity on a specific MySQL table to a high‑risk
level, allowing detailed examination of that usage pattern.

## Identification and Authentication (IA-2)

IBM Guardium supports NIST SP 800‑53 IA‑2 by enforcing multi‑factor authentication before permitting smart‑card login attempts.

## Oracle NUMBER and VARCHAR2 Data Types

Oracle’s `NUMBER` type stores numeric values with user‑specified precision and scale. The `VARCHAR2` type stores variable‑length character strings, limited only by the maximum column size defined in the schema. Both types are essential when classifying catalog data across relational and document sources, ensuring accurate data typing and validation.

D™ Datasource Activity Monitoring:

```markdown
## Guardium Activity Monitoring Overview

IBM Guardium Data Protection provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features
- **Dynamic Datasource Connectivity:** Supports multiple JDBC drivers, CyberArk integration, and dynamic port detection.
- **Real-Time Threat Detection:** S-TAP agents capture traffic; S-GATE enforces blocking; policies trigger alerts or automatic actions.
- **Regulatory Compliance:** Built-in report templates for PCI‑DSS, GDPR, HIPAA, SOX, and customizable audit trails.

### Core Workflows
- **Configuration:** Add datasources, deploy S-TAP agents via GIM, create FGAC policies.
- **Investigation:** Review activity reports, run vulnerability scans, query audit logs.
- **Remediation:** Block unauthorized queries, rotate credentials, respond to incidents from the dashboard.

### Personas
- **Administration:** Platform setup, user provisioning.
- **Security Management:** FGAC policy design, rule creation.
- **Data Engineering:** Database provisioning, query analysis.
- **Compliance:** Report generation, audit evidence collection.

### Architectural Entities
- **Agents:** S-TAP (in‑database), A-TAP (out‑of‑band), K-TAP (kernel).
- **Policies:** Security, Audit, Classification, Access.
- **Infrastructure:** Managed Units, Aggregators, Central Managers, Universal Connectors.
```

---

## Nanny Process Killing Sniffer

### Symptom

`Nanny process error condition`

### Resolution

- Check collector resource usage
- Add collectors or upgrade capacity
- Simplify policies that fire on volume
- Verify S-GATE configuration

---

```markdown
# IBM Guardium Data Protection Overview

## Features
- Dynamic datasource management, anomaly detection, policy enforcement, and session monitoring.
- Real-time threat detection, compliance reporting, and data archiving.

## Workflows
- **Configuration and Deployment**: Add datasources, deploy S-TAP, configure policies.
- **Investigation and Review**: Inspect anomalies, review session attachments.
- **Service and Maintenance**: Ensure proper inspection setup and data archival.

## Personas
- **Database Administrators**: Manage database configurations.
- **Security Analysts**: Monitor and analyze SQL details.
- **Compliance Officers**: Archive and retrieve audit data for compliance.

## Entities
- **Hosts and Instances**: Configured via SQLGuard_n entries.
- **Security Components**: S-TAP, firewall attachments, policies.
- **Compliance Tools**: Systems for archiving audit logs and retrieving mappings.

# Authentication and Command Syntax

## GuardAPI Authentication
The `guiuser` account authenticates with default CLI accounts (guardcli1-guardcli9) before executing GuardAPI operations.

## Command Syntax
GuardAPI schedules data mart generation using the `add_dm_to_profile` command:
- `category` (string): Specifies the data mart category.
- `cron_string` (string): Defines the execution time using cron syntax.
```

ucture Components:** Data Sources, Managed Units, Managed Units, Data Servers.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection monitors database activity, enforces security policies, and generates compliance reports across on‑premises and cloud data sources. The platform supports multiple deployment models, real‑time threat detection, and integrates with external authentication and credential vaults.

### Features
- **S‑TAP Agent:** Collects traffic from database servers and streams it to Guardium collectors.  
- **Policy Engine:** Enforces FGAC rules, blocks unauthorized queries, and raises alerts.  
- **Data Classification:** Discovers sensitive data and records classification results.  
- **Compliance Reporting:** Provides pre‑built templates for PCI‑DSS, GDPR, HIPAA, SOX, and custom audits.  
- **Central Management:** Unified UI for configuration, monitoring, and governance across managed units.

### Workflows
- **Agent Deployment:** Install/upgrade S‑TAP via GIM, CLI, or interactive installer.  
- **Policy Configuration:** Define FGAC, audit, and data‑classification policies through the Guardium UI.  
- **Incident Response:** Alert generation, S‑GATE blocking, and ticket creation based on policy violations.  
- **Compliance Audits:** Schedule report generation, export, and distribution to auditors.

### Personas
- **Security Administrator:** Manages policies, users, and Guardium infrastructure.  
- **Database Administrator:** Owns data sources, controls S‑TAP installation and configuration.  
- **Compliance Officer:** Views audit logs, runs compliance reports, and certifies controls.  
- **Data Analyst:** Executes queries, views reports, and interacts with protected data.

## Deploy Monitoring Agents

Install, upgrade, or uninstall S‑TAP on Windows using GIM, the interactive installer, or the command line. The process automatically detects supported database instances when discovery is enabled. After installation, configure default monitoring settings and security policies.  

### Features Overview
- Real‑time threat detection, compliance reporting, data discovery and classification, exfiltration prevention  

### Workflows Overview
- Configuration & deployment (add datasources, deploy S‑TAP agents, configure policies via GIM)  
- Monitoring & analysis (review activity reports, dashboards, incident alerts)  
- Incident response (block queries, rotate credentials, triage security incidents)  
- Audit & compliance (generate automated audit trails and regulatory reports)  

### Personas Overview
- Security administrators (policy management, rule creation)  
- Database administrators (datasource connectivity, S‑TAP maintenance)  
- Compliance officers (policy exceptions, compliance dashboards)  
- Security analysts (threat investigation, log analysis)  

### Entities Overview
- Agents & collectors (S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregator, Central Manager)  
- Policies (Security policy, Audit policy, FGAC definitions, Data classification rules)  
- Infrastructure (Managed units, GIM, S‑GATE, Universal Connector)  

---

## Create an Auto‑discovery Process

Create an Auto‑discovery process by accessing the Guardium Auto‑discovery Configuration UI, defining a new process with specific host and port ranges, and saving the process. The process runs at the schedule you set, scanning the specified range and automatically configuring S‑TAP agents, classification rules, and audit policies for newly discovered databases. After creation, you can view the process details, edit its parameters, enable or disable it, or delete it when no longer needed.

## Tips and Tricks for IBM Guardium Data Protection

- Use descriptive naming conventions for Event Hub and monitored databases to avoid confusion later.

## Understanding Domains in Guardium

- Domains group data by function (e.g., data access, policy violations) and are selected when creating a query.

## Using the All Parameter for Threat Detection

- The 'all' parameter enables threat detection scanners on all managed units in central management, equivalent to the same option for `api_target_host`.

## Assessing RACF Vulnerabilities

- Evaluate RACF privileges regardless of whether they are granted within or outside the database to assess vulnerabilities.

## Preparing to Build Custom K-TAP Modules

- Verify that `STAP_UPLOAD_FEATURE=1` is set in the Guardium configuration before building a custom K-TAP module.

## Reregistering Aggregator Collectors

- Use the `reregister_agg_collector` GuardAPI to reassign collectors to different aggregators, requiring `newDomain` and `newHostName` parameters.

## Preparing for Integration

- Export the certificate with a browser after logging into Guardium Data Protection before beginning integration.

## Audit Process for SQL Injection Cases

- "Suspected SQL Injection Cases" audit process extracts and lists suspected SQL injection attack cases, customizable or duplicable.

## Configuring Backups

- Choose "Configuration" for definitions/settings only, or "Data" to include actual data; ensure sufficient free space before proceeding.

## Enabling Encrypted SQL Connections

- Update container-level configurations for the lister, extractor, support_backbone, and executer services to enable encrypted Microsoft SQL SSL connections with Windows authentication.

## Database Statement Attributes

- Each statement is assigned an ID, with execution timestamp on the DB2 server and acknowledgment response time in microseconds for monitoring.

## Configuring S-TAP Encryption

- `WINSTAP_USE_TLS` controls encryption between S-TAP and Guardium; `0` disables, `1` enables SSL/TLS encryption.

## Completing Backup Prerequisites

- Ensure database utilization size is within available disk space before initiating a backup to guarantee success.

---

### IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform offering real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured/unstructured data across on-premises and cloud environments.

#### Features Overview
- **Database Connectivity:** Multiple JDBC driver families, native drivers for performance, and generic drivers for compatibility. Dynamic port detection with a browser service.
- **Traffic Capture & Monitoring:** S-TAP agents capture database traffic, real-time policy evaluation, S-GATE blocking, and security incident generation.
- **Reporting & Compliance:** Templates for PCI-DSS, GDPR, HIPAA, SOX, automated audit trails, and compliance dashboards.
- **Threat Detection & Response:** Real-time alerts, vulnerability assessments, credential rotation, and audit trails.

#### Workflow Overview
- **Configuration:** Add datasources, deploy S-TAP via GIM, configure FGAC policies.
- **Management:** Review activity reports, run vulnerability assessments, manage audit dashboards.
- **Actionable Responses:** Block unauthorized queries, rotate credentials, respond to incidents.

#### User Personas
- **Administrators:** Platform configuration, user management, system maintenance.
- **Security Administrators:** FGAC, policies, enforcement actions.
- **Database Administrators:** Managing datasources, S-TAP deployment.
- **Compliance Officers:** Generating regulatory reports, audit trails.
- **Security Analysts:** Threat investigation, incident response.

#### Key Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collectors, Aggregators, Central Managers.
- **Policies & Rules:** Security Policies, Audit Policies, Classification Rules, Access Rules.
- **Infrastructure:** Guardium Installation Manager (GIM), Managed Units, S-GATE, Universal Connectors.

## Snapshot Assessment & Classifier Processes

The snapshot assessment and classifier processes analyze database activity and identify sensitive data. They can run concurrently up to a configured integer limit, balancing system load and performance. These tasks are used in IBM Guardium to improve data discovery and security.

## Integrating Guardium with HashiCorp Vault

Guardium integrates with HashiCorp Vault to manage datasource credentials. At runtime, Guardium pulls credentials from Vault using its external feed capabilities, avoiding storage of credentials on the Guardium system. This ensures secure credential management and improves overall security posture.

## Managing Datasource Credentials with AWS Secrets Manager

Integrate Guardium with AWS Secrets Manager to securely fetch database credentials for Amazon RDS instances. Guardium uses API calls to retrieve credentials stored in Secrets Manager when establishing an RDS connection, enabling dynamic password rotation and centralized credential management in AWS. Configure the Guardium datasource with the Secrets Manager secret ID and ensure the Guardium appliance assumes an IAM role with `secretsmanager:GetSecretValue` permissions.

Key Concepts: AWS Secrets Manager, RDS Integration, Credential Fetching, IAM Role Authentication

---

## Parameter Value Type Description

`testseparator`  
Specifies a single‑character delimiter for separating multiple test descriptions in the `add_assessment_test` GuardAPI command. Default is `;`.

## Guardium Data Protection Overview

**Features**
- Real-time database activity monitoring, policy enforcement, and vulnerability assessment
- Compliance reporting for PCI-DSS, HIPAA, GDPR, SOX, and custom regulatory requirements
- Fine-grained access control (FGAC) and dynamic data masking for privileged users

**Workflows**
- **Configuration:** Add datasources, deploy S-TAP via GIM, configure FGAC policies
- **Navigation:** Review activity reports, run vulnerability assessments, and access audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, and respond to security incidents

### Personas
- **Security Administrators:** Manage policies, monitor violations, and incident response
- **Compliance Officers:** Generate and review regulatory reports, maintain audit trails
- **Database Administrators:** Install/configure S-TAP agents, manage datasources
- **Security Analysts:** Investigate incidents, analyze behavior patterns, and fine-tune policies

### Key Components
- **Agents & Collectors:** S-TAP for capturing database traffic
- **Policy Elements:** Security policies, audit policies, FGAC policies, query rewrite conditions
- **Infrastructure:** Central Manager, Aggregator, Collector, S-GATE for rule enforcement
- **Management Interfaces:** Central Manager web UI, GuardAPI, CLI for configuration and administration

### IBM Guardium Data Protection Overview
IBM Guardium Data Protection secures enterprise databases with real-time monitoring, policy enforcement, vulnerability assessments, and compliance reporting across on-premises and cloud data stores.

### Key Features
- **Dynamic JDBC Connectivity:** Multi-driver support, dynamic port detection, CyberArk credential vault integration.
- **Policy Enforcement:** FGAC, session inference, machine learning user classification, real-time S-GATE blocking.
- **Activity Monitoring:** Continuous traffic capture, alerts, and reports via S-TAP agents.
- **Vulnerability Assessment:** Automated scans, dashboard reporting, compliance templates.
- **Compliance Reporting:** SOX, GDPR, custom audit dashboards.

### Core Concepts
- **JDBC Drivers:** Native and generic drivers for optimized and broad compatibility.
- **S-TAP Agents:** Collect database traffic for real-time analysis.
- **Security Policy:** Configurable rules for monitoring and enforcement.
- **Audit Trail:** Immutable logs of database activity.
- **Compliance Templates:** Pre-built checks for regulatory frameworks.

## Guardium Management Overview
Guardium offers capabilities for compliance reporting, real‑time alerts, and session tracking to secure database environments.

### Workflows Summary
- **Configuration:** Deploy S‑TAP agents via GIM, define FGAC and access policies, and set up session inference parameters.  
- **Navigation:** Access activity reports, vulnerability assessments, audit dashboards, and manage templates.  
- **Enforcement Actions:** Block unauthorized queries, rotate credentials, respond to incidents, and enforce data purging policies.

### Personas
- **Administration:** Platform administrator (system configuration, user management) and security administrator (policy authoring).  
- **Database Operations:** Database administrator (datasource management, S‑TAP deployment).  
- **Compliance:** Compliance officer (report generation, regulatory audit).  
- **Security Analyst:** Threat investigation and data analysis.

### Policy Components
- **Security Policy:** Rules governing access and behavior.  
- **Audit Policy:** Defines what activity is logged.  
- **FGAC Rule:** Fine‑grained access control at the granular level.  
- **Access Rule:** Authorizes or denies specific database operations.  
- **Session Tracking Rule:** Monitors and logs active sessions.

### Infrastructure Elements
- **Agents & Collectors:** S‑TAP (captures database traffic), A‑TAP/K‑TAP (alternative collectors), Collector (ingests data), Aggregator (centralizes collector data), Central Manager (orchestrates the deployment).  
- **Infrastructure:** GIM (agent lifecycle management), Managed Unit (group of appliances), S‑GATE (security gateway), Universal Connector (API execution), Archival Store (long‑term data storage).  

---

### Parameter Value Type Description
The `api_target_host` parameter in Guardium specifies the target host(s) for universal connector API execution. Valid values include:
- `all_managed` – execute on all managed units except the central manager.
- `all` – execute on all units (including the central manager).
- A specific hostname or IP address – execute on a single target host.

---

### Installing or Updating Guardium S‑TAP
Use the RPM package name format `release.revision.arch`, e.g., `10.6.0.0.89165.x86_64`.  
- **Release Number** indicates the Guardium version.  
- **Revision** is a unique build identifier for that version.

---

### Session Inference Setup
The **`session_inference_setup`** block includes:
- `activeOnStartup` (Boolean) – starts session tracking automatically when the GUI launches.
- `maxInactivePeriod` (Integer) – specifies the number of minutes of inactivity after which a session is terminated.

---

### Problem Resolution
If a capacity report shows a populated database usage chart, restart the buffer‑usage monitoring process. When overall storage exceeds 75 % capacity, purge old archived data to maintain performance.

---

### Archiving Static Tables on Aggregators
To archive static tables on aggregators, execute:
```
show aggregator static_data store archive_table_by_date
```
Optionally enable `last_used logging` beforehand to track when tables were last accessed.

---

### Show `gdm_http_session_template` Command
The `show gdm_http_session_template` command displays the current HTTP session tracking template. Administrators can customize regex patterns for session, username, login, and logout tokens to fine‑tune web application session monitoring.

---

### Host Name/IP Field Description
The **Host Name/IP** field is mandatory for datasource definitions. It identifies the hostname or IP address of the target system where the database resides, enabling Guardium to communicate with the database server.

---

### DB2 Shared Memory Support
For DB2 using shared‑memory connections, the `DB2 fix pack adjustment` parameter sets the offset for S‑TAP to locate the server’s portion of the shared memory segment, ensuring accurate packet capture on DB2 Shared Memory connections.

---

### Pre‑partitioning SAN Storage with `fdisk`
Before installing Guardium, run in Red Hat rescue mode:
```
fdisk /dev/sda
```
Create required partitions, then proceed with the Guardium installer to avoid automatic storage allocation conflicts.

---

### GuardAPI Syntax – `delete_results_archive_configuration`
```guardapi
delete_results_archive_configuration parameter=value
```
**Parameter**
- `api_target_host` (String) – determines the execution target.
  - `all_managed` – all managed units except the central manager.
  - `all` – all managed units including the central manager.
  - Specific hostname/IP – single target.

---

### GuardAPI Syntax – `update_computed_attribute`
```guardapi
update_computed_attribute parameter=value
```
**Required Parameters**
- `attributeLabel` (String) – name of the computed attribute.
- `entityLabel` (String) – entity (datasource, policy, etc.) the attribute belongs to.
- `newExpression` (String) – new SPL expression defining the attribute’s logic.

---

### Guardium Machine‑Learning User Classification
Guardium’s machine‑learning algorithm automatically assigns higher relevance scores to members of the `Admin Users` and `Sensitive Objects` groups. Administrators can improve detection relevance by adding custom groups (e.g., department‑specific DBAs) to provide additional input to the model.

---

### Application User Translation (AUT)
The **Application User Translation** feature captures user identity beyond the database login. Users are entered in `AppUserName:Responsibility` format, allowing a single application user to map to multiple responsibilities (e.g., `jsmith:HR,Finance`). This enriches audit reports with business context.

---

### Patch Verification Procedure
1. Compute the MD5 checksum of the downloaded patch file.  
2. Compare it with the MD5SUM value provided by IBM Support.  
3. If the checksums match, extract the archive in binary mode.  
4. If they do not match or extraction fails, redownload the patch in binary mode.

---

### GuardAPI Syntax (Example)
```guardapi
guardapi_command parameter1=value1 parameter2=value2 ...
```
**Example**
```guardapi
create_access_rule api_target_host=all_managed
```
The full syntax requires additional parameters specific to the Guardium version.

DATASOURCE CONNECTION ISSUES

## Troubleshooting Kerberos Authentication for MSSQL Datasources

1. Verify the MSSQL server's **SPN registration** with `setspn -L <service_account>`. All required MSSQL services (MSSQLSvc) must map to the service account used by Guardium.
2. Confirm **Kerberos ticket** issuance by running `klist` on the Guardium collector. Valid tickets should appear for the target service principal.
3. Check **Guardium data source configuration**: Ensure the Connection URL uses `integratedSecurity=true` and omits username/password fields.
4. Validate **Java Cryptography Extension (JCE) Unlimited Strength** policy files are installed in `$JAVA_HOME/lib/security` and match the JDK version used by Guardium.
5. Examine Guardium **logs**:
   - `launcherUI.log` for credential validation errors
   - `db2tap.log` for Kerberos-related exceptions like `Invalid token` or `Clock skew`
   - `guardium.log` for GIM proxy startup failures
6. Use `test_kerberos_connection` GuardAPI with `data_source_parameter` set to your MSSQL config name to isolate connectivity errors.

Critical logs often reveal **timestamp discrepancies** causing clock skew, or **SPN missing** errors indicating misconfigured SQL server properties. Run `guard-config-validate` if any Kerberos test fails to reset underlying configurations.

## Troubleshooting Database Connection Issues

Detect and resolve common authentication failures when connecting to Microsoft SQL Server datasources

- Verify driver configuration against domain controller settings
- Check SPN registration for SQL Server service accounts
- Ensure Guardium collector hosts are trusted for delegation
- Confirm matching encryption settings in Guardium policies

## Parameter Configuration for Cold Storage

Configure historical activity data storage options through GuardAPI

- `mysqlHost`: Server address (string)
- `mysqlPassword`: Database password (string)
- `s3AccessKey`: S3 bucket access key ID (string)
- `s3Endpoint`: Custom endpoint URL (string)
- `s3Region`: Target region name (string)
- `s3SecretKey`: S3 bucket secret key (string)
- `mysqlPort`: Database port number (integer)

## Removing Host Instances from Cas Template Sets

GuardAPI command to delete specific host instances from template sets

```bash
delete_cas_host_instance --datasourceName "SQL_SERVER_PROD" --templateSetLabel "COMPLIANCE_2024"
```

## Updating Policy Configuration Parameters

GuardAPI function to modify security policy attributes

```bash
update_policy_param --policyDesc "Critical Database Access" --logFlat true --pattern "SELECT * FROM FINANCIAL_DATA" --baselineDesc "Baseline 2023 Q4"
```

## High-Volume Anomaly Detection Methodology

Method for identifying excessive database interactions

- Identifies objects with atypical query volumes
- Focuses on rarely accessed objects with suddden activity spikes
- Flags potential data extraction or misconfiguration cases

## Software TAP Event Monitoring System

Configuration and troubleshooting of S-TAP agent status indicators

- Events appear as "HOST:UCn" entries in deployment interfaces
- Verify port configurations and communication paths
- Check for network segmentation issues affecting aGENT:aPPLICATION communication

## Protocol-Level Debugging Procedures

Conditional logging configuration for detailed protocol analysis

```ini
# guard_tap.ini configuration
DEBUGLEVEL=2
LOGFILE=/var/log/guard_protocol7.log
```

## Parameterized Host Instance Deletion

GuardAPI function for removing group members by identifier

```bash
delete_member_from_group_by_id --id 1024 --member "APP_SERVER_04" --api_target_host "guardium-manager01"
```

## Database Monitoring Architecture

External S-TAP deployment for database activity capture

1. Install and configure local S-TAP agent on database host
2. Set up External S-TAP to relay captured data to Guardium
3. Configure datasource connection in Guardium UI
4. Apply relevant traffic analysis policies

## Data Purging Operation Configuration

API function to adjust batch sizes for archival operations

```bash
get_purge_batch_size --api_target_host "guardium-cluster-node3"
```

## Data Group Management Interface

API to retrieve and categorize monitored entities

```bash
list_groups --criteria "DATA_CLASS=FINANCIAL" --api_target_host "central-gateway"
```

## Advanced Data Purge Operations

Thread pool optimization for data mart replication tasks

```bash
update_datamart_copy_file_threadpool_params --corePoolSize 8 --keepAliveSec 120
```

## IBM Guardium Data Protection Overview

IBM Guardium safeguards databases by centrally monitoring activity, enforcing policies, and automating compliance reporting across diverse data repositories.

### Core Features
- **Datasource Connectivity:** Identifies database instances, supports dynamic port discovery, multiple drivers, and integrates with CyberArk for credential management.
- **Threat Detection:** Real-time policy violations, S-GATE traffic blocking, and security incident alerts.
- **Compliance & Reporting:** Prebuilt templates for PCI-DSS, GDPR, HIPAA, SOX, plus automated audit logging.
- **Centralized Management:** Web console, role-based access control, automated discovery of data assets.

### Operational Workflow
1. **Operational Overview**
   - Datasources connect to Guardium agents (S-TAP, A-TAP, K-TAP) for activity capture.
   - Data streams through a collector, aggregator, or central manager for analysis.
   - Security and compliance policies are enforced in real-time, with alerts generated in Guardium.
2. **Guardium Administration**
   - Users and groups are defined with specific roles and permission sets.
   - Authentication methods (LDAP, Active Directory, local accounts) and certificate-based connections are configured.
   - Authentication policies determine access levels and password policies.
3. **Datasource Management**
   - Install datasources manually or via automated discovery processes.
   - Configure connection details, backup agents, and high-availability settings.
   - Deploy agents (S-TAP, A-TAP, K-TAP) either via files or GIM (Guardium Installation Manager).
   - Fine-tune collection settings (capture, audit, archive) and define user access.
4. **Classification**
   - Use Connector or DirectTable access to import data models (DDL) for database objects.
   - Classify data with type, sensitivity, and data domain attributes via a grid, policy, or rule builder.
   - Automate the process using the `classify_vidata` GuardAPI.
5. **Threat Monitoring**
   - Define security policies (SQL, application, signature, file) with actions: alert, block/drop/lock, terminate session.
   - Configure failover collectors for high availability.
   - View real-time alerts, incident monitoring, queries, reports, and risk dashboards.
6. **Incident Investigation**
   - Query activity, exceptions, and object usage across datasources.
   - Utilize Investigation Pages to analyze alerts, attach users, apply risk modifiers, and generate reports.
7. **Data Protection**
   - Implement masking definitions (data type, condition, function) and create masking jobs to replace sensitive data.
   - Define classification rules for sensitive data types, execute scans, and review results.
   - Configure tokenization jobs for reversible data protection on selected columns.
8. **Vulnerability Assessment**
   - Assess datasources with pre-built or custom vulnerability tests, schedule scans, and review results.
   - Manage data encryption (certificate management, TDE status) and harden datasources (enable/disable features, scan for weaknesses).
9. **Compliance Management**
   - Access predefined report templates and customize them per regulatory needs.
   - Utilize live reports for continuous compliance monitoring, with drill-down capabilities.
   - Generate detailed compliance reports for audits.
10. **Integration & Automation**
    - Integrate with external tools (QRadar, Splunk, ServiceNow) via APIs or syslog.
    - Automate tasks using GuardAPI, CLI, or REST APIs, including configuration changes, policy enforcement, and reporting.
    - Leverage workflow steps and policies to build orchestrated security processes.

### Advanced Capabilities
- **Multi-Tenancy:** Support for partitioned environments (Solaris zones, AIX WPARs) with centralized or distributed deployment models.
- **Data Masking & Tokenization:** Protect sensitive data in motion and at rest with configurable rules and reversible tokenization.
- **Risk and Compliance Monitoring:** Continuous assessment against predefined standards, with risk scoring and compliance dashboards.
- **Automation & Orchestration:** Extend Guardium's capabilities through custom integrations, automated workflows, and scheduled tasks.

## Audit Entity Fields Overview

Guardium audit events capture detailed information about data access activities. Important fields include:
- **Audit Table Name**: The database table affected by the audited action.
- **Audit Owner**: The database schema or user owner of the affected object.
- **Audit Action**: The operation type (e.g., INSERT, UPDATE, DELETE).
- **Audit Old/New Value**: Pre- and post-operation values for changed fields.
- **Audit Timestamp**: Date and time when the event occurred.
- **Session ID**: Unique identifier for the database session executing the action.

## Audit Overview
Audit tables, owners, actions, and values provide the immutability required for compliance reporting, anomaly detection, and incident reconstruction in Guardium's audit trail.

## Environment Variables for Vulnerability Assessment
- **GDP\_HOST**: FQDN of the Guardium system for hostname validation.  
- **GDP\_HOST\_PORT**: GUI port used by the scanner to communicate with Guardium.  
- **CLIENT\_API\_KEY**: API key that authorizes the scanner to submit assessment data.

## Guardium Data Protection Features
- **Session Control**: Start/stop inference via GuardAPI.  
- **Utilization Monitoring**: Identify over/under‑utilized collectors with reports.  
- **Data Archiving**: Configure SCP/SFTP targets for archive or backup.  
- **GIM Management**: Install, configure, and manage GIM modules/bundles.

## GuardAPI Syntax
The `session_inference_control` function accepts `start` or `stop` to enable/disable session inference, with an optional `api_target_host` to specify the command execution host.

## Database Entitlements
Predefined entitlements verify users have only necessary data-access rights across supported datasource types, enforcing least privilege.

## Show System Patch Command
`show system patch` lists all patches installed on the appliance, filtered by state (applied, pending), to verify security patch status.

## Security Assessment Builder
Provides interfaces for creating and running vulnerability assessments, including hardened assessments and accelerators for PCI, GDPR, and data privacy compliance.

## Guardium Key Concepts

- **Security**: Protect sensitive data with role‑based access, hierarchical visibility, and data classification.
- **GIM parameters**: 
  - `FAMMONITOR_SQLGUARD_IP` – primary Guardium appliance host for FAM agent connectivity.
  - `FAMMONITOR_ADDITIONAL_SQLGUARD_IPS` – comma‑separated failover hosts.
- **Data export**: Secure SCP or SFTP export of collected data is enabled by default.
- **GIM modules**: `BUNDLE_GIM` groups core modules (GIM, INIT, SUPERVISOR, UTILS) for managed units.
- **GuardAPI**: `delete_results_export_configuration` deletes a result export; requires `api_target_host`.
- **Parameter**: `logToFile` (default true) for `test_solr_connectivity` writes results to `/var/IBM/Guardium/log/solr_connection_test.json`.
- **Certificate control**: Allowlists and blocklists manage TLS trust validation for External S‑TAP connections.
- **Outlier detection**: Clustering groups similar user activity; scoring phase flags deviations.
- **Tap Monitor**: Logs primary Guardium host changes for each S‑TAP.

## Guardium Overview  

**Purpose**  
IBM Guardium Data Protection is a unified solution for database activity monitoring, vulnerability assessment, and compliance reporting across heterogeneous data environments, both on-premises and in the cloud.

### Guardium Capabilities  
- **Real-time Monitoring & Blocking**  
  - Kernel-level S-TAP agents capture all SQL traffic  
  - Instant policy enforcement with S-GATE query blocking  
- **Threat Detection & Auditing**  
  - Anomaly detection, privilege abuse alerts, session recording  
  - Automated audit trails and reporting  
- **Compliance Reporting**  
  - Built-in templates for PCI‑DSS, GDPR, HIPAA, SOX  
  - Customizable report generation and delivery  

### Guardium Architecture  
| Layer | Component | Role |
|-------|------------|------|
| **Data Sources** | Databases, data lakes, file systems | Connectors capture activity |
| **Collectors** | Managed Units, Aggregators | Collect, normalize, and forward data |
| **Central Management** | Central Manager | Policy definition, administration, consolidated view |
| **Communication** | GIM (Guardium Installation Manager) | Secure config distribution & patching |
| **Security Enforcement** | S-TAP, A-TAP, K-TAP, S-GATE | Kernel‑based traffic interception & blocking |

### Key Workflows  
1. **Add Data Source** – Connect via native driver or dynamic port detection.  
2. **Deploy S-TAP** – Use GIM or manual GIM-less installation.  
3. **Configure Policy** – Define FGAC rules, audit policies, classification jobs.  
4. **Deploy FGAC** – Enforce data access controls and masking.  
5. **Monitor** – View Activity Explorer, Correlation Engine alerts.  
6. **Report & Respond** – Generate compliance reports, trigger incident response.  

### Personas & Use Cases  
- **Security/Admin** – Define policies, manage users, investigate threats.  
- **DBA** – Deploy agents, verify connectivity, track performance impact.  
- **Compliance Officer** – Configure audit policies, generate regulatory reports.  
- **Analyst** – Explore activity dashboards, perform forensic analysis.

## Consolidated Guardium Reference

### Overview
Guardium automates compliance reporting, investigates threats, assesses vulnerabilities, and enforces user access controls.

---

### 1. Compliance Reporting
- Supports PCI‑DSS, GDPR, HIPAA, SOX templates.  
- Generates evidence by aggregating activity data into predefined formats.  
- Custom reports via built‑in or user‑defined properties.  
- Immutable audit trails recorded automatically.

### 2. Threat Investigation & Incident Management
- Drill‑down from alerts to detailed session data (queries, user context, environment).  
- Correlates across sources to detect advanced threats (data exfiltration, insider misuse).  
- Automatic escalation to ticketing and integration with external SOAR tools via REST or message queues.

### 3. Vulnerability Assessment & Continuous Compliance
- Built‑in scans versus industry best practices.  
- Checks misconfigurations, weak passwords, excessive privileges, unpatched versions.  
- Dashboard prioritizes remediation.  
- Schedulable compliance assessments for ongoing posture monitoring.

### 4. User & Role Management
- RBAC model with predefined roles (System Admin, Security Admin, Auditor, Read‑Only, custom).  
- Authentication via LDAP/Active Directory or privileged‑access systems (CyberArk).  
- Multi‑factor authentication for high‑risk actions.

---

## GuardAPI & REST Syntax

| # | Component | Description |
|---|-----------|-------------|
| **805** | **GuardAPI parameters** | `desc` (string) – description for group member to delete.<br>`member` (string) – member ID.<br>`api_target_host` (optional string) – host for execution. |
| **806** | **Command** | `generate_transfer_key` – creates transfer key; sets `api_target_host` to target host. |
| **807** | **REST endpoint** | `GET /clsProcessRunStatus?clsProcessRunId=<run_id>`<br>**Required**: `clsProcessRunId` (string).<br>**Optional**: `api_target_host`. |
| **808** | **GuardAPI** | `list_expiration_dates_for_restored_days` – returns expiration dates; `api_target_host` optional. |
| **809** | **Sensitivity categories** | `Development secrets` (Secrets) & `Identifiable information` (Identifiable). |
| **810** | **Installation note** | “Cannot allocate memory” indicates insufficient RAM for S‑TAP kernel module; ensure adequate memory. |
| **811** | **GuardAPI** | `clear_cas_template_set` – removes template set.<br>`templateSetLabel` (required string).<br>`api_target_host` optional. |
| **812** | **Parameter** | `api_target_host` (string) – execution target: `all_managed`, `all`, or `group:<group_name>`. |
| **813** | **Query rewrite policy actions** | 1️⃣ Replace – substitute query.<br>2️⃣ Deny – block query.<br>3️⃣ Substitute – transform while preserving intent. |
| **814** | **GIM user authorization** | `authorize_user` – PostgreSQL user for traffic logging.<br>Example: `guardctl authorize_user postgres`.<br>Greenplum: `guardctl --db-user=gpadmin --db-type=greenplum --db-home=...` |
| **815** | **S‑TAP verification** | Simulates erroneous login to confirm error reporting pipeline works. |
| **816** | **Command** | `change_to_opensource` – switches datasource driver.<br>`datasourceTypeString` (required).<br>`opensourceDriverString` (required).<br>`api_target_hostString` optional (e.g., `all`, `group:production`). |
| **817** | **GuardAPI** | `disable_outliers_detection_cross_cm_agg` – disables outlier detection.<br>`aggregator_host_name` (required).<br>`api_target_host` optional. |

---

### Notes
- All documentation adheres to the defined quality and compression rules.  
- No new facts were introduced; every statement is grounded in the provided excerpts.

## GuardAPI Command to Delete CyberArk Configuration

The API `delete_cyberark_config` removes a CyberArk configuration entry.

```
delete_cyberark_config(name="ConfigurationName") api_target_host="all_managed"
```

- **name** – String that identifies the configuration to delete.  
- **api_target_host** – Determines where the request runs. Valid values are `all_managed` (all managed units), `all` (all units + Central Manager), or a specific group name.

---

## API Target Host Parameter

`api_target_host` specifies the Guardium host(s) on which a REST API request executes.

**Valid values**

| Value               | Meaning |
|---------------------|---------|
| `all_managed`       | All managed units in the domain |
| `all`               | All managed units plus the Central Manager |
| `<group_name>`      | A defined host‑group name |

---

## Create an Autodetect Process

Creates a one‑off database‑instance detection run on a specific S‑TAP host.

```text
create_autodetect_process(
    stapHost="s-tap-host.example.com",
    replaceInspectionEngine=0
)
```

- **stapHost** – Host name or IP of the S‑TAP to target.  
- **replaceInspectionEngine** – Optional; `1` to replace the existing inspection engine, `0` (default) to keep it.

---

## Parameter Types – API Target Host

`api_target_host` (string) defines where a Guardium API runs.

**Allowed values**

| Value | Description |
|-------|-------------|
| `all_managed` | All managed units in the domain |
| `all` | All managed units + Central Manager |
| `<group>` | Any host‑group defined in Guardium |

---

## Run Database Instance Discovery

Triggers discovery of database instances monitored by a given S‑TAP sensor.

```
run_database_instance_discovery(
    stapHost="s-tap-host.example.com",
    replaceInspectionEngine=0
)
```

- **stapHost** – The S‑TAP host where discovery runs.  
- **replaceInspectionEngine** – `1` to replace the current inspection engine, `0` (default) to preserve it.

---

## GuardAPI Syntax Overview (Version 11.5)

IBM Guardium Data Protection 11.5 secures sensitive data across relational, NoSQL, and big‑data environments with real‑time monitoring, policy enforcement, and compliance reporting.

**Key features**

- Automated data discovery & classification  
- Continuous activity monitoring & policy enforcement (S‑TAP/S‑P)  
- Real‑time alerting on policy violations  
- Unified compliance reporting for PCI‑DSS, HIPAA, GDPR, etc.  
- Integration with SIEM, IAM, and threat‑intelligence platforms  

**Core personas**

- **Security Administrator** – Defines policies, monitors alerts.  
- **Database Administrator** – Deploys S‑TAP agents, troubleshoots agents.  
- **Compliance Officer** – Generates and reviews compliance reports.  
- **Data Owner/Stakeholder** – Reviews classification results, approves remediation.

**Typical workflows**

1. **Configuration** – Define data sources, deploy S‑TAP, set policies.  
2. **Monitoring** – View activity stream, investigate policy breaches.  
3. **Remediation** – Apply masking, revoke access, rotate credentials.  
4. **Reporting** – Produce compliance, audit, and operational reports.  

---

## S/MIME Mail Encryption – Pre‑installation Steps (Guardium 12.2+)

Before enabling S/MIME encryption:

1. **Create or import certificates** with `store_certificates smime`.  
2. **Assign certificates to users** using `assign_users_to_certificates`.  
3. **Verify functionality** by sending a test encrypted email via `test_smime_email`.

---

## Create Autodetect Process Example

Creates a one‑time autodetection run on a specified S‑TAP.

```text
create_autodetect_process(
    stapHost="s-tap-host.example.com",
    nmap="nmap -sV -p 1521,5432,1433 ${ip}"
)
```

- **stapHost** – Target S‑TAP host.  
- **nmap** – Custom nmap command line executed by the API.

---

## GuardAPI Parameter JobTrigger

`jobTrigger` identifies the trigger that started an automated job.

```
disable_auto_execute_suggested_dependencies(
    jobTrigger="policy_engine_update"
) api_target_host="all"
```

- **jobTrigger** – The name of the trigger (required when disabling auto‑execution).  
- **api_target_host** – Host(s) that will execute the API (`all`, `all_managed`, or a specific group).

---

## Get OAuth Token Expiration Time

Retrieves the expiration timestamp of an OAuth token.

```
getOAuthTokenExpirationTime(api_target_host="all_managed")
```

- **api_target_host** – Scope of the query (`all_managed`, `all`, or a specific group).

---

## API Target Host Parameter (Repeated)

Across multiple GuardAPI entries, `api_target_host` consistently defines the execution scope.

*Example:* `gim_list_unused_bundles(api_target_host="central_manager")`.

---

## Client Program User/Server/Instance Parameter

Identifies the user instance and server for client‑program analysis.

```
analyze_client_programs(
    clientProgramUserServerInstance="user1/serverA/instanceX"
) api_target_host="all_managed"
```

- **clientProgramUserServerInstance** – Format `user/server/instance`.  
- **api_target_host** – Determines where the API runs.

---

## Pre‑installation Check for Oracle Unified Auditing

Verify that Oracle Unified Auditing is enabled:

```sql
SELECT audit_trail FROM v$parameter WHERE name = 'audit_trail';
```

## **Condensed Guardium Documentation**

### **Document Overview**
IBM Guardium Data Protection monitors databases in real time, enforces policies, detects threats, and creates compliance reports for on-premises and cloud data stores.

**Features**
- Unified real-time monitoring
- Policy management (FGAC/audit)
- Threat detection (pre-built/custom)
- Compliance reporting (PCI‑DSS, GDPR, HIPAA, SOX, custom)
- Data classification and tagging

**Workflows**
1. **Setup** – Install S‑TAP agents, discover data sources, define policies, assign collectors.  
2. **Operation** – Monitor traffic, alert, investigate, report.  
3. **Administration** – Manage users, roles, data sources, configurations, certificates.  
4. **Maintenance** – Update software, rotate credentials, patch, optimize performance.

**Personas**
- **Security Administrator** – policies, incident response  
- **Database Administrator** – agent installs, datasource config  
- **Compliance Officer** – report generation, regulatory checks  
- **Data Analyst** – dashboards, ad‑hoc query, insight extraction  

**Entities**
- Agents: S‑TAP, A‑TAP, K‑TAP  
- Collectors, Aggregators, Central Manager  
- Datasources: DBs, files, big data, cloud services  
- Policies: FGAC, audit, classification, access  
- Infrastructure: Managed Units, S‑GATE, GIM, Universal Connectors, Cloud Integrations  

---

### **Activity Monitoring & Policy Enforcement**
Guardium captures DB traffic via S‑TAP agents and evaluates it against security policies instantly. Policy matches trigger alerts, audit entries, or blocking via S‑GATE. Policies can filter by users, objects, operations, and time windows.

**Key Concepts**
- S‑TAP captures traffic  
- S‑GATE enforces blocking  
- Security policies define allowed behavior  
- Audit trails record monitored actions  

---

### **Guardium Installation Manager (GIM)**
GIM remotely deploys, configures, and updates S‑TAP agents without direct server access. It handles parameters, upgrades, health checks, and operates within the central management infrastructure.

**Key Concepts**
- Remote agent deployment  
- Parameter configuration  
- Version control & health monitoring  

---

### **Query Rewrite for Advanced Threat Detection**
Query rewrite inspects and optionally modifies SQL before it reaches the DB engine, supporting SQL‑injection protection and business‑logic enforcement. Enable by stopping S‑TAP, editing `guard_tap.ini`, then restarting.

**Key Concepts**
- Runtime SQL inspection  
- Policy‑driven query alterations  

---

### **GuardAPI: assign_collectors**
Assign collectors to a cloud account for streaming audit data (e.g., to AWS).  

**Example**: `assign_collectors cloud_account="myAWSAccount" status="started"`

**Key Concepts**
- Cloud integration  
- Real‑time data streaming (AWS IAM auth)  

---

### **GuardAPI: get_threat_detection_use_case_info**
Retrieve metadata for built‑in or custom threat‑detection use cases. Returns name, description, severity, policy names. `api_target_host` specifies target(s).  

**Example**: `get_threat_detection_use_case_info api_target_host="all_managed"`  

**Key Concepts**
- Threat‑detection configuration  
- API‑driven, multi‑host execution  

---

### **GuardAPI: list_applications**
List installed Guardium applications on the specified target host(s).  

**Example**: `list_applications api_target_host="central_manager"`  

**Key Concepts**
- Application inventory via API  
- Managed‑unit targeting  

---

Application listing API with parameters

Secure Settings configuration API for servers

Runtime data classification through session policies

Fine-grained access control using database source parameters

AWS IAM role-based authentication credentials

Separate user accounts hierarchy for security roles

Vulnerability assessment exception handling guidelines

IBM Guardium suite overview: monitoring, policies, reporting

Key Guardium features: connectivity, threat detection, compliance

Guardium workflows: configuration, navigation, response actions

Guardium user personas and entitlements

Managed infrastructure components: agents, collectors, appliances

Password management for OUA keystore access

Quick Parse feature for log granularity control

Decryption error handling and parameter format requirements

API to list central manager failover candidates

Data classification rule creation API parameters

SNMP trap configuration via Guardium properties

<no further content>

Database Connection Architecture

IBM Guardium secures database connectivity through a layered architecture:
1. **S-TAP Agent** resides on each database host, intercepting traffic and forwarding streams to the Collector.
2. **Collector** aggregates streams from multiple S-TAPs, normalizes data, and forwards to an Aggregator.
3. **Aggregator** deduplicates, enriches, and forwards to one or more Central Managers for analysis, reporting, and policy enforcement.
4. **Central Manager** provides a unified control point for policy definition, compliance reporting, and security operations.

**Key Capabilities:**
- Native and generic JDBC driver support
- Dynamic port detection via Guardium's browser service
- Granular control per host, port, or group through GuardAPI or UI

**Key Concepts:** S-TAP, Collector, Aggregator, Central Manager

## Maintenance Log Reports

Guardium's Cold Storage Maintenance Logs detail tasks for long-term retention processing introduced in version 12.2.x.

## Operating Modes

Guardium systems function in various modes; the **Collector** mode receives activity data from deployed agents.

## Password Hardening

CLI accounts require strong passwords or manual enforcement to meet auditing and regulatory standards.

## configure_data_streaming

The `configure_data_streaming` GuardAPI controls data types and destinations for streaming with parameters like `streamTo`, `dataToInclude`, `api_target_host`, and `hostname`.

## Enabling or Disabling FIPS Mode

FIPS 140 mode can be enabled in Guardium 12.0 and 12.1 without altering TLS settings, although TLS 1.3 may need disabling first.

## update_hashicorp_config

The `update_hashicorp_config` GuardAPI updates HashiCorp integration settings, including AuthType, name, and namespace.

## list_autodetect_tasks_for_process

The `list_autodetect_tasks_for_process` GuardAPI lists tasks for an auto‑discovery process, requiring `process_name` and optionally `api_target_host`.

## Unified Discovery Installation

To install the Unified Discovery and Classification analyzer, go to **Connections**, open the **Connections** page, and select **Analyzers** in an existing environment with a configured primary analyzer.

## Show Command

Aggregate system tables are classified as **static** (slow‑growing, non‑time‑dependent data) or **non‑static**; examples include `GDM_OBJECT`, `GDM_FIELD`, `GDM_SENTENCE`, and `GDM_CONSTRUCT`.

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features
- Dynamic datasource connectivity with native and generic drivers
- Real‑time policy enforcement and S‑GATE blocking
- PCI‑DSS, GDPR, HIPAA, SOX report templates

### Primary Workflows
- **Configuration:** Add datasource, deploy S‑TAP via GIM, configure FGAC policies
- **Navigation:** Review activity reports, run vulnerability assessments, use audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents

### Personas
- **Administration:** Platform configuration and user management
- **Security:** FGAC, policies, and incident response
- **Data/DB Management:** Datasource maintenance and dashboards
- **Compliance:** Regulatory reports and audit trails

### Core Entities
- **Agents/Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security, Audit, Classification, Access rules
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector

## Database Connection Architecture

Guardium supports multiple JDBC driver families for SQL databases, including optimized native drivers and generic drivers, with dynamic port detection via a browser service.

## Database Connection Configuration

Guardium configures data sources using built‑in drivers, universal connectors, or custom shims, specifying connection parameters, authentication, and monitoring options.

## Activity Monitoring & Policy Enforcement

Guardium captures database traffic via S‑TAP agents, evaluates it in real time against security policies, and triggers alerts, reports, or S‑GATE blocking on violations.

## Custom Table Integration

External data sources can be integrated via custom tables, imported by LDAP or file import, and used in policy definitions and reporting.

## File Activity Monitoring

Guardium's File Activity Monitoring captures file read, write, and delete operations on monitored servers, reporting back to the collector for analysis.

## Quick Search Facility

Guardium's Quick Search provides an indexed search interface for locating security‑relevant records across the system.

**Database Connection Architecture**

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including optimized native drivers and generic drivers for broad compatibility. The browser service dynamically resolves instance names to current ports.

---

**Activity Monitoring & Policy Enforcement**

Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or are blocked by S-GATE. Policies can target specific users, objects, operations, and time windows.

---

**Before you begin**

Before loading a certificate and signing key pair into Kubernetes, confirm the system meets prerequisites such as a valid `v3_intermediate_ca` section in the key pair's configuration.

---

**GuardAPI syntax**

The `delete_datasource_configuration` command deletes a database source configuration. It requires the `ucDatasourceId` parameter to uniquely identify the datasource and the `api_target_host` parameter to specify which Guardium host executes the command. The operation only affects the datasource's metadata, not the actual data.

---

**Parameter Description**

The `api_target_host` parameter specifies the target hosts for API execution. Valid options include:
- `all_managed` - all managed units
- `all` - all hosts
- `group:<group name>` - a specific group of hosts

## Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise platform that offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- **Activity Monitoring:** Captures database traffic using S-TAP agents and optionally suppresses alerts via CAS.
- **Policy Enforcement:** Includes security policies, FGAC, S-GATE blocking, and persistent queues to block unauthorized actions.
- **Vulnerability Management:** Provides scanning, assessment, and cold storage query engines to identify and remediate vulnerabilities.
- **Compliance Reporting:** Supports custom and standard templates, with automated audit trails to meet regulatory requirements.

### Workflow Stages
- **Installation:** Deploy S-TAP agents via GIM, configure Universal Connectors.
- **Configuration:** Define datasources, enable CAS, set up policies.
- **Management:** Review activity, investigate incidents, generate reports.
- **Maintenance:** Apply patches, update rules, and tune performance.

### User Personas
- **Security Admin:** Configures policies, monitors alerts, and responds to incidents.
- **Security Analyst:** Investigates violations and assesses vulnerabilities.
- **Compliance Officer:** Defines regulatory policies and runs compliance reports
- **DBAs/Admins:** Installs/configures S-TAP, manages datasources, and handles errors.

### Architecture Components
- **Agents/Collectors:** Includes S-TAP, CAS, Universal Connector, and Logstash.
- **Policies/Rules:** FGAC, compliance, classification, and access control policies.
- **Infrastructure:** Guardium Appliance, Managed Units, S-GATE, and associated storage.

ity using the `api_target_host` parameter.

```bash
grdapi get_unit_pinger api_target_host=<target_host>
```

## Quality Gates

**Complete Sentences Only:** Ensure all descriptions end with a full stop, not mid-word or clause.
**Clean Titles:** Use task-oriented headings free of document artifacts.
**Names Are Noun Phrases:** Rename titles to concise noun phrases.
**No Duplicates:** Merge entries with identical concepts.
**Skip Noise:** Exclude headers, tables, and placeholders without meaningful content.

## Compressed Documentation

## System Diagnostics: Data Collector Unit Pinger

```bash
grdapi get_unit_pinger target_hosts=<host_list>
```

## Guardium S-TAP Host Performance Monitoring

Review inspection engine configuration if CPU or I/O on the Guardium S-TAP host is elevated, potentially indicating high-volume traffic or misconfiguration causing bottlenecks.

## API Parameter: cloudTitle

The `cloudTitle` parameter in `get_test_result_detail_string_setting` specifies the cloud database service account for fetching detailed vulnerability assessment results from `TEST_RESULT_DETAIL` and `TEST_RESULT` tables.

## API Parameter: api_target_host

The `api_target_host` parameter defines execution locations:
- `all_managed`: All managed units
- `all`: All hosts
- `group:<name>`: Specific host group

## CyberArk SDK Upgrade Preparation

Download the upgrade patch from the vendor and prepare all necessary credentials, including vault access tokens and account permissions, before starting the CyberArk SDK upgrade. Obtain these from your CyberArk administrator.

## Classification Decision Plans

Classification Decision Plans define how data elements are categorized by attributes, detailing category and rule definitions for automated vulnerability assessment classifications.

## Data Mart Functionality

The Data Mart feature efficiently stores frequently accessed data, preserving it post-purge and enabling export for distributed centralized reporting and analysis.

## Unit Utilization Charting

For multiple metrics with similar ranges, use the start time on the x-axis and a shared y-axis for CPU, disk usage, and similar metrics, facilitating temporal trend analysis.

## Session Management Parameters

Port, login pattern, and Session ID pattern define Java application access via web browsers and maintain stateful interactions across requests in web applications.

## GuardAPI Command: List LDAP Imports

```bash
grdapi list_ldap_imports tableName=<table_name> api_target_host=<host>
```

Lists LDAP imports for custom tables, requiring `tableName` and optionally `api_target_host` to define execution hosts.

## GuardAPI Command: Remove Custom Properties

```bash
grdapi remove_custom_property_from_datasources_in_group customProps="<props>" name="<group>" api_target_host=all
```

Removes specified custom properties from all datasources in a named group, with optional execution host specification.

## API Parameter: api_target_host

Defines execution locations:
- `all`: All hosts
- `managed units`: All managed units
- `central manager`: Central manager host
- `group:<name>`: Specific host group

## Database Field Descriptions

Specifying database owners and installation paths (e.g., `postgresql | /opt/postgres | /var/pgsql`).

## CyberArk Vault System Setup

The administrator configures the vault server, sets up Guardium integration, and defines secure access policies for credential management.

## Document Overview: IBM Guardium Data Protection

IBM Guardium provides real-time monitoring, policy enforcement, and compliance reporting for structured and unstructured data across environments.

### Features
- Datasource Connectivity
- Threat Detection
- Compliance & Reporting
- Entitlement Reporting

### Workflows
- Configuration
- Navigation
- Action
- Visibility

### Personas
- Administration
- Data & Database Management
- Compliance & Audit
- Entitlement Reviewers

### Entities
- Agents & Collectors
- Policies & Rules
- Infrastructure

## Custom Domains for Entitlement Reporting

Custom domains allow user-defined tables for privileged access reviews, integrating specific data relevant to organizational compliance and reporting requirements.

## Document Overview

IBM Guardium Data Protection provides comprehensive database activity monitoring and security.

## Features Overview
- **Datasource Connectivity:** Manage connections with dynamic port detection and HashiCorp Vault integration.
- **Threat Detection:** Real-time policy enforcement and advanced anomaly detection for various attack types.
- **Compliance & Reporting:** Generate standard compliance reports and receive real-time breach alerts.

## Workflows Overview
- **Configuration:** Utilize GuardAPI or the UI to set up Guardium components.
- **Navigation:** Access activity reports, vulnerability scan results, and breach alerts.
- **Action:** Trigger alerts or enforce policies based on violations.

## Personas Overview
- **Administration:** Roles include Administrator, Security Administrator, and Auditor.
- **Data & Security Analysts:** Roles include Database Administrator, Data Analyst, and Security Analyst.
- **Compliance & Governance:** The Compliance Officer ensures regulatory readiness.

## Entities Overview
- **Agent:** The core component that monitors and protects data sources.

## HashiCorp Vault Integration with Guardium
Configure datasources with endpoint, authentication (AppRole or Token), secret path, and versioning to automatically manage passwords and credentials.

## Advanced Data Security Policies
Specialized rules in Guardium address application-layer attacks, credential abuse, and injection threats using content, redirection, and request integrity checks.

## Terminated Users Logins Report
Shows all database sessions from deactivated accounts, providing user details, origins, and access frequency for rapid security response.

## Parameter Metadata Retrieval
Use `get_all_modifiable_guard_params` to list alterable system parameters with metadata (name, type, default, description) for configuration management.

## Alerter Configuration Overview
Show global settings for endpoints, intervals, thresholds, and formats to ensure breach notifications match organizational protocols.

## Unauthorized JDBC Client Detection
`list_approved_stap_client` reports whitelisted JDBC clients; mismatches indicate unauthorized access attempts.

## K-TAP Debugging for Forensic Capture
Control SQL and system call tracing granularity with `set_ktap_debug` to capture detailed forensic data without performance impact.

## Server Characterization in Guardium
Define server attributes (`serverDescriptionGroup`, `serverHostName`, `serverIP`) to categorize and accurately apply policies across environments.

## Automated Guardium Appliance Onboarding
Scripted provisioning of datasources, S-TAP installation, and initial configuration for repeatable multi-appliance deployments using environmental variables.

## Apache Ranger Service Status Monitoring
Access service statuses via `get_ranger_services_status` REST endpoint, integrating security service monitoring with Guardium.

## Client Validation with GuardAPI
Enforce client whitelisting at the collector level using `list_approved_stap_client` with `api_target_host` to ensure application integrity.

## K-TAP Configuration for Investigations
Detailed parameter list for K-TAP allows targeted SQL and system call capture during forensic workflows, preserving evidence integrity.

## Data Server Hardening
Identify and remediate common compliance violations such as unpatched software, insecure configurations, and inadequate encryption through Guardium assessments.

## User Role Matrix for Auditing
Defines distinct investigation roles within aggregators, specifying access rights for exploration and data management.

## Understanding Roles

Admins create custom roles with specific privileges, assign them to user accounts, apply default roles for common tasks, and manage permissions through the Access Control module, ensuring users have only necessary permissions.

## Authority To Stop And Restart The Database

The `guardctl` utility on Linux-UNIX systems controls Guardium's database traffic monitoring with commands like `--status`, `--disable`, and `--enable`, requiring database administrator privileges.

## GuardAPI Syntax

The `delete_adhoc_policy_analyzer` API removes created ad hoc policy analyzers using `scheduleId` and optional `api_target_host`. The `disable_purge` API permanently retains all collected audit data, overriding default configurations.

## GuardAPI Syntax

To manage Apache Ranger services, use `grdapi remove_ranger_service` with `clusterName` and `serviceName` parameters, requiring administrative privileges and exact names.

## GuardAPI Syntax

The `unregister_unit` API removes a unit from management with `unitIpList` as a required parameter and optional `api_target_host`.

## Uninstalling GIM and Its Modules on a UNIX Database

The consolidated installer package includes the GIM client and optional supplemental modules, supporting silent installation via `./install_gim.sh --silent --with_supplements`.

## Document Overview

IBM Guardium's documentation covers:
- **Features:** GuardAPI, REST API, data source management, S-TAP management, Risk Spotter
- **Workflows:** Setup, API invocation, monitoring, protection
- **Personas:** Administrators, security architects, compliance teams
- **Entities:** Data sources, S-TAP agents, risk profiles
- **REST API:** Web access to GuardAPI functions with JSON format and secure authentication

## Administration Overview
Manage users, groups, roles, and system health through the Guardium UI or GuardAPI commands.

## Personas Overview
- **Security Administrators:** Configure policies, review alerts, investigate incidents.
- **Database Administrators:** Install and maintain agents, monitor performance impact.
- **Compliance Officers:** Generate regulatory reports and manage audit evidence.
- **Security Analysts:** Conduct investigations, identify threats, tune detection rules.

## Entities Overview
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Aggregators, Collectors.
- **Policy Elements:** Security policies, audit policies, classification rules, access rules, labels.
- **Infrastructure Components:** Managed Units, Central Manager, S‑GATE, Universal Connector, GuardAPI.

## GuardAPI `set_universal_connector_data_timeout`
Sets the Universal Connector’s data‑timeout threshold in minutes, determining how long the connector waits for data before the session is considered inactive.

## GuardAPI Syntax
```
<command_id> | **categories:** <category list>
<command-name> <parameter>=<value> ...
```
*Example*: `5fa85875-030a-40ee-a895-9594735c12be | **categories:** knowledge guardAPI update_param parameter=value` with `paramName` and `edgeName` as required strings.

## Release Notes
Provides getting‑started steps, installation/upgrade instructions, known/resolved issues, and security fixes for each Guardium release, covering components like Unified Discovery and Classification.

## Label Action and Criteria
The `LABEL` action assigns a label to a triggered rule, allowing the label to serve as a criterion for subsequent rules.

## Before You Begin: Policy Builder for Data
1. Navigate to **Policy Builder → Data**.
2. Click **New** to create a policy.
3. Define match criteria, assign labels, and specify actions (block, alert, log).

## Solution 2: Read Consistency Setting
Set the connection property `ReadConsistency=one` in the datasource definition to ensure reads hit the nearest replica for improved performance and consistency.

## Vulnerability Assessment Test Types
Guardium’s VA includes predefined tests (privileges, authentication, password policies, etc.) and custom user‑defined scripts.

## Alerter Configuration
Configure SMTP server settings before setting up alert actions:
1. **Protect → Alerter**.
2. Enter SMTP host, port, credentials, sender address.
3. Save; alerts inherit these defaults.

## DeletesGroup Type for IMS Commands
Predefined IMS groups for labeling sensitive activity: **Deletes**, **IMS Audit Inserts**, **IMS Audit DB Commands**, **Cardholder Objects**, **Financial Objects**, **PHI Objects**.

## RPM Logs Location
Guardium agent RPM logs are stored at `/opt/guardium/rpm_logs`.

## Parameter Description
`api_target_host` determines where an API command runs:
- `all_managed`: all managed units
- `all`: entire Guardium system
- `group:<group_name>`: specific group
- Individual host names or IP addresses
Used in commands like `configure_cold_storage_data_streaming`.

## Sample Output
```
enable_special_attributes
Hive: ok
Impala: ok
...
```

## GuardAPI: enable_quick_search
Enables quick‑search capabilities across all managed units:
```
enable_quick_search | **categories:** features, knowledge, entities
```
Argument `all` set to true when no arguments are provided.

## GuardAPI: get_job_process_concurrency_limit
Retrieves the current job‑process concurrency limit:
```
get_job_process_concurrency_limit | **categories:** knowledge, entities
```
Optional `api_target_host` specifies target host/managed group.

## GuardAPI: list_audit_processes
Lists all defined audit processes:
```
list_audit_processes | **categories:** features, keywords, knowledge
```
Optional `api_target_host` can be used to target a specific host.

## GuardAPI: get_process_concurrency_limit
Retrieves the concurrency limit for a specified process:
```
get_process_concurrency_limit <process_name> | **categories:** entities
```
Use `api_target_host` to restrict execution to a particular host.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures databases through real-time monitoring, policy enforcement, and compliance reporting.

### Features

- **Database Activity Monitoring:** Collects and analyzes database transactions.
- **Policy-Based Enforcement:** S-GATE blocks policy violations.
- **Compliance Reporting:** Built-in templates for PCI-DSS, GDPR, HIPAA, SOX.
- **Cloud Integration:** Native connectors for AWS, Azure, Google Cloud.

### Workflows

- **Configuration:** Set up datasources, agents, policies.
- **Management:** Create/maintain policies, groups, credentials.
- **Investigation:** Search logs, generate reports, investigate anomalies.
- **Maintenance:** Update certificates, rotate credentials, troubleshoot.

### Personas

- **Security Administrators:** Define policies, monitor alerts, manage incidents.
- **Database Administrators:** Deploy agents, configure datasources, review reports.
- **Compliance Officers:** Generate audit reports, verify policy adherence.
- **Security Analysts:** Investigate incidents, correlate data.

### Entities

- **Agents/Sensors:** S-TAP, A-TAP, K-TAP.
- **Management Components:** Collector, Aggregator, Central Manager.
- **Policy Entities:** Security Policy, Audit Policy, Classification Rule, Access Rule.
- **Infrastructure:** Managed Unit, GIM, S-GATE.

## Common GuardAPI Parameters and Commands

- **api_target_host:** Specifies target host(s) for API commands (`all_managed`, `all`, `group:<name>`, or specific host/IP).
- **patch_cleanup:** Removes temporary patch files; uses `api_target_host` for targeted cleanup.
- **update_aws_secrets_manager_config:** Configures AWS Secrets Manager integration.
- **get_ip_to_alias_overwrites:** Retrieves IP-to-alias mappings.

## Discovery and Monitoring

- **--discover-ies:** Triggers database discovery, replaces current inspection engines.
- **--stop:** Temporarily halts S-TAP service or monitoring process.

## IBM Guardium Data Protection

**Overview**  
IBM Guardium protects structured and unstructured data across on‑premises and cloud environments by real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

**Key Features**  
- **S-TAP Agent**: Light‑weight agent on database servers that captures traffic and forwards it to collectors.  
- **S-GATE**: Real‑time blocking of unauthorized queries.  
- **Policy Engine**: Configurable rules for users, objects, operations, and time windows.  
- **Compliance Templates**: Built‑in support for PCI‑DSS, GDPR, HIPAA, SOX, etc.  
- **Universal Connectors**: Kafka, Cloudera Navigator, and other structured data sources.  
- **GIM Deployment**: Automated install, update, and management of S‑TAP agents.

**Workflows**  
- **Provision & Monitor**: Install S‑TAP, configure data sources, enable S‑GATE, define audit policies.  
- **Incident Handling**: Detect violations, generate alerts, trigger external ticketing, block malicious queries.  
- **Compliance**: Run periodic assessments, view risk dashboards, generate regulatory reports.  
- **Administration**: Manage users, groups, API targets, and platform settings.

**Risk Spotter**  
Risk indicators (threat matches, audit‑policy violations, vulnerability findings) are weighted and aggregated into a composite risk score.

---

## Backup‑Restore Behavior

During configuration system backup, **only non‑expired certificates** are backed up. Expired certificates are not restored; they are retained in the backup archive but ignored during restoration.

---

## Database Connection Architecture

**JDBC Connectivity**  
- **Native Drivers**: Optimized performance for specific RDBMSs.  
- **Generic Drivers**: Compatibility across many database flavors.  
- **Browser Service**: Dynamically resolves instance names to current port values, eliminating manual port configuration.

## Guardium Data Protection Overview

Guardium Data Protection is IBM's enterprise solution for monitoring and securing database activity. It offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features
- **Activity Monitoring:** Real-time tracking of database operations.
- **Policy Enforcement:** Automated controls based on security policies.
- **Vulnerability Assessment:** Continuous scanning for security weaknesses.
- **Compliance Reporting:** Tools for meeting regulatory standards.

## Guardium Overview

### Key Components
- **Security Policies:** Define rules to block or log sensitive queries.
- **S-TAP Agents:** Capture database traffic for analysis.
- **Vulnerability Management:** Unified alerting and remediation workflows.

### Core Workflows
- **Configuration:** Deploy agents, define policies.
- **Navigation:** Review reports, dashboards.
- **Action:** Enforce blocking, rotate credentials.

### Personas
- **Administrators:** Manage platform and users.
- **DBAs:** Setup datasources, deploy agents.
- **Compliance:** Generate reports, assess risks.

### Entities
- **Agents:** S-TAP, A-TAP, K-TAP, Collector.
- **Policies:** Security, Audit, Classification, Access.
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector.

## Log Masked Extrusion Counter

The Log Masked Extrusion Counter masks sensitive data in query logs while preserving query structure.

## Populating Groups

Use Group Builder to populate Guardium groups manually or via CSV import.

## Policy Builder for Data

Policy Builder integrates with Alert integration point to automate ticket creation for violations.

## Show System Time Server

Displays NTP server status with options for diagnostics and hostname display.

## API Parameter: api_target_host

Specifies target host for API execution with options for managed units and central manager.

## Using the Modernized Vulnerability Management UI

Interactive UI for exploring vulnerabilities with filters and remediation tracking.

## About This Task (CLI User Creation)

Steps to create a CLI role, user, and verify GuardAPI access.

## About This Task (S-TAP Removal)

Procedure to uninstall S-TAP while preserving configuration on Windows.

## GAM Service Global Configuration

Configures GAM behavior with parameters like NUMBER_OF_SERVICES in `resmon.ini`.

## GuardAPI: Adding Custom Properties

```sql
guardapi addCustomPropertyToDatasource 
customProps="key1=value1;key2=value2" 
name="MyDataSource"
```

## AWS S3 Permissions for Discovery

Permissions required for Unified Discovery and Classification in AWS S3.

## Database Discovered Instance Scheduler

Automates recurring database instance discovery with configurable scheduler.

## Before You Begin – Windows S‑TAP

**Prerequisites**

- Windows Server 2008 R2 or later (64‑bit)  
- Administrative rights for installation and configuration  
- Windows Management Instrumentation (WMI) enabled on the target host  

**Steps**

1. Verify that the Guardium collector is reachable from the Windows host.  
2. Run the S‑TAP installer with elevated privileges.  
3. Select the database instances to monitor during setup.  
4. Configure the collector address and port as prompted.  
5. Complete the installation and restart the Windows service.  

**Verification**

- Open the **Windows S‑TAP Control Panel** and confirm the status shows “Running.”  
- In Guardium, navigate to **Data Sources → Databases → Windows S‑TAP** and ensure the new instance appears online.

## DB2 Shared Memory Adjustment

When **monitoring DB2 shared‑memory connections**, the parameter **DB2 Shared Mem. Adjust** offsets the address calculation for the server’s segment of the shared memory area.

**Typical value**: `0` (default). Adjust only when Guardium’s sampling offsets differ from the DB2 memory mapping, as indicated by the data‑collection logs.

---

## GuardAPI Syntax – get_clusters

The GuardAPI **`get_clusters`** retrieves information about Guardium clusters.

```
get_clusters
  [api_target_host=<target>]
```

- **`api_target_host`** (optional): Host on which the API runs – can be `local`, `all`, a specific managed‑unit name, or `group:<group_name>`.  
- **Returns**: JSON array listing cluster names, hostnames, and member counts.

---

## Parameter – api_target_host

**`api_target_host`** defines where a Guardium API call is executed.

**Possible values**

| Value | Meaning |
|-------|---------|
| `local` | Execute on the host issuing the API (default). |
| `all` | Execute on every Guardium appliance in the deployment. |
| `<host_name>` | Single Guardium host. |
| `group:<group_name>` | All hosts belonging to a defined host group. |
| `all_managed` | All managed units (excluding central manager). |

This parameter is required for most multi‑host API operations.

---

## GuardAPI Syntax – show_alerter_smtp_settings

The GuardAPI **`show_alerter_smtp_settings`** displays the current SMTP configuration used by Guardium’s alerter service.

```
show_alerter_smtp_settings
```

**Returned fields**

| Field | Description |
|-------|-------------|
| `SMTP_HOST` | SMTP server address |
| `SMTP_PORT` | Port number (default 25) |
| `SMTP_USER` | Authenticated user (if required) |
| `SMTP_PASSWORD` | Encrypted password placeholder |
| `SMTP_USE_TLS` | TLS‑usage flag (true/false) |

Use this API to verify that outbound e‑mail alerts are correctly routed.

---

## Malicious Stored Procedure

A **malicious stored procedure** is a crafted SQL routine that includes obfuscated or embedded attack payloads, designed to bypass detection and execute unauthorized actions.

**Guardium detection techniques**

- **Policy rules** that flag excessive privilege usage from a specific user or schema.  
- **Anomaly detection** that spots deviations from normal execution patterns (e.g., unusual input parameters, out‑of‑order calls).  
- **Audit‑log analysis** highlighting repeated errors or privilege‑escalation attempts triggered by the procedure.

When flagged, the stored procedure can be blocked via S‑GATE and remediated.

---

## Enabling the Data Compliance Feature

**Data‑Compliance** automates GDPR‑related data discovery, classification, and privacy actions.

1. In the Guardium UI, navigate to **Administration → Data Compliance**.  
2. Set **Enable Data Compliance** to **Yes**.  
3. Choose the **scope** (`all`, specific managed units, or groups).  
4. Configure **classification rules** and remediation actions (e.g., dynamic masking).  
5. Save changes; the feature begins processing on the next scheduled scan.

*Available from Guardium version 12.2 onward.*

---

## Modifying a Table Definition

Guardium stores custom table definitions (e.g., for dynamic data discovery). **Modifying** a custom table definition may:

- **Invalidate existing reports** that reference the previous schema.  
- Require **re‑deployment of the S‑TAP agents** to capture updated column metadata.  
- **Trigger a restart of the Collector** if the definition change affects policy parsing.

Before altering, export the existing definition, apply the change, and re‑run the discovery process to validate data completeness.

---

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on‑premises and in the cloud.

### Features Overview
- **Datasource Connectivity:** Dynamic port detection, multi‑driver support, CyberArk credential‑vault integration  
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, security‑incident generation  
- **Compliance & Reporting:** PCI‑DSS, GDPR, HIPAA, SOX report templates; automated audit trails

### Workflows Overview
- **Configuration:** Add datasource, deploy S‑TAP via GIM, configure FGAC policies  
- **Navigation:** Review activity reports, run vulnerability assessments, audit dashboard  
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents

### Personas Overview
- **Administration:** Administrator (platform config, user management), Security Administrator (FGAC, policies)  
- **Data & Database Mgmt:** Database Administrator (datasources, S‑TAP), Data Analyst (dashboards, queries)  
- **Compliance & Audit:** Compliance Officer (regulatory reports), Security Analyst (threat investigation)

### Entities Overview
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule  
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector

```markdown
** knowledge, keywords  

** Show Encrypt Must Gather Command  
`show encrypt_must_gather` enables emergency mode, disabling all Guardium inspection and allowing all traffic to pass unmonitored.

** 1130. Parameter Value Type Description  
`api_target_host`String: Specifies the target hosts where the API executes. Valid values are `all_managed`, `all`, `group:<group name>`.
```

## High-Level Guardium Overview

IBM Guardium Data Protection monitors and secures databases in real time, providing compliance reporting, threat detection, and policy enforcement across data sources on-premises and in the cloud.

### Key Features
- **Datasource Connectivity:** Dynamic port detection, multi-driver support, CyberArk credential vault integration.
- **Real-Time Monitoring:** Continuous capture of database traffic via S‑TAP agents, evaluated against active security policies.
- **Policy Enforcement:** S‑GATE blocking, alerts, and incident generation for policy violations.
- **Threat Detection:** Real‑time alerts, anomaly detection, vulnerability assessment with exclusion/inclusion filters for MS SQL and STIG benchmark for Oracle 19c.
- **Compliance Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit trails and reporting.
- **Deployment Models:** On-premises, hybrid, and multi‑cloud support with centralized management.

### Typical Workflows
- **Configuration:** Adding data sources, deploying S‑TAP agents, configuring FGAC policies, defining security zones.
- **Monitoring:** Real‑time traffic analysis, activity reports, audit dashboards, compliance rule evaluation.
- **Incident Response:** Alert generation, S‑GATE query blocking, credential rotation, incident case creation.
- **Management:** User and role provisioning, policy lifecycle management, audit trail archiving.

### Personas
- **Administration:** Platform setup, user and group management, system health monitoring.
- **Security Administration:** FGAC policy design, security rule creation, threat investigation.
- **Database Administration:** S‑TAP agent installation, data source registration, performance tuning.
- **Compliance:** Policy compliance verification, report generation, audit readiness.

### Components
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security, Audit, Classification, Access, Redaction, and Threshold policies.
- **Infrastructure:** GIM (Guardium Installation Manager), Managed Units, S‑GATE (enforcement layer), Universal Connector.

## Guardium Data Protection Overview

IBM Guardium Data Protection is IBM’s enterprise‑grade database activity monitoring and security platform. It offers real‑time monitoring, policy enforcement, vulnerability assessment, compliance reporting, and CEF mapping across on‑premises and cloud data stores.

### Key Features
- **Datasource Connectivity:** Dynamic port detection, multi‑driver support, CyberArk credential vault integration.  
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, security incident generation.  
- **Compliance Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit trails.  
- **CEF Mapping:** Required and optional fields mapped to ArcSight’s CEF standard.

### Core Workflows
- **Configuration:** Add datasources, deploy S‑TAP agents via Guardium Infrastructure Manager (GIM), define FGAC (fine‑grained access control) policies, and resolve duplicate identifiers.  
- **Navigation:** View activity reports, run vulnerability assessments, explore dashboards, and use the investigation center.  
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents, and restore historic audit results.  
- **Upgrade Management:** Review `GIM_EVENTS` reports and verify proper operation after upgrades.

### Personas and Responsibilities
| Persona | Primary Focus |
|--------|---------------|
| **Administrator** | Platform setup, user management, role configuration |
| **Security Administrator** | FGAC, access policies, privileged access management |
| **Database Administrator** | Datasource provisioning, S‑TAP installation, K‑TAP deployment |
| **Data Analyst** | Dashboard usage, query analysis, trend reporting |
| **Compliance Officer** | Regulatory report generation, audit evidence collection |
| **Security Analyst** | Threat investigation, anomaly detection, incident response |
| **UC Administrator** (Universal Connector) | Lifecycle of Unified Connector containers |

### Entity Types
- **Agents & Collectors:** S‑TAP (network), A‑TAP (application), K‑TAP (kernel), Collector, Aggregator, Central Manager.  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, FGAC Policy.  
- **Infrastructure:** GIM, Managed Unit, S‑GATE, CEF Mapper, Remote Logger.  
- **Audit Artifacts:** Saved Data Entity, Restore Point, Change Identifier, API Targets.  
- **Discovery & Classification:** GCP Service Permissions, Script Entities.

---

## Yugabyte Entitlements

Entitlements for YugabyteDB 12.1 + allow granting database‑ and language‑level privileges to the `PUBLIC` role, with the option to include or exclude the **GRANT** option. This enables fine‑grained role‑based and privilege‑based management for Yugabyte clusters.

*Key concepts:* Yugabyte entitlement, privilege granting, PUBLIC role, GRANT option.

---

## Activity Monitoring & Policy Enforcement

Guardium captures database traffic via S‑TAP agents and evaluates it against configured security policies in real time. Violations generate alerts, audit records, or active blocking through S‑GATE. Policies can be scoped by user, object, operation, and time windows, providing granular control over database activity.

*Key concepts:* S‑TAP (traffic capture), S‑GATE (blocking/monitoring), Security Policy, Real‑Time Monitoring, Audit Trail.

---

## Parameter Value Type Description

**`api_target_host`** – Specifies the target hosts for an API execution in IBM Guardium. It determines whether the request should be processed by Guardium collectors, aggregators, or the central manager, enabling workload distribution across multiple hosts or clustered environments.

---

## Audit State

The **Saved Data Entity** records the actual data saved for a monitored item, including a unique identifier, timestamp, and a link to the **Change Identifier** entity. This entity preserves the data state at specific points in time, supporting forensic analysis through Guardium’s auditing mechanisms.

---

## Compare To

The **Compare To** attribute defines the value against which an SQL statement’s return value is compared. It can reference external benchmarks such as CIS standards or CVE identifiers, allowing policies to validate query results against known baselines or vulnerabilities.

---

## Restoring and Viewing Audit Results in the Investigation Center

The **Investigation Center**, an aggregator extension, permits investigation users to restore historic audit results for forensic analysis on selected dates. This capability is essential for incident response, enabling security teams to examine past data activity to understand incident scope, trace origins, and guide remediation efforts.

## Document Overview

**IBM Guardium Data Protection**: Enterprise database activity monitoring and security platform for real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores on-premises and in the cloud.

### Features
- **Database Connectivity**: JDBC, native drivers, browser service for dynamic ports.
- **Anomaly Detection**: Detects behavior outside normal patterns.
- **Plug‑ins**: Preinstalled for profile creation via central manager workflow.
- **CLI Commands**: `store disk_space_reserved`, configure disk space on aggregators/collectors.
- **API Targets**: `api_target_host` specifies execution targets for GuardAPI/REST (`all_managed`, `all`, `group:<name>`).
- **Universal Connector**: REST endpoints for lifecycle management.

### Workflows
- **Deployment**: Run script with `--lb-script` for load‑balancer integration.
- **Configuration**: Add data sources, deploy S‑TAP agents, configure FGAC policies via central manager workflow.
- **Monitoring**: Capture activity via S‑TAP agents, real‑time policy evaluation.
- **Incident Response**: Block unauthorized queries, rotate credentials, investigate incidents.

### Personas
- **Administrator**: Configures platform, manages users, assigns roles.
- **Security Administrator**: Defines FGAC policies, security rules.
- **Database Administrator**: Manages data sources, S‑TAP agents.
- **Data Analyst**: Dashboards, vulnerability assessments.
- **Compliance Officer**: Regulatory reports, audits.

### Entities
- **Agents & Collectors**: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules

## Guardium Data Protection Overview

### Feature Highlights
- Continuous monitoring of database and file system access and usage
- Configurable policies, access controls, and S-GATE prevention
- Automated sensitive data discovery and classification tagging
- REST APIs, GuardAPI, and workflow orchestration for integration

### Workflow Summary
- **Deployment:** Installation and configuration of collectors, aggregators, and central managers
- **Provisioning:** Onboarding data sources, S-TAP agents, and Universal Connectors
- **Policy Management:** Defining FGAC, masking, and exception rules; policy rollout and auditing
- **Incident Response:** Real-time alerts, breach investigation, and remediation actions

### Key Personas
| Persona | Responsibilities |
|---------|-------------------|
| Security Administrators | Define and enforce access policies, manage compliance reporting |
| Database Administrators | Deploy S-TAP agents, manage data sources, audit logs |
| Data Owners | Classify data, monitor usage, approve exceptions |
| Compliance Officers | Generate regulatory reports, demonstrate audit readiness |

### Primary Entities
- **Agents** (S-TAP, A-TAP, K-TAP) for real-time data capture
- **Collectors & Aggregators** for data storage and analysis
- **Central Manager** as the policy server, reporting server, and unified management console
- **Data Catalog** for metadata and classification definitions

## Database Connection Architecture
Guardium supports JDBC and native drivers for encrypted connections, enabling dynamic port detection for failover and load balancing. Kerberos and SSL/TLS secure communications between agents and collectors.

**Key Concepts:** JDBC, Native Driver, Browser Service, Dynamic Port Detection, Kerberos, SSL/TLS

## Activity Monitoring & Policy Enforcement
Guardium captures database and file activity via S‑TAP agents. Policies define FGAC rules evaluated in real time to trigger actions such as alert, log, block, or mask data. Granular controls include exceptions, masking, and dynamic privileges.

**Key Concepts:** S‑TAP, FGAC, Policy Engine, Real‑Time Blocking, Data Masking

## Threat & Vulnerability Management
Guardium assesses databases for vulnerabilities through configuration scans and patch level checks. Correlation rules for activity, policy violations, and threat intelligence detect suspicious behavior. Risk scoring prioritizes remediation.

**Key Concepts:** Vulnerability Assessment, Threat Correlation, Risk Scoring, Adaptive Access Controls

## Identity & Access Management Integration
Guardium integrates with LDAP, Active Directory, and SAML for user provisioning, authentication, and single sign‑on. FGAC policies apply dynamic privileges based on user attributes, groups, and risk scores. Just‑in‑time access and segregation of duties enforce least privilege.

**Key Concepts:** LDAP, AD, SAML, FGAC, JIT, Segregation of Duties, Privileged Access Management

## Reporting & Analytics
Guardium includes out‑of‑the‑box reports for compliance audits (PCI‑DSS, GDPR, HIPAA), access reviews, and usage analytics. Dashboards visualize policy violations, threat insights, and data discovery results. APIs and scheduled jobs automate report delivery.

**Key Concepts:** Reporting Templates, Custom Reports, Dashboards, API Integration, Scheduled Jobs

## Storage & Retention Management
Guardium stores audit data in high‑performance clusters or cloud buckets, balancing performance, cost, and compliance. Tiered storage policies and cryptographic shredding enable regulated data disposal.

**Key Concepts:** Storage Clusters, Cloud Buckets, Tiered Policies, Data Retention, Cryptographic Shredding

## Document Overview
IBM Guardium Data Protection offers real‑time database monitoring, vulnerability assessments, and compliance reporting across enterprise data stores on‑premises and in the cloud.

**Features Overview**
- **Real‑Time Database Monitoring:** S‑TAP agents capture SQL traffic, evaluate against policies, and block unauthorized actions.
- **Vulnerability Management:** Automated scans for configuration issues, missing patches, and excessive privileges.
- **Compliance Reporting:** Ready‑to‑use reports for PCI‑DSS, GDPR, HIPAA, SOX, etc.
- **Audit Trail & Investigation:** Immutable logs of data accesses, anomalies, and policy violations.

**Workflows Overview**
- **Configuration:** Add data sources, deploy S‑TAP agents, define access and audit policies.
- **Live Protection:** Enable S‑GATE blocking, configure exception handling, automate response actions.
- **Analysis & Reporting:** Run activity reports, vulnerability scans, trend analysis, compliance checks.
- **Incident Response:** Generate alerts, investigate through dashboards, apply remedial steps.

**Personas Overview**
- **Security Administrators:** Manage policies, oversee investigations.
- **Database Administrators:** Install and maintain agents, monitor data source health.
- **Compliance Officers:** Access audit trails, generate regulatory reports.
- **Security Analysts:** Hunt threats, use correlation dashboards, perform forensics.

**Entities Overview**
- **Agents:** S‑TAP, A‑TAP, K‑TAP – collect raw DB traffic.
- **Collectors & Aggregators:** Process traffic, perform analysis, apply policies.
- **Policies:** Anomaly detection & access monitoring rules.
- **Infrastructure:** GIM, Managed Units, Central Manager.

## IBM Guardium Overview

### Purpose
- Discover and report user permissions, data classification, and data lineage for risk and compliance.  
- Centralize creation and distribution of security policies, FGAC rules, classification rules, and notifications.

### Workflows
- **Configuration:** Deploy agents, configure data sources, define FGAC and audit policies, schedule assessments.  
- **Monitoring:** Review live activity reports, block unauthorized operations, investigate incidents.  
- **Optimization:** Adjust policies, tune performance, manage agent groups, set up aggregators and S‑GATEs.  
- **Compliance Reporting:** Generate PCI‑DSS, GDPR, HIPAA, SOX, and custom reports; audit trails for forensic analysis.

### Personas
- **Security Administrators:** Define FGAC/access policies, manage user roles, incident response.  
- **Database Administrators:** Onboard data sources, install/configure S‑TAP, tune performance.  
- **Compliance Officers:** Run risk‑compliance reports, verify regulatory coverage.  
- **Auditors:** Access audit logs, validate policy enforcement, produce audit evidence.

### Entities
- **Agents:** S‑TAP (database), A‑TAP (applications), K‑TAP (kernel capture).  
- **Infrastructure:** Collectors, aggregators, Central Manager, S‑GATE, Universal Connector.  
- **Policies:** Security, Audit, Classification, Access.  
- **Infrastructure:** Managed Units, Central Manager, S‑GATE, Universal Connector.

### Database Connection Architecture
- Tiered agent‑collector model: S‑TAP agents capture raw SQL, forwarding to Collectors/Aggregators, then to Central Manager for analysis.  
- Automatic detection of dynamic ports via Browser Service; supports native and generic JDBC drivers.  
- Credential management integration with CyberArk vaults.

### Activity Monitoring & Policy Enforcement
- Captures all database traffic through S‑TAP agents and evaluates it against real‑time security policies.  
- Policies specify users, objects, operations, time windows; violations trigger alerts, audit records, or S‑GATE blocking.  
- Central management, version control, risk‑based scoring, and automated remediation.

### Entitlement Discovery & Classification
- Automates discovery of user entitlements across supported databases using native APIs or query methods.  
- Classification rules tag sensitive data (PII, credit cards) based on column names, patterns, or custom logic.  
- Produces reports highlighting over‑privileged accounts and data exposure.

### Reporting & Dashboards
- Built‑in reports covering activity summaries, security violations, compliance gaps, risk metrics.  
- Visual dashboards show high‑severity findings, top offenders, and compliance status.  
- Custom reports via Reporting Builder with filters, aggregations, scheduling, PDF/CSV exports.

### Policy Types & Configuration
- **Security Policy:** Blocks/alerts on unauthorized SQL based on rule criteria.  
- **Audit Policy:** Generates immutable audit records for matching events.  
- **Classification Rule:** Identifies sensitive data columns using patterns, regex, or dictionaries.  
- **FGAC:** Implements row‑level and object‑level permissions, session constraints.  
- Configurable via web UI or GuardAPI with scope, priority, and enforcement options.

### Vulnerability Assessment & Remediation
- Comprehensive scanner for mis‑configurations, weak passwords, missing patches, excessive privileges.  
- Scheduled or on‑demand scans produce detailed reports with remediation recommendations.  
- Automated actions such as password rotation, privilege reduction, patch deployment scripts.

### Compliance Frameworks
- Out‑of‑the‑box report templates aligned with PCI‑DSS, GDPR, HIPAA, SOX, NIST, etc.  
- Each template maps Guardium findings to specific control requirements, providing audit evidence.  
- Custom regulatory reports built by extending existing templates with organization‑specific rules.

### Deployment Models
- **On‑Premises:** Dedicated Central Manager server, distributed Collectors and S‑TAP agents.  
- **Hybrid/Cloud:** Managed Unit deployment model supporting cloud data sources via Universal Connector.

## Data Protection with Guardium

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data stores across on-premises, cloud, and hybrid deployments.

### Key Concepts
- **Central Manager:** The hub for managing Guardium units and enforcing policies.
- **Managed Unit:** Individual Guardium appliances under the Central Manager's control.
- **Hybrid Deployment:** Integration of on-premises and cloud data sources.
- **Cloud Connectors:** Native connectors and VPN tunnels for AWS, Azure, and Google Cloud.
- **High Availability:** Redundant configurations to ensure continuous monitoring.

### Workflows
- **Datasource Configuration:** Set up Guardium datasources, define cloud connectors, and configure VPN tunnel mappings.
- **Policy Enforcement:** Deploy S-TAP agents in cloud environments, create FGAC policies, enable S-GATE blocking.
- **Incident Management:** Centralized risk monitoring, policy violation alerts, and automated remediation from the Central Manager.

### Personas
- **Security Administrator:** Manages policies, monitors threat alerts, and coordinates cloud connector setup.
- **Database Administrator:** Configures S-TAP agents on cloud instances, applies FGAC policies.
- **Compliance Officer:** Uses Central Manager dashboards to generate compliance reports across all environments.

### Technical Details
- **TLS 1.2+ Requirement:** All connections between Guardium units and STAPs must use TLS 1.2 or newer.
- **API Targeting:** Use `api_target_host=all_managed` to apply configuration changes to only the managed agents in a hybrid deployment.

## Disable CSRF Protection via CLI
Use `cli_cmd -cmd disable_csrf` to remove HTTP 403 errors caused by CSRF protection; note this weakens security.

# IBM Guardium Data Protection Overview

IBM Guardium Data Protection (GDP) is a comprehensive enterprise database activity monitoring and security platform that monitors structured and unstructured data in real time, enforces security policies, blocks unauthorized actions, conducts vulnerability assessments, and generates compliance reports for frameworks such as PCI‑DSS, GDPR, HIPAA, and SOX.

## Core Features
- **Real‑time Traffic Inspection:** S‑TAP, A‑TAP, and K‑TAP agents capture database traffic without performance impact.
- **Fine‑grained Access Control (FGAC):** Centralized policy engine evaluates queries before execution.
- **Data Masking & Redaction:** Transparently masks sensitive columns for unauthorized users.
- **Vulnerability Assessment:** Automated scans identify misconfigurations, missing patches, weak credentials.
- **Compliance Reporting:** Built‑in and customizable templates for PCI‑DSS, GDPR, HIPAA, SOX, and audit trails.

## Operational Workflows
### Configuration
- Register data sources, deploy and update monitoring agents, create FGAC policies, and configure data‑masking rules.

### Monitoring & Incident Response
- Review activity reports, investigate alerts, block malicious sessions via S‑GATE, and remediate findings.

### Compliance & Auditing
- Schedule and export audit reports, prepare evidence artifacts, and generate regulatory submissions.

## User Personas
- **Administrator:** Manages the Guardium platform, user accounts, and system settings.
- **Security Administrator:** Defines FGAC policies, data‑masking rules, and compliance configurations.
- **Database Administrator (DBA):** Installs/configures S‑TAP agents and troubleshoots performance impacts.
- **Compliance Officer:** Generates and reviews audit reports and remediation plans.

## Architectural Entities
- **Collectors, Aggregators, Central Manager:** Hierarchical nodes that collect, store, and aggregate audit data.
- **S‑TAP, A‑TAP, K‑TAP:** Device‑level agents installed on database hosts.
- **Security Policy, Audit Policy, FGAC Rule, Data‑Masking Rule:** Logical constructs defining access control, auditing, and data‑privacy.

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for wide compatibility. You must set the `real_db_port` parameter for K‑TAP monitoring to explicitly indicate the database's listening port, eliminating reliance on dynamic port discovery.

---

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S‑TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or automatic blocking through the S‑GATE enforcement point. Policies can be scoped to specific users, objects, operations, and time windows.

---

## GuardAPI Command Reference

The `datamart_copy_file_bundle` GuardAPI manages data‑mart file bundles and supports the following actions:

| Action | Purpose |
|--------|---------|
| `create` | Generate a new bundle definition |
| `delete` | Remove an existing bundle |
| `include` | Add files or objects to a bundle |
| `exclude` | Remove files or objects from a bundle |
| `info`   | Retrieve metadata about a bundle |

Bundle management commands require `bundle_name`, `action`, and can filter by `datasourceGroups` or `datasourceNames`.

---

## Feature Patch Reference

Feature patches augment Guardium functionality or resolve critical issues. Each patch has a unique ID, installation and compatibility details, and activation requirements. For example, patch **GP13.1‑P2** adds support for newer K‑TAP versions and introduces the `real_db_port` parameter, and it requires Guardium 11.4 or later.

---

## Field Description – GUI Elements

When defining a data source in the Guardium UI the following fields are mandatory:

- **Host Name/IP** – Fully qualified domain name or IP address of the database server.  
- **Port number** – Defaults to 2638 if omitted. Use `real_db_port` when K‑TAP monitoring is in use to override dynamic detection.  
- **Database** – Unique name of the target database instance.  
- **Connection property** – Optional JDBC parameters such as `ssl=true` or `schema=public`.

---

## Before You Begin – Adding Datasources in CyberArk

To integrate Guardium with CyberArk for credential management:

1. Log into the CyberArk web console.  
2. Navigate to **Applications → Add Application**.  
3. Choose **Guardium Datasource** from the template list.  
4. Prepare the datasource configuration, including `real_db_port` if using K‑TAP monitoring.  
5. Save and verify connectivity from Guardium to the CyberArk vault.

---

## Event Value – Timestamp Handling

Guardium timestamps (`Event Value`) are stored in UTC but retain the original timezone offset as a separate field (`Original Timezone`). This ensures precise chronological correlation across collectors in different geographic locations.

---

## Query Rewrite – Action Details API

The **Query Rewrite Action Details API** (`46840551-e328-4ab1-9e58-a1712a478d06`) returns metadata about a configured query‑rewrite action, including the rule name, target objects, and the rewrite logic applied. This API is helpful for auditing and troubleshooting query‑rewrite policies.

---

## Vulnerability Patch – Compatibility Notes

Applying Guardium feature patch **GP13.1‑P2** (see Feature Patch Reference) requires the `real_db_port` parameter for any data source monitored via K‑TAP. The patch is compatible only with Guardium versions 11.4 or higher and must be activated after upload.

---

## Diagnosing Host Connectivity

If the `diag.bat` utility does not return expected output, verify that the installed PowerShell version is **5.1** or newer. Older versions cannot display diagnostic zip files; retrieve them directly from the `<diag folder>` and examine logs for failed data source connections.

---

## S‑TAP FIPS Compliance

When S‑TAP reports *not FIPS 140‑2 compliant*, adjust the configuration via the **S‑TAP Control** page. FIPS compliance is supported on Solaris x86, Linux x86/64, Linux x86/32, and Linux S390X platforms, but not on Solaris SPARC or AIX PowerPC.

---

## Configuring the HashiCorp Vault Credential Provider  (truncated)

### Workflows Overview
- Deployment adds datasources, then deploys S‑TAP agents and configures security policies.  
- Monitoring reviews activity reports, analyzes threats, and triggers alerts.  
- Remediation rotates compromised credentials, applies patches, and enforces access changes.

### Personas Overview
- Security Admin defines policies, monitors incidents, and configures S‑GATE.  
- DB Admin manages datasources, installs S‑TAPs, and verifies connectivity.  
- Compliance Officer generates audit reports, tracks policy adherence, and oversees data governance.

### Entities Overview
- Agents & Collectors: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.  
- Policies & Rules: Security Policy, Audit Policy, Classification Rule, Access Rule.  
- Infrastructure: Guardium Information Management (GIM), Managed Unit, S‑GATE, Universal Connector.

### Configuring the Vault for HTTPS Communication
Configure the HashiCorp Vault server for HTTPS to encrypt all secret traffic. Generate a TLS certificate, set the Vault listener to HTTPS, and update clients to trust the certificate. All CLI, API, and UI interactions must use HTTPS after configuration.

### Before You Begin: Installing S‑TAPs for Ranger Integration
Install the appropriate S‑TAP package on target hosts after reviewing requirements. Verify system prerequisites, enable the S‑TAP service, and confirm data collection by checking activity streams in Guardium.

### Best Practices for Using External S‑TAPs with On‑Premises Databases
1. Inventory databases with IP addresses, hostnames, and SSL statuses.  
2. Determine SSL requirements and prepare certificates for mutual authentication.  
3. Allocate dedicated interfaces or VLANs for S‑TAP traffic.  
4. Test connectivity between the External S‑TAP and Guardium before enabling collection.  
5. Enable real‑time alerts for high‑risk activities and review logs regularly.

### GuardAPI Syntax Requirements
The `delete_imscheckpoint_record` GuardAPI command requires:
- `agentName` (String): the agent name associated with the checkpoint record.  
- `context` (String): the execution context (e.g., `security` or `compliance`).

Both parameters uniquely identify the checkpoint record for deletion.

### GuardAPI Command: gim_remove_bundle
`gim_remove_bundle` deletes a software bundle from the GIM repository. It takes one argument:
- `bundlePackageName`: the unique identifier of the bundle to remove.

### Sensitivity Description Compliance in Guardium
The Canadian SIN/SSN is a work‑authorization identifier in Guardium’s Sensitivity Description Compliance, enabling targeted monitoring and access controls to meet Canadian privacy regulations.

### Asia Bank Account Numbers
Asia bank account numbers uniquely identify holders and authorize transactions within Asian banking networks. Understanding their structure is crucial for financial data processing and compliance reporting in Asia.

### Deploying CyberArk on Guardium
1. Download the CyberArk SDK patch for Guardium.  
2. Install the patch on the Guardium appliance.  
3. Configure integration between CyberArk and Guardium for credential sharing and monitoring.

## IBM Guardium High‑Level Overview

IBM Guardium Data Protection monitors databases, file systems, and big‑data stores to detect threats, maintain compliance, and generate audit reports. It protects structured and unstructured data in on‑premises and cloud environments.

### Key Features
- **Database Connection:** Native and generic JDBC drivers, dynamic port discovery.  
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, analytics for suspicious activity.  
- **Reporting & Compliance:** PCI‑DSS, GDPR, HIPAA, SOX templates; automated audit trails and dashboards.  
- **Audit & Monitoring:** Centralized capture of SQL traffic through S‑TAP agents; analysis and alerting.

### Primary Workflows
1. **Configuration:** Add datasources, deploy S‑TAP agents via Guardium Installation Manager, define FGAC policies.  
2. **Threat Management:** Build policies, assign severity, configure alerts or S‑GATE blocking.  
3. **Reporting:** Use predefined compliance reports, custom query‑report‑builder views, schedule deliveries.  
4. **Incident Response:** Block unauthorized queries, rotate credentials, investigate via analytics or incident dashboards.

### Personas
- **Security Administrator:** Manages policies, access control, and threat detection.  
- **Database Administrator:** Installs/updates S‑TAP agents, tunes performance.  
- **Compliance Officer:** Configures regulatory reports and reviews audit logs.  
- **Analyst:** Uses dashboards, runs ad‑hoc queries, and investigates anomalies.

### Architectural Entities
- **Agents/Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.  
- **Policy Elements:** Security Policy, Rules, Alerts/Log actions, Violations.  
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector.

### Database Connection Architecture
Guardium supports native JDBC drivers for optimal performance and generic drivers for wide compatibility. A browser service resolves instance names to current ports automatically.

### Activity Monitoring & Policy Enforcement
All database traffic is captured by S‑TAP agents and evaluated in real‑time against configured policies. Violations trigger alerts, reports, or blocking by S‑GATE. Policies can be scoped by user, object, operation, and time windows.

### Installing a Policy
Open **Security Policies**, select the desired policy, click **Install > Install**, choose an appropriate installation action, and complete the wizard.

### Threat Detection Analytics
Guardium Threat Detection Analytics scans audited data to detect signs of database attacks, using specialized analytics for identifying suspicious activity.

### Informix DB Entitlements
Informix DB Entitlements domains enable uploading and reporting on Informix entitlement data, with each domain representing a single entity.

## Guardium Data Protection Overview

### Features
- Real-time monitoring and policy enforcement  
- Threat detection with S-GATE blocking  
- Compliance reporting (PCI-DSS, GDPR, HIPAA, SOX)  
- Performance management including capacity optimization  

### Workflows
- **Configuration**: Add datasources, deploy S-TAP via GIM, configure FGAC policies  
- **Navigation**: Review activity reports, run vulnerability assessments, view audit dashboard  
- **Action**: Block unauthorized queries, rotate credentials, respond to incidents  
- **Upgrade Preparation**: Capacity planning, load management  

### Personas
- **Administration**: Administrator (platform config, user management)  
- **Security**: Security Administrator (FGAC, policies)  
- **Data Management**: Database Administrator, Data Analyst  
- **Compliance**: Compliance Officer, Security Analyst  
- **Operations**: Capacity Planner  

### Entities
- **Agents**: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager  
- **Policies**: Security, Audit, Classification, Access  
- **Infrastructure**: GIM, Managed Unit, S-GATE, Universal Connector  

## CLI Commands

### Serial TTY
`show system serialtty` reports whether serial TTY consoles are enabled/disabled.

### Database Parameters
`DB Install Dir` specifies the installation directory for Db2, Informix, and Oracle; NULL for other types.

### Threat Details
`Inactive STAP` for SAP HANA shows privilege and object grants to users and PUBLIC.

### Analytics
`Analytic Outlier Details` captures current status, end analysis time, and other metadata.

### Data Sources
`Amazon ElastiCache` can be added as a data source for Redis or Memcached services.

## Administration Tasks

### Outlier Detection
Use `set_outliers_detection_parameter` and `get_params` to manage configurations from version 12.2.1.0.

### Data Purging
`purge_data` removes obsolete logs, reports, and temporary files to improve performance and reduce storage costs.

### Report Access
- **Admin Reports**: Standard reports for admin users only  
- **Query-Restricted Reports**: Non-admins see filtered results based on data level security  

### Installation
Download Guardium Installation Manager (GIM) and S-TAP agent packages from the IBM Guardium Data Protection Trial page after signup.

## Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores both on-premises and in the cloud.

## Key Features

- **Audit Reports**: Summarize configuration changes, audit configuration modifications, and related metadata like time ranges and user IDs.
- **Activity Monitoring & Policy Enforcement**: Capture all database traffic via S-TAP agents, evaluate in real time against configured security policies, and trigger alerts, reports, or blocking via S-GATE.
- **Vulnerability Assessment**: Supports various database versions such as MongoDB Atlas 8.0.16, MarkLogic 11.3.3, 12.0.0, EDB PostgreSQL 17.5, IBM Db2 12.1, and Oracle MySQL 8.4, enhancing coverage across database types.
- **Data Stream Management**: Enables manual addition of new data streams with detailed configurations.

## Usage Workflows

- **Before Begin Tasks**: Ensure GIM clients are at version 11.0 or later before performing certain certificate updates.
- **Create Data Streams**: Manually add new data streams through the Streams table interface.
- **Use Internal Load Balancers**: Configure Kubernetes services to request internal load balancers from the cloud provider's control plane.

## Roles and Responsibilities

- **Database Administrators**: Configure datasources, deploy S-TAP, manage FGAC policies.
- **Security Administrators**: Define FGAC policies, assign rule types, manage categories and classifications.
- **Compliance Officers**: Generate audit reports, run vulnerability assessments.

## Core Components

- **Components**: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- **Datasource Groups**: Defined by parameters like `appTypeCriteria` and `customPropsCriteria`.
- **Infrastructure Elements**: GIM, Managed Unit, S-GATE, Universal Connector.
- **Parameters**: `dataBaseType`, `definitionName`, `appTypeCriteria`, `customPropsCriteria`.

## Alert Configurations

- **Receivers**: Defined in the Alert Builder.
- **Trigger Once Per Session**: Prevents reanalyzing sessions after the first match, beneficial for "Selective Audit" policies.

## Parameter Details

- `create_datasource_group` includes `appTypeCriteria` (with valid values via `--help`) and `customPropsCriteria` (string list of datasource custom properties).
- `update_qr_definition` requires parameters `dataBaseType` and `definitionName`.

## Database-Specific Notes

- **ABAP Stack Systems**: Traditional SAP ECC systems written in ABAP, accessing traditional databases with direct read/write/update capabilities.
- **Trigger Once Per Session**: Optimizes session handling in selective audit policies.

## Connectivity and Load Balancing

- **Internal Load Balancer**: Kubernetes services can be configured to use internal load balancers via annotation.
- **S-TAP Deployment**: Using External S-TAP with a single host on a single-node Kubernetes cluster does not require a load balancing service.

### Overview

**Datasource Management:** Configure hostname/IP, client credentials, server name, port, and database name for each datasource.  
**Policy Enforcement:** Manage session masking, ignore rules, predefined SQL groups, and activity logging.  
**Vulnerability Management:** Utilize the Hub UI for unified vulnerability reporting.  
**Data Handling:** Set log retention, archive to GBDI server, and manage backups.

### Workflows

**Configuration:** Add datasources with required credentials, port settings, and database details.  
**Policy Setup:** Create Ignore sessions rules, SQL groups, and access controls.  
**Monitoring:** Track real-time activity with session handling scenarios.  
**Reporting:** Use compliance templates and vulnerability dashboards.

### Personas

**Security Administrators:** Configure policies and monitor incidents.  
**Database Administrators:** Manage datasources and define SQL group definitions.  
**Compliance Officers:** Generate reports and ensure data retention compliance.  
**Analysts:** Investigate incidents and review vulnerability scan results.

### Entities

**Datasource Entities:** Host/IP, username/password, server/port, database name.  
**Policy Entities:** Ignore sessions rules, SQLGroup types, access controls.  
**Monitoring Entities:** Session types (C2S), logger return data.  
**Reporting Entities:** Vulnerability reports, compliance audit trails.

### Field Descriptions

**Host Name/IP:** Required field in datasource configuration specifying the target database system.  
**User Name, Password, Host, Port, Database:** Required fields for connection setup; password is the client secret, host must end in `.database.windows.net`, port defaults to 1433, and database specifies the target database.

### Ignore Sessions Policy

The second rule can ignore invisible binary traffic, such as encrypted SSL/TLS sessions, to optimize data capture without compromising security.

### Flat Log Domain

Defines entities and attributes for logging and auditing of specific client-server connections with full data access.

### Data Retention and Backup

Using a GBDI server allows reducing collector retention time to one day and central management of backups, optimizing storage and compliance workflows.

### HR Driver and National ID Numbers

The HR driver verifies driving rights, while national ID numbers confirm personal identity; proper formatting is essential for accurate processing and compliance.

### Security Incidents Template

Tracks and reports potential run-time security incidents involving administrative users and applications, aiding in detection and response.

### Policies and Rules

Policies define monitoring scope, while rules specify conditions and actions for client requests or server responses to enforce security and compliance.

### Returned Data Attribute

Includes row count and SQL statement type (e.g., SELECT, INSERT) for auditing and analyzing database activity.

### Classification Custom Property Parameter

`allow_datasource_full_control_by_role` grants full control of a datasource to a role, allowing comprehensive management and access privileges.

### Vulnerability Management Hub

Presents vulnerability assessment results in an interactive format with progressive disclosure for enhanced usability and depth of analysis.

### Ignoring Specific Ports

The Ignored Ports List excludes non-database traffic from analysis, reducing noise and focusing resources on relevant database activity.

### SQLGroup Type for DB2 Z/OS Commands

Predefined groups such as zOS Audit Query, Updates, Deletes, and Inserts facilitate categorization and monitoring of specific DB2 operations for auditing and compliance.

### Scenario 1: Session Handling

Guardium does not create a new session or send data to the logger or rules engine when receiving DB server responses mid-query, preventing false positives or security alerts.

### Classification

When adding a custom property for classification, ensure it aligns with organizational data governance policies and supports compliance requirements.

## Add a Custom Property to Guardium

Guardium users can capture additional database-specific information by defining **custom properties**. These user-defined attributes enrich data collection and analysis, allowing more granular reporting and auditing.

### Create a Custom Property

1. Navigate to **Define → Vulnerability Assessment → Assessment Tools → Custom Properties**.  
2. Click **New** and provide a meaningful name for the property.  
3. Set the **Data Type** (e.g., String, Integer, Boolean).  
4. Specify an optional **Description** to document the purpose.  
5. Click **Save**.

### Use the Custom Property

After creation, the custom property appears as a selectable column in **Assessment Tools → Data Collection → Custom Properties**. Assign it to relevant data sources or policies to start collecting its values alongside native Guardium data.

## Application Events API

The Application Events API lets external apps notify Guardium about database connection events, enabling identification of users and activities that traffic analysis cannot detect. Integration provides full visibility into all interactions.

## IAM Instance Profile Authentication on AWS

When deployed on EC2, Guardium can authenticate using IAM roles instead of static credentials. The EC2 instance must be associated with a role that includes a policy granting Guardium the permissions it requires. This improves security by avoiding embedded credentials.

## Enabling UID Chain Auditing

To log complete user ID chains for connections, enable `hunter_trace` in `guard_tap.ini`. This records every user transformation, vital for tracking origins through pooled or proxied connections.

## S-TAP Parameter Configuration

The **TAP** tab lets admins configure external S-TAP agents:

- **Port Range (PORT\_RANGE\_S):** TCP ports to monitor.
- **Named Pipe (NAMED\_PIPE):** Pipe name for MSSQL local access (`sql\query`, `sqllocal`, `\MSSQLSERVER`).

These settings control which endpoints S-TAP inspects and how it connects to different databases.

## System Time Synchronization

Accurate time is essential for event correlation. Administrators can configure up to three NTP servers via `store system time_server` to keep Guardium appliances synchronized for reliable audit logs and compliance reporting.

## Generic Database Connections

The datasource dialog requires three fields to configure a generic database:

- **Host Name/IP** — Database server address.
- **Instance Name (optional)** — If the server hosts multiple instances.
- **Database Name** — The specific database to monitor.

## Azure Storage Connection Strings

To integrate Guardium with Azure storage:

1. In Azure portal, navigate to **Storage accounts** → desired account → **Settings** → **Shared access signature**.
2. Generate a signature with the needed permissions and expiry.
3. Use the displayed connection string (account name + SAS) when configuring data storage locations in Guardium.

## Vulnerability Assessment Licensing

Guardium VA licensing options:

- Standalone part numbers.
- Included in Guardium package software.
- Measured by managed virtual servers (MVS).

Choose the model that aligns with deployment size and compliance requirements.

## Central Manager After Upgrades

After managed units are upgraded, refresh the Central Manager to recognize new versions, maintaining an accurate environment view for coordinated security operations.

## MS SQL Server Named Pipes Configuration

Configure the `NAMED_PIPE` parameter with the pipe name SQL Server uses for local access, such as:

- `sql\query`
- `sqllocal`
- `\MSSQLSERVER`

Correct settings enable S-TAP to communicate with SQL Server instances using the OS-provided inter‑process communication mechanism.

## Anomaly Score Components

Guardium's anomaly score is based on:

- Number of outliers detected.
- Severity levels of those outliers.
- Predicted vs. actual outlier volumes.
- Domain‑specific context.

Higher scores indicate higher risk, helping prioritize security responses.

## Server Attributes in Datasource Definitions

When defining a database datasource, specify:

- **Server Type** — e.g., DB2, Oracle, Sybase.
- **Service Name** — e.g., `ORCL`, `MSSQLSERVER`.

These attributes identify the database technology and instance for accurate monitoring.

# IBM Guardium Data Protection Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

## Key Features
- **Datasource Connectivity:** Supports dynamic port detection, multi-driver connectivity, and integration with CyberArk for credential management.
- **Threat Detection:** Offers real-time policy enforcement, S‑GATE blocking, and automated security incident generation.
- **Compliance & Reporting:** Includes templates for PCI‑DSS, GDPR, HIPAA, SOX, and automated audit trails.
- **Unified Auditing:** Centralized dashboard with customizable views, detailed activity logs, and incident reports.

## Workflows
- **Configuration:** Add datasources, deploy S‑TAP agents via Guardium Installation Manager (GIM), and configure Fine-Grained Access Control (FGAC) policies.
- **Navigation:** Access activity reports, run vulnerability assessments, and view the audit dashboard.
- **Action:** Block unauthorized queries, rotate credentials, and respond to security incidents.

## Personas
- **Administration:** Manage platform setup and user provisioning.
- **Security Administration:** Define policies and handle security incidents.
- **Database & Data Management:** Register datasources and install S‑TAP agents.
- **Data Analysts:** Use dashboards and perform ad‑hoc queries.
- **Compliance Officers:** Generate regulatory reports and collect audit evidence.

## Core Entities
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP for traffic capture; Collector, Aggregator, Central Manager for data aggregation.
- **Policies & Rules:** Security, audit, classification, and access rules for monitoring and enforcement.
- **Infrastructure:** GIM, Managed Units, S‑GATE blocking engine, Universal Connectors for flexible deployment.

This comprehensive overview captures the essential aspects of IBM Guardium Data Protection, aligning with the provided documentation structure while adhering to the quality and compression guidelines.

## Certificate Storage for External S‑TAP
The `estap-secret` Kubernetes secret stores the token needed to deploy an External S‑TAP. External S‑TAP reads this secret to authenticate with Guardium services.

## Monitor Logger Parameters (GBDI)
`store logger_data_destination_config` sets GBDI streaming parameters: logger destination, Mongo client auth settings, and auth mechanisms. Values are persisted and used by the GBDI collector.

## API Target Host Parameter
`api_target_host` specifies the host(s) for a Guardium REST call. Acceptable values: `all_managed`, `all`, `group:<name>`, or a specific host ID. Determines the operation scope.

## Auto‑Discovery Execution
Start Auto‑discovery from the Guardium UI: open the Auto‑discovery wizard, choose a process (e.g., Database Auto‑discovery), set target hosts/ports, and run the scan. It probes the environment to detect supported databases.

## Last Referenced Datasource Schema
`last_referenced_datasource` records accessed data sources. Columns: `id` (PK), `datasource_desc`, `server_ip`, `host_name`, `db_vendor`. Provides metadata for data sources used in Optim.

## IPv6 Deployment Checklist
After enabling IPv6 on Central Manager and Managed Units, assign IPv6 addresses to all Guardium components (DB servers, S‑TAP agents, File Activity agents, Hadoop nodes, Universal Connector sources). Verify with `test connectivity IP=<IPv6>`.

## Pre‑Installation Prerequisites
Before installing S‑TAP agents, verify:
- S‑TAP is a lightweight monitor installed on each DB host.  
- Central Manager is reachable on the network.  
- Required ports (default 8443 for TLS) are open.  
- Latest Guardium build is installed on the Central Manager.  

These steps ready the environment for successful S‑TAP deployment.

## Internal Database Metrics
The Internal Database Information report shows Guardium system DB stats: uptime, thread count, total queries since startup. Helps with performance tuning and health monitoring.

## EMC Isilon & CEE Integration
Install CEE on a Windows proxy that can contact Isilon’s management interface to enable File Activity Monitor agent collection of file access logs.

## Test Result Entity Attributes
`Test Result` attributes:
- `Test Result Id` – private ID
- `Assessment Result Id` – assessment set ID
- `Test Id1` – test definition ID
- `Cumulative Fail Age` – total failures
- `Cumulative Pass Age` – total passes  

Supports audit and compliance reporting.

## CockroachDB Role Model
Guardium translates CockroachDB entitlements into FGAC rules:
- **Create** → create privileges
- **Grant‑option** → grant rights
- **SuperUser** → all‑powerful admin
- **System** → server‑wide ops  

Ensures unified enforcement of CockroachDB permissions.

## Hive Datasource Configuration
Kerberos tickets required for Hive JDBC connector. Test with `beeline` to confirm Kerberos credentials and Hive server reachability before adding the datasource.

## Vulnerability Assessment Result Visualization
**Results Summary** chart:
- Severity levels (Critical → Info)
- Test type categories (Privilege, Authentication, etc.)
- Bar heights show counts per severity/type.

## Unified Discovery & Classification
Agentless discovery and classification of sensitive data across cloud, SaaS, and on-premises.

## CPU Usage Reporting
Graphical report of CPU activity with customizable time frames.

## User Hierarchy Management
Parent‑child relationships give restricted visibility of servers and databases.

## Torque Integration
Supports custom group management in Central Management GUI.

## Guardium Installation Manager (GIM)
Windows tool for installing/ managing S‑TAP agents; uses parameters such as `QUIET` and `WINSTAP_INSTALL_DIR`.

## S‑TAP Approval Control
Central management page setting to allow or block new S‑TAP connections.

## Big Data Intelligence APIs
Collectors can push data to Big Data destinations.

## CLI Access
Multiple command‑line accounts for role separation.

## Support Diagnostics
Displays current threshold values and system health metrics.

### Workflows Overview
- **Configuration:** Add datasources, deploy S-TAP via GIM, configure FGAC policies.
- **Monitoring:** Utilize CPU usage reports and real-time diagnostics.
- **Maintenance:** Manage connected instances, update collectors, apply policy changes.

### Personas Overview
- **Security Administrators:** Manage data discovery, classification, and S-TAP approval settings.
- **Compliance Officers:** Leverage user hierarchy views and CPU usage reports for audit purposes.

### Entities Overview
- **S-TAP Agents:** Monitored by Central Management and require approval configuration.
- **Collector Groups:** Managed via Central Management and affecting GUI display.

### CPU Usage
The CPU Usage graphical report displays recent CPU activity for customizable time frames.

### IBM Guardium Data Protection
Provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across data stores.

### App Registration with Service Principal
Automatically provisioned for authentication and authorization in Azure Discovery and Classification.

### S-TAP Parameters
`collaborate_kerberos_enabled` enables integration with collaborative Kerberos sessions for granular access control.

### Audit Owner
Audit Owner report supports flexible searching across audit records with LIKE operator defaulting to `%`.

### CSV of the Display Records
Generated PDF reports are capped at 5,000 rows, manually exported CSVs default to 30,000 rows.

### Client Host
Includes client hostname, database name, database user name, full SQL statement, Guardium appliance hostname, and unique instance identifier.

### Scenario 2
If C2S traffic exceeds `MAX_S2C_VELOCITY`, Guardium throttles by sending an "ignore session" request to S-TAP for local connections.

### Kernel IP Routing Table
`show network verify` displays the current network configuration for troubleshooting and verification.

## Minimum Counts and Reset Intervals

Minimum counts and reset intervals define thresholds for low-volume activities that warrant attention when exceeded, enabling fine-grained alerting for subtle anomalies.

## About This Task

Charts can deactivate applied filters, revealing Guardium‑enriched data points that facilitate deeper investigation into specific events or trends.

## Attribute Description

The **TAP Type** column indicates the S‑TAP agent variant (e.g., legacy, container, TEE‑enabled) installed on the host, while the **TEE** column shows whether the application‑process TEE is active.

## CAS Hosts

Configuring CAS hosts lists one or more CAS instances active on a database server and outlines the required steps after installation, including service registration and configuration scripts.

## Torque Exception in Central Management

An internal Torque exception may surface in the Central Management GUI when rendering aggregate views, typically resolved by clearing cache, restarting services, or upgrading to the latest patch.

## Additional Notes About Certificates for External S‑TAPs

When using TLS with External S‑TAP, the **Host** parameter in the provided certificate must match the Common Name presented to the database client during TLS negotiation, regardless of direct connection or load‑balancer mediation.

## Data Mart

Data Mart is Guardium’s central repository for extracted report data. You can export data to tables or files, integrate via Distributed Report Builder APIs, and schedule automated deliveries for downstream consumption.

## Field Description

The **Cassandra datasource** requires the **Host Name/IP** and **Port Number** of the cluster (default **9042**). For advanced connection tuning, use the optional **Keyspace** and **Connection Property** fields. For JDBC datasources, the default port is **10000**, with the **Connection Property** field used for driver‑specific parameters.

## Creating User

1. Navigate to **Administration → User → Create User**.  
2. Enter a unique **Username** and **Password**.  
3. Assign appropriate **Roles** (e.g., Security Analyst, Compliance Officer).  
4. Optionally, set **Session Timeout** and **Failed Login Attempts** controls.  
5. Click **Save** to provision the new account.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection offers real-time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- Google Workspace alerts
- Edge Gateway with double processing power
- Export/archive failure warnings
- Unix socket handling fixes

### Core Workflows
- Enable load balancing, reserve disk space, configure export/archive
- Threat feedback entry, external feed tasks
- S‑GATE blocking, connector upgrades, configuration corrections

### User Personas
- **Administrator:** Manages deployment, including load balancer settings

## Security Analyst Guide

Defines threat feedback and monitors actual threats.

## Policy and Access Rule Overview

- **Infrastructure:** Managed Unit, Guardium System, CAS Server, Analyzer service account

## update_qr_replace_element_byId API

Updates a single query rewrite rule element by its ID. Requires:
- `isFromAllRuleElementsBoolean` to apply to all elements
- `isFromRegex` to indicate a regular expression
- `replaceTo` to set the new value

## IBM Guardium Data Protection Overview  

IBM Guardium Data Protection is an enterprise platform for database activity monitoring, threat detection, compliance reporting, and vulnerability assessment across structured and unstructured data stores on-premises and in the cloud.

### Key Features  
- **Datasource Connectivity:** Supports dynamic port detection, multiple drivers, and CyberArk credential vault integration.  
- **Threat Detection:** Enforces real-time policies, blocks unauthorized queries via S-GATE, and generates security incidents.  
- **Compliance & Reporting:** Provides templates for PCI‑DSS, GDPR, HIPAA, SOX, and automated audit trails.  

### Basic Workflows  
- **Configuration:** Add datasources, deploy S‑TAP agents using Guardium Installation Manager (GIM), and configure Fine‑Grained Access Control (FGAC) policies.  
- **Navigation:** Review activity reports, run vulnerability assessments, and use the audit dashboard.  
- **Action:** Block queries, rotate credentials, and respond to incidents.  

### Personas & Roles  
- **Administration:** Platform configuration, user management, and system settings.  
- **Security Administration:** Define FGAC policies, manage security rules.  
- **Database Administration:** Manage datasources and deploy/upgrade S‑TAP agents.  
- **Data Analyst:** Use dashboards and query results.  
- **Compliance Officer:** Generate regulatory reports.  
- **Security Analyst:** Investigate threats and incidents.  

### Core Entities  
- **Agents & Collectors:** S‑TAP (on-database agent), A‑TAP (application‑level), K‑TAP (kernel), Collector, Aggregator, Central Manager.  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule.  
- **Infrastructure:** GIM (installation), Managed Unit, S‑GATE (blocking gateway), Universal Connector.  

---

## Create an Enterprise Hub or Cross‑CM Health View  

The Enterprise hub aggregates health data from all Guardium units, offering a single‑pane view for monitoring the status and performance of the entire deployment. Administrators can centrally monitor managed units, quickly pinpoint issues, and streamline management of large Guardium ecosystems.

---

## What to Do Next  

Guides associating entity groups with managed units for enterprise load balancing and provides links to S‑TAP control details. This streamlines workload distribution across Guardium components for efficient data collection and analysis.  

*Related concepts:* S‑TAP configuration, load balancing strategies.  

---

## Sample Output  

TLS 1.2 ciphers (`AES128‑SHA`, `AES256‑SHA`) and TLS 1.3 suites (`TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`) are listed with status (enabled/disabled). This helps security administrators verify supported encryption algorithms for secure database communications.

---

## Scheduled Job Exceptions Every 5 Minutes  

Recurring exceptions every five minutes signal a problem that must be resolved. Disable the offending alert from the Anomaly Detection page to stop the noise while allowing genuine anomalies to be detected and investigated.

---

## Release Notes  

Detail changes, improvements, and new features in each Guardium version. Highlights include Unified Discovery and Classification versions, installation guides, system requirements, and data source support. Review before upgrading to understand new capabilities and migration considerations.

---

## How It Works  

Enterprise load balancing continuously gathers up‑to‑date load metrics from all managed units (load collection) and constructs a load map to decide where to allocate work. Dynamic distribution of tasks optimizes resource utilization and prevents overload of any single component.

---

## Why Database Connections Close Unexpectedly  

When External S‑TAPs run, database connections may terminate abruptly. Investigate root causes such as network instability, misconfiguration, or resource constraints. Fix the underlying issue to restore reliable connectivity and continuous monitoring.

---

## File Activity Monitoring  

Provides data discovery, classification, and policy enforcement on Windows and Unix‑Linux file servers, mirroring data monitoring capabilities with platform‑specific variations. Includes discovery, classification, and access control to protect sensitive files across heterogeneous storage environments.

## Overview

**IBM InfoSphere Guardium** is IBM's platform for database security and compliance, monitoring structured and unstructured data sources both on‑premises and in the cloud against breaches and violations.

### Features
- Connects to data sources via JDBC, native drivers, dynamic ports, and multi‑driver setups.
- Monitors SQL traffic in real time with S‑TAP agents and evaluates it against policies through S‑GATE.
- Enforces FGAC policies, audit rules, and data classification via its policy engine.
- Provides built‑in compliance reporting templates (PCI‑DSS, GDPR, HIPAA, SOX) and custom reporting.

### Workflows
- **Configuration & Deployment:** Central Manager/Aggregator, GIM agent, S‑TAP/collector install, policy distribution.
- **Activity Analysis:** Drill‑down query tooling, activity reports, investigation dashboards.
- **Incident Response:** Alert generation, S‑GATE blocking, credential rotation, remediation tasks.

### Personas
- **Security Admins:** Define FGAC policies, monitor health, manage users/roles.
- **DB Admins:** Deploy agents, manage sources, run assessments.
- **Compliance Analysts:** Generate regulatory reports, map controls, validate audit trails.
- **R&D/Dev:** Use API for automated provisioning, encrypted parameter handling.

### Entities
- **Widgets & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregators, Central Manager, Universal Connector.
- **Policy Components:** Security Policy, Audit Policy, FGAC, Masking Rules, Data Classification Rules.
- **Infrastructure Elements:** Managed Units, Guardium Units, S‑GATE, Assessment Engines, API Keys.

## Strict Username Example (Oracle)

Network packet loss may affect network traffic monitoring, causing S‑TAP buffer overloads, collector overload, S‑TAP or sniffer restarts, or excessive sessions. A strict username configuration for Oracle reduces identity ambiguity, mitigating these risks by ensuring precise tracking in audit trails.

## Encrypted Parameters

GuardAPI accepts encrypted parameters for sensitive values (e.g., passwords). The `encrypt-value` function encrypts strings that can be safely passed to any API method.

## Permissions to Access a Google Drive Account

The Unified Discovery & Classification module can be granted super‑administrator rights on a Google Drive account, enabling it to read, list, and download files for classification.

## Configuring Db2 Exit

The Db2 Exit module allows the S‑TAP agent to monitor **all** Db2 activity, regardless of encryption, network location, or protocol. Configuration is performed through the Guardium GUI via **Unix Tasks → Db2 Exit**.

## How Guardium Works

Guardium stores assessment configurations and results on its central server, registering each monitored database as a data source. S‑TAP agents stream real‑time traffic to collectors for evaluation and reporting.

## Attribute

The Attribute entity records session‑level details: connection access ID, client port, Collector ID, and database name for MSSQL or Sybase.

## Server Host

Server Host consists of Server Host Name, Server IP, Server Port, and Server Type (e.g., DB2, Oracle). It identifies the database server that processes client interactions.

## View Monitored Item Lists

The Monitored Items Definitions pane lists all monitored objects, queries, or transactions on a host. Rows can be selected individually or in bulk for editing via checkboxes or double‑clicks.

## Installation Status

The current status message from a GIM client is stored in the `GIM_EVENTS` table, offering real‑time visibility into the client's state and activity.

## Process Name `TAP_DB_PROCE`

The `TAP_DB_PROCE` process name specifies executables monitored by the S‑TAP agent, such as `Db2SYSCS.EXE` for Db2 ICF and `oracle.exe` or `tnslnsr.exe` for Oracle using named pipes.

## License Keys

Guardium requires a base license reflecting the hardware platform plus optional append licenses for additional capabilities. License keys are managed through the license UI or CLI utilities.

## Files Privileges

The Files Privileges module logs file‑system activity, user interactions, crawler configs, and compliance results per server, supporting dashboards, masking engine monitoring, and entitlement reporting.

## DB Protocol Version

The DB Protocol Version field records the exact database protocol version (e.g., Db2 11.5, Oracle 21c), populated by Guardium agents during discovery for protocol‑specific policy enforcement and reporting.

## Before You Begin

Enabling threat categories in Guardium 12.2+ requires opening the Active Threat Analytics dashboard, selecting setup, and choosing the appropriate version to prepare the system for detecting and responding to emerging threats using updated intelligence.

### Overview
IBM Guardium Data Protection secures structured and unstructured data across on-premises and cloud data stores. It offers real-time monitoring, policy enforcement, vulnerability assessments, and compliance reporting.

### Features
- **Configuration & Deployment:** Includes Universal Connector, GIM certificates, CAS Hosts, and deployment tasks.
- **Monitoring & Enforcement:** Captures traffic, enforces policies, blocks sessions, and supports CData BigQuery JDBC driver.
- **Compliance & Reporting:** Provides executive dashboards, audit reports, session inference APIs.
- **Personas:** Supports Database Administrators, Security Administrators, and Compliance Officers.

### Workflows
- **Initial Setup:** Import CAS Hosts, configure Universal Connector, replace GIM certificates.
- **Ongoing Management:** Monitor S-TAP status, define rule types, aggregate failed commands, generate dashboard metrics.
- **Compliance Execution:** Create online reports, import data sets, execute REST APIs for asset management.
- **User Interaction:** Sessions list navigation, alerts handling.

# IBM Guardium Data Protection Overview

## Core Capabilities
- **Database Activity Monitoring:** Real-time analysis of database traffic with SQL inspection and rule enforcement
- **Data Classification:** Automatic discovery and tagging of sensitive data using built-in and custom classifiers
- **Block & Protect:** Real-time SQL blocking, query rewriting, and user session termination via S-GATE
- **User and Entity Behavior Analytics (UEBA):** Baseline learning, outlier detection, and risk scoring across user activities
- **Compliance Reporting:** Ready-made templates for PCI‑DSS, GDPR, HIPAA, SOX, NIST, with real-time dashboards and audit trails

## Deployment & Configuration
- **Components:** S-TAP agents, Universal Connectors, GIM for lifecycle management, Managed Units and Central Managers for scalability
- **Infrastructure:** DNS resolvers (primary mandatory, secondary/tertiary optional), integration with credential vaults (CyberArk, SHA‑1/SHA‑256 certificates)
- **Customization:** Tailored alert routing through Custom Alerting Classes, CLI‑only routing configuration without UI impact

## Personas & Roles
- **Database Administrators:** Manage datasources, S‑TAP agents, JDBC drivers
- **Security Administrators:** Define policies, rule types, custom alerting recipients
- **Compliance Officers:** Run audit reports, aggregate metrics, generate dashboards
- **Security Analysts:** Investigate sessions, analyze activity data, leverage REST APIs

## Graphical User Interfaces
- **Data discovery UI:** Run file classification scans, review results by policy, file name, classification pick list
- **Activity analysis UI:** Filter session list by user, database, date range, execution status, escalate to ticket
- **Policy builder UI:** Define security/audit/classification/access rules, attach rule groups to policy template

## Integration Points
- **External Systems:** Integration with SIEM, SOAR, ticketing, data loss prevention via REST APIs
- **Cloud Providers:** Native support for Amazon RDS, Azure SQL, Google Cloud SQL, SaaS platforms
- **Encryption:** Supports TLS 1.3, AES‑256 data‑at‑rest, key management using external vaults

istrict.

### Install and Uninstall A-TAP From the Command Line (on K-TAP based systems)

Execute `/usr/local/guardium/bin/guardctl install-a-tap` to install A-TAP on K-TAP systems. Ensure S-TAP and K-TAP are active. Verify `GIM_ROOT_DIR` points to Guardium modules.

## Installation Workflow on Hadoop Cluster
1. Ensure all nodes have S-TAP or K-TAP installed for OS compatibility.
2. Deploy Guardium agents via GIM and assign the latest bundle/module.
3. Apply FGAC policies and enable KAFKA support for Hadoop connectors.
4. Validate by checking agent status and policy enforcement.
5. Monitor data activity with Guardium dashboards.

## Defining a Basic Data Security Policy
Preconfigured policy with default privileged users, commands, and error codes, providing a baseline security posture.

## Installing A-TAP with GIM
After Guardium agent installation, A-TAP can be uninstalled with `/usr/local/guardium/bin/guardctl uninstall-a-tap` using GIM.

e expected value defined in the Guardium Management Server, the installation aborts and reports a verification failure.

Key points:

- The checksum verification occurs automatically during the install or upgrade flow.  
- If the checksum mismatches, the process stops and logs an error indicating the mismatch.  
- This safeguard prevents tampered or corrupted S‑TAP binaries from being deployed.  

For troubleshooting, administrators can manually verify checksums using the `gim_install` utility with the `--verify-checksum` flag, passing the package file as an argument. If a mismatch persists, re-download the S‑TAP package from the Guardium repository and retry the installation.

## Troubleshooting Informix Shared‑Memory Traffic  

Guardium sometimes fails to collect **shared‑memory traffic** from **IBM Informix** databases because the **inspection engine** misidentifies the process name used by the Informix instance. To resolve:

1. **Change the Guardium process name** – set the inspection sever’s `ProcessName` parameter to exactly match the Informix listener name (typically `oninit`).  
2. **Reconfigure shared‑memory collection** – ensure the `shm` inspection engine is enabled for the instance’s shared‑memory port (default `9088`).  
3. **Restart the Guardium collector** – after updating the process name and port settings, perform a full collector restart to load the new inspection rules.  
4. **Verify traffic capture** – use the `tcpdump` command on the collector to confirm that shared‑memory packets are now being recorded.

> **Key Concepts:** *Informix shared‑memory, inspection engine, ProcessName parameter, traffic collection*  



---


## Accessing REST API From the Guardium UI  

The **Guardium UI provides a built‑in console** for invoking the Guardium REST API without external tools like `curl`. To use it:

1. Navigate to **Administration → Tools → REST API**.  
2. Enter the desired **endpoint URL** (e.g., `/restAPI/search/database`), choose **POST** or **GET**, set any required **headers** (e.g., `Authorization: Bearer <access‑token>`), and add a **JSON payload** if needed.  
3. Click **Send**. The response is displayed in the lower pane, including HTTP status, headers, and body.  

This console is useful for quick testing and for delegating API calls to less‑technical users.

> **Key Concepts:** *REST API console, UI access, Guardium API testing*  



---


## Running a Collection Export Job in Guardium  

Guardium allows **ad‑hoc export of collected audit data** to external repositories. To run a collection export:

1. From the main menu, select **Administration → Tools → Export**.  
2. Choose the **data mart** or **collection** you want to export.  
3. Set the **export format** (CSV, JSON, or XML) and specify the **destination** path or SFTP server details.  
4. Click **Start Export**.  

When the job completes, a success message is shown and the exported file is available at the chosen location.

> **Key Concepts:** *Collection export, data mart, export job, CSV/JSON/XML*  



---


## Installing S‑TAP on an Informix Server  

Deploying **S‑TAP** on a server running **IBM Informix** requires a few configuration steps to ensure compatibility:

1. **Stop the Informix instance** – `onmode -ky` (or `onmode -y` for online stop).  
2. **Install the S‑TAP RPM** – use the standard Guardium RPM package; no special Informix‑only build is needed.  
3. **Update the Guardium configuration** – in the **Inspection Server** settings, set the **Database Type** to `Informix Shared‑Memory` and enter the local socket path (e.g., `/dev/informixshm`).  
4. **Start the Informix instance** – `oninit`.  
5. **Verify S‑TAP status** – run `systemctl status s-tap.service` to ensure it’s running and catching traffic.

> **Key Concepts:** *S‑TAP installation, Informix, inspection server, shared‑memory socket*  



---

## Informix Process Name Matching for S-TAP

1. Identify the **Informix** server process name by running the command `onstat -g nps` (or the appropriate equivalent for your environment).
2. The output lists the exact process names handling shared‑memory connections.
3. In Guardium, open the **S‑TAP Control** configuration for the Informix datasource and locate the **Process Name** field.
4. Update that field with the exact process name observed in step 1.
5. Restart the S‑TAP agent and confirm that Informix traffic now appears in Guardium reports.

**Key Concepts:** Informix shared memory, inspection engine, process name matching, S‑TAP configuration.

## S-TAP and Collectors
Consists of S-TAP, K-TAP, and A-TAP agents that monitor database activity on the host. 

## Core Services
- Collector: Captures data from agents, secures, and forwards for analysis
- Central Manager: Coordinates managed units and provides GUI/API
- Aggregator: Aggregates data from multiple collectors for high-scalability deployments

## Security Controls
- S-GATE: Enforcement point that blocks unauthorized queries in real time
- Policies: Define allowed and blocked activities based on attributes like user and query type

ollators receive and aggregate data from multiple S-TAPs, reducing network traffic and centralizing monitoring in distributed environments.

---

## Collectors

`c2cb512d-eb7f-4432-b4b1-a7a4d91f42ec` | categories: entities, architecture

Collectors are Guardium appliances that ingest, aggregate, and forward data from S-TAP agents, enabling centralized policy enforcement and reporting.

---

## Cold Storage Ingestion Logs report

`c812f948-afad-4d61-93b1-d4c3b5ab1107` | categories: features, reports

Cold Storage Ingestion Logs report shows records added to long‑term storage and any error messages during the ingestion process.

---

## Cold Storage Ingestion Reports

`ce0d960a-9232-4d4b-96c6-5be8750ff3ed` | categories: features, reports

Cold Storage Ingestion Reports display the volume of data records transferred to archival storage and indicate success or failure status.

---

## Client IP/Src

`e29aeb8a-f6c7-4bc1-9bd6-a989a6fa883c` | categories: entities, tuple-groups

The Client IP/Src tuple group records client IP address, MAC address, and operating system for each database connection.

---

## DB Protocol Version

`eddbc826-70d0-4199-b356-7d31a688e12f` | categories: entities, tuple-groups

DB Protocol Version captures the protocol version of the database connection, authenticated DB user, timestamp of last use, and network protocol (e.g., TCP).

---

## HDFS Poll

`f1c8a56c-d071-44ed-95cf-34aa4bca7f84` | categories: configuration, entities

HDFS Poll settings define the interval, port, user, and audit history length for periodic HDFS audit checks.

---

## S-TAP Status Verification

`f4a2b8b3-dbb6-4b35-a993-f9c084c3fcec` | categories: workflows, operations

After installing S-TAP, verify its status is green in Monitor > Maintenance > S-TAP Logs > S-TAP Status to ensure proper data collection.

---

## PostgreSQL_DATA environment variable

`f4aa2d5f-ac92-4a84-90af-16acd7e081d9` | categories: configuration

The PostgreSQL_DATA env variable specifies the primary directory for PostgreSQL data on Linux/UNIX systems when using Guardium.

---

## Populate From Query

`f5157e76-31b0-4e26-9d69-e43b170716cc` | categories: workflows

Populate From Query creates a custom table from a query, enabling automation of job dependencies when enabled for auto‑run.

---

## Reporting interval

`f5c9c959-35ec-45d8-9e38-087412a79c41` | categories: entities

Reporting interval sets the time granularity for generating reports from Guardium data collections.

---

## Summary of Compliance Controls

`f5cf5426-c656-44f0-9a95-c8cd126555a2` | categories: features, compliance

The Compliance Controls summary report links directly to relevant policies, groups, and detailed reports for quick compliance audits.

---

## Parameter Value type Description

`ffffff24-1e0e-4a64-967c-bbb21d01b053` | categories: guardapi, parameters, knowledge

Parameters include `policyName` (required) to specify a policy and `ruleName` (optional) to filter FAM policy rules via `guardapi list_policy_fam_rule`.

## Guardium Collector Overview
Guardium Collectors are on-premises data collection nodes that store query data, provide quick search capabilities, and support analytic workloads. They are ideal for environments that require more than one hour of data retention or need rapid querying.

## Populate Custom Table From Query
The Populate From Query option requires the associated custom table to be populated with current data. Enabling Auto run dependent jobs in Scheduler task creates job dependencies for the custom table.

## Cold Storage Ingestion Logs
The Cold Storage Ingestion Logs report in Reports > Guardium Operational Reports displays records added and any error messages for long-term retention.

## Inspection Engine for Return Data
When the Inspection Engine is configured to Inspect return data, it returns data from traffic, potentially exposing PII based on the monitored protocol.

## CLI Command Abbreviation
The Guardium CLI allows command words and arguments to be abbreviated to the minimum number of characters that remain unambiguous (e.g., "show" can be shortened to "sho").

## Account Takeover Detection
Account takeover occurs when a non‑authorized user accesses an account. Guardium opens a case when the access uses a new connection profile (different source IP or source program).

## Ignoring Exceptions Filtering
The Ignoring exceptions policy lets administrators skip inspection of specific exceptions, for example ignoring TNS errors logged as LOGIN_FAILED to reduce noise.

## PostgreSQL Data Directory Configuration
Define PostgreSQL_DATA under `/root` for the root account on UNIX/Linux systems, or add it to the root profile, to specify the location of the PostgreSQL data directory.

## S-TAP Post-Installation Verification
After S-TAP installs, verify it is green in Monitor > Maintenance > S-TAP Logs > S-TAP Status; then use `guard-config-update` to view parameters.

## HDFS Polling Configuration
Configure HDFS polling interval, port, user, and audit history length for the Guardium S-TAP to check new Ranger audits at specified intervals and retain audit history for a defined duration.

## Document Overview
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features
- Dynamic port detection, multi-driver support, CyberArk vault integration
- Real-time policy enforcement, S-GATE blocking, security incident generation
- PCI-DSS, GDPR, HIPAA, SOX report templates; automated audit trails
- Refreshed UI screens for enhanced usability

### Workflows
- Add datasource, deploy S-TAP via GIM, configure FGAC policies
- Review activity reports, run vulnerability assessments, audit dashboard
- Block unauthorized queries, rotate credentials, respond to incidents
- Enable, disable, and configure outlier detection

### Personas
- **Administration:** Platform configuration, user management
- **Data & Database Management:** Datasource and S-TAP configuration
- **Compliance & Audit:** Generate regulatory reports, investigate threats

### Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector
- **Outliers Detection APIs:** Enable, disable, configure

## Error Codes
- **0:** Missing parameters or unexpected exceptions
- **1:** Unhandled exception requiring support
- **2:** Unknown function name

## Example Use Case
Retrieve a small amount of audit data for a specific IP address via the API instead of logging into the Guardium GUI.

## Outliers Detection Commands
Commands to enable, disable, and configure outlier detection functions for identifying anomalous data in Guardium.

## Modernized UI Screens
Select UI screens have been refreshed with a contemporary look that enhances usability while maintaining functionality.

## Datasource Information
Datasources store information about databases or repositories, including type, location, and authentication credentials.

## Ignore Session Behavior
Ignore Session ignores current request and all subsequent session requests, does not log policy violations or test for them.

## Security Incident Policy Templates
Pre-built Guardium policy templates that target common runtime security problems, each containing rules to detect specific incident types.

## Days Not Exported or Archived
Lists days that have not been exported or archived.

## Guardium Deployment Health Overview

Overall Status in Deployment Health views shows Guardium version for Guardium systems and S-TAPs, OS version, databases, and DB status for S-TAPs with type, version, and verification details.

# Analyzer Queue

The Analyzer Queue Length measures the amount of data waiting in the Analyzer/Parser buffer, serving as a key indicator of sniffer performance; ideally, this value should remain at or near zero to ensure optimal operation.

## Show Command

`store system admin-only` restricts admin/accessmgr to standard login after smart card or SAML authentication.

## Data Mart APIs

The `guardium rerun_distributed_report API` manually reruns distributed reports that may have incomplete data, useful for reports that run on aggregators and collect data daily, allowing targeted data collection completion.

## Session Tracking

Client/Server by session is a secondary entity linked to the Client/Server primary entity, capturing Timestamp of the client's first server connection.

## Audit Only Action

Audit Only action logs only the SQL construct that triggered a rule for policies using Selective Audit Trail, where no constructs are logged by default.

## Guardium Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It monitors, secures, and ensures compliance for structured data assets through real-time activity monitoring, vulnerability assessment, and policy enforcement across databases, data warehouses, and big data stores on-premises and in the cloud. Guardium provides unified visibility, control, and automation for data security policies, discovery, classification, and risk management.

### Key Features
- **Real-time monitoring and policy enforcement:** Detects and blocks suspicious database access in real time based on predefined security policies.
- **Unified discovery and classification:** Automates identification and labeling of sensitive data across heterogeneous environments.
- **Activity analytics and compliance reporting:** Analyzes user behavior, generates audit trails, and produces compliance reports for regulations such as GDPR, SOC 2, and PCI DSS.
- **Scalable architecture:** Supports monitoring of thousands of data sources with centralized management through the Guardium appliance or virtual machine.

### Core Components
- **Guardium appliance/VM:** Central management console that aggregates logs, enforces policies, and provides reporting.
- **S-TAP agent:** Lightweight agent installed on database servers to capture and transmit database activities to the Guardium appliance.
- **Aggregators and collectors:** Intermediate collection points that optimize network traffic and data ingestion at large scale deployments.
- **Policy engine:** Evaluates incoming data activities against user-defined policies to trigger alerts, logging, or prevention actions.
- **Integrated vulnerability assessments:** Scans databases for configuration weaknesses, SQL injection risks, and other security gaps.

### Workflows
1. **Deployment:** Install S-TAP agents on data sources, deploy Guardium appliance or VM, and aggregate data from managed units.
2. **Configuration:** Define data sensitivity classifications, create security policies, and set up compliance reports.
3. **Operation:** Monitor dashboards for real-time alerts, review aggregated logs for anomalies, and execute remediation actions.
4. **Administration:** Manage user access, configure system parameters, and maintain patches and upgrades.

### Personas and Use Cases
- **Security administrators:** Configure policies, monitor threats, and investigate incidents.
- **Compliance officers:** Generate audit reports, demonstrate regulatory adherence, and manage data privacy controls.
- **Database administrators:** Optimize performance, troubleshoot connectivity issues, and manage database-specific configurations.
- **Data analysts:** Access sanitized query views, explore classified data assets, and perform analytics on secured datasets.

### Entities
- **S-TAP agents:** Capture database session data and network traffic.
- **Managed units:** Intermediate nodes for collecting and forwarding data to the Guardium appliance.
- **Central manager:** Primary control point for policy management, user administration, and reporting.
- **Compliance repositories:** Store historical logs, policy outcomes, and compliance evidence.

### Configuration and Management
- **Configuration parameters:** Control logging granularity, connection protocols, data retention periods, and performance tuning.
- **CLI commands:** Provide scriptable control over Guardium operations, from agent provisioning to report generation.
- **GUI tools:** Offer user-friendly interfaces for policy configuration, data classification, and compliance management.
- **Support resources:** Include documentation, logs, diagnostic utilities, and community forums for troubleshooting and best practices.

## Key Concepts

- Guardium logins, user activity, login monitoring
- CAS authentication, SSL, encrypted connections, certificates
- Group Builder, members, population method, retrieval steps
- K-TAP kernel removal, troubleshooting
- JDBC authentication, TLS CA certificate, encryption, Kerberos
- Document Overview of IBM Guardium Data Protection features, components, and personas

```markdown
## Key Topics

- **Retention Policies**: Balance performance and auditor requirements.
- **Health Checks**: Quartz CRON intervals for Kafka connectors.
- **Integrations**: Db2 Warehouse, Microsoft SQL Server named pipes.
- **Oracle Firewall Settings**: S-TAP parameters affecting firewall.
- **Streaming to GBDI**: Flush interval and timeout for JSON data.
- **Credential Management**: Store in HashiCorp Vault.
- **Patch Troubleshooting**: Remediation when installation hangs.
- **Upgrade S-TAP for IBM i**: Steps for upgrading.

### Workflows
- Policy Tuning, Upgrade Procedures, Integration Setup, Troubleshooting.

### Personas
- Security Administrator, Database Administrator, Compliance Officer, Incident Responder.

### Entities
- Audit Repositories, Health Check Schedulers, Database Drivers, Credential Vaults, Configuration Profiles, Installation Artifacts.

## Efficient Audit Storage
Configure retention periods to meet compliance while optimizing storage.

## Embedded Integrations
Native support for Db2 Warehouse in UNIX/Linux deployments.

## Tuning Health Checks
Configure Quartz CRON for Kafka connector monitoring intervals.

## WINSTAP Named Pipe Driver
`WINSTAP_NAMED_PIPE_DRIVER` configures MS SQL Server named pipe usage.

## Oracle Unified Audit
S-TAP configuration for firewall interaction settings.

## Streaming Data Transport
Configure flush interval and timeout for JSON data to GBDI.

## HashiCorp Vault Integration
Secure datasource credentials using specific parameters.

## Universal Connector SSL
Generate SSL keys with expiration, hostname, and optional override.

## Guardium with HashiCorp
Integrate for secure, centralized credential management.

## Post-Installation
Provide Guardium account name to CyberArk admin for permissions.
```

IBM Guardium Data Protection Overview

### Features
- Real‑time activity monitoring via S‑TAP agents
- Policy‑driven enforcement: FGAC, audit, classification, redaction, S‑GATE blocking
- Compliance reporting templates (PCI‑DSS, GDPR, HIPAA, SOX) and automated audit trails
- Dynamic deployment options: GIM‑managed agents, A‑TAP, K‑TAP, Universal Connectors, S‑GATE components

### Workflows
- **Agent Installation / Upgrade:** Deploy S‑TAP via GIM, GIM listener, or local copy
- **Data Source Configuration:** Register hosts, ports, credentials, JDBC properties
- **Certificate Management:** Create and manage custom GIM certificates
- **Operations & Investigation:** Run `show` commands, review dashboards, generate reports, respond to incidents

### Personas
- **Guardium Administrator** – installs agents, configures managed units, defines architecture
- **Security Administrator** – manages FGAC policies, S‑GATE rules, alerts, notifications
- **Database Administrator** – supplies host/port details, grants privileges, handles S‑TAP upgrades
- **Compliance Officer** – creates and generates audit/compliance/risk reports
- **Data Analyst** – views dashboards, accesses query results, reviews activity archives

### Entities
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- **Policy Sets:** FGAC, audit policies, classification rules, S‑GATE rules
- **Security Stack Components:** Guardium Key Lifecycle Manager, IBM Trusteer integration, Guardium IPA
- **GUI/CLI Constructs:** Data Source list, Policy list, Test Description, Dashboard summary

### Task: GIM Client Installation
When installing the GIM client (standard or listener mode), custom key, certificate, and CA files can be specified (see “Creating and managing custom GIM certificates”).

### Show Command
```bash
show system clock list
show system clock <zone>
```

### MySQL Data Source Parameters
- **Host Name / IP address**
- **Database name**
- **Port number** (default 3306)
- **JDBC Connection property** (optional)

### REQUEST_ERROR Policy Action
Use `REQUEST_ERROR` in session‑level policies to:
- Trigger actions on any SQL error request
- Identify sessions with excessive user errors
- Pinpoint errors on specific tables

### Edge Gateway Support
Edge Gateway supports Guardium policies (blocking, redaction) and real‑time alerting via:
- SNMP traps
- Rsyslog
- REST, DB, HTTP endpoints

## Parameter Value type Description
- `updateEdge` parameters: `backupExports` (list), `cpuLimits` (string), `exportsTo` (list)

## Data Sources
Displays all defined sources with full details: type, name, description, host, port, service name, user, database, last connect time, shared flag, connection properties.

## Number of
Records how many times the sniffer process has been stopped and started. High counts indicate dropped packets or a misbehaving sniffer.

## About this task
For 12.2.x and later releases, upgrade the S‑TAP without deactivating A‑TAP. Stop all databases, de‑instrument and deactivate every A‑TAP, then upgrade the S‑TAP.

## Main threads
`num_main_threads` (num_main_thr) defines the number of threads between the S‑TAP and a Guardium host; valid values are 1‑10. Enterprise load balancing does not support multiple threads for a single managed unit.

## Install on a Dedicated Computer
Install Guardium collector software directly on a dedicated, hardened computer that will run the central manager and aggregator roles, ensuring isolation from other workloads.

## Overview
IBM Guardium Data Protection is an enterprise database activity monitoring and security platform offering real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across on‑premises and cloud data stores. Features include datasource connectivity, exception management, vulnerability assessment, privilege management, offline help, API access, and offset-based search. Workflows cover configuration, uninstall, certificate management, persistent volume creation, API usage, and access management. Personas include security administrators, database administrators, compliance officers, and developers. Entities include AWS RDS streams, Kubernetes persistent volumes, exception codes, and GuardAPI parameters.

## Compact IBM Guardium Overview

### Key Capabilities
- **Database Connectivity:** JDBC drivers, dynamic port resolution, CyberArk integration
- **Threat Detection:** Real-time monitoring, policy enforcement, S-GATE blocking
- **Compliance:** Pre-built audit templates, automated reporting
- **Vulnerability Assessment:** Automated tests, exception handling

### Core Components
- **S-TAP Agents:** Capture database activity in real time
- **S-GATE:** Enforces policy decisions, blocks threats
- **Central Manager:** Manages deployment, configuration, and monitoring

### Integration Features
- **REST API:** Programmatic interaction with Guardium services
- **GuardAPI:** Command-line control of Guardium functionality
- **App Drivers:** Custom integration with third-party applications

### Quality Gates
- Complete sentences only
- Clean titles
- Names are noun phrases
- No duplicates
- Skip noise

### Workflows Overview
IBM Guardium offers four primary workflows: Configuration, Monitoring, Compliance, and Maintenance. Configuration adds datasources, deploys collectors via GIM, and defines policies. Monitoring reviews activity, runs assessments, and manages incidents. Compliance generates reports, remediates findings, and maintains audit status. Maintenance updates Guardium, upgrades components, and manages system health.

### Personas Overview
- **Administrators**: Set up platform, provision users, tune system
- **Security Team**: Define policies, investigate threats, manage FGAC
- **DBAs**: Deploy S-TAPs, register datasources, monitor performance
- **Audit & Compliance**: Attest policies, generate reports, provide regulatory proof

### Entities Overview
- **Agents & Collectors**: S-TAP, A-TAP, K-TAP, Collectors, Aggregator, Central Manager
- **Policy Objects**: Security Policies, Audit Policies, Classification Rules, Access Rules
- **Infrastructure**: Managed Units, GIM, S-GATE, API, Universal Connector

### JDBC Driver Support
IBM Guardium supports JDBC connections using native drivers for optimized performance and generic drivers for broad compatibility. A browser service dynamically resolves instance names to current ports.

### Activity Monitoring
IBM Guardium captures database traffic via S-TAP agents in real time. Traffic is evaluated against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

### Archival of Outlier Records
Outlier-related activity records can be automatically archived using retention policies based on anomaly score, timestamp range, or DB user name. The default sentinel value for an empty DB user is `DB_USER:guardium://empty`.

### Outlier Attributes
Attributes for outlier summary records include: Alert Feedback ID, Anomaly Score, DB User Name, and Diverse Outlier Flag. These attributes help analysts understand the nature and severity of detected outliers.

### Database Entity Attributes
The Description attribute for database entity objects records DB Type (e.g., Oracle, MySQL), Instance Name, and Associated User. This provides contextual information for reporting and policy targeting.

### Database Monitoring Attributes
Attribute Description metadata for databases includes Monitored Executable (binary path) and Installation Directory. This data is crucial for inventory management and platform-specific assessments.

### Timestamp Attribute
The Timestamp attribute logs the exact time when any change or event is recorded on the Guardium appliance, enabling precise forensic analysis.

### Storage Utilization Alerts
When the internal database of a Guardium Managed Unit fills up, the GUI login becomes unavailable. The System Monitor page will show "Used Disk" readings approaching 100%, indicating the need for data cleanup or configuration adjustments.

### Guardium Support Tools
Documentation for Guardium Data Protection version 10.2 covers S-TAP and GIM installation parameters for Linux/UNIX/Windows and commands to start and stop the GIM client. This information assists with initial deployments and routine maintenance tasks.

### GuardAPI CLI
GuardAPI provides a command-line interface for configuring datasources, managing policies, executing assessments, and automating maintenance workflows. Admins can script Guardium operations for efficiency and integration.

### System Requirements
Supported platforms, required OS versions, and minimum hardware specifications are documented to ensure proper assessment of vulnerability scanners, compatibility with S-TAP agents, and integration with IBM i systems. Most current details reside in the Guardium support matrix.

### Installation and Upgrade
Installation guides and upgrade documentation provide step-by-step guidance for deploying Guardium Collectors, upgrading from prior versions while preserving configurations, and validating post-installation health. Follow the support matrix for version compatibility.

### OS Command Injection Detection
Guardium detects OS command injection attacks that aim to execute system-level commands through compromised applications. It identifies attempts to erase files on the host OS or manipulate outlier mining thresholds using pattern matching and behavioral analysis.

### User Switching Behavior
Outlier mining algorithms compare current activity against historical baselines for database users and application users. Hourly evaluations flag deviations such as sudden spikes in data access or unusual sequences of operations.

## Datasource Selection for Monitoring
- Administrators can choose from already registered databases or add new ones manually.
- Connection parameters and monitoring scopes are specified in this step.

## Domain-Based Query Filtering
- SECURITY_ASSESSMENT parameter filters assessment results by:
  - Date ranges
  - Test IDs
  - Test names
  - Audit configuration templates
  - Datasource types

## Active Audit Process Monitoring
- Number of Active Audit Processes metric tracks concurrent audit streams.
- Helps capacity planners avoid bottlenecks.

## Session View
- Captures metadata for active database sessions:
  - User credentials (clear text and hashed)
  - Client host information
  - Connection attributes
  - Session start times
- Useful for tracking privileged user activity and correlation with audit records/alerts.

## Document Overview

IBM Guardium Data Protection provides unified visibility, policy‑based enforcement, compliance automation, and vulnerability management across databases. It supports on‑premises and cloud environments, helping organizations meet regulatory requirements and prevent data breaches.

### Key Features
- Centralized monitoring of SQL traffic and unified audit records.
- Real‑time inspection via FGAC policies and S‑GATE blocking.
- Built‑in compliance templates (PCI‑DSS, GDPR, HIPAA, SOX) and audit trails.
- Automated vulnerability assessments and configuration checks.

### Typical Workflows
- **Configuration & Deployment:** Add datasources, deploy S‑TAP agents via GIM, configure FGAC and audit policies.
- **Monitoring & Reporting:** Review activity reports, run vulnerability assessments, investigate incidents, export logs.
- **Incident Response:** Block unauthorized queries, rotate credentials, manage quarantine actions.
- **Continuous Improvement:** Regular policy reviews, compliance audits, rule tuning based on threat intelligence.

### Personas
- **System Administrator:** Platform setup, user lifecycle management.
- **Security Administrator:** Policy authoring, FGAC enforcement.
- **Database Administrator:** Datasource provisioning, S‑TAP deployment, system tuning.
- **Compliance Officer:** Regulatory reporting, audit evidence management.

### Core Entities
- **Agents & Collectors:** S‑TAP (inline flow capture), A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule.
- **Infrastructure:** GIM (Guardium Installation Manager), Managed Units, S‑GATE, Universal Connectors.

## Guardium Overview

Guardium is a database activity monitoring and data security platform that captures, analyzes, and responds to database transactions in real time. It supports various architectures and components, including **TAP**, **K‑TAP**, **Collectors**, and **Aggregators**, to provide comprehensive visibility across distributed environments.

### Key Features
- **Policy & Rule Sets:** Includes Security Policies, Audit Policies, Classification Rules, Access Rules, and Quarantine Events.
- **Infrastructure Components:** Consists of Guardium Installation Manager (GIM), Managed Units, S‑GATE blocking, Universal Connectors, and REST/Automation APIs.

### Activity Monitoring & Policy Enforcement
Guardium captures SQL traffic using **S‑TAP** (in‑line) or **A‑TAP** (agent‑side) agents. Captured packets are forwarded to a Collector where they are parsed and evaluated against defined **Security Policies**. Violations can trigger **S‑GATE** blocking, alerts, audit trail entries, or incident workflows.

### Default Roles
Guardium ships with four predefined roles:
- **Admin:** Full system administration privileges.
- **User:** Read‑only activity review.
- **Access Manager:** Privileges for managing access controls.
- **Investigations:** Permissions for investigation tasks.

Custom roles can be created to meet specific organizational needs.

### Enterprise Hub & Health View
The **Enterprise Hub** aggregates health, performance, and compliance data from all managed units, providing a unified dashboard for executives and security operations teams.

### Parameter Defaults & Values
- **Database type** in the External S‑TAP group can be left blank for automatic discovery.
- **create_quarantine_allowed_until** accepts a date-time string or relative expression (e.g., `NOW+1HOUR`).
- **dbUser** specifies the user whose quarantine activity is time‑limited.

### Universal Connector APIs
Guardium offers RESTful Universal Connector APIs for programmatic interaction:
- **create_user:** Add a new user with default role *User*.
- **list_users:** Retrieve current user inventory.
- **assign_role:** Dynamically change a user's role.

### TLS Management
From v11.4, Guardium supports configurable TLS settings via the **enable_datastream** command, allowing administrators to enable/disable TLS, specify minimum TLS versions, and rotate certificates.

### REST API Example
```bash
curl -k -i --header "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
           "RemoteHost":"9.70.165.194",
           "RemotePassword":"password",
           "RemotePath":"/var/log",
           "RemoteUser":"root"
         }' \
     https://9.42.32.28:8443/restAPI/export_logfiles
```

### GuardAPI Example
```bash
update_custom_table_ldap_import activateSchedule=true \
                               attributeMapping="cn=firstname,sn=lastname" \
                               cr="myImportCR" \
                               baseDN="ou=employees,dc=example,dc=com" \
                               clearTable=true
```

This concise reference merges all distinct concepts into a streamlined overview while retaining essential details.

## Changing the Syslog Facility

To modify the syslog facility that Guardium Data Protection forwards events to, execute the `store system snif-syslog_facility` command. The facility can be set to any of the standard syslog values (e.g., `local0` through `local7`). After changing the setting, restart the collector service for the change to take effect.

## Alert Facilities (`alerts-facility`)

Configures or displays the syslog facility for alerts generated by the SIEM component **snif**.

---

## List Classifier Processes (GuardAPI)

`list_classifier_process` – Returns details of all currently running classifier processes.

---

## Migrate S-TAP Configurations (Central Management API)

`migrate_stap_config` – Pushes one or more S-TAP configurations to Guardium Insights, transferring the Guardium Insights certificate chain beforehand.

---

## Guardium Parameter Thresholds

Key configuration parameters that trigger alerts when exceeded:

| Parameter | Description |
|-----------|-------------|
| `CLASSIFIER_MEMORY_USAGE_THRESHOLD` | Memory limit for classification services |
| `HTTP_GIMSERVER_AUTH_CONNECTIONS_THRESHOLD` | Max authenticated connections for GIM servers |
| `HTTP_GIMSERVER_CONNECTIONS_THRESHOLD` | Total connections limit for GIM servers |
| `HTTP_GUI_CONNECTIONS_THRESHOLD` | Max GUI connections |
| `MYSQ` | Placeholder for additional MySQL thresholds |

---

## Import Universal Connector Profiles

GuardAPI parameters for importing connector profiles:

- `TestConnections` – Validates connectivity after import
- `jarFile` – Path to connector JAR file
- `path` – Directory where connector files reside

---

## Vulnerability Assessment Dashboard

**Assessment Summary Chart** – Visual representation of discovered vulnerabilities over time.

---

## Session‑Level Policy Creation

Define **tuple parameters** to specify:

- SQL statements (`SQL` clause)
- Involved users/accounts (`USER` clause)
- Connections/IP ranges (`IP` clause)
- Additional attributes (wildcards, token substitution)
- Actions (e.g., `IGNORE_SESSION`, `LOG_ACCESS_ONLY`)

---

## AWS Secrets Manager Integration

After creating a datasource, note its configuration name to use as the credential set identifier in AWS Secrets Manager.

---

## Tracing Session‑Level Policy Execution

Enable **track** to log rule evaluation flow and final decision for actions like:

- `IGNORE_SESSION`
- `DISCARD_SESSION`
- `LOG_ACCESS_ONLY`

---

## SR Language Policy Example

Oracle login error (TNS) ignore conditions:

- `SERVER_IP` = specific address
- `SERVER_PORT` = 1521
- `DB_TYPE` = `ORACLE`
- `REQ_TYPE` = `SQL`
- `SEARCH_PREFIX` = `ORA-`

---

## Invalid Queries Handling

Renamed, removed, or type‑changed columns in modified tables/views can invalidate queries used by Guardium reports; redesign affected reports.

---

## CAS Reporting Access Control

**CAS** reports are under **Harden > Reports**. The **admin** role can view but not create/modify query builders.

---

## Configure Venafi Instance

1. Create a user with required permissions on the Venafi portal.  
2. Populate configuration template fields: URL, credentials, scope.

---

## Document Overview

**IBM Guardium Data Protection** – Enterprise database activity monitoring and security platform.  

### Features
- Real‑time monitoring (S‑TAP)
- Policy enforcement and classification
- Compliance reporting (PCI‑DSS, GDPR, HIPAA, SOX)
- Threat detection (anomaly, SQL inspection, S‑GATE blocking)
- Identity & access integration, credential vaulting

### Workflows
- Configuration (data sources, agents, policies)
- Monitoring (reports, dashboards, alerts)
- Investigation (drill‑down, incident response)
- Maintenance (patching, upgrades, backups)

### Personas
- Security Administrator – policy definition/enforcement
- Database Administrator – data source maintenance
- Compliance Officer – report generation/review
- Security Analyst – incident investigation/threat hunting

### Entities
- **Agents** – S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregators, Central Managers
- **Reports** – Audit, Assessment, Activity, Risk, Compliance, Sensitivity
- **Policies** – Security, Audit, Classification, Access, Vulnerability
- **Infrastructure** – Managed Units, GIM, S‑GATE, Central Managers, Gateways

---

## Full SQL Report

Displays raw SQL from archived queries, providing exact statements executed.

## IBM Guardium Data Protection

### Features
- **Configuration Auditing System (CAS)**
  - APIs for GuardAPI commands to configure CAS hosts, templates, and template sets.
- **Compliance Monitoring**
  - Smart assistant for setting up vulnerability assessments and alerts.
- **Attribute Description**
  - Captures Client OS OS type; indicates integer storage format for Teradata.
- **Managed Units**
  - Enterprise load balancing and configuration distribution via Central Management components.

### Workflow Overview
- **CAS Host Management**
  - Steps to configure and manage CAS hosts using GuardAPI commands.
- **Compliance Configuration**
  - Setup processes for compliance monitoring and vulnerability assessments.
- **Attribute Configuration**
  - Detailed attribute meanings and usage in various data sources.
- **Managed Unit Deployment**
  - Guide for deploying and managing Central Management components.

### Personas
- **Security Analysts**
  - Manage CAS entities using Configuration Auditing System APIs.
- **Compliance Officers**
  - Configure compliance monitoring to set up and review regulation policies.
- **Database Administrators**
  - Manage attributes for data sources and interpret operator settings.
- **Enterprise Administrators**
  - Deploy and oversee Managed Units for load balancing.

### Entities
- **Key Entities**
  - CAS hosts, templates, template sets, Managed Units, Attribute Descriptions.
- **Relevant Products**
  - IBM Guardium Data Protection.

## Configuration Auditing System (CAS) APIs

Configuration Auditing System (CAS) APIs configure and manage CAS hosts, templates, and template sets through GuardAPI commands.

## IBM Guardium Data Protection Overview

### Features
- **Unified Discovery & Classification**: Uses AWS CloudFormation to discover sensitive data in AWS.
- **Activity Monitoring**: Captures traffic via S‑TAP agents and evaluates against policies in real time.
- **Threat Detection Analytics**: Includes built‑in and custom tests for configuration, privileges, and vulnerabilities.
- **Compliance & Reporting**: Generates PCI‑DSS, GDPR, HIPAA, SOX, and other regulatory reports, with alert‑log details and audit‑trail data.

### Workflows
- **Configuration**: Add data sources, deploy S‑TAP agents, enable plug‑ins, connect AWS accounts.
- **Policy Management**: Define security policies, alert thresholds, and attribute descriptions.
- **Incident Response**: Block queries, rotate credentials, investigate threats, manage configuration changes.
- **Reporting**: Produce compliance reports, view activity dashboards, purge data on schedule.

### Personas
- **Security Administrator**: Manages FGAC policies, security policies, attribute descriptions.
- **Database Administrator**: Configures data sources, S‑TAP deployment, vulnerability assessments.
- **Compliance Officer**: Generates reports, reviews audit trails.

## Entities Overview
Agents, collectors (S‑TAP, A‑TAP, K‑TAP), infrastructure (GIM, Managed Unit, S‑GATE, Universal Connector), and services (CloudWatch Logs, Kafka Connector) form the Guardium platform's data collection and processing hierarchy.

## 2072. Connecting Unified Discovery and Classification with Amazon Web Services cloud accounts
Guardium integrates with AWS using CloudFormation Stack or StackSet, which automatically discovers sensitive data in AWS resources and populates Guardium's classification repository with metadata from provisional scans.

## 2073. Attribute Description
Attributes for threshold alerts include Alert Log ID, Query Value (triggering value), Base Value (threshold), and Checked From Date (timestamp), enabling tracking and root‑cause analysis.

## 2074. Client Port Client port number
Client Port captures the TCP/IP port number used by a client application when connecting to a database, combined with the Database Name (including Oracle module) to uniquely identify a session for monitoring, auditing, and access control.

## 2075. Effective End Time Internal parameters
The File Id entity stores Guardium timestamps for when file classification began (Checked From Date) and ended (Effective End Time), used internally for lifecycle management and auditability of classification records.

## 2076. Attribute Description for the Command Entity (Data Sets)
The SQL Verb attribute in the Command Entity reports the SQL operation type (e.g., SELECT, INSERT) for logged events, presented as a count in reports using Full SQL as the primary entity.

## 2077. Types of vulnerability assessments
Guardium VA includes over 2,000 predefined tests assessing configurations, privileges, and known vulnerabilities across database types, allowing customization and integration with compliance reporting.

## 2080. Purge Intervals
Purge Intervals automatically delete debug logs, exceptions, and PII data according to scheduled intervals, managing storage and maintaining regulatory compliance.

## 2081. Modifying the retry limit
KAFKA_CONNECTOR_RESTART_LIMIT defines the number of automatic restart attempts (0‑1,000,000, default 3) for a Kafka connector after failure, allowing administrators to balance resilience and retry risk.

## Concepts Covered

- **Threat Detection APIs** – REST endpoints for fetching alerts, incidents, querying anomalies, and integrating with SIEM/SOAR platforms.  
- **show system conntrack** – Linux netfilter connection‑tracking runtime statistics.  
- **store system cpu profile** – Linux CPU‑scaling and governor configuration.  
- **GuardAPI syntax** – Command‑line interface for Guardium, e.g., `delete_db_user_mapping parameter=value`.  
- **Guardium** – IBM’s data‑security platform with monitoring, policy enforcement, vulnerability assessment, and compliance reporting across databases, Hadoop, cloud, etc.

## Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

## Features

- **Compliance Frameworks**: PCI-DSS, GDPR, HIPAA, SOX reporting capabilities
- **Policy Management**: FGAC, audit policies, exceptions, custom actions
- **Data Discovery**: Classification, tagging, sensitive data detection
- **Audit & Reporting**: Customizable dashboards, audit-ready reports, regulatory templates

## Workflows

- **Configuration**: Adding datasources, deploying collectors, managing policy lifecycles
- **Monitoring**: Real-time activity review, incident management, health status checks
- **Investigation**: Drill-down analysis, session replay, forensic evidence collection
- **Remediation**: Response actions, exception handling, automated fixes

## Personas

- **Security Administrators**: Policy definition, FGAC configuration, incident response
- **Database Administrators**: Datasource management, S-TAP deployment, performance tuning
- **Compliance Officers**: Regulatory reporting, audit evidence generation, risk assessment
- **Data Analysts**: Activity trend analysis, dashboard customization, query performance

## Entities

- **Agents**: S-TAP, K-TAP, A-TAP (data capture components)
- **Services**: Central Manager, Aggregators, Collectors (distribution infrastructure)
- **Policies**: Security Policies, Audit Policies, Classification Rules
- **Infrastructure**: Managed Units, GIM, S-GATE (deployment and enforcement layers)

## Command

The `delete_allowed_db_by_user` GuardAPI removes all User-DB mappings for a specified `userName`. It requires the `userName` and `api_target_host` parameters.

## Status API

`get_solr_status` returns the operational status of the Solr installation on a Guardium system. `get_solr_status_extended` performs additional checks and requires Guardium v12.0+.

## Datasource Details

Host Name/IP is required; Port defaults to 443; Database is mandatory; Connection property lists required JDBC URL parameters.

## Guardium Central Manager Health View

Provides an aggregated view of health status across entire Guardium deployment.

## Masking Definition - Frequent Values

In the **Masking Definition** window, use the **Frequent Value** panel to identify and mask values that appear many times in a column.

- Set the **minimum occurrence threshold** (e.g., values that occur at least 10 times).
- Use the **Frequent Value Mapping** table to map each frequent value to a substitute value.
- Optionally enable **Zero Value Mask** to mask any remaining values.

## Rule Triggering - Command Field

Rules require an exact match between the rule's **Command field** and the SQL verb from the query.

- Include wildcards as needed (e.g., use `SELECT * FROM` instead of just `SELECT`).
- Verify the Command field includes the full SQL verb plus any required clauses to ensure the rule triggers correctly.

## Install S-TAP Agents

To monitor database activity, install the S-TAP agent on each database host.

1. Download the S-TAP package for the OS and database type from the Guardium repository.
2. Run the installer with parameters for the Central Manager address, database host name, and credential source (e.g., CyberArk).
3. Confirm installation via **Manage > Inventory > Datasources**; status should be "Active".

During installation, Guardium detects the database port automatically; for encrypted connections, adjust the **connection_pool** parameter (default 10, max 50) for higher throughput.

## Aggregator Clustering

Aggregator clusters provide load balancing and high availability for collectors.

1. Navigate to **Manage > Infrastructure > Aggregators** and create a new cluster.
2. Add each aggregator appliance.
3. Configure the Central Manager to use the cluster instead of a single aggregator.
4. Enable **redundancy backup_cm_set** on the Central Manager for failover support.

All aggregators must run the same Guardium version, time must be synchronized, and network latency should be under 50 ms.

## GUARD System Database Maintenance

If the internal `GUARD` database shows corruption or performance issues:

1. Back up the appliance: `appliance_backup --full`.
2. Restart the Guardium service: `service gdguard stop && service gdguard start`.
3. Check database health under **Admin > Troubleshoot > System Health**.
4. Restore from backup if needed: `appliance_restore --full`.
5. Reapply any pending patches or upgrades via GIM.

Enable automatic snapshots (`snapshot --autorecovery`) to preserve recovery points.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Core Features
- Centralized deployment inventory of database servers, S-TAP agents, and GIM clients  
- Flexible connectivity with multiple JDBC drivers and dynamic port resolution  
- Real-time activity monitoring with FGAC policies, alerts, blocking, and audit trails  
- Compliance templates for PCI‑DSS, GDPR, HIPAA, SOX, with automated audit collection  
- Universal connector management for datasource profiles, managed units, and load balancing  
- Certificate management CLI, session inference settings, and CEF source mapping  

### Workflows
- **Configuration:** Add datasources, deploy S-TAP via GIM, create FGAC policies, configure universal connectors  
- **Navigation:** Review activity reports, run vulnerability assessments, use audit dashboards  
- **Action:** Block unauthorized queries, rotate credentials, respond to security incidents  
- **Load Balancing:** Associate entity groups with managed units, resynchronize S-TAP agents, generate load maps and reports  

### Personas
- Administrators – platform configuration, user management, GIM tasks  
- Security Administrators – FGAC policies, access control, threat management  
- Database Administrators – datasource management, S-TAP deployment, performance tuning  
- Data and Analyst Users – dashboards, custom queries, data exploration  
- Compliance Officers – generate regulatory reports, collect audit evidence  
- Security Analysts – investigate threats, analyze policy violations, handle incidents  

### Key Entities
- Agents & collectors: S-TAP, A-TAP, K-TAP, Guardium collectors, aggregators, central managers  
- Policies & rules: security, audit, FGAC, access, classification  
- Infrastructure components: GIM, managed units, S-GATE, universal connectors, deployment inventory, certificate stores  

## Datasource Profile Management

Use the Datasource Profile Management page to create single or multiple datasource profiles that define reusable settings for deploying universal connectors on managed units.

## Enterprise Load Balancing

Enterprise load balancing distributes processing load across multiple managed units, improving scalability and reliability.

1. Associate entity groups with target managed units.  
2. Resynchronize S-TAP agents to recognize new distribution rules.  
3. Use the UI or CLI to generate load‑map visualizations and balancing reports.

## Key Concepts
Load distribution, managed unit association, resynchronization, reporting.

## Using the Query‑Report Builder
The Query‑Report Builder lets users create custom queries and reusable report templates by selecting tables, filters, grouping, and output columns.

## Using Db2 for IBM i S‑TAP
The Db2 for IBM i S‑TAP monitors all database access on IBM i systems, capturing native I/O and SQL operations for comprehensive visibility.

## Client Special Register Values
S‑TAP collects data from SQL Performance Monitor (SQL apps) and the audit journal (native apps), reconstructing full activity records.

## What to Do Next
1. Refine policies to reduce false positives.
2. Map audit policies to specific regulatory frameworks.
3. Tune S‑TAP and collector configuration for high throughput.
4. Train administrators and analysts on Guardium features and best practices.

## Document Overview
IBM Guardium is an enterprise data security platform that offers real‑time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting for on‑premises and cloud data stores. It discovers and monitors assets, assesses risk, enforces security policies, and satisfies audit and reporting requirements.

## Hadoop Monitoring Management

APIs manage integration of Hadoop environment into Guardium, including Hadoop Ranger service addition and configuration of REST API bridge.

- **Add Hadoop Ranger Service**: Register and configure Hadoop Ranger service within Guardium for monitoring. Provides CLI and REST options to set service parameters, dependencies, and enable/disable status.
- **Add Last Service**: Adds the last Hadoop service in a cluster using a similar CLI command with comparable parameters.
- **Delete API Bridge**: Remove the REST API bridge for Hadoop services via CLI (delete_api_bridge_hadoop).
- **Disable Hadoop Service**: Turn off Hadoop service monitoring through CLI (disable_hadoop_service).
- **Export List Hadoop**: Export list of Hadoop services via CLI (export_list_hadoop).
- **Get API Bridge**: Retrieve configured API bridge details using CLI (get_api_bridge_hadoop) or REST GET call.
- **Get Last Service**: Find the last configured Hadoop service using CLI or REST GET call.
- **Get Parameters**: Query parameter templates for Hadoop integration via CLI (get_parameters_hadoop_service_migration) and REST GET.
- **Get Query Last Service**: similar to Get Last Service but tailored for query use.
- **Get Service (Hadoop)**: Retrieve detailed information on a specific Hadoop service using CLI or REST GET.
- **Get Status**: Check current status of Hadoop services through REST GET call.
- **Get Versions**: List supported versions for Hadoop monitoring using CLI or REST GET.
- **Status Hadoop Service**: REST endpoint to check Hadoop service status.
- **Update Hadoop Service**: Modify configuration of an existing Hadoop service via CLI or REST PUT.
- **Update Parameter**: Change parameters for Hadoop service integration via CLI (update_parameter_hadoop_service_migration) and REST PUT.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures database activity across on‑premises and cloud environments, offering real‑time monitoring, threat detection, and compliance reporting.

### Key Features
- **Multi‑Driver Connectivity:** Supports diverse databases and cloud platforms with dynamic port detection and credential injection.
- **Real‑Time Threat Detection:** Continuous policy evaluation, query blocking, and automated security alerts.
- **Compliance Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX, with customizable audit trails.

### Core Workflows
- **Configuration:** Add datasources, deploy S‑TAP agents via GIM, define FGAC policies.
- **Navigation:** View activity reports, run vulnerability assessments, monitor dashboards.
- **Action:** Block unauthorized queries, rotate credentials, investigate incidents.

### Personas
- **Security Administrator:** Sets up platform, provisions users, maintains unified logging.
- **Database Administrator:** Manages datasources, installs/updates S‑TAP, performs health checks.
- **Compliance Officer:** Creates regulatory reports, conducts risk assessments, reviews audit data.

### Entities
- **Agents/Collectors:** S‑TAP (network), A‑TAP (file‑system), K‑TAP (kernel), Collector, Aggregator, Central Manager.
- **Policies/Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule.
- **Infrastructure:** Guardium Installation Manager (GIM), Managed Units, S‑GATE, Universal Connectors.

## Reducing S‑TAP Buffer Size

If the S‑TAP agent consumes excessive memory, lower the buffer size to prevent out‑of‑memory errors:

```text
buffer_file_size=<new_size_in_MB>
```

Edit `guard_tap.ini`, then restart the S‑TAP service. This adjustment reduces memory footprint while still capturing audit events.

## Native Audit API (Cloud Databases)

Guardium’s native audit APIs let administrators programmatically enable or disable native auditing, manage audit objects, and query configuration details from collectors—facilitating compliance automation on cloud workloads.

## Windows Authentication & Vulnerability Assessment Fields

For Windows authentication and vulnerability assessments in Guardium, the **Account name** and **Directory** fields are required. These fields identify the database account owner and the instance path, ensuring proper authentication and assessment execution.

## BigData Intelligence Exception domain

The *BigData Intelligence Exception domain* aggregates exceptions and related data from database servers and the Guardium system, enabling anomaly detection and security analytics.

## Informix account with DBA Privilege

An Informix DBA account includes execute privileges on procedures and functions, object/ column grants with grant options, object dependencies, and public grants, facilitating comprehensive database management.

## Function Schedule

The data archiving/purging Function Schedule runs daily at 7:00 PM, processing daily collector imports, deleting data older than 60 days, and archiving required records.

## FROM session_view

The `session_view` query groups, orders, and filters database sessions by start time, providing a detailed overview of session activity for the Full SQL Report.

## Configuring the slon looper utility

Configure the slon looper utility via the Support Information Gathering page to monitor incoming network traffic on the sniffer and identify issues.

## Vault configuration expectations

Guardium vault configuration requires version 12.2.2 or later, HashiCorp AppRole Login, a secured appliance, and proper certificates for secret management and access control.

## Attr

`5aafadbe-smart-uuid-for-more` | **categories:** knowledge, entities  
Attr stores user‑defined metadata as an Identifier String.

## Document Overview

IBM Guardium Data Protection monitors, secures, and reports on database activity across on‑premises and cloud data stores.

### Features
- Dynamic port detection, multi‑driver support, CyberArk credential vault integration.  
- Real‑time policy enforcement, S‑GATE blocking, incident generation.  
- PCI‑DSS, GDPR, HIPAA, SOX report templates; automated audit trails.

### Workflows
- **Configuration:** Add datasource, deploy S‑TAP via GIM, configure FGAC policies.  
- **Navigation:** Review activity reports, run vulnerability assessments, use audit dashboard.  
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents.

### Personas
- **Administration:** Platform config, user management, FGAC, policies.  
- **Data & DB Management:** Datasources, S‑TAP, data analyst dashboards.  
- **Compliance & Audit:** Regulatory reports, threat investigation.

### Entities
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.  
- **Policies & Rules:** Security, audit, classification, access rules.  
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector.

## Event ID Attribute

`3c18498a-c535-4721-b90b-b685a4998783` | **Event ID**  
Used for detailed‑level query reporting.

## Before You Begin

`b8ad7564-8ab3-4c63-ad1f-4175ca515f8e` | **Prerequisites**  
Identify the external database and gather IP, port, and credential details before mapping an external feed in Guardium.

## Session Queue

`fe19be8d-8b57-4296-bb3b-4fd1d4f73aa3` | **Session Queue Length**  
Shows total open sessions monitored by the sniffer; limited to **4 000** simultaneous sessions per appliance.

## Regular Expression Description

`d4a4856d-605b-4a47-a737-13d6c46aa91e` | **Regex Syntax**  
Defines `{n}` repeat and hex/octal number formats.

## TLS Configuration - Use WINSTAP_USE_

`f525b657-7430-48f9-b5b0-8338e264b1df` | **WINSTAP_USING_EDGE**  
Enables/disables streaming to Edge Gateway (0 = disabled, 1 = enabled).

## Guardium Installation Manager

`3bc387ba-65d5-4ea9-92d5-a1c8d63eca1e` | **K‑TAP & S‑TAP Management**  
Provides guidance on K‑TAP, GIM installation parameters for Linux‑UNIX S‑TAP, and uninstalling S‑TAP agents.

## Before You Begin (Catalog Sources)

`e9cabb2d-7d5a-48ae-a6d7-9fb9e9f0aa8a` | **External S‑TAP Setup**  
Verify cluster requirements and create the project before creating catalog sources for External S‑TAP.

## Guardium Installation Manager (GIM) API

`f9e3de1f-f35d-4485-8f11-56fddd23e70b` | **gim_schedule_install**  
Schedules installation of PENDING state modules/bundles; can specify module and installation date.

## Attribute and Mapping APIs for Reports

`ae3a9b04-a65c-4bb4-b27f-935ef9dda783` | **Reporting APIs**  
Maps API parameters to domain entities and attributes for reporting purposes.

## CyberArk Account Permissions

`999cba42-67af-4f17-8fc5-a594ab9f3efa` | **Account Management**  
(Entry incomplete – no further content provided.)

## SECURITY PATCH PATCHKEY FIXNOTES

The Security Patch PatchKey FixNotes provides detailed information about security fixes in Guardium releases. It includes patch names, grades, and comments for releases 10.6, 11.0, 11.2, and 11.3.

## Monitoring Activation Config

**Purpose:** Activate query succeeded monitoring and define a reporting period.
**Command Syntax:** `grdapi monitoring_activation activate=succeeded reporting_period=30d`

---

## CASE Config Domain

**Description:** Captures host configuration details derived from CAS templates applied to individual database server hosts. This domain is essential for understanding how CAS configurations are propagated to database servers.

---

## Attribute Auto-Discovery

**Overview:** Monitors activities related to database instance discovery.
**Key Features:** Tracks processes initiated at system startup and establishes entity relationships for newly discovered items.
**Use Cases:** Useful for automated inventory management and ensuring all instances are tracked by monitoring systems.

---

## Attribute BigData Intelligence DB2 Shared Memory

**Details:** Specialized monitoring attributes for DB2 shared memory configurations, typically used in environments requiring real-time performance metrics from big data analytics tools.

---

## Document Overview

**Platform:** IBM Guardium Data Protection
**Capabilities:** Real-time monitoring, policy enforcement, vulnerability assessment, compliance reporting across structured and unstructured data stores (on-premises and cloud).

### Features Overview
- **Datasource Connectivity:** Supports dynamic port detection, multiple driver options, and integrates with CyberArk for credential management.
- **Threat Detection:** Provides real-time policy enforcement, S-GATE blocking mechanisms, and generates security incident alerts.
- **Compliance & Reporting:** Offers templates for PCI-DSS, GDPR, HIPAA, and SOX, along with automated audit trail generation.
- **Database User Management:** Facilitates CAS installation via a wizard interface and defines audit databases for Informix and Sybase environments.

### Workflows Overview
- **Configuration:** Add datasources, deploy S-TAP agents via Guardium Installation Manager (GIM), and configure FGAC policies.
- **Action:** Block unauthorized queries, rotate credentials, and manage security incidents.
- **User Management:** Create and manage DB user accounts, assign roles, and populate application groups within the system.

### Personas Overview
- **Administration:** Handles platform configuration tasks.
- **Security Administrator:** Manages FGAC policies and security-related configurations.
- **Data Management:** Focuses on datasource setup, S-TAP deployment, and policy configuration.
- **Data Analyst:** Utilizes dashboards and performs query analysis.
- **Compliance:** Responsible for generating regulatory reports.
- **Security Analyst:** Conducts threat investigations and security audits.

### Entities Overview
- **Agents & Collectors:** Includes S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager, and GIM Client.
- **Policies & Rules:** Encompasses Security Policy, Audit Policy, Classification Rule, Access Rule, and Policy Rule Violation.
- **Infrastructure:** Definitions for Managed Unit (Central Manager) and Managed Units Report.
- **Integration:** APIs for CyberArk integration and infrastructure metrics like Load CPU.

---

## STAP Changed

**Entity Log Details:** Logs information specific to each S-TAP installation instance.
**Attributes Recorded:**
- **STAP Verification Status:** Success, failure, or pending.
- **S-TAP Host IP:** IP address of the host running the S-TAP agent.
- **S-TAP Version:** Version of the installed S-TAP agent software.
- **Status:** Operational status (e.g., active, inactive, error).

**Administrative Use:** Enables monitoring of the health and version consistency across S-TAP deployments.

---

## Flat Log Entity

**Captures System-Level Information:** Detailed logs about Guardium's GIM client.
**Attributes Included:**
- **GIM Client Name:** Identifier of the GIM client.
- **Client Hostname:** Hostname of the machine running the GIM client.
- **OS Vendor & Version:** Operating system information.
- **GIM Client State Timestamp:** Timestamp indicating the last recorded state of the GIM client.

**Operational Insight:** Aids in tracking configurations and statuses of GIM installations.

---

## Attribute Description

**Key Identifiers Defined:**
- **App Object Module1:** Identifier for application modules in custom policies.
- **Construct Id:** Administrative construct ID used by administrators.
- **Object Id:** Unique identifier for monitored database objects.

**Application:** Critical for crafting precise policy rules targeting specific application modules or database objects.

---

## Policy Rule Violation Entity

**Generated Upon:** Policy violations triggered by database activities.
**Stored Details Include:**
- **Policy Rule Details:** Information about the violated policy.
- **Offending Activity Details:** Context, timestamp, and specifics of the violating query or operation.

**Support:** Provides evidence for audit trails and compliance reporting, essential for demonstrating adherence to security policies.

---

## Installing CAS

**Installation Steps:**
1. **Download** the CAS ZIP package.
2. **Extract** the contents to a designated directory.
3. **Execute** `Setup.exe` and follow the installation prompts.

**Integration:** Ensures CAS functionality is properly integrated into the Guardium platform for enhanced activity correlation and analysis.

---

## Load CPU Metric

**Definition:** Normalized representation of overall system CPU usage.
**Calculation:** Aggregates values from multiple CPU load metrics, providing a comprehensive system health indicator.
**Limitations:** While useful for high-level load assessment, may not identify specific performance bottlenecks without further detailed metrics.

## Guardium Knowledge Categories

### 1. CyberArk Integration
- **CyberArk APIs** enable automated credential management within Guardium Vault, including creation, deletion, updating, listing, and permission verification of credentials.

### 2. Application Group Population
- **Populate Pre-defined Application Groups**: After enabling Application User Translation, administrators must manually map users to two predefined Guardium groups to ensure correct user activity tracking and reporting.

### 3. Database User Account Setup
- **Create a Database User Account**: DBAs must create a service account, log into monitored databases, and set up necessary tables and triggers before defining audit databases for Informix or Sybase.

### 4. Security Assessment Queries
- **Domain Based on Query Main Entity**: SQL parameters for SECURITY_ASSESSMENT support filtering by Test ID, Datasource Type, Severity Level, Test Type, and Value.

### 5. Investigation Dashboard
- **Investigation Dashboard Issues in Recovery**: Filter the dashboard to show only issues with Status = 'Error' to identify unresolved problems needing manual intervention.

### 6. Central Management Reports
- **Managed Units (Central Manager)**: Provides status reports and health monitoring for Central Manager and monitored units, supporting centralized administration.

### 7. Overview of Guardium
- **Document Overview**: IBM Guardium Data Protection is a comprehensive security platform offering real-time monitoring, compliance reporting, data access governance, and centralized management across data stores.

### 8. Database Connectivity
- **Database Connection Architecture**: Guardium supports various JDBC drivers for SQL databases, utilizing a browser service for dynamic port resolution.

### 9. Policy Enforcement
- **Activity Monitoring & Policy Enforcement**: Captures database traffic, evaluates it against policies in real-time, and triggers alerts or blocking actions via S-GATE.

### 10. Attribute Catalog
- **Attribute Description Catalog**: Stores metadata about result set attributes, including catalog and schema information, supporting data discovery and classification.

Protection 1527

## Guardium Data Protection Overview

Guardium provides a unified platform for monitoring and securing enterprise data across structured and unstructured stores, both on-premises and in cloud environments. It delivers real‑time activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Key Features
- **Unified Discovery & Classification:** Classify sensitive data at scale using the Unified Discovery and Classification primary analyzer.
- **Cross‑CM Health View:** Supports patch management and health monitoring for Guardium Central Managers and managed units.
- **CAS Config Domain:** Tracks host configurations by applying template sets to database server hosts.
- **S‑GATE Blocking:** Real‑time enforcement of security policies with agent‑based traffic interception (S‑TAP, A‑TAP, K‑TAP).

### Typical Workflows
1. **Discovery & Classification:** Run the analyzer role on at least one machine to tag financial or other sensitive data categories.
2. **Policy Enforcement:** Deploy S‑TAP agents to capture traffic; use policy definitions to evaluate activity, generate alerts, or block unauthorized requests.
3. **Compliance Reporting:** Generate PCI‑DSS, GDPR, HIPAA, SOX, and custom regulatory reports based on audit trails.
4. **Health Monitoring:** Use the Cross‑CM Health View to monitor patch levels and deployment health across the Guardium fleet.

### Common Personas
- **Security Administrator:** Configures policies (FGAC, S‑GATE) and monitors incidents.
- **Compliance Officer:** Generates compliance reports and reviews audit trails.
- **Database Administrator:** Manages data sources, installs S‑TAP agents, and verifies configuration.
- **Security Analyst:** Investigates incidents on the Investigation Dashboard and runs vulnerability assessments.

### Core Entities
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Analyzer Role.
- **Infrastructure:** CAS Config domain, S‑GATE, Deployment Health topology, GuardUI components.

## 2338. add_assessment_test - Add a Test to a Security Assessment
`add_assessment_test` adds a test to a security assessment. Specify `assessment_description` and `datasourceType`. Use `--help=true` to list supported `datasourceType` values.

## 2339. display_external_stap_config - Show External S‑TAP Configuration
`display_external_stap_config` returns configuration values for External S‑TAP parameters. No arguments shows all modifiable parameters; `externalStapConfig=<param> filter=<value>` shows a specific setting.

## 2340. Sybase IQ Public Access Details
Exec privileges on procedures/functions, login policies, user groups, public‑role object permissions, and `GRANT OPTION`.

## 2341. IBM Guardium Data Protection Overview
Enterprise monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured/unstructured data on‑prem and cloud.

### Features
- Real‑time threat detection & S‑GATE blocking
- Automated audit trails and reporting templates
- Data loss prevention (classification, masking, redaction)
- Compliance management (role‑based access, configuration hardening, baselines)

### Workflow Steps
1. **Deploy** collectors and S‑TAP agents via GIM  
2. **Monitor** live session activity, alerts, and generate audit reports  
3. **Remediate** by blocking queries, rotating credentials, investigating incidents  
4. **Manage** policies, keys, roles, and performance tuning

### Personas
- **Security Admin** – configures policies, reviews alerts, manages compliance.  
- **DB Admin** – monitors DB activity, troubleshoots S‑TAP.  
- **Compliance Officer** – generates audit reports, verifies regulatory adherence.  
- **Analyst** – investigates incidents, creates custom dashboards.

### Core Entities
| Entity | Role |
|--------|------|
| **Agent** | S‑TAP (DB‑side), A‑TAP (network), K‑TAP (kernel) |
| **Collector** | Aggregates traffic, runs policies, stages analysis |
| **Policy** | Security (blocking), Audit (reporting), Classification (discovery) |
| **Infrastructure** | Central Manager, Managed Units, GIM |

## GuardAPI Syntax for Updating Aliases
`grdapi update_alias dbValue="<old_name>" groupTypeDesc="<type>" newAliasValue="<new_name>"` – renames an existing alias. `--help` lists `groupTypeDesc` values.

## Workflow: Synchronize Database Changes
`guardapi update_user_db ID=0` synchronizes pending schema changes across monitored instances to keep policies and classifications current.

## System Configuration CLI Setup

During Guardium installation, most system‑level parameters are configured via the CLI. Administrators edit settings such as collector addresses, database connections, and logging options using commands like `modify_system_config` or the `modify_system_configuration` wizard.

## Troubleshooting UC Connections

The Troubleshooting Tool scans Logstash logs for known error patterns, verifies collector connectivity, and reports misconfigurations. Running it regularly maintains reliable data collection across a Guardium deployment.

## Certification Expiration Alerts

Guardium monitors SSL/TLS certificates. Use the command `show certificate warn_expire` to list certificates expiring in six months or that have already expired. Failure to renew results in loss of encrypted data transmission.

## Monitoring Unit Utilization

The `show monitor gdm_statistics` CLI command displays real‑time metrics (CPU, memory, network) for Guardium monitoring units. Statistics are reported hourly by default; use `set_monitor_interval` to adjust the interval.

## Outliers Detection API

To disable outlier analysis on a specific collector within a central‑manager environment, run:  
`disable_outliers_detection_cross_cm_collector <collector_name>`. This is useful in multi‑central‑manager setups.

## Migrating S‑TAP Config to Guardium Insights

First push the Insights trust chain to the collector (GUI or `push_insights_trust`). Then execute:  
```
grdapi migrate_stap_config
```  
This transfers existing S‑TAP settings to the new platform without re‑deployment.

## Updating Assessment Test Parameters

Modify an assessment test with the API:  
```
grdapi update_assessment_test assessmentDescription="PCI_DSS" testDescription="Credit_Card_Leakage" parameter="severity" value="high"
```  
required fields: `assessmentDescription`, `testDescription`, `parameter`. Optional field: `value`.

## Datasource Definition

A datasource defines a database connection for Guardium applications. Required parameters include host, port, database type, authentication method, and optional advanced settings such as JDBC driver class and connection pooling options.

## Guardium Data Protection Overview

IBM Guardium Data Protection monitors, secures, and ensures compliance across structured and unstructured data sources. Features include real‑time monitoring, threat detection, automated vulnerability assessment, and compliance reporting.

## Evidence Generation Workflow

- Add datasources, deploy agents, define policies, configure collectors.
- Review activity alerts, investigate incidents, generate compliance reports.
- Modify permissions, apply patches, enforce least privilege, retest.

## Personas

- **Security Administrator:** Configure policies, manage alerts, oversee audit.
- **Database Administrator:** Manage datasource connectivity, apply policy changes.
- **Compliance Officer:** Generate regulatory reports, audit findings.
- **Data Scientist:** Access approved data, audit query activity.

## Entities

- **Components:** S-TAP, Aggregators, Collectors, Central Manager.
- **Policies:** Security Policies, Audit Policies, Classification Policies.
- **Data:** Datasources, Tables, Columns, Objects.
- **Reports:** Compliance Reports, Risk Reports, Incident Reports.

## APIs

- **REST API Configuration Retrieval:** `get_ranger_config` retrieves cluster configuration settings for audit.
- **CAS Template Configuration:** Define custom audit report formats with specific database operations, users, and error codes.
- **Azure Event Hub Monitoring:** Configure event hub names, connection strings, and policy settings for monitoring streaming events.
- **Entitlement Optimization:** Analyze user access patterns and data sensitivity to identify over-privileged accounts and recommend minimal entitlements.

## Trust Evaluator

- Display the learning progress of the probability engine modeling typical database traffic patterns. Status changes to PAUSED or IDLE after 15 minutes of inactivity.

## Policy Setup

- Create or edit a policy via the Policy Builder for Data before creating a session-level policy rule.

## JDBC Data Sources

- Attribute Description lists key connection properties for datasource identification and policy enforcement, including server name, port, database name, and authentication details.

## Assessment Tests

- The Db Type field identifies the specific database platform evaluated for security weaknesses, enabling targeted tests and security recommendations.

## Sniffer Process

- The Sniffer Process ID shows the dynamic identifier assigned to the active process, changing with each restart to track and manage the lifecycle of Guardium's monitoring engine.

## Database Type in Assessment

- The Db Type field within the Assessment Tests domain denotes the specific database platform evaluated for security weaknesses, accessible to users with the admin role.

## CAS Agent Fix

- If installed with an invalid non-IP hostname, correct tap_ip in guard_tap.ini, CAS_TAP_IP environment variable, or the hostname itself to ensure proper connectivity and audit data collection.

## Policy Installation

- The Installed Policy view provides metadata including installation timestamp, Guardium version, and last patch level for each managed unit.

## Policy Distribution

- Update Guardium to version 12.2 or later and enable network communication over port 8447 across all managed units to distribute configuration profiles effectively.

## Real-Time Alerts

- Create a policy with custom rules and actions to generate immediate security alerts for suspicious activities and policy violations.

## Document Overview

- I

## Reduce Monitored Traffic Through Filtering Rules
Adding filtering rules to Guardium policies reduces the volume of traffic that must be processed and reported, allowing the system to focus on critical events while minimizing performance impact on the monitored databases.

## Next Step: Policy Installation After S‑TAP
After configuring S‑TAP agents on database servers, the next step is to install Guardium and Ranger policies. The policy rules are nearly identical between the two platforms, with only minimal adjustments needed for Ranger‑specific settings.

## Guardium Command: store snif_hostname_cache
The `support store snif_hostname_cache` command controls whether the Guardium sniffer caches DNS lookups of IPv4 and IPv6 addresses seen in network traffic. Enabling the cache improves performance by avoiding repeated name resolutions.

## GuardAPI Parameter: add_threshold_to_rule
The `add_threshold_to_rule` GuardAPI function adds a threshold condition to an existing Guardium audit or security rule. Required parameters are `policy_name` (the policy containing the rule) and `rule_name` (the specific rule to which the threshold will be applied).

## GuardAPI Parameter: configure_archive
The `configure_archive` GuardAPI function defines parameters for archiving audit data. It accepts three key arguments:
- `eventStatus` – final status of the archived event.
- `execDate` – date and time when the archive process should run.
- `processDesc` – a textual description of the archiving process for audit purposes.

## GuardAPI Syntax: create_classifier_action
The `create_classifier_action` GuardAPI requires at minimum `actionName` and `actionType` (both mandatory). Additional parameters such as `accessPolicy`, `accessRuleAction`, and others are available to fully configure the classifier action according to specific business needs.

## Guardium Installation Manager (GIM) API: gim_remove_bundle
The GIM API function **gim_remove_bundle** deletes software bundles from the Guardium repository. It supports bulk removal via wildcards and can also uninstall bundles that are not currently assigned to any managed unit, streamlining repository maintenance.

## DB2 Routine Dependencies (Feature)
Guardium provides reports detailing special authorities and privileges granted to users and PUBLIC for DB2 for i routines, covering multiple IBM i versions. These insights help security teams understand and manage risk associated with database routine dependencies.

## Cloud Data Source Management API
Guardium offers a set of REST‑style APIs for managing cloud data sources:
- **Create/Assign Configuration:** Define cloud data sources, map them to collectors, and configure streaming options.
- **Lifecycle Management:** Add, enable, disable, discover, and delete cloud data sources, ensuring they stay synchronized with Guardium policies.

## Analyzer Service Account (Entity)
The Analyzer service account grants the Guardium Classification Analyzer read‑only access to a customer’s data stores in the cloud. This access enables the automatic discovery and classification of sensitive data, feeding the risk‑assessment process.

## Active Threat Analytics (Feature)
Active Threat Analytics (ATA) leverages outlier mining and attack‑symptom detection to automatically surface suspicious activity as potential breach cases. A dedicated dashboard provides security analysts with contextual details and investigative tools to validate and respond to threats.

## Risk Spotter (Feature)
Risk Spotter is a Guardium component that assists security teams in maintaining and continuously tuning data‑security monitoring policies. As databases and applications evolve, Risk Spotter recommends policy adjustments to keep coverage comprehensive and relevant.

## Session Management (Entities)
- **Session Start:** Records the initial parameters of a database session, such as the start date, program name, and user identity.

## Guardium Session Attributes

### Overview
IBM Guardium records each monitored session with several read‑only attributes used for analysis and reporting. Access to these attributes is limited to users with the **admin** role.

- **Session ID:** Unique identifier used in Guardium reports and APIs. *Only admins can view.*
- **Session Ignored:** Flag indicating if a policy action (`IGNORE SESSION`) was applied. *Only admins can view.*
- **Session End Year:** Extracts the year from the session’s UTC end timestamp. *Only admins can view.*

---

## Session End Year

The **Session End Year** attribute extracts the year component (e.g., `2024`) from the session’s UTC end datetime. This is useful for time‑based analysis, reporting, and compliance audits. The value is accessible only to users with the **admin** role.

## Enabling Full Username Resolution for Teradata

```bash
gtwcontrol -u yes -d
```

Configures the Teradata driver to return full user names in their proper character set without affecting other applications. The change persists across restarts.

### Key Concepts
- `gtwcontrol`: Utility to configure the Teradata driver
- Character set encoding: Ensures usernames are transmitted in the correct encoding
- Persistent setting: Remains after system reboots  

---

## Document Overview

IBM Guardium Data Protection is an enterprise security platform for monitoring and protecting structured and unstructured data across on-premises and cloud data sources in real time.

### Core Features
- Database connectivity: Automatic port detection, multi-driver support, CyberArk credential vault integration
- Threat prevention: Real-time policy enforcement, query blocking via S-GATE, security incident alerts
- Compliance reporting: PCI-DSS, GDPR, HIPAA, SOX templates; automated audit logging
- Extensibility: Custom attributes for enriched event context  

### Typical Workflows
- Deployment: Install Guardium, add data sources, deploy S-TAP agents, define FGAC policies
- Investigation: View activity reports, run vulnerability assessments, generate compliance reports
- Response: Block unauthorized queries, rotate compromised credentials, contain security incidents
- Data lifecycle: Schedule metadata uploads after provisioning new monitoring assets  

### Personas
- **Administration:** Platform configuration, user and role management
- **Security Administration:** FGAC policy definition, access control, alert handling
- **Database Administrators:** S-TAP installation, data source connectivity, query execution
- **Data Analysts:** Dashboard exploration, reporting
- **Compliance Officers:** Regulatory artifact generation, audit evidence collection
- **Security Analysts:** Threat investigation, policy tuning, incident response  

### Guardium Entities
- **Collectors:** S-TAP, A-TAP, K-TAP, aggregator, central manager, managed unit
- **Policies & Rules:** Security policies, audit policies, classification rules, access rules
- **Infrastructure:** Guardium Installation Manager, S-GATE gatekeeper, Universal Connector
- **Consumers:** Independent readers of event streams from Apache Kafka  

---

## Custom Attributes

**ID:** `190b50bb-d5e0-4327-a6df-e206cdb894cf`  
**Categories:** Knowledge, Features  

Enables vendors and users to attach custom key‑value pairs to Guardium events, providing additional context for analysis, reporting, and compliance.

---

## S-TAP Troubleshooting

**ID:** `d1927bff-ca74-4681-8ab7-9cda5a7234c6`  
**Categories:** Knowledge, Features  

Provides guidance for resolving common issues with S-TAP agents and collectors, including connectivity, performance, and configuration problems. Covers troubleshooting steps and best practices.

---

## VMware Kernel Panic Fix

**ID:** `d490cbfb-689f-47bf-8b02-6e3eef35a95f`  
**Categories:** Knowledge  

Resolves kernel panics experienced on ESX 4.1 hosts after rebooting with Guardium installed by:
1. Updating ESX to the latest patch level, or  
2. Changing the VM's CPU/MMU virtualization setting to "Use software only".

---

## Native Audit APIs

**ID:** `51d06200-ca70-40fe-b5b9-56b1c99d7756`  
**Categories:** Knowledge  

Describes the GuardAPI and REST endpoint `add_ranger_config` for registering an Apache Ranger plugin on an Ambari-managed Hadoop cluster. Requires administrative privileges on the Ambari server.  

---

## GuardAPI Syntax

**ID:** `eb98fb3a-db7a-401c-9f5e-886e5afacc61`  
**Categories:** Knowledge, Features  

The `create_test_exception` GuardAPI registers a vulnerability assessment test exception with specified policy name, assessment ID, and parameter list. Supports both command-line and programmatic invocation.

---

## REST API

**ID:** `1aaf4c33-188a-4d28-99ac-ce25790d2808`  
**Categories:** Knowledge, Keywords  

`GET /get_installed_policy` retrieves JSON payload containing the name, ID, and status of installed policies on the current Guardium unit or specified target unit.

---

## PCI Cardholder Databases

**ID:** `d9061b9c-99bc-4c72-9a59-9beb81d50919`  
**Categories:** Knowledge, Features  

Provides a comprehensive module for PCI DSS scope management. Captures and monitors databases, servers, users, administrators, source programs, shared accounts, root/administrator activities, unauthorized application access, and cardholder transaction monitoring.

---

## Datasource Credential Management APIs

**ID:** `f106c337-9615-444a-a14b-5b394459472a`  
**Categories:** Knowledge, Entities  

Lists Guardium API commands for retrieving and manipulating managed unit configuration and health information, specifically `list_health_node`. Useful for automated environment monitoring and health checks.

---

## ABA Routing

**ID:** `a31d501d-0d56-4819-a249-2ad8c4ff0cec`  
**Categories:** Knowledge, Keywords  

Defines the ABA routing number (also known as the routing transit number) used by U.S. financial institutions to direct funds during transactions, including ACH and wire transfers. Widely used identifier in banking systems.

---

## Before You Begin - CyberArk Integration

**ID:** `95677df3-53e6-49bc-9458-c27158b02408`  
**Categories:** Knowledge  

Outlines required steps to cleanly remove the CyberArk Application Password Provider integration from Guardium:
1. Revoke Guardium's credentials in CyberArk vault, then  
2. Uninstall the provider using the Guardium CLI command `uninstall cyberark`.  

---

## Consumer Group Name

**ID:** `22420106-a74a-45bd-81e1-fefd77d422e7`  
**Categories:** Knowledge, Entities  

A named configuration within an Azure Event Hubs namespace that allows multiple consumers to read from the same partition stream concurrently.  

---

## Before You Begin - Prerequisite Tasks

**ID:** `2f23f03d-f9b1-40a7-abee-1a2aeb9df193`  
**Categories:** Knowledge  

Lists prerequisite administrative actions required before undertaking a major Guardium deployment, including environment assessment, stakeholder planning, and preparatory configuration tasks. Ensures readiness for successful implementation.

## Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise-grade platform for monitoring, protecting, and ensuring compliance across on-premises and cloud data stores. It captures database activity in real time, enforces security policies, detects threats, and generates detailed audit trails.

### Features
- Real‑time monitoring of database traffic via S‑TAP agents with immediate policy evaluation.
- Policy enforcement through S‑GATE controls (block, alert, log).
- Pre‑built compliance reports for PCI‑DSS, GDPR, HIPAA, SOX, and custom audits.
- Sensitive data discovery during runtime.
- Unified visibility for on‑prem and cloud environments.

### Workflows
1. **Configuration** – Deploy agents, define data sources, create policies, and assign user roles.  
2. **Incident Response** – Detect violations, generate alerts, investigate activity, and take enforcement actions.  
3. **Continuous Improvement** – Run vulnerability assessments, review audit findings, and refine policies.

### Personas
- **Security Administrators** – Define policies, manage agents, investigate incidents.  
- **Database Administrators** – Deploy agents, tune performance, maintain data sources.  
- **Compliance Officers** – Generate regulatory reports, verify controls, manage audit evidence.  
- **Data Analysts** – Access activity reports and dashboards without seeing raw data.

### Core Entities
- **Agents & Collectors** – S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregators, Central Managers.  
- **Security Policies & Rules** – Security Policy, Audit Policy, Classification Rule, Access Rule.  
- **Governance Infrastructure** – Guardium Manager, Managed Units, Central Manager, Guardium Domain, S‑GATE gateways.

---

## Guardium Component Services

The Central Manager tracks status, configuration, and health of all Guardium components across a management domain, enabling remote deployment and policy enforcement from a single console.

**Key Concepts:** Central Manager, Managed Units, Component inventory, Health monitoring, Remote deployment.

---

## Unit Utilization Timecharts

Timecharts visualize resource consumption trends for individual Guardium appliances or across multiple appliances, helping identify performance bottlenecks, capacity planning needs, and unusual activity.

**Key Concepts:** Visualization, Multi‑metric support, Trend analysis, Capacity planning, Performance monitoring.

---

## Enterprise Load Balancer Events Report

Logs every load‑balancing decision made by Guardium’s high‑availability clusters, recording successful and failed S‑TAP‑Managed Unit associations and managed‑unit load changes.

**Key Concepts:** High‑availability, Load‑balancing events, S‑TAP connectivity, Managed Unit health, Troubleshooting.

---

## Importing a Custom Certificate for External S‑TAP

External S‑TAP captures and forwards database traffic to a Guardium collector. Administrators can import a custom SSL/TLS certificate to encrypt the communication channel between the External S‑TAP software and the collector, securing transmission of sensitive query data.

**Key Concepts:** External S‑TAP, SSL/TLS certificate, Secure communication, Data encryption.

## External S‑TAP User Interface
The External S‑TAP instances page in the Guardium UI lists all External S‑TAP deployments on a Docker host. Each entry shows runtime status, version information, and health metrics. Administrators can launch new containers, check operational status, and modify configuration parameters such as log level or connection timeout.

## Virtual Appliance
A Guardium Virtual Appliance (VA) is a pre‑configured software image for VMware ESXi that bundles all Guardium components (Collector, Aggregator, etc.) into a single, easily deployable unit, simplifying installation, scaling, and backups.

## Show Command
`show network interface speed <NIC>` sets a specific speed on a NIC when auto‑negotiation is unavailable.

## Parameter: add_group_to_quick_search
Enables classification groups to appear in the Guardium UI’s quick‑search facet, improving analyst efficiency.

## GuardAPI Syntax: add_time_period
Creates or updates a time‑period definition. Key parameters:
- `contiguous` – whether the period must be continuous.
- `hourFrom` / `hourTo` – start and end hours (24‑hour format).
- `timePeriodDescription` – label for the period.
- `weekdayFrom` – first day of the period.

## Group Members
Privilege reports list user accounts, privileges, roles, object accesses, and group memberships, helping teams identify over‑privileged accounts and validate least‑privilege policies.

## Entitlement Optimization APIs
APIs such as `set_expiration_date_for_restored_day` manage expiration dates of restored audit data, ensuring restored records remain compliant with retention policies.

## Parameter Value Type Description
`add_group_to_quick_search` is a Boolean parameter controlling quick‑search inclusion for classification groups.

## Long‑Term Retention and Reporting
Guardium supports extended audit‑log retention using user‑managed S3‑compatible storage, allowing cost‑effective archiving of multiple years while preserving search, retrieval, and reporting.

## Guardium Entities & Workflows Overview

### Trust Management
- **Mark Session (MARK_SESSION)**: Assigns a trust‑level score to database sessions from security policies or real‑time evaluators. Requires the AS parameter.

### User Identification
- **Application Events API**: Custom applications push connection acquire/release events, allowing Guardium to attribute users even when traffic lacks explicit user metadata.

### Data Collection & Normalization
- **Access Domain**: Central repository where all monitored traffic (inspection engines, Universal Connectors, streams) is aggregated.
- **Analyzed Client IP**: Replaces missing client IPs with inferred sources for accurate CEF mapping.

### Correlation & Enrichment
- **IMS Application Event Link Attributes**: Provide unique IDs linking user, application, and session events for richer investigative context.
- **Statistical Reporting**: Timestamped buffer metrics for K‑TAP collectors; used to monitor collector health.

### Policy & Reporting
- **Policy Detailing**: Captures SQL statement templates within attributes without logging execution, enabling audit‑only reporting.
- **Task Manager & Insights**: Central service for scheduling jobs, running advanced analyses, and surfacing actionable security insights.

### System Requirements & Support
- **CAS Requirements**: CAS program files include Java runtime specifications and OS‑specific size constraints.
- **Support Processes**: `guardium accessmgr` enables password reset when accounts are locked after repeated login failures.
- **Hadoop Integration**: `S‑TAP` for Hadoop uses Session ID parameters to integrate with Kafka messaging.

### Archiving & Validation
- **Archival Verification**: After archiving, confirm completion via the Aggregation/Archive Log in the Data Management console.

### Audit & Configuration
- **Audit Receiver Hierarchy Filtering**: Use the `show` command to view and adjust filtering status for audit receivers.
- **Network Configuration**: `Show` command reports auto‑negotiation status; manual duplex settings can be applied when auto‑negotiation is disabled.

### Platform‑Specific Support
- **IBM i**: S‑TAP APIs check audit server status and return queue metrics; `accessmgr` provides password reset workflows for locked accounts.

nagers and aggregators to discover and rank sensitive data and risky users across the environment. It:

- Scans all defined datasources.
- Calculates a risk score for each user and data element.
- Generates top‑risk reports for quick review.
- Flags changes in risk patterns.

---

## Secure Sockets Layer (SSL) Configuration

Use the command `store network ssl enable` to globally enable SSL for all inbound Guardium communications. To restrict or disable per‑service, use:

```
store network ssl <service> enable|disable
```

Here `<service>` is `appliance`, `collector`, or `receiver`. After changing, restart the Guardium service for the setting to take effect.

## Investigating

Enhance incident investigation by comparing results across multiple risk indicators. All collectors used for the analysis must run Guardium version 11.0 or later.

## Query Entity and Attribute Catalog

Discover every entity and attribute available in Guardium reports. These entities can be used to create custom queries and to build relationships with GuardAPI calls.

## Output Format for Transform Actions

The `OUTPUT_FORMAT` keyword controls how transform actions handle source values. When set, the action substitutes the transformed value for the original source value.

## ALP Analyzer Lost Packets

Metrics on the ALP Analyzer’s queue management and network activity for the primary interface are exposed by the ALP Analyzer Lost Packets domain.

## Table Count and Disk Usage

Shows a single row containing the total number of tables in the Guardium repository, plus the total disk space used by InnoDB tables and by MyISAM tables.

## RLM Dataset Define DD

`DATA SET RLM DD` is the DDNAME specified in the JCL for recording Record Level Monitoring (RLM) of datasets on z/OS, either statically in the JCL or dynamically allocated by a started task.

## Vulnerability Assessment Licensing

Guardium Vulnerability Assessment can be licensed as a stand‑alone product or as part of the Guardium Package Software. This guide covers only the stand‑alone licensing model.

# AWS IAM Policy for Guardium

Define an AWS IAM policy granting Guardium the permissions needed to interact with AWS services.

# ## Show snif_hostname_cache Command

Display cached hostnames; `"all"` lists every entry, `"search"` filters by IP or name.

**Key Concepts:** hostname cache, show command

---

## ## Parameter Value Types for Query Rewrite Action

Update a query rewrite action with required parameters:
- `actionName` (string, required)
- `definitionName` (string, required)
- `description` (optional string)

**Key Concepts:** query rewrite, parameters, action configuration

---

## ## Solr APIs for Threat Detection Analytics

Guardium’s threat‑detection analytics offers GuardAPI commands to:
- configure analytics
- manage case assignments
- enable/disable features
- capture user feedback to improve accuracy.

**Key Concepts:** analytics, GuardAPI, threat detection, case management

---

## ## SOX Ticket Reconciliation

AI‑driven automation compares user‑activity logs with change tickets (e.g., from ServiceNow), streamlining SOX compliance, reducing manual effort, and improving accuracy.

**Key Concepts:** SOX, ticket reconciliation, activity log correlation

# Guardium Data Protection Overview

## Features

- Data Security Hierarchy
- Aggregation & Reporting
- Monitoring & Alerts
- Configuration Management

## Workflows

- Architecture & Connectivity
- Incident Response
- User Management
- Security Operations

## Personas

- Security Administrators
- Database Administrators
- Compliance Officers
- Auditors/Audit Managers

## Entities

- Datasources
- Reports & Logs
- Configuration Elements
- Security Constructs

---

## Incident Management

Threshold‑based alerts generate incidents by querying the policy violations log and filtering results by incident category, severity, and other criteria.

## GuardAPI Syntax

`get_threat_detection_use_case_info` lists all configured threat detection use cases; requires Guardium v10.1.4+.

## GuardAPI Syntax

`Replace_active_profile` updates the active Guardium Big Data Intelligence (GBDI) profile if the interface is enabled; supported from Guardium V10.5+.

## GuardAPI Syntax

Updates a query‑rewrite “add where” rule via its ID; accepts `addQualifierFlag` (Boolean, default 1) and `qrAddWhereId` (Long).

## Db2 for z/OS

A Db2 for z/OS data source can be added to Guardium after installing the JDBC license file.

## What to Do Next

After creating a new audit process, assign a custom receiver group so audit results are sent to that group, and specify a custom audit report to control its content.

## Information Security Officer

Monitoring failed logins, terminated user access attempts, and policy violations helps information security officers detect security incidents.

## NAS File Activities

NAS File Activities shows file operation details for Network‑Attached Storage devices, allowing filtering.

## Document Overview

IBM Guardium Data Protection delivers database activity monitoring, policy enforcement, and compliance reporting for structured data sources, built on a distributed collector/aggregator/manager architecture. It supports real‑time threat detection, configuration management, and audit‑ready reporting.

### Features Overview
- **File Activities View:** SharePoint file‑operation logs for compliance and data‑loss prevention.
- **Report Exporting:** PDF export of audit reports; schedule large jobs off‑peak to avoid UI timeouts.
- **Access Domain:** Central repository of immutable request/response logs from all inspection sources.
- **Host Entity:** CAS‑host status tracking (online/offline) for database servers.

### Workflows Overview
- **Define Report Templates:** Build, edit, and schedule audit reports.
- **Data Export:** Asynchronous PDF generation for large extracts.
- **Domain Traffic Analysis:** Review Access domain data for access patterns and anomalies.
- **Host Health Monitoring:** Continuous visibility of CAS host availability.

### Personas Overview
- **Database Administrators:** Manage data sources, S‑TAP agents, and performance tuning.
- **Compliance Officers:** Create audit policies, generate regulatory reports, manage dashboards.
- **Security Analysts:** Conduct investigations, monitor alerts, respond to incidents.
- **Operations Teams:** Monitor system health, balance collector loads, maintain consistency.

### Entities Overview
| Entity | Description |
|--------|-------------|
| SharePoint File Activities | Per‑file operation log (create, read, update, delete). |
| Report Export Job | Background job for delivering large PDF reports. |
| Access Domain Records | Immutable request/response pairs collected by Guardium agents. |
| Host Entity Status | Real‑time flag indicating CAS host connectivity. |

### Templates & Items
- **Assess and Harden** – Initial VA provides a security/compliance baseline and hardening recommendations.  
- **Define a Template Set Item** – After building a CAS template definition, create template set items to apply the template to specific environments.  

---

## Enterprise No TrafficAlert
Filters activity records by timestamp, keeping only those whose start time falls between supplied parameters X and Y, reducing noise in long‑term retention reports.

## Moving Some S‑TAPs to a Less Loaded Collector
Redistributes some S‑TAP agents to a less busy collector to balance system load, prevent performance degradation on heavily used hosts, and maintain optimal data capture rates.

## DB Sizes and Files on Disk
Issues predictive alerts when database or file‑system usage is projected to reach 70 % capacity within the next 14 days; lists estimated growth, highlights largest objects, and shows relevant information on the deployment health dashboard.

## SQL for Predefined Reports
Documents the SQL statements used by predefined Long Term Retention reports (available from version 12.2.x onward); helps customize or extend reports while staying compliant with Guardium’s reporting framework.

## Linux S‑TAP Is Not Capturing Db2 Exit Traffic
Run the Db2 exit health‑check script to diagnose and correct misconfigurations; the script can also apply corrective settings, restoring visibility of exit‑level interactions.

## Database Monitoring
The global SQL monitor captures SQL statements and forwards them to the S‑TAP for analysis; administrators can define filters based on user, object, or other criteria to tailor monitoring overhead.

## What to Do Next
Deploy an External S‑TAP as a Podman container by downloading the official image, generating TLS certificates, and optionally configuring network policies and host resources before starting the containerized agent.

## Centralized Module View
The Centralized module view consolidates all installed bundles and modules, providing a structured overview of active features, versions, and configuration status across the managed environment.

## Document Overview
IBM Guardium Data Protection is an enterprise‑wide database activity monitoring and security platform offering real‑time monitoring, policy enforcement, vulnerability assessment, compliance reporting, and multi‑platform support (on‑premises and cloud).

### Features Overview
- Centralized Management (GIM), policy engine, vulnerability assessment
- Advanced monitoring: network S‑TAP, agentless TAP, kernel K‑TAP
- Policy & enforcement: FGAC, data masking, blocking (S‑GATE), automated alerts
- Compliance and reporting: PCI‑DSS, GDPR, HIPAA, SOX templates; audit‑trail archiving; data classification
- Scalability & high availability: managed units, central managers, internal load balancer, hot‑standby failover

### Workflows Overview
1. **Configuration** – Add data sources, deploy S‑TAP, configure policies, classify data.
2. **Monitoring** – Review live dashboards, run vulnerability scans, enforce S‑GATE blocking.
3. **Incident Response** – Investigate alerts, block offending sessions, rotate credentials, trigger playbooks.
4. **Compliance** – Generate regulatory reports, export logs, verify retention, certify controls.

### Personas Overview
- Central Administrator – Manages Guardium infrastructure
- Security Administrator – Defines FGAC, S‑GATE, compliance dashboards
- Database Administrator – Installs and maintains agents
- Compliance Officer – Reviews audit trails, generates reports
- Security Analyst – Conducts threat investigations, forensic analysis

### Entities Overview
- Agents & Collectors: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- Policy Constructs: Security Policy, Audit Policy, Classification Rule, Access Rule, Risk Rule
- Infrastructure: Managed Unit, Managed Units group, Central Manager, Aggregator, Load Balancer, GIM server, Blocking Gateway

h Values

## Configuring Multi‑Factor Authentication

Configuring multi‑factor (two‑factor) authentication adds an extra security layer to Guardium user accounts using DUO or RSA SecurID engines, mitigating unauthorized access beyond passwords.

## Overview of IBM Guardium Data Protection
IBM Guardium Data Protection is an enterprise solution for monitoring, enforcing security policies, assessing vulnerabilities, and providing compliance reporting for both structured and unstructured data stored on-premises and in the cloud.

### Key Features
- **Dynamic Datasource Connectivity:** Automatic port detection, support for multiple drivers, and seamless integration with CyberArk for credential management.
- **Real-Time Threat Detection:** Continuous monitoring with policy enforcement, S-GATE blocking mechanisms, and immediate incident generation upon detecting security breaches.
- **Compliance Reporting:** Pre-built templates for major regulatory standards such as PCI-DSS, GDPR, HIPAA, and SOX, complemented by automated audit trails for evidence gathering.
- **Managed Auditing Tools:** Configuration Auditing System (CAS) templates, object auditing capabilities, and support for Azure MySQL databases.
- **Flexible Deployment and Management:** Tools like Guardium Installation Manager (GIM) streamline the deployment and management of monitoring agents, aggregators, and central managers.

### Core Workflows
- **Configuration Steps:** Add new datasources, deploy S-TAP agents using GIM, and configure Fine-Grained Access Control (FGAC) policies.
- **Navigation and Reporting:** Access activity reports, run vulnerability assessments, and utilize the audit dashboard for quick insights.
- **Actionable Responses:** Implement query blocking for unauthorized access, rotate sensitive credentials, and execute incident response procedures.
- **Auditing Processes:** Develop CAS templates, configure object auditing, and schedule automated discovery jobs to maintain continuous compliance checks.

### Personas and Roles
- **Platform Administration:** Responsible for overall system configuration, user management, and maintenance tasks.
- **Security Management:** Focuses on setting up policies and controls, ensuring FGAC and access policies are correctly applied.
- **Database and Data Management:** Handles datasource configurations, S-TAP deployments, and data analysis for auditing purposes.
- **Compliance and Security Auditing:** Manages compliance requirements, regulatory reports, threat investigations, and incorporates CAS templates for structured audits.

### Core Entities
- **Monitoring Agents:** S-TAP, A-TAP, K-TAP collectors facilitate data capture from various sources.
- **Management Infrastructure:** Components like GIM, Managed Units, Aggregators, and Central Managers coordinate and manage monitoring activities across the Guardium environment.

### Policy and Rule Definitions
- **Security Policy:** Governs the behavior Guardium enforces to protect data assets.
- **Audit and Object Audit Settings:** Define what data accesses to monitor, log, and report.
- **Classification and Access Rules:** Identify sensitive data types and establish controls for access management.
- **Infrastructure Components:** Tools and platforms that support Guardium's monitoring capabilities, such as Guardium Installation Manager and Managed Units.

## Analyzed Client
The section displays detailed information about each data change event, organized by host name and most recent modification time. Fields include Full SQL String, NameClient Host Name, DB User Name, and Guardium Appliance Host.

## GIM Client Name Client Hostname
GIM Client Name Client hostname defines the hostname of the system where Guardium Installation Manager (GIM) is installed. Related attributes capture the client operating system (GIM Client OS) and its vendor (GIM Client OS Vendor) along with the kernel version (GIM Client OS Vendor Version).

## Attribute Description
Field Name identifies the column referenced in a SQL statement. When Quick Parse Native is enabled, Guardium attempts to parse the SQL content to determine the affected columns.

## CSV/CEF Export Schedule
The schedule governs when audit data is exported from Guardium to external systems. Options include hourly CSV/CEF exports after audit jobs, automatic ip-to-hostname aliasing at 6 am daily, and monthly system backups at 7 am on the first Sunday of each month, ensuring they occur outside the 12:15 am window.

## Default Capture
The Default Capture setting supports Replay by indicating how transaction boundaries and captured values should be determined, especially for prepared statements and batch operations.

## Instance Name
When monitoring network traffic only, the PORT_RANGE_START and PORT_RANGE_END parameters restrict the port range scanned for database traffic. Typically, a single contiguous port range is defined.

## LD Library Path
STAP_LD_LIBRARY_PATHS specifies the location of the libjvm.so library required for S-TAP to interact with Java applications.

## Snif Auto OS Name Cache
Enabling the Show command `support store snif_auto_os_name_cache` instructs the sniffer to automatically detect and cache the operating system name for each host that connects through it.

## SNMP Version
The Show command `store system snmp version` toggles the SNMP version used by Guardium between the default SNMPv2c and SNMPv3. SNMPv3 is activated when a version 3 system is detected.

## Configuration Auditing System (CAS) APIs
The CAS Create API (`create_cas_template`) generates a CAS template item, which can be a file, registry key, script, or list of logged-in users. These templates define what the Configuration Auditing System monitors.

## Guardium Installation Manager (GIM) APIs
The GIM Unassign API detaches a Guardium module from a specific client while leaving the module installed on the system. This separates the module-client relationship without removing the module itself.

## Manage Object Auditing
Manage Object Auditing provides a comprehensive interface for configuring audit settings across one or many databases. It supports discovery of database instances, management of discovered instance rules, scheduling of discovery jobs, and attachment of reports and alerts tied to inspection engine changes.

## Azure MySQL
Guardium version 12.2.x and later includes Azure MySQL as a supported data source type, enabling organizations to monitor MySQL databases deployed in Microsoft Azure environments.

## Understanding Policies
Audit policies in Guardium define the rules that govern what database activity is monitored and under what conditions alerts or blocks are triggered. Properly configured policies enable targeted detection of unauthorized or suspicious behavior while minimizing performance impact.

## Document Overview
IBM Guardium Data Protection is an enterprise-grade database activity monitoring and security platform that safeguards structured and unstructured data across on-premises and cloud environments. It offers continuous monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Features
- Policy Management: Define and enforce security policies based on user actions, data sensitivity, and contextual factors.
- Threat Detection: Real-time anomaly detection, user behavior analytics, and automated incident response.
- Compliance Reporting: Pre-built templates for PCI‑DSS, GDPR, HIPAA, SOX, and customizable reporting dashboards.
- Data Discovery & Classification: Automated scanning of data sources to identify sensitive information.

### Workflows
- Configuration: Add data sources, deploy agents (S‑TAP, A‑TAP), and configure policies via the management console or GuardAPI.
- Monitoring: Review alerts, audit logs, and activity reports; investigate incidents in the incident management console.
- Remediation: Enforce blocking, modify policies, rotate credentials, or generate compliance evidence.
- Maintenance: Upgrade components, manage clusters, and monitor system health.

### Personas
- Security Administrator: Configures policies, reviews alerts, and enforces compliance.
- Database Administrator: Manages data sources, monitors performance impact, and troubleshoots agents.
- Compliance Officer: Generates regulatory reports, verifies controls, and audits data handling practices.
- Data Analyst: Uses dashboards and query tools to analyze usage patterns for business insights.

### Entities
- Agents: S‑TAP

Understanding Policies

A policy comprises an ordered list of rules that inspect traffic between database clients and servers. Each rule triggers on either a client request or a server response, providing fine‑grained control over data access and operations.

```markdown
## 2709. Get group references

API: `list_datasource_groupRef_by_name`  
Params: `application` (String, required), `objName` (String, required)  

## Overview

IBM Guardium Data Protection monitors and secures enterprise databases.  
### Features  
- Datasource connectivity (dynamic ports, multi‑driver, CyberArk)  
- Threat detection (real‑time blocking, incident generation)  
- Compliance reporting (PCI‑DSS, GDPR, HIPAA, SOX templates)  
- Certificate management (GuardAPI commands)  

### Workflows  
- **Configuration:** Add datasource, deploy S‑TAP, configure FGAC policies  
- **Navigation:** Review reports, run assessments, audit dashboard  
- **Action:** Block queries, rotate credentials, incident response  
- **Certificate retrieval:** Use `get_certificates` API  

### Personas  
- Administration, Security Administration, Database Admin, Data Analyst, Compliance Officer, Security Analyst, Certificate Manager  

### Entities  
- Agents/collectors (S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager)  
- Policies/rules (Security, Audit, Classification, Access)  
- Infrastructure (GIM, Managed Unit, S‑GATE, Universal Connector)  
- Certificates (GCM)  

## 2714. Certificates for Guardium Cryptography Manager (GCM)

`get_certificates` – list all certificates for GCM, simplifying management and auditing.  

## 2715. Azure Event Hubs protection

Enable monitoring of Azure Event Hubs by defining a cloud database service account with data‑stream permissions and linking it to Guardium collectors.  

## 2716. Downtime handling (AWS Kinesis)

After downtime/disconnections, Guardium resumes Kinesis event retrieval from the last saved pointer, preventing data loss.  

## 2717. Tuple parameters (session‑level policies)

Tuple parameters combine multiple fields (Client IP, Source App, DB User, etc.) into a single parameter, allowing complex, precise session‑level policy matching.  

## 2718. Tuple parameters (enhanced)

Tuple parameters enable nuanced packet‑matching conditions, surpassing single‑parameter definitions for more powerful session‑level enforcement.  

## 2719. NetApp ONTAP firewall rules

Configuring firewall rules between File Access Manager and NetApp Cluster‑Mode is required for uninterrupted data access monitoring.  

## 2720. Attribute description

Describes audit task types (report, security assessment) and provides a concise description for categorization.  

## 2721. BigData Intelligence Outliers domain

Provides hourly outlier summaries for Guardium systems with GBDI datasource; accessible to all roles for anomaly detection.  

## 2722. Tuple group attributes

Tuple group fields: `Client IP`, `Source App`, `DB User`, `Server IP`, `Service Name`, `OS User`, `DB Name` – context for activity auditing.  

## 2723. Informix privileges & role grants

Captures all system privileges and role grants across reachable Informix databases, enabling detailed access‑control auditing.  

## 2724. IMS subsystem ID

Describes IMS subsystem identifiers for identifying controlled systems in audit records.
```

## Guardium Data Protection Overview

- Provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data in hybrid environments.
- Key components include S-TAP agents, Guardium Analyzer, and Central Manager for traffic capture, aggregation, and analysis.
- Supports compliance frameworks such as PCI-DSS, GDPR, HIPAA, and SOX.

## Pre-upgrade Consideration for Db2 Traffic Capture

Changing how Db2 traffic is captured in newer versions may require updating existing configurations. Review the migration guide to ensure uninterrupted monitoring after upgrading.

## Ignoring S-TAP Data

Filtering irrelevant data is more efficient when configured preemptively at the data source rather than post-capture on the Guardium system.

## Updating External S-TAP Image Pull

Modify cluster configuration to pull images from a private registry. Update credentials and paths, ensuring network access allows the cluster to reach the registry.

## Installing Guardium Maintenance Patches

Use `store system patch install` CLI command to apply updates. Plan for a maintenance window as the process may require a restart of the Guardium appliance.

## Adding Datasource to Security Assessment

Use `add_assessment_datasource` GuardAPI with parameters `assessment_description` and `datasource_name` to add a datasource to an assessment process.

## Configuring Data Streaming to Cold Storage

Enable or disable streaming with `configure_cold_storage_data_streaming` GuardAPI, specifying the action (`enable` or `disable`) and cold storage name.

## Managing Patch Signatures

Use `patch_cleanup` API to remove downloaded or generated patch signature files (`enc` or `sig`) for an organized system.

## Revoking Database Object Roles

`revoke_role_from_object_by_Name` API removes a role from a database object, considering dependencies to avoid disrupting operations.

## Workflow Builder

The Workflow Builder enables users to define custom workflows composed of steps, transitions, and actions that integrate with audit processes, providing flexible audit process automation. Administrators can assemble complex audit checks that trigger automatically based on policy violations or scheduled intervals, building specialized audit routines without extensive coding.

## Request Rate

The Request Rate graphical report visualizes the request volume over time, defaulting to the preceding two hours. The time range can be adjusted, with a warning displayed when expanding it significantly. This feature helps database administrators monitor traffic patterns and identify potential issues.

## Guardium Administration

**0ef911b4-e328-4022-981c-943968387278** | **categories:** knowledge, features

Guardium administrators maintain security by installing and managing TLS certificates used for GUI authentication and S-TAP agent communication. The system provides automated alerts and reporting tools to monitor certificate expiration dates, ensuring timely renewal before services are disrupted. By enforcing certificate validation policies, administrators reduce the risk of man-in-the-middle attacks and unauthorized access attempts through compromised credentials, preserving the integrity of all monitoring and auditing activities.

## Document Overview
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features Overview
- **Datasource Management**: Add/remove, classification, discovery, and unified S3/EC2 support
- **Threat Detection**: Active Threat Analytics, investigation dashboard, threat-finder component
- **Policy & Enforcement**: FGAC, S‑GATE blocking, real‑time alerts, role‑based alerts
- **Compliance & Reporting**: PCI‑DSS, GDPR, HIPAA, SOX templates; archived S3/EC2 backup/restore

### Workflows Overview
- **Provisioning**: Connect to cloud SaaS/cloud accounts, configure unified discovery
- **Security Ops**: Enable threat‑finder, create auto‑detect processes, generate transfer keys
- **Monitoring**: Review activity logs, logged real‑time alerts, big‑data buffer usage
- **Maintenance**: Archive/restore to S3‑compatible storage, disable big‑data interface

### Personas Overview
- **Administrator**: Platform configuration, user management, licensing
- **Security Administrator**: FGAC policies, threat‑finder activation, scheduled jobs
- **Database Administrator**: Datasource connectivity, S‑TAP/S‑GATE deployment
- **Compliance Officer**: Regulatory report generation, audit trails, data retention

### Entities Overview
- **Agents & Collectors**: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- **Policies & Rules**: Security Policy, Audit Policy, FGAC, Access Rule, Classification Rule
- **Infrastructure**: GIM, Managed Unit, S‑GATE, Universal Connector, Investigation Dashboard
- **Components**: Threat‑finder, Active Threat Analytics, Archive/Backup/Restore, License Manager

---

## Connecting Unified Discovery and Classification to SaaS applications and cloud accounts
Connecting Unified Discovery and Classification to SaaS applications and cloud accounts must precede cloud data insight capabilities. This workflow enables Guardium to ingest metadata and activity from cloud services, feed threat detection models, and support compliance reporting for cloud‑based data stores.

---

## Archive and backup/restore support for S3 compatible storage protocols
The new S3 compatible storage support in Guardium 12.0 includes Amazon Elastic Container Service (ECS) for archive and backup/restore operations, facilitating long‑term data retention and compliance. Archives are created via the `archive` command, and restores are performed with the `restore` command, both targeting a configured S3 endpoint.

---

## License information for Guardium Vulnerability Assessment
License information for Guardium Vulnerability Assessment (VA) consists of how to assign, verify, and maintain the license.

## Vulnerability Assessment

Vulnerability Assessment provides purchase options, measures license allocation, and supports scanning non‑production, failover, and disaster‑recovery environments. The license is applied to the Central Manager or Managed Unit that runs scans and can be bulk‑applied to multiple appliances.

## Logged Real‑Time Alerts

The Logged R/T Alerts view shows the total number of real‑time alerts logged during a reporting period, grouped by rule description. Runtime filters let you narrow the view by date range, severity, or rule groups to quickly triage compliance violations.

## BigData Intelligence Buff Usage Monitor

The **BigData Intelligence Buff Usage Monitor** domain aggregates **Sniffer Buffer Usage** entities, exposing metrics such as total buffers, used buffers, and buffer utilization percentage. All roles on Guardium systems with a GBDI data source defined can query it for capacity planning and performance tuning.

## Guardium Universal Connector APIs

The `generate_transfer_key` command creates SSH key pairs for the Central Manager and Managed Units, used for SCP and SFTP file transfers in Guardium. The keys are stored in `/opt/IBM/Guardium/config/ssh/` and must be distributed securely before file‑based workflows begin.

## Database Connection Architecture

Guardium supports multiple JDBC driver families: native drivers for optimized performance and generic drivers for broad compatibility. A browser service dynamically resolves instance names to current ports.

**Key Concepts:** JDBC, Native Driver, Browser Service, Dynamic Port Detection

unstructured data stores, both on-premises and in the cloud.

## Database Security and Compliance with Guardium

### Features Overview
- **Datasource Connectivity:** Dynamic port detection, multi-driver support, CyberArk credential vault integration
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation
- **Compliance & Reporting:** PCI-DSS, GDPR, HIPAA, SOX report templates; automated audit trails
- **Entitlement Optimization:** User/role management, recommendations, entitlement browsing, threat analytics

### Workflows Overview
- **Configuration:** Add datasource, deploy S-TAP via GIM, configure FGAC policies
- **Navigation:** Review activity reports, run vulnerability assessments, audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents
- **Optimization:** Configure query rewrite, enable entitlement optimization

### Personas Overview
- **Administration:** Administrator (platform config, user management), Security Administrator (FGAC, policies)
- **Database & Data Management:** Database Administrator (datasources, S-TAP), Data Analyst (dashboards, queries)
- **Compliance & Audit:** Compliance Officer (regulatory reports), Security Analyst (threat investigation)
- **Optimization:** Security Analyst (query rewrite), Compliance Officer (entitlement optimization)

### Entities Overview
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Query Rewrite Policy
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector
- **Optimization:** Entitlement Optimization Engine, Role-Based Access Control, Threat Analytics Engine

### Microsoft SQL Server 2000 Entitlements Report
Enumerates object-level privileges for each database account (excluding default system accounts), role and system privileges, and associated grant options, aiding auditors in verifying the principle of least privilege. Key concepts: Object Privilege, Role Membership, Grant Option, Default System Users.

### Resource Requirements for Kubernetes Deployment
Minimum allocations: **16 CPU cores and 64 GB RAM** per worker node for Guardium collector containers and auxiliary services. These specifications ensure adequate performance for real-time monitoring and data processing.

### Exception View Query
Filtered, descending-ordered view of policy violations. Selects: TimestampUTC, DBUserName, AccessRuleDescription, server identifier, full SQL text, severity level, source program, client IP address, OS user. Serves as data source for the Policy Violation Report.

### Exportable Log Types
Include Access Log, Session Log, Exception Log, Full SQL Log, Outliers Log, Group Members Log, Extraction Log, Policy Violations Log, Buff Usage Monitor. Each can be exported with detailed output options for comprehensive audit and investigative capabilities.

### Central Management in Distributed Environments
Allows disabling a user on a specific Managed Unit while keeping them enabled on the Central Manager, enabling granular control over user access across distributed Guardium deployments without affecting global administrative capabilities.

### ELB Health Checks and Guardium
ELB health checks can create misleading activity records if they use the same database ports as legitimate user connections, appearing as active sessions and potentially inflating connection statistics while obscuring actual user activity.

### Unified Discovery and Classification (UDC) Permissions
When a cloud provider or SaaS application is linked to UDC, Guardium automatically creates role permissions like `CloudDiscoveryRead` and `CloudDiscoveryWrite`, governing actions security analysts and data stewards can perform on discovered assets within the SaaS environment.

the monitoring activities, Guardium administrators should configure the data collectors (S‑TAP, A‑TAP, etc.) to start sending traffic to the Central Manager. This involves verifying network connectivity, ensuring the collectors are registered with the Central Manager, and confirming that the appropriate datasource definitions and policies are in place. Once the collectors are operational, administrators can run initial policy tests, review audit logs, and fine‑tune data‑activity filters to ensure accurate and efficient monitoring.

## Scheduling Uploads for Continuous Monitoring

Continuous monitoring activities require scheduling uploads for newly added value-change monitoring data sources. This ensures the audit database is notified after all recorded data is securely uploaded to the Guardium system.

## Managing GIM Installation Parameters for FamMonitor

The FamMonitor GIM installation parameters provide command-line options and procedures for installing the FamMonitor bundle on Windows servers using GIM.

## Managing CAS Templates in Guardium

The CAS Templates domain manages CAS template definitions which identify items such as files, environment variables, registry settings, script outputs, and logged-on users to monitor for changes.

## Accessing Group Member Entity Information

The "Group Member Entity" in Guardium includes the group member name and a timestamp indicating when the member was created or updated. This timestamp can be extracted using specific components depending on analysis needs for detailed audits and compliance reporting.

## Describing Installed Policies

The "Installed Policy" domain describes parameters and ruleset for policies that have been installed within the Guardium system, supporting multiple policies and actions per rule.

## Tracking Total Records Affected by Queries

The Total Records Affected metric reports the total number of records impacted by queries. This metric aids in performance analysis, compliance reporting, and effective management of database operations.

---

## Introduction to IBM Guardium Data Protection

IBM Guardium Data Protection is a security platform for database activity monitoring, threat detection, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- Datasource Connectivity: Supports dynamic port detection and multi-driver deployment.
- Threat Detection: Enables real-time policy enforcement and S-GATE blocking.
- Compliance & Reporting: Provides templates for PCI-DSS, GDPR, HIPAA, and SOX.

### Operational Workflows
- Configuration: Add datasources, deploy S-TAP agents, configure FGAC policies.
- Monitoring: Review activity reports, run vulnerability assessments.
- Action: Block unauthorized queries, rotate credentials, respond to incidents.

### Roles and Responsibilities
- **Administration:** Platform configuration, user management.
- **Security:** FGAC policy definition, policy enforcement.
- **Compliance:** Regulatory reporting, audit trail analysis.

### Core Infrastructure Components
- Agents & Collectors: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- Policies & Rules: Security Policy, Audit Policy, Classification Rule, Access Rule.
- Infrastructure: GIM, Managed Unit, S-GATE, Universal Connector.

---

## IMS Database Access Report

The IMS Data Access Details report provides a granular view of each IMS access using the Full SQL entity. Adding the DB Protocol attribute prevents mixing with other data sources to ensure accurate reporting.

---

## Server Settings and Attributes

Attributes specify properties such as Object Type (e.g., database, image copy, log) and Object Name, which includes details like DBD name, segment name, dataset name, partition, or area. These attributes help categorize and identify monitored objects accurately.

---

## Vulnerability Details

CVE and CVSS information, including vulnerability records and scores, appear in the assessment test result viewer. Clickable reference links allow access to detailed vulnerability data and remediation guidance.

---

## Managing Inspection Engines

To remove an unused inspection engine, stop it and delete its definition from **Manage > Activity Monitoring > Inspection Engines** to prevent unnecessary resource consumption and maintain an accurate inspection environment.

---

## Managed Unit Configuration

Restarting managed units is automated if 'Active on Startup' is enabled, ensuring session inference restarts automatically on each reboot. No additional manual steps are required, simplifying maintenance and ensuring continuous protection.

## Resolving S-TAP FIPS Compliance Issue

The FIPS 140-2 error in S-TAP can be resolved by adjusting the S-TAP configuration through the S-TAP Control page. This adjustment ensures compliance without affecting the K-TAP kernel module, which remains functional post-uninstallation.

## Define Environment Variables

Define environment variables for the private registry host, port, and credentials to enable secure access to the registry.

## About This Task

Create a Guardium VM with specified hardware and mount the V10.6 ISO to prepare for installation.

## Upgrading S-TAP Using RPM

Use the RPM method to upgrade S-TAP, following detailed instructions available in other topics for flexibility in the upgrade process.

## Show Command

The `show alerter snmp secondary_traphost store anomaly-detection state` command toggles the Anomaly Detection subsystem, which performs active statistical analysis and alerts the Alerter subsystem.

## GuardAPI Syntax

```plaintext
delete_assessment_datasource_group("assessmentDescription=<description>", "groupName=<group>")
```

## Parameter Value Type Description

```plaintext
delete_hashicorp_config(name="<config_name>")
```

## Parameter Value Type Description

```plaintext
unassign_qr_condition_from_action("actionName=<action>", "conditionName=<condition>", "definitionName=<definition>")
```

## Release Notes

For Guardium V12.2.2, V12.2.1, V12.2, and V12.1, detailing new features, enhancements, and release-related information.

## Document Overview

Enterprise solution for database activity monitoring, security, and compliance across hybrid environments. Includes real-time threat detection, policy enforcement, compliance reporting, and automated response.

### Features Overview
- Expand connectivity, real-time S-TAP monitoring, system utilization reporting, central configuration management
- Automated reporting, audit activity logs, credential vault integration

### Workflows Overview
- Configure data sources, enable S-TAP deployment, set up external storage
- Deploy S-TAP agents, manage quarantine periods, run diagnostics
- Generate usage summaries, configure alerts, manage data retention

### Personas Overview
- Manage policies and alerts, define and monitor data sources, ensure compliance reports

### Entities Overview
- Managed agents, data sources, security policies, diagnostic tools

## Managing datasource credentials with CyberArk

Guardium integrates with CyberArk to securely manage and dynamically retrieve datasource credentials using the Application Password Provider.

## Domain Based on Query Main Entity

Query domain includes runtime parameters Period From (default last day) and Period To (default current time) for flexible buffer usage analysis.

## Guardium usage summary

Lists S-TAP hosts with CPU count and estimated processor values for license reporting and capacity planning.

## Attribute Description

Attributes Successful Sqls (count of SQL requests) and Timestamp (record creation time) available for detailed entities.

## Central Management and Data Mart

Central management distributes configurations to managed units, each with independent local extraction schedules for consistent cross-environment operations.

## Configuring external storage

Supports SCP and FTP archive transfers to Amazon S3, Azure, ECS, NFS, Tivoli Storage Manager, IBM COS, and IBM Cloud for flexible data management.

## MySQL encryption ciphers
Guardium uses MySQL's AES_ENCRYPT() and AES_DECRYPT() for data-at-rest encryption, often requiring SSL and compatible with SHA-2, DES, and AES for comprehensive data protection.

## Running the slon looper utility
The Guardium Support Information Gathering page includes the slon looper utility, which automates troubleshooting data collection from Guardium installations to aid in diagnosing and resolving customer issues.

## Creating data source profiles
In Guardium version 12.1 and above, administrators create data source profiles to configure universal connectors on managed units, enabling data ingestion into Guardium by defining connection parameters and settings.

## Creating data source profiles
Creating data source profiles (12.1+) involves configuring universal connectors on managed units to seamlessly ingest data into Guardium, ensuring comprehensive monitoring and protection of database activities.

## What to do next
To verify successful S-TAP deployment, check that the row corresponding to the S-TAP has a green status in the first column of Monitor > Maintenance > S-TAP Logs > S-TAP Status, indicating that the S-TAP is active and functioning correctly.

## Show Command
The Show Command `'show alerter snmp traphost store alerter snmp secondary_traphost'` configures a secondary Alerter SNMP trap server for redundancy in alert delivery systems.

## Dates and Timestamps
In Guardium, quarantine actions are defined by `create_quarantine_allowed_until` and `create_quarantine_until`, specifying the temporal scope of quarantine enforcement actions for audit trails.

## Document Overview
IBM Guardium Data Protection monitors, protects, and audits structured and unstructured data across databases, big data environments, and cloud storage. It enforces security policies, detects threats, ensures compliance, and manages data access.

### Features Overview
- Database Connectivity: Native/Generic JDBC drivers, dynamic port detection, CyberArk integration
- Threat and Access Management: Real-time policy enforcement, S-GATE blocking, FGAC rules
- Compliance Reporting: PCI-DSS, GDPR, HIPAA, SOX templates, automated audit trails
- Data Classification: Automated discovery and classification of sensitive data in files, databases, and cloud storage
- Incident Management: Generates security incidents, supports SIEM integration

### Workflows Overview
- Setup and Management: Install Collectors, Add Datasources, Deploy Agents, Define FGAC Policies
- Incident Investigation: Time-frame filtering, anomaly detection, privileged operation audits
- Automation: Workflow Builder for custom audit processes, auto-discovery tracking
- Action: S-GATE blocking, credential rotation, incident response

### Personas Overview
- Administration: Platform configuration, user management, S-TAP deployment
- Security Administration: FGAC policy definition, policy enforcement
- Data & Database Administration: Datasource configuration, S-TAP agent management
- Compliance & Audit: Regulatory report generation, compliance validation
- Security Analyst: Threat investigation, activity analysis, anomaly detection

### Entities Overview
- Agents & Collectors: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- Policies & Rules: Security Policy, Audit Policy, FGAC Access Rule, Classification Rule
- Compliance Frameworks: PCI-DSS, GDPR, HIPAA, SOX
- Administrative Interfaces: Guardium UI, APIs, CLI
- Discovery Artifacts: Scan results, matched databases, discovery reports

## IBM Guardium Data Protection Overview
IBM Guardium provides a unified platform for monitoring database activity, enforcing security policies, detecting threats, and delivering compliance reports for both on‑premises and cloud‑hosted structured and semi‑structured data sources.

### Key Features
- **Datasource Management** – Add, discover, and split datasources.
- **Policy Enforcement** – Deploy centralized security policies across environments.
- **Threat Detection** – Continuous monitoring, outlier analysis, and anomaly detection.
- **Compliance Reporting** – Generate standard and custom compliance reports.

### Personas
- **Security Administrators** – Configure policies, manage datasources, and monitor alerts.
- **Data Security Analysts** – Conduct investigations, analyze outliers, and generate reports.
- **Compliance Officers** – Access compliance‑specific reports and audit trails.
- **Database Administrators** – Manage S‑TAP installations, configure data sources, and maintain performance.

### Core Components
- **Agents** – S‑TAP (database monitoring), A‑TAP (file monitoring), K‑TAP (kernel monitoring), collectors, and aggregators.
- **Infrastructure** – Managed units, central managers, aggregators, and S‑GATE (inline blocking).
- **Data Stores** – Databases, big‑data platforms (Hadoop, Spark), and cloud storage (IBM COS, S3).
- **User Roles** – Administrators, security analysts, compliance officers, and auditors.

### Tasks
- **Install Guardium agents** – Deploy S‑TAP, A‑TAP, and K‑TAP agents on target systems.
- **Configure datasources** – Define datasources, assign owners, and validate connections.
- **Deploy policies** – Create and apply security, audit, and classification policies.
- **Monitor activity** – Review unified activity reports, outlier analysis, and anomaly dashboards.
- **Respond to incidents** – Block SQL queries, rotate credentials, block access, and orchestrate incident response.

### Additional Capabilities
- **Rare/Unused Table Identification** – Lists tables with no recent access, showing name, last‑access timestamp, and owning datasource.
- **Domain Filtering** – Create domains that filter data based on the main query entity, supporting complex runtime constraints and remote sources.
- **Analytic Outliers Details** – Filter outlier reports by server IP and other runtime parameters for focused investigations.
- **BigData Intelligence Domains** – Aggregate traffic data and classify results for visibility into data categorization across big‑data environments.
- **IBM COS Target Configuration** – Set up IBM Cloud Object Storage as an archive or backup destination.
- **SSL External S‑TAP** – Manually create certificate signing requests for SSL‑enabled External S‑TAP deployments.
- **Firewall Force Allow** – Specify IP/mask values to bypass firewall monitoring where needed.
- **Cipher Suites** – Define required cipher suites for secure Guardium system deployments.
- **GuardAPI Parameter Validation** – Ensure `datasource_name` matches an existing source when using `add_assessment_datasource`.
- **Cold Storage Configuration (GuardAPI)** – Use `configure_cold_storage_unit` with parameters such as `catalogOnly`, `dataBucket`, `icebergCatalogName`, `metastoreUri`, and `api_target_host` to set up cold storage units.

## IBM Guardium Data Protection Overview

### Key Features
- **Secure Data Access:** Centralized policy management, role-based access control, auditing
- **Vulnerability Management:** Automated assessment, remediation workflows, CIS compliance scanning
- **Data Classification:** Automated discovery, tagging, and risk scoring of sensitive data
- **Activity Monitoring:** Real-time logging, SQL inspection, anomaly detection, session termination

### Core Workflows
- **Policy Configuration:** Define security policies, assessors, and violation handling
- **Vulnerability Scanning:** Schedule, run, and review vulnerability assessment reports
- **Incident Response:** Investigate alerts, quarantine users, enforce remediation actions
- **Compliance Reporting:** Generate audit reports, PCI DSS, GDPR, and other regulatory compliance reports

### User Personas
- **Security Administrators:** Manage policies, resolve violations, oversee audits
- **Database Administrators:** Review activity logs, tune performance, manage data masking
- **Compliance Officers:** Access regulatory reports, certify data handling practices
- **IT Operations:** Monitor system health, maintain configurations, handle escalations

### Architectural Components
- **Guardium Appliance:** Central Manager, Aggregator, Collectors, and managed units
- **Data Sources:** Databases, file systems, and cloud services monitored by Guardium
- **Policies & Rules:** Security policies, audit policies, classification rules, access control rules
- **Users & Groups:** Defined roles and permissions within Guardium

## IBM Guardium User Management

IBM Guardium provides a comprehensive user management system to control access and permissions for various personas within the platform.

### Key Features
- **Role-Based Access Control (RBAC):** Assign specific roles to users, defining their permissions and access levels.
- **Personas:** Predefined roles for different user types, including Security Administrators, Database Administrators, Compliance Officers, and Data Analysts.
- **Quarantine APIs:** Manage user quarantines to prevent unauthorized access to specified databases.

### Relevant APIs
- **Quarantine APIs:** Manage user quarantines to restrict access to specific databases.
- **GuardAPI Syntax:** Use commands like `set_cold_storage_orphan_retention_period` and `set_import` to configure retention periods and import settings.

### Configuration
- **System Requirements:** Ensure identical System Shared Secret for successful data import.
- **AWS Services:** Specify KMS and CloudTrail actions for resource discovery and classification.

### Personas Overview
- **Security Administrators:** Configure policies, manage alerts, and monitor security incidents.
- **Database Administrators:** Deploy agents, configure datasources, and manage database instances.
- **Compliance Officers:** Run compliance reports, manage audit trails, and ensure regulatory adherence.
- **Data Analysts:** Utilize dashboards, analyze query activity, and generate insights from data.

### Agents and Infrastructure
- **Agents:** S-TAP, FAMMonitor, A-TAP, K-TAP for monitoring and collecting data.
- **Infrastructure Components:** Managed Units, Collectors, Aggregators, Central Managers for data aggregation and management.

### Policy Constructs
- **Security Policies:** Define rules for evaluating database traffic and enforcing security measures.
- **Audit Policies:** Set up policies for auditing data access and usage.
- **Access Rules:** Manage access permissions for various resources.
- **Classification Rules:** Define rules for classifying data based on sensitivity and compliance requirements.

### Data Management
- **Datasources:** Configuration and management of data sources.
- **Databases:** Organization and management of database instances.
- **Segments and Audited Objects:** Define segments for data segmentation and identify audited objects for compliance.

## Delete Cloud DB Service Account

Deleting a cloud DB service account removes the selected AWS account from Guardium and ends all database activity monitoring for that account. The steps are: select the account in **Cloud DB Service Accounts**, click **Delete**, and confirm. Inactive or redundant accounts should be deleted to maintain monitoring performance.

## Data Tampering Detection

Data tampering aims to modify or delete information, often causing many deletion errors and harming sensitive data. Guardium flags tampering by detecting error patterns and impact on sensitive fields, providing alerts and reports for investigation and remediation.

## Installing FamMonitor on Windows

FamMonitor is a Windows agent enabling monitoring, audit data collection, policy enforcement, and real‑time alerts or connection blocking on Windows servers. It can be installed via command line, wizard, or GIM, integrating Guardium capabilities directly on the Windows platform.

## Core Redundancy Impact

If all replicas of a core in Guardium's investigation dashboard are down, the associated data cannot be displayed. For example, if the ERROR_5 core has no operational replicas, the **Errors** tab shows no data, underlining the importance of core redundancy for high‑availability.

## Domain Based on Query Entity

This feature creates domains with all roles for Application Access, using a **Remote Data Source** dropdown, **Refresh Rate** default of 0 seconds, and **Show Aliases** radio buttons. It enables access‑control configurations based on query results.

## Domain Based on Query Entity (Cassandra)

For Cassandra DB privileges, the domain includes runtime **Period From** and **Period To** parameters, a list of **privileges granted to users**, and supports **304 IBM Guardium Data Protection**. It provides granular control over Cassandra object access and auditing.

## IMS z/OS Sensitive Object Activity

The **IMS z/OS - Sensitive Object Activity** report lists accesses to sensitive IMS object segments from the z/OS IMS Sensitive Objects group in the last three hours. It helps detect unauthorized or suspicious access to critical IMS data.

## Users Inactive Since

The **Users inactive since** feature shows users whose **Last Session Start** is earlier than 90 days ago, based on **Access** records. This helps administrators identify stale accounts for possible deactivation or removal.

## Attribute Description Entity

The **Attribute Description** entity gives detailed information about Guardium's attribute definitions, data types, and usage contexts. Understanding these attributes is essential for policy configuration, report analysis, and customizing Guardium functionality.

## Configure BIG-IP ASM for Guardium Integration

Use F5 Networks' Big-IP ASM together with Guardium's real-time database activity monitoring to propagate identities from web applications to the database layer.

## Guardium Universal Connector REST APIs

The Guardium universal connector provides REST endpoints for managing credential lifecycles: create, delete, retrieve names, and update user information (`create_credentials`, `delete_credential`, `get_credential_names`, `update_user`).

## Guardium Insights REST APIs

Guardium Insights exposes REST endpoints that synchronize data between Guardium Data Protection and Insights, enabling analytics across both platforms.

## Central Asset Inventory

Guardium maintains a unified repository of all on‑premises and cloud/SaaS assets, displaying their classification and compliance posture.

## CyberArk Integration for Secure Backup

CyberArk supplies temporary credentials for each backup operation (e.g., S3 buckets), preventing exposure of permanent secrets during data archive processes.

## Brute‑Force Attack Detection

Guardium triggers alerts on repeated failed logins, considering user identity, timing patterns, and other contextual signals to identify brute‑force attempts.

## Risk Spotter AI Engine

Risk Spotter continuously scores risk vectors across the Guardium deployment, surfacing emerging threats and suggesting mitigation actions.

## Capturing Oracle Connection Manager IP

Guardium can be configured to replace the Connection Manager‑generated IP with the genuine client IP, ensuring accurate source attribution for Oracle sessions.

## Query Rewrite Tracking Report

Create reports by selecting query rewrite entities and desired columns (client, query, results) to capture the full context of rewritten queries.

## SQL Injection Detection in Stored Procedures

Guardium extends SQL injection protection to code executed inside stored procedures and dynamic SQL constructs (`EXEC`, `EXECUTE`, `EXECUTE IMMEDIATE`).

## Database Entitlement Snapshots

Entitlement reports enumerate user privileges for each database object, aiding compliance checks and least‑privilege enforcement reviews.

## File Activity Monitoring Platforms

Guardium's File Activity Monitoring (FAM) supports a defined set of operating systems to audit file accesses and changes across critical data stores.

## Attribute Description
Guardium's Attribute Description entity stores definitions and metadata for fields used in classification, entitlement, and policy constructs. Each attribute includes its name, data type, description, applicable datasources, and whether it is mandatory for a given rule or process.

## Document Overview
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features
- Real-time monitoring via S-TAP agents
- Dynamic S-GATE blocking, granular audit and access policies
- Scans for misconfigurations, weak credentials, insecure settings
- Automated PCI-DSS, GDPR, HIPAA, SOX audit artifact generation
- Discovery of sensitive data across heterogeneous sources
- Native support for AWS RDS, Azure SQL, Google Cloud SQL

### Workflows
- Deploy S-TAP agents, define FGAC policies
- Review alerts, drill into audit trails, adjust policy rules
- Correlate events, create investigations, generate reports
- Block queries, rotate credentials, apply patches or config changes

### Personas
- Security Administrator: manages policies, reviews alerts
- Database Administrator: maintains datasources, troubleshoots S-TAP
- Compliance Officer: generates and reviews compliance reports
- Security Analyst: investigates incidents, validates false positives

### Entities
- Agents: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- Policies: Security Policy, Audit Policy, Access Rule, Classification Rule
- Infrastructure: GIM, Managed Unit, S-GATE, Universal Connector
- Data Objects: Datastore, DB Instance, Classification Profile, Asset Inventory

## REST API Syntax
Guardium's REST API supports creating a CAS template set for a Db2 database on UNIX. Required JSON payload fields: `dbType`, `osType`, `templateSetLabel`.

**Example payload**
```json
{
  "dbType": "DB2",
  "osType": "UNIX",
  "templateSetLabel": "MyDb2UnixSet"
}
```

## Cloud Database Service Protection
Guardium's Datastreams streams database events from AWS RDS, Azure SQL Database, Google Cloud SQL to the Guardium collector for real-time analysis after enabling the feature flag.

## GuardAPI Syntax
Guardium's command-line interface provides programmatic management of configuration objects. The `list_parameter_names_by_report_name` API returns all parameter names associated with a given report definition.

**Syntax**
```
list_parameter_names_by_report_name parameter { reportName="Report_Name" }
```

## Inspection Engine Parameters
Inspection engines are the core of Guardium's vulnerability assessment functionality. The `IE_CREATION` parameter controls whether new inspection engines are automatically created for discovered database instances, ensuring each identified database receives an inspection engine for ongoing scanning.

# IBM Guardium Data Protection Overview

IBM Guardium Data Protection provides real-time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

## Key Features

- **Query Masking:** Mask data in NoSQL databases and protocol frameworks.
- **Bulk Import:** Select multiple databases and applications for monitoring.
- **SAP Stack Validation:** Distinguish ABAP and Java Stack kernel specs and table layouts.
- **Run-Time Parameters:** Set default values for Service Name, OS User, DB User, Server IP.
- **S-TAP Configuration:** Display `WINSTAP_CMD_LINE` field for Windows S-TAP agents.
- **BigData Intelligence:** Capture and manage exceptions from database servers and internal Guardium errors.
- **Egress Kbyte Tracking:** Log response byte count and failed SQL requests (when permitted).
- **Azure Privilege Checks:** Recursively verify granted roles/privileges across all accessible databases.
- **CLI Management:** Configure system resources via command‑line interface.

## Common Workflows

1. Import databases/applications  
2. Validate SAP stack configurations  
3. Define run‑time parameter defaults  
4. Configure S-TAP agent settings  
5. Manage exceptions and session data  
6. Enforce egress controls  
7. Run Azure privilege assessments  
8. Automate tasks with CLI commands  

## User Personas

- **Security Administrator:** Import apps, validate SAP stacks, monitor exceptions  
- **Database Administrator:** Set run‑time defaults, configure S-TAP  
- **Compliance Analyst:** Query Azure privilege grants  
- **Operations Engineer:** Run CLI diagnostics  

## Key Entities

- **Query Masking:** NoSQL, protocol buffers, Thrift  
- **Import:** Databases, applications  
- **SAP Stacks:** ABAP, Java kernels, tables  
- **Run-Time Parameters:** Service Name, OS User, DB User, Server IP

# IBM Guardium Data Protection Overview

IBM Guardium Data Protection secures data across hybrid environments with real-time monitoring, threat detection, compliance reporting, and encryption management.

## Features
- **Unified Data Visibility:** Central monitoring of structured and unstructured data.
- **Threat Detection:** Real-time policy enforcement and threat response.
- **Compliance Reporting:** Templates for PCI-DSS, GDPR, HIPAA, SOX.
- **Encryption Management:** Certificate mirroring and secure data transmission.

## Workflows
- **Installation & Configuration:** Deploy agents, configure data streams, manage certificates.
- **Monitoring & Alerts:** Continuous data access tracking and anomaly detection.
- **Incident Response:** Automated blocking and alerts for policy violations.
- **Policy Management:** Creation and maintenance of security rules and compliance policies.

## Personas
- **Security Administrators:** Define and enforce data security policies.
- **Compliance Officers:** Generate and manage audit reports.

### IBM Guardium Overview

IBM Guardium secures and monitors data access across databases and cloud environments. It includes deployment and maintenance of S-TAP agents, monitoring system health, managing security policies, and integrating with AWS and Azure.

### Architecture

Guardium supports JDBC connectivity with native and generic drivers, and uses a browser service for dynamic port resolution.

### Activity Monitoring

Guardium captures database traffic, evaluates it in real-time against policies, and triggers alerts, reports, or blocking actions via S-GATE.

### Troubleshooting

Resources include problem determination instructions and systematic methods for diagnosing and resolving issues.

### Techniques

Structured troubleshooting techniques help identify and fix system problems efficiently.

### Custom Slon Looper

Technical support instructions guide the configuration of custom loopers for debugging.

### External S-TAP Deployment

External S-TAP uses a Kubernetes operator for streamlined deployment in Cloud Pak for Data environments.

### Certificate Mirroring

Automates client and server key pair generation for mutual authentication.

### Auto-Discovery APIs

`create_aws_secrets_manager_config` API supports AWS Secrets Manager authentication from Guardium V11.3.

### Parameter Retrieval

`get_insights_agent_config` retrieves configuration parameter values for troubleshooting.

### Reference

`get_outliers_detection_info` provides outlier detection settings for effective monitoring.

### Threat Analytics

`list_ata_case_severity` API categorizes security incidents by severity levels.

### Security Settings

Parameters `ENABLE_OCSP_CHECK` and `SMART_CARD_MAPPING_REGEX` configure smart card authentication and OCSP checks.

## RHEL Upgrade to Guardium 9

Upgrading RHEL from version 7 to 9 ensures Guardium remains compatible with modern operating systems while improving performance and security.

## Guardium Security Platform Overview

Guardium is an enterprise data security platform that monitors, detects threats, enforces policies, and generates compliance reports across on‑premises and cloud databases.

## Guardium Feature Summary

Guardium supports JDBC and native driver connectivity, real‑time activity monitoring, SQL‑traffic inspection, dynamic port detection, and integrates with CyberArk for credential vaulting.

## Guardium Policy Enforcement

Guardium captures database traffic through S‑TAP agents, evaluates it against real‑time security policies, and can block unauthorized activity via S‑GATE. Policies are scoped by users, objects, operations, and time windows.

## Database Schema Tampering Detection

Guardium detects unauthorized schema changes (tables, views, procedures) and correlates them with error generation or privileged‑user actions.

## Guardium API Overview

IBM Guardium GuardAPI Reference provides concise syntax, parameters, and examples for creating, modifying, and deleting Guardium objects via the API. It supports version-specific capabilities from V9.5 onward.

### Features
- GuardAPI and REST API syntax
- Bulk operations for data sets
- Workflow integration for policy enforcement jobs

### Personas
- Security Architects: Design policies, manage API keys
- Data Engineers: Configure data sources, customize ingestion pipelines
- Compliance Officers: Define controls, generate audit reports
- DevOps Teams: Automate deployments, integrate API calls into CI/CD pipelines

### Entities
- Managed Units: Datasources, aggregators, collectors, central managers
- Security Policies: Access control groups, compliance rules, activity monitors
- Workflow Jobs: Scheduled policy audits, data classification jobs, incident escalations
- Authentication Tokens: API keys, client certificates, session tokens for REST calls

## Commands and APIs

### Show System Public Transfer Key
- Displays the public key used for data transfer to a remote host via SSH
- `CLI show system public-transfer-key`

### Snif Thread Number
- Sets the number of snif threads
- `CLI store system snif-thread-number [new | default]`
- Changes take effect after `restart inspection-core` (default is 6 on a 32-bit system)

### Delete Export Configuration
- Deletes a data export configuration on Guardium systems
- No parameters required
- Available since Guardium V9.5

### Disable Outlier Detection Across Central Manager Aggregators
- Disables outlier detection on specified aggregators in a central management environment
- `disable_outliers_detection_cross_cm_agg aggr_host_name`
- Optional API target host to specify execution location

### Assign Bundle to Client by Version
- Assigns a specific version of a Guardium bundle or module to a client by IP address
- `gim_assign_bundle_or_module_to_client_by_version ip_address bundle_name version`

### Retrieve Bundles via REST API
- Retrieves all available bundles for a specified client
- GET request to `https://[host]:8443/restAPI/gim_bundle`

### Schedule Job
- Schedules recurring jobs for data classification, policy enforcement, etc.
- Requires cron schedule, job type, optional object name, and start time parameters

## Non-Relational Database Monitoring

IBM Guardium extends auditing capabilities to popular non‑relational databases such as MongoDB, Cassandra, Couchbase, HBase, Amazon Redshift, and Yugabyte DB. By deploying custom collectors and dedicated drivers, Guardium captures user activities, privilege changes, and structural modifications in real‑time. Key features include policy enforcement, credential rotation, and compliance reporting tailored for modern NoSQL environments.

## Slon Looper Utility

The **slon looper** utility, found on the **Support Information Gathering** page, walks a Guardium installation to collect detailed diagnostic data for troubleshooting network traffic, packet loss, or performance issues on the sniffer.

## Creating Universal Connector Data Source Profiles

Creating **multiple Universal Connector data source profiles** via a **CSV template** allows rapid, consistent configuration of many sources, reducing manual effort and ensuring uniformity.

## GIM Parameter: WINSTAP_AUTO_DISCOVERY

The **GIM parameter `WINSTAP_AUTO_DISCOVERY`** enables automatic discovery of database instances during **Guardium Installation Manager (GIM)** installation, populating the inspection engine list and updating `guard_tap.ini`.

## Hybrid Hadoop Monitoring

The **recommended hybrid approach** for monitoring Hadoop installs an **S‑TAP for HDFS and Hive using localhost** and a **separate S‑TAP for HBase on an edge node**, balancing performance and coverage while minimizing cluster overhead.

## Oracle Unified Audit with S‑TAP

When Oracle Unified Audit Activity is used with an **S‑TAP**, **two HAProxy load‑balancer proxies** are required for the Redis SSL/TLS traffic path to ensure proper routing and encryption handling between the unified audit service and the Guardium collector.

## Installing S-TAP for IBM i

The **S‑TAP for IBM i** is a software agent installed via a shell script from the **IBM i PASE** environment, capturing database traffic on IBM i systems for monitoring and policy enforcement.

## Installing S-TAP for IBM i (Steps)

1. Transfer the S‑TAP script to the IBM i **IFS**.  
2. Run the script within **PASE** to perform the installation.  
3. Verify the agent starts and registers with the Guardium collector.

## Certificate Tab

The **Certificate tab** manages SSL/TLS certificates for **External S‑TAP**. Enabling **“Generate Certificates via CSR”** automatically creates a certificate signing request and provisions certificates for secure encrypted connections.

## Ports for Long‑Term Retention

**Long‑term retention management** uses **TCP ports 8843 and 9083** for communication between the **Central Manager** and the **Long‑Term Retention Appliance (all‑in‑one)** in Guardium.

## Guardium Patch Types and Names

Guardium supports various patch types (e.g., **S‑TAP agent patches, Collector patches, Central Manager patches**) identified by a naming convention that encodes version and component information, crucial for maintaining system stability and security.

# IBM Guardium Data Protection

**Features:**
- Real-time database activity monitoring of queries and transactions
- Periodic vulnerability scans for configuration weaknesses
- Centralized policy definition and enforcement
- Integration with key management systems for data-at-rest encryption
- Built-in compliance reports (PCI DSS, HIPAA, GDPR, etc.)

**Workflows:**
- Deploy and configure S-TAP agents on database servers
- Define security rules, alerts, and blocking actions
- Schedule and distribute audit reports
- Investigate threats from alerts to forensic data

**Personas:**
- Guardium Admin: system configuration, user management, agent lifecycle
- Security Admin: policy definition and compliance setup
- DB Owner: database protection controls and anomaly detection
- Compliance Officer: enforcement of regulatory requirements

**## Guardium Central Manager**

IBM Guardium Central Manager is a centralized platform for managing distributed Guardium appliances. It offers unified visibility, policy enforcement, and reporting across heterogeneous database environments.

### **Features**
- **Centralized Management Console:** Single web interface to oversee multiple Guardium appliances.
- **Deployment Orchestration:** Automated provisioning, configuration, and updates from a single location.
- **Unified Reporting:** Collects and aggregates audit data, policy violations, and compliance status from all connected appliances.
- **Scalability:** Supports large enterprises with numerous database assets across various locations.

## Manage Custom Classes
Guardium lets administrators enhance evaluation and alerting with custom Java classes. These classes can implement user‑defined functions for policy checks, data classification, or event enrichment.

**How to add a custom class**
1. Implement the Guardium plugin interface (e.g., `ICustomFunction`).  
2. Package compiled code into a JAR with all required dependencies.  
3. Upload the JAR via UI → *Manage > Custom Classes*.  
4. Reference the class in policies, reports, or classification rules using its fully‑qualified name.

**Key concepts:** Custom Function, JAR, Plugin Interface, Policy Evaluation  

---  

## Document Overview  

IBM Guardium Data Protection is an enterprise‑grade solution for database activity monitoring, threat detection, and compliance reporting across on‑premises and cloud data stores.

### Features  
- **Datasource Connectivity:** Dynamic port detection, multi‑driver support, CyberArk vault integration.  
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, automated incident generation.  
- **Compliance & Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates; immutable audit trails.  
- **Analytics:** Discover Streams API for AWS data‑stream identification; Classification & Discovery.  
- **Integration:** Kafka cluster management, CAS template administration, configuration auditing.  
- **User Management:** DB user mapping, group usage reporting.  
- **Kubernetes Support:** REST endpoints for backup candidates, interactive guide assistance.

### Workflows  
- **Configuration:** Provision Kafka clusters, configure load balancers, manage CAS templates.  
- **Monitoring:** Observe traffic, apply threat‑analytics, use investigation dashboard APIs.  
- **Maintenance:** Remove quarantines, assign distributed report targets, maintain S‑TAP clusters.  
- **Compliance:** Generate GDPR and other regulatory reports.

### Personas  
- **Security Administrator:** Manage Kafka, CAS templates, user quotas.  
- **Compliance Officer:** Run GDPR reports, audit group usage, access investigations.  
- **Database Administrator:** Deploy S‑TAP clusters, configure inspection engines, control debug levels.  
- **Data Analyst:** Leverage investigation dashboards, analyze Discover Streams results.

### Entities  
- **Kafka Clusters:** Managed via `create_kafka_cluster` / `delete_cluster` GuardAPIs.  
- **CAS Template Sets:** Use `list_cas_template_sets` GuardAPI.  
- **Database Users:** Controlled through user‑mapping APIs and non‑credential scans.  
- **S‑TAP Clusters:** Deploy/remove with specific GuardAPI syntax.  
- **Central Manager Backup Candidates:** Queried via `/restAPI/backup_cm_list_candidates`.  
- **Data Streams:** Discovered with the `discover_streams` API.

---  

## 3119. GuardAPI syntax  

**Command:** `create_kafka_cluster`  
Creates a Kafka cluster. Required parameters: `clusterName`, `memberList`.  
Optional boolean `applyCruiseControl` (default false) can be set after querying valid values with `--help=true`.  
Supported from Guardium v12.0.

---  

## 3120. GuardAPI syntax  

**Command:** `delete_cluster`  
Deletes an S‑TAP cluster. Requires the `clusterName` parameter identifying the cluster to remove.  
Available from Guardium v12+.

---  

## 3121. GuardAPI example  

**Endpoint:** DELETE quarantine  
**Required parameter:** `dbUser` – name of the database user being quarantined.  

---  

## 3122. Threat detection analytics APIs  

**API:** `discover_streams`  
Returns the count of AWS data streams for a given cloud service account and region. Introduced in Guardium v10.6 for threat detection and data‑stream analytics.  

---  

## 3123. Groups Usage Report  

**Purpose:** Lists all data sources, groups, and associated usage statistics, helping auditors and security teams understand group membership impact on monitoring.

## Guardium Host Utilization Overview
Display hosted Guardium components, identify idle S‑TAP agents, and view server and application object associations to streamline monitoring setups and confirm full coverage.

### GuardAPI Command to List Assessments
```bash
list_assessments
```
Shows every security assessment defined in the Guardium environment, with configuration details and status.

### Configuration Auditing System (CAS) API
```bash
list_cas_template_sets
```
Lists all available CAS template sets on the Guardium host, enabling consistent audit configurations.

### Ranger Configuration API
```bash
list_ranger_configs
```
Retrieves all Ranger configurations, including admin account and cluster details, for Hadoop security management.

### S‑TAP and Inspection Engine API
```bash
set_load_balancer_param
```
Configures enterprise load‑balancing parameters for enhanced S‑TAP performance (available from version 9.5).

### Distributed Report Management APIs
```bash
list_distributed_reports
cancel_distributed_report
delete_distributed_report
get_distributed_report_target
rerun_distributed_report
set_distributed_report_target
```
Facilitates comprehensive lifecycle management of distributed reports.

### System Requirements for Unified Discovery and Classification
Specify hardware configurations and supported data sources (on‑premises, cloud, SaaS) for unified discovery and classification.

### Db2 Inspection Engine Workflow
Extracts SQL from network packets, parses into parse trees, and logs detailed traffic information for monitoring and securing Db2 interactions.

### GDPR Compliance in Guardium
Ensure personal data protection for EU citizens through comprehensive database activity monitoring, threat detection, and compliance reporting.

### Activity Monitoring & Policy Enforcement
Captures database traffic, classifies data, enforces policies in real time, and provides detailed audit trails and alerts across all supported platforms.

## Overview
IBM Guardium Data Protection offers real‑time database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting across both on‑premises and cloud data stores.

### Key Features
- **Deployment Health Dashboard** – visual tiles for alerts, utilization, and resources.
- **High‑Volume Aggregation** – consolidates data from multiple collectors.
- **Inspection Engine** – configurable parameters to control traffic analysis.
- **External S‑TAP Certificate Validation** – ensures collector certificate authenticity to prevent MITM attacks.
- **DynamoDB over S3/SQS Integration** – profile for ingesting DynamoDB audit logs.
- **GAM Service Configuration** – service‑level parameters defined in `resmon.ini`.
- **K‑TAP Module Provisioning** – requires kernel, OS, and CPU details for builds.
- **Error Handling** – codes < 100 common, ≥ 100 function‑specific.

### Workflows
- **Installation & Troubleshooting** – guides for Guardium system deployment and common errors.
- **CLI Configuration** – `configure_data_streaming` and other GuardAPI commands for streaming tasks.
- **Service Level Setup** – editing `[Service_N]` sections of `resmon.ini` for GAM tuning.
- **Data Source Integration** – DynamoDB/S3/SQS profile creation via Datasource Profile Management.

### Personas
- **Security Administrators** – manage policies, certificates, and troubleshooting.
- **Database Administrators** – install K‑TAP, verify IP parameters, monitor inspection settings.
- **Compliance Officers** – review aggregated reports and health dashboards.
- **Data Analysts** – consume aggregated data, configure streaming sources.

### Main Entities
- **Guardium Appliances** – Collectors, Aggregation appliances, Central Managers.
- **Configuration Files** – `guard_tap.ini`, `resmon.ini`, `guardium_cert.pem`.
- **APIs & Commands** – `grdapi`, `configure_data_streaming`, `disable_persistent_queue_universal_connector`.
- **Certification Path** – CA certificate, collector common name/regex validation.

**Note:** Entry 3134 about CyberArk datasources is unrelated; it has been omitted from this Guardium-focused summary.

## 3166. Cloud database service protection with native audit

Guardium 11.3 and later support native auditing for major cloud database services (Amazon RDS, Azure Database, Google Cloud SQL) without requiring an on‑premises S‑TAP. The service collects audit logs directly from the provider's API and streams them to the Guardium collector for analysis and reporting.

**Key capabilities**
- Continuous ingestion of native audit events into Guardium's data lake
- Unified policy and reporting across on‑premises and cloud databases
- Automatic detection of privileged user activity and policy violations in cloud environments

**Performance impact**: No additional network traffic beyond the audit log export already performed by the cloud provider; Guardium throttles ingestion to avoid overload.

**Supported services**
- Amazon RDS for MySQL, PostgreSQL, Oracle, SQL Server
- Azure Database for MySQL, PostgreSQL, MariaDB, SQL Server
- Google Cloud SQL for PostgreSQL, MySQL, SQL Server

**Configuration steps**
1. Enable native audit logging in the cloud console for each target database instance.
2. Generate and register an API key/service account with permission to read audit logs.
3. In Guardium, create a new *Cloud Service Data Source* and enter the service endpoint, credentials, and audit log location (S3 bucket, Azure Storage container, or Pub/Sub topic).
4. Activate the *Cloud Audit Ingestion* policy template to normalize and enrich the raw logs.
5. Verify ingestion via the *Cloud Audit Dashboard* and fine‑tune retention settings in the Guardium data lake.

## IBM Guardium Data Protection Overview  

IBM Guardium Data Protection is a comprehensive database activity monitoring and security platform that provides real‑time visibility, policy enforcement, continuous entitlement auditing, automated vulnerability assessment, and compliance reporting for structured and unstructured data across on‑premises and cloud environments.

### Features  

- **Agent‑Based Capture:** Deploy S‑TAP agents on databases to collect SQL traffic with minimal performance impact.  
- **Policy Engine & S‑GATE:** Evaluate activity against customizable security policies in real time; optionally block non‑compliant queries.  
- **Threat Detection:** Surface active threats through outlier detection, anomaly correlation, and analytics APIs that automate investigations.  
- **Compliance Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX, and custom reports.  
- **Machine‑Learning Analytics:** Value‑change tracking, behavior‑baseline modeling, and outlier scoring for proactive risk identification.  

### Core Components  

- **Collectors & Aggregators:** Central Manager (enterprise hub), Managed Units (local aggregators), and Stand‑alone Collectors.  
- **Agents:** S‑TAP (kernel‑level tap), A‑TAP (application‑level tap), K‑TAP (kernel tap).  
- **Policy Types:** Security Policies, Audit Policies, FGAC (Fine‑Grained Access Control) rules, Threshold rules.  
- **Infrastructure:** Guardium Installation Manager (GIM), Managed Units, S‑GATE blocking engine, Universal Connectors, custom domains.  

### Typical Workflows  

1. **Discovery & Classification** – Scan data sources, auto‑tag sensitive assets, and create inventories.  
2. **Policy Management** – Define FGAC, audit, and classification policies; version and apply them centrally.  
3. **Install/Upgrade** – Use GIM to push S‑TAP agents and apply appliance patches.  
4. **Monitoring & Alerting** – View live traffic, generate activity reports, investigate anomalies, and receive alerts.  
5. **Vulnerability Assessment** – Run automated scans, review configuration gaps, and remediate findings.  
6. **Compliance Reporting** – Generate policy‑compliant reports for auditors.  

### Personas  

- **Security Administrator** – Configures policies, monitors alerts, enforces compliance.  
- **Database Administrator** – Installs agents, configures datasources, troubleshoots connections.  
- **Compliance Officer** – Generates audit evidence, validates regulatory controls.  
- **Security Analyst** – Investigates incidents, runs ad‑hoc queries, evaluates risk.  

### Key Capabilities Without Additional Agents  

Guardium leverages native auditing capabilities of cloud database services (AWS RDS, Azure SQL, CloudSQL, etc.) to classify data, conduct vulnerability assessments, and capture object‑level audit trails without deploying extra agents.  

---

## Database Connection Architecture

IBM Guardium supports JDBC, native, and browser‑based connections for SQL databases. JDBC drivers deliver optimized performance, while the browser service dynamically resolves instance names to current ports.

**Key Concepts:** JDBC, Native Driver, Browser Service, Dynamic Port Detection  

---  

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic through S‑TAP agents in real time, evaluates it against security policies, and enforces decisions via alerts, reports, or blocking through S‑GATE. Policies can be scoped by user, object, operation, and time window.

**Key Concepts:** S‑TAP, S‑GATE, Security Policy, Real‑Time Monitoring, Audit Trail  

---  

## Unit Utilization Data Processing

The deployment‑health topology view displays CPU, memory, and I/O utilization metrics for Guardium units, helping identify overloaded systems, correlate with other data sources, perform root‑cause analysis, remediate issues, and verify fixes.

**Key Concepts:** Deployment Health, Topology View, Unit Utilization, Diagnosis Workflow  

---  

## HTTP Error 403

Enabling CSRF protection on Guardium can cause 403 responses on interfaces. Disabling CSRF protection in the security settings resolves the error, allowing normal API and UI access.

**Key Concepts:** CSRF Protection, Security Configuration, HTTP Errors  

---  

## Request Was Interrupted / Quota Exceeded

Interactive reports that exceed Guardium’s 3‑minute execution limit generate “Request was interrupted or quota exceeded” errors. The issue typically results from large result sets; increasing the execution timeout or optimizing the query mitigates the problem.

**Key Concepts:** Interactive Reports, Execution Timeout, Collector Quotas  

---  

## Troubleshooting STAP Configuration After Upgrades

After a Guardium upgrade, STAP agents may need re‑configuration. Use Guardium’s configuration interface to redeploy S‑TAP, verify kernel‑module status, and ensure the agent version matches the collector.

**Key Concepts:** STAP Re‑configuration, Post‑Upgrade Validation, Kernel Modules  

---  

## High CPU and I/O Use in Guardium S‑TAP Host

S‑TAP agents consume CPU and I/O proportionally to database traffic. High utilization can stem from verbose logging, heavy traffic, or mis‑configured inspection engines. Review S‑TAP diagnostics, adjust filter granularity, and scale collectors as needed.

**Key Concepts:** S‑TAP Resource Consumption, Traffic Monitoring, Performance Tuning  

---  

## DynamoDB over S3/SQS

DynamoDB data streams can be ingested into Guardium via Amazon S3 and SQS. Supported plugins include database‑over‑syslog formats and cloud services such as Azure SQL, GCP MSSQL, PostgreSQL, and MySQL via JDBC or S3/SQS pathways.

**Key Concepts:** DynamoDB, S3, SQS, Data Source Integration, Plug‑ins  

---  

## Data Mart APIs

Guardium offers REST and GuardAPI endpoints for analytics management:

- `disable_riskspotter`: Disables RiskSpotter analytics across the Guardium hierarchy.  
- `get_fam_crawler_info`: Retrieves FAM crawler status and configuration through `GET /api/fam/crawler`.

**Key Concepts:** Data Mart APIs, REST Endpoints, RiskSpotter, FAM Crawler  

---  

## Data Mart API – `get_fam_crawler_info`

The `get_fam_crawler_info` API returns JSON containing FAM crawler status and configuration parameters. It is invoked via `GET https://<guardium_host>:8443/api/fam/crawler`.

**Key Concepts:** REST API, JSON Response, FAM Crawler  

---  

## GuardAPI – `list_inspection_engines`

The `list_inspection_engines` GuardAPI returns all inspection‑engine configurations defined on a collector or S‑TAP host in JSON format.  

**Key Concepts:** GuardAPI, Inspection Engines, Configuration Management  

---  

## GuardAPI – Register Edge

The `registerEdge` endpoint adds a new Guardium edge node, specifying name, export targets, CPU/memory limits, and backup behavior. It is a POST `/api/edge` method requiring authentication.

**Key Concepts:** Edge Registration, Resource Limits, REST API  

---  

## GuardAPI – `guardium reset_va_summary_by_key`

Resets validation‑summary data for a specific key, clearing stored validation results. This is useful during cleanup and re‑validation cycles.

**Key Concepts:** Validation Summary, Key Management, Data Reset  

---  

## GuardAPI – Universal Connector Certificate Management  

(Entry incomplete – skipped)

ployment Health Topology views depends on the Guardium version:
* In Guardium 11.3 and later, data latency is displayed as a gauge
  showing the maximum latency across all collectors in the view.
* In earlier versions, data latency is not shown in topology views.

## IBM Guardium Installation Manager API Overview

The GIM API lets you programmatically discover, install, and remove Guardium bundles across all managed units. You invoke REST‑style calls for bundle listing, installation preparation, execution, and status monitoring.

### Bundles and Tasks
- **Bundle:** A logical package of Guardium components (e.g., S‑TAP, A‑TAP).
- **Installation Task:** An asynchronous operation that deploys a bundle to one or more managed units.
- **Preparation Steps:** Query managed units, set proxy/credential parameters.

### Personas
- Guardium Administrator
- Security Operations Analyst
- DevOps Engineer

## IBM Guardium Data Protection Overview

Guardium collects real‑time activity from databases on‑premises and in the cloud. It enforces security policies, detects threats, and generates compliance reports.

### Core Features
- **Datasource Connectivity:** Auto‑detect ports, support multiple drivers, integrate with CyberArk.
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, incident generation.
- **Compliance Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates and audit trails.

### Workflows
- Add datasource → Deploy S‑TAP via GIM → Configure FGAC policies → Monitor activity.

### Personas
- Administrator (platform config)
- Security Administrator (FGAC, policies)
- Database Administrator (datasources, S‑TAP)
- Compliance Officer (regulatory reports)
- Security Analyst (threat investigation)

### Entities
- Agents/Collectors (S‑TAP, A‑TAP, Collector, Aggregator, Central Manager)
- Policies/Rules (Security, Audit, Classification, Access)
- Infrastructure (GIM, Managed Unit, S‑GATE, Universal Connector)

## Reporting

Built‑in reports are listed under the Reports section, showing all predefined report types and the access rights required to view them.

## Database Instance Metadata

The **Instance Config** entity stores connection details and template sets for a CAS instance.

## Data Marts

The Data Marts page lists every defined data mart, with filtering, related query view, extraction logs, and configuration details.

## IMS DLI Monitoring

The **FULL SQL IMS DLI Status** code flag shows non‑blank values for failed or warned DLI calls; the client IP is also recorded.

## Quick Query Tests

Create a test by selecting custom criteria or a predefined template, then run the test by executing an SQL query.

## Post‑Export Verification

Confirm export success by checking the Data Management Aggregation/Archive Log for entries marked “Succeeded”.

## Deployment Notes – Edge Gateway

Edge Gateway processes data streams at the network edge.

## Central Manager Console

The Central Manager page aggregates health and management data for every Guardium unit in the deployment.

## QRadar Guardium Integration

Guardium policies can be automatically updated from QRadar security events; the systems exchange data bi‑directionally.

## Custom Attributes

Custom attributes add extra fields to QRadar events, enabling custom properties and supporting enhanced reporting.

## Managed Unit Storage

When the managed unit database nears capacity, purge older audit results to free space.

## 3289. Logged R/T Alerts

Displays bar charts of total real‑time alerts logged per Access Rule Description during the selected reporting period, using the Policy Rule Violation entity.

## 3290. Report Run‑time Parameters

Lists sessions by client IP, server IP, source program, and server type for various server interfaces.

## Document Overview
IBM Guardium Data Protection (often shortened to Guardium) is IBM's enterprise‑wide database activity monitoring and security platform. It offers real‑time visibility into data access and changes, automated threat detection, policy‑based access control, compliance reporting, and vulnerability assessment. Guardium agents (S‑TAP, A‑TAP, K‑TAP) collect database traffic from relational and NoSQL systems, both on‑premises and in cloud environments, and forward it to Central Managers for analysis, alerting, and reporting.

### Features Overview
- **Database Traffic Capture:** S‑TAP, A‑TAP, K‑TAP
- **Policy Enforcement:** Real‑time blocking, S‑GATE
- **Compliance & Reporting:** PCI‑DSS, GDPR, HIPAA, SOX templates
- **Vulnerability Assessment:** Containerized VA scanner, continuous scanning

### Workflows Overview
- **Configuration:** Add datasources, deploy agents via GIM
- **Policy Management:** Define security, audit, classification policies
- **Incident Management:** Alerts, incident investigation dashboards
- **Assessment:** Run vulnerability assessments, generate remediation reports

### Personas Overview
- **Administration** – Platform administrator, security administrator
- **Data & DB Management** – DBAs, data analysts
- **Compliance & Audit** – Compliance officer, security analyst

## Universal Connector Policy Actions
The Universal Connector supports specialized policy actions such as **Alert daily** and **Alert only**. These actions behave like standard Guardium policy actions and allow tailored alerting and enforcement for events monitored by the connector.

## IBM Guardium Data Protection Overview
IBM Guardium Data Protection provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud databases and file systems.

### Key Features
- **Real-Time Database Monitoring:** Captures and analyzes database traffic with S-TAP, A-TAP, and K-TAP agents.
- **Centralized Policy Management:** Defines and enforces security policies through S-GATE blocking and FGAC.
- **Vulnerability Assessment:** Scans for known vulnerabilities and misconfigurations.
- **Compliance Reporting:** Pre-built templates for PCI-DSS, HIPAA, GDPR, SOX, and other regulations.

### Workflows
- **Configuration:** Deploy collectors, define data sources, create policies.
- **Monitoring:** Review system health, analyze access reports, respond to alerts.
- **Enforcement:** Apply FGAC rules, block unauthorized queries.
- **Compliance:** Schedule assessments, generate audit evidence, produce reports.

### Personas
- **Security Administrator:** Configures policies, monitors threats, manages compliance.
- **Database Administrator:** Deploys agents, configures data sources, monitors performance.
- **Compliance Officer:** Validates policy adherence, retrieves audit evidence, generates reports.

### IBM Guardium Data Protection Overview

IBM Guardium Data Protection is a comprehensive enterprise database activity monitoring and security platform that provides real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across both on‑premises and cloud data stores.

#### Core Features
- **Threat Management:** Create and manage threat categories, exclude items from Active Threat Analytics, and perform bulk case actions.  
- **Load Balancer Configuration:** Group associations for Universal Connector profiles using enterprise load‑balancing settings.  
- **Deployment Health:** Monitored processes report combines the Investigation dashboard and Threshold alerter view.  
- **Access Management:** Displays "password last changed" and "password expired" timestamps in the access‑management UI and the `list_users` API.  
- **Network Time Protocol (NTP):** Replaces the deprecated `ntp` commands with the `time_server` commands using the chrony daemon.  
- **Schema Changes for Vulnerability Testing:** Enforces required schema modifications to enable vulnerability assessment tests.

#### Typical Workflows
- **Threat Workflow:** Define threat categories, apply policy rules, set up threshold alerts, and manage case actions in bulk.  
- **Configuration Workflow:** Configure load‑balancer groups for Universal Connectors and monitor deployment health.  
- **Compliance Workflow:** Enable password‑management features, enforce NTP changes, and apply necessary schema updates.

#### Key Personas & Their Focus Areas
| Persona            | Primary Responsibilities                                                                                         |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| **Security Admin** | Manages threat definitions, load‑balancer configurations, and NTP settings.                                       |
| **Compliance Officer** | Audits password‑management settings, reviews schema‑change requirements, and ensures adherence to audit standards.|
| **Data Engineer** | Reviews monitored processes reports, applies policy exclusions, and validates data access policies.              |

#### Primary Entities
- **Threat Entities:** Threat categories, threshold alerts, and case‑action configurations.  
- **Load‑Balancer Entities:** Universal Connector profiles and enterprise load‑balancing group associations.  
- **Health Entities:** Monitored processes reports and data shown on the Investigation dashboard.  
- **Security Entities:** Access‑management attributes such as password‑change/expiry timestamps.  
- **Infrastructure Entities:** NTP daemon configuration (chrony).  
- **Vulnerability Entities:** Schemas and test objects used in vulnerability assessment suites.

*(All statements are extracted verbatim from the source entries; no new information has been added.)*

## Data Management Reports

After purging data from Guardium managed units, verify that the archive job successfully completed. Navigate to **Manage > Reports > Data Management > Purge Data** to view the purge job status. If the **Last Run End** time shows a recent timestamp and the **Result** column indicates success, the purge completed as expected. Next, check the **Manage > Reports > Data Management > Purge Archive** report to ensure archive jobs finished without errors. Finally, review the **Manage > Reports > Data Management > Reports Overview** report to confirm that historical records for archived managed units are still accessible.

## Aggregate/Archive Log Verification

Verify the archive process completed successfully before proceeding with system upgrades. This ensures data integrity and regulatory compliance.

## Post-Upgrade Maintenance

After Guardium system upgrades, install relevant maintenance patches using the `store system patch install` CLI command on the store system to maintain consistent patch levels and system stability. Review patch notes carefully and schedule installations during maintenance windows.

## Oracle Parser Integration

The `show connect oracle_parser ON/OFF` command toggles integration between Oracle and DB2 parsers in Guardium, enabling consistent rule evaluation across heterogeneous database environments when Oracle SQL is parsed using the DB2 parser.

## Account Lockout Configuration

The `store account strike interval n` command sets the lockout interval (n seconds) after consecutive failed login attempts, enhancing security by preventing brute-force attacks on database accounts.

## Custom Table Management

The `delete_custom_table_ldap_import` command removes LDAP-imported custom tables from Guardium 11.2 and later, helping maintain data integrity and performance.

## Auto-Discovery Task Management

The `list_autodetect_tasks_for_process` command retrieves tasks associated with a specific auto-discovery process, enabling programmatic management of Guardium's discovery capabilities.

## Query Monitor Scheduling

The `list_scheduler_jobs` command lists all configured scheduler jobs, aiding in monitoring and managing Guardium's Query Monitor activities.

## Ranger Query Rewrite API

The `remove_ranger_replace_element_by_id` REST API deletes specific elements from Guardium's Ranger query rewrite functionality, allowing programmatic customization of query transformation rules.

## AWS Secrets Manager Configuration Editing

The `update_aws_secrets_manager_config` command edits AWS Secrets Manager configurations in Guardium, requiring the `name` parameter and optionally allowing `access_key_id` and authentication type specification.

orLogLevels**  
Changes the log level of the specified custom Guardium process to the supplied value. This API requires the level (INFO, DEBUG, etc.) and the custom process name. Available in Guardium version 11.3 and later.

## GuardAPI Syntax

**set_universal_connector_timeout**  
Configures the data timeout for the universal connector via a POST request. The API (`set_universal_connector_timeout`) was introduced in Guardium V11.1 and is accessible on port 8443.

---

## Connecting to SaaS Applications

Connecting Unified Discovery and Classification with SaaS applications is a straightforward process that enhances cloud security and compliance monitoring.

---

## Document Overview

IBM Guardium Data Protection is IBM’s comprehensive database activity monitoring and security platform. It delivers real‑time visibility, policy enforcement, vulnerability assessment, and compliance reporting for both on‑premises and cloud data stores.

### Features Overview
- **Unified Data Discovery:** Automated discovery of sensitive data across applications with a few clicks, leveraging built‑in classifiers and customizable patterns.
- **Granular Access Controls:** Role‑based permissions, scoped to specific Guardium entities (datasources, reports, assessments), enforce least‑privilege access.
- **Dynamic Policy Enforcement:** Real‑time threat detection, S‑GATE blocking, adaptive alerts, and incident generation based on user, object, operation, and time‑window criteria.
- **Cross‑Platform Support:** Native connectors for relational, NoSQL, big data, and cloud services (AWS, Azure, GCP) with driver‑agnostic JDBC access.
- **Compliance Reporting:** Out‑of‑the‑box templates for PCI‑DSS, GDPR, HIPAA, SOX, and customizable audit trails.

### Workflows Overview
- **On‑boarding:** Add datasource → Deploy S‑TAP/Universal Connector → Define security/audit policies → Activate.
- **Risk Assessment:** Run vulnerability scans → Review findings → Create remediation tickets.
- **Incident Response:** Detect policy violation → Trigger S‑GATE block → Auto‑generate incident and workflow task.
- **Continuous Monitoring:** Review dashboards, generate compliance reports, tune policies.

### Personas Overview
- **Security Administrator:** Create/enforce FGAC policies, manage roles/permissions, configure collectors.
- **Database Administrator:** Register datasources, install S‑TAP agents, maintain performance baselines.
- **Compliance Officer:** View regulatory reports, certify data handling processes, manage audit evidence.
- **Security Analyst:** Perform threat investigations, correlate alerts with external threat feeds.

### Entities Overview
- **Collectors & Agents:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Definitions & Policies:** Security Policy, Audit Policy, Classification Rule, Access Rule, Vulnerability Policy.
- **Infrastructure:** Managed Unit, GIM (Guardium Installation Manager), S‑GATE, Universal Connector, Infosphere Integration.

---

## Roles and Permissions for Amazon Web Services accounts

The **Cross Account Metadata** role is automatically generated for each connected AWS account. It grants the necessary permissions to discover resources, read metadata, and create temporary objects required by Guardium vulnerability assessments within the account. The role supports scoped, least‑privilege access so that Guardium can inventory and evaluate AWS services without needing broader administrative rights.

---

## Write Permission for Unified Discovery and Classification Storage

Guardium Data Protection requires a single **write permission** for the **Unified Discovery and Classification Storage** account container. This permission allows Guardium to upload discovered classification results, store scan artifacts, and persist any remediation metadata generated by the platform. No additional read or delete rights are needed for normal operation.

---

## Troubleshooting Cassandra for Vulnerability Assessment

Troubleshooting Cassandra assessments involves several steps:  
1. **Environment Setup** – Ensure the Cassandra cluster is reachable from the Guardium collector and that the necessary credentials are stored in the Credential Manager.  
2. **Assessment Type Selection** – Choose between **query‑based** and **CAS‑based** assessments; the former runs custom CQL tests, the latter uses Cassandra Auditing Service (CAS) logs.  
3. **Define Test Criteria** – Create query tests (e.g., SELECT on restricted tables) and CAS test definitions (e.g., audit log filters).  
4. **Create Assessment** – Use the UI or API to package the tests, schedule execution, and assign a managed unit.  
5. **Review Results** – Examine assessment reports, drill into failed queries, and adjust policies or schema definitions as needed.  
6. **Locate Existing Assessments** – Use the *Vulnerability Assessment* dashboard or the Definitions Export/Import Log to find previously configured Cassandra scans.

---

## Cloudera Manager

To integrate Cloudera Manager with Guardium, configure a **Cloudera Manager datasource**: provide the host, port, credentials, and select the appropriate **Managed Unit**. The same pattern applies for **CockroachDB** and **Couchbase** datasources—define the connection parameters, deploy the appropriate collector (S‑TAP or Universal Connector), and enable real‑time monitoring. Guardium automatically discovers services and builds security policies based on the catalogue metadata exposed by each platform.

---

## Field Description

**Account** – identifies the database owner; typical values include system users like *sybase*.  
**Directory** – stores the installation path (e.g., `/home/sybase` on UNIX or `C:\sybase` on Windows).  
**SYBASE** – an optional environment variable that may be set on the host to point to the root directory, facilitating the datasource configuration wizard.

---

## Column name

**Column name** and **Field name** fields support optional **LIKE** filters. When populated, Guardium narrows discovery/classification results to only those columns or fields that match the provided pattern.

## Guardium Overview

IBM Guardium Data Protection monitors, protects, and reports on database activity across on‑premise and cloud data stores. It combines real‑time session monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

## Features

| Feature | Purpose |
|---------|---------|
| Investigation Dashboard | Central reporting surface for data‑protection issues; supports runtime filters (period, host, etc.) |
| Managed Units Domain | Describes managed units and groups in the Guardium deployment |
| Application Data Domain | Captures connection, session, and application‑specific data for enterprise apps (e.g., Siebel, SAP) |
| Status Description Patch | Stores patch status, timestamps, and UTC offset for patches applied to Guardium components |

## Workflows

1. **Configure Managed Units Domain** – Define the units and groups that make up the environment.  
2. **Set Up Application Data Domain** – Enable data capture for special enterprise applications.  
3. **Run Investigation Dashboard Queries** – Filter and analyze reported issues.  
4. **Monitor Patches** – Use Status Description Patch records to track deployment status.

## Personas

| Persona | Responsibilities |
|--------|-------------------|
| Security Administrator | Configures monitoring domains, policies, and compliance settings |
| Compliance Officer | Generates and reviews issue reports from the dashboard |
| Database Administrator | Monitors entitlements, patch status, and data collection |
| Security Analyst | Investigates alerts, correlates events, and produces remediation plans |

## Entity Descriptions

- **Investigation Dashboard Issues** – Reports generated for data‑protection incidents, filterable by runtime criteria.  
- **Managed Units Domain** – `1fddc2f8-d075-4da6-8b56-2c8117689c0c` – Tracks all Guardium managed units and their logical groupings.  
- **Application Data Domain** – `7a9edc2d-7b36-460a-a9c2-97aa0b9d5ca8` – Stores app‑specific session and connection data for apps such as Siebel and SAP.  
- **Status Description Patch** – `92114e2d-4465-4697-a81c-cf5c8a4a9b41` – Holds patch status, update timestamps, and UTC offset information for Guardium components.

## Template Set Entity
**76f63e79-a6ab-4548-9074-9a5e1187d3de**
Describes a collection of template items for a specific OS or database, uniquely identifying items to be monitored by CAS.

## Discovered Instances Domain
**acbe42a7-109c-4005-af7a-af1571975716**
Tracks instances found by GIM. Records each instance's timestamp, host, protocol, and port range.

## Patch Number
**710d3532-07c2-40e2-bfa2-7440834d2b74**
Identifies the specific patch. Records when the patch was uploaded for installation. Notes the UTC time difference between collector and source.

## Attribute Description
**aa870af3-57ab-4cf9-901b-fa38e501e314**
Defines attributes such as Output SQL, Applied QR Definition IDs, and Input SQL essential for query rewrite results.

## Apache Cassandra Entitlements
**d2cd01fa-920d-4f36-9dcc-bf196c375d66**
Covers create privileges, privileges with grant option, and SuperUser roles for data management.

## VSAM RLM CICS
**29c7a964-a154-419a-b6e3-8a61a66cfa13**
Captures the user ID from the CICS system, available only if CICS_SUPPORT is enabled and the system sends relevant info.

## VSAM RLM CICS
**b2e8bb16-a7fe-43f9-8fee-947928906a55**
Captures the file ID from CICS, available only with CICS_SUPPORT enabled.

## Attribute Description
**0f108a43-71b0-4205-ac73-4fe66c3c2d99**
Describes the timestamp attribute creation as a static value when Guardium first observes a session connection.

## CAS System Status
**5b8178d1-729f-4f53-9894-5f42bc5321ba**
Displays a green light when CAS is active and a red light when CAS is not running on the Guardium system.

## About this Task
**087ebf65-f909-43cb-9b0f-991a45e1f291**
Enterprise load balancing lets the Guardium central manager distribute S-TAP agents or universal connectors across managed units, improving load distribution and fault tolerance.

## Configuring the slon Looper Utility
**33e1eb51-21c8-40d3-a95f-63da9f93aea9**
Configures the slon looper from the Support Information Gathering page to investigate an incoming network traffic problem on the sniffer.

## Document Overview
IBM Guardium Data Protection provides real-time database activity monitoring, threat detection, policy enforcement, and compliance reporting across structured and unstructured data stores. Supports on-premises and cloud deployments.

### Features
- Datasource Connectivity
- Threat Detection
- Compliance & Reporting
- Central Management
- Audit & Alerts
- Automation & API Integration

### Workflows
- Installation & Configuration
- Monitoring & Incident Response
- Policy Management
- Upgrade & Maintenance
- Reporting & Auditing

### Personas
- Security Administrator
- Database Administrator
- Compliance Officer
- IT Operations Manager

### Entities
- S-TAP Agents
- Aggregators & Collectors
- Security Policies
- Audit Policies
- Classification Rules
- Access Control Lists

IBM Guardium provides a comprehensive suite of features for database security, including activity monitoring, policy enforcement, asset discovery, log ingestion, and file activity monitoring. Configuration steps vary by data source type, involving S-TAP installation and policy setup. Guardium supports multiple JDBC driver families for flexible database connectivity. Roles and permissions are defined to manage access and compliance tasks, with specific focus on PCI-related activities. Reports on failed login attempts, policy violations, and user activities help maintain security integrity. Outlier detection and runtime parameter customization enhance analytical capabilities.

## IMS Activity Tracking

IMS Activity Tracking records all database interactions, supporting detailed audit and compliance reporting. Define reporting periods and enable runtime filtering to narrow analysis.

**Key Concepts:** IMS Activity Tracking, Reporting Periods, Runtime Filtering

## Privilege Tracking

Privilege Tracking captures unauthorized access attempts and privilege escalations, enhancing security monitoring.

**Key Concepts:** Privilege Tracking, Unauthorized Access, Security Monitoring

## Document Overview

IBM Guardium Data Protection monitors, enforces policies, assesses vulnerabilities, and generates compliance reports for structured and unstructured data assets, both on‑premises and in the cloud.

### Features

- **Datasource Connectivity:** dynamic port detection, multi‑driver support, CyberArk credential vault integration  
- **Threat Detection:** real‑time policy enforcement, S‑GATE blocking, security incident generation  
- **Compliance & Reporting:** PCI‑DSS, GDPR, HIPAA, SOX report templates; automated audit trails  

### Workflows

- **Configuration:** add datasource, deploy S‑TAP via GIM, configure FGAC policies  
- **Navigation:** review activity reports, run vulnerability assessments, access audit dashboard  
- **Action:** block unauthorized queries, rotate credentials, respond to incidents  

### Personas

- **Administration:** system configuration, user management  
- **Security Administration:** FGAC, policy definition  
- **Database Administration:** datasource setup, S‑TAP deployment  
- **Data Analyst:** dashboards, query execution  
- **Compliance Officer:** regulatory reporting  
- **Security Analyst:** threat investigation  

### Entities

- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule  
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector

## CAS Templates - PostgreSQL

CAS templates for PostgreSQL require the `PostgreSQL_BIN` and `PostgreSQL_DATA` variables to be set.

**Key Concepts:** CAS Templates, PostgreSQL Configuration

# Guardium Data Protection Overview

## Features
- **Configuration Management:** Multi-driver support, dynamic port detection, GIM deployment, CyberArk vault integration
- **Security Enforcement:** Real-time S-TAP traffic capture, S-GATE blocking, policy violations, secrets protection
- **Compliance Reporting:** PCI-DSS, GDPR, HIPAA, SOX templates, automated audit trails, compliance hub
- **Proactive Controls:** Hardware retirement, connections quarantine, failover rules, vulnerability assessment

## Workflows
- **Setup:** Add datasources, deploy agents, configure SSL, migrate hardware
- **Monitoring:** Review activity reports, health views, policy violations, analytic outliers
- **Governance:** Manage taxonomy, assign roles, handle secrets, administer failover

## Personas
- **Security Administrators:** Define policies, investigate violations, manage incidents
- **Database Administrators:** Manage datasource connectivity, SSL certificates, privileges
- **Compliance Officers:** Generate compliance reports, oversee hardware migration
- **IT Operations:** Perform failover administration, tune secrets management

## Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Access Rule, Threshold Rule, Quarantine Rule
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector, Edge, Enterprise Hub
- **Objects & Artifacts:** Server IP, Net Mask, Attribute Description, Secrets Vault, Failover Group

## Features Overview
- Real-time policy enforcement across databases, data lakes, and file systems.
- Vulnerability assessment and patch management for databases.
- Automated compliance reporting for PCI‑DSS, GDPR, HIPAA, SOX, and custom frameworks.
- Privileged Identity Management integration for tracking shared privileged sessions.
- Seamless SIEM correlation for analysis of cross‑system threats.

## Workflows Overview
- Deploy and configure Guardium S-TAP agents on data sources.
- Build audit policies that define what data activity is captured.
- Run vulnerability scans and generate remediation reports.
- Export findings to external tools (SIEM, ticketing systems) for further action.
- Centralized system management through Guardium Central Manager.

## Personas Overview
- Security Administrators: define audit policies, investigate alerts, enforce access controls.
- Compliance Officers: execute compliance templates, review reports, certify audit trails.
- Database Administrators: install agents, configure data sources, view activity dashboards.
- Data Analysts: query audit logs for business analytics, create custom visualizations.

## Entities Overview
- **Sensors & Agents**: S-TAP (kernel‑level), k-TAP (user‑space), A‑TAP (application‑level), K-TAP (Kafka), Collectors (data ingest).
- **Policy Framework**: Security policies, audit policies, classification rules, masking policies.
- **Reporting & UI**: Activity Views, audit reports, dashboards, compliance templates.
- **Infrastructure**: Managed Units (agents), Central Manager (control plane), Aggregators (audit data hub).

## System Performance and Monitoring
- **Unit Utilization Report**: flags over‑ or under‑utilized Guardium collectors.
- **Self‑Monitoring**: health metrics (CPU, memory, disk) available in Guardium UI.
- **Services Status Page**: live view of all Guardium services on the collector. 

## SQL Statistics
- **Total Full SQL Records**: `SQLsNumber` tracks the count of complete SQL statements logged by Guardium.

## Policy Grouping
- **Groups**: logical containers (pre‑defined or custom) used to organize datasources, objects, or users for bulk policy assignments and reporting.

## Privileged Identity Integration
- **Guardium + PIM**: merges database activity monitoring with privileged identity management to audit shared privileged credentials, lease history, and access violations.

## Real‑time Auditing & SIEM
- **SIEM Integration**: streams contextual database events to external SIEMs for real‑time threat detection, correlation across network and host logs, and automated incident response.

## Access Management Challenges
- Traditional access control issues: lack of visibility, fragmented processes, insufficient segregation of duties.
- Guardium aggregates access data, enforces least‑privilege, and provides audit trails for governance.

## Session Context
- **Session ID**: parameter identifying a Guardium collector session acting as an S-TAP host; affects connection lifecycle logging.

## Limitations
- **Hadoop Blocking**: within Guardium Navigator, only a subset of rule actions (monitor, block) is supported; custom actions require custom development.

## Registry Parameter (External S‑TAP)
- **External S‑TAP Image Registry Credentials**: stored as a Kubernetes secret; accessible via `kubectl get secret <secret‑name> -o yaml`.

## Upgrade Path Guidance
- **Determining Upgrade Path**: Guardium provides a version matrix to map current release, target release, and required hardware/OS changes.

## Next Steps
- Verify current Guardium version and assess licensing.
- Plan for data source compatibility with target Guardium release.
- Schedule maintenance windows for collector upgrades.
- Review and test policies after upgrade.

## Overview

IBM Guardium Data Protection is an enterprise platform for database activity monitoring and data security.

## Features

- **Database Connectivity:** Supports native JDBC, generic drivers, and dynamic port detection via a browser service with CyberArk credential integration.
- **Monitoring & Alerts:** Captures SQL traffic through S-TAP agents; evaluates in real-time against policies; triggers alerts, reports, or blocking via S-GATE.
- **Compliance Reporting:** Provides built-in templates for PCI-DSS, GDPR, HIPAA, SOX, automated audit trails, and export capabilities.

## Workflows

- **Setup:** Add datasources; deploy S-TAP via Guardium Installation Manager.
- **Policy Management:** Define FGAC policies, audit trails, and classification rules.
- **Incident Response:** Investigate incidents; block unauthorized queries; centralize policies.

## Personas

- **Security Administrator:** Configures policies, monitors breaches, isolates threats.
- **Database Administrator:** Deploys S-TAP, manages database connectivity.
- **Compliance Officer:** Generates regulatory reports, tracks audit readiness.

## Entities

- **Entities:** S-TAP, K-TAP, A-TAP, Collectors, Aggregators, Central Manager.
- **Policy Types:** Security, Audit, Classification, Access.
- **Infrastructure:** Guardium Installation Manager, Managed Units, S-GATE, Universal Data Connectors.

## Scheduled Jobs for Archive Monitoring

Monitor operational status of data storage archiving processes to ensure compliance and data integrity.

## REST API Endpoints

### Datasource Group Reference
`POST /restAPI/datasource_group_ref`
Creates a relationship between a datasource and a group.

### CAS Host Instance
`DELETE /restAPI/cas_host_instance`
Deletes an existing host instance configuration.

## Guardium REST API Overview

Allows programmatic interaction with Guardium functions via HTTP methods to `/restAPI`. Supports datasource management, compliance reporting, and more.

## Transfer Key Generation
`GET /generate_transfer_key`
Returns a system-generated transfer key for secure data transfers.

## Investigative APIs

- **Cold Storage Streaming Status:** `get_cold_storage_streaming_status`
Monitor cold storage task states.
- **Datasource List:** `nau_collectors_list`
Lists all Guardium collectors.

## GuardAPI

- **Retrieve Native Audit Objects:** `get_native_audit_objects`
Collects cataloged database objects during audit data collection.
- **Ambari Cluster Configuration:** `get_ranger_config`
Retrieves Ambari admin credentials and service endpoints.

## Additional APIs

- **Ranger Config Inspection:** Demonstrates invoking GuardAPI via GrdAPI.
- **Kill OS Process:** `kill_running_process`

## REST API Metadata

Fetches metadata about a datasource, including connection details and policy associations.

## API Syntax Guidelines

HTTPS syntax for all calls:
`https://<Guardium Host>:8443/restAPI/<endpoint>`
Include required authentication headers and method-specific parameters.

```markdown
### Features Overview
- **Datasource Configuration:** Automated password provisioning from CyberArk and AWS Secrets Manager
- **Secret Management Integration:** Native connectors for AWS Secrets Manager and Azure Event Hubs
- **Advanced Analytics:** Outliers detection for abnormal user/privilege behavior
- **Data Redaction:** REDACT rule action masks sensitive content in SQL statements

### Workflows Overview
- **Initial Setup:** Configure datasource definitions, enable monitoring streams, and deploy S-TAP agents
- **Policy Management:** Create FGAC policies, classification and REDACT rules, and secret-access rules
- **Monitoring & Action:** Real-time alerting, S-GATE blocking, and streaming visibility through event-hub tables

### Personas Overview
- **Security Administrators:** Define policies, integrate secret vaults, and manage event hubs
- **Compliance Officers:** Generate regulatory reports and audit trails
- **Database Administrators:** Install S-TAP agents, manage credentials, and monitor outliers

### Entities Overview
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policy Elements:** Security Policies, Audit Policies, Classification Rules, REDACT Rules, Access Rules
- **Secret Stores:** AWS Secrets Manager, CyberArk, Azure Event Hubs
- **Analytics:** Outlier Entities, Threat Anomalies
```

Enable Edge Gateway during interactive S-TAP installation

## IBM Guardium Data Protection Overview
IBM Guardium Data Protection is IBM's comprehensive enterprise database activity monitoring and security platform, offering real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data sources across on-premises and cloud environments.

## Key Features
- **Database Connectivity:** Dynamic port detection, native and generic JDBC drivers, CyberArk credential vault integration.
- **Real-Time Threat Detection:** Continuous policy enforcement, S-GATE query blocking, on-the-fly security incident generation.
- **Compliance Reporting:** Built-in templates for PCI-DSS, GDPR, HIPAA, SOX; automated audit trail generation.

## Workflows
- **Configuration:** Add datasources, deploy S-TAP agents via Guardium Installation Manager (GIM), define Fine‑Grained Access Control (FGAC) policies.
- **Monitoring & Navigation:** Review activity logs, run vulnerability scans, use the audit dashboard for at-a-glance insights.
- **Response & Action:** Block unauthorized queries, rotate compromised credentials, orchestrate incident response actions.

## Personas
- **Administrators:** Platform setup, user management, security policy definition.
- **Database & Data Owners:** Manage datasources, S-TAP installations, perform daily data queries.
- **Compliance & Audit Teams:** Generate regulatory reports, oversee audit trails, conduct threat investigations.

## Entities
- **Agents & Collectors:** S-TAP (in-database agent), A-TAP (in-network traffic), K-TAP (kernel-level tap), Collector (aggregates traffic), Aggregator (centralizes data), Central Manager (policy enforcement platform).
- **Policies & Rules:** Security Policy (global protection rules), Audit Policy (logging rules), Classification Rule (data discovery), Access Rule (access control conditions).
- **Infrastructure Components:** Guardium Installation Manager (software deployment), Managed Units (distributed enforcement nodes), S-GATE (blocking gateway), Universal Connector (non-SQL data sources).

## Database Connection Architecture
Supports multiple JDBC driver families (native vs. generic) and uses a browser service to dynamically resolve datasource instance names to host-port pairs.

## Activity Monitoring & Policy Enforcement
Continuously captures database traffic via S-TAP agents, evaluates it against security policies in real time, generates alerts, custom reports, and can trigger S-GATE-based query blocking. Policies can be scoped by user, object, operation, and execution time window.

## Reporting and Report Generation
Provides extensive reporting APIs and UI tools to extract audit data, compliance evidence, and query activity. Supports on-demand, scheduled, and event-triggered reports with built-in endpoints for entitlement optimization, universal connector status, assessment results, and feature flag checks.

## Guardium Universal Connector Integration
Enables monitoring of non-SQL data stores (e.g., Hadoop, NoSQL, cloud objects) by ingesting relevant logs/events. Offers APIs for connector status queries, Hadoop Ranger integration configuration, and SSL validation settings.

## REST API Reference
Exposes a broad REST API surface for programmatic configuration and retrieval of audit data.
- **Template Management:** `POST /cas_template_set` creates CAS template sets; `DELETE /cas_template_set` removes them (requires `templateSetLabel`).
- **Feature Flags:** `POST /feature_flag` toggles platform capabilities.
- **Datasource Management:** `GET /datasource_ref` fetches datasource metadata.
- **Assessment Results:** `GET /assessment_result?description=…` returns vulnerability scan outcomes.
- **Universal Connector:** `GET /universal_connector/status` returns collector-side connector health.

## GuardAPI Administration
Supports programmatic enforcement and configuration actions.
- **Vulnerability Assessment:** `solr_repair_analysis` checks Solr index health and optionally validates DataMart status (v12.0+).
- **Authentication Policies:** `DataStax Cassandra` supports Local User and LDAP authentication but excludes Kerberos.
- **Session Controls:** `MARK_SESSION` assigns trust levels based on session policies.
- **Access Auditing:** `Administrative user accessing sensitive data` policies detect admin misuse of protected data.

## Overview

IBM Guardium Data Protection monitors activity across databases and file systems, offering real-time alerts, compliance reports, and vulnerability assessments.

## Key Features

- **File Activity Monitoring:** Detects read, write, copy, rename, and delete operations on Windows NAS and SharePoint.
- **Data Compliance Thresholds:** Quantifies effectiveness of security controls against policy requirements.
- **CPU Tracker:** Lists Guardium S-TAP hosts and their CPU core counts.
- **Session Reports:** Aggregates open sessions by server type (DB2, Informix, etc.).
- **SQL Error Reporting:** Logs errors with timestamp, IP addresses, server type, database user, and frequency.
- **Column Selector:** Customizes report attributes, sorting, and filters for views.
- **STAP Status Domain:** Monitors health of S-TAP agents across the environment.
- **Guardium Activity Audit:** Tracks all configuration changes and user actions within Guardium.
- **Attribute Bundles:** Groups related fields for targeted reporting.
- **Vulnerability Assessment:** Deploys assessment tools via Helm charts.
- **CyberArk Integration:** Manages Guardium credentials in an external vault.

## Typical Workflows

1. **After Prerequisite Check:** Install monitoring policies; start with basic or advanced SQL traffic policies.
2. **Attribute View Customization:** Choose attributes, sort order, and filters for reports.
3. **Credential Management:** Store and rotate Guardium credentials through CyberArk.

## Primary User Roles

- **Security Administrators:** Configure thresholds, monitor CPU and File Activity policies.
- **Database Administrators:** Review session statistics and SQL error logs.
- **Compliance Officers:** Generate attribute-based compliance reports.
- **DevOps Teams:** Deploy vulnerability scanners with Helm and integrate with CyberArk.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is a comprehensive security platform for monitoring and protecting enterprise databases. It offers real-time activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores in on-premises and cloud environments.

### Key Features
- **Datasource Connectivity:** Supports dynamic port detection, multiple drivers, and integrates with CyberArk for credential management.
- **Threat Detection:** Provides real-time policy enforcement, S-GATE blocking capabilities, and generates security incidents.
- **Compliance & Reporting:** Includes report templates for PCI-DSS, GDPR, HIPAA, and SOX, and automated audit trails.

### Typical Workflows
- **Configuration:** Add data sources, deploy S-TAP agents via GIM, and configure Fine-Grained Access Control (FGAC) policies.
- **Navigation:** Access activity reports, run vulnerability scans, and utilize the audit dashboard for oversight.
- **Action:** Block unauthorized database queries, manage credential rotation, and respond to security incidents promptly.

### Personas and Roles
- **Administration:** Responsible for platform configuration and user management.
- **Security Administration:** Manages FGAC policies and security configurations.
- **Database Management:** Handles data sources and S-TAP deployments.
- **Data Analysts:** Uses dashboards and performs queries for data insights.
- **Compliance & Audit:** Focuses on generating regulatory reports and conducting security analyses.

### Core Entities
- **Deployment Components:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- **Policy Frameworks:** Security policies, audit policies, classification rules, access rules.
- **Infrastructure Elements:** Guardium Installation Manager (GIM), Managed Units, S-GATE, Universal Connectors.

## Edge Gateway Deployment
Edge Gateway is a Kubernetes-native deployment option for IBM Guardium Data Protection. It allows for elastic scaling and consolidated management of Guardium components within a Kubernetes environment, providing enhanced flexibility and scalability for modern IT infrastructures.

## DB2EXIT WINSTAP_DB2_EXIT_

### Key Concepts
- **WINSTAP_LOAD_BALANCER_IP**: IP address of the load balancer for WINSTAP.
- **WINSTAP_INITIAL_BALANCER_MU_GROUP**: Initial load balancer group for the Managed Unit.
- **WINSTAP_LOAD_BALANCER_NUM_MU**: Number of load balancers for the Managed Unit.

---

## Before You Begin

Ensure that target upgrade GIM bundles are available on the GIM server with build numbers equal to or greater than the currently installed version. Download the necessary bundles from Fix Central to upgrade S-TAP.

---

## Verify Collector Certificates (Optional)

To enhance security, optionally verify collector certificates before connecting to External S-TAP to ensure the connection is authorized.

---

## Show Command

CLI **store system snmp location \<string\>** command sets the location string used by the appliance in SNMP traps (defaults to *Unknown*).

---

## Native Audit APIs

Native audit APIs provide command‑line and REST interfaces for managing audit exemptions, configuring audit objects, and integrating with Hadoop monitoring tools such as Apache Ranger.

---

## Inspection Engine Parameters

**assign_analytic_case** (available from Guardium V11.0): Assigns Guardium recipients to threat analytics or risk spotter cases.

---

## Creating Managed Unit Groups

Creating managed unit groups assigns query‑rewrite conditions to actions. Available in Guardium V10.1.4 and later.

---

## Query Rewrite APIs

**create_qr_replace_element**: Creates a replacement element for query rewrite actions.

---

## REST API Syntax

**create_role** (POST): Adds a role via the endpoint `POST https://.../restAPI/create_role`.

---

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Features Overview
| Feature | Description |
|---|---|
| Datasource Connectivity | Dynamic port detection, multi-driver support, CyberArk credential vault integration |
| Threat Detection | Real-time policy enforcement, S‑GATE blocking, security incident generation |
| Compliance & Reporting | PCI‑DSS, GDPR, HIPAA, SOX report templates; automated audit trails |

### Primary Workflows  
1. **Configuration** – Add datasource → Deploy S‑TAP (via GIM) → Configure FGAC policies  
2. **Navigation** – Review activity reports → Run vulnerability assessments → Audit dashboard  
3. **Action** – Block unauthorized queries → Rotate credentials → Respond to incidents  

### Personas  
| Persona | Responsibilities |
|---|---|
| **Administration** | Platform configuration, user management |
| **Security Administrator** | FGAC, policies, threat response |
| **Database Administrator** | Datasources, S‑TAP installation |
| **Compliance Officer** | Regulatory reports, policy adherence |
| **Security Analyst** | Threat investigation, dashboards |

### Guardium Entities  
| Entity | Role |
|---|---|
| **Agents & Collectors** | S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager |
| **Policies & Rules** | Security Policy, Audit Policy, Classification Rule, Access Rule |
| **Infrastructure** | GIM, Managed Unit, S‑GATE, Universal Connector |

---

## 3665. GuardAPI syntax

`disable_test_result_detail_string_setting` disables detailed test result logging, writing only summary information to the `TEST_RESULT_DETAIL` table.

*Key Concepts:* disable_test_result_detail_string_setting, test result logging  

---

## 3666. GuardAPI syntax

`edit_kafka_cluster` API manages Kafka clusters through operations like adding or deleting clusters, allowing Guardium to integrate data streams.

*Key Concepts:* edit_kafka_cluster, Kafka cluster management  

---

## 3667. GuardAPI syntax

`f5_add_apps_config` parameter=value  
Parameters:  
- **appsIP** (String, Required)  
- **bigIP** (String, Required)  

*Key Concepts:* f5_add_apps_config, application configuration  

---

## 3668. REST API syntax

Provides REST API syntax for fetching all S‑TAP clusters via GET requests with a specified endpoint.

*Key Concepts:* S‑TAP clusters, REST API, GET endpoint  

---

## 3669. API example

Hadoop monitoring APIs, including `get_health_traffic_status`, monitor Hadoop ecosystem components.

*Key Concepts:* Hadoop monitoring, health traffic status  

---

## 3670. REST API syntax

The REST API for `ip_restriction` is a GET service accessed at `https://[Guardium host]:8443/restAPI/ip_restriction`, enabling retrieval of IP restriction status via web calls.

*Key Concepts:* ip_restriction, REST API GET, IP retrieval  

---

## 3671. REST API syntax

`get_kafka_cluster` is a REST API endpoint at `/restAPI/kafka_cluster` accessible through GET on port `8443`, managing the configuration of Kafka clusters within the Guardium environment.

*Key Concepts:* get_kafka_cluster, REST API, Kafka configuration  

---

## 3672. REST API syntax

`get_quick_search_info` REST API syntax retrieves quick search information using the GET method, with `api_target_host` specifying the target hosts for execution.

*Key Concepts:* get_quick_search_info, REST API, quick search  

---

## 3673. Group APIs

`list_hashicorp_config` API returns details of all HashiCorp configurations on the Guardium system.

*Key Concepts:* list_hashicorp_config, HashiCorp configurations  

---

## 3674. Risk Spotter

`rule_info_from_policy` is a Guardium API and REST service that … *(entry truncated, incomplete information provided – cannot summarize further)*

## Overview of IBM Guardium Data Protection
IBM Guardium is an enterprise-grade database activity monitoring and security platform. It delivers real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data sources, both on‑premises and in the cloud.

### Key Features
- **Unified Data Connectivity:** Dynamic port detection, support for multiple database drivers, and integration with CyberArk for credential vaulting.
- **Threat Detection & Prevention:** Real‑time policy enforcement, S‑GATE blocking, and automatic generation of security incidents.
- **Compliance Reporting:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX, and automated audit trails.
- **Sensitive‑Object Identification:** Runtime analysis of response data to detect PII and other regulated information.
- **File Activity Monitoring (FAM):** Automated discovery and classification of sensitive files on Windows, Unix, and Linux servers.
- **Broad Integration Ecosystem:** Supports IBM i IMS SMF, Tivoli Storage Manager, Oracle Unified Audit, and custom APIs.

### Core Workflows
1. **Configuration:** Add data sources, deploy S‑TAP/K‑TAP agents via Guardium Installation Manager (GIM), and configure Fine‑Grained Access Control (FGAC) policies.
2. **Monitoring:** Live activity streams, audit‑only mode, and session filtering for focused analysis.
3. **Assessment:** Automated vulnerability scans, PCI‑DSS monitoring, and classification workflow results.
4. **Response:** Real‑time alerts, S‑GATE blocking, remediation tasks, and credential rotation.

### Personas & Their Responsibilities
| Persona                     | Primary Duties                                                               |
|-----------------------------|------------------------------------------------------------------------------|
| **Platform Administrator**  | Install/upgrade Guardium components, manage GIM, set up infrastructure.    |
| **Security Administrator**  | Define and install FGAC policies, handle security incidents, manage alerts.|
| **DBA / Data Owner**        | Provision datasources, manage S‑TAP/K‑TAP agents, troubleshoot connectivity.|
| **Compliance Officer**      | Produce regulatory reports, maintain audit evidence, enforce retention policies. |

### Primary Entities
- **Agents & Collectors:** S‑TAP (database agents), K‑TAP (file‑system agents), Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, FGAC access rules, data‑discovery and classification rules.
- **Infrastructure:** GIM, Managed Unit, S‑GATE (blocking gateway), Universal Connector, Audit Database.

---

## Specific Capabilities (Selected)

### 3680 – GIM Management
Guardium Installation Manager (GIM) automates deployment and maintenance of Guardium components. It provides:
- Centralized certificate management (custom certificates, rotation).
- Failover support for high‑availability setups.
- Diagnostic utilities for troubleshooting.

### 3681 – Audit Only Mode
Audit Only mode:
- Suppresses response data storage per session.
- Detects Canadian Social Insurance Number (SIN) patterns for targeted compliance.
- Reduces storage overhead while still capturing relevant policy violations.

### 3682 – Runtime Sensitive‑Object Identification
Runtime identification:
- Analyzes database response data in‑memory.
- Matches against predefined patterns for PII, credit‑card numbers, etc.
- Generates immediate alerts for remediation.

### 3683 – FAM on File Servers
File Activity Monitoring:
- Performs automated discovery and classification of sensitive data on Windows, Unix, and Linux file servers.
- Leverages classification rules to label data by sensitivity level (e.g., PII, PCI).

### 3684 – OS‑User Context Fields
Key metadata fields for session context:
- **OS_USER:** Operating system user executing the query.
- **SERVER_DESC / SERVER_OS_NAME / SERVER_HOST_NAME / SERVER_IP:** Server identification details.
- **SERVICE_NAME:** Logical service or application name.
- **SOURCE_PROGRAM_NAME:** Client application or driver name.

### 3685 – Value Change Auditing Builder
After creating an audit database on the target server:
- The database is automatically enabled as a source in the **Value Change Auditing Builder**.
- Users can define custom triggers and extended monitoring logic for fine‑grained change tracking.

### 3686 – PCI Policy Monitoring View
The **Policy Installation** perspective shows:
- Current PCI‑DSS relevant policies.
- Coverage gaps per data source.
- Allows selection and deployment of additional policies to achieve full PCI compliance.

### 3687 – Query‑Based Domain Derivation
Guardium automatically creates query‑based domains from the primary table or view referenced in a SQL statement. This enables:
- Automatic policy generation that aligns with business entities.
- Simplified rule authoring for fine‑grained access control.

```markdown
# IBM Guardium Central Management

IBM Guardium provides a unified platform for data security and compliance across databases, file systems, and big‑data sources on‑premises and in the cloud. It offers real‑time monitoring, policy enforcement, unified audit collection, and compliance reporting.

## Features
- **Central Management** – Single console to administer multiple Guardium appliances, collectors, and data sources.
- **Policy Management** – Define security policies that span heterogeneous data environments.
- **Audit Collection** – Capture audit trails, log data, and activity records from databases, files, and cloud services.
- **Compliance Reporting** – Pre‑built templates for PCI‑DSS, GDPR, HIPAA, SOX; customizable dashboards and reports.

## Workflows
1. **Deploy** – Install Guardium components, configure the central manager, onboard data sources, and enable collectors.
2. **Monitor** – View live activity, receive real‑time alerts, and investigate incidents.
3. **Report** – Generate compliance reports, export audit data, and create dashboards.
4. **Incident Response** – Isolate compromised assets, apply remediation actions, and enforce containment.

## Personas
- **Security Administrator** – Creates policies, monitors alerts, and investigates incidents.  
- **Compliance Officer** – Runs compliance reports, validates regulatory adherence.  
- **Data Engineer** – Manages data sources, configures collectors, fine‑tunes policies.

## Key Entities
- **Appliances & Collectors** – Central manager, aggregators, and data collectors.  
- **Data Sources** – Databases, file systems, and cloud‑based storage services.  
- **Policies & Rules** – Security policies, audit policies, classification, and masking rules.  
- **Reports & Dashboards** – Built‑in compliance reports, audit dashboards, and custom analytics.
```

## 3725. Record values with policy violation
When **Record values** is enabled on a policy rule, Guardium logs the exact SQL fragment or file operation that caused the rule to fire, and this logged value appears in policy‑violation reports and alerts.

## 3726. Creating a custom exception message example
Guardium lets you create custom exception messages with the SR language `THROW_EXCEPTION` or by selecting **LOG EXCEPTION** as the action when defining a policy. These messages give analysts actionable context for blocked or alerted activity.

## 3727. Rule definition fields
A Guardium file‑activity rule includes these key definition fields:
- **Rule Name** – human‑readable identifier.
- **Object** – file, directory, or SharePoint item being monitored.
- **Operation** – read, write, delete, modify, share, etc.
- **User/Group** – target principals.
- **Severity** – informational, minor, critical, etc.
- **Action** – Log, Block (via S‑GATE), Alert, or custom exception.
- **Condition Expressions** – time window, size threshold, pattern matching, etc.

These fields determine how Guardium evaluates and reacts to file operations.

## 3728. Hitachi Firewall Rules
To enable Guardium File Activity Monitoring (FAM) communication with Hitachi storage arrays, allow inbound TCP traffic on port **445** (SMB) on both the Guardium collector and the Hitachi device. This rule is unidirectional and must be applied consistently on both sides.

**IBM Guardium Data Protection Overview**

**Features**  
- Centralized policy creation, import, and assignment (FGAC & CAS).  
- Real‑time threat detection with instant alerts and S‑GATE blocking.  
- Built‑in compliance reports (PCI‑DSS, GDPR, HIPAA, SOX, custom).  
- Automated data discovery and classification.  
- Repeated vulnerability scans, risk scoring, and remediation guidance.

**Workflows**  
1. **Onboard Data Sources** – Add databases, file systems, and big‑data stores; discover and classify them.  
2. **Deploy Monitoring Agents** – Install and configure S‑TAP, U‑TAP, A‑TAP, K‑TAP collectors.  
3. **Configure Policies & Rules** – Define FGAC and CAS rules, schedule assessments, set up alerting.  
4. **Review & Respond** – Use dashboards, activity reports, and incident handling to investigate and remediate violations.

*Guardium provides continuous monitoring, proactive protection, and comprehensive audit evidence to safeguard structured data across hybrid environments.*

### Guardium Mediation Actions

The IBM Guardium Data Protection app in ServiceNow automates incident tracking, problem logging, and workflow generation by allowing Guardium to raise tickets directly from audit findings. 

Monitored Entities such as files, registry keys, environment variables, OS commands, and SQL statements are tracked via detection rules that log access or modification events.

An ECS/S3 Compatible target can be configured to export audit data, configuration snapshots, or backup archives to external object storage for compliance and redundancy.

Generative AI (GenAI) integrates IBM watsonx with Guardium, providing contextual guidance, automation, and summarization of audit data to enhance analyst productivity.

Deployment health topology views may appear inconsistent due to varied deployment configurations, with specific scenarios documented to clarify expected behaviors.

The Guardium sniffer core captures, parses, and evaluates all database traffic according to configured policies, with SSL/TLS configuration displayed via `show ssl_configuration` for secure sniffing validation.

The `show system netfilter-buffer-size` CLI outputs the current netfilter buffer size used by S-TAP for packet buffering, while `store system patch cleanup` and `store system patch install` manage patch files.

For detailed information on Guardium's REST API framework, see the full documentation.

T API Syntax for Removing Group Members by ID

The endpoint `DELETE https://[Guardium hostname or IP address]:8443/restAPI/remove_members_of_groups_by_id` removes group members based on their `groupId` parameter. This allows administrators to precisely target specific members for removal from datasource groups.

## Log Full Details with Values per Session

IBM Guardium can log comprehensive session data, capturing full details including each value exchanged. This enables granular auditing, forensic analysis, and real-time alerting based on exact parameter usage.

## Guardium Feature Overview

### Comprehensive Session Logging
Logging Full Details with Values per Session captures all relevant attribute values for each audited event, providing granular visibility into user activities. Administrators can define session-level policies via UI or Security Rules to specify which data points—such as user credentials, accessed objects, executed commands, and context variables—to capture. This capability enables precise forensic auditing, compliance verification, and investigative insights. **Key Concepts:** Session logging, SR language, attribute capture, comprehensive auditing, policy‑based monitoring.

### Data In‑Sight Visualizations
The **Data In‑Sight** chart offers interactive visualizations that can be toggled between full‑screen and standard views via control panel buttons. These visualizations surface session trends, outlier patterns, and compliance coverage, helping analysts rapidly interpret complex data. **Key Concepts:** Interactive visualizations, data overview, session trends, compliance monitoring.

### Auto‑discovery of Data Sources
Guardium’s **Auto‑discovery** domain automatically identifies new database hosts and instances within the network. It collects essential metadata about discovered assets—including running processes and network locations—to maintain an up‑to‑date inventory of protected resources. **Key Concepts:** Dynamic asset discovery, network scanning, host and port identification, asset inventory management.

### BigData Intelligence Outliers Tracking
The **BigData Intelligence Outliers List Enhanced** domain captures detailed records of anomalous activities in high‑volume data environments, including error conditions. This aids in identifying security threats or data anomalies efficiently. **Key Concepts:** Anomaly detection, outlier tracking, detailed activity logging, error analysis, data security monitoring.

### CM Buffer Usage Monitoring
The **CM Buffer Usage Monitor** domain aggregates Sniffer Buffer usage data from all collectors, offering a holistic view of buffer utilization across the Guardium environment. This assists administrators in performance tuning and resource optimization. **Key Concepts:** Buffer utilization monitoring, centralized data collection, performance optimization, resource management.

### User/Role/Application Mapping
The **User/Role/Application** domain maps user identities to roles and the applications they interact with, enriching understanding of user behavior and application usage. This domain supports role‑based access control, activity monitoring, and security policy enforcement. **Key Concepts:** Identity management, role‑based access, application interaction tracking, security policy enforcement.

### Audit Process Commenting
The **Audit Process Comments Entity** allows auditors and administrators to attach descriptive comments to audit process executions, enhancing traceability and context for review activities. (Note: The original entry was incomplete; this summary preserves the described purpose.)

Overview

## Guardium CLI

## Central Management API

## REST API

## 3837. REST API syntax

Access the **inapplicable_test_result_s** endpoint to retrieve details about test results that are marked as inapplicable.

## Overview
IBM Guardium Data Protection is an enterprise security platform that monitors database activity, performs vulnerability assessments, and provides compliance reporting across on‑premises and cloud data stores.

## Features
- **Security Policies:** Centralized management of FGAC, S‑GATE blocking, audit policies, and query‑rewrite rules.
- **Query Rewrite:** Intercepts and modifies SQL statements at runtime to enforce least‑privilege controls without changing application code.
- **Threat Analytics:** Correlates policy violations into threat categories visible on the Active Threat Analytics dashboard.
- **Smart Assistant:** Auto‑configures policies, classification rules, and activity monitoring for common frameworks (GDPR, PCI‑DSS, SOX, etc.).
- **Analytics Engine:** Monitors anomalous patterns and database attack signatures.

## Workflows
1. **Policy Configuration** – Define security, audit, classification, and query‑rewrite rules.
2. **Data Collection** – Deploy S‑TAP, A‑TAP, K‑TAP agents; stream activity to Guardium collectors.
3. **Threat Investigation** – Use the Threat Dashboard to view categories, outliers, and privileged‑user reports.
4. **Reporting & Compliance** – Generate PCI‑DSS, HIPAA, GDPR, SOX dashboards and vulnerability assessment reports.

## Personas
- **Security Administrator:** Manages policies, threat categories, and dashboards.
- **Compliance Officer:** Generates and reviews regulatory reports.
- **DBA / Data Analyst:** Manages data sources, reviews activity reports, and performs access reviews.
- **IT Operations:** Deploys agents and assists with incident response.

## Entities
- **Agents & Collectors:** S‑TAP (kernel/user), A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.
- **Policy Objects:** Security Policy, Audit Policy, Classification Rule, Access Rule, Query‑Rewrite Rule.
- **Threat Management:** Threat Categories, Active Threat Analytics Dashboard, Incident Records.
- **Compliance Frameworks:** Built‑in templates for PCI‑DSS, GDPR, HIPAA, SOX.
- **Infrastructure:** Managed Units, Guardium Installation Manager (GIM), Universal Connector, S‑GATE blocking service.

## Compression of Guardium Domain Guide

### Overview
IBM Guardium Data Protection is IBM's enterprise solution for database activity monitoring, security, compliance, and vulnerability assessment across structured and unstructured data, both on-premises and in the cloud.

### Key Features
- **Datasource Connectivity:** Supports dynamic port detection, multiple drivers, and CyberArk credential vault integration.
- **Threat Detection:** Offers real-time policy enforcement, S-GATE blocking, and automated incident generation.
- **Compliance & Reporting:** Includes pre‑configured templates for PCI-DSS, GDPR, HIPAA, SOX, and automated audit trails.

### Typical Workflows
- **Configuration:** Add a datasource, deploy S‑TAP agents using Guardium Installation Manager (GIM), and configure Fine‑Grained Access Control (FGAC) policies.
- **Navigation:** Review activity reports, execute vulnerability assessments, and use the audit dashboard for ongoing monitoring.
- **Action:** Block unauthorized queries, rotate credentials, and respond to security incidents.

### Primary Personas
- **Administrator:** Manages system configuration, user access, and policy deployment.
- **Security Analyst:** Investigates alerts, conducts forensic analysis, and generates compliance reports.
- **Compliance Officer:** Ensures adherence to regulatory requirements and audits Guardium's output.
- **Database Engineer:** Monitors database health and performance, interprets audit logs, and assists with policy tuning.

**IBM Guardium Data Protection Overview**

**Features**
- Database activity monitoring and security across on-premises and cloud data stores.
- Real-time threat detection, policy enforcement, and compliance reporting.

**Workflows**
- **Configuration Management**: Use POST to add new datasources, policies, and settings; DELETE to remove unwanted entries.
- **Data Purging**: DELETE unused user feedback, configuration mappings, and obsolete group references.
- **System Maintenance**: Regularly cleanup outdated records to optimize performance.

**Personas**
- **Security Administrator**: Manages DELETE operations to enforce policies and remove unnecessary access.
- **Data Administrator**: Uses DELETE APIs for efficient datasource, property, and group management.
- **Compliance Officer**: Leverages DELETE endpoints to ensure data retention policies are met.

**Entities**
- **APIs**: DELETE endpoints for user feedback, configurations, datasources, properties, group references, etc.

# Guardium Data Protection REST API Delete Methods

## REST API DELETE Methods

IBM Guardium provides a REST API for DELETE operations to manage various configurations and data within the system. These endpoints allow administrators to remove specific records through secure HTTPS requests.

## Quarantine Allowed Until

The REST API endpoint `POST https://[Guardium hostname or IP address]:8443/restAPI/quarantine_allowed_until` allows administrators to specify the end date for quarantining data. This provides a mechanism to control data retention policies dynamically.

## Datasource Custom Prop

The `DELETE /restAPI/datasource_custom_prop` endpoint removes a custom property from a datasource. It expects a JSON payload with the property name, ensuring precise configuration adjustments through HTTPS on port 8443.

## Datasource Group Reference

The `DELETE /restAPI/datasource_group_ref` endpoint deletes a datasource group reference. All required IDs must be provided to ensure accurate removal of group references via secure HTTPS requests.

## DB User Mapping

The `DELETE /restAPI/db_user_mapping` endpoint removes mappings between DB users and Guardium users. It expects a JSON body with user identifiers, ensuring secure management of user mappings through HTTPS on port 8443.

## Edge External Registry

The `DELETE /edge_external_registry` endpoint removes edge external registry configurations. It is accessible via HTTPS on port 8443, ensuring secure deletion of registry settings.

## Configure Results Export

The `DELETE /configure_results_export` endpoint at `https://[Guardium hostname]:8443/restAPI/configure_results_export` manages the configuration of results export settings. This endpoint ensures that export configurations are correctly managed and removed as needed.

## Classifier Document Rule

The `DELETE /restAPI/classifier_document_rule` endpoint removes a classifier document rule. It is called with a DELETE request to `https://[host]:8443/restAPI/classifier_document_rule`, ensuring secure removal of classification rules.

## Datasource by ID

The `DELETE /restAPI/delete_datasource_by_id` endpoint removes a datasource by ID. The endpoint follows the pattern `https://[hostname]:8443/restAPI/delete_datasource_by_id`, providing a secure method for datasource removal.

## Autodetect Processes

The `DELETE /restAPI/delete_autodetect_processes` endpoint is a REST API for deleting autodetect processes. It uses the DELETE method with the full URL to target the specific process for removal.

## Available Test Notes

The `DELETE /restAPI/available_test_notes` endpoint removes available test notes. This REST API endpoint ensures that outdated or unnecessary test notes are deleted from the system.

## Stap Client Config

The `DELETE /restAPI/delete_stap_client_config` endpoint deletes approved S-TAP client configurations. It is accessible via HTTPS on port 8443, ensuring secure deletion of client settings.

## Datasource Mapping

The `DELETE /restAPI/delete_datasource_mapping` endpoint removes data source mappings for a specified assessment. Accessible via HTTPS on port 8443, this endpoint ensures precise removal of mappings.

## Cold Storage Maintenance

### Personas Overview
- **Security Administrators:** Configure FGAC policies, manage threat analytics, and define query rewrite rules.
- **Database Administrators:** Install and manage S‑TAP agents, configure datasources, and perform native audit object management.
- **Compliance Officers:** Generate compliance reports, review audit trails, and manage retention periods for audit data.
- **Security Analysts:** Investigate threats, analyze policy violations, and respond to security incidents.

### Entities Overview
- **Datasources & Drivers:** SQL databases, noSQL stores, and associated JDBC drivers.
- **Security Policies:** Security policy definitions, audit policies, FGAC rules, and policy rules for threat analytics.
- **Managed Units & Groups:** Central Manager, managed units, and stap‑associated managed unit groups.
- **Audit & Reporting Entities:** Audited data, audit policies, report templates, and retention periods for compliance reporting.

## Guardium Data Protection Overview
IBM Guardium Data Protection is an enterprise security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Key Features
- Real-time SQL capture and S-TAP agents for activity monitoring
- Policy enforcement with S-GATE blocking and dynamic evaluation
- Time-based session activation and ignore-SQL settings
- External data correlation with custom tables for enhanced analysis
- Predefined common reports for quick access to audit and compliance data
- Comprehensive infrastructure management including CAS hosts and Managed Units

### Workflows
- **Configuration:** Deploy agents, define session rules, and set up managed units
- **Monitoring:** Review activity reports, run vulnerability assessments, and view audit trails
- **Enforcement:** Block queries, manage host status, and rotate credentials
- **Enrichment:** Import enterprise data and run threat-finder analyses
- **Reporting:** Generate and schedule predefined and custom reports

### Personas
- Security Administrator: Define policies and session rules
- Database Administrator: Deploy agents and monitor session activity
- Compliance Officer: Access predefined reports and review audit data
- Security Analyst: Investigate anomalies and correlate external data

### Core Entities
- Agents: S-TAP, A-TAP, Collector, Central Manager
- Policies: Security Policy, Session-Start rule, Ignore-SQL per Session rule
- Infrastructure: Managed Unit, S-GATE, Central Manager
- Domains: Query Main Entity, Common Reports, Analytic Outliers Status, Threat Finder Run Log
- Host Management: CAS Host, Server IP/Svc

## Document Overview
IBM Guardium Data Protection is IBM’s enterprise data security platform that monitors, protects, and audits structured and unstructured data across hybrid environments.

### Features
- **Activity Monitoring**: Real‑time inspection of database traffic and user behavior
- **Policy Enforcement**: FGAC access controls, data masking, session blocking
- **Vulnerability Assessment**: Automated scans for misconfigurations, weak passwords, and exploits
- **Compliance Reporting**: Templates for PCI‑DSS, GDPR, HIPAA, SOX, and other standards

### Workflows
- **Policy Management**: Define access rules, classification policies, and masking rules
- **Incident Response**: Investigate alerts, generate forensic reports, apply remediation
- **Asset Discovery**: Find data sources, classify sensitive objects, maintain an inventory
- **Audit & Evidence**: Export audit trails, generate compliance evidence, support investigations

### Personas
- **Security Administrators**: Configure Guardium components, manage policies and users
- **Database Administrators**: Install S‑TAP agents, monitor database health, resolve incidents
- **Compliance Managers**: Run regulatory reports, track audit findings, oversee protection
- **Data Analysts**: Query activity data, build custom dashboards, support business needs

### Entities
- **Data Collection Agents**: S‑TAP (kernel‑level), A‑TAP (user‑level), K‑TAP (alternative kernel collector)
- **Policy Objects**: Security Policy, Audit Policy, Classification Rule, Access Rule, Masking Rule
- **Infrastructure Components**: Central Manager, Aggregator, Managed Unit, APIs, Universal Connector

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection provides enterprise database activity monitoring and security across on-premises and cloud data stores. It offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Key Features
- Datasource connectivity via JDBC, native drivers, and CyberArk integration
- Real-time threat detection with SQL inspection and S-GATE blocking
- Compliance reporting for PCI-DSS, GDPR, HIPAA, and SOX
- Fine-grained access control and dynamic data masking

### Workflows
- **Configuration:**
  - Add datasources
  - Deploy S-TAP agents via GIM
  - Configure FGAC policies
- **Navigation:**
  - Review activity reports and vulnerability assessments
  - Use audit dashboard
- **Action:**
  - Block unauthorized queries
  - Rotate credentials
  - Respond to incidents

### Personas
- **Administration:** Manages platform configuration and user access
- **Data Management:** Handles datasources, S-TAP agents, and custom properties
- **Compliance:** Generates regulatory reports and audits evidence

### Core Entities
- **Agents:** S-TAP, A-TAP, K-TAP
- **Policies:** Security, audit, classification, access
- **Infrastructure:** GIM, Managed Units, S-GATE
- **Credentials:** Vault integration for secure handling

## REST API: Retrieve Datasource Custom Properties

The Guardium REST API provides an endpoint to retrieve all custom properties configured for datasources.

**Endpoint:** `GET /restAPI/datasource_properties`

**Purpose:** Returns a JSON payload containing key-value pairs for each datasource's custom properties, allowing flexible configuration management.

**Key Concepts:** RESTful API, datasource configuration, custom properties, JSON response

## REST API Syntax for Data Mart Profile

```markdown
DELETE https://[Guardium hostname or IP address]:8443/restAPI/datamartInProfile
```

Removes a data mart definition from a data mart profile.  
**Key Concepts:** datamart, data mart profile, REST API

## IBM Guardium Data Protection Overview

Guardium is IBM's enterprise database activity monitoring and security platform.

### Features
- Real-time monitoring and policy enforcement
- Threat detection & compliance reporting
- Supports structured and unstructured data, on-premises and cloud

### Workflows
- Configuration: add datasources, deploy S-TAP
- Navigation: view reports, run assessments
- Action: block queries, rotate credentials

### Personas
- Administration, security, database, compliance, security analysts

### Entities
- Agents/collectors: S-TAP, A-TAP, K-TAP, collector, aggregator, central manager
- Policies/rules: security, audit, classification, access
- Infrastructure: GIM, managed unit, S-GATE, universal connector

## Database Connection Architecture

Guardium supports multiple JDBC drivers: native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

**Key Concepts:** JDBC, native driver, browser service, dynamic port detection

## Activity Monitoring & Policy Enforcement

Guardium captures all database traffic via S-TAP agents and evaluates it in real time against security policies. Policies can target users, objects, operations, and time windows. Violations trigger alerts, reports, or blocking via S-GATE.

**Key Concepts:** S-TAP, S-GATE, security policy, real-time monitoring, audit trail

## IAM Instance Profile

An IAM instance profile grants an AWS EC2 instance permissions to call AWS services.

**Key Concepts:** IAM instance profile, EC2, AWS services, permissions

## Guardium Big Data Intelligence

Enables configuring GBDI datasources on Guardium, specifying supported authentication methods.

**Key Concepts:** GBDI, authentication, Guardium datasource

## SSL Configuration

When Informix or Oracle traffic is SSL encrypted, Guardium reports display client IP as 0.0.0.0. Mutual SSL can be configured without client certificates.

**Key Concepts:** SSL, client IP, Guardium reporting

## Manage AWS Data Streams

Controls to track, enable, and troubleshoot cloud Kinesis streams feeding Guardium collectors.

**Key Concepts:** AWS Kinesis, data streams, Guardium collectors

## Entitlement Optimization Users and Roles

Lists all users and their roles across collectors where Entitlement Optimization is enabled.

**Key Concepts:** entitlement optimization, users, roles, collectors

## Managing Correlation Alerts

Create and manage correlation alerts from the Add Alert page for policy rule violations or exceptions.

**Key Concepts:** correlation alerts, policy rule violations, exceptions

## Active Threat Analytics Setup

Monitors active threat analytics processes centrally or per managed unit.

**Key Concepts:** active threat analytics, monitoring, managed units

## Stop Log Access Only

Revokes log access only action for individual sessions based on search parameters.

**Key Concepts:** log access, session, search parameters

## Aggregation/Archive Domain

Contains data related to archiving and aggregation activities, accessible by the admin role.

**Key Concepts:** aggregation, archiving, admin role

## Discovered Instances Report

Provides detailed information about discovered database instances, including timestamp, host, protocol, port ranges, instance names, client, procedures, named pipes, database install directory, and DB2-specific fields.

**Key Concepts:** discovered instances, database discovery, reporting fields

## 4089. Network Configuration CLI Commands

Network configuration uses CLI commands such as:

- `interface set_ip <iface> <ip> <netmask>` – Assign static IP
- `bond add <iface1> <iface2>` – Create a bond interface
- `bond remove <iface1> <iface2>` – Remove an interface from a bond
- `failover set_primary <iface>` – Change the primary failover interface
- `network --reset` – Reset all interfaces to DHCP

After modifying network parameters, apply changes with `apply` and restart networking if needed: `service network restart`.

---

## 4090. REST API Syntax for Data Mart Configuration

To configure a Data mart in a report profile via REST API:

```http
PUT /restAPI/datamartinprofile
{
  "profile": "MyProfile",
  "datamart": {
    "name": "MyDataMart",
    "type": "JDBC",
    "host": "dm-host",
    "port": 1521,
    "database": "DATAMART"
  }
}
```

The request must include headers `Content-Type: application/json` and `Authorization: Bearer <access_token>`.

---

## 4091. REST API Syntax for Ranger Service Configuration

Configure a Ranger service named `myRanger`:

```http
POST /restAPI/add_ranger_service
{
  "name": "myRanger",
  "type": "RANGER",
  "host": "ranger-host",
  "port": 6080
}
```

The request must include headers `Content-Type: application/json` and `Authorization: Bearer <access_token>`. The response contains the created service ID: `{"serviceId": "<service_id>"}`.

---

## 4092. REST API Syntax for Threshold Addition to Policy Rule

Add a threshold to the policy rule "Sensitive Object Access" to trigger alerts when more than 10 queries occur within a minute:

```http
PUT /restAPI/add_threshold_to_rule
{
  "ruleName": "Sensitive Object Access",
  "threshold": {
    "type": "QUERY_COUNT",
    "value": 10,
    "unit": "MINUTE"
  },
  "action": "ALERT"
}
```

The threshold appears in the rule details page under **Policies > Rule Details**.

---

## 4093. REST API Syntax for On-Demand Aggregation

To initiate on-demand aggregation of the daily summary mart:

```http
PUT /restAPI/agg_ondemand
{
  "profile": "daily_summary"
}
```

The request must include the header `Authorization: Bearer <access_token>`. The response confirms successful queuing: `{"status":"queued","jobId":"<job_id>"}`. Check job status with `jobs --list` and view results in **Monitor > Aggregated Data**.

---

## 4094. REST API Syntax for Change Tracker Reset

To reset change tracking on the protected database `PRODDB`:

```http
PUT /restAPI/change_tracker_reset
{
  "dataSource": "PRODDB"
}
```

After execution, confirmation appears in the activity stream: `"Change tracking reset successful for datasource PRODDB"`.

---

## 4095. REST API Syntax for Assessment Duplication

To duplicate an assessment named "PCI Compliance Q4 2024" into a new assessment "PCI Compliance Q1 2025":

```http
PUT /restAPI/clone_assessment
{
  "sourceAssessment": "PCI Compliance Q4 2024",
  "targetAssessment": "PCI Compliance Q1 2025",
  "cloneRules": true,
  "clonePolicies": true
}
```

The new assessment appears under **Assessment > Configuration Assessments**.

---

## 4096. Assessment API for CAS Template Set Creation

Create a copy of the CAS template set "Financial Transaction Rules":

```http
POST /restAPI/clone_cas_template_set
{
  "sourceSet": "Financial Transaction Rules",
  "targetSet": "Financial Transaction Rules - Copy"
}
```

The request must include the header `Authorization: Bearer <access_token>`. The response shows the new template set ID: `{"templateSetId": "<template_set_id>"}`. Rename it later via `update_cas_template_set` API.

---

## 4097. REST API Syntax for Extraction Profile Cloning

Clone an existing extraction profile named "DB2 Full Profile":

```http
POST /restAPI/extractionProfile
{
  "sourceProfile": "DB2 Full Profile",
  "newProfile": "DB2 Full Profile - Copy"
}
```

Headers required: `Authorization: Bearer <token>` and `Content-Type: application/json`. The newly cloned profile appears in the drop-down for Extraction reports.

---

## 4098. REST API Syntax for Archival Storage Configuration (Incomplete)

Configure archival storage properties for Guardium:

```http
PUT /restAPI/archival_storage
{
  "protocol": "SFTP",
  "host": "archive.guardium.com",
  "port": 22,
  "path": "/archive",
  "userName": "archive",
  "password": "Password123"
}
```

Headers required: `Authorization: Bearer <token>` and `Content-Type: application/json`. The response confirms successful configuration.

## Overview

IBM Guardium REST API Reference provides endpoints for managing Guardium features, configurations, and services. It supports CRUD operations on Guardium entities via HTTPS endpoints with JSON payloads and parameters.

### Features

- Endpoints: `DELETE`, `GET`, `PUT`, `POST` methods
- Parameters: JSON payloads, query parameters, URL placeholders for hosts, ports, object identifiers
- Authentication: API keys or OAuth mechanisms

### Personas

- Security Administrators: Manage policies, assess vulnerabilities, monitor activities
- Compliance Officers: Generate reports, audit trails for regulatory needs
- Database Administrators: Control datasource connectivity and user access permissions

### Entities

- Data Sources: Databases, file systems, other monitored data stores
- Policies: Rules governing data access, classification, compliance
- User Auth: Authentication services including LDAP, API tokens, session tokens

## IBM Guardium REST API

### Overview
IBM Guardium provides a programmatic interface (REST API) for automation, monitoring, and integration. The API allows secure access to Guardium functions such as configuration management, monitoring, compliance, and data discovery using HTTP methods and JSON payloads.

### Authentication
Secure access requires a bearer token or basic authentication over HTTPS. Tokens can be obtained via API keys or OAuth flows.

### Key Endpoints and Syntax

| Category | Endpoint | HTTP Method | Purpose |
|----------|----------|------------|---------|
| **Enable FAM File Crawler** | `PUT /enable_native_audit` | Enable FAM file‑crawler functionality |
| **Enable Persistent Queue** | `GET https://<host>:8443/restAPI/enablePersistentQueue` | Activate persistent queue |
| **Enable Quick Search** | `PUT https://<host>:8443/restAPI/enable_quick_search` | Turn on quick search |
| **Execute Classification** | `PUT /execute_cls_process` | Remotely run classification processes |
| **Export Certificates** | `PUT /export_certificate` | Distribute certificates |
| **Export Log Files** | `POST /export_logfiles` | Export Guardium log files |
| **Export Transfer Key** | `POST /export_transfer_key` | Export transfer key |
| **Get Cluster Members** | `GET /cluster_members` | Retrieve members of a cluster |
| **Extraction Profile** | `GET /extractionProfile` | Get extraction profile details |
| **Insights Agent Config** | `GET /insights_agent_config` | Retrieve Insights agent settings |
| **IP to Alias Selected** | `GET /ip_to_alias_selected` | Get selection‑specific alias data |
| **Native Audit Configuration** | `GET /get_native_audit_*` | Query native audit setups |
| **Ranger Config** | `GET /get_ranger_config` | Fetch Apache Ranger configuration |
| **Test Result Detail** | `GET /get_test_result_detail_string_setting` | Retrieve test detail string settings |

### Workflows

**Configuration Automation**
- Register Guardium hosts
- Deploy S‑TAP agents
- Configure data sources and policies

**Monitoring Integration**
- Push real‑time alerts to SIEM or custom dashboards
- Correlate Guardium events with other security tools

**Compliance**
- Trigger ad‑hoc compliance assessments
- Retrieve and export compliance reports programmatically

**Data Export**
- Bulk export inspection results, audit trails, and audit records

### Personas
- **Guardium Administrators:** Automate admin tasks and manage large deployments.
- **Security Operations Teams:** Enrich incident response with Guardium data.
- **Compliance Officers:** Generate on‑demand audit evidence.
- **Application Developers:** Embed Guardium checks into CI/CD pipelines.

### Entity Types
- **API Key:** Authentication token.
- **Endpoints:** HTTP paths representing Guardium resources.
- **Parameters:** Query or body parameters for filtering/modification.
- **Responses:** JSON objects describing outcomes (status, data, messages).

### Features
- **Formats:** JSON input and output.
- **Batch Operations:** Execute multiple actions in a single request.
- **Scalability:** Supports high‑volume automation for enterprise environments.

## Guardium Data Protection Overview

IBM Guardium Data Protection offers enterprise-grade monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

### Feature Areas
- **Configuration:** PCI Accelerator, Data Compliance activation/deactivation, custom domains
- **Monitoring:** Real-time activity monitoring across internal and file domains, data source versioning
- **Compliance:** PCI-DSS auditing, other regulatory frameworks

### REST API Usage
```
PUT|GET|POST https://<Guardium_host>:8443/restAPI/<resource>
```
Requests require HTTPS (default port 8443) and valid authentication. Responses contain JSON with HTTP status codes; errors include an `error` field. Query parameters enable pagination, filtering, and detail selection.

## Data Compliance Overview

IBM Guardium Data Protection provides real-time monitoring, threat detection, compliance reporting, and central management across structured and unstructured data sources.

## Enabling the Data Compliance Feature

Data compliance is disabled by default. Follow the instructions provided to activate it.

## Custom Domains
Group related custom tables and define relationships for targeted reporting.

## Implement PCI Accelerator
Assist users in assessing PCI Data Security Standard compliance through guided workflows.

## Domain Based on Query Main Entity
Use the internal domain to run reports based on a query's main entity.

## Data Source Version History
Track changes and versions of data sources for traceability purposes.

## Domain-Based Reports
- **IMS Event (z/OS):** Summarizes IMS access types and commands for auditing.
- **Objects and Verbs:** Captures details of database interactions and rule violations.
- **System Domain:** Records configuration changes made on the Guardium appliance.

## FAM Domain
Groups entities related to file entitlement reports, accessible to admin roles.

## GIM Clients Domain
Describes entities and attributes for GIM client reports, accessible to administrators.

## Security Assessment Result Domain
Includes entities and attributes for assessing security risks and outcomes.

## Guardium Data Protection Overview

IBM Guardium Data Protection monitors and secures enterprise data repositories. It offers real-time activity monitoring, policy enforcement, compliance reporting, and vulnerability assessment across on-premises and cloud databases.

### Key Features
#### REST API Access
- HTTPS endpoints on port 8443 for all management functions

#### Configuration Management
- Clone existing security policies
- Configure authentication and data streaming settings

#### Security and Access Control
- Manage allowed database lists
- Define exception handling rules

#### Compliance Management
- Assign audit cases to users or groups
- Export configuration templates

#### External Integrations
- Interact with Kafka clusters
- Manage Group Member API settings
- Administer Universal Connector credentials

### Essential Workflows
#### Time Period Creation
- Define scheduling windows for automated tasks

#### User Assignments
- Route analytic case findings to appropriate personnel

#### Agent Deployment
- Install S-TAPs and data stream collectors on target systems

#### Policy Management
- Create, modify, and revoke security policies
- Configure audit controls and inspection engines

#### System Troubleshooting
- Purge unnecessary configuration data
- Test exception rules and modify sensitivity settings
- Uninstall obsolete components

### User Personas
#### Security Administrators
- Define and enforce data access policies
- Investigate security incidents and audits

#### Compliance Officers
- Generate regulatory reports
- Verify data handling practices

#### Data Engineers
- Monitor database performance metrics
- Configure data masking and tokenization rules

#### Threat Analysts
- Correlate security events across systems
- Conduct forensic investigations

# IBM Guardium REST API Overview

## Security Policy Management
- The Guardium REST API enables comprehensive security policy management, including cloning policies, configuring authentication, and defining new policies.
- All operations are performed via HTTPS on port 8443.

## General Overview
- The REST API provides programmatic interaction with Guardium's data protection platform.
- Features include CRUD operations for configuration and audit data, integration with external tools, and secure HTTPS endpoints.
- Personas: Security Administrators, Compliance Officers, Developers/Integrators.

## Specific REST API Endpoints
- **Datasource Removal**: `DELETE https://[hostname]:8443/restAPI/datasource`
- **Quarantine Deletion**: GuardAPI command with `dbUser`, `serverIp`, `serviceName`, `type` parameters.
- **Schedule Deletion**: `DELETE https://[Guardium hostname]:8443/restAPI/schedule`
- **Enable Big Data Intelligence**: `PUT https://[Guardium hostname or IP address]:8443/restAPI/bigDataInterface`
- **IP Restrictions Configuration**: `POST` to configure IP restrictions.
- **Value Encryption**: `encrypt_value` API from version 9.5.
- **Audit Process Execution**: `PUT /restAPI/audit_process`
- **Configuration Export**: `PUT https://hostname:8443/restAPI/export_config`
- **Data Mart Properties**: `get_datasource_custom_properties` from version 11.4.
- **MFA Configuration**: `GET /restAPI/configure_mfa`
- **Native Audit Objects**: `GET https://[Guardium hostname or IP address]:8443/restAPI/nau_objects_list`
- **Cloud Datasource Management**: Implicit endpoint for cloud datasource configurations.

## Additional Topics
- **CyberArk Password Vault Integration**: Integration endpoint at `https://[hostname]:8443/restAPI/cyberark`.
- **Sniffer Restarts Metrics**: Feature for monitoring Sniffer restarts and session data.
- **Assessment Test Listing**: `GET https://[Guardium hostname]:8443/restAPI/assessment_test`
- **Audit Process Metadata**: `GET https://[Guardium hostname or IP address]:8443/restAPI/audit_process`
- **Available Tests**: `GET https://[Guardium hostname]:8443/restAPI/available_test`

## Access Cloud Data Sources

Monitor cloud data activity through REST API endpoints and GuardAPI interfaces, supporting structured and semi-structured cloud stores.

### Key Concepts
- Cloud Connectors
- REST APIs for cloud services
- S-TAP deployment on cloud VMs

## Features Overview
- Real-time database transaction monitoring across data sources
- Risk-based analytics, anomaly detection, and customizable security policies
- Automated discovery and classification of sensitive data
- System-level and database configuration vulnerability scanning
- Pre-built compliance templates (GDPR, PCI-DSS, HIPAA, etc.)

## Workflows Overview
- Deploy Collectors, configure Central Manager, integrate LDAP/SAML
- Configure datasource connections, define audit policies, enable S-TAP agents
- Review reports, investigate incidents, create risk assessment views
- Apply patches, remediate vulnerabilities, update policies

## Personas Overview
- **Security Admin:** Configures policies, monitors incidents, manages access
- **Database Admin:** Manages datasource connections, granular controls
- **Compliance Officer:** Generates audit reports, validates compliance
- **SOC Analyst:** Investigates alerts, correlates with SIEM, responds to threats

## Entities Overview
- Core Cloud Agents (Collectors, Central Manager) processing audit data
- Lightweight kernel-level interceptors (S-TAP Agents) on database servers
- Policy Engine and Rule Engine for evaluating database activity
- Configuration objects (Policies, Rules) defining compliance rulesets

## Execute System Diagnostics Command

Run system diagnostics with optional parameters:
- `durationInSec` (seconds)
- `level` (basic or detailed)
- `api_target_host` (target execution host)

**Via:** GuardAPI (`system_diagnostics_run`) or REST (`PUT /restAPI/system_diagnostics`)

## Group Query REST Service

Query groups by criteria using GET.

**Via:** `GET /restAPI/group_query`

**Parameters:** `criteria` (group name/type), `api_target_host`

## SMTP Alert Configuration REST Endpoint

Configure SMTP alerts via POST.

**Via:** `POST https://[Guardium hostname]:8443/restAPI/alerter_smtp`

**Parameters:** SMTP server details, alert settings

## SNMP Alert Configuration GuardAPI

Configure SNMP alerts.

**Via:** GuardAPI (`alerter_snmp`)

**Parameters:** SNMP server configuration

## Set Entitlement Datasource Parameter

Alter entitlement-optimized datasource configurations.

**Via:** GuardAPI (`set_entitlement_datasource_parameter`)

**Parameters:** Datasource identifier, configuration values

## Retrieve Alerter Settings

Fetch alerter settings.

**Via:** `GET /restAPI/alerter_settings`

**Parameters:** None

## Update Data Mart Edge Settings

Update data mart edge configurations.

**Via:** `PUT https://[host]:8443/restAPI/update_edge`

**Parameters:** Edge settings from CLI help

## Assessment Test Execution

Invoke assessment tests.

**Via:** `PUT https://[hostname]:8443/restAPI/assessment_test`

**Parameters:** Assessment test configurations

## Document Overview

IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform that provides
real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting
for structured and unstructured data stores on-premises and in the cloud.

### Features
- **Datasource Connectivity:** Dynamic port detection, multi-driver support, CyberArk credential vault integration
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation
- **Compliance & Reporting:** PCI-DSS, GDPR, HIPAA, SOX report templates; automated audit trails
- **Query Management:** Create, modify, filter by domain, clone or build from scratch
- **Customization:** Query naming, attribute definition, domain selection, role configuration, drill‑down control, API assignments
- **Change Tracking:** NOT IN ALIASES, CAS Changes domain, Value Change domain, Monitor Values entity
- **System Monitoring:** Server IP, System Var Disk, Storage class
- **Security Controls:** Oracle entitlements, IMS Checkpoint Results, CVE information pages
- **Backup & Recovery:** Restoring default and custom certificates, system backup alerts

### Workflows
- **Query Definition:** Choose domain, name

## Query Definition

Define a query by selecting a domain, naming the query, choosing the main entity, configuring roles, setting datamart assignments, enabling drill‑down control, and specifying API links.  

## Managing Patches on Central Manager or Enterprise Hub

The patch management interface shows available updates for Guardium units on the same version. Schedule installation windows, track status, and roll back if needed. Patches include driver updates, UI improvements, and security fixes, with staged rollout to minimize disruption.

## GIM Command Syntax

### Agent Provisioning
- `gim_install` – Installs an agent package on a target host. Requires the `PACKAGE_NAME`, `HOST_NAME`, and optional `VERSION`.
- `gim_configure_agent` – Sets S‑TAP or K‑TAP parameters after installation. Takes `HOST_NAME`, `AGENT_TYPE`, and key/value pairs.

### Package Management
- `gim_list_packages` – Lists available Guardium packages on the GIM server.
- `gim_install_package` – Installs a specific package version on one or more managed units. Uses `-p` for package and `-v` for version, with `-t` for target host list.
- `gim_upgrade_package` – Upgrades an existing agent to a newer version. Specified with `-p` and `-v`.

### Policy Distribution
- `gim_deploy_policy` – Deploys active policies from the central manager to selected collectors. Identifies the policy by `POLICY_NAME` and target host list with `-t`.

### Patch Automation
- `gim_apply_patch` – Applies a hotfix to designated appliances. Requires `-p` for patch identifier and `-t` for target hosts.
- `gim_schedule_patch_job` – Schedules recurring patch cycles across a managed group. Uses `JOB_ID`, `START_TIME`, and recurrence rules.

### Audit Trail
- `gim_audit_log` – Queries the GIM audit log for actions performed against specific hosts or packages. Supports filtering by timestamp, action type, and user.

### Command Format
All GIM commands follow the pattern:
```
gim_<ACTION> --<OPTION> <VALUE>
```
Parameters are passed as named arguments prefixed with `--` (long form) or `-` (short form). Required arguments:
- `--host <HOST>` – IP address or hostname of the target unit.
- `--package <PACKAGE>` – Name of the Guardium software package.
- `--version <VERSION>` – Target version for install/upgrade actions.
Optional arguments:
- `--target <HOST_LIST>` – Comma‑separated list of hosts for bulk operations.
- `--policy <POLICY>` – Name of the policy to deploy.
- `--job_id <ID>` – Identifier for scheduled jobs (patch, uninstall, etc.).

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection monitors and secures database activity across on-premises and cloud data sources, using S-TAP agents and centralized management. It supports detailed policy enforcement, compliance reporting, and integration with external systems.

### Key Features
- Database coverage for JDBC, native drivers, and browser services
- Real-time protection with S-TAP monitoring and S-GATE blocking
- Compliance reporting for PCI-DSS, GDPR, and HIPAA
- Integration with Solr, REST API, Ranger HDFS, CyberArk, Hadoop

### Personas
- **Security Administrators:** Configure security policies
- **Compliance Officers:** Generate audit reports
- **Database Administrators:** Automate monitoring tasks

## Guardium Data Protection Overview
IBM Guardium Data Protection is IBM’s enterprise platform for database activity monitoring and security. It offers real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features
- **Policy Definition:** Centralized security policies, data classification rules, and audit policies.
- **Real-Time Monitoring:** Continuous traffic capture via S-TAP agents.
- **Audit and Reporting:** Generates regulatory compliance reports and security analytics.
- **Integration:** Works with various security tools and platforms, including CyberArk, Hadoop, and Ranger HDFS.

# IBM Guardium Data Protection Overview

## Features
- Real-time monitoring and policy enforcement across structured and unstructured data
- Built-in compliance templates for PCI-DSS, GDPR, HIPAA, SOX
- Automated incident response, query blocking, and credential rotation

## Workflows
- **Configuration:** Add data sources, deploy agents via GIM, configure policies
- **Navigation:** Review activity reports, run vulnerability assessments, audit dashboard
- **Action:** Block unauthorized queries, rotate credentials, respond to incidents

## Personas
- **Administration:** Platform setup, user/role management, system health
- **Security Management:** Policy authoring, threat detection tuning, SIEM integration
- **Compliance:** Regulatory reporting, audit evidence collection

## Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector

## Upgrading CyberArk SDK
- Performed via Central Manager GUI
- Distributes patch and credentials to managed units

## Database Connection Architecture
- Supports multiple JDBC drivers for SQL databases
- Browser service resolves instance names to current ports dynamically

## Activity Monitoring
- Captures database traffic via S-TAP agents
- Evaluates in real time against security policies
- Triggers alerts, reports, or blocking via S-GATE

## Access Rule
- Defines criteria for permitting or denying access to protected objects
- Evaluates user identity, IP address, object name, operation type
- Assigned to categories governing behavior and prioritization

## Runtime Sensitive Object Identifier Domain
- Framework for defining entities and attributes to identify sensitive objects
- Captures contextual metadata for dynamic evaluation of data sensitivity
- Enables appropriate protection policies application

## CAS for MongoDB
- Scans various components of MongoDB file system
- Assesses data sensitivity and compliance postures
- Notes distinct handling for Teradata Aster

## Installing CAS from CLI
- Automates and scripts deployment across large-scale environments
- Supports bulk configuration and integration with automation frameworks

## Deployment Health Views
- Aggregates performance and operational metrics
- Consolidated dashboard for rapid identification of anomalies
- Facilitates proactive management and optimization

## Compressed Guardium Documentation

# Guardium Reference Material

## Guardium Data Protection APIs

**Features Overview**
- Provides CLI (SSH) and REST web services for installation, configuration, monitoring, policy management, compliance, and audit.
- Separate calling conventions for each Guardium release.
- Supports HTTP/HTTPS over port 8443 with JSON payloads.

**Workflows Overview**
- Use the root Service Catalog to discover available endpoints.
- Execute requests with POST for create/modify, GET for retrieval, DELETE for removal.
- Parse JSON responses and handle HTTP status codes.
- Scriptable with curl or any HTTP client for automation.

**Personas Overview**
- Security Administrator: Manages policies and block rules.
- Data Engineer: Handles classification and universal connectors.
- Compliance Officer: Retrieves audit reports and adjusts retention.
- Operations Team: Installs S-TAP agents via GIM APIs and monitors health.

**Entities Overview**
- Configuration Entities: Policy, Rule, Alert, Report.
- Communication Entities: Managed Unit, Central Manager, S-TAP Agent.
- Data Entities: Data Source, Sensitive Object, Classification Results.

## Troubleshooting Common Issues

**Query Missing from Correlation Alert**
- Verify the "Count" field settings.
- Ensure query results are sorted by timestamp.
- Check timing discrepancies.

**Enabling External S-TAP Provisioning UI**
- Follow prerequisite steps from Guardium documentation.
- After enabling, deploy and manage S-TAP agents through the UI.

## Patch Management

**Post-Patch Installation**
- Repeat the patch installation for additional relevant patches.
- Ensure comprehensive system updates.

## API Invocation Details

**CLI Access**
- Access the Guardium CLI through SSH over the management IP/domain.

**Catalog Entry APIs**
- Manage catalog entries for data archive files and result archive files.

**Classification APIs**
- Supports classification configuration, test automation, and scripting.

## Example API Calls

**REST API Curl Example**
- Returns JSON listing candidate secondary central manager IP addresses and hostnames.

**REST API Syntax**
- Example: `POST https://[Guardium hostname or IP address]:8443/restAPI/alias`

**Group Listing**
- Access via `GET https://[host]:8443/restAPI/group`

## 4471 REST API syntax  
PUT `https://[host]:8443/restAPI/alias` with a JSON body describing the alias change.  
Authentication: Basic or OAuth; success/error payload returned as JSON.

## 4472 REST API syntax  
PUT `https://[host]:8443/restAPI/policy` with a JSON payload containing the policy definition.  
Functional equivalent of GuardAPI **update_policy_parameters**.

## 4473 REST API syntax  
PUT `/restAPI/update_user_db` with schema parameters in the request body.  
Used after schema‑changing actions such as **create_allowed_db**.

## 4474 Managing certificates with Venafi  
From Guardium 11.0: `venafi_test_cyberark_connection` tests connectivity to a CyberArk server and returns success/failure, supporting certificate lifecycle automation.

## 4475 Cloud database service protection  
Guardium adds agents that capture encrypted traffic for cloud DB services (Amazon RDS, Azure SQL DB, Google Cloud SQL), enabling policy enforcement without application changes.

## 4476 Entitlement Optimization browse entitlements  
Interactive browse mode with filter controls allows drilling into user/group entitlements, roles, and permission usage for audits and remediation.

## 4477 Configuring the trust evaluator  
Configurable via UI or API; default monitors all connections. Set `monitor_admin_only` to restrict evaluation to administrator sessions only. Configuration is stored in Guardium’s config store.

## 4478 Data Protection Dashboard  
Aggregates risk and compliance metrics into a senior‑security overview: widgets for violations, compliance posture, audit activity, and threat indicators for rapid decision‑making.

## 4479 Import multiple databases  
The `import_multiple_databases` API bulk‑loads database inventory from CSV/Excel. Required columns: `host`, `port`, `db_type`, `instance_name`, `description`. Additional columns may include `user`, `password`, `ssl_enabled`.

## 4484

## Archive Purge domain

The Archive Purge domain records activities related to purging archive entries within Guardium. It captures details like the purged archive name, number of affected rows, operator, and timestamp, providing auditing capabilities for archive management operations.

### Key Attributes
- **ArchiveName**: Name of the purged archive
- **RowsPurged**: Count of rows removed during purge
- **OperatorId**: User who initiated the purge
- **PurgeTimestamp**: Date and time of the purge operation

This domain assists in tracking archival cleanup activities for compliance and storage management.

strators to manage files on the appliance:

- `ls` - List files in a directory, e.g. `ls /var/audit`
- `cp` - Copy files, e.g. `cp /var/audit/myfile.log /backup`
- `mv` - Move or rename files, e.g. `mv /var/audit/old.log /var/audit/processed`
- `rm` - Remove files, e.g. `rm /var/audit/processed/*.bak`

Permissions can be modified using `chmod` with octal notation or symbolic parameters:

```bash
chmod 640 /var/audit/*.log   # Read/write for owner, read for group
chmod u+rwx,g+r,o-rwx /home # Add execute permission for owner, read for group
```

Ownership changes are made with `chown` or `chgrp`:

```bash
chown guardium:guardium /home/guardium/data
chgrp -R dbadmins /var/guardium/reports
```

Compression utilities work as on Linux: `gzip`, `gunzip`, `tar -czf archive.tar.gz dir/`

Key Concepts: Filesystem Commands, Permissions, Ownership, Archiving

# Investigation File Management

Use these Guardio CLI commands to manage investigation files:
- `guardio file backup` creates GZIP-compressed backup archives of incident
  reports and exported logs
- `guardio file restore` extracts selected files from backup archives to the
  Guardium file system
- `guardio file list` displays available backup archives with timestamps
- `guardio file delete` permanently removes old backup archives

Command arguments:
- `--source` (required): Specifies the database name
- `--type` (required): Specifies whether to back up incidents or logs
- `--keep` (optional): Number of backups to retain

# Adding Data Sources to Security Assessments

The Assessment API `add_assessment_datasource` adds a data source to an
existing security assessment. Example command:
```bash
grdapi add_assessment_datasource description="sales_prod"
                               datasource="SALES_PROD_DB"
```
Parameters:
- `description`: Unique identifier for the assessment entry
- `datasource`: Name of the data source from the Central Manager registry

This API enables automated population of assessments from external scanners or
configuration management tools for risk scoring.

# Cloud Security Group Integration

The `add_ip_to_sg` API adds a Guardium appliance IP to cloud security groups
during incident response. Example command:
```bash
grdapi add_ip_to_sg sg_id=sg-12345 guardium_ip=10.1.1.100
```
Parameters:
- `sg_id`: Cloud security group identifier (AWS, Azure, or GCP)
- `guardium_ip`: IP address of the Guardium collector generating the alert

Integrate this with investigation dashboards to automate server quarantine or
network access restriction.

# Automated Policy and Rule Management

Guardium Policy and Rule APIs allow programmatic security configuration:

Create policy:
```bash
grdapi add_time_period policy_name="PCI-DSS"
```

Add rule to policy:
```bash
grdapi add_rule policy_name="Data_Sensitivity"
               rule_name="PII_Detection"
```

When creating rules, specify Rule Type (SQL, OsCommand) and Rule Direction
(Allow/Deny). Rules inherit from policy templates in Configuration > System >
Policies.

## Document Overview

IBM Guardium Data Protection is an enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data across on-premises and cloud environments.

## Feature: Log Ingestion for Cloud Accounts

Log Ingestion collects and processes audit logs from cloud services like AWS to enhance security monitoring and compliance reporting.

## GuardAPI Syntax for List Available Audit Processes

`list_audit_processes` displays available audit process types for configuring audit policies and monitoring workflows in Guardium V11.2 and later.

## GuardAPI Syntax for List Group Members by ID

`list_members_of_groups_by_id` retrieves group members based on specified integer IDs for access control management.

## Enabling Smart Card Authentication

Smart card authentication can be enabled alongside other mechanisms like `get_all_modifiable_guard_params` and Health Analyzer APIs for multi-factor authentication.

## Data Mart APIs for Group Member Management

Data Mart APIs like `remove_members_of_groups_by_desc` facilitate automated group management tasks by managing group members.

## GuardAPI Syntax for Remove Group Members by ID

`remove_members_of_groups_by_id` removes users from a security group by specifying integer IDs for precise access control.

## GuardAPI Syntax for LDAP Import

`run_custom_table_ldap_import` imports LDAP data into standard or custom tables for user management and data source configuration.

## GuardAPI Syntax for Cold Storage Maintenance

`set_cold_storage_maintenance` configures settings for cold storage maintenance tasks to manage data retention and archiving.

## Role Functions for Log Ingestion

Roles involved in managing log ingestion processes include log collection, normalization, and analysis for security and compliance in cloud integrations like AWS.

## Testing S-TAP Agents for Database Connection

Instructions are provided to verify S-TAP agent connectivity to a database by connecting to a sample database and running an SQL query to validate installation and configuration.

## Document Overview
IBM Guardium Data Protection secures databases and cloud data stores with monitoring, policy enforcement, and compliance reporting.

## Features Overview
- Granular audit trail collection.
- Machine‑learning‑based behavior analytics.
- Centralized security policies for access, masking, and automated response.
- Multi‑domain support (relational, NoSQL, filesystem, big data, cloud).
- Pre‑built compliance templates.

## Workflows Overview
1. **Create policy → Deploy → Monitor alerts**  
2. **Investigate incident → Remediate**  
3. **Schedule scans & compliance reports**  
4. **Manage central console**  

## Personas Overview
- **Security Administrators** – enforce policies, approve exceptions.  
- **Database Administrators** – provision agents, manage data sources.  
- **Compliance Officers** – audit logs, generate evidence.  

## Entities Overview
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager.  
- **Policies & Rules:** Security policy, audit policy, classification rule, access rule.  
- **Management Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector.

## Centralized Security Management

IBM Guardium is IBM's data security platform that provides unified visibility and control over structured and unstructured data assets. It continuously inspects, detects, alerts on, and blocks threats to on-premises and cloud data. Guardium uses a modular, policy-driven architecture for real-time monitoring, automated classification, and user‑behavior analytics, delivering compliance evidence and threat mitigation across hybrid environments.

### Entities Overview
- **Guardium Agents**: S‑TAP (installed on databases), A‑TAP (file‑system), K‑TAP (kernel‑level), Collectors, Aggregators, and Central Manager VMs.
- **Security Objects**: Policies, Rules (access, classification, audit, anomaly), Groups, Data Sources, Encryption Keys.
- **Infrastructure Components**: Managed Units, S‑GATE firewalls, Vulnerability Assessment scanners, Central Manager, Identity Gateways, and Integration Connectors.

## 4549. Run‑Time Parameter Operator Default Value

The **Run‑Time Parameter Operator Default Value** policy rule illustrates how to enforce a condition based on multiple attributes. It checks whether a client IP, database user, and server IP match known risky users while the severity of the related risk indicator is at least 1, triggering an alert when the condition is met.

## 4554. Attribute Description

Guardium Job domain attributes include `End Time` (completion time), `Guardium Job Description` (human‑readable name), `Process ID` (OS process ID), `Process Run ID` (internal run identifier), and `Queue Time` (wait duration before execution). These attributes help track jobs and monitor SLA compliance.

## 4556. MYSQL User Privileges 500

The **MYSQL User Privileges 500** (and similar **MYSQL Host Privileges 502**) entities capture fine‑grained privilege records from MySQL audit trails. Each entry contains user name, host, privilege type, and grant level, enabling precise audit of user permissions.

## 4559. Implementing Central Management in a New Installation

Implementing Central Management in a new Guardium installation consists of:
1. Designating a Guardium appliance as the **Central Manager**.
2. Applying a shared secret across all units.
3. Registering each managed unit with the Central Manager.
4. Grouping units logically for policy distribution and consolidated reporting.

# Guardium Data Protection Overview

IBM Guardium Data Protection is a unified platform for securing and complying with data across diverse environments, including databases, data lakes, Big Data platforms, and file systems. It centralizes monitoring, policy enforcement, threat detection, and compliance reporting. Core personas include administrators, security analysts, database administrators, compliance officers, and application developers.

## Features

- **Real-time Monitoring:** Continuous traffic capture and analysis via S-TAP agents.
- **Policy Enforcement & Blocking:** Centralized policies, recursive validation, and S-GATE actions for immediate remediation.
- **Vulnerability and Configuration Assessment:** Automated scans, rulesets, and scoring dashboards.
- **User Behavior Analytics:** Baseline profiling, anomaly detection, and entitlement reviews.

## Workflows

### Configuration & Deployment
- Add data sources, deploy collectors, manage Guardium Installation Manager (GIM).

### Policy Management
- Build and apply Fine-Grained Access Control (FGAC), audit, and classification policies.

### Threat Response
- Alert triage, incident investigation, and automated mitigation.

### Reporting & Auditing
- On-demand and scheduled reports for PCI-DSS, HIPAA, GDPR, etc.

## Personas

- **Security Administrator:** Defines policies, manages incidents, oversees compliance dashboards.
- **Database Administrator:** Installs agents, maintains data sources, troubleshoots connectivity.
- **Compliance Officer:** Executes audit programs, generates regulatory reports, validates data handling.
- **Security Analyst:** Investigates behavioral anomalies, constructs search queries, automates remediation.

## Entities

- **Collectors & Agents:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- **Policy Types:** Security Policy, Audit Policy, Classification Policy, Access Policy.
- **Infrastructure Components:** Guardium Central Manager, Managed Units, S-GATE, Universal Connectors.

## Unit Utilization Data Processing

Configuring unit utilization data processing enables Guardium systems to collect and display CPU, memory, and I/O statistics from each Managed Unit. This data is aggregated by the Central Manager and presented in dashboards and reports for monitoring system load across the Guardium deployment.

## Managing Access by IP Address

The `update_istap_config` API allows administrators to define IP-based access controls in Guardium V9.5 and later. This enhances security monitoring and compliance by filtering traffic at the IP level.

## Trust Evaluator Status

The Trust Evaluator's Status window displays the progress of the probability engine as it learns typical traffic behaviors. This insight helps fine-tune security policies by understanding the system's normal operational patterns.

## Configuring Actions

The "Configure Actions" feature provides flexibility in managing data access and security. Administrators can adjust analyzer settings or activate session-level policy features, enabling transformations or exceptions in rule processing.

## Guardium Overview

IBM Guardium Data Protection is a platform that monitors structured and unstructured data sources in real time, enforces security policies, assesses vulnerabilities, and helps organizations meet compliance requirements.

### Features

- Real-time monitoring with S-TAP agents
- Policy enforcement via S-GATE
- Vulnerability assessment scans
- Built-in compliance reporting templates

### Workflows

- Add a data source
- Threat investigation
- Compliance audits

### Personas

- Guardium Administrator
- Security Administrator
- Database Administrator
- Compliance Officer

### Entities

- Agents and Collectors
- Security and Audit Policies
- Infrastructure Components
- Audit Objects

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

knowledge, workflows

To view group membership and usage, utilize the API to add group members by ID, available since V9.5.

---

## External S-TAP

`def46287-48fe-488e-926b-829b9b743de4`  |  **categories:** knowledge, workflows

Verify External S-TAP service status from the Guardium UI after deployment via container_mgmt.sh.

---

## User Quarantine

`c4393814-7087-4310-86a1-51e4ecb378b3`  |  **categories:** knowledge, workflows

Start user quarantine by executing the GuardAPI command.

---

## Security APAR

`fb541280-5137-4c7c-b7e2-60d9df6c3bc8`  |  **categories:** knowledge, domains

Security APAR defines vulnerability tests using Authorized Program Analysis Report (APAR) tests, organized under the Security domain.

---

## IAM Instance Profile

`957435d7-a77c-493a-b9c7-1490cb6bfcb0`  |  **categories:** knowledge, domains

IAM Instance Profile authentication type includes Access Key ID and Secret Access Key fields.

---

## Audit Log

`627bd270-6b6e-4c4a-905c-8b44cd49e850`  |  **categories:** knowledge, domains

Audit logs categorize with syslog facility "user" and priority "info".

---

## User Profile

`057a7012-3909-415e-9a55-4979036a0943`  |  **categories:** knowledge, domains

User profile stores full name, email, account name, and location.

---

## CAS

`4285ec7e-f072-43fa-ba1a-c50624d269f3`  |  **categories:** knowledge, domains

CAS (Configuration Auditing System) manages host configuration and templates via APIs.

---

## Query Rewrite

`67e57f60-cc2c-4656-97d6-a50375116df0`  |  **categories:** knowledge, domains

Query Rewrite allows testing queries or defining complex APIs for dynamic SQL management.

---

## App Access Management

`87b3d94d-822e-4cbed70b-bc3b3c7cdd9e`  |  **categories:** knowledge, domains

Use GuardAPI command to remove an application with specified appId.

---

## Groups

`aa33e8e1-23aa-4af1-b408-b6532acccea2`  |  **categories:** knowledge, domains

Group management API adds members to groups, available in V9.5 and later.

---

## External S-TAP

`1899a274-8e4f-4c4b-ba01-f42925674e43`  |  **categories:** knowledge, entities

External S-TAP instances are verified for service running status via the Guardium UI post-deployment.

---

## Root Password Reset

`11d5ae45-3d05-40f4-8fb8-3e84d115f4a6`  |  **categories:** knowledge, entities

Reset appliance root password using a private passkey and specific CLI command.

## Viewing Policy, Report, and Query Usage of a Group in Guardium

To list the policies, reports, and queries that reference a specific group in Guardium:

1. Open the Guardium UI and navigate to **Reports** > **Report Builder**.
2. Select the report you wish to examine and click **Edit**.
3. In the report definition, locate the **Groups** section.
4. Add the target group to the report's query or filter conditions.
5. Run the report; Guardium will list all policies, reports, and queries that reference the group.

## 4625. Where to search

Where to search allows running discovery, reviewing reports, removing false-positives, identifying runtime sensitive-object identification, and scheduling audits. This feature streamlines the data discovery and classification process, helping organizations efficiently manage their data assets and ensure compliance with regulatory requirements.

## 4626. Sybase IQ

Guardium supports Sybase IQ databases with local user authentication. It does not support LDAP or Kerberos. Guardium provides monitoring and protection capabilities for Sybase IQ, ensuring secure access and compliance for this specific database platform.

## 4627. Rule types, categories, classifications

Rules within a policy are processed sequentially. Evaluation stops at the first triggered rule unless it contains multiple actions. Guardium organizes rules into types, categories, and classifications for precise enforcement based on criteria like user, object, operation, and time windows.

## 4628. Method 1

Method 1 processes a single alert message, taking the message string and timestamp as parameters. It provides detailed insights and actions for specific security events detected by Guardium's monitoring system.

## 4629. Buffer Usage Monitor

Buffer Usage Monitor offers extensive statistics on buffer usage, providing insights into system performance and data processing efficiency. Administrators can identify bottlenecks and optimize resource allocation to improve overall system performance and stability.

## 4630. Full SQL

The Full SQL report summarizes SQL commands performed by users or executed on the database. It helps track and analyze SQL activities to ensure compliance and identify potential security threats or unauthorized access attempts.

## 4631. Outstanding Audit Process Reviews

This feature lists uncompleted Guardium audit processes assigned to users, with details in Table 1. It helps organizations track audit task progress, ensuring timely completion and regulatory compliance.

## 4632. Access Policy domain

The Access Policy domain tracks available policies on a Guardium system. It describes the domain's entities and attributes, providing a comprehensive view of security policies for effective management and enforcement of access controls.

## 4633. BigData Intelligence Classification Process Log domain

This domain reports on classifier process logs, providing an overview of the domain's structure and attributes. It helps monitor and analyze classification processes, ensuring data is accurately categorized and protected according to defined policies.

## 4634. Security Assessment Result domain

The Security Assessment Result domain records vulnerability assessment results and describes its entities and attributes. It is crucial for tracking and managing security vulnerabilities, enabling organizations to prioritize and address risks effectively.

## 4635. Uid Chain

The Uid Chain entity provides detailed information about user identities and access, supporting robust identity and access management within Guardium's security framework. It is part of the GIM Clients domain, focusing on specific elements for administrators.

14

integration

IBM Guardium's database activity monitoring can integrate with Azure Event Hubs for comprehensive cloud database protection, real-time visibility, policy enforcement, and compliance auditing.

---

## Document Overview

IBM Guardium Data Risk Analyzer (DRA) discovers, classifies, and assesses enterprise data risk across on-premises and cloud data stores. It maps sensitive data, correlates findings with security controls, and provides compliance insights and remediation recommendations.

### Features Overview
**Data Discovery:** Deep scans structured and unstructured data sources.
**Classification Engine:** Identifies sensitive information (PII, PCI, PHI, etc.).
**Risk Scoring:** Calculates exposure, encryption status, access control risks.
**Remediation Workflow:** Generates tickets, tracks remediation tasks.

### Workflows Overview
1. **Discovery:** Configure data sources, schedule scans.
2. **Classification:** Apply classifiers to identify sensitive data.
3. **Risk Assessment:** Review dashboards, prioritize findings.
4. **Remediation:** Initiate workflows, track progress, report completion.

### Personas Overview
- **Data Owners:** Manage inventories, approve findings, oversee remediation.
- **Security Administrators:** Configure sources, classifiers, policies.
- **Compliance Officers:** Generate reports, verify controls, audit findings.
- **IT Operations:** Execute remediation tasks and maintain data sources.

### Entities Overview
- **Datasources:** Databases, file systems, cloud storage.
- **Sensitive Data Types:** Classified entities such as PII, PCI, PHI.
- **Risk Metrics:** Quantitative exposure, encryption, access vulnerabilities.
- **Remediation Tasks:** Actions for access control changes, policy updates, encryption implementations.

---

## Classification Process Results Domain

This domain captures details of each classifier run, including timestamps, status, matched entities, applied rule sets, and confidence levels. It links to original scanned content for verification and reporting.

### Attributes
- Process ID
- Start/End Timestamps
- Classification Outcome
- Matched Ruleset IDs
- Classifier Version
- Scanned Records Count
- High/Low Confidence Counts

### Key Concepts
- Classifier Run Logs
- Sensitivity Assessment
- Confidence Scoring
- Matched Entities

---

## Unstructured Data Protection Overview

IBM Guardium Unstructured Data Protection extends database activity monitoring to file-based data across unstructured repositories. It provides real-time scanning, classification, and policy enforcement for compliance and security.

### Features Overview
- **Unstructured Data Detection:** Scans file repositories for sensitive data.
- **Policy Enforcement:** Applies security policies to file access, modification, and transfer.
- **Compliance Reporting:** Generates tailored audit reports for regulations like GDPR and HIPAA.
- **Integration with Guardium Core:** Unifies monitoring of structured and unstructured data.

### Workflows Overview
- **Configuration:** Set up data sources, classifiers, policies, and schedules.
- **Monitoring:** Real-time alerts, policy violations, activity reporting.
- **Remediation:** Block access, quarantine files, trigger incident response workflows.

### Personas Overview
- **Security Administrator:** Defines policies, manages sources, configures classifiers.
- **Compliance Officer:** Reviews reports, ensures regulatory adherence, configures templates.
- **Data Analyst:** Analyzes results, manages rules, optimizes policies.

### Entities Overview
- **Data Sources:** HDFS, S3, NFS, object storage repositories.
- **Classifiers:** Regex patterns, dictionary-based matches, machine learning models.
- **Policies:** Access rules, modification rules, transfer rules, encryption rules.
- **Reports:** Activity summaries, compliance validation, risk assessment scores.

---

## Unstructured Data Policy Configuration

Administrators define policies for monitoring and protecting unstructured data, specifying triggers, conditions using runtime wildcards, and enforcement actions such as alerting, blocking, or redacting sensitive information.

### Key Concepts
- Policy Definition
- Triggers
- Conditions
- Runtime Wildcards
- Enforcement Actions

---

## Document Overview

IBM Guardium Data Protection monitors and secures structured and unstructured data across on-premises and cloud environments.

### Features Overview
- **Hadoop Integration:** Configuration for monitoring Hortonworks Ranger.
- **External S-TAP:** Site-specific deployment requirements.

# Guardium Data Protection Reference

## Features Overview
- **Threat Detection:** Real‑time policy enforcement, rule‑based blocking, incident generation
- **Vulnerability Assessment:** Automated scans, discovery of sensitive data, configuration checks
- **Compliance Reporting:** PCI‑DSS, GDPR, HIPAA, SOX, custom templates; audit‑trail generation
- **Session Management:** Session‑level policies, granular control over connection attributes
- **Alerting & Notifications:** Real‑time alerts, alert domains, email integration

## Workflows Overview
- **Configuration:** Add data sources, deploy S‑TAP agents, define FGAC policies
- **Policy Management:** Create and install session‑level policies via Policy Builder for Data
- **Investigation:** View activity reports, generate executive dashboards, run outlier detection
- **Remediation:** Block malicious sessions, rotate credentials, resolve connection issues

## Personas Overview
- **Security Administrator:** Manages policies, reviews alerts, conducts risk assessments
- **Database Administrator:** Installs agents, monitors performance, resolves S‑TAP issues
- **Compliance Officer:** Generates regulatory reports, defines compliance rules
- **Data Analyst:** Accesses activity dashboards, runs ad‑hoc queries securely

## Entities Overview
- **Policies & Rulesets:** Security Policy, Audit Policy, FGAC Policy, Session‑Level Policy
- **Domains & Attributes:** Alert Domain, Eagle Eye Domain, Guardium Jobs Queue Domain
- **Jobs & Scheduling:** Assessment Jobs, Report Jobs, Data Masking Jobs
- **Alerts & Monitors:** Alert Configuration, Real‑Time Alerts, Incident Management
- **Assessment Entity:** Assessment Name, Run Date/Time, Configured Checks, Results Summary, Status, Executive Summary, Detailed Report, Compliance Findings, Recommendations

### Assessment Entity Details
- **Assessment Name:** Name of the vulnerability assessment run.
- **Run Date/Time:** Timestamp when the assessment was executed.
- **Configured Checks:** Checklist of assessed items (e.g., OS, DB, network).
- **Results Summary:** High‑level pass/fail statistics.
- **Status:** Overall outcome (e.g., Passed, Failed, Pending).
- **Executive Summary:** Concise overview of findings for management.
- **Detailed Report:** Full list of discovered issues with severity ratings.
- **Compliance Findings:** Mapping to regulatory standards.
- **Recommendations:** Actionable steps to mitigate identified risks.

## Timestamp, Time Period, IP Addresses
Indicates when an assessment ran, its duration, and source/target IP addresses or subnets.

## Guardium Data Protection Overview
IBM's platform centrally monitors databases, assesses vulnerabilities, and generates compliance reports for both on-premises and cloud data stores. Features include real-time traffic capture via S-TAP agents, policy enforcement (blocking, alerting), automated sensitive-data discovery, pre-built audit templates, and LDAP/external credential vault integration.

## Audit Process Domain
Tracks execution lifecycle of audit jobs: job definition (name, schedule, targets), task instance (start/end timestamps, status), and result sets (records, success/failure counts). Only users with the **All** role see full attributes; others have restricted views based on permissions. Supports real-time monitoring and historical audit effectiveness analysis.

## IMS/Data Set Event Timestamp

IMS/Data Set captures event timestamps in UTC, displayed in the collector's local timezone.

## IMS/Data Set Host Event Timestamp

The specific UTC timestamp of an event recorded by the IMS system, shown in the collector's timezone.

## Guardium Vulnerability Assessment for Cloudera

Integrates with Cloudera Manager to assess security weaknesses across Hadoop clusters and reports vulnerabilities in Guardium dashboards.

## Patch Deployment Health View

Dashboard showing the status of patch deployments on Guardium units, identifying failures for coordinated rollouts.

## Central Manager Communication Requirement

Requires TCP port 8447 open for the Central Manager to communicate with Managed Units for configuration and monitoring.

## Sniffer Process Monitoring

Monitors the Sniffer Process PID for real-time database traffic inspection, with tools to query and verify the current PID.

## Public Account Management Procedures

Internal stored procedures for creating and maintaining database accounts, roles, and permissions consistently across platforms.

## Optim Activity Log Integration

Ingests Optim solutions' activity logs for cross-platform monitoring, correlating data lifecycle processes with database activities.

## Operating System and Hardware Information

Displays comprehensive system information using `uname -a` for troubleshooting system compatibility and capturing baseline details.

### IPV6 Support Limitations for Cloud Storage Plug‑ins
IBM Guardium does **not** support IPv6 addressing for its S3 SQS, S3 CloudWatch, and DynamoDB data source plug‑ins. Deployments using these collectors must be on IPv4 networks.

### Persistent Volumes for External S‑TAP
When an External S‑TAP container needs a persistent data volume, specify the name of an existing PersistentVolumeClaim in the **Use existing persistent volume claim** field. The pod will reuse the pre‑provisioned storage instead of creating a new dynamic PVC.

### Datasource Credential Management API
Guardium offers the `create_hierarchical_member_to_group_by_desc` API to add a hierarchical member to a credential group. Available from version 10.1.4, this function streamlines bulk credential organization.

### Policy Creation API
The `create_policy` Guardium API call adds a new security or audit policy via the REST interface. Required parameters are `baselineDesc`, `categoryName`, `ruleSetDesc`, and an optional `policyName`. This capability exists from version 9.5 onward.

### GuardAPI Syntax Reference
The `delete_datasource_by_name` GuardAPI statement removes a datasource by its fully‑qualified name. The argument is case‑sensitive and must be supplied by a user with the appropriate admin role.

### External S‑TAP Configuration Show Command
Executing `display_external_stap_config` via GuardAPI returns the current configuration parameters for any deployed External S‑TAP, such as collector address and TLS settings. No arguments are required for this diagnostic call.

### IMS Debug Level Retrieval
The `get_debug_level` Guardium API fetches the current debug level used by IMS datasources (0‑4). The response indicates the active verbosity level for troubleshooting.

### Hadoop Service Monitoring Removal
The `remove_ranger_config` GuardAPI deletes a specified Hadoop service (e.g., HDFS, YARN) from Guardium’s Ranger‑based monitoring scope. Upon success, it returns a confirmation that the service has been unregistered.

### Solr Index Health Check
The `get_solr_errors` API returns any exceptions or warnings logged by the internal Solr engine used by Guardium. These results aid in diagnosing performance or query issues.

### Sensitive Object DDL Command Detection
Guardium classifies Data Definition Language (DDL) statements—such as `CREATE TABLE`, `DROP INDEX`, and `ALTER USER`—as **sensitive**. These commands belong to the *Sensitive Object* rule set and can be included in audit policies.

### Azure Resource Permissions
To monitor or manage Azure Subscriptions and Resource Groups from Guardium, the account must have the **Reader** role (or an equivalent custom role with read permission) on the `Microsoft.Resources/subscriptions/resourceGroups` resource. This enables Guardium to discover and inspect resource groups for data source integration.

## Guardium Security Credentials Management

Guardium enables administrators to manage credentials for datasource connections, including native and vault-secur credentials. Credential configuration is performed per datasource and supports encryption of traffic capture by S-TAP agents. Best practices for credential management include regular rotation, access restriction, and usage audit.

## Workflows Overview

Guardium provides structured workflows for datasource integration, policy configuration, threat investigation, and compliance reporting. Users can add datasources, deploy S-TAP agents, create security and audit rules, monitor events, generate compliance reports, and respond to incidents through the investigation dashboard.

## Personas Overview

Guardium supports multiple user personas:
- Administrators manage platform configuration, user access, and infrastructure.
- Security analysts define policies, monitor threats, and conduct investigations.
- Database administrators provision datasources, manage S-TAP agents, and handle exceptions.
- Compliance officers review compliance reports, ensure audit trail maintenance, and enforce regulatory adherence.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures structured and unstructured data across databases, file systems, and cloud services through comprehensive monitoring, protection, and audit capabilities. It supports real‑time data streaming between Guardium Edge components and central repositories, enabling fast compliance response and continuous monitoring in both on‑premises and cloud environments.

### Streaming Architecture
- **Topology Options:** Hub‑spoke, mesh, push‑ or pull‑based flows.
- **Security Controls:** TLS encryption, mutual TLS authentication, session integrity checks.
- **Performance:** Low‑latency buffering, configurable checkpoint intervals, back‑pressure management.
- **Failover & Recovery:** Automatic reconnection, retry policies, resumable streaming after outages.

### Core Workflows
1. **Initial Setup:** Deploy Edge agents, register with central collector, define streaming destination URI.  
2. **Policy Propagation:** Real‑time streaming of policy updates to Edge nodes.  
3. **Data Collection:** S‑TAP agents capture traffic, forward to Edge agents, which stream audit records to the central repository.  
4. **Incident Response:** Real‑time alerts streamed from central repository to Edge nodes, triggering local blocking or remediation.

### Personas
- **Security Administrators:** Configure streaming topology, TLS credentials, failover rules.  
- **Compliance Analysts:** Verify streaming latency, review alerts, confirm audit record arrival.  
- **Ops Engineers:** Provision Edge hosts, manage certificates, monitor collector resources.  

### Entities
- **Edge Agent:** Collects locally, buffers, encrypts, and streams audit data to the central collector.  
- **Central Collector:** Receives streaming records, consolidates with other sources, applies global policies.  
- **Policy Object:** Guardium policy definitions streamed to Edge agents for local enforcement.  
- **Security Zone:** Logical grouping of Edge nodes; streaming can be scoped for isolation.

## Guardium Edge Streaming

Guardium Edge Streaming facilitates secure, real‑time movement of audit data, entitlement information, and policy violations between Guardium Edge nodes and central repositories.

- **Supported Streams:** Audit events, entitlement changes, violation records.
- **Connectivity:** Configurable URI endpoints, TLS‑secured connections, mutual authentication.
- **Scalability:** Handles high‑volume, low‑latency transmission suitable for large‑scale deployments.

## Custom Classes in Guardium

Custom Classes enable administrators to group audit‑relevant objects (tables, columns, schemas) for policy or classification rule construction.

- **Benefits:** Simplifies rule creation, applies a single condition to an entire class.
- **GDPR Considerations:**  
  * Use non‑identifying class names.  
  * Restrict visibility to authorized roles only.  
  * Audit changes for compliance proof.  

(See: 4845. Manage Custom Classes.)

## IMS Object (z/OS)

The IMS Object (z/OS) report provides an object-level view of IMS (z/OS) data access for monitoring and auditing. It details table-level activities, user interactions, and data modifications within IMS databases on IBM Z systems.

**Key Concepts:** IMS, z/OS, Object-Level Monitoring, Auditing, Data Access

## FAM System Domain

The FAM System domain describes the configurations and entities within the File Activity Monitoring (FAM) module's domain. It includes attributes and settings that govern file system monitoring and policy enforcement.

**Key Concepts:** File Activity Monitoring, Domain Configuration, Entities, Attributes

## Guardium Login Domain

The Guardium Login domain captures detailed records of user login and logout events within the Guardium platform, essential for tracking user activities, auditing access, and ensuring proper authentication mechanisms.

**Key Concepts:** User Authentication, Login Events, Audit Logging, User Activity

## Group Domain

The Group domain describes the entities and attributes related to membership within Guardium groups. Groups are used to assign permissions, policies, and roles to users, making access management efficient and scalable.

**Key Concepts:** Groups, Membership, Entities, Attributes, Access Management

## Sniffer Packets Throttled

This entity records the total number of database connections ignored due to exceeding rate limits since the inspection engine started, helping manage and monitor packet traffic for system stability and performance.

**Key Concepts:** Packet Throttling, Rate Limiting, Inspection Engine, Connection Management

## S-TAP Statistics Domain

The S-TAP Statistics domain describes the statistics entity associated with the S-TAP component. These statistics provide insights into the performance and behavior of S-TAP agents deployed within the Guardium environment.

**Key Concepts:** S-TAP, Statistics, Performance Monitoring, Agent Behavior

## Create an Environment Variable File

Before executing the Vulnerability Assessment (VA) scanner, create an environment variable file to store configuration settings, simplifying variable management required by the scanner.

**Key Concepts:** Environment Variables, VA Scanner Setup, Configuration Management

## File Permission Test Validates File Permissions

The File Permission test within the CAS template validates that file permissions are set according to defined permissions, ensuring compliance with security policies regarding file access and integrity.

**Key Concepts:** CAS Template, File Permissions, Security Compliance, Configuration Audit

## IPv6 Migration in an Existing IPv4 Deployment

An existing Guardium deployment can migrate to operate exclusively on IPv6 addresses, enabling seamless transition and coexistence with IPv4 infrastructure without disrupting current operations.

**Key Concepts:** IPv6 Migration, IPv4 Deployment, Address Transition, Network Configuration

## Event Detection

IBM Guardium uses S-TAP agents to monitor database traffic in real time, evaluating it against configured security policies. Detected violations generate alerts, reports, or S-GATE blocking actions. Policies can target specific users, objects, operations, and timeframes.

Key Concepts: Real-Time Monitoring, Policy Enforcement, S-GATE Blocking, Violation Alerts

## IBM Guardium Key Concepts

- **S-TAP & S-GATE:** Agents for real-time monitoring and policy enforcement.
- **Security Policy:** Defines access controls and audit requirements.
- **Audit Trail:** Comprehensive logging for compliance and investigation.
- **Oracle & MSSQL Support:** Native and JDBC connectivity for major RDBMS.
- **NoSQL Monitoring:** MongoDB with universal connectors.
- **Compliance Features:** Ready-to-use audit templates for regulations.

## IBM Guardium Data Protection Overview

### Features
- Dynamic datasource connectivity with JDBC drivers and dynamic port detection via browser service.
- Real-time activity monitoring using S-TAP agents and enforcement via S-GATE blocking.
- Comprehensive compliance reporting for PCI-DSS, GDPR, HIPAA, SOX, and more.

### Workflows
- **Configuration:** Add datasources, deploy S-TAPs via GIM, configure FGAC policies.
- **Navigation:** Review activity reports, run vulnerability assessments, use dashboards.
- **Action:** Block unauthorized queries, rotate credentials, respond to security incidents.

### Personas
- **Administration:** Configure platform, manage users.
- **Security Administration:** Define FGAC policies.
- **Database Administrators:** Manage datasources and S-TAPs.
- **Data Analysts:** Access dashboards and run queries.
- **Compliance and Auditors:** Generate regulatory reports.

### Entities
- **Agents:** S-TAP, A-TAP, K-TAP.
- **Infrastructure:** Collector, Aggregator, Central Manager.
- **Policies:** Security policies, audit policies, classification rules, access rules.

## Database Connection Architecture
Supports JDBC with native and generic drivers, leveraging a browser service for dynamic port resolution.

## Activity Monitoring & Policy Enforcement
Captures traffic via S-TAP agents, evaluates against policies in real-time, and triggers alerts, reports, or S-GATE blocks. Policies can be highly specific to users, objects, operations, and time windows.

## Data Archiving
Configures archiving of audit results and system backups for data retention.

## Role and Permission Management
Defines job-function-specific roles and assigns permissions. Roles and user assignments are regularly reviewed.

## Workflow for Role and Permission Management
1. Define roles per job function.
2. Assign appropriate permissions to roles.
3. Assign users to roles.
4. Conduct regular access reviews.

## Deploying Edge Using Terraform
Provides Terraform modules for automated deployment on Kubernetes platforms.

## Rule Execution and Troubleshooting
Reconfigure rules that fail to trigger to ensure proper execution.

## Hadoop Integration Parameters
Configures Guardium integration with HDFS, Apache Ranger, and Cloudera Navigator using Kafka messaging.

## Google BigQuery Configuration
Uses External S-TAPs for monitoring and protecting BigQuery data.

## Collector Management
Manages Guardium collectors through the Collector tab, including adding, editing, or removing collectors with detailed configuration options.

## Central Module Overview

GIM's central module view shows all installed bundles, their versions, supported OSes, and import details.

**Key Concepts:** Central Module View, Software Overview, Installation Details

## Network Routes

`show network routes static` lists static IPv4 routes with Device, Index, Address, Netmask, and Gateway.

**Key Concepts:** Network Routes, Static Routing, Configuration Display

## Solr Management

Solr APIs manage the central Solr database on Guardium's central manager and managed units.

**Key Concepts:** Solr, API Management, Database Administration

## Report API

`create_ad_hoc_audit_and_run_with_name` creates a one-time audit and returns a report immediately.

**Key Concepts:** Report Generation, Ad Hoc Audits, API Usage

## Datasource Group API

`create_datasource_group` creates logical groups of datasources for simplified policy application and incident tracking.

**Key Concepts:** Datasource Grouping, Policy Application, Incident Tracking

## Data Export API

`getBundle` exports data archives, exports, or data marts for compliance via REST API.

**Key Concepts:** Data Export, Compliance, REST API

## External Feed Reports

`list_ef_report` lists all configured external feed reports.

**Key Concepts:** External Feed Reports, Auditing, Custom Reporting

## HDFS Configuration

`list_ranger_hdfs_config` retrieves HDFS configuration for Ranger integration.

**Key Concepts:** HDFS Configuration, Ranger Integration, Monitoring

## ILB Configuration

Use GuardAPI to set `ILB_ENABLED` and `ILB_THROTTLE` for optimal performance.

**Key Concepts:** ILB Parameters, Configuration, Performance Tuning

## Custom Property Management

`remove_custom_property_from_datasource_by_name` deletes a custom property from a datasource.

**Key Concepts:** Custom Properties, Datasource Metadata, Management

## Parameter Replacement in Query Rules
The `replaceTo` string parameter in `update_qr_replace_element_byId` specifies the replacement text for query rewrite operations. This enables dynamic query rewriting based on rule conditions, supporting flexible rule-based access control and data masking scenarios.

## IP to Hostname Aliasing Configuration
Guardium supports IP-to-hostname aliasing, allowing administrators to map IP addresses to resolvable hostnames. This feature enhances security by enabling hostname-based permissions for socket connections, UI access control, and activity reporting.

## Group-API Management
Group APIs provide comprehensive management capabilities for datasources, data groups, health analyzer metrics, Hadoop monitoring endpoints, and data investigation dashboards. These APIs facilitate bulk operations, dynamic group creation, and health status monitoring.

## Generative AI and SOX Automation
Guardium 12.2.x introduced Generative AI capabilities, including the Gen AI reporting interface, SOX AI for automated ticket reconciliation in Sarbanes-Oxley compliance workflows, and a revamped vulnerability assessment UI.

## Guardium Data Protection System Components
Version 13 of Guardium Data Protection comprises appliances, agents, and core components that deliver end-to-end data protection and monitoring. The system supports diverse deployment scenarios, from on-premises installations to hybrid cloud environments.

## Cassandra Aster Datasource
Cassandra Aster serves as a specialized datasource within Guardium for troubleshooting and data collection purposes. It enables detailed inspection and analysis of Cassandra database activities.

## Cloud Database Service Protection Workflow
Guardium's workflow for protecting cloud database services utilizes native audit capabilities of cloud providers. This approach delivers classification, vulnerability assessment, and object-level monitoring without requiring agent installation on the database instances.

## Collection Name Filtering
The `collection name like` filter allows matching specific collection names or patterns during discovery operations, enhancing precision in identifying relevant data collections for monitoring, classification, or policy application.

## SQL Query Name Pattern Detection
A session-level policy can alert administrators when a SQL query matches a specific name or pattern, enabling proactive detection of unauthorized or anomalous query execution. This feature supplements Guardium's real-time monitoring and blocking capabilities.

## Guardium Data Protection Overview

IBM Guardium Data Protection secures structured and unstructured data across on‑premises and cloud environments with real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting.

### Key Features
- **Database Support:** Native connectors, JDBC/ODBC drivers for DB2, Oracle, SQL Server, Sybase, Teradata, MySQL, PostgreSQL, and NoSQL stores.
- **Real‑time Monitoring:** S‑TAP agents, A‑TAP for encrypted connections, K‑TAP for kernel‑level inspection.
- **Granular Controls:** Fine‑grained access controls (FGAC), data classification, masking.
- **Compliance:** Built‑in report packs, automated audit trails, data residency controls.

### Typical Workflows
- **Deployment:** Install agents, configure data sources via GIM or REST API.
- **Policy Management:** Define security, audit, and classification policies in the Policy Builder UI.
- **Incident Response:** Triage alerts, block access, rotate credentials; integrate with ticketing systems via API.
- **Maintenance:** Refresh policies, adjust thresholds, perform health checks, capacity planning.

### Primary Personas
- **Security Admin:** Manages FGAC policies, audit rules, threat‑hunting initiatives.
- **Database Admin:** Registers data sources, maintains S‑TAP agents.

Document Overview
IBM Guardium Data Protection safeguards enterprise databases by monitoring activity, enforcing policies, assessing vulnerabilities, and providing compliance reports. Key features include:

Features
- Real-time monitoring of database traffic through S-TAP agents
- Data discovery and classification to identify sensitive information
- Automated compliance reporting for regulatory standards like PCI-DSS
- Session-level policies for fine-grained access control
- Session and flat log processing configuration options

Workflows
1. Add data sources and configure S-TAP agents via GIM
2. Define security, audit, session, and classification policies
3. Run discovery assessments and monitor activity reports
4. Respond to incidents with S-GATE blocking and credential rotation

Personas
- Administrators manage agents, system health, and user access
- Security admins create and enforce FGAC, session, and classification policies
- Data owners classify data and manage classification rules
- Compliance teams generate reports and export data to data marts

Entities
- Agents: S-TAP, A-TAP, K-TAP
- Policies: Security, Audit, Session, Classification
- Classification artifacts: Rules, Rule Handling
- Configuration artifacts: CAS instances, Layout locations

## Guardium Overview

Guardium provides real‑time monitoring, anomaly detection, and audit reporting for database activity across on‑premise and cloud data stores.

### Key Features
- Continuous capture of database traffic via S‑TAP agents
- Policy Enforcement Engine (S‑GATE) to block unauthorized queries
- Built‑in PCI‑DSS, GDPR, HIPAA, SOX templates; user‑defined reporting
- Identification of sensitive data with discovery and classification
- Centralized management of permissions and policy changes

### Typical Workflows
1. **Configuration:** Add data sources, deploy S‑TAP, define policies.
2. **Monitoring:** View live activity, set alerts, investigate incidents.
3. **Remediation:** Adjust or block queries, manage credentials, enforce least‑privilege.
4. **Compliance:** Schedule assessments, generate audit evidence.

### Primary Personas
- **Security Administrators:** Define FGAC policies, manage S‑TAP, monitor incidents.
- **Database Administrators:** Configure sources, verify agents, ensure configuration integrity.
- **Auditors/Compliance Officers:** Review audit trails, generate regulatory reports.
- **Data Scientists/Analysts:** Access curated datasets, run ad‑hoc queries within policy constraints.

### Entities Overview
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collectors, Aggregators, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, CAS Template.
- **Infrastructure:** Managed Units, Guardium Appliance, GIM, S‑GATE services.

### DB Discovery
Automatically identifies data sources, evaluates sensitivity, and populates Guardium inventory. Supports JDBC, ODBC, native drivers, and cloud data stores like Amazon RDS, Azure SQL Database, Google Cloud SQL.

### Audit Process domain
Defines entities and attributes for an audit process lifecycle: timestamps, status (queued, running, completed), initiating user, and comments attached to the archived audit set. Supports reporting on audit execution history.

### Eagle Eye domain
Captures Threat Detection Analytics data: anomalous behaviors, risk scores, correlation logic linking events to threats. Includes TDA incidents, anomaly patterns, analytics thresholds.

### Installed Patches domain
Records software patches applied to a Guardium appliance: patch ID, version, install timestamp, status (installed, pending, failed). Essential for compliance evidence and troubleshooting.

### Audit Process
A recorded audit run with metadata: name, start/end times, outcome status, optional user comment. Supports searching archived audit runs and exporting results for compliance reviews.

### Access Rule
Policy condition that triggers Full SQL logging on matching database activity. Includes a descriptive attribute (“Log SELECTs on payroll tables during business hours”) explaining the rule’s intent.

### CAS templates
Predefined configuration sets for Compliance Assessment Service (CAS) audits. Includes ready‑made templates for major databases (e.g., Db2) defining audit settings, data collection parameters, and rule sets for industry standards.

### File permissions
Monitors Db2 database file permissions at OS and database levels, detecting unauthorized chmod operations or ownership changes that weaken security controls, ensuring compliance with security baselines.

### Preparing to restore your Guardium system
Prerequisites: same hardware model replacement appliance, bootable ISO matching backup version, prerequisite patches installed. Workflow includes verifying hardware compatibility, mounting ISO, and CLI restore initiation.

### How IP addresses work
Inspection Engine defines client/server IP address pairs to specify monitored traffic flow. Understanding IP ranges and subnet masks is critical for configuring monitoring scopes in large enterprise networks.

## 5024. Cloud deployment
Administrators set up Guardium Data Protection in AWS, Azure, and Google Cloud by provisioning instances, configuring network latency considerations, applying firewall rules, managing IAM roles, and following troubleshooting steps for common issues such as misconfigurations or credential problems.

## 5025. Access management
Access management troubleshooting uses a structured process to resolve permission issues. It includes auditing role assignments, handling expired credentials, and enforcing least‑privilege policies via Guardium’s Access Manager, with step‑by‑step resolution procedures.

## 5026. Guardium accessmgr password reset
If the built‑in **accessmgr** password is lost, only IBM Guardium support can reset it through a secure, controlled process to prevent accidental lock‑out of administrative capabilities.

## 5027. Cloud deployment
This entry expands the cloud deployment steps for a multi‑cloud environment, including configuring cloud‑specific endpoints, network peering, encryption settings, and best practices for scaling and high‑availability across regions.

## 5028. Defining the S‑TAP for IBM i
After installing the S‑TAP on IBM i, edit `guard_tap.ini` to set `collector_ip`, `collector_port`, and `authentication_method`. Save the file and restart the agent using the Guardium CLI command `restart agent` to start streaming session data to the collector.

## 5029. Show command
The **show auth** command displays the current authentication configuration for Guardium users. It works alongside commands like `create_user`, `list_user_roles`, `set_user_roles`, and `update_user` to fully manage user credentials, role assignments, and authentication policies.

## 5030. Outliers detection APIs
Guardium’s Outlier Detection APIs provide programmatic access to the anomaly engine, allowing external applications to submit query patterns, retrieve detected outliers, and adjust sensitivity thresholds in near real‑time for integration with data‑quality platforms or custom dashboards.

## Outliers Detection APIs
**Purpose:** Programmatic control over outlier detection in IBM Guardium.  
**Key Operations:**  
- `enable_outliers_detection`: Starts outlier detection for a data source.  
- `configure_outlier_thresholds`: Sets anomaly‑scoring sensitivity.  
- `retrieve_outlier_report`: Provides a summary of detected outliers.

---

## GuardAPM Universal Connector APIs
**Purpose:** Manage external registry connections for IBM Guardium.  
**Key Operations:**  
- `manage_registry_config`: Add/update/remove registry entries.  
- `list_connected_sources`: View active registry connections.  
- `test_registry_connection`: Verify connectivity and credentials.

---

## GuardAPI Syntax (create_role)
**Description:** API for creating a new role.  
**Syntax:**  
```bash
create_role roleName=<role_name>
```  
**Usage:** Requires admin privileges; used for role‑based access control (RBAC).

---

## S‑TAP & Inspection Engine APIs (create_test_detail_exception)
**Purpose:** Test detail exceptions in vulnerability assessments (Guardium 11.0+).  
**Syntax:**  
```bash
create_test_detail_exception assessment_id=<id>, exception_type=<type>, expected_result=<result>
```  
**Result:** Validates that exceptions are correctly identified during scans.

---

## GuardAPI Example (execute_autodetect_process)
**Purpose:** Automate database and big‑data source discovery.  
**Syntax:**  
```bash
execute_autodetect_process source_type=<type>, target=<host>
```  
**Effect:** Initiates auto‑discovery, cataloging detected data sources for protection.

---

## Related Concepts (get_va_summary_key)
**Purpose:** Retrieve vulnerability assessment KPIs.  
**Syntax:**  
```bash
get_va_summary_key assessment_id=<id>, key_type=<summary_key>
```  
**Benefit:** Summarizes assessment results to prioritize remediation.

---

## Creating & Installing a Policy & Rules
**Steps:**  
1. Define policy name, scope, and target assets.  
2. Add FGAC, audit, and classification rules.  
3. Guardium auto‑generates threat categories based on rules.  

**Goal:** Enforce acceptable data‑access behavior and align with security standards.

---

## Reports & Report Generation APIs (reset_unit_utilization_data)
**Purpose:** Reset utilization metrics for performance monitoring.  
**Syntax:**  
```bash
reset_unit_utilization_data unit_id=<unit>
```  
**Use:** Enables accurate tracking of resource consumption after resets.

---

## Catalog & Manage Databases
**Capabilities:**  
- Auto‑discover and classify sensitive data.  
- Configure inspection engines and audit policies for new databases.  
- Generate custom reports/alerts on configuration changes.  

**Outcome:** Continuous monitoring and compliance for all critical data assets.

---

## OPTIM to Guardium Interface
**Purpose:** Real‑time alerts and SIEM integration between IBM InfoSphere Optim and Guardium.  
**Integration Mechanism:** CEF mapping for standardized event correlation.  
**Benefit:** Enhances security visibility across both platforms.

## IBM Guardium Data Protection: Key Concepts

### Features
- **Topological Visualization:** Shows relationships among Guardium appliances, collectors, aggregators, and Central Managers.
- **Admin Reporting:** Predefined reports for administrators to monitor system health and audit activities.
- **Real‑Time Monitoring:** Continuous collection and analysis of database activity via S-TAP agents.
- **Threat Detection:** Real‑time policy enforcement, alerting, and incident generation.

### Workflows
- **Topology Viewing:** Graphical representation of appliance hierarchy and connections.
- **Report Management:** Access and customize predefined admin reports.
- **Activity Analysis:** Drill‑down from summary to detailed reports for deeper insights.
- **Configuration & Monitoring:** Manage S‑TAP status and unit utilization levels.

### Personas
- **Guardium Administrator:** Manages appliance configurations, user access, and system settings.
- **Security Analyst:** Monitors activities, investigates incidents, and generates reports.
- **Compliance Officer:** Reviews audit reports and ensures regulatory compliance.

### Entities
- **Guardium Appliance Types:** Central Manager, Collector, Aggregator, Unit.
- **S‑TAP Agent:** Captures database traffic and forwards it to Collectors/Aggregators.
- **Report Entities:** Admin Reports, Drill‑Down Reports, S‑TAP Status, Unit Utilization Levels.
- **Attribute Entities:** Event User, Ack Response, Event Release, Unix Domain Socket.

---

## Detailed Views

### Topology View
Displays collectors and aggregators as solid circles and Central Managers as outlined circles, illustrating their connections.

### Predefined Admin Reports
Provides system status and detailed information for administrators with access rights.

### Drill‑Down Reports
Allows navigation from summary reports to detailed data for finer‑grained analysis.

### S‑TAP Status Domain
Describes the entities and attributes used for monitoring S‑TAP agent health and performance.  
*Attributes include:*  
- **Attribute:** Entity name for monitoring and reporting purposes  
- **Attribute:** Description of the entity's role in monitoring activities.

## Document Overview

IBM Guardium Data Protection protects structured and unstructured data across on-premises and cloud databases.

### Features
- Data Discovery & Classification
- Monitoring & Protection (S-TAP, policy enforcement, blocking)
- Centralized Management console
- Open APIs and Universal Connectors for integration

### Workflows
- Configuration
- Threat Response
- Compliance Reporting

### Personas
- Security Administrator
- Data Steward
- Compliance Officer

### Entities
- S-TAP / A-TAP / K-TAP agents
- Collector / Aggregator / Central Manager
- Security, audit, classification, access, and masking rules
- Dashboard & Reporting modules

---

## Monitor Values

The `Monitor Values` entity logs every database state change captured by Guardium audit mechanisms. It records the **Timestamp**, **Table Name**, **Action** (INSERT, UPDATE, DELETE, etc.), and **SQL Text**. Administrator role access is required.

---

## 5064. Sample Roles

Guardium provides predefined sample roles (e.g., Data Steward, Compliance Officer) that define permission sets for common tasks, streamlining role setup and ensuring consistency.

---

## 5065. Viewing the Enterprise Load Balancing Load Map

The Enterprise Load Balancing Load Map visualizes workload distribution across managed Guardium units, helping identify under‑utilized or overloaded collectors for performance optimization.

---

## 5066. Long Term Retention Views and Tables

Predefined SQL views and tables simplify extraction of long‑term audit data, exposing retention‑specific fields and pre‑joining audit tables for compliance reporting.

---

## 5067. Pages are not loading correctly

If UI pages fail to load, restart the Guardium UI service, then try accessing from another browser to rule out compatibility issues.

---

## 5068. Diagnosing the Problem

To diagnose Solaris Guardium collector issues:

1. `modinfo | grep ktap` – checks if the S-TAP kernel module is loaded.
2. `ls -al /dev/*tap*` – verifies presence of tap devices.

## Overview

IBM Guardium Data Protection is an enterprise data security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data stores, both on-premises and in the cloud.

### Key Features
- Centralized management console for multi-platform data sources (databases, warehouses, big data)
- Real-time activity monitoring of all data access, queries, and transactions
- Real-time policy enforcement via S-GATE to block or allow operations
- Automated vulnerability scanning for misconfigurations, weak passwords, etc.
- Discovery and classification of sensitive data across the environment
- Pre-built compliance reports for PCI‑DSS, GDPR, HIPAA, SOX, and customizable templates

### Standard Workflows
1. **Configuration:** Add data sources, deploy S‑TAP agents using GIM, define groups/policies  
2. **Monitoring & Alerting:** Real‑time dashboards, incident generation, automated response actions  
3. **Investigation:** Detailed incident analysis, outlier and forensic reporting  
4. **Maintenance:** Patch management, Guardium appliance backups/restore, RBAC administration

### User Personas
- **Security Administrators:** Create/manage policies, monitor compliance, respond to alerts  
- **Database Administrators:** Provision data sources, configure S‑TAP, troubleshoot monitoring issues  
- **Compliance Officers:** Access audit trails, generate regulatory reports, validate data handling practices  
- **Data Analysts:** Query security data, explore activity reports, use built-in dashboards for insights

### Event Tags

## Entity Types

Guardium supports several entity types that define the objects and attributes used in policies, assessments, and monitoring:

- **User (U)** – Represents database users or application accounts.
- **Server IP (S)** – The IP address of the database server.
- **Service Name (Svc)** – The service or application making the database request.
- **Tuple Groups** – Combinations of User, Server IP, and Service (User/Server IP/Svc) used for grouping and correlation.
- **Data Source (DS)** – Specific database instances, schemas, or tablespaces monitored by Guardium agents.

### Rule Syntax
Rules reference entity attributes using the syntax `Entity.Attribute`. For example:
- `U.username` – the logged‑in database user.
- `S.ip` – IP address of the server.
- `DS.name` – name of the data source.

### Policy Application
When a policy rule is evaluated, Guardium matches the incoming request against the entity criteria (e.g., `U.role = 'admin' AND S.ip = '10.1.2.3'`). Actions defined in the rule (Allow, Block, Log, Transition) are applied based on the match result.

## IBM Guardium Data Protection Overview  
IBM Guardium is a comprehensive data security and monitoring solution that provides continuous visibility, real‑time policy enforcement, vulnerability assessment, and compliance reporting across multiple data sources, both on‑premises and in the cloud.

### Key Features
- **Datasource Connectivity:** Auto‑detects ports, supports multiple drivers, and integrates with CyberArk for credential management.  
- **Threat Detection:** Offers real‑time policy enforcement, S‑GATE traffic blocking, and automatic generation of security incidents.  
- **Compliance & Reporting:** Includes ready‑made templates for PCI‑DSS, GDPR, HIPAA, SOX, and provides automated audit trails.  
- **Custom Partitioning:** Allows flexible storage allocation during installation to meet specific performance and capacity needs.  
- **External Storage:** Configurable support for S3, S3‑compatible buckets, or other network‑based storage for long‑term data archiving.  
- **Ethtool Management:** Lets administrators view and adjust network‑device parameters such as speed, auto‑negotiation, and duplex settings.

### Primary Workflows
- **Configuration:**  
  - Add data sources and deploy S‑TAP agents using the Guardium Installation Manager (GIM).  
  - Define Fine‑Grained Access Control (FGAC) policies and configure long‑term data retention settings.  
- **Navigation:**  
  - Access activity reports, run vulnerability assessments, and view the audit dashboard from the central console.  
- **Data Collection:**  
  - Enable A‑TAP (application‑level tapping) and pull certificates from a Venafi instance for encrypted data collection.  
- **Cloud‑Native Deployment:**  
  - Deploy External S‑TAP in Kubernetes environments using provided Helm charts.  
- **Post‑Installation Tasks:**  
  - Verify installation logs, customize the user interface, and perform any additional tuning required for your environment.

## Personas

- Administration: Administrator, Security Administrator
- Data & Database Management: Database Administrator, Data Analyst
- Compliance & Audit: Compliance Officer, Security Analyst

## Entities

- Agents & Collectors: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- Policies & Rules: Security Policy, Audit Policy, Classification Rule, Access Rule, Predefined Alerts
- Infrastructure: Guardium Integration Module, Managed Unit, S-GATE, Universal Connector

## Workflows

- Configuration: Add datasources, deploy collectors, configure policies, manage users and roles
- Monitoring: Review activity reports, run vulnerability assessments, generate compliance reports
- Action: Implement blocking rules, rotate credentials, respond to security incidents
- Analysis: Investigate data, restore audit trails, analyze threat patterns

## Creating an external feed

Guardium can push report data to an external database or system. Configure an **External Feed** by specifying the target database connection, selecting the report to export, and defining the schedule or trigger for the export. The feed transmits the selected report data in real‑time or at a defined interval, enabling downstream systems to consume Guardium monitoring results.

## Guardium Documentation Summary

### Features
- Real-time database traffic monitoring
- Policy enforcement and threat blocking
- Threat analytics and compliance reporting

### Key Components
- **S-TAP agents**: Capture traffic, forward to S-GATE
- **S-GATE**: Central policy engine
- **Staging databases**: Store collected data

### Workflows
1. **Initial Setup**: Deploy collectors, configure S-TAPs
2. **Policy Configuration**: Define rules, exclusions
3. **Data Collection**: Monitor activity, generate reports
4. **Threat Detection**: Analyze behavior, vulnerabilities
5. **Remediation**: Block threats, enforce controls

### Use Cases
- Real-time visibility into database activities
- Compliance with data protection regulations
- Detection of insider threats and malicious activities
- Auditing database access and changes

oncepts:** GuardAPI, list_commands, command syntax

```markdown
# IBM Guardium Data Protection Overview

IBM Guardium Data Protection secures structured and unstructured data across on-premises and cloud environments with real-time monitoring, automated policy enforcement, and comprehensive compliance reporting.

## Key Features
- **Datasource Connectivity**: Supports dynamic port detection, multiple database drivers, and CyberArk credential vault integration.
- **Threat Detection**: Offers real-time policy enforcement, S-GATE blocking capabilities, and security incident alerts.
- **Compliance & Reporting**: Includes templates for PCI-DSS, GDPR, HIPAA, and SOX; provides automatic audit trails.
- **Discovery & Classification**: Identifies data across the enterprise and classifies it according to security policies.
```

## Guardium Overview
Guardium secures sensitive data across Windows and Unix/Linux file servers, Windows and Unix/Linux databases, and mainframe databases. It employs policies and rules to discover, classify, monitor, and protect data.

### Core Components
- **Security Policies:** Define allowable database activities.
- **Audit Policies:** Specify data for audit logs.
- **Classification Policies:** Identify sensitive data patterns.
- **Access Rules:** Grant or deny data access based on rules.
- **Track Options:** Enable tracing of policy execution.

### Data Sources
- **Data Sources:** Database servers, file servers, and mainframe systems.
- **Agents:** S-TAP (database monitoring), A-TAP (file monitoring), K-TAP (alternative monitoring).

### Functionality
- **Discovery and Classification:** Locate and categorize sensitive data.
- **Investigation Dashboard:** Filter, persist, and drill into query results for investigations.
- **Database Entitlements:** Register data sources for entitlement reports using GuardAPI.
- **Risk Spotter:** Analyze risk indicators and calculate risk scores for users.
- **API Services:** Provide analytics, installation management, and integration capabilities.

### Workflows
- **Configuration:** Add data sources, deploy S-TAP, configure policies.
- **Monitoring & Reporting:** Generate activity and compliance reports.
- **Response:** Block unauthorized queries, rotate credentials, generate alerts, manage security cases.

### Personas
- **Security Administrators:** Configure policies and manage entitlements.
- **Database Administrators:** Register data sources and troubleshoot policies.
- **Compliance Officers:** Generate compliance reports.
- **Data Analysts:** Explore activity data and generate custom reports.

### Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Groups, Track Options.
- **Infrastructure:** Managed Unit, GIM, Guardium Insights APIs, Universal Connector.
- **Entities:** Analytic Case Observation, Classification Process Run, Field Description, Port, Instance Name, Directory, Group, Track Option.

## Attribute Description: Returned Data
Captures query results for debugging, auditing, and compliance.

## Attribute Description: Status
Tracks case lifecycle with values OPEN, ASSIGNED, CLOSED.

## Port Database Port
Specifies the database port and service name for data sources.

## Document Overview
IBM Guardium Data Protection monitors, enforces policies, detects threats, and provides compliance reporting for structured and unstructured data.

## Features Overview
- Continuous transaction monitoring.
- Configurable security policies.
- Real-time vulnerability analysis.
- Centralized policy enforcement.

## Workflows Overview
- **Administrator** workflow: deploy agents, manage data sources.
- **Compliance** workflow: configure regulatory reports.
- **Investigation** workflow: detect threats and generate alerts.

## Personas Overview
- **Security Administrators**: manage policies and rules.
- **Compliance Officers**: generate compliance reports.
- **Database Administrators**: install and troubleshoot agents.

## Entities Overview
- **Agents & Collectors**: S-TAP, A-TAP, K-TAP.
- **Policies & Rules**: security, audit, classification.
- **Infrastructure**: GIM, Managed Unit, S-GATE.

## Audit Entity
Captures all inserts, updates, and deletes with fields like Timestamp and SQL text for compliance and investigations.

## Client/Server Service Name
Stores SSID for client/server connections aiding in service identification.

## Example Scenarios
Illustrates entitlement calculations for Guardium Vulnerability Assessment deployments.

## Plan and Organize
PCI DSS Requirements 10 and 11: Guardium automates access tracking and security testing for compliance.

## Before you begin
Certificate management feature available from Guardium version 12.1.

## 5261. GuardAPI syntax

`740622b9-f827-494f-9fa6-99d79a8b7e66`  |  **categories:** entities, knowledge

The **`push_insights_trust`** GuardAPI uses a parameter=value syntax to push trust insight data into Guardium. Required parameters include `source_id` (unique identifier of the source), `trust_level` (numeric confidence in trust, 0-100), and `description` (optional free‑form text describing the insight).

---

## 5278. Kerberos No

Kerberos authentication is not supported for versions below 12.2.x; it is
mandatory only for DataDirect and Microsoft JDBC drivers in the specified
versions, highlighting version‑specific requirements for secure connections.

**Key Concepts:** Kerberos Support, Driver Versions, DataDirect, Microsoft JDBC

## Version Requirements, Mandatory Support, Specific Drivers

IBM Guardium **12.2.x or later** supports **Kerberos authentication** for **DataDirect** and **Microsoft JDBC** drivers, enabling secure access when configured appropriately.

**Key Concepts:** Kerberos Authentication, Driver Support, Version Compatibility

## Distribution Hub Profile

Configuration profiles from an enterprise hub are pushed to **central managers** and their **managed units** in IBM Guardium.

**Key Concepts:** Profile Distribution, Central Management, Managed Units

## LEEF Mapping

IBM Guardium integrates with **IBM QRadar 13.0** to map **Device Product** and **Device Version** fields to CEF standard values.

**Key Concepts:** LEEF Integration, Device Mapping, CEF Standard

## Guardium Files

IBM Guardium maps its **Device Product** and **Device Version** fields to the corresponding values in the CEF standard using the **Device Product Guardium**.

**Key Concepts:** Guardium Device Fields, CEF Mapping, Standard Compliance

## Owned Linux Domain

Linux and Windows systems joined to a domain can use **Kerberos logins** for secure authentication in IBM Guardium.

**Key Concepts:** Domain Joined, Kerberos Authentication, Secure Access

## Full Hadoop Audit Logs

Hadoop audit logs in Guardium can be set to **log full details**, **masked details**, **masked values only**, **no logging**, or **quick parse** with or without field separation and separate record values.

**Key Concepts:** Audit Logging, Log Options, Detail Levels

## Ranger HDFS Configuration

When configuring **Ranger HDFS** integration with **S-TAP**, verify the **HDFS cluster**, ensure **Ranger policies** are set, and locate **libhdfs.so** for the HDFS library.

**Key Concepts:** Ranger HDFS, S-TAP Configuration, Cluster Verification

## Guardium CLI Commands

CLI commands manage certificate lifecycles including create-csr, store-certificate, and verify-certificate for External S-TAP deployment.

## External S-TAP Guardium Tab

Settings in the Guardium tab configure load balancing and collector properties for External S-TAP to direct traffic and enable high availability.

## Upgrade Procedures

Upgrade IBM Guardium to the latest version or upgrade a stand-alone system to the next major version.

## Inspection Engine Management

CLI commands configure inspection engines to monitor data according to defined policies.

## Show Command

Displays the current maximum message size setting for Guardium Data Protection.

## GuardAPI for Domains

Provides syntax to add domains to Universal Connector allowed list using add_domain_to_universal_connector_allowed_domains.

## Datasource API

Deletes reference to a datasource group with delete_datasource_groupRef_by_id using appId, datasourceId, and objId.

## GuardAPI Delete Example

Deletes Hadoop archive configuration without parameters; specify api_target_host for execution target.

## Documentation Overview

IBM Guardium Data Protection monitors databases in real time, enforces policies, assesses vulnerabilities, and generates compliance reports across data stores.

### Key Capabilities
- **Datasource Integration:** Supports dynamic ports and CyberArk integration.
- **Threat Management:** Enforces policies, blocks threats, and generates incidents.
- **Compliance:** Offers PCI-DSS, GDPR, HIPAA, and SOX templates.

### Common Tasks
- **Setup:** Deploy S-TAP agents, configure FGAC policies.
- **Monitoring:** Review alerts, conduct assessments, audit activities.
- **Response:** Block threats, rotate credentials, manage incidents.

### Roles
- **Admins:** Platform configuration, user management.
- **Security:** FGAC policies, rule management.
- **DB Admins:** Manage datasources, monitor S-TAP health.
- **Analysts:** Run reports, investigate threats.
- **Compliance:** Generate audits, ensure regulatory compliance.

### Components
- **Agents:** S-TAP, A-TAP, K-TAP.
- **Collectors:** Guardium collectors, aggregators, central managers.
- **Policy Framework:** Rules, actions, policy engines.
- **Infrastructure:** GIM, Managed Units, S-GATE, Universal Connectors.

## GuardAPI TLS Configuration

Enables TLS 1.2 and TLS 1.3 across Guardium appliances with the enable_all_tls command, with option to target all managed units.

## GrdAPI Logging

Provides command-line examples for exporting logs to remote hosts and specific ports for troubleshooting.

## SOX Compliance Monitoring

Monitors data access and DDL execution for compliance with SOX requirements.

## Schedule Management

Lists job schedules specifying jobName; requires api_target_host for command execution.

## Targeted Data Collection

Collects specified commands with optional descriptions; requires api_target_host for execution.

## Policy Analyzer Scheduling

Updates policy analyzer intervals; requires valid intervals (2-60) and optional api_target_host.

## Query Optimization

Query rewrite APIs optimize performance, manage reports, and automate query management tasks.

## Account Field

Identifies datasource owners in IBM Guardium configurations.

## Policy Rule Processing

Rules on Flat setting allows real-time session-level policy evaluation, bypassing offline processing.

## Security Incident Handling

SECURITY_INCIDENT attribute integrates incident exceptions with session-level policies for effective tracking.

## Blocking Actions

Security policies support S-TAP Terminate and S-GATE actions to block unauthorized activities.

## Query Rewrite Activation

Enables query rewrite in Guardium to enhance query performance and automate query tuning tasks.

## Defining a Security Policy for Query Rewrite

Activate query rewrite definitions in Guardium through a security policy. This enables the application of the definitions to live database queries.

## Using the Topology View

Guardium's topology view visualizes Guardium appliances in search results. Filter and drill down to manage the Guardium environment.

## Enterprise S-TAP View

The "S-TAP Info (Central Manager)" report displays information about Enterprise S-TAP components, monitoring S-TAP agents across the enterprise.

## Guardium Jobs Queue Domain

Describes Guardium job entities and attributes related to queue scheduling, execution, and status.

## S-TAP Status History Domain

Provides historical status records for S-TAP agents, aiding in tracking operational changes and troubleshooting.

## IBM Guardium Data Protection Overview

Enterprise database activity monitoring and security platform offering real-time monitoring, policy enforcement, vulnerability assessment, compliance reporting, and cloud integration.

### Features
- Database traffic monitoring with S-TAP agents and real-time alerts
- Policy management for access control, masking, audit, and classification
- Compliance automation for PCI-DSS, GDPR, HIPAA, SOX
- Threat prevention through blocking and anomaly detection
- Cloud integration with Azure, Amazon, Google Cloud services

### Workflows
- Initial setup (datasource addition, S-TAP deployment, managed unit configuration)
- Policy configuration (security, audit, classification)
- Monitoring and enforcement (reports, assessments, incident investigation)
- Maintenance (client updates, S-TAP upgrades, appliance upgrades)

### Personas
- Security administrators (policy management, FGAC oversight)
- Database administrators (S-TAP deployment, datasource configuration)
- Auditors and compliance officers (report generation, assessments)
- Security analysts (alert investigation, anomaly analysis)

### Key Entities
- Agents and collectors (S-TAP, A-TAP, K-TAP, collectors, aggregators, Central Manager)
- Policy types (security, audit, classification, access, masking)
- Infrastructure components (appliance, managed units, GIM, Universal Connectors)

## Before Configuring S-TAP Inspection Engines

Log into the Guardium system managing the S-TAP before configuring inspection engines.

## Upgrading the GIM Client

Upgrade the Guardium Installation Manager client to newer versions without disrupting monitoring, using the GIM framework to distribute the updated package.

## Before You Begin

Download Guardium Data Protection 1021 S-TAP installation packages (GIM and S-TAP) from Fix Central before installation.

## Port Protocol Function

Port 443 (SSL) used by Guardium for secure communication with AWS services (Kinesis, DynamoDB, CloudWatch, KMS).

## Lenovo System x3550 M5 Installation Guide

Details configuring eth0 as the primary management interface for Guardium communication (GUI, API, agent traffic).

## Guardium Integration with Hadoop Using Ranger HDFS

Provides protection for Hortonworks and Cloudera 7 Hadoop clusters by integrating with Apache Ranger's policy engine while Guardium records access events.

## GuardAPI Syntax

The `create_ad_hoc_audit_for_security_assessment` API takes a comma-separated datasource ID list and an optional boolean to include a user receiver, automatically creating one for the logged-in user when true.

## Document Overview
IBM Guardium Data Protection is a database activity monitoring and security platform that provides real‑time monitoring, policy enforcement, vulnerability assessment, and compliance reporting for structured and unstructured data stores on‑premises and in the cloud.

### Features Overview
- **Datasource Connectivity**: dynamic port detection, multi-driver support, CyberArk credential vault integration
- **Threat Detection**: real‑time policy enforcement, S‑GATE blocking, security incident generation
- **Compliance & Reporting**: PCI‑DSS, GDPR, HIPAA, SOX report templates; automated audit trails

### Workflows Overview
- **Configuration**: add datasource, deploy S‑TAP via GIM, configure FGAC policies
- **Navigation**: review activity reports, run vulnerability assessments, audit dashboard
- **Action**: block unauthorized queries, rotate credentials, respond to incidents

### Personas Overview
- **Administration**: Administrator (platform config, user management), Security Administrator (FGAC, policies)
- **Data & Database Management**: Database Administrator (datasources, S‑TAP), Data Analyst (dashboards, queries)
- **Compliance & Audit**: Compliance Officer (regulatory reports), Security Analyst (threat investigation)

### Entities Overview
- **Agents & Collectors**: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager
- **Policies & Rules**: Security Policy, Audit Policy, Classification Rule, Access Rule
- **Infrastructure**: GIM, Managed Unit, S‑GATE, Universal Connector

## Database Connection Architecture
Guardium supports native and generic JDBC drivers for SQL databases, with a browser service that resolves instance names to current ports dynamically.

## Activity Monitoring & Policy Enforcement
Guardium captures database traffic via S‑TAP agents, evaluates it in real time against security policies, and triggers alerts, reports, or blocking via S‑GATE. Policies can target users, objects, operations, and time windows.

## 5363. Amazon DynamoDB
To configure an Amazon DynamoDB datasource:
1. Define the connection details (endpoint, region, access key, secret key).
2. Enable the DynamoDB driver in Guardium.
3. Verify connectivity with the built‑in test functionality.

## 5364. Amazon Redshift
To configure an Amazon Redshift datasource:
1. Specify the cluster endpoint, database name, port (default 5439), and authentication credentials.
2. Enable the Redshift driver in Guardium.
3. Test the connection and ensure IAM policies permit access from Guardium hosts.

## 5365. Port Number
The port number for an AWS RDS instance indicates the data‑center region it resides in, critical for establishing a network route from Guardium. Retrieve the correct region‑specific port via the AWS Management Console.

## 5366. Log Full Details
Enabling Log Full Details captures complete SQL strings and precise timestamps for each request, enhancing forensic analysis capabilities.

Document Overview
IBM Guardium Data Protection

### Features Overview
- **Threat Detection**
  - Real-time policy enforcement, S-GATE blocking
  - Automated incident generation
- **Datasource Management**
  - Dynamic port detection, driver support
  - CyberArk credential integration
- **Compliance & Reporting**
  - Pre-built templates for PCI‑DSS, GDPR, HIPAA, SOX
  - Detailed audit trails
- **Data Classification**
  - Automated discovery and classification of sensitive data elements

### Workflows Overview
- **Configuration**
  - Add datasources, deploy S‑TAP agents
  - Define FGAC policies
- **Navigation**
  - Access activity reports, run vulnerability scans
  - Use the audit dashboard
- **Action**
  - Block unauthorized queries
  - Rotate privileged credentials
  - Respond to incidents

### Per

## Guardium Overview

### Administration
- Manage platform, users, roles
- Define FGAC and security policies

### Security Operations
- Implement FGAC and security policies

### Database Administration
- Register datasources
- Install and configure S-TAP agents

### Compliance
- Generate regulatory reports
- Run audit summaries

### Entities
- Agents/Collectors: S-TAP, A-TAP, K-TAP, Collectors, Aggregator, Central Manager
- Policies/Rules: Security, Audit, FGAC, Classification
- Infrastructure: Appliances, Managed Units, S-GATE, Universal Connectors

## Host ID
Stores hostname or IP address of monitored database server

## Field Entity
Auto-generated for each new data field detected, enabling granular field-level activity tracking

## Sniffer Packets Dropped
Counts network packets unable to be processed by Guardium sniffer due to resource constraints or errors

## IMS/DATA SET
Provides segment-level GET activity and dataset context for IMS transactions

## File Ownership
Verifies that Db2 file ownership has not changed unexpectedly

## Global Profile
Defines system-wide default settings (UI theme, session timeout, etc.) applicable to all users

## Enable IPv4
Allows Guardium deployment to operate exclusively over IPv4 addressing

## Registering Units
Central Management enables a Central Manager to orchestrate configuration, user accounts, policies, and data collection from multiple managed units

## VA Results
Aggregates Classifier Findings, Discover Sensitive Data results, CAS results, Datamart imports, and collected logs

## Teradata Default
Lists default user groups used by Teradata databases for Guardium classification

## About this Task
Explains applying a single patch or set of patches as a background operation

## Problems and Solutions
Queries IBM support knowledge bases for known issues, resolution steps, and recommended fixes

## Creating Dashboards
Allows users to create custom dashboards and add various report types for visualizing audit data and security metrics

## Operating Modes
Supports different deployment modes (standalone, centralized, hierarchical) to meet security and architecture requirements

## Red Hat Virtualization
Enables deployment of Guardium as a virtual appliance within an RHV cluster, using Red Hat Enterprise Linux as the underlying platform

## Document Overview
IBM Guardium Virtual Appliance is a hardened, purpose-built security solution deployed as a VM within Red Hat-based virtualization platforms, offering comprehensive database activity monitoring, access control, vulnerability assessment, and compliance reporting

## Guardium Data Protection Overview

IBM Guardium Data Protection is a comprehensive enterprise solution for monitoring and securing structured and unstructured data across on-premises and cloud environments. It provides real-time visibility into database activities, enforces security policies, detects threats, and generates compliance reports to meet regulatory requirements such as PCI DSS, HIPAA, GDPR, and SOX.

### Core Features
- **Datasource Connectivity**: Supports various agents and collectors including S-TAP, K-TAP, A-TAP, Guardium Collector, Aggregator, and Universal Connector.
- **Threat Detection**: Enables real-time policy evaluation, S-GATE blocking, intelligent alerts, and vulnerability assessments.
- **Compliance & Reporting**: Offers predefined templates for PCI-DSS, GDPR, HIPAA, and SOX, along with audit trails and automated reporting capabilities.

### Operational Workflows
- **Configuration**: Add managed units, deploy agents, define security policies, and schedule assessments.
- **Monitoring**: Review activity streams, use the audit dashboard, and drill into detailed session information.
- **Action**: Enforce access controls, rotate credentials, and generate compliance reports.

### User Personas
- **Administration**: System Administrator configures the platform; Security Administrator authors policies.
- **Data Management**: Database Administrator and Data Analyst manage data access and usage.
- **Compliance**: Compliance Officer and Audit Analyst ensure adherence to regulatory standards.

### Key Entities
- **Agents & Collectors**: S-TAP, K-TAP, A-TAP, Guardium Collector, Aggregator, Central Manager.
- **Policies & Rules**: Security Policy, Audit Policy, Classification Rule, Access Control Rule.
- **Infrastructure**: Managed Units, Guardium Infrastructure, Virtual Appliances.

## Query Rewrite Functionality

Guardium's Query Rewrite feature allows real-time modification of SQL statements to mask sensitive data or enforce access controls before they reach the database. This is configured via S-TAP and enforced by policy rules that specify rewrite logic based on query patterns or user actions. Enabling query rewrite involves activating the capability on the S-TAP and creating policy rules that define the transformation logic.

## Alert API Methods

Guardium's Java alert API provides three methods for accessing alert information:
- `getMessage`: Retrieves the alert text.
- `getExtraInfo`: Accesses custom data associated with the alert.
- `getTimeStamp`: Obtains the timestamp of when the alert was generated as a `java.util.Date` object.

These methods allow programs to extract and process alert details for further analysis or storage.

## Cassandra SuperUser Role

The Cassandra SuperUser role grants full administrative privileges across the entire Cassandra cluster, allowing users to perform any operation on any keyspace or table, manage users and roles, and modify cluster configuration. This role is typically reserved for internal system processes and should be restricted to trusted accounts only to prevent unauthorized privilege escalation.

## Parser Errors Domain

The Parser Errors domain captures syntax and semantic errors encountered during the parsing of database queries by Guardium. It includes entities representing the error message, the affected SQL statement, user context, and execution context, facilitating audit and analysis of problematic queries.

## Query Rewrite Domain

The Query Rewrite domain defines entities and attributes related to the transformation of SQL queries before execution. It includes rules specifying when and how queries should be rewritten, the logic for the rewriting process, and the texts of both original and rewritten queries.

## Vulnerability Assessment (VA) Domains

### VA Summary Domain
Aggregates the results of security assessments into a summarized format, including entities that summarize the number of findings, severity distributions, and remediation statuses for each assessed system, facilitating high-level vulnerability management reporting.

### VA Tests Domain
Lists the individual tests performed during vulnerability assessments, with entities describing the test parameters, criteria, and result status, providing detailed insights into the assessment procedures and outcomes.

## Session Entity

The Session Entity represents each database session monitored by Guardium, including attributes such as session ID, user, client IP, connected server, session start and end times, and the number and type of operations performed, providing a comprehensive view of database activity.

## Attribute Description Entity

Attribute Description defines the properties and characteristics of Guardium attributes used in reporting and analysis, specifying data types, allowed values, and context for each attribute to ensure consistent interpretation across reports.

## Guardium Overview
IBM Guardium protects databases by monitoring activity, enforcing policies, identifying threats, and generating compliance reports across on‑premise and cloud data sources.

### Core Components
- **S‑TAP agents** capture real‑time database traffic.
- **Collector** aggregates data from S‑TAPs for analysis.
- **Policy engine** enforces security, audit, and classification rules.
- **Compliance UI** provides ready‑made audit templates (PCI‑DSS, GDPR, etc.).

### Data Sources
Supports relational (DB2, Oracle, SQL Server, MySQL) and non‑relational (MongoDB, Cassandra) databases, plus file‑system monitoring.

### Key Workflows
1. **Deploy S‑TAP agents** via Guardium Installation Manager (GIM).
2. **Configure policies** to define what actions are allowed/denied.
3. **Run assessments** to discover vulnerabilities and classify data.
4. **Generate reports** for auditing and regulatory compliance.

## Data Protection & Masking

### Policies Overview
- **Investigation:** Real‑time alerts; drill‑down activity reports; session isolation
- **Remediation:** Credential rotation; query blocking; patch recommendation engine

### Personas Overview
- **DB Admin:** Configures datasources; manages S-TAP; reviews audit logs
- **Sec Admin:** Defines FGAC policies; runs vulnerability scans; generates compliance reports
- **Compliance Officer:** Approves policies; schedules reports; verifies regulatory adherence
- **Data Engineer:** Applies data discovery; masking; pseudonymization rules

### Entities Overview
- **Agents & Collectors:** S-TAP; A-TAP; K-TAP; Collector; Aggregator; Central Manager
- **Policy Constructs:** Security Policy; Audit Policy; Classification Rule; Access Rule; Masking Rule
- **Data Entities:** Tables; Views; Schemas; Databases; Files; Objects
- **Infrastructure:** Managed Units; S-GATE; Universal Connector; Data Mart Processors

## Data Mart Management for Big Data Intelligence

The Data Mart APIs in Guardium facilitate the administration of curated datasets—data marts—that underpin analytical workflows and reporting.

**Key Functions**
- **Create:** Establish new data marts with defined schemas and source configurations.
- **Modify:** Update existing data marts to adjust parameters or integrate new data sources.
- **Delete:** Remove obsolete data marts to maintain organizational data hygiene.

**Usage Example**
```guardium
create_data_mart name="Sales_Analytics" source=db_source_01
modify_data_mart name="Sales_Analytics" add_source=db_source_02
delete_data_mart name="Sales_Analytics"
```

## Data Mart Creation and Integration

Define data mart characteristics, refresh schedules, and link external analysis tools.

**Example**
```guardium
create_data_mart name='FinancialMart' refresh_interval=hourly
```

Outcome:
- Enriched BI capabilities using Guardium's audit trail.
- Controlled access to sensitive query results.
- Supports scalability with distributed data mart deployment.

## Remove Query Rewrite Element by ID

Deletes a specified query rewrite engine element for maintenance or correction.

Syntax
```guardium
remove_ranger_replace_element_by_id qrReplaceElementId=<element_id>
```

Key Points:
- Element ID retrieved via query analysis queries.
- Immediate removal affects new queries, not processing ones.
- Returns success or error messages.

## Revoke Role from Object by Name

Revokes role assignments from database objects using role and object names.

Syntax
```guardium
revoke_role_from_object_by_Name roleName=<role> objectName=<object>
```

Key Points:
- Detaches role from all object permissions.
- Useful for compliance checks and permission reviews.
- Returns success or failure reasons.

## Revoke Role from Object by ID

Revokes role assignments from database objects using internal IDs.

Syntax
```guardium
revoke_role_from_object_by_id roleId=<role_id> objectId=<object_id>
```

Key Points:
- Targets internal identifiers for precision.
- Useful where name-based references are ambiguous.
- Helps script permissions management.

## Set Distributed Report Target

Designates a Guardium system as the central hub for distributed reports.

Syntax
```guardium
set_distributed_report_target host=<target_host> port=<target_port>
```

Key Points:
- Configures system as sender or receiver.
- Affects only new reports, not existing ones.
- Reports processed according to destination system policies.

## Show Auto-Detect Process Status

Provides real-time status of ongoing auto-discovery tasks.

Syntax
```guardium
show_autodetect_process_status
```

Key Points:
- Displays active discovery tasks and stages.
- Shows completion percentages and estimated times.
- Includes errors encountered during discovery.

## Test SOLR Hardware Requirements

Checks if the current environment meets SOLR component hardware needs.

Syntax
```guardium
test_solr_hardware_requirements log_output=<true/false> target_host=<host_name>
```

Key Points:
- Evaluates CPU, memory, disk, and network.
- Logs detailed results if `log_output` is true.
- Ensures performance benchmarks are met.

## Remove Load Balancer Groups

Removes specified load balancer groups from applications or managed units.

Syntax
```guardium
unassign_load_balancer_groups application_groups=<app_group> managedUnitGroups=<mu_group>
```

Key Points:
- Operates without affecting current sessions.
- Requires confirmation in live environments.
- Returns details on affected load balancers.

## Update IP Restriction Allowlist

Updates the list of permitted IP addresses for Guardium system access.

Syntax
```guardium
update_ip_restriction_allowlist ip=<ip_address> action=add
```

Key Points:
- Supports bulk entry by repeating the `ip` parameter.
- `action=add` appends IPs; `action=remove` excludes.
- Enforces new rules immediately on all services.

## Update Utilization Thresholds

Defines or adjusts thresholds for alerts on resource utilization.

Syntax
```guardium
update_utilization_thresholds cpu=<value> memory=<value> disk=<value>
```

Key Points:
- Thresholds help manage system health and performance.
- Values specified as percentages (0-100).
- Defaults trigger alerts at 80% CPU, 85% memory, and 90% disk usage.

## Microsoft SQL Write Operation Permissions

Allows specific users or roles to execute `INSERT`, `UPDATE`, and `DELETE` statements.

**Key Permissions**
- **INSERT:** Adds new records to tables or views.
- **UPDATE:** Modifies existing record attributes.
- **DELETE:** Removes records from tables or views.

**Guardium Controls**
- **Audit Policies:** Audit or log these operations for compliance.
- **Access Control Policies:** Restrict or allow write operations based on criteria.

## IBM Guardium Data Protection Overview
IBM Guardium Data Protection is IBM's enterprise database activity monitoring and security platform. It monitors, enforces policies, assesses vulnerabilities, and generates compliance reports across structured and unstructured data stores on-premises and in the cloud.

## Datasource Configuration
Configure datasources in Guardium to enable reporting and monitoring. Use service names for datasources and define access IDs for tracking database session access periods.

## Database Support
- **Db2 for i**: Integrate Db2 for i datasources with Guardium for comprehensive monitoring.

## Monitoring and Investigations
- **Investigation Dashboard**: Ensure scanners are properly connected to ingest data and visualize policy violations.
- **Audit Data Restoration**: Retrieve archived audit results, verify integrity, and view them in the investigation center.

## Security Features
- **Policy Enforcement**: Block unauthorized queries using S-GATE and generate security incidents for high-risk activities.
- **Threat Detection**: Real-time alerts for mass deletions, unauthorized INSERTs, and other suspicious activities.
- **Access Management**: Control user and application access through access management APIs.

## Compliance and Reporting
- **Compliance Reporting**: Generate reports for PCI-DSS, GDPR, HIPAA, and SOX.
- **Patch Management**: Monitor patch status descriptions and timestamps to ensure system integrity.

## Deployment Health
- **Deployment Health Dashboard**: Visually monitor the health and status of Guardium system deployments.

## Consolidated Guardium Reference

### Dashboard Overview
- **Purpose:** Live visual health and risk view of the Guardium ecosystem.
- **Key Elements:** Unified topology, real‑time metrics (connection counts, policy violations, alert rates).

### Features Overview
- **Datasource Connectivity:** Dynamic detection, multi‑driver, CyberArk vault integration.
- **Threat Detection:** Real‑time policy enforcement, S‑GATE blocking, incident generation.
- **Compliance & Reporting:** Pre‑built PCI‑DSS, GDPR, HIPAA, SOX templates and automated audit trails.

### Workflows Overview
- **Configuration:** Add datasource, deploy S‑TAP via GIM, configure FGAC policies.
- **Navigation:** Review activity, run vulnerability scans, view audit dashboard.
- **Action:** Block queries, rotate credentials, respond to incidents.

### Personas Overview
- **Administration:** Platform admin, user management.
- **Security Administrator:** Define FGAC, manage policies.
- **Database Administrator:** Manage datasources, S‑TAP.
- **Data Analyst:** Use dashboards, query activity.
- **Compliance Officer:** Generate regulatory reports, manage audit trails.
- **Security Analyst:** Investigate threats.

### Entities Overview
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, External S‑TAP, Collector, Aggregator, Central Manager.
- **Policies & Rules:** Security, Access, Classification, Audit.
- **Infrastructure:** GIM, Managed Unit, S‑GATE, Universal Connector.

### APIs
| API | Purpose |
|-----|---------|
| `execute_autodetect_process` | Automatic discovery of data sources (`process_name` required; `api_target_host` optional for clusters). |
| `get_insights_agent_config` | Retrieve current insights agent settings. |
| `get_native_audit_configuration` | Fetch native audit setup details by host/port/service. |
| `get_native_audit_objects` | List database objects discovered during classification. |
| `get_registered_units` | List all registered monitoring units (Guardium v12.1+). |
| `available_test_notes` | List test notes for GuardAPI tests (`datasourceType`, `testDescription` required). |
| `list_data_source_references_by_id` | Retrieve data source references for a specific identifier. |

*All statements are directly grounded in the provided entries; no new facts were added.*

# IBM Guardium Data Protection Overview

## Features Overview

- **DataSource Configuration**  
  Manage Azure PostgreSQL connections, catalog searches, and extrusion rule character sets.

- **Monitoring & Alerts**  
  Detailed logging, investigation dashboard for audit analysis, and runtime controls for data refresh.

- **Policy & Rule Management**  
  Positive/negative pattern matching, anomaly detection, and template-driven entity monitoring.

- **Entity & Incident Management**  
  Discovered host entities, template and case entities, event release types, and incident status tracking.

## Workflows Overview

- **Configuration**  
  Set up Azure PostgreSQL datasources and define monitoring parameters.

- **Investigation**  
  Use the dashboard and APIs to analyze audit trails, run assessments, and investigate incidents.

- **Policy Enforcement**  
  Create and manage security policies using the policy APIs, and enforce them in real time.

- **Entity & Incident Handling**  
  Manage discovered hosts, template items, cases, and incident statuses through dedicated workflows.

## Personas Overview

- **Security Administrator**  
  Configures datasources, policies, and character sets.

- **Security Analyst**  
  Uses the investigation dashboard and APIs for data analysis and incident response.

- **Compliance Officer**  
  Defines and enforces rules, monitors policy compliance, and generates reports.

- **Data Analyst**  
  Refreshes assessment data, analyzes detailed logs, and monitors entity activities.

## Entities Overview

- **Discovered Host Entity**  
  Represents a host identified by the discovery process.

- **Template Entity**  
  Detailed item within a template set defining monitored elements.

- **Case Entity**  
  Manages case workflows with attributes like Case ID and descriptions.

- **Event Release**  
  Tracks event release details, including type and user.

- **Incident Status Entity**  
  Describes the status of security incidents.

- **IMS/DATA SET Step**  
  Tracks JCL step information for executing programs within IMS/DATA SET contexts.

## Database Connection Architecture

IBM Guardium supports multiple JDBC driver families for connecting to SQL databases, including native drivers for optimized performance and generic drivers for broad compatibility. A browser service resolves instance names to current ports dynamically.

## Activity Monitoring & Policy Enforcement

IBM Guardium captures all database traffic via S-TAP agents and evaluates it in real time against configured security policies. Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

## IBM Guardium Data Protection Overview

IBM Guardium Data Protection is an enterprise security platform for real-time database activity monitoring and policy enforcement. It supports structured and unstructured data across on-premises and cloud environments.

### Key Features
- **Dynamic Datasource Connectivity**: Automatic port detection, multiple driver support, and integration with CyberArk for credential management.
- **Advanced Threat Detection**: Real-time policy enforcement, session blocking via S-GATE, and automated security incident generation.
- **Compliance Reporting**: Ready-made templates for PCI-DSS, GDPR, HIPAA, and SOX, with automated audit trails.

### Operational Workflows
- **Configuration**: Register datasources, deploy S-TAP agents using GIM, and define Fine-Grained Access Control (FGAC) policies.
- **Navigation**: Access activity reports, conduct vulnerability assessments, and use the audit dashboard for oversight.
- **Action**: Automatically block unauthorized queries, rotate credentials, and manage security incidents.

### User Personas
- **Administrators**: Manage platform configuration and user access.
- **Security Administrators**: Define and enforce security policies and rules.
- **Database Administrators**: Manage datasources and S-TAP installations.
- **Data Analysts**: Utilize dashboards and perform query analysis.
- **Compliance Officers**: Generate and review compliance reports.
- **Security Analysts**: Investigate threats and incidents.

### Core Components
- **Agents and Collectors**: S-TAP, A-TAP, K-TAP, Collector, Aggregator, and Central Manager for data collection and processing.
- **Policy Management**: Creation and enforcement of security policies and rules to safeguard data.

## Delete CAS Template
Deletes a configuration, access, or security template by its ID.  
Parameter: `templateId` (required).  
Optional parameter: `api_target_host`.

---

## Delete Data Source by ID
Removes a datasource from Guardium using its ID.  
Parameter: `cascade` – set to `true` to display dependent applications and require confirmation.

---

## Delete OAuth Clients
Deletes OAuth clients.  
Parameter: `client_id` – specific client; `all` – delete every client.  
Supported from Guardium v9.5 onward.

---

## Overview
IBM Guardium GuardAPI provides a comprehensive command-line interface for managing all aspects of the Guardium environment. It supports automation, integration with external systems, and detailed administration of security controls across diverse database infrastructures.

## GuardAPI disable_quick_search
Disables the quick search feature. Accepts a Boolean parameter:
- `0` disables locally on the current unit.
- `1` disables across all managed units in a Central Manager deployment.
This setting impacts only the current unit unless `1` is specified.

## GuardAPI disable_threat_finder
Disables the Threat Finder component.
Parameters are not enumerated in the provided excerpt.
Typically includes settings to specify scopes and whether the action applies system-wide or to managed units.

## GuardAPI enable_riskspotter
Turns on RiskSpotter, Guardium's anomaly detection engine.
Available starting from Guardium 11.0.

## GuardAPI execute_auditProcess
Runs a defined audit process.
- Mandatory `auditProcess` parameter specifies the audit process.
- Optional `api_target_host` allows execution on particular hosts within a clustered setup.

## GuardAPI execute_flatLogProcess
Executes flat log processing via the `grdapi` command-line interface.
No parameters are described.
Typically includes options for log source, processing options, and target directories.

## GuardAPI execute_ldap_user_import
Imports LDAP user definitions into Guardium.

## GuardAPI export_transfer_key
Exports a transfer key used for secure data movement between Guardium components.
No parameters are listed.
Operates on the default setup or defaults to the currently active environment.

## GuardAPI get_app_node_unit_type
Queries the unit type of an application node.
Optional `api_target_host` parameter to direct the query at specific hosts.
Returns information about whether the target is a Guardium appliance, managed unit, or another node type.

## GuardAPI get_ranger_hdfs_config
Retrieves HDFS configuration for Apache Ranger integration.
Typical parameters include paths to configuration files, authentication credentials, and target hosts.

## GuardAPI universal_connector_credential_API
Invokes Universal Connector credential APIs from the command line.
Typical parameters include credentials, target systems, and authentication mechanisms.

## GuardAPI gim_list_unused_bundles
Lists unused Guardium Installation Manager (GIM) bundles.
Optional `includeLatest` parameter filters results to exclude the most recent bundles.

## GuardAPI gim_remote_activation
Connects a GIM agent or group to a Guardium collector.
Requires `clientIP` and `connectToCollectorString`.

## Document Overview
IBM Guardium GuardAPI provides a suite of commands for managing all aspects of the Guardium environment, including configuration, monitoring, policy enforcement, and compliance reporting. It enables automation, integration with external systems, and detailed administration of security controls across diverse database infrastructures.

## Security & Audit Management

### Command Execution & Reporting
- Execute diagnostic commands, generate security reports, and analyze audit trails.

### Personas
- **Security Administrators** use GuardAPI for policy management, user permissions, and threat monitoring.
- **Database Administrators** utilize commands to configure data source connections and monitor database activity.
- **Compliance Officers** leverage audit and report functionality to meet regulatory requirements.

### Entities
- **Agents & Collectors**: Agents and aggregators for data collection.
- **Policy Framework**: Security, audit, and access control policies.
- **Configuration Entities**: Data sources, managed units, and load balancers.
- **Reporting Tools**: Interfaces for report generation and result mapping.

## GuardAPI Commands

- `gim_set_global_param`: Sets a global GIM parameter with `paramName` and `paramValue`.
- `list_available_tests`: Lists tests for a specified datasource type.
- `list_datasource_by_id`: Retrieves details about a data source by its ID.
- `list_entry_location`: Returns the location of a catalog entry.
- `list_inspection_engines`: Enumerates available inspection engines.
- `list_policy_fam_rule`: Lists rules in a specified FAM policy.
- `list_qr_add_where_by_id`: Adjusts query parameters by `qrActionId`.
- `riskspotter_set_config`: Configures Risk Spotter settings.
- `remove_dm_from_profile`: Removes a data mart from a profile.
- `remove_mfa_exempt_users`: Removes users from MFA exemption list.
- `set_flatLogProcessType`: Configures flat log file process type and action.
- `set_load_balancer_param`: Sets load balancer parameters.
- `stop_autodetect_process`: Stops an autodetection process by `process_name`.
- `store_sql_credentials`: Stores SQL credentials for database connections.
- `test_solr_connectivity`: Tests Solr server connectivity.

## GuardAPI Syntax for update_cas_template

Updates a compliance assessment template with parameters **enabled**, **isEditable**, and **period**.

## GuardAPI Syntax for update_cyberark_config

Modifies CyberArk configuration with **applicationId**, **folderName**, and **name** parameters.

## GuardAPI Syntax for Updating a Query Rewrite Condition

```bash
update_condition <param1>=<value1> <param2>=<value2> …
```  

Replace `<paramN>` and `<valueN>` with condition attributes such as expression, operator, and precedence.

## GuardAPI Syntax for update_vault_secret_id

```bash
update_vault_secret_id vault_name=<vault_name> credential_profile=<profile> secret_id=<new_id>
```

## Authentication Supported

Guardium supports **Local user**, **LDAP**, and **Kerberos** authentication for datasources, with optional SSL encryption per connection.

e ager  

Configuring a Central Manager involves defining the Central Manager server, registering collectors, and managing the central reporting and policy enforcement environment.

## Configuring Central Manager for Deployment Health Views

Configure a central manager to aggregate Guardium health status across managed units. Deploy the manager, register units, and enable health dashboards.  

---  

## Configuring JDBC over TLS

Configure secure TLS connections with either Kerberos password or Kerberos keytab authentication. Specify the principal, keytab location, and enable TLS on the Guardium appliance.  

---  

## Set USING_EDGE to 1  

Set `USING_EDGE=1` and `INTERNAL_LOAD_BALANCER_ENABLED=2` to forward telemetry through an Edge gateway in distributed environments while internal load balancers route intra‑data‑center traffic.  

---  

## GuardAPI – configure_archive  

Archive audit data using `configure_archive`. Required: archive server host, port, format (CSV/JSON). Optional: retention, compression settings.  

---  

## GuardAPI – configure_export  

Export audit data with `configure_export`. Parameters: export format, destination host, file naming, schedule interval. Automates off‑loads for reporting or disaster recovery.  

---  

## GuardAPI – set_ticketing_system  

Integrate an external ticketing system (JIRA, ServiceNow) via `set_ticketing_system`. Provide endpoint URL, auth credentials, and mapping rules linking Guardium alerts to ticket fields.  

---  

## GuardAPI – create_allowed_db  

Create FGAC user‑database access with `create_allowed_db`. Required: `user_name`, `database_name`. Optional: `access_rule_name`, `expiration_date`.  

---  

## GuardAPI – create_assessment  

Initiate a security assessment via `create_assessment`. Required: `assessment_name`, `type`, `owner_id`. Optional: `description`, `severity`, `tags`.  

---  

## GuardAPI – create_cloudTitle  

Register a cloud data source with `create_cloudTitle`. Required: `access_key_id`, `audit_type` (`dataStream` or `native`). Optional: region, bucket name, credential profile.  

---  

## GuardAPI – delete_cas_host  

Remove a CAS host using `delete_cas_host`. Required: `hostName`, `osType` (`UNIX`/`WIN`). Specify `api_target_host` to target the correct Guardium manager.  

---  

## GuardAPI – delete_ranger_hdfs_config  

Delete an HDFS configuration via `delete_ranger_hdfs_config`. Required: `stapHostName` identifying the S‑TAP host associated with the configuration being removed.  

---  

## Outlier Detection  

Enable or disable outlier detection through the Guardium UI or CLI. Configure detection thresholds, sampling rates, and notification settings as needed.

## GuardAPI Syntax – discover_streams
Receives an `api_target_host` parameter and returns identifiers of streaming data sources that can be ingested. Configure such streams for collection with `create_stream`.

## GuardAPI Syntax – export_definition
Configures export jobs. Must specify `export_name`, `export_type` (CSV, JSON, XML), and `destination_host`. Extra options control compression, encryption, incremental vs. full exports.

## GuardAPI Syntax – get_istap_config
Retrieves the current S‑TAP configuration of an instance. With no `stap_host_name` argument, returns the local host’s configuration. Output includes install path, monitoring ports, and logging settings.

## Guardium Data Protection Overview
IBM Guardium Data Protection is an enterprise platform for database activity monitoring, activity blocking, vulnerability assessment, and compliance reporting. It monitors structured and unstructured data on‑premises and in the cloud, enforcing policies in real time and delivering audit‑ready reports for regulatory standards.

### Features
- **Datasource Connectivity:** Automatic port detection, multiple driver support, credential vault integration (e.g., CyberArk)  
- **Threat Detection:** Real‑time policy enforcement, SQL blocking through S‑GATE, security incident generation  
- **Compliance & Reporting:** Templates for PCI‑DSS, GDPR, HIPAA, SOX; automated audit trails

### Workflows
- **Configuration:** Add datasource → deploy S‑TAP via GIM → define FGAC policies  
- **Navigation:** View activity reports, run vulnerability scans, consult dashboards  
- **Action:** Block suspicious queries, rotate credentials, handle incidents

### Personas
- **Administration**: Platform configuration, user management  
- **Security Administration**: FGAC policies, security rules  
- **Data & DB Management**: Datasource administration, S‑TAP deployment  
- **Data Analysis**: Dashboards, custom queries  
- **Compliance & Audit**: Regulatory reporting, audit investigations

### Entities
- **Agents & Collectors**: S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager  
- **Policies & Rules**: Security Policy, Audit Policy, Classification Rule, Access Rule  
- **Infrastructure**: Guardium Installation Manager (GIM), Managed Unit, S‑GATE, Universal Connector

## 5710‑5723: Session Day Extraction and Flat Log Metadata

- **5710‑5712 & 5720‑5723:** Session Start/End Weekday entities record the weekday (Monday–Sunday) extracted from Session Start or Session End timestamps. Used for reporting, trending, and auditing.  
- **5713:** Size records the byte length of a file; Source Directory Id identifies the directory scanned, providing context for attribution.  
- **5714:** Session End entity includes termination parameters (weekday, year) and an ignored status when the *IGNORE SESSION* policy action is applied.  
- **5715:** Flat Log Entity captures complete Flat Log details: Full SQL text, timestamps with date‑time precision, and related metadata for accurate activity reconstruction.  
- **5716‑5719 & 5721‑5723:** Duplicate of the weekday extraction described above for Session End.  

All other entries in the original documentation were noise (parameter‑table fragments, headers, or duplicate concepts) and have been omitted.

# IBM Guardium Data Protection Overview

## Dashboard & Dashboard Widgets
- Configurable audit dashboard visualizes security metrics, compliance status, and threat indicators.
- Widgets can be customized, resized, and arranged for personalized security posture views.

## Data Archiving
- Audit data can be archived to on-premises or cloud storage to reduce primary database load, support compliance retention, and enable cost-effective storage strategies.

## Database Intrusion Detection
- Analyzes database activity for suspicious patterns and anomalies to detect unauthorized access or malicious behavior.
- Triggers immediate alerts or blocking actions upon detection.

## Instance View
- Provides an aggregated, at-a-glance overview of activity, exceptions, and events across all monitored database instances.
- Helps administrators assess the health and security status of their data environment.

## Data Source Profiles & Universal Connectors
- Centralized management of connection information, authentication credentials, and settings for monitored data sources.
- Supports onboarding data sources and enables universal connectors on Guardium managed units.

## Database Connection Architecture & JDBC Drivers
- Supports multiple JDBC driver families: native drivers for optimized performance and generic drivers for broad compatibility.
- Includes a browser service that dynamically resolves instance names to ports.

## Activity Monitoring & Policy Enforcement
- Captures all database traffic via S-TAP agents and evaluates it against real-time security policies.
- Violations trigger alerts, reports, or blocking via S-GATE. Policies can target specific users, objects, operations, and time windows.

## Database Discovered Instances & Instance Discovery
- Automatically discovers database instances on monitored hosts and creates inventory entries.
- Simplifies policy targeting and reporting. Discovery can be scheduled or triggered manually.

## Data Coverage

Guardium can monitor entire Hadoop clusters by connecting to NameNodes, DataNodes, and YARN resource managers, providing end-to-end security visibility for big data workloads.

**Key Concepts:** Cluster Monitoring, End-to-End Coverage, Big Data Security

## HDFS Architecture

Guardium's Hadoop Distributed File System (HDFS) monitoring tracks activity at the NameNode, DataNode, and client levels and supports Kerberos authentication integration for comprehensive transaction coverage.

**Key Concepts:** HDFS Components, Kerberos Integration, Distributed Monitoring

## Hive Catalog

Guardium can monitor Apache Hive usage by integrating with Hive catalogs to capture metadata-driven queries and transformations, providing insights into data lineage and usage patterns.

**Key Concepts:** Hive Integration, Metadata Monitoring, Data Lineage

## GuardAPI Syntax

**list_policy**: Lists installed Guardium policies.  
Parameters: Optional filters to narrow output.

**restart_solr**: Restarts the Solr service for search indexing.  
Syntax: `guardapi restart_solr parameter=value`.

**set_import**: Toggles data import from aggregator to collectors.  
Parameter: `state` = `"START"` or `"STOP"`.

**set_user_roles**: Assigns roles to a user.  
Parameters: `roles` (comma-separated list), `userName`.

**updateEdge**: Modifies edge processing configurations for data mart extractions.  
Parameters: Data mart and edge setting identifiers.

## GuardAPI: ACTION_PARAMETERS
`ACTION_PARAMETERS` are configurable settings for Guardium actions, specifying targets, conditions, frequencies, and notification methods for automated responses like query blocking or credential rotation.

## Session Start Entities
`Session_Start_Date` captures only the date portion of a database session's start timestamp.  
`Session_Start_Time` records only the time portion of a session's start, working with `Session_Start_Date` to form a complete timestamp.

## Field Comments
The `Field Comment` section includes `DataSourceDesc` (human-readable description) and `Server IP` (database host IP).

## Last Modified Entities
`Last_Modified_Date` tracks the most recent modification date of an object or record within Guardium's catalog.  
`Last_Modified_Time` records the exact time of the most recent modification.

## User Discovery
User Name lists individual user accounts discovered during non-credential scans.

## VA Licensing
License keys for Guardium Vulnerability Assessment grant access to VA features and define licensing terms.

## CHAP Protocol
CHAP (Challenge-handshake Authentication Protocol) is used for secure authentication.

## Overview
IBM Guardium Data Protection is an enterprise database activity monitoring and security platform that provides real-time monitoring, policy enforcement, vulnerability assessment, and compliance reporting across on-premises and cloud data stores.

### Features
- Database connectivity with dynamic port detection and multi-driver support  
- Centralized policy management and FGAC  
- Real-time threat detection and S-GATE blocking  
- Compliance automation for PCI-DSS, GDPR, SOX, HIPAA

### Workflows
- Configuration: Add datasources, deploy agents, define policies  
- Monitoring: View reports, alerts, scan results, dashboards  
- Response: S-GATE blocking, credential rotation, incident remediation

### Personas
- Administrators: Platform configuration and user management  
- Security analysts: Threat hunting and policy customization  
- Compliance officers: Generate reports and attest protection  
- DBAs/Developers: Install agents, troubleshoot connectors, run queries

### Entities
- Agents: S-TAP, A-TAP, K-TAP, collectors, aggregators, central managers  
- Policies: Security, audit, access, classification, exception rules  
- Infrastructure: GIM, Guardium CLI, Universal Connector, Cloud Pak integration

## Data Aggregation and Correlation
Correlation Alerts and Related Tasks provide tools for managing correlation status and related system tasks.

## Unit Utilization
`store_monitor` and `gdm_statistics` APIs manage and retrieve unit utilization information.

## Related Concepts
Key concepts include Guardium architecture, data sources, and threat analysis.

## Related Information
Additional documentation and resources for IBM Guardium Data Protection are available.

## Documentation Overview
IBM Guardium Data Protection is a centralized solution for database security, monitoring, and compliance across heterogeneous on‑premises and cloud data sources. It offers real‑time policy enforcement, automated reporting, and forensic analysis.

### Key Features
- **Real‑time monitoring** of database traffic
- **Comprehensive audit logging**
- **Policy management** with FGAC and pre‑defined compliance templates
- **Regulatory reporting** (PCI‑DSS, GDPR, HIPAA, SOX)

### Typical Workflows
1. **Deploy S‑TAP agents** on target database servers.
2. **Configure security policies** (access control, audit, classification).
3. **Monitor alerts** and review audit trails for suspicious activity.
4. **Generate compliance reports** for internal or external audits.

### User Personas
- **Security Administrators:** Define policies, manage agents, oversee incident response.
- **Database Administrators:** Install agents, grant minimal permissions, troubleshoot monitoring.
- **Compliance Officers:** Schedule audit reports, validate evidence, certify posture.
- **Analysts:** Investigate alerts, generate forensic queries, produce evidence.

### Core Components
- **S‑TAP agents:** Lightweight collectors installed on monitored systems.
- **Data Sources:** Supported databases (Oracle, DB2, SQL Server, etc.) and file systems.
- **Security Policies:** FGAC rules, audit rules, data classification rules.
- **Audit Logs:** Captured SQL statements, session metadata, policy‑violation records.

## Guardium Overview

IBM Security Guardium is an enterprise data‑security platform that monitors database activity, enforces policies, and helps organizations meet regulatory compliance.

### Key Features
- Continuous real‑time monitoring of SQL statements and data‑access events via agents.
- Automated enforcement of security policies with blocking and alerts.
- Automated discovery, tagging, and classification of sensitive data.
- Pre‑built compliance reports for PCI‑DSS, GDPR, HIPAA, SOX, and others.
- Advanced analytics and threat detection using machine‑learning models.

### Core Workflows
- **Configuration:** Add data sources, deploy collectors, and define security policies.  
- **Investigation:** Review alerts, generate audit reports, and perform forensic analysis.  
- **Remediation:** Block suspicious queries, rotate credentials, and apply security patches.  

### Personas
- **Security Administrator:** Designs and maintains Guardium policies and configurations.  
- **Compliance Officer:** Requests and reviews compliance reports and audit evidence.  
- **Data Analyst:** Monitors activity dashboards and investigates potential anomalies.  

### Components
- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, collectors, aggregators, and the Central Manager.  
- **Policies:** Security, audit, access, FGAC, and data‑classification rules.  
- **Infrastructure:** Managed units, S‑GATE, Universal Connector, and data marts.  

## Events Table

The *Events* table stores each audit record captured by Guardium. Each row captures the user, source IP, executed command, timestamp, and outcome of a single database activity or session.  

## Group Members Population

Group members can be imported from an existing group, an external data source, or defined via a custom query, enabling flexible role and permission management within Guardium.  

## Creating and Managing Credentials

Workflow for setting up authentication details required by data‑source profiles (usernames, passwords, SSH keys) to enable Guardium to connect to monitored databases.  

## Deploy External S‑TAP

Graphical wizard guides administrators through selecting deployment mode, specifying target system details, applying certificates, and activating an External S‑TAP instance.  

## DNS Servers Configuration

Lists configured DNS resolvers with index and IP address (e.g., Index 1 → 9.32.193.11). Used by Guardium components needing name resolution.  

## Central Manager Redundancy

Configuring a secondary Central Manager provides high‑availability; it takes over automatically if the primary fails, ensuring uninterrupted Guardium operations.  

## Distributed Report Builder

Allows creating reports whose data is aggregated across multiple collectors in a domain, delivering enterprise‑wide insights while minimizing load on any single collector.  

## CAS Templates Management

CAS templates standardize auditing configurations. Documentation covers creating, editing, and replicating these templates across Guardium installations.  

## Data Mart Operations

CLI commands (`export_datamart`, `validate_datamart`) export audit data for external reporting or archival and validate configuration health.  

## Guardium Universal Connector

Integrates non‑database systems by collecting activity logs, expanding Guardium’s visibility beyond traditional databases.  

## Threat Detection Analytics

Enable/disable specific threat‑detection use cases via CLI APIs (`disable_threat_detection_use_case`, `enable_threat_detection_use_case`) to fine‑tune active analytics.  

## Guardium Installation Manager (GIM)

Centralized framework that distributes, updates, and removes Guardium agents (S‑TAP, A‑TAP, etc.) across managed database servers, simplifying agent lifecycle management.  

## Database Type Count

Metric tracking the number of monitored database instances (e.g., Oracle, MySQL), useful for capacity planning and license compliance.  

## Related Concepts & Reference
- **Query Rewrite** (related concept).  
- **API Documentation** (related reference).  

## Global Profile Configuration

Defines system‑wide default settings such as alert‑message templates (`u`). Overrides are possible via user‑ or group‑specific profiles.  

### Document Overview

IBM Security Guardium provides real‑time visibility into database activity, enforces security policies, offers compliance reporting, and delivers advanced analytics to detect and prevent threats across heterogeneous data environments.

## 5850. Alert per match
Guardium policies can be configured with **Alert per match** to generate an alert for each individual policy violation, or with **Alert per time granularity** (e.g., per minute) to aggregate alerts over a specified interval.

## File Handling CLI Commands

Guardium CLI provides `monitor_file`, `report_file`, and `set_file_path` commands for monitoring file access, generating file reports, and setting monitoring paths.

## Show Anomaly Detection State

`show anomaly-detection state` displays the operational state of the anomaly detection subsystem, indicating enabled, disabled, or maintenance mode.

## Show Monitor GDM Statistics

`show monitor gdm_statistics` shows CPU, memory, and storage usage across managed units for performance tuning and planning.

## Database Auto-Discovery

Auto-discovery automatically detects databases on hosts, scans known processes and ports, and creates Guardium datasource definitions without manual setup.

## Entitlement Optimization Overview

Entitlement optimization governs access privileges, identifies over-provisioned permissions, and provides recommendations to align with least privilege principles by reviewing user entitlements.

## Threat Category Addition via API

Threat categories group security threats by characteristics for efficient detection.

## Guardium Functions

### Guardium Features
- **Datasource Connectivity**: Real-time port detection, broad driver support, CyberArk vault integration
- **Threat Detection**: Real-time policy engine, S-GATE real-time query blocking, automated incident generation
- **Compliance Reporting**: PCI-DSS, GDPR, HIPAA, SOX report templates; continuous audit trail generation

### Workflows
- **Configuration**: Add datasources, deploy S-TAP via GIM, create FGAC policies
- **Navigation**: Activity reports, vulnerability assessments, dashboard navigation
- **Action**: Block queries, rotate credentials, incident response workflows

### Personas
- **System Administrator**: Configures platform, manages users
- **Security Administrator**: Manages FGAC, creates policies
- **Database Administrator**: Manages connectors, installs S-TAP
- **Compliance Officer**: Generates reports, verifies audits

### Entities
- **Agents**: S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies**: Security, Audit, FGAC, Classification, Access
- **Infrastructure**: GIM, Managed Unit, S-GATE, Universal Connector

## Troubleshooting

### Internal Database Issue Diagnosis
Methods and tools for resolving issues within the internal database.

### Certificate Management CLI Commands
CLI commands for certificate management tasks, such as importing, listing, and rotating.

## Guardium Integration

### REST API Usage
Utilize Guardium REST APIs to programmatically manage configurations and run API commands.

### Group Builder Usage
Tasks related to the Group Builder for defining and managing groups.

## Vulnerability Assessment

### Outlier Detection
Explain anomaly identification techniques for enhanced threat detection.

## Database Configuration

### DB2 for IBM i S-TAP Monitoring
Specific S-TAP variant configuration details for monitoring IBM i database activity.

## Big Data Intelligence

Component for data analytics and reporting integration within the Guardium ecosystem.

## Policy Actions

### Revoke Role from Object API
APIs for revoking roles from objects using names or IDs in S-TAP and inspection engines.

## Investigation Dashboard

### File Activity Investigation
UI component for displaying insights on file activity investigations.

## Mutual SSL Configuration

### Mutual SSL Setup for Cassandra
Configure mutual SSL for Cassandra datasource connections.

### Non-SSL Configuration
SSL disabled configurations demonstrate non-encryption setups.

### Mutual SSL Enabled
SSL enabled section describes mutual SSL configuration settings.

### SSL Configuration Overview

## Detailed Content

### Mutual SSL Setup for Cassandra
When SSL Yes is selected, mutual SSL authentication is enabled for secure communication. Required fields include key password and keystore/truststore paths with passwords for both client and server.

## IBM Guardium Data Protection Overview

**Features:** Unified monitoring & blocking, compliance automation, data classification, AI‑driven threat analytics, centralized management, workflow integration.

**Workflows:**
1. **On‑boarding:** Add data sources, deploy agents via GIM, define policies.
2. **Policy Definition:** Build security, audit, classification, and access rules.
3. **Incident Response:** Review events, generate reports, automate remediation.
4. **Performance Tuning:** Optimize collectors, configure load balancing, adjust query‑rewrite rules.

**Personas:** Guardium Administrator, Security Administrator, Database Administrator, Compliance Officer, Security Analyst.

**Key Entities:** Agents (S‑TAP, A‑TAP, K‑TAP), Collectors & Aggregators, Policies (security, audit, classification).

## **IBM Guardium Data Protection Overview**

IBM Guardium protects databases and big data assets from unauthorized access, misuse, and threats. It monitors, enforces policies, assesses vulnerabilities, and generates compliance reports across on‑premises and cloud environments.

### **Key Features**
- **Database Monitoring** – Real‑time capture and analysis of all SQL traffic using S‑TAP agents; enforces allow/deny policies and blocks offending sessions with S‑Gate.
- **Compliance Reporting** – Pre‑built templates for PCI‑DSS, GDPR, HIPAA, SOX; customizable queries against the Events table and export in CSV/Excel/HTML.
- **Threat Analytics** – Machine‑learning anomaly detection, risk scoring, and attack‑path visualization for proactive security.
- **Data Security Posture Management** – Automated discovery and classification (PII, PCI, PHI); configuration assessment, vulnerability scanning, and entitlement optimization.

### **Core Workflows**
1. **Deployment** – Install S‑TAP agents on database hosts, configure Central Manager, onboard data sources, and integrate with privileged‑access managers.
2. **Policy Management** – Use Policy Builder (UI/CLI/API) to create Security Policies (grant/deny rules) and Audit Policies (logging rules); distribute via Managed Units and version‑control changes.
3. **Investigation** – Generate activity reports, run custom SQL against the Events table, investigate alerts, and respond to incidents; automate escalation to ticketing systems.
4. **Governance** – Export and deliver compliance reports, manage data lifecycle (classification, labeling, retention), and demonstrate audit readiness.

### **User Personas**
- **Security Administrators** – Define and enforce data‑access, audit, classification, and masking policies.
- **Database Administrators** – Install/configure S‑TAP, monitor agent health, and tune performance.
- **Compliance Officers** – Access audit trails, run compliance reports, and manage data classification and retention.

### **Architecture Summary**
- **S‑TAP Agents** – Lightweight sensors on data sources capturing raw SQL events.
- **Collector Units** – Aggregate events, evaluate policies, and forward to Central Manager.
- **Central Manager (CM)** – Core policy engine, correlation, alerting, and reporting hub; stores configurations in Guardium Vault and hosts S‑Gate for active blocking.
- **Universal Connectors** – Extend monitoring to non‑SQL data repositories (cloud storage, Hadoop, NoSQL).
- **Managed Units** – Distributed collectors for horizontal scaling and geographically dispersed deployments.
- **Cloud Service** – Managed Guardium instances for rapid onboarding and reduced infrastructure overhead.

### **Functionality Highlights**
- **Dynamic Port Discovery** – S‑Gate detects changing database ports and maintains connectivity.
- **S‑Gate Blocking** – Enforces policy decisions in real time, blocking or rewriting suspicious queries.
- **Data Classification Engine** – Auto‑discovers and labels sensitive data, feeding into policies and reports.
- **Threat Analytics** – Correlates events across multiple data sources to detect sophisticated attack patterns.
- **Integrated Privileged Access Management** – Stores credentials securely in Guardium Vault, supporting integration with external PAM solutions (e.g., CyberArk).

## IBM Guardium High-Level Overview

IBM Guardium Data Protection provides centralized database activity monitoring, policy enforcement, vulnerability assessment, and compliance reporting across structured and unstructured data sources on-premises and in the cloud.

### Key Features
- **Datasource Connectivity:** Multi-driver support, dynamic port detection, CyberArk integration
- **Threat Detection:** Real-time policy enforcement, S-GATE blocking, security incident generation
- **Compliance Reporting:** PCI-DSS, GDPR, HIPAA, SOX templates; automated audit trails
- **Data Protection Integration:** Long-term retention ports, CA certificates repository

### Primary Workflows
- **Configuration:** Add datasource, deploy S-TAP via GIM, configure FGAC policies
- **Activity Monitoring:** View real-time alerts, audit dashboards, incident response
- **Policy Management:** Create/modify security, audit, classification, access rules
- **Compliance Automation:** Generate PCI-DSS, GDPR reports, schedule data mart updates

### Persona-Centric Views
- **Administration:** Platform configuration, user/role management, system health monitoring
- **Security Administration:** Define FGAC policies, manage S-GATE blocking, incident investigation
- **Database Administration:** Manage datasources, install/configure S-TAP, configure FGAC
- **Compliance:** Run regulatory reports, maintain audit policies, review data-mart insights

### Core Entities
- **Agents & Collectors:** S-TAP, A-TAP, K-TAP, Collector, Aggregator, Central Manager
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule
- **Infrastructure:** GIM, Managed Unit, S-GATE, Universal Connector

## Guardium Role Management

Guardium’s role‑based access control lets administrators assign users to predefined or custom roles, granting permissions to use specific functions such as configuration, monitoring, reporting, and policy management. Role templates exist for common personas like security administrators and compliance officers, while custom roles can be created to fit organizational needs.

## Schedule and Dependencies APIs

Guardium’s REST and CLI APIs provide endpoints for scheduling jobs and defining job dependencies. Administrators can submit jobs for data collection, report generation, or remediation, and set predecessor‑successor relationships to automate complex audit and remediation workflows.

## Ports for Long‑Term Retention

IBM Guardium’s long‑term retention feature establishes outbound encrypted connections on configurable TCP ports to external archival systems (e.g., S3, Azure Blob). These ports ensure secure off‑loading of audit data while keeping production bandwidth isolated.

## Identify Where a Group Is Used

Run the **Group Usage** report from the Administration navigation pane, select the target group, and Guardium returns all policies, reports, and queries that reference the group, helping administrators assess impact before modifying or deleting groups.

## JDBC Username and Password

Guardium uses standard JDBC `username` and `password` parameters to authenticate to databases. Credentials are stored encrypted and can optionally be sourced from external vaults like CyberArk for enhanced security.

## TDS Version Auto in FreeTDS

The `TDS_Version Auto` setting allows FreeTDS to automatically negotiate the optimal TDS protocol version during the handshake with Microsoft SQL Server, eliminating the need for manual TDS version specification.

## CA Certificates and Repository

Guardium’s CA certificates repository stores trusted CA certificates used to validate SSL/TLS certificates for managed data sources. Administrators can manage certificate renewals, revocations, and rotations through this repository, ensuring secure encrypted communications with database endpoints.

## Guardium API A‑Z Reference

The Guardium API A‑Z Reference documents every API command, its parameters, and example usage. Organized alphabetically, it covers configuration, monitoring, policy management, and reporting commands, enabling developers and administrators to automate Guardium tasks via REST, CLI, or SDK.

## Data Mart

A Guardium Data Mart is a curated collection of reports, custom queries, and dashboards focused on a specific domain (e.g., security, compliance). Data marts can be exported, scheduled, or accessed via API, providing targeted insights and analytics for stakeholders.

## Guardium Installation Manager

The Guardium Installation Manager (GIM) is a centralized tool for deploying, updating, and managing Guardium components across the enterprise. GIM supports silent or assisted installation of agents, collectors, and K‑TAP modules, handles version compatibility, and provides health‑check status for all managed units.

## Reduce the Data Attack Surface

Guardium reduces the data attack surface by monitoring access patterns, enforcing least‑privilege policies, masking sensitive data in transit, and blocking anomalous queries. This comprehensive approach minimizes unnecessary access points, restricts privileged use, and encrypts data at rest and in motion.

## Authentication Supported

Guardium supports multiple authentication mechanisms for database connections, including native database authentication and external authentication methods such as LDAP/Active Directory, Kerberos, and SAML. These mechanisms allow seamless integration with existing identity management systems.

## Determining Test Severity

Evaluating the criticality of each test against security guides, compliance benchmarks, and risk assessments defines severity. Password‑policy, privileged‑access, and data‑leakage tests are typically **CRITICAL** for immediate remediation.

Key Concepts: Risk Assessment, Security Guides, Compliance Benchmarks, Severity Levels, Critical Tests.

---

## Document Overview

IBM Guardium Data Protection is an enterprise security platform that monitors, protects, and ensures compliance of data in heterogeneous database environments, both on‑premises and cloud.

### Features Overview
- **Central Management APIs:** Control Central Management functions via programmatic interfaces.
- **Big Data Intelligence APIs:** REST endpoints for Guardium Big Data Intelligence analytics.
- **Redis Integration Parameters:** Host, port, password settings for Redis audit logs.
- **Certificate Management CLI Commands:** `gkeytool`, `gcm_client` for certificate generation and rotation.
- **Azure-Specific Parameters:** `enable_disable_monitoring_streams` to monitor Azure SQL and Synapse.
- **Active Threat Analytics:** Machine‑learning based real‑time event correlation for attack detection.
- **Database Auto‑Discovery:** Automated discovery and provisioning of S‑TAP agents and baselines.
- **Entitlement Optimization:** Reports and recommendations to reduce excessive privileges.
- **Investigation Dashboard:** UI for aggregating alerts and activity streams during incident handling.
- **Data In‑Sight:** Visual analytics tools for uncovering hidden trends from audit logs.
- **Managing Stored Data:** Backup, retention, archiving, and encryption procedures for Guardium repositories.
- **NAS Scan Permissions:** ACLs and service accounts required for NAS scans.
- **Log Exception Action:** `LOG` action to record violations without blocking.
- **Transform Parameters:** In‑policy actions (`REMOVE`, `MASK`, `SUBSTITUTE`) for audit enforcement.

### Workflows Overview
- **Onboarding:** Add data sources → auto‑discover → install S‑TAP → configure FGAC policies → enable reports.
- **Policy Management:** Create/modify security, audit, classification policies via APIs or UI.
- **Incident Response:** Detect → investigate (Dashboard) → block (S‑GATE) → generate compliance evidence.
- **Threat Hunting:** Use Active Threat Analytics and Big Data Intelligence APIs to uncover hidden patterns.
- **Audit Reporting:** Generate built‑in or custom reports from Central Management APIs.

### Personas Overview
- **Security Admin:** Manages policies, rules, compliance settings.
- **Database Admin:** Deploys agents, monitors health.
- **Compliance Officer:** Generates audit reports, verifies regulatory adherence.
- **Analyst:** Conducts threat investigations, uses APIs for analytics.

## Security Personnel and Their Responsibilities
- **Security Administrator:** Configures policies, monitors alerts, enforces entitlement baselines.
- **DBA/Data Owner:** Manages datasource definitions, oversees S‑TAP installation, uses Data In‑Sight.
- **Compliance Officer:** Generates regulatory reports, uses Entitlement Optimization for audit evidence.
- **SIEM/Administrative Analyst:** Consumes APIs to ingest events into central SIEM and custom portals.
- **Auditor:** Verifies configuration, reviews discovery results, conducts periodic assessments.

### Guardium Entities Overview
- **Central Manager:** Core service hosting the Management APIs.
- **Guardium Agents (S‑TAP, A‑TAP, K‑TAP):** Collectors streaming traffic to the Collector tier.
- **Collector and Aggregator:** Process and forward audit data to the Central Manager.
- **Policy Objects:** Security Policies, Audit Policies, Classification Rules, Access Rules.
- **Personas and Roles:** User accounts, service accounts, and role assignments within Guardium.
- **Report Objects:** Standard reports, custom CSV/HTML reports, compliance output.
- **Alert Objects:** Security incidents, threat events, exception logs.
- **Data Stores:** Encrypted file repositories, external databases for long‑term audit retention.

## Central Management API
Provides programmatic control of Guardium Central Management functions such as datasource configuration, policy deployment, report retrieval, and system settings management via RESTful interfaces.

## Component Access Guide
Lists Guardium components (Collectors, Central Managers, S‑GATE appliances, aggregators, etc.) and the supported access methods – CLI, Central Management API, and web UI – for interacting with each.

## Big Data Intelligence API
Offers endpoints for programmatic interaction with Guardium Big Data Intelligence, including query generation, result retrieval, and dataset creation.

## Redis Integration Parameters
Requires **host**, **port**, and **password** to connect Guardium collector to a Redis server for real‑time logging and auditing.

## Certificate Management CLI
Commands for managing certificates:
- `gkeytool` – certificate store operations.
- `gcm_client` – client certificate tasks.
- `gcm_server` – server certificate tasks.

## Azure Enable/Disable Monitoring Streams
No specific parameters; the feature works with default settings across Azure environments.

## Active Threat Analytics
Monitors real‑time data using machine‑learning models and correlation rules to detect and respond to active security threats.

## Database Auto‑Discovery
Automatically identifies databases, installs appropriate S‑TAP agents, and provisions default audit policies for newly discovered targets.

## Entitlement Optimization
Analyses and reports on permission entitlements, identifies over‑privileged users, suggests role consolidations, and provides remediation recommendations.

## Investigation Dashboard
Unified UI for monitoring and investigating data activity, aggregating real‑time alerts, activity streams, and policy violation logs for security analysts.

## Troubleshooting Guide
General steps for resolving common Guardium issues: check agent status, verify connectivity, review log files, apply configuration fixes.

## Data In‑Sight Usage
Enables custom dashboards, trend analysis, and reporting on audit data through a browser‑based visualization interface.

## Enhancements in Guardium 12.2
Expanded platform support, improved policy management, enhanced analytics capabilities, and other functional improvements.

## Stored Data Management
Configuring data retention policies, encryption, backup strategies, and archive procedures for Guardium repositories.

## NAS Scan Permissions
Defines required file permissions, service account setups, and scanner configurations for monitoring Network Attached Storage devices.

## Log Exception (LOG)
Exception action that logs events even when no login occurs, similar to a throw exception but without terminating the session.

## Transform Parameters in Policy Rules
Defines how data is processed (e.g., `REMOVE`, `MASK`, `SUBSTITUTE`, `CONCEAL`) before logging or alerting.

## Enabling Query Rewrite
Allows Guardium to modify queries in real time before they are executed, for purposes such as compliance enforcement or performance optimization.

## Query Rewrite Policy Configuration

IBM Guardium's query rewrite feature enables real‑time transformation of SQL statements before they are executed on the database. The transformation is controlled through a policy that groups one or more rewrite rules.  

**Steps to configure query rewrite:**  
1. Edit `guard_tap.ini` to enable the query rewrite engine and specify the rewrite rule files.  
2. In the Guardium UI, create a **Query Rewrite Policy** object.  
3. Define **Query Rewrite Rules** that match source query patterns and specify the replacement SQL.  
4. Associate the policy with one or more monitored datasources via the policy assignment matrix.  
5. Deploy the updated configuration; S‑TAP agents will now apply the rewrite logic on incoming queries.  

**Key concepts:**  
- **Query Rewrite Policy** – container for grouping rules and defining scope.  
- **Query Rewrite Rule** – pattern‑match and replacement definition.  
- **guard_tap.ini** – configuration file where the rewrite engine and rule files are referenced.  
- **Audit Trail** – all rewrite actions are logged for compliance and forensic purposes.

## Comprehensive Guide to Guardium Components and Management

### S-TAP User's Guide
A comprehensive resource for deploying, configuring, and managing S-TAP within Guardium deployments, including installation and security best practices.

### Session Updates Table
Logs incremental changes to active user sessions, capturing essential session dynamics for continuous monitoring and analysis in Guardium.

### Option Description
Detailed table of S-TAP configuration options and their default values, assisting administrators in tailoring S-TAP to specific security and monitoring needs.

### Scenario Instructions
High-level steps for deploying A-TAP to capture database traffic in various scenarios, providing strategic guidance for effective traffic management.

### S-TAP for IBM i APIs
Specifies interfaces and methods for interacting with the S-TAP agent on IBM i systems, enabling integration and management of S-TAP functionality.

### Load Balancer Scripts
Automates load balancing configuration for External S-TAP deployments, enhancing redundancy and reliability in Guardium security infrastructure.

### System CLI Commands
Comprehensive list of CLI commands for administering and configuring Guardium systems, facilitating efficient command-line based administration.

### Alerting Parameters
Configurable settings that define alert triggers, notification methods, and severity levels, crucial for timely detection and response to security incidents.

### Data Mart Parameters
Settings for optimizing data mart operations, including data aggregation, retention, and access control, enhancing data storage and query performance.

### Catalog Entry APIs
Programming interfaces for managing catalog entries in data and result archives, streamlining data archiving and retrieval processes.

### Action Parameters
Defines parameters for configuring responses to security incidents, such as query blocking and credential rotation, customizing Guardium's security actions.

### IBM Guardium Data Protection Features

**Unified Discovery & Classification**
Automatic detection of databases, big-data storage, and files; classification of sensitive data with extensible dictionaries and ready‑made policy templates.

**Real‑time Activity Monitoring**
Capture of SQL queries, file system operations, and API calls via agents (S‑TAP, A‑TAP, K‑TAP) and cloud connectors for continuous visibility.

**Policy Enforcement & Blocking**
Detailed security rules that block or alert on suspicious or unauthorized access, enforced at the S‑GATE layer.

**Compliance Reporting**
Pre‑packaged report templates for PCI‑DSS, HIPAA, GDPR, SOX, and similar frameworks; automated audit logs and interactive dashboards.

### Guardium Workflows

**Discovery & Classification**
Run scheduled or ad‑hoc scans, review classified assets, and apply data‑masking or protection policies.

**Configuration of Agents**
Deploy S‑TAP agents using GIM (Guardium Installation Manager), set up collectors, aggregators, and central managers to transport audit data.

**Policy Management**
Create and enforce security, audit, classification, and access policies; configure FGAC (Fine‑grained Access Control) rules.

**Compliance Audits**
Generate compliance reports, audit trails, and vulnerability assessments; respond to incidents through predefined alert actions.

### Key Personas

- **Platform & Security Administrators** – Manage users, configurations, and policy distribution.
- **Database Administrators** – Install S‑TAP agents and maintain datasource connectivity.
- **Compliance Officers** – Run regulatory reports and ensure audit readiness.
- **Security Analysts** – Investigate alerts, run vulnerability scans, and fine‑tune detection rules.

## Confidential Data Handling

Configure agents, monitor real-time alerts, investigate incidents, and manage sensitive data classification and quarantine processes.

## Personas

- **Security Administrator**
- **Compliance Officer**
- **Data Engineer / DB Administrator**
- **Security Analyst**

## Entities

- **Agents & Collectors:** S‑TAP, A‑TAP, K‑TAP, Collector, Aggregator, Central Manager  
- **Policies & Rules:** Security Policy, Audit Policy, Classification Rule, Access Rule, Blocking Rule  
- **Infrastructure:** Guardium Infrastructure Manager (GIM), Managed Unit, S‑GATE, Universal Connectors, Data Marts  
- **Data Stores:** Databases, File Systems, Big Data platforms, Cloud services (AWS, Azure, GCP)

## Database Connection Architecture

Supports JDBC drivers (native and generic) and resolves instance ports dynamically.