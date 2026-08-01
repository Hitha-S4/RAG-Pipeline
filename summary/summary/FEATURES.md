# IBM Guardium Data Protection — FEATURES

**Category:** features  |  **Generated:** 2026-07-13  |  **Source:** gdp-12.x-documentation 2.pdf

---

## Datasource Connectivity
- **Dynamic Port Detection** supports SQL Server, Oracle, Db2, MySQL, requires the browser service (except z/OS), and links to Database Connection Architecture and Browser Service.  
- **CyberArk Integration** works with all supported Guardium databases, with SDK export restrictions, and connects to Credential Management and Dynamic Secrets.

## Guardium Features Reference
- **Identify Users via Stored Procedures** works on all relational databases, requires Guardium‑API calls in procedures, and links to GuardAppUser, GuardAppEvent, and Application User Capture.  
- **Auto‑Install on DB Server OS Upgrade** requires GIM 11.0+, a reboot, and links to GIM Architecture and Bundle Management.  
- **Central Risk Spotter Management** centralizes Risk Spotter policies from a Central Manager, linking Risk Spotter Engine and Guardium Multi‑System Management.  
- **Query‑Based Test Creation** operates within the Assessment Builder, limiting to assessment queries, and connects to Assessment Query Builder and Test Lifecycle Management.  
- **MD5 Data and CAS Timeout Limits** applies to collectors with CAS, caps md5_size_limit at 1000 and command_wait at 300 seconds, linking to CAS Monitoring and Data Collection Limits.  
- **Decoding Failed Login Names** works with Guardium Insights and Collectors, requiring a custom decoding class implementing Guardium’s interface, and links to Failed Login Events and Custom Decoding.  
- **Periodic Entitlement Review** integrates with external entitlement systems, linking Database Security Posture and Access Review Process.  
- **Query‑Report Builder Options** operates in Guardium Insights Reporting Module, limiting reports to saved queries, and links to Reporting Architecture and Saved Queries.  
- **Private Key‑Protected Certificates** supports Guardium 12.0+, separate keys for GUI and GIM, and links to Certificate Management, PEM Format, and Keystore Operations.  
- **Active Threat Analytics Case Details** provides post‑analysis case details in the AT Analytics Module, linking Threat Analytics Workflow and Case Management.  
- **FAM Discovery & Classification** supports Windows, AIX, Red Hat, Ubuntu file servers, linking File Activity Monitoring and Data Classification.  
- **Universal Audit Log Collection** aggregates AWS CloudTrail, Azure Monitor, Google Cloud Audit Logs, and on‑premises syslog sources, requiring the universal connector.

## Guardium Component Overview

### Pre‑Shipped Plug‑Ins
- Supported on Guardium 12.5+ with read‑only enable/disable workflow for each plug‑in.

### Informix Extended Insight
- Works with Informix 14.10+; requires EXPLAIN plan enabled on the source DB.

### Exit Inspection Engine Activation (Informix)
- Involves enabling the engine and deploying the Guardium shared library.

### Db2 Traffic Encryption
- Applies to all supported Db2 versions; involves enabling Db2 exit and deploying the Guardium library.

### CyberArk Integration
- All Guardium‑supported databases; export restrictions may apply in some regions.

### Dynamic Port Detection
- Available for SQL Server, Oracle, Db2, MySQL; requires browser service; not for z/OS.

### Cloud Database Service Protection (Native Audit)
- Cloud‑specific; integrates with Classification and Vulnerability Assessment.

### Configure Actions
- Modifies Analyzer settings; requires appropriate permissions.

***All other entries are noise or impractical to compress further.***

## Distributed Report Builder on Central Manager

**Support Matrix:** All relational database platforms supported by Guardium  
**Limitations/Constraints:** Requires managed units reachable over network; cannot handle cross‑file references  
**Configuration — Enable Distributed RB**; **Navigation — View Consolidated Results**  
**Knowledge:** Central Manager Architecture, Managed Unit Synchronization  
**Keywords:** Concurrent Query, Data Consolidation, RB Propagation

### Sample Role Description

**Support Matrix:** All Guardium role management interfaces  
**Limitations/Constraints:** None  
**Configuration — Create Role**; **Navigation — Edit Role Properties**  
**Knowledge:** Role Permissions, Sample Role  
**Keywords:** dba role, infosec role, built‑in roles

### About this task (Guardium 11.4+)

**Support Matrix:** Guardium 11.4 and later  
**Limitations/Constraints:** Requires Data Mart tables to exist before creation  
**Configuration — Create Data Mart Table**; **Navigation — Manage Data Mart Icon**  
**Knowledge:** Data Mart Architecture, Aggregation Concepts  
**Keywords:** Hourly Granularity, Data Mart Icon, Summary Tables

### Known limitations

**Support Matrix:** All Guardium versions  
**Limitations/Constraints:** Session‑level policies affect only sessions started after installation; existing sessions remain unaffected  
**Monitoring — Review Session Policies**; **Configuration — Update Session Policies**  
**Knowledge:** Policy Lifecycle, Session Management  
**Keywords:** New Session, Policy Enforcement, Installation Impact

### Field Description (JDBC connector 9.2+)

**Support Matrix:** JDBC connector 9.2+  
**Limitations/Constraints:** None  
**Configuration — Set Connection Property**; **Testing — Validate JDBC URL**  
**Knowledge:** JDBC Driver Parameters, Datasource Connection  
**Keywords:** semicolon‑separated parameters, JDBC URL, property=value pairs

### Parameter Script Question/Meaning (Linux/Unix)

**Support Matrix:** Linux/Unix Guardium deployment scripts  
**Limitations/Constraints:** Hostnames must be resolvable via DNS or /etc/hosts  
**Installation — Run Deployment Script**; **Configuration — Set SVC_HOST**  
**Knowledge:** Deployment Script Parameters, Service Container  
**Keywords:** --svc-host, service containers, host list, default value

### Resource monitoring example (Guardium Agent Monitor 2.1.0)

**Support Matrix:** Guardium Agent Monitor 2.1.0  
**Limitations/Constraints:** Memory thresholds are configurable but not enforced automatically  
**Monitoring — Enable GAM**; **Reporting — View Memory Usage Reports**  
**Knowledge:** Guardium Monitoring Framework, Resource Utilization  
**Keywords:** GAM, memory usage

## Data Management

### Application Parameter
Application scope parameters: ChangeAuditSystem, Access_policy, MonitorValues.

### Creating a Custom Domain
Custom domains can be created for all database types for custom tables and queries.

### Configuring SIEBEL DB
Supported from version 11 onward; database type is fixed after selecting Application Type.

### Guardium Vulnerability Assessment Licensing
Requires per‑MVS virtual server entitlements.

### Log Full Details
(No meaningful content—skipped)

## Datasource Connectivity
### Dynamic Port Detection
**Support Matrix:** SQL Server, Oracle, Db2, MySQL  
**Limitations/Constraints:** Browser service required; z/OS unsupported  
**Workflows:** Add Datasource, View Ports  
**Links:** Database Architecture, Browser Service  
**Keywords:** S-TAP, Collector, JDBC, Browser Service  

## Auditing and Logging
### Verify Upgrade Reboot Requirement
**Workflows:** Upgrade S-TAP  
**Links:** Guardium Installation Manager, Database Reboot  

### S-TAP Client Filtering
**Workflows:** Manage S-TAP Connections, Approve Connections  
**Links:** S-TAP Workflow, Guardium Features  
**Keywords:** CLI, GuardAPI, S-TAP Configuration  

### Cassandra Audit Settings
**Workflows:** Modify Cassandra Settings  
**Links:** Data Auditing Workflow, Cassandra Configuration  
**Keywords:** Audit Reader, Log Settings, Cassandra Cluster  

### Access Management Roles
**Workflows:** Manage User Permissions  
**Links:** Role-Based Access Control  

---

## Investigation Dashboard for Files
**Support Matrix:** Guardium with file monitoring  
**Workflows:** File Investigation Dashboard  
**Links:** File System Monitoring, Dashboards, Forensics  
**Keywords:** File Monitoring, Investigation Dashboard, System Activity  

## Encrypting Syslog
**Support Matrix:** Guardium forwarding to remote syslog receivers  
**Limitations/Constraints:** TCP only; protocols unsupported  
**Workflows:** Secure Syslog  
**Links:** Syslog, Encryption, SIEM  
**Keywords:** Syslog Encryption, TCP, SIEM Integration, Security Forwarding  

## Creating Reports for Data Security Monitoring
**Support Matrix:** All Guardium reporting interfaces  
**Limitations/Constraints:** Appropriate templates and data sources required  
**Workflows:** Create Security Monitoring Reports  
**Links:** Report Building, Data Security, Monitoring  
**Keywords:** Report Creation, Investigate Module, Query Builder, Security Monitoring  

## Teradata ParameterValue Determination
**Support Matrix:** Teradata environments  
**Limitations/Constraints:** Valid instance and path entries required  
**Workflows:** Set Teradata Parameters  
**Links:** Teradata Installation, Parameter Configuration  
**Keywords:** Teradata Instance, Installation Path, Parameters  

## S-TAP Terminate
**Support Matrix:** IBM Guardium Data Protection  
**Limitations/Constraints:** Terminates active sessions, blocks future requests  
**Workflows:** Terminate Sessions  
**Links:** Session Management, Connection Termination  
**Keywords:** S-TAP, Connection Termination, Session Blocking  

## Group Granted to User
**Support Matrix:** Database platforms supporting groups  
**Limitations/Constraints:** Group membership must align with privileges  
**Workflows:** Assign Groups  
**Links:** Database Security, Privileges, Groups  
**Keywords:** Privilege Assignment, Group Membership, Privilege Management

```markdown
## Guardium Applications
**Keywords:** Admin Role, Role Permissions, Access Controls

## Datasource Connectivity
**Support Matrix:** SQL Server, Oracle, Db2, MySQL  
**Limitations/Constraints:** Requires browser service running; not supported on z/OS  
**Workflows:** Configuration — Add Datasource; Navigation — View Ports  
**Knowledge:** Database Connection Architecture, Browser Service  
**Keywords:** S-TAP, Collector, JDBC, Browser Service

## Datasource Connectivity
**Support Matrix:** All relational databases  
**Limitations/Constraints:** None  
**Workflows:** Configuration — Revoke Extrusion; Navigation — Report Builder  
**Knowledge:** Extrusion Monitoring, Logging Mechanism  
**Keywords:** Revoke Checkbox, Already-Logged Responses, Unique Logging

## Blocking (Ranger Dynamic Policy integration)
**Support Matrix:** All Guardium-supported databases  
**Limitations/Constraints:** Requires Ranger 2.0 or higher; not supported on Hive 1.x  
**Workflows:** Policy Management — Configure Ranger Blocking; Monitoring — Review Blocked Events  
**Knowledge:** Access Control Policies, Dynamic Policy Enforcement  
**Keywords:** Ranger, Dynamic Policy, SQL Blocking, Policy Violation

## CyberArk Integration
**Support Matrix:** All Guardium-supported databases  
**Limitations/Constraints:** CyberArk SDK export restrictions apply in some regions  
**Workflows:** Configuration — Install CyberArk SDK  
**Knowledge:** Credential Management, Dynamic Secrets  
**Keywords:** CyberArk SDK, Credential Vault

## Balancing S-TAP Load with Oracle Advanced Security Option
**Support Matrix:** Oracle databases with ASO  
**Limitations/Constraints:** Additional network configuration may be required  
**Workflows:** Configuration — S-TAP Load Balancing  
**Knowledge:** Traffic Distribution, Oracle ASO  
**Keywords:** S-TAP, Collector, Oracle ASO, Traffic Distribution

## External S-TAP
**Support Matrix:** Cloud and on-premises database environments  
**Limitations/Constraints:** Requires network-level access; not suitable for highly distributed databases  
**Workflows:** Configuration — External S-TAP Deployment  
**Knowledge:** Network Monitoring, Database Security  
**Keywords:** External S-TAP, Network Monitoring, Database Traffic, Cloud Deployment

## Guardium Investigation Dashboard
**Support Matrix:** All Guardium versions supporting dashboards  
**Limitations/Constraints:** Custom dashboards require administrator privileges  
**Workflows:** Navigation — Investigation Dashboard Setup; Configuration — Custom Widget Addition  
**Knowledge:** Dashboard Configuration, Widget Customization  
**Keywords:** Investigation Dashboard, Custom Widgets, Security Analysis, Alert Correlation
```

## Feature Reference

### LDAP Authentication
Support LDAP server (vendor‑specific), requires user pre‑import, separate configuration and authentication workflows.  
**Knowledge:** Directory Services, Credential Management **Keywords:** LDAP, Imported User, LDAP Login

### Remove User Account
Admin privileges needed; deletes account and triggers deletion alert.  
**Knowledge:** User Management, Alert Routing **Keywords:** Delete, User Browser, Alert Admin

### 146. Receiver Details  
All platforms supported, no constraints, supports role assignment and ./LoggedUser handling.  
**Knowledge:** Policy Assignment, Workflow Automation **Keywords:** Role, User Group, LoggedUser

### 147. Transform Action Examples  
Supported on all Guardium versions with Transform actions; includes HOSTNAME CACHING and Failed Login rules.  
**Knowledge:** Data Transform, Policy Management **Keywords:** Transform Rule, Failed Login

### 148. Remote Host Logging  
Requires SSH access; configure host settings and transfer logs via SCP/FTPS.  
**Knowledge:** Log Forwarding, Remote Storage **Keywords:** Remote Host, SCP Port

### 149. LIKE / NOT LIKE Operators  
Used in SR policy group expressions, no constraints, supports wildcards.  
**Knowledge:** Session Policy Language, Pattern Matching **Keywords:** LIKE, Wildcard, SR Policy

### 150. Status Unavailable  
S‑TAP must be installed; provides discovery and auto‑discovery workflows.  
**Knowledge:** S‑TAP Agent, Auto‑Discovery **Keywords:** S‑TAP, Daily Execution

### 151. Session‑Level Policies  
Supported on all policy‑capable versions; enables real‑time session inspection and security actions.  
**Knowledge:** Real‑Time Monitoring, Policy Execution **Keywords:** Session Policy, Real Time

### 152. Show SSL Configuration Command  
Available via Guardium appliance CLI; no constraints.  
**Knowledge:** SSL/TLS Settings, Cipher Suites **Keywords:** SSL, CLI Show

### 153. REST API Example (Ranger)  
Requires authenticated API access; call REST endpoint for Ranger retrieval.  
**Knowledge:** REST API, Ranger Configuration **Keywords:** REST, curl, Ranger

### 154. Add to Schedule / Revoke Sessions  
Admin rights needed; manage S‑TAP schedule and ignore/revoke sessions.  
**Knowledge:** S‑TAP Management, Traffic Ignoring **Keywords:** Schedule, Revoke, Ignored Sessions

### 155. Fail‑Over File Size Settings  
Applicable to all DSC configurations; disk space needed is twice the fail‑over size.  
**Knowledge:** Fail‑Over Mechanism, Disk Space Planning **Keywords:** Fail‑Over Size, Reconnection Attempts

### 156. Flat Log Process  
Supported on high‑traffic appliances; requires later parsing of raw logs.  
**Knowledge:** Log Processing, High‑Volume Handling **Keywords:** Flat Log, High Traffic

### 157. Quick Parse Native Redact Action  
Operates on extrusion policy rules; no constraints, preserves context during redaction.  
**Knowledge:** Data Redaction, Extrusion Policies **Keywords:** Redact Action, Extrusion Rule

## 190. Digits - 0-9
- **Categories:** features
- **Keywords:** b0f2847e-46b9-4fba-8c51-f1b480fdae00

## 191. About this task
- **Categories:** keywords, features, workflows
- **Workflows:** Configuration

## Modify DB Ownership
### Reassign a Database Owner
- **How to reassign ownership:** In *Manage > Databases*, locate the database, click **Edit > Ownership**, select a new owner from the list, and **Save**.
- **Considerations:** Ensure the new owner has appropriate privileges before changing.

## Working with custom queries
### Use Custom Query Builder
- **What it does:** Create and run ad‑hoc SQL queries against Guardium data sources.
- **How to access:** *Reports > Query Builder > New Query*.
- **Key feature:** Combines **Custom Query**, **Custom Table**, and **Custom Domain** capabilities.

## Parameter Value type Description
### Define Parameter Types
- **Categories:** Keywords, features
- **Supported values:** Strings, integers, booleans, timestamps.
- **Usage:** Configure parameters via **Policy Installation** and **User Blocking**.

## About this task
### External S‑TAP Deployment
- **What is configured:** External S‑TAP proxy key (`proxy.Key`) and certificate (`proxy.pem`) stored as a Kubernetes secret.
- **Purpose:** Enables secure communication and trusted‑root validation.

## Datasource APIs
### Manage Data Source Configuration
- **APIs available:** `add connection`, `delete datasource`, `modify_guard_param`.
- **Integration:** Used in **Data Source Configuration** and **Connection Management** workflows.

## Access management
### Default Roles & UI Access Control
- **Core concepts:** Default roles, **Access Query Builder ALL**, UI access permissions.
- **How to manage:** *Admin > Access Management* → configure roles and query builder permissions.

## Adding workflow events
### Define Audit Task Workflow
- **Steps:** *Workflow Designer > New Task > Audit Task*.
- **Components:** Choose audit process, add events, define additional columns, edit task settings.

## Attribute Description
### Connection Properties
- **Attributes:** Access ID, Client Port, Database Name.
- **Where used:** In **Connection Attributes** for data source discovery and reporting.

## Determining the severity of CRITICAL and MAJOR tests
### Policy Hardening Guidelines
- **Severity mapping:** Assign **CRITICAL** to policy violations with high risk; **MAJOR** for significant but lower‑risk issues.
- **Configuration:** Adjust in **Policy Hardening** → **Password Default** and **Authentication Security** settings.

## The alert message template
### Global Profile Alert Configuration
- **Template components:** Message body, placeholders for rule details.
- **Location:** *Admin > Global Profile > Alert Content*.

## Define an Incident Generation Process
### Workflow – Incident Generation
- **Trigger source:** Policy Violations Log.
- **Workflow steps:** Define query to fetch first 5000 violations, map fields, create incidents.
- **Outcome:** Automated creation of incidents for policy violations.

## About this task
### Import External Data Sources
- **Supported imports:** External data source, custom tables, custom domains, custom queries.
- **Process:** *Manage > Databases > Import > External Data Source*.

## Define Audit Task
### Assessments with CAS‑Based Tests
- **Setup:** *Assessment Builder > New Assessment > CAS‑based Test*.
- **Configuration steps:** Select test type, define scope, schedule, and reporting options.

## Collector Management

### Define Collectors
- All Guardium-supported database platforms supported.
- Requires active S-TAP on managed units.
- Configuration via Define Collector; administration via Manage Collectors.
- See Collector Overview and S-TAP Installation for details.

### Configure Cloud DB Service Protection
- Supported: AWS RDS, Azure SQL, Google Cloud SQL.
- Requires IAM role with read access to cloud metadata.
- Configuration via Enable Cloud DB; discovery via Cloud Service.
- See Cloud Data Accelerators and GDPR Data Discovery for details.

## Security Assessment

### Create Security Assessment
- Supported on all Guardium-supported databases.
- Requires datasource access permissions.
- Use Assessment Builder in Configuration; Assess in Security.
- See Security Assessment Process and Test Selection for more information.

### Manage Evaluation Profiles
- All supported evaluation profile types available.
- Conflicting profiles generate validation errors.
- Manage via Profile Management in Configuration; evaluate in Security.
- See Evaluation Profiles and Conflict Resolution for details.

## Data Management Features

### Create Client Group
- Supported on Guardium 11.0+.
- No limitations; configure via Set up by Client workflow.
- Useful for bulk deployment and software distribution.
- See Bulk Deployment and Client Management for details.

### Bind Variables
- Available on all Guardium-supported DBMS.
- Requires Full SQL logging enabled.
- Configure via DB Configuration workflow.
- Relevant for SQL Monitoring and Audit Policy.
- See SQL Monitoring and Audit Policy for more information.

### SNMP Monitoring
- Supported on Guardium Appliance v10.1.2+.
- SNMPv3 requires valid credentials.
- Configure via Network Monitoring workflow.
- See SNMP Protocol and OID Configuration for details.

### GRANT/REVOKE Tracking
- Supported in all Audit Policy configurations.
- Audit policy must be active to capture events.
- Configure via Privilege Management workflow.
- See Audit Trail and Privilege Auditing for details.

### S-TAP Verification
- Supported on S-TAP v11.0+.
- Requires verified environment.
- Configure via Verification workflow in Operations.
- See S-TAP Configuration and Verification Schedules for details.

### Datasource Group
- Supported on all datasources compatible with Guardium.
- No limitations; configure via Datasource Management workflow.
- Useful for application integration and classification.
- See Datasource Configuration and Application Integration for details.

### SQL Criteria for Failed Logins
- Supported on all DBMS with SQL logging.
- Requires Full SQL logging enabled.
- Configure via Failed Login Rule in Compliance workflow.
- See Failed Login Detection and Audit Logs for details.

### Partition Optimization
- Supported on Guardium 12.0+; enabled by default.
- Requires proper configuration.
- Configure via Database Optimization workflow.
- See Query Performance and Table Partitioning for details.

### View ANTLR3 Settings
- Supported on Guardium with ANTLR3 parser enabled.
- Requires parser configuration.
- Configure via ANTLR3 Settings workflow.
- See ANTLR3 Parser and Parser Configuration for details.

### Anomaly Detection Investigation
- Supported on Guardium 12.0+.
- Requires Anomaly Detection module enabled.
- Investigate via File Activity workflow in Investigation.
- See File Activity Monitoring and Outlier Detection for details.

### ATTACH ON REQUEST Enforcement
- Supported on Guardium with firewall module.
- Requires firewall policy configuration.
- Configure via Firewall Management workflow.
- See Firewall Policies and Session Management for details.

### Uploading Table Definitions
- Supported on Guardium with custom table support.
- Requires valid product key.
- Configure via Upload Table Definitions workflow.

## Database Security

### Enable Database Security Assessment
- **Support:** All Guardium-supported databases
- **Requirements:** API credentials; non-relational databases not supported
- **Workflow:** Configuration – Enable Database Security Assessment
- **Knowledge:** Database Security Assessment Architecture, API Permissions
- **Keywords:** SQL Security, Compliance, SQL Auditing, IAM Roles

---

## Deployment Health

### Deployment Health Topology and Table Views
- **Support:** Guardium Central Manager and all managed units
- **Requirements:** Network connectivity; not compatible with pre-10.6 versions
- **Workflows:** Monitoring – View Deployment Health; Alerting – Set Deployment Health Thresholds
- **Knowledge:** Central Manager Architecture, Distributed Deployment
- **Keywords:** Guardium System Health, Deployment Monitoring, Central Manager, Health Dashboard

---

## Threat Services

### Dynamic Load Balancing for Managed Units
- **Support:** Guardium 12.1+
- **Requirements:** Configured central manager; managed units must run 12.1+
- **Workflows:** Configuration – Central Manager Settings; Navigation – Managed Unit Assignment
- **Knowledge:** Load Balancing Algorithms, Managed Unit Health Checks
- **Keywords:** Central Manager, S-TAP Agent, Universal Connector, Elasticity

### Enterprise Load Balancing Overview
- **Support:** Guardium 12.1+
- **Requirements:** Managed units enrolled in central manager; no external load balancer integration
- **Workflows:** Configuration – Assign Managed Unit; Monitoring – Unit Load Report
- **Knowledge:** System Load Metrics, Availability Monitoring
- **Keywords:** Dynamic Allocation, Workload Distribution

---

## Guardium Host Configuration

### Parameter Configuration: `guardium_host`
- **Support:** All Guardium-supported platforms
- **Workflow:** Administration – Guardium Host Settings; Setup – Multi-Tier Deployment
- **Knowledge:** Host Identification, High Availability Setup
- **Keywords:** Hostname, IP Address, Multi-Host Configuration

---

## S-TAP Buffer Mechanism

### S-TAP Buffer Mechanism
- **Support:** All S-TAP versions 12.0+
- **Requirements:** Disk space for physical buffers; memory for anonymous buffers
- **Workflows:** Configuration – Buffer Settings; Maintenance – Disk Usage Management
- **Knowledge:** Data Staging, High-Volume Data Handling
- **Keywords:** Buffer Size, Memory Allocation, Disk Space

---

## Policy Management

### Policy Installation Procedure
- **Support:** Guardium 11.0+
- **Requirements:** Policy Builder for Data license; not applicable to archived systems
- **Workflow:** Workflow – Install Policy; Management – Policy Deployment Scope
- **Knowledge:** Policy Builder, Managed Units
- **Keywords:** Policy Deployment, Managed Unit List, Installation Process

---

## Network Configuration

### Proxy Connectivity Support
- **Support:** All Guardium versions from 11.0
- **Requirements:** Proxy allows outbound Guardium connections; no authenticating proxies
- **Workflows:** Configuration – Proxy Settings; Network – Proxy Configuration Guide
- **Knowledge:** Network Proxies, Remote Source Connections
- **Keywords:** Web Proxy, Remote Database Connection

---

## Oracle Configuration

### Oracle CM Connection Logging
- **Support:** Oracle databases using Connection Managers; all Guardium versions
- **Requirements:** Correct IP logging configuration; does not affect non-Oracle systems
- **Workflows:** Configuration – Oracle CM Settings; Security – IP Audit Configuration
- **Knowledge:** Oracle Configuration Manager, IP Logging Mechanism
- **Keywords:** Oracle CM, IP Logging, Audit Trail

---

## Reporting

### Days Reporting Not Archived or Exported
- **Support:** Guardium 11.0+
- **Requirements:** Daily Guardium operations; excludes external export processes
- **Workflows:** Reporting – Days Report; Maintenance – Data Age Management
- **Knowledge:** Data Retention Policies, Archival Processes
- **Keywords:** Data Retention, Archive Report, Export Status

---

## Ranger Configuration

### Ranger Configuration via GuardAPI
- **Support:** Ambari-managed clusters (details incomplete)

## External S-TAP Deployment

### Prepare Deployment
- **Components:** Linux containers (Docker/Kubernetes)
- **Support Matrix:** Guardium 11.5+
- **Limitations:** Requires SSL-enabled collector and trusted certificate

### Links
- **Knowledge:** External S-TAP Architecture, Kubernetes Deployment
- **Keywords:** Master URL, Token Integration, Docker Location

## Datasource Connectivity

### Delete Datasource
- **Components:** All datasource types
- **Support Matrix:** API delete_datasourceRef_by_name, delete_datasource_by_id
- **Limitations:** Requires correct name/ID, appropriate permissions, cascade flag for dependencies

### Links
- **Knowledge:** API Reference, Datasource Management
- **Keywords:** datasourceName, cascade, ConfirmationNumber, API, delete

## Assessment & Compliance

### Security Assessments
- **Components:** All installed collectors and aggregators
- **Support Matrix:** All versions supporting security assessments
- **Limitations:** None

### Links
- **Knowledge:** Security Policy Management, Risk Assessment
- **Keywords:** assessment, host, IP, result, query

## Guardium Documentation Compression

### Entity Management
**Support Matrix:** All Guardium versions with custom table support  
**Keywords:** Alias Management, Custom Table Usage  
**Query:** Must return valid alias/resolution pairs; custom table must be accessible.

### Guardium Installation and Verification
**Support Matrix:** All Guardium-supported platforms  
**Keywords:** GIM, SUPERVISOR, Guardium System  
**Note:** Verify after successful installation only.

### Set Job Process Concurrency Limit
**Support Matrix:** All Guardium versions supporting GuardAPI  
**Note:** None specified.

### File Pattern Configuration
**Support Matrix:** All Guardium-supported databases  
**Keywords:** File Pattern, $SYBASE, CAS Monitoring  
**Constraints:** Paths must use $SYBASE or relevant variables.

### S-TAP Status Monitor
**Support Matrix:** All Guardium S-TAP installations  
**Keywords:** S-TAP Status, Host Attributes, Instance Flags  
**Note:** Requires active S-TAP instances.

### Target Host Specification
**Support Matrix:** All Guardium API-enabled systems  
**Keywords:** api_target_host, managed units, central manager  
**Constraints:** Valid values include all_managed, all, group:<group name>.

### CAS File Pattern Definition
**Support Matrix:** All supported CAS integrations  
**Keywords:** File Pattern, $INSTHOME, CAS Monitoring  
**Constraints:** Paths must use $INSTHOME or absolute paths.

### CLS Process Run Information
**Support Matrix:** All Guardium classification installations  
**Keywords:** CLS Process, Classification Details, Incident ID  
**Note:** Requires executed classification processes.

### Principal Definition for Kafka TLS
**Support Matrix:** All Guardium systems using Kafka with TLS  
**Keywords:** kafka_principal, TLS, Kerberos Authentication  
**Constraints:** Principal must be valid in Kerberos environment.

### Remote Log Display and Configuration
**Support Matrix:** Guardium systems with rsyslog  
**Keywords:** remotelog, rsyslog, Remote Log Commands  
**Note:** Requires configured rsyslog.

## Guardium Technical Reference (Compressed)

### Guard and Filtering
- **Support:** All Guardium reporting systems  
- **Row limit:** 10,000 rows max displayed  

### Classifier Log Level Adjustment (GuardAPI)
- **Guardium versions:** All with classifier log levels  
- **Constraint:** logLevel values are schema‑defined  

### Operating System User Management
- **Supported OS:** All Guardium‑supported operating systems  
- **Prerequisite:** System administrator privileges required  

### External Reporting Feeds
- **Supported versions:** All Guardium versions with external feed capability  
- **Requirement:** Valid external database connection  

### Classifier Log Level API
- **Guardium versions:** All with GuardAPI  
- **No special constraints**  

### Active Threat Analytics
- **Appliance:** Guardium appliance  
- **Workflows:** Threat Management → Close Cases; Case Management → Exclude Cases  

### Auto‑Update Client (352)
- **Clients:** Windows, macOS, Linux (x86_64)  
- **Requirement:** Internet access to GIM server; schedule non‑overrideable  
- **Related concepts:** Guardium Installation Manager (GIM), version bump, secure repository  

### S‑TAP Info on Central Manager
- **Scope:** All platforms with S‑TAP agents  
- **Key term:** Stapsvc/GDM integration  

### Example 2: Session‑Level Policy with Server Port Filtering & DB\_USER Transformation  
- **Policy support:** All releases that support session policies  
- **Behavior:** Transformation only applied to matching conditions  

### Parameter Value Types – delete\_datasource\_by_name  
- **API:** Guardium API  
- **Privilege needed:** Administrator  
- **Workflow:** API → remove datasource; CLI → `delete_datasource_by_name`  

### Managing Users
- **Console:** Guardium web console  
- **Features:** Add/disable users, LDAP import (network‑dependent), edit roles  

### Additional API Examples: Create New Data Source (POST)  
- **API:** Guardium REST API  
- **Security:** Authentication token required  
- **Workflow:** `POST /api/application/add_datasource` with JSON payload  

### Most Active Clients by IP
- **License:** Reporting license required  
- **Purpose:** Identify high‑traffic IP addresses, aggregate database activity  

### Parameter Value Types (Additional details)  
- **Note:** Entry appears incomplete in source material.

## Guardium API Documentation
### Support Matrix
- All versions of Guardium API
### Limitations
- Context dependent; see API reference
### Workflows
- List Parameters (API Exploration)
- Parameter Descriptions (Documentation Review)

## Navigation Lifecycle
### Support Matrix
- All versions of Guardium UI
### Limitations
- Dependent on user role permissions
### Workflows
- Access Security Lifecycle (UI Navigation)
- Role Management (Expand Components)

## SOX Compliance
### Support Matrix
- Guardium FAM module
### Limitations
- Requires FAM agent installed
### Workflows
- SOX Template Setup (Compliance)
- Continuous SOX Auditing (Monitoring)

## CLI Command: `disable_ip_to_host_aliases`
### Support Matrix
- All Guardium CLI versions
### Limitations
- Must be run on Guardium collector
### Workflows
- Host Aliasing Management (Configuration)

## Session Management
### Parameter: `session_inference_setup`
### Default Values
- Overrides required for specific use cases

## Shared Memory Configuration: DB2
### Parameter: `Adjust.db2_fix_pack_adjustment`
### Specificity
- Offset calculation specific to DB2 internals

## Guardium Command Reference

### Configure Datamart Export Settings
*Supported on Guardium appliances. No limitations.*  
Configuration command: `datamart_update_copy_file_info`.

### Verify S-TAP Diagnostics
*Supported on appliances with S-TAP installed. May disrupt authentication if invalid credentials are used.*  
Verification workflow: `S-TAP verification`.

### Update Privileged User Lists
*Supported on Guardium systems with value‑change triggers and valid DB permissions.*  
Maintenance workflow: `Maintain Privileged Users Lists`.

### Upgrade Edge Runtime
*Supported on Edge version 2.0.0 and later that can access the patch repository.*  
Upgrade workflow: `Upgrade Edge`.

### Guardctl Deactivate Instance (Greenplum)
*Supported on Greenplum installations with guardctl.*  
Operation: `deactivate instance`.

### High‑Volume Outlier Detection
*Supported on systems monitoring transaction volume.*  
Monitoring workflow: `Vulnerable obj. outlier`.

### Convert Collector to Aggregator
*Supported on Guardium Collector appliances.*  
Migration workflow: `Promote to Aggregator`.

### External S-TAP Setup
*Supported on Guardium appliances and remote database servers.*  
Monitoring workflow: `External S-TAP setup`.

### Windows S-TAP GIM Parameters
*Supported on Windows Guardium agents.*  
Installation workflow: `Configure via GIM`.

### Data Group Listing API
*Supported on Guardium appliances. Requires admin role access.*  
Query: `list_groups`.

### Unsupported API Parameters
*Supported on all Guardium API clients.*  

### SMTP Email Alert Configuration
*Supported on appliances with configured SMTP gateway.*  
Configuration: `SMTP Settings`.

### Install GIM Client on Non‑Standard Partitions
*Supported on Solaris secondary zones and AIX WPARs (may need extra zone configuration).*  
Installation workflow: `GIM in Partitions`.

### Toggle Fault‑Tolerant Execution
*Supported on appliances with S3 configuration.*  
Configuration: `Toggle Fault Tolerance`.

---

## Datasource Connectivity

### Dynamic Port Detection
*Supported on SQL Server, Oracle, Db2, MySQL where the browser service runs (not on z/OS).*  
Used in: Add Datasource, View Ports.

## Database Entitlements
- **Support Matrix:** Predefined entitlements for many datasource types
- **Workflow types:** Data Access Review, Policy Enforcement

## Datasource Connectivity
### list_datasource_by_id API
- **Support Matrix:** General API
- **Constraints:** Requires api_target_host; call from a Guardium system
- **Workflows:** CLI — list_datasource_by_id
- **Links:** API Structure, Target Host Configuration

### CAS Template Execution
- **Support Matrix:** DSE Cassandra, CAS scripts
- **Constraints:** Directory and pipe‑separated variables required
- **Workflows:** Configuration — Add Datasource; Edit CAS Template
- **Links:** Cassandra Query Language, CAS Templates

## GuardAPI Configuration
### GuardAPI Configuration
- **Support Matrix:** All Guardium‑supported databases
- **Constraints:** api_target_host required
- **Workflows:** Configuration — Add API Parameter

### Parameter Configuration
- **Support Matrix:** API configuration parameters
- **Constraints:** None
- **Workflows:** Configuration — Update Parameter
- **Links:** API Configuration, Parameter Management

## MongoDB Data Loading
### MongoDB Data Loading
- **Support Matrix:** MongoDB, datasource_name
- **Constraints:** datasource_name and collectionName required
- **Workflows:** Configuration — Load Data
- **Links:** MongoDB Connector, Data Loading

## Amazon Data Stream Configuration
### Amazon Data Stream Configuration
- **Support Matrix:** Amazon Web Services, datasource_name
- **Constraints:** Cloud account name definition required
- **Workflows:** Configuration — Activate Service
- **Links:** Amazon Data Streams, Cloud Configuration

## Rule Management
### Rule Change Order
- **Support Matrix:** Guardium policies
- **Constraints:** fromPolicy, order, ruleDesc required
- **Workflows:** Configuration — Change Rule Order
- **Links:** Rule Management, Policy Configuration

## Key File Management
### Key File Copying
- **Support Matrix:** Key file management
- **Constraints:** fileName and targetUnit required
- **Workflows:** Configuration — Copy Key File
- **Links:** Key File Management, API Configuration

## Application Management
### Application Entity Definition
- **Support Matrix:** Guardium applications
- **Constraints:** appId and api_target_host required
- **Workflows:** Configuration — Define Application
- **Links:** Application Management, GuardAPI Entities

## Security Configuration
### Secure Settings Configuration
### Engine Configuration Update
### Runtime Sensitive Object Management

## Guardium User Accounts
Guardium supports managing user access through a workflow that handles user accounts.

## Quick Parse No Fields
The Quick Parse feature supports parsing in all Guardium versions without requiring any fields.

## DB_USER Matches SCOTT
In all Guardium releases, DB_USER can be matched to the value SCOTT during user access analysis queries.

## GuardAPI Syntax “change_monitor_value”
The GuardAPI `change_monitor_value` command is available in Guardium 11.3 and later. It allows administrators to alter monitor values as part of configuration management.

## GuardAPI Syntax “configure_auth”
Starting with Guardium 11.3, the `configure_auth` API enables configuring authentication settings such as basedn and port for LDAP integration.

## About This Task
The “Report Building – Columns Selection” workflow in the reporting module allows users to select columns for report customization.

## Parameter Value Type Description
The `api_target_host` parameter specifies the host for API targets and cross‑manager calls. It is used in Guardium 11.3 and later releases.

## System Health
Guardium’s asset management capabilities include monitoring system health and inventory across all versions.

## GuardAPI Syntax “list_all_reports”
From Guardium 11.3 onward, `list_all_reports` lists all available reports via the API.

## Parameter Value Type Description – API Target Host
In Guardium 11.3+, `api_target_host` configures the target host for API operations, supporting API management and host settings.

## Parameter Value Type Description – Cross‑Manager API Calls
`api_target_host` is used in API integration workflows to specify hosts for cross‑manager API calls, applicable in all Guardium versions.

## Session Ignore (IGNORE_SESSION)
Ignore session functionality allows dropping or discarding sessions without requiring specific constraints, supported across all Guardium versions.

## Report – Current Results
The reporting module enables users to view and compare report results in all Guardium releases.

## Maintenance Log
Cold storage logs are accessible for Guardium 12.2.x and later, requiring the Cold Storage Module for maintenance tasks.

## Password Hardening
The CLI provides strong password policy enforcement across all Guardium versions, enhancing security compliance.

## Show Command
The **Show Command** workflow in the Aggregation System supports diagnosing static and non‑static table types, including classifications such as GDM\_OBJECT and GDM\_CONSTRUCT.

## GuardAPI Syntax “Change_to_microsoft”
The `Change_to_microsoft` GuardAPI syntax is not described in the provided entries and thus cannot be summarized.

Matrix:** All Guardium versions with Policy Analyzer feature
- **Limitations/Constraints:** Requires API credentials with administrator rights; policy analyzer must be enabled prior to disabling
- **Workflow types:**
  - **Configuration — Manage Policy Analyzer**  
  - **Navigation — Policy Analyzer Settings**
- **Links:**
  - **Knowledge:** Policy Analyzer, API Permissions  
  - **Keywords:** policyAnalyzerEnabled, api\_target\_host, disable, Guardium services

## 481. Backup Operators

### Backup Operators
- **Support Matrix:** Windows Server
- **Limitations:** No full admin rights; limited to backup tasks
- **Keywords:** backup operators, privileged access

---

## 482. CAS Client Ignore Change Alerts

### CAS Client Ignore Change Alerts
- **Support Matrix:** All CAS client versions
- **Workflow:** Configuration → Suppress Change Alerts
- **Keywords:** ignoreChangeAlerts, cas.client.config.properties

---

## 483. GuardAPI Syntax (Incomplete – Skipped)

---

## Datasource Connectivity

### Dynamic Port Detection
- **Support Matrix:** SQL Server, Oracle, Db2, MySQL (excludes z/OS)
- **Workflows:** Add Datasource, View Ports
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

---

## GuardAPI Maintenance

### Persistent Queue Enablement for Universal Connectors
- **Support Matrix:** Logstash inputs
- **Workflow:** Configuration → Enable Persistent Queue
- **Keywords:** GuardAPI, pq_enabled, Logstash Restart

---

## User Management

### Group Membership Retrieval
- **Support Matrix:** All supported Guardium databases
- **Workflow:** Queries → list_members_of_groups_by_id
- **Keywords:** group_id, member_retrieval

---

## User Hierarchy Operations

### Child Hierarchy Retrieval
- **Support Matrix:** All supported Guardium databases
- **Workflow:** Queries → list_user_hierarchy_by_parent_user
- **Keywords:** parent_user, child_creation

---

## Alert Configuration

### Alert Rate Adjustment
- **Support Matrix:** All supported Guardium databases
- **Workflow:** Configuration → set_alerter_settings
- **Keywords:** alert_on_startup, poll_interval, api_target_host

---

## Patch Management

### Universal Connector Fixes
- **Support Matrix:** All supported Guardium databases
- **Workflow:** Updates → Cumulative Patches
- **Keywords:** universal_connector, cumulative_patches

---

## API Development

### Action Removal Syntax
- **Support Matrix:** Guardium V11.4+
- **Workflow:** Maintenance → delete_classifier_action
- **Keywords:** actionName, policyName, ruleName

---

## Parameter Reference

### Execution Target Specification
- **Support Matrix:** All supported Guardium databases
- **Workflow:** Configuration → api_target_host
- **Keywords:** target_hosts, execution_scope

---

## Endpoint Security

### push_insights_trust
- **Support Matrix:** All Guardium Insights deployments
- **Workflow:** Security → Trust Management
- **Keywords:** trust certificate, API token, Insights platform

## Guardium Datasource Connectivity

### Defining Guardium datasources to access the HashiCorp vault
- **Components:**
  - All Guardium versions that include HashiCorp Vault integration
- **Supports:**
  - Configuration — HashiCorp Vault Integration
- **Enable:**
  - Connection — HashiCorp Vault API
- **Key Points:**
  - Requires valid API credentials and appropriate Vault policies

## Understanding UI Examples

- **Components**: UI Ribbon interface version 11.1+  
- **Constraints**: None  
- **Workflows**: UI Ribbon > Session Policies  
- **Links**: UI Navigation, Policy Configuration  

## PCI Policy Violations Monitoring

- **Components**: All PCI‑compliant databases (e.g., SQL Server 2019, Oracle 19c)  
- **Constraints**: PCI module license; data classification required  
- **Workflows**: Monitor > PCI Report Card; Configuration > PCI Settings  
- **Links**: PCI DSS Requirements, Data Classification  

## Defining Guardium Datasources to Access HashiCorp Vault

- **Components**: Guardium 11.3 +  
- **Constraints**: Vault API v1/v2 only; `enable_secrets_management` flag required  
- **Workflows**: Datasource > Create New > Vault; Secrets Management > Configure Vault  
- **Links**: Datasource Configuration, Secrets Management  

## Parameter Default Meaning

- **Components**: All collectors with external S‑TAPs (e.g., 11.3.1 +)  
- **Constraints**: None  
- **Workflows**: S‑TAP > Load Balancing Settings  
- **Links**: S‑TAP Load Balancing, External S‑TAP Architecture  

## 514. Understanding UI Examples

- **Components**: UI Ribbon (11.1+)  
- **Constraints**: None  
- **Workflows**: UI Ribbon > Session Policies  
- **Links**: UI Navigation, Policy Configuration  

## 519. Building Audit Processes

- **Components**: Enterprise & premium editions (11.4+)  
- **Constraints**: None  
- **Workflows**: Audit Builder > Create New Process; Audit > Audit Processes  
- **Links**: Automatic Auditing, Vulnerability Assessment  

## 521. GuardAPI Syntax

- **Components**: Guardium 10.6 + CLI  
- **Constraints**: Requires `api_admin` role; `api_target_host` reachable  
- **Workflows**: Administration > CLI > `list_approved_stap_client`  
- **Links**: GuardAPI CLI, API Access Control

## Active Profiles Deactivation

Deactivate a profile before modifying it. Use **GBDI Configuration > Data Ingestion Profiles > Remove Extraction Profile** to delete a GBDI profile.

## S‑TAP Fail‑Over File Size

- **Support Matrix:** All S‑TAPs ≥ 10.5  
- **Limitations/Constraints:** Larger settings raise storage usage and can affect network resilience.  
- **Workflow:** Advanced Tuning → Fail‑Over File Settings.  

## Guardium Exclude Client IP

- **Support Matrix:** All collectors ≥ 10.1  
- **Workflow:** System Settings → Exclude Client IP/Mask.  

## Policy One‑Match Rule

- **Support Matrix:** Versions with prioritized policies (≥ 11.3)  
- **Limitations/Constraints:** Only one matching rule fires per event.  
- **Workflow:** Policies → Create/Modify Rule → One Match.  

## Vulnerability Assessment Test Types

- **Support Matrix:** SQL Server, Oracle, DB2, SAP HANA, Informix, Sybase (not DB2 on z/OS)  
- **Workflow:** Test Configuration → Add Test → Policy Association → Assign Vulnerability Assessment.  

## Guardium Search Configuration – Customize Search Page

- **Support Matrix:** Guardium Search Interface  
- **Workflow:** Navigation → Search Page Configuration.  

## GuardAPI – Enable Special Attributes

- **Support Matrix:** All managed units  
- **Workflow:** API Execution.  
- **Keyword:** `enable_special_attributes` (e.g., Hive, Query‑Report Builder).  

## GuardAPI – Enable Quick Search

- **Support Matrix:** Investigation Dashboard  
- **Workflow:** API Call with Boolean `quick_search=all`.  

## GuardAPI – List Audit Processes

- **Support Matrix:** Any target host(s)  
- **Workflow:** GuardAPI call using `api_target_host`.  

## GuardAPI – Discover Name and Description

- **Support Matrix:** Classification scenarios  
- **Workflow:** Scenario Definition → DiscoverName / Description.  

## GuardAPI – Custom Alerting

- **Support Matrix:** Alert Notification Channels  
- **Components:** Email, SNMP, Syslog, Java Notification.  

## Multi‑CM Outliers Propagation

- **Support Matrix:** Multi‑CM environments – enabled on any Central Manager.  

## Universal Connector Restart & Logs

- **Support Matrix:** UC on collectors  
- **Components:** `restart_uc`, `uc-logstash.log`, `logstash-plain.log`.  

## Investigation Dashboard – Search

- **Components:** UI & Data files  
- **Workflow:** Search in Dashboard.  

## Search Parameter Transforms

- **Support Matrix:** Search parameters with transforms  
- **Limitations/Constraints:** Non‑standard behaviors (examples provided).  

### Parameter Default Meaning  

(No further content supplied)

## Components

- **Support Matrix:** 
  - Multi‑Collector Configurations  
  - Cloud Service Providers  
  - GuardAPI  
  - Custom Tables and Domains  
  - Certificate Restoration  
  - All Guardium‑supported databases  
  - Guardium‑supported audit tasks  
  - All Guardium‑supported managed units  
  - All Guardium‑supported GIM servers  
  - All Guardium‑supported databases (CyberArk)  
  - Ranger 1.0+  
- **Limitations/Constraints:**  
  - Default value behavior  
  - Cloud‑specific constraints  
  - Parameter definitions  
  - Requires valid certificates  
  - Data import dependencies  
  - Zip size limited by system  
  - Requires Ranger policies  

## Workflows with Different Types

- **Configuration – Parameter Setting**
- **Deployment – Cloud Installation**
- **Configuration – API Execution**
- **Configuration – Data Integration**
- **Maintenance – Certificate Restoration**
- **Configuration – Install CyberArk SDK**
- **Configuration – Audit Tasks**
- **Configuration – Failover Groups**
- **Configuration – Ranger HDFS**
- **Deployment**
- **Troubleshooting**
- **Configuration – Ranger HDFS**
- **Configuration – Deploy Monitoring Agents**

## Knowledge References

- Default Values, Multiple Collectors  
- IBM Guardium, Cloud Platforms  
- API Reference, IP Aliases  
- Custom Tables, Data Correlation  
- Certificate Restoration, Default Certificates  
- CyberArk SDK, Credential Vault  
- Audit Data Management, Email Integration  
- High Availability, Managed Units  
- GIM Architecture, Troubleshooting  
- HDFS Auditing, Ranger Integration  
- Guardium Deployment, S‑TAP Installation  
- Host IP, Port Configuration  
- GIM Architecture, Customization  
- Guardium V11.3+, API Development, Testing Framework  
- CSV, CEF, Email Notification  
- Managed Units  
- GIM Client, GIM Server  
- Ranger Policy, STAP\_RANGER\_HDFS\_AUDIT\_DIR  

## Keywords

- All Can Control, Collector Configuration, Primary Collector  
- Guardium, Cloud Deployment, Data Activity Monitoring  
- get\_ip\_to\_alias\_overwrites, Parameter Syntax, API Reference  
- Custom Tables, Domains, External Data Integration  
- Restore Certificate, Default Certificate, Custom Certificate  
- CyberArk SDK, Credential Vault  
- Audit Data Management, Email Integration  
- S‑TAP, Collector, JDBC, Browser Service  
- Credential Management, Dynamic Secrets  
- Query Optimization, Testing Framework  
- CSV, CEF, Email Notification  
- High Availability, Managed Units  
- GIM Client, GIM Server  
- HDFS Auditing, Ranger Integration  
- Guardium Deployment, S‑TAP Installation  
- Host IP, Port Configuration  
- GIM Architecture, Customization

## Guardium Reference

### revokeOAuthToken GuardAPI
- **Supported:** Guardium V11.0+
- **Constraints:** Token must be valid, active
- **Workflow:** None
- **Link:** OAuth Integration, API Security

### Log Masked Extrusion Counter
- **Supported:** All Guardium databases
- **Constraints:** None
- **Workflow:** None
- **Link:** Log Masking

### Policy Builder for Policies
- **Supported:** All Guardium policies
- **Constraints:** Requires correct policy configuration
- **Workflow:** None
- **Link:** Security Policy Framework

### Configuration Guidelines
- **Supported:** All Guardium configurations
- **Constraints:** None
- **Workflow:** None
- **Link:** Configuration

## Datasource Connectivity

### Dynamic Port Detection
- **Supported:** SQL Server, Oracle, Db2, MySQL
- **Constraints:** Requires browser service; not supported on z/OS
- **Workflows:** Add Datasource, View Ports
- **Link:** Database Connection Architecture, S-TAP

## Guardium Table Definition

### Modifying Custom Table Schema
- **Supported:** All Guardium data sources
- **Constraints:** Avoid breaking existing reports; version tables
- **Workflow:** Edit Table Schema
- **Link:** Report Lifecycle, Data Modeling

## CAS-based Vulnerability Tests

### CAS Test Definitions and Execution
- **Supported:** All CAS template types with OS scripts
- **Constraints:** Accuracy depends on CAS data freshness
- **Workflow:** Define Test Item, Add CAS Template
- **Link:** CAS Data Collection, Vulnerability Management

## File Transfer Protocol Configuration

### Transfer Method Setup
- **Supported:** FTP, SCP (explicit SFTP)
- **Constraints:** SCP needs SSH key pair; FTP needs firewall rules
- **Workflows:** Set Transfer Method, FTP/SCP Log Monitoring
- **Link:** Data Transfer Security, SFTP Protocol

## GuardAPI Command Parameters

### API Parameter Definitions
- **Supported:** All Guardium GuardAPIs
- **Constraints:** Misconfigured api_target_host causes execution failures
- **Workflow:** Run API Command
- **Link:** API Security, Execution Targets

### api_target_host Details
- **Supported:** All APIs with api_target_host
- **Constraints:** Incorrect value leads to wrong targets
- **Workflow:** Configure Execution Scope
- **Link:** GuardAPI Execution, Clustering

## Guardium Component Ports

### Required Network Ports
- **Supported:** Database collectors, aggregators, central managers
- **Constraints:** Avoid conflicts; follow security policies
- **Workflow:** Open Ports, Network Setup
- **Link:** Network Architecture, Security Configuration

## Defragmentation Settings

### Defrag Command Usage
- **Supported:** All Guardium appliances
- **Constraints:** Requires service restart
- **Workflow:** Set Defrag Size, Restart Service
- **Link:** Performance Optimization, System Configuration

## GuardAPI Function: make_bundle_with_uploaded_kernel_module

### Kernel Module Bundle Creation
- **Supported:** Guardium V9.5+
- **Constraints:** Module compatibility with Guardium release
- **Workflow:** Upload Kernel Module, Create Bundle
- **Link:** GuardAPI Capabilities, Kernel Module Integration

## Job Queue Management

### Scheduled Job Monitoring
- **Supported:** All Guardium appliances
- **Constraints:** UI responsiveness affected by job volume
- **Workflow:** Monitor Jobs

aths:** Requires appropriate permissions

### Workflows with different types
- **Configuration:** Group Management
- **API Execution:** Group API Commands

### Links
- **Knowledge:** Group Management, API Commands
- **Keywords:** Group APIs, Central Management, Hierarchical Groups

```markdown
## Guardium Policy and Incident Management

### Policy Violation Assignments
- **Components:**
  - **Support Matrix:** All Guardium versions and platforms
  - **Limitations/Constraints:** Requires appropriate user permissions
  - **Workflows with different types:** Incident Management — Assign to Incident; Policy Violations — Manual Review
- **Links:**
  - **Knowledge:** Incident Prioritization, Policy Exception Handling
  - **Keywords:** Incident Action, Manual Assignment

### Remote Logging Configuration
- **Components:**
  - **Support Matrix:** Appliances and S-TAP agents
  - **Limitations/Constraints:** Syslog protocol limitations
```

## ## Installation Directory Settings
**Directory must exist before installation** and must **not contain spaces on Windows**. Use the same directory for upgrades to preserve customizations.

## ## Security Anomaly Detection
Requires **activity learning** and **enabled anomaly profiles**. Create policies and investigate details of detected anomalies.

## ## Plug‑In Management
Plug‑ins are **version‑specific** and cannot be used with earlier products. Enable or extend plug‑ins for supported data sources.

## ## GUI Parameter Configuration
Changes to parameters **require a collector restart**. Not all parameters are exposed in the GUI; some handle machine state during failures.

## ## Disk Space Management
Aggregators must **reserve < 30%** of space to avoid performance issues. Monitor utilization and set **disk_space_reserved** thresholds.

## ## Parameter Details for Customization
Parameters are **version‑dependent**; some are deprecated. Update entries via CLI/API and validate catalog file integrity.

## ## Guardium Universal Connector API Suite
Requires **API tokens** and **HTTPS endpoints**. Use APIs for start/stop, filter adjustment, and status monitoring.

## ## Teradata Privilege and Role Overview
Privileges are **hierarchy‑based** with **no superuser role**. Assign and audit system privileges and roles.

## ## Command‑Line Deployments
The `--lb-script` flag is mandatory for load‑balancer integration. Use deployment scripts for Linux/UNIX, Hadoop, and cloud environments.

## ## Azure MySQL Data Source Configuration
An **Azure Admin role** is needed for the client secret, and **TLS 1.2** must be enabled on the MySQL server.

## ## Audit Trail and Event Selection API
Policies must include **Audit Only rules**; API payloads must be JSON. Start selective audits, log events, and correlate incidents.

## Audit and Reporting Domains

### Overview
- Audits data access and policy violations across domains.
- Supports integration with Guardium features.

## Server Metrics Reporting

### Overview
- Monitors server status and resource utilization.
- Displays messages and disk space metrics.

## Additional IP Address Specification

### Overview
- Allows specifying additional IP addresses for scans.
- Supports wildcards and ranges.

## Parameter Execution Variables

### Overview
- Defines variables for executing CLI processes.
- Supports mandatory and optional parameters.

## Collector Aggregator Capacity

### Overview
- Manages capacity of Collector-Aggregator pairs.
- Default limit of 10 Collectors per Aggregator.

## Data Movement Monitoring

### Overview
- Monitors data extraction and ingestion processes.
- Supports Guardium 12.2.x and later.

## Query Rewrite Activation

### Overview
- Activates query rewrite per session upon rule trigger.
- Requires firewall_default_state=0.

## Rollback Procedures

### Overview
- Provides rollback for non-bundle modules.
- Applicable during scratch installs or upgrades.

## MySQL Datasource Configuration

### Overview
- Configures MySQL datasource connections.
- Supports default port 3306 and connection properties.

## Host/Port/Database Connection
- **Components:** Host name/IP, Port number, Database name, Optional connection properties
- **Constraints:** Valid host/IP and port required; Database must exist
- **Workflows:** Setup Datasource; Scan Vulnerability Assessment
- **Links:** Guardium Datasource Configuration, Vulnerability Assessment | datasource host port database connection properties

## DB2 z/OS zSecure Object Dependencies
- **Components:** Support Matrix (Oracle, Microsoft SQL Server, Sybase IQ, Informix, DB2); Platform-specific object dependency reports
- **Workflows:** Reporting Object Dependencies
- **Links:** Object Dependencies Platform-Specific Reporting | DB2 zSecure object dependencies platform-specific

## GuardAPI update_user_db
- **Components:** All supported Guardium platforms
- **Constraints:** Authorization required to update configuration
- **Workflows:** Configuration API Target Hosts
- **Links:** GuardAPI Syntax Database Configuration | GuardAPI update_user_db API target hosts

## CASE Expression Salary Ranges
- **Components:** SQL-compatible databases
- **Constraints:** CASE syntax must be correct
- **Workflows:** Reporting Salary Ranges
- **Links:** SQL CASE Salary Fairness Evaluation | CASE salary ranges fairness categories high medium fair poor

## Trusted vs Untrusted Connections
- **Components:** All Guardium configurations
- **Workflows:** Security Connection Validation
- **Links:** Trust Evaluator Connection Groups | trusted trusted connection untrusted connection guardium connection evaluator

## Risk/Compliance Statistics
- **Components:** All Guardium platforms
- **Constraints:** Requires compliance policies configured
- **Workflows:** Reporting Compliance Statistics
- **Links:** Risk Management Compliance Reporting | risk statistics compliance critical failures datasources vulnerability identification

## Audit Process Receivers
- **Components:** Audit processes with configured receivers
- **Constraints:** Receivers cannot be modified during process execution
- **Workflows:** Post-Processing Modify Receivers
- **Links:** Audit Process Configuration Result Distribution | audit receivers modification process completion recipients results distribution

## GuardAPI api_target_host Parameter
- **Components:** Central manager API executions
- **Constraints:** Valid targets must exist in the configuration
- **Workflows:** Execution API Invocation
- **Links:** Central Manager Configuration API Execution Targets | api_target_host central manager all_managed all group

## Statement Syntax in Session Policies
- **Components:** All Guardium session-level policies
- **Constraints:** Correct syntax required for wildcard or regex matching
- **Workflows:** Policy Session Monitoring
- **Links:** SQL Evaluation Session-Level Policy Syntax | statement STATEMENT wildcard regex SQL evaluation

## Data Security: User Hierarchy & Database Associations
- **Components:** All data security configurations
- **Constraints:** User hierarchy must be established
- **Workflows:** Security Access Control
- **Links:** User Hierarchy Database Associations | user hierarchy database associations data security

## Edit Session-Level Policies
- **Components:** Script-based session-level policies
- **Constraints:** Syntax must be valid
- **Workflows:** Configuration Policy Editing
- **Links:** Script Editor Policy Validation | session-level policy script editor check syntax changes

## LDAP User Import
- **Components:** Guardium LDAP integration
- **Constraints:** LDAP server must be accessible
- **Workflows:** Identity Management User Import
- **Links:** LDAP Integration Guardium User Management | ldap import user addition guardium administrators

## CyberArk SDK Integration
- **Components:** All Guardium-supported databases
- **Constraints:** CyberArk SDK export restrictions apply in some regions
- **Workflows:** Configuration Install CyberArk SDK
- **Links:** Credential Management Dynamic Secrets | CyberArk SDK Credential Vault

## Anomaly Detection Scoring
- **Components:** All Guardium platforms and data sources
- **Constraints:** Requires anomaly detection configured

## License Scoring
Configuration enables scoring for structured logs; scoring not available for unstructured logs.

## Datasource Connectivity
No specific components, limitations, workflows, or links are applicable.

## 704. FIELD
No specific components, limitations, workflows, or links are applicable.

## 705. Discard session (DISCARD_SESSION)
**Workflows:** Configuration – Configure Rules  
**Links:** Session Analysis, Traffic Filtering, S-TAP, Collector, Rule Configuration

## 706. Audit process receivers
**Workflows:** Administration – Configure Monitoring  
**Links:** Audit Process Builder, Notification Setup, Auditing, Reporting, Email Notifications

## 707. FROM policy_violation_view
**Workflows:** Configuration – Reports  
**Links:** Data Queries, Policy Violations, TimestampUTC, DBUserName, ServiceName

## 708. Configuring the HashiCorp Vault
**Workflows:** Configuration – Enable HTTPS  
**Links:** Secret Management, Secure Communication, Vault Server, HTTPS, Secret Transmission

## 709. Sensitivity Description Compliance
No specific components, limitations, or workflows are applicable.  
**Links:** Compliance Identifiers, Regulatory Requirements, SIN, SSN, Work Authorization

## 710. Source application using plain text password
**Workflows:** Security – Monitor Traffic  
**Links:** Security Monitoring, Application Traffic, Plain Text, Security Incident, Network Traffic

## 711. Attribute Description
**Workflows:** Configuration – Manage Attributes  
**Links:** User Attributes, System Administration, Access ID, Attribute Set, Administration

## 712. About this task
**Workflows:** Data Management – Perform Backup  
**Links:** System Backup, Data Preservation, Database, Configuration Files, Virtual Environments

## 713. Threat Detection Analytics
**Workflows:** Security – Detect Threats  
**Links:** Database Security, Threat Analytics, Database Attacks, Suspicious Activity, Analytics

## 714. About this task
**Workflows:** Reporting – Add Custom Fields  
**Links:** Vulnerability Reporting, Custom Fields, Custom Risk Scores, Vulnerability Assessment, Query-Report Builder

## 715. Show command
**Workflows:** Configuration – Modify Security Settings  
**Links:** Password Hashing, GUI Configuration, Password Hashing, Disable SHA1, Security Settings

## 716. Investigation Dashboard
**Workflows:** Monitoring – Use Investigation Tools  
**Links:** Environment Monitoring, Problem Identification, Problem Assessment, Investigative Tools, Guardium Environment

## 717. About this task
No components, limitations, workflows, or links are applicable.

## Data Transfer
**Workflows:** Configuration – Enable Data Transfers  
**Links:** CLI Configuration, SSH Setup

### Viewing Results
- **Components:** SQL policy rule evaluation results
- **Workflows:** Navigation → Policy → View Results
- **Links:** Knowledge → Policy Evaluation, Statement Classification; Keywords → Policy Results, SQL Rules, Evaluation Outcome

## Components Overview

### Log Analysis
- **Support Matrix:** Result set analysis
- **Limitations:** Requires log storage access
- **Workflows:** View Log, Export CSV

### Role Management
- **Support Matrix:** Role-based access control
- **Limitations:** Datasource role assignments required
- **Workflow:** Role Assignment

### Vulnerability Management
- **Support Matrix:** Vulnerability reporting UI (requires license)
- **Workflow:** Unified View, Drill-Down

### Policy Processing
- **Support Matrix:** Policy rule processing modes
- **Limitation:** May increase realtime load
- **Workflow:** Policy Settings

### Port Filtering
- **Support Matrix:** Port filtering configuration
- **Limitation:** Ignored ports excluded from analysis
- **Workflow:** Port Configuration

### Deployment Health
- **Support Matrix:** Deployment health topology view (admin role)
- **Workflow:** Health Topology

### Data Protection Dashboard
- **Support Matrix:** Senior security officer view
- **Limitation:** Summary-only, no drill-down
- **Reference:** Policy Metrics

### Kerberos Authentication
- **Support Matrix:** Guardium authentication
- **Limitation:** Requires krb5.conf and Kerberos credentials
- **Workflow:** Authentication Setup, Config File Upload

### Db2 Memory Adjustment
- **Support Matrix:** Db2 shared memory connections
- **Limitation:** Administrator privileges required
- **Workflow:** Connection Setup

### Health Check Patch
- **Support Matrix:** Guardium system upgrades
- **Limitation:** Must precede major version upgrades
- **Workflow:** Health Check, Pre-Upgrade Validation

### Classification for Sybase
- **Support Matrix:** Classification scans (version 12.1+)
- **Workflow:** Custom Property Setup

### Service Name
- **Support Matrix:** Database user activity indicators
- **Workflow:** User Activity, Source Availability

### Charts and Tables
- **Support Matrix:** Chart details interaction
- **Limitation:** Requires displayed chart
- **Workflow:** View Table, Sort/Filter

### GuardAPI User Update
- **Support Matrix:** Guardium user update
- **Limitation:** Requires API permissions
- **Workflow:** User Management, User Fields Update

## Identify Users with API
### Description
Application Events API enables user identification for connections not detectable from traffic alone.

### Components
- **Support Matrix:** All supported databases
- **Limitation:** API-enabled application required; manual config for legacy systems
- **Workflows:** Register Application Events, View Identified Users

### Links
- **Knowledge:** Application Events, Connection Tracking
- **Keywords:** app-events, API, connection monitoring, user identification

## Guardium Installation Manager (GIM) APIs

**REST endpoints for managing GIM functions** – assigning/canceling/listing/removing/updating modules.

### Components
- **Support Matrix** – Guardium-supported platforms
- **Limitations/Constraints** – GIM client installed; REST API enabled
- **Workflows** – Configuration (assign GIM module) / Management (remove GIM client)

### Links
- **Knowledge** – Guardium Installation Manager, REST API, GIM client  
- **Keywords** – GIM_ENDPOINT, GIM_CLIENT, INSTALL_MODULE, REMOVE_CLIENT  

*The entry is a complete description of the GIM APIs. No additional information is required.*

## IP Identification
IP Identification detects database servers by analyzing network traffic. It works with all Guardium systems but requires observing legitimate connections. Use it in DB Type Identification and IP Anomaly Detection workflows. Keywords: IP Identification, Server IP, Anomaly Detection.

## Single Sign-On SAML Authentication
SAML SSO enables web applications to authenticate users through Guardium. Requires SAML configuration in Guardium. Use in SAML Single Sign-On and SAML Settings workflows. Keywords: SSO, SAML, Authentication, Web Applications.

## Alias and PDF Settings
Configure aliases and PDF footer settings for all Guardium systems. Requires appropriate permissions. Use in Alias Settings and PDF Footer Settings workflows. Keywords: Aliases, PDF Footer, Report Customization.

## Before You Begin
Prepare for Guardium technical support by downloading files and interacting with support representatives. Keywords: File Download, Technical Support, Support Representative.

## Guardium Installation Manager (GIM)
Silently install GIM on Windows with parameters like WINSTAP_INSTALL_DIR and SETTING_QUIET. Use in GIM Silent Install and GIM Parameters workflows. Keywords: GIM, Silent Install, Installation Manager.

## Dynamic Port Detection
Detect database ports for SQL Server, Oracle, Db2, MySQL when the browser service runs. Use in Add Datasource and View Ports workflows. Keywords: S-TAP, Collector, JDBC, Browser Service.

## CyberArk Integration
Integrate Guardium with CyberArk for dynamic credential management. Limited by export restrictions in certain regions. Use in Install CyberArk SDK workflow. Keywords: CyberArk SDK, Credential Vault.

## S-TAP Approval
Manage S-TAP certification in post-v11.4 Guardium releases, required for regulated environments. Use in S-TAP Certification Management workflow. Keywords: S-TAP Approval, Admin Approval, S-TAP Service.

## CLI Login
Access Guardium appliances via CLI, requiring additional configuration for root access. Use in CLI Access workflow. Keywords: cli, guardcli, sudo, admin.

## Big Data Intelligence APIs
Export data to Big Data platforms using Guardium collectors. Requires valid profile_name. Use in Big Data Integration workflow. Keywords: local_enable_big_data_interface, data_export, collector_profile.

## S-TAP Parameters
Configure Kerberos collaboration for S-TAP on Unix Guardium agents in IBM Guardium 11.x+. Use in S-TAP Deployment workflow. Keywords: collaborate_kerberos_enabled, session_policy, krb5.

## Field Description
Configure datasource fields including hostname, port, and schema for all datasource types. Keywords: hostname, port_number, schema_name, default_port.

## Audit Owner
Define audit owners using LIKE operator in reports. Use in Audit Owner Analysis workflow. Keywords: audit_owner, LIKE_operator, report_criteria, filter_settings.

## CSV of the Display Records
Export up to 100,000 records in CSV format from Guardium UI. Adjust export size via CLI. Use in Export Data workflow. Keywords: csv_max_size, export.

## Policy Management

### Using Rules for File Activity Policies
- **Supports:** Guardium File Activity Monitoring (FAM) modules
- **Constraints:** Rules are order-dependent; first match applies
- **Links:** FAM Rule Engine, Conditional Actions

## Database User Interfaces

### GIM Installed Modules
- **Supports:** Guardium Installation Manager (GIM) supported OS
- **Constraints:** Requires GIM client access
- **Links:** GIM Architecture, Module Lifecycle

## Datasource Connectivity

### MS SQL Server Required Fields
- **Required fields:** hostname, port (default 1433)

### PostgreSQL Required Fields
- **Required fields:** hostname, port (default 10000)

### Secure Sockets Layer (SSL) Required Fields
- **Required for:** Secure datasources with SSL enabled

# Guardium Parameter & Workflow Overview

## Alert Verb Number Limit
- **Support:** All versions  
- **Limits:** 1‑50 (default 10)  
- **Workflow:** Configuration → Parameter Settings  
- **Related:** Alert Log, SQL Verb Limit, Parameter Tuning  

## SMIME Alert Signing
- **Support:** 10.5+  
- **Requires:** Provisioned S/MIME keystore  
- **Workflow:** Configuration → Email Settings  
- **Related:** S/MIME, Secure Alert Transport  

## Reporting on Datasources
- **Support:** All releases  
- **Requires:** Datasource discovery enabled  
- **Workflow:** Reports → Datasource Activity  
- **Related:** Datasource Lifecycle, Audit Process  

## Per‑Query Row Limit
- **Support:** 11.0+  
- **Limits:** Must be lower than system Row Count threshold  
- **Workflow:** Policy Builder → Row Count Threshold  
- **Related:** Row Count Enforcement, Sniffer Limits  

## Unix Socket Marker
- **Support:** Unix deployments  
- **Requires:** Correct socket path set  
- **Workflow:** System Settings → Unix Socket Marker  
- **Related:** Guardium Data Collection, UNIX Domain Communication  

## Ranger Monitoring
- **Support:** Ranger‑enabled Hadoop, Guardium 12.0+  
- **Requires:** S‑TAP on edge nodes, Kerberos SPNEGO  
- **Workflow:** Data Streams → Ranger Integration  
- **Related:** Ranger Audit, S‑TAP for Hadoop  

## Analytic Case Parameter Type
- **Support:** Analytic Case feature  
- **Requires:** Value type matches receiver rule column type  
- **Workflow:** Analytic Cases → Parameter Definition  
- **Related:** Analytic Case Engine, Case Builder  

## Custom Search Compare To
- **Support:** 9.5+  
- **Limits:** Single‑column SQL, no complex types  
- **Workflow:** Custom Search → Compare To Clause  
- **Related:** Custom Search Builder, SQL Syntax  

## Credential Stuffing Detection
- **Support:** 11.3+  
- **Requires:** Network Activity policy with rule actions  
- **Workflow:** Policy Builder → Credential Stuffing Detection  
- **Related:** Anomaly Detection, Brute Force Protection  

## Application User Translation
- **Support:** 12.0+  
- **Requires:** Active Application User Translation rules  
- **Workflow:** Access Control → Application User Translation  
- **Related:** User Identification, Entity Mapping  

## Selective Audit Trail
- **Support:** Policy‑level feature  
- **Requires:** Selective Audit Trail in policy  
- **Workflow:** Add Selective Audit Trail → Run Update Policy  
- **Related:** Audit Policy Development, User‑Mapping Rules  

*Unfinished content (e.g., “Client Activity Monito”) was omitted.*

## Guardium Feature Reference

### GuardAPI Syntax
- **Scope:** Guardium Data Protection  
- **Note:** No limitations specified. Used for configuring and managing Guardium through the GuardAPI.  

### User-defined IP Lists
- **Scope:** Guardium Data Protection  
- **Limitation:** Cannot be used with excluded IPs.  
- **Workflow:** Configure IP allowlists or blocklists.  

### F5 BIG-IP Data Monitoring
- **Scope:** Supported F5 BIG-IP versions  
- **Prerequisite:** F5 SDK must be installed.  
- **Configuration Task:** Set up data monitoring for BIG-IP devices.  

### Application User Detection
- **Scope:** All supported databases  
- **Workflow:** Translate application code users to end‑user names for auditing.  

### Guardium Open Traversal Protocol (GOT)

## Policy and Rule Workflows

### Specifying Rule Parameters through Groups
- **Support Matrix:** N/A
- **Constraints:** None
- **Workflow:** Create a group; assign the group to a rule.
- **Knowledge:** Policy Management, Rule Parameters
- **Keywords:** Group, Rule Parameter, Condition, Parameter Group

## System and Database Management

### Resolving Lost Accessmgr Password
- **Support Matrix:** N/A
- **Constraints:** Requires CLI rescue access
- **Workflow:** Reset Accessmgr password via CLI.
- **Knowledge:** Access Management, CLI Troubleshooting
- **Keywords:** rescue, passkey, support reset-password, accessmgr

### Informix Shared Memory Traffic Issue
- **Support Matrix:** All Guardium-supported databases
- **Constraints:** Requires S-TAP Control access
- **Workflow:** Modify Inspection Engine to specify `process_name`.
- **Knowledge:** Activity Monitoring, Inspection Engine
- **Keywords:** inspection_engine, process_name, database_server_command

### Retrieving Client Events via GIM API
- **Support Matrix:** All platforms with GIM installed
- **Constraints:** Requires GIM version 10.1.3 or later
- **Workflow:** Call `gim_get_client_last_event` with `client_id`.
- **Knowledge:** Installation Manager, Client Events, API Usage
- **Keywords:** gim_get_client_last_event, client_id, latest_operation, status_code

## Cloud and On‑Premises Integration

### Connecting Cloud Provider Accounts
- **Support Matrix:** AWS, Azure, Google Cloud
- **Constraints:** Requires IAM credentials
- **Workflow:** Add cloud account and view cloud resources.
- **Knowledge:** Cloud Integrations, IAM, Resource Discovery
- **Keywords:** cloud_account, region, data_store, cloud_provider

## Data Source Configuration

### Field Parameters for JDBC Data Sources
- **Support Matrix:** All JDBC‑compliant databases
- **Constraints:** Host and Port are mandatory
- **Workflow:** Add DataSource; test connection.
- **Knowledge:** JDBC Architecture, Connection Properties
- **Keywords:** host_name, ip_address, port_number, database_name, jdbc_parameter

## Advanced Monitoring and Risk Detection

### AI‑Driven Risk Spotter Policy
- **Support Matrix:** All Guardium deployments
- **Constraints:** Requires Advanced Analytics license
- **Workflow:** Create a risk policy; monitor risk alerts.
- **Knowledge:** Advanced Analytics, Risk Management
- **Keywords:** risk_spotter, policy_creation, risk_alerts

## 977. Close case

### Close case
- **Support Matrix:** All Guardium‑supported platforms
- **Limitations/Constraints:** None
- **Workflows:** Support → Close Case, Incident Management → Resolve
- **Knowledge Areas:** Incident Closure Process, Remedy Workflow
- **Keywords:** Case Resolution, Close Status

## Guardium Features Reference

### Close Case Action
- **Support Matrix:** Guardium 12.2.2 and later
- **Limitations/Constraints:** None

### Ignore Responses per Session
- **Support Matrix:** All supported database platforms
- **Workflows:** Monitoring → Inspection Engine Configuration
- **Knowledge Areas:** Session Architecture, Inspection Engine Behavior
- **Keywords:** S‑TAP, Response Ignoring, Session

### Configuring External Storage
- **Support Matrix:** Amazon S3, Azure Blob, ECS, NFS, Tivoli Storage Manager, IBM COS, IBM Cloud
- **Workflows:** Data Archiving → Export, Storage Configuration → Set External Storage
- **Knowledge Areas:** Data Archiving, External Storage Options, Cloud Storage
- **Keywords:** SCP, FTP, S3, Azure Blob, NFS, TSM, IBM COS

### Groups Column
- **Support Matrix:** All Guardium management nodes
- **Workflows:** Administration → Managed Unit Group Management
- **Knowledge Areas:** Managed Units, Group Types, Role‑Based Access
- **Keywords:** All Units, Custom Subset, Manage Units, Grouping

### GIM Installation for Oracle/Linux
- **Support Matrix:** Linux distributions supported by Guardium
- **Workflows:** Installation → GIM Deployment, Configuration → Store Oracle Parameters
- **Knowledge Areas:** GIM Installation, GuardCTL, Oracle Configuration
- **Keywords:** guardctl, Oracle Instance, Database Home, GIM, Shell Install

### IE_CREATION Parameter

## Guardium Collector Management

**All Guardium Collectors Matrix**
- **Support:** All Guardium collectors
- **Constraints:** Requires Database Discovered Instances Rules configured
- **Workflow:** Inspection Engine Setup — Enable Automatic IE Creation

## Logging Control

**Skip Logging**
- **Support:** All supported database platforms
- **Constraints:** None
- **Workflows:** Policy Management — Construct Logging Settings
- **Related Knowledge:** Construct Logging, Policy Violations, Request Filtering
- **Keywords:** Skip Logging, Logging Control, Policy, Matched Requests

## Client IP/Src Tuple Group

**Client IP/Src Tuple Group**
- **Support:** All Guardium data sources
- **Constraints:** None
- **Workflows:** Reporting — Query Builder, Alerts — Rule Definition
- **Related Knowledge:** Source Identification, Client Information, Tuple Groups
- **Keywords:** Client IP, Client MAC, Client OS, App/User

## CAS Agent

**CAS Agent Component**
- **Support:** All supported database platforms
- **Constraints:** None
- **Workflows:** Configuration Management — CAS Setup
- **Related Knowledge:** Configuration Auditing, S-TAP Integration, Independent Components
- **Keywords:** CAS Agent, Config Change, Guardium System, Database Server

## Guardium Collector Use Cases

**When to Use Guardium Collectors**
- **Support:** Guardium versions supporting collectors
- **Constraints:** None
- **Workflows:** Data Collection — Collector Deployment
- **Related Knowledge:** Data Retention, Reporting, Analytics, Collector Benefits
- **Keywords:** Collectors, Rapid Querying, Query Data, Analytic Workloads

## SNMP Data Retrieval

**SNMP Data Retrieval**
- **Support:** SNMP‑compatible Guardium collectors
- **Constraints:** None
- **Workflows:** Monitoring — SNMP Setup
- **Related Knowledge:** SNMP Commands, SQL Guard Data, SNMP Retrieval
- **Keywords:** snmpget, snmpwalk, SNMP, SQL Guard, UI Tools

## Cold Storage Ingestion Logs

**Cold Storage Ingestion Logs Report**
- **Support:** Guardium Enterprise and upper tiers
- **Constraints:** Requires cold storage integration
- **Workflows:** Reports — Guardium Operational Reports
- **Related Knowledge:** Long-Term Retention, Ingestion Process, Error Reporting
- **Keywords:** Cold Storage, Ingestion Logs, Report, Error Messages

## GIM Global Parameters

**GIM Global Parameters**
- **Support:** All GIM‑enabled Guardium appliances
- **Constraints:** None
- **Workflows:** GIM Configuration — Global Settings
- **Related Knowledge:** Secure Communication, Unauthenticated GIM, SSL Encryption
- **Keywords:** enable_secure_unauthenticated_communication, Global Parameter, SSL Port 8444

## CLI Command Abbreviations

**CLI Command Abbreviations**
- **Support:** All installed Guardium CLI interfaces
- **Constraints:** None
- **Workflows:** CLI Usage — Command Abbreviation
- **Related Knowledge:** CLI Syntax, Command Shortening, Unambiguous Abbreviations
- **Keywords:** CLI, Abbreviate, show, sho, Command Reduction

## Backup Operations

**Backup Operations**
- **Support:** All supported Guardium backup mechanisms
- **Constraints:** None
- **Workflows:** Administration — Backup Management, Disaster Recovery
- **Related Knowledge:** Backup Processes, Backup Procedures
- **Keywords:** Backup, Operation, Interaction

## Vulnerability Assessment

**Manage AWS Data Streams**
- **Support:** AWS data streams
- **Constraints:** None listed
- **Workflows:** Configuration — get_test_result_detail_string_setting
- **Related Knowledge:** Vulnerability Assessment, Test Result Storage
- **Keywords:** TEST_RESULT_DETAIL, TEST_RESULT, Vulnerability Scanning, Data Streams

**Create New Rule Action**
- **Support:** Rule Builder Interface
- **Constraints:** Requires policy editor permissions
- **Workflows:** Configuration — Add New Action
- **Related Knowledge:** Policy Management, Rule Actions
- **Keywords:** Rule Builder, Policy Editor, Rule Actions, Security Policies

## Datasource Connectivity

**Dynamic Port Detection**
- **Support:** SQL Server, Oracle, Db2, MySQL
- **Constraints:** Requires browser service running; not supported on z/OS
- **Workflows:** Configuration — Add Datasource; Navigation — View Ports
- **Related Knowledge:** Database Connection Architecture, Browser Service
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

**CyberArk Integration**
- **Support:** All Guardium-supported databases
- **Constraints:** CyberArk SDK export restrictions apply in some regions
- **Workflows:** Configuration — Install CyberArk SDK
- **Related Knowledge:** Credential Management, Dynamic Secrets
- **Keywords:** CyberArk SDK, Credential Vault

## Database Discovery

**Databases Discovered Report**
- **Support:** DB2, Oracle, MySQL, Informix, PostgreSQL
- **Constraints:** Auto‑discovery does not detect ports using non‑standard services (e.g., custom listeners); manual whitelist needed for encrypted ports
- **Workflows:** Configuration — Add Datasource; Navigation — View Discovered Ports
- **Related Knowledge:** Auto‑discovery Process, Endpoint Scanning
- **Keywords:** CLI, lo

## audit only
Components: Support Matrix (Selective Audit Trail), Limitations/Constraints (rule specification, no data values), Workflows (Apply Audit Only, Check Logs). Links: Knowledge (Audit Trail Mechanics), Keywords (rule construct, log entry, Guardium Policy).

## import multiple databases
Components: Support Matrix (DB2, ORACLE, INFORMIX, MYSQL), Limitations/Constraints (valid import file, cannot import active compliance runs), Workflows (Import Settings, Scheduled Import). Links: Knowledge (Compliance Data Hygiene), Keywords (import icon, Applications tab, datasource entries).

## domain based on query main entity
Components: Support Matrix (Threat Analytics Open Cases), Limitations/Constraints (fixed default time window), Workflows (Open Cases, Set From). Links: Knowledge (Threat Analytics Workflow), Keywords (threat case, runtime parameter, time filter).

## attribute description
Components: Support Matrix (Server Type in data streams), Limitations/Constraints (Service Name alias varies by OS), Workflows (Server Monitoring, Service Name Validation). Links: Knowledge (Server Monitoring Configuration), Keywords (DB2 type, Oracle service name, Teradata interaction).

## deploy external s-tap manually
Components: Support Matrix (Docker 20.x+), Limitations/Constraints (SSL certificate signed by trusted CA, no manual editing), Workflows (Docker Deployment, SSL Verification). Links: Knowledge (S-TAP Deployment), Keywords (Docker script, signed certificate, external S‑TAP).

## basel ii dml distribution
Components: Support Matrix (Basel II regulatory framework), Limitations/Constraints (financial data schema required), Workflows (Client IP Activity, DML Operations). Links: Knowledge (Change Detection), Keywords (DML operations, client IP activity, financial data monitoring).

## monitor and audit
Components: Support Matrix (Security monitoring policies), Limitations/Constraints (must be installed before rule enforcement), Workflows (Enable Monitoring, Admin Activity). Links: Knowledge (Security Policy Installation), Keywords (privileged activity, application monitoring, compliance report).

## view status history
Components: Support Matrix (Status History view in Data Stream Management), Limitations/Constraints (separate timelines per collector), Workflows (View Timeline, Timeline Interpretation). Links: Knowledge (Monitoring Timeline Analysis), Keywords (status changes, timestamp, collector timeline).

## find name in sql query example
Components: Support Matrix (SQL queries in session‑level policies), Limitations/Constraints (no regular expressions), Workflows (Add SQL Rule, Send Alert). Links: Knowledge (Session Policy Mechanics), Keywords (SQL query, name detection, policy alert).

## test detail exceptions
Components: Support Matrix (Exception groups in test configurations), Limitations/Constraints (cannot overlap existing exception rules), Workflows (Add Exception Group, Fine‑Tune Properties). Links: Knowledge (Exception Handling in Testing), Keywords (exception group, test properties, detailed exceptions).

## date formats
Components: Support Matrix (timestamp formats in logging), Limitations/Constraints (unsupported custom formats), Workflows (Choose Format, Parse Timestamp). Links: Knowledge (Timestamp Standards), Keywords (epoch milliseconds, formatted timestamp, log parsing).

## guardium requirements
Components: Support Matrix (Guardium versions with Intelligent Change Detection), Limitations/Constraints (valid license required), Workflows (Enable Change Detection, Confirm History Updates). Links: Knowledge (Change Detection Mechanism), Keywords (Intelligent Change Detection, key-value pairs, compliance update).

## teradata configuration
Components: Support Matrix (Teradata Gateway 16.x+), Limitations/Constraints (only if Guardium enabled on gateway), Workflows (Gateway Settings, Check SendConnectRespNoSecurity). Links: Knowledge (Teradata Gateway Security Settings), Keywords (gtwcontrol).

# Guardium Data Protection Documentation

## Show Command Syntax
Provides the syntax for executing commands related to security auditing. Links to Command Syntax and Security Auditing knowledge areas.

## User Defined Parameters
Allows users to extend Guardium Data Protection with custom parameters for policies and reports. Supported on all Guardium platforms with limitations on API access and addition through the Admin Console.

## Enumerate Shares via REST API
Details the API endpoint for listing shares, requiring Power Users permission and admin role. Links to REST API Permissions, Access Control Model, and Anchor Roles.

## TDS Packet Limit Configuration
Adjusts the maximum number of packets inspected by the TDS Packet Limit, with a default of 5 packets. Affects performance significantly. Links to Inspection Engine and Data Transfer Protocol.

## Update External Stap Configuration API
Updates external Stap configurations with `stapHost`, optional `category`, and `GroupType`. Links to Configuration Management and External Stap.

## ALTER Command Auditing
Audits ALTER SQL commands, requiring database monitoring. Links to DDL Auditing and Database Activity Monitoring.

## Reapply Security Policy
Reinstalls security policies on managed units. Links to Policy Builder and Managed Unit Configuration.

## Upgrade S-TAP for IBM i
Details upgrading S-TAP for IBM i via FTP. Links to Agent Installation and IBM i Integration.

## Monitor NAS and SharePoint
Guides monitoring NAS devices and SharePoint with Windows agents. Links to File Monitoring and Data Loss Prevention.

## MySQL Data Source Configuration
Configures MySQL connections with host, port, and JDBC properties. Links to JDBC Configuration and Data Source Setup.

## REQUEST_ERROR Policy Action
Handles session-level policy errors. Links to Session Policy and Error Detection.

## Java Stack Environment Overview
Summarizes the Java stack for SAP portals, focusing on smaller databases. Links to SAP Architecture and Java Platform.

## Security Test Description
Describes security test prerequisites for SQL-based assessments. Links to Assessment Tests and SQL Test.

## Health Dashboard Summary
Displays real-time health status of Guardium components. Links to Health Monitoring and System Status.

## Policy Alert Configuration via SNMP
Configures policy alerts with SNMP requirements. Links to Policy Alert Configuration.

## ## Policy Management

### Policy Builder and Rule Entity
- **Components:** All IBM Guardium installations
- **Limitations:** Search capabilities depend on GuardAPI modules; rule definitions must follow Guardium syntax
- **Workflows:** Configuration — Define Policies; Navigation — Rule Management
- **Knowledge:** Access Policies, Segmentation Policies
- **Keywords:** GuardAPI, Rule Sets, Policy Definition, Compliance Rules

### Distribution of Configurations
- **Components:** Physical and virtual Guardium appliances, S-TAP agents
- **Limitations:** Requires central manager setup; custom tables need schema validation
- **Workflows:** Configuration — Profile Distribution; Navigation — Configuration Props
- **Knowledge:** Enterprise Wide Deployment, Guardium Certificates
- **Keywords:** Central Manager, Configuration Propagation, Appliance Certificates

## ## Reporting and Alerts

### Email Notifications
- **Components:** Guardium Data Protection with SMTP server access
- **Limitations:** External recipients need monitored email availability; internal users need Guardium portal access
- **Workflows:** Configuration — Alert Setup; Navigation — Email Configuration
- **Knowledge:** Alert Configuration, SMTP Integration
- **Keywords:** Alert Thresholds, Notification Settings, SMTP Server, Alert Types

### Throughput (graphical) Report
- **Components:** Guardium installations with throughput monitoring enabled
- **Limitations:** Visualization depends on Data Collector health; time range limited by data retention settings
- **Workflows:** Navigation — Throughput Visualization; Configuration — Enable Throughput Monitoring
- **Knowledge:** Throughput Metrics, Distributed Label Line Charts
- **Keywords:** Access Counts, Period Start, Visualization, Data Retention

## ## Security and Compliance

### Database Protocol and User Identification
- **Components:** All supported database protocols (e.g., JDBC, ODBC)
- **Limitations:** Requires accurate database credential management; DB_USER identification depends on privileged user access
- **Workflows:** Configuration — Database Identification; Navigation — Policy Tuning
- **Knowledge:** Credential Management, Granular Policy Definition
- **Keywords:** DB_PROTOCOL, DB_TYPE, Database Users, Policy Granularity

### CyberArk Integration for Credential Vaulting
- **Components:** Guardium systems supporting CyberArk SDK
- **Limitations:** SDK export restrictions may affect availability in certain regions; credential vaulting requires initial vault setup
- **Workflows:** Configuration — CyberArk Integration Setup
- **Knowledge:** Credential Vaulting, Security Secrets
- **Keywords:** CyberArk SDK, Vault Credentials, Credential Vault, Privilege Management

### Security Entitlement Optimization
- **Components:** All Guardium configurations enforcing least privilege
- **Limitations:** Balancing business needs with security requires periodic access reviews; tool effectiveness depends on existing policy baselines

Workflows with different types: Administration — Entitlement Review
- Knowledge: Least Privilege Principle, Access Review Processes
- Keywords: Least Privilege, Access Balancing, Security Entitlements, Policy Tuning

---

Workload and Performance Management

Throughput (graphical)
Components:
Support Matrix: Guardium versions supporting graphical reporting
Limitations/Constraints: Requires throughput monitoring enabled; graph granularity depends on data collector sampling rates
Workflows with different types: Navigation — Graphical Reports
Links:
Knowledge: Performance Dashboards, Monitoring Workloads
Keywords: Throughput Reporting, Graphical Analysis, Sampling Rates, Data Collection

Multi-thread Assessment Execution
Components:
Support Matrix: Guardium installations with hardware supporting multi-threading
Limitations/Constraints: Assessment performance depends on hardware capabilities; results may vary with concurrent system loads
Workflows with different types: Configuration — Vulnerability Assessment Setup
Links:
Knowledge: Vulnerability Scanning, Multi-core Optimization
Keywords: Assessment Threads, Parallel Execution, Performance Optimization, Vulnerability Scanning

---

Troubleshooting and Diagnostics

Diagnostic Flats Logs
Components:
Support Matrix: All Guardium appliances
Limitations/Constraints: Log analysis requires expertise in Guardium error handling; frequent alerts may indicate system overload
Workflows with different types: Troubleshooting — Log Review
Links:
Knowledge: Log Analysis, System Health Checks
Keywords: Flat Logs, Error Rates, Queue Management, Log Analysis

TCP/IP Exceptions Logging
Components:
Support Matrix: Guardium configured to log network exceptions
Limitations/Constraints: Exception logging may impact network performance; detailed analysis needs network packet context
Workflows with different types: Diagnostics — TCP Exception Investigation
Links:
Knowledge: Network Diagnostics, Exception Handling
Keywords: TCP Exceptions, IP Logging, Network Exceptions, Exception Analysis

---

Search Action Matching

Search Pattern Detection
Components:
Support Matrix: Standard search operators (wildcards, regular expressions), custom search plugins
Limitations/Constraints: Default `DB_USER:guardium://empty` matches only when no actual user is present; exact-match, case‑insensitive; cannot use multiple conditions simultaneously without a plugin
Workflows with different types: Configuration — Define Search Criteria; Navigation — Execute Search
Links:
Knowledge: Search Engine Architecture, Default DB_USER Handling
Keywords: search_criteria, default_user, guardium_empty, plugin_api

---

Guardium Data Monitoring

Guardium 1120. Network Mirroring Methods
Components:
Support Matrix: SPAN, N-TAP (Network Tap)
Limitations/Constraints: Requires network hardware support; not applicable when S-TAP can be installed
Workflows with different types: Data Capture — SPAN, Data Capture — N-TAP
Links:
Knowledge: Inspection Engines, Network Architecture
Keywords: SPAN, N-TAP, Mirroring, Inspection Engine

Guardium 1117. Investigation Dashboard APIs
Components:
Support Matrix: All Guardium versions with dashboard module
Limitations/Constraints: Requires API access permissions
Workflows with different types: Dashboard Access — Open, Search — Execute
Links:
Knowledge: API Documentation, Dashboard Controls
Keywords: Investigation Dashboard, API, Search Execute

Guardium 1118. Viewing Drill-Down Reports
Components:
Support Matrix: All GUI-enabled Guardium releases
Limitations/Constraints: None
Workflows with different types: Report View — Open, Navigation — Drill Down
Links:
Knowledge: Report Configuration, User Interface
Keywords: Drill-Down, Context Menu, Tabular Report

Guardium 1119. Client/Server OS Indicators
Components:
Support Matrix: All supported client/server operating systems
Limitations/Constraints: DEC indicator only for legacy DEC Alpha servers
Workflows with different types: Configuration — Client OS, OS Detection — Automatic
Links:
Knowledge: OS Compatibility Matrix, Data Format Types
Keywords: IEEEM, IEEEI, DEC, OS Indicators

Guardium 1116. Suspicious Administrative Activity
Components:
Support Matrix: All Guardium installations
Limitations/Constraints: None
Workflows with different types: Alert — Generate, Monitoring — Administrative Activity
Links:
Knowledge: User Management, Alerting Mechanisms
Keywords: Admin Rights, Intrusion Detection

Guardium 1115. Search Offset Parameter
Components:
Support Matrix: All Search APIs
Limitations/Constraints: Advanced use; may affect performance
Workflows with different types: Search — Configure, Pattern Matching — Enable
Links:
Knowledge: Regular Expressions, Search Syntax
Keywords: SEARCH_OFFSET, Matching, Pattern

Guardium 1114. Edge Gateway Deployment
Components:
Support Matrix: Kubernetes versions supported by Guardium Edge Gateway
Limitations/Constraints: Requires compatible storage classes; resource limits may affect performance
Workflows with different types: Deployment — Configuration, Resource Allocation — K8s
Links:
Knowledge: Kubernetes Deployment, Storage Configuration
Keywords: Kubernetes, Storage Class, Resource Specs

Guardium 1113. GuardAppUserReleased Workflow
Components:

## Default Roles

**Description:** Default roles supplied with Guardium include admin, user, access manager, and investigations.

**Components:**
- Support Matrix: All Guardium deployments
- Limitations/Constraints: None
- Workflows: Configure roles, modify role settings

**Links:**
- Knowledge: Role management, privilege hierarchy, access controls
- Keywords: admin, user, access manager, investigation, role creation, role hierarchy

## Verify Collector Certificate

**Description:** Ensures S‑TAP clients validate the collector’s TLS certificate before establishing a secure connection.

**Components:**
- Support Matrix: Platforms with TLS-enabled collectors
- Limitations/Constraints: TLS must be enabled on the collector
- Workflows: Configure security settings → verify certificate

**Links:**
- Knowledge: TLS/SSL configuration, S‑TAP communication
- Keywords: S‑TAP, collector certificate, TLS verification, security settings

## Parameter Value Type Description

**Description:** Details the `create_quarantine_allowed_until` parameter, accepting a date‑time string (`YYYY‑MM‑DD hh:mm:ss`) or a relative expression like `NOW+1HOUR`, plus a `dbUser` string for the targeted database login.

**Components:**
- Support Matrix: Guardium APIs that support quarantine actions
- Limitations/Constraints: Date format must be precise; relative expressions are evaluated at execution time
- Workflows: Configure quarantine settings

**Links:**
- Knowledge: API parameter types, quarantine mechanism, GuardAPI reference
- Keywords: create_quarantine_allowed_until, NOW+1HOUR, dbUser

## Select Session (SELECT_SESSION)

**Description:** Complementary filter to **Ignore Session**; enables the sniffer to drop sessions that do not match specified criteria, reducing unnecessary traffic.

**Components:**
- Support Matrix: Guardium versions with session filtering
- Limitations/Constraints: Criteria must be defined in sniffer configuration
- Workflows: Configure session filtering → select sessions

**Links:**
- Knowledge: Session filtering, sniffer architecture, traffic management
- Keywords: SELECT_SESSION, ignore session, sniffer, traffic filtering, session criteria

## GuardAPI Syntax

**Description:** GuardAPI commands follow a consistent syntax; e.g., `delete_alias` requires `dbValue` and `groupTypeDesc`. Full valid type list is available via `guardium > help`.

**Components:**
- Support Matrix: All Guardium versions with GuardAPI
- Limitations/Constraints: Commands must be properly formed

## Entitlement Optimization APIs

### Description
Activates the File‑Activity Monitoring file‑metadata crawler.

### Limitations/Constraints
Requires proper configuration of the file‑metadata collector agent.

### Keywords
enable_fam_crawler, FAM crawler, file metadata, data discovery

---

## GuardAPI Examples

### Description
Transfers a keystore between Guardium components.

### Limitations/Constraints
Both source and destination components must be reachable over the network.

### Keywords
pull_external_stap_keystore, keystore, external S‑TAP, Guardium components

---

## GRDAPI Update External S‑TAP Configuration

### Description
Specifies which active S‑TAPs can connect to the collector using pattern‑matching on `stapHost`. Flag `TAP.all_can_control:1` determines if any S‑TAP can control.

### Limitations/Constraints
Requires correct `stapHost` patterns.

### Keywords
grdapi, update_external_stap_config, stapHost, all_can_control, S‑TAP configuration

---

## GuardAPI Syntax Update Test Detail Exception

### Description
Updates the `test_detail_exception` setting with parameters `assessmentDesc`, `datasourceGroup`, `datasourceName`, and `exceptionType`.

### Limitations/Constraints
Parameters must conform to defined data types and allowed value sets.

### Keywords
update_test_detail_exception, assessmentDesc, datasourceGroup, datasourceName, exceptionType

---

## Investigation Dashboard APIs

### Description
Enables, disables, and configures the Investigation Dashboard, including Quick Search Results Table and predefined charts.

### Limitations/Constraints
Requires appropriate user permissions.

### Keywords
investigation dashboard, enable API, disable API, quick search results, pre‑defined charts

---

## File Activity Policies Using Rules

### Description
Monitors file changes on Windows, UNIX, NAS, and SharePoint with manually authored or auto‑generated rules.

### Limitations/Constraints
Requires FAM agent version compatibility with Guardium release.

### Keywords
file activity monitoring, FAM policies, file changes, Windows, UNIX, NAS, SharePoint, investigative dashboard

---

## Guardium Installation Manager

### Description
Centralized tool for installing, maintaining, and upgrading Guardium components via a GIM server and GIM client.

### Limitations/Constraints
Requires network connectivity between GIM server and clients; certain OSes may need additional prerequisites.

### Keywords
Guardium Installation Manager, GIM server, GIM client, installation, upgrade, managed systems

---

## Active Threat Analytics Setup

### Description
Enables and manages Threat Finder and DAM Outlier Mining across the Guardium environment or specific managed units.

### Limitations/Constraints
Requires Threat Analytics license; proper configuration of the Threat Analytics module.

## Data Sources
**Description:** Workflows with different types: Administration — Threat Analytics → Setup

**Links**
- **Knowledge:** Threat Analytics, Threat Finder, DAM Outlier Mining, Managed Unit Configuration
- **Keywords:** active threat analytics, threat finder, DAM outlier mining, setup, configuration, managed units

## Analyzer Lost
**Description:** Logger Rate indicates the volume of parsed SQL traffic (in megabytes per minute) that Guardium’s internal MySQL database receives. It reflects the rate at which the Guardium Logger processes incoming traffic components.

**Components**
- **Support Matrix:** All Guardium versions with Logger enabled
- **Limitations/Constraints:** High traffic volumes can affect database performance; monitor rate closely
- **Workflows with different types:** Monitoring — Logger Statistics → View Rate

**Links**
- **Knowledge:** Logger Functionality, Traffic Analysis, Performance Monitoring
- **Keywords:** logger rate, SQL traffic, megabytes per minute, Logger, traffic components, performance monitoring

## Data Source Parameters
**Description:** Changing KAFKA_CONNECT_HEALTH_FREQUENCY

**Components**
- **Support Matrix:** Kafka connector environments
- **Limitations/Constraints:** Valid range 1‑1000 seconds; parameter requires restart of connector
- **Workflows with different types:** Configuration — Update Parameter

**Links**
- **Knowledge:** Connector Health Monitoring, Parameter Configuration
- **Keywords:** KAFKA_CONNECT_HEALTH_FREQUENCY, Kafka, Connector Health

## Data Management
**Description:** Switching DB and OS Users

**Components**
- **Support Matrix:** All supported Guardium database types
- **Limitations/Constraints:** None
- **Workflows with different types:** Configuration — Switch User

**Links**
- **Knowledge:** User Management, Multi‑User Environments
- **Keywords:** DB User, OS User, Impersonation, cf234b2e

### Policy Rule Actions
**Components**
- **Support Matrix:** All policy‑capable Guardium versions
- **Limitations/Constraints:** None
- **Workflows with different types:** Enforcement — Block, Alert, Log

**Links**
- **Knowledge:** Policy Engine, Rule Evaluation
- **Keywords:** Policy Rule, Block, Alert, Log, 9f6159f3

## ## Show Command

### Support Matrix
- Guardium CLI

### Limitations/Constraints
- None

### Workflows
- Monitor SMTP Authentication (Configuration)

### Links
- Knowledge: Administration, Reporting  
- Keywords: Show, SMTP Authentication, auth, none, 1161  

---

### Show Command (Policy Simulation)

### Support Matrix
- Guardium V12+

### Limitations/Constraints
- None

### Workflows
- Policy Simulation (Testing)

### Links
- Knowledge: Policy Simulation, Rules Engine  
- Keywords: store allow_simulation, enable, disable, 1162  

---

### Role Validation for GuardAPI Commands

### Support Matrix
- All Guardium roles

### Limitations/Constraints
- None

### Workflows
- Role Assignment (Administration)  
- Command Permission (Validation)

### Links
- Knowledge: Role‑Based Access Control, Command Security  
- Keywords: Role Validation, GuardAPI, Command Permission, bb17a930  

---

## 1178. System IP Address

Parameter that specifies which network interfaces or IP addresses to monitor or include in reports.

---

## 1180. Profile Comparison

Compares different stack analysis profiles to identify configuration differences.

---

## 1181. Dashboard description

Explains the purpose and functionality of the dashboard.

---

## 1182. Default Overwrite

Determines the default behavior for overwriting existing data/configurations.

---

## 1183. Show audits by category

Filters audit records by specific types or criteria.

---

## 1184. Loggable change

Entity that represents auditable changes in the system.

---

## ## Scheduled Jobs

### Parameter Value type Description
- **Support Matrix:** Not applicable  
- **Limitations/Constraints:** Default value is DAM; other types validated against documentation  
- **Workflows:** DAM_FAM parameter configuration (Configuration)  

### Links
- Knowledge: Enable Outliers Detection, Parameter Configuration  
- Keywords: DAM, DAM_FAM, outliers, enable_outliers_detection  

---

## ## 1192. MS SQL Server (DataDirect - Dynamic Port)

### Support Matrix
- MS SQL Server  

### Workflows
- Add Datasource (Configuration)  
- Manage Data Sources (Navigation)  

### Links
- Knowledge: Dynamic Port Detection, DataDirect Driver  
- Keywords: S-TAP, DataDirect, dynamic port  

---

## ## 1193. Objects List

### Support Matrix
- All Guardium-supported databases  

### Workflows
- Objects List (Reporting)  

### Links
- Knowledge: Access Period Entity, Hourly Aggregation  
- Keywords: object_enumeration, period_start, Access Period  

---

## ## 1194. Changes are not saved when you add an inspection engine

### Support Matrix
- All Guardium-supported platforms  

### Limitations/Constraints
- Requires correct parameter syntax  

### Workflows
- Install Inspection Engine (Configuration)  

### Links
- Knowledge: Parameter Validation, Inspection Engine Configuration  
- Keywords: inspection_engine, validate_parameters, configuration  

---

## ## 1195. OS user in group of Oracle DBAs

### Support Matrix
- Oracle databases  

### Limitations/Constraints
- Requires correct protocol specification  

### Workflows
- Create/Rules (Configuration)  
- View Rules (Navigation)  

### Links
- Knowledge: Oracle Bequeath Protocol, Failed-Login Alerts  
- Keywords: bequeath_protocol, ORA-01017, rule_condition  

---

## ## 1196. Customizing the user interface

### Support Matrix
- Guardium appliances  

### Workflows
- UI Settings (Configuration)  
- Dashboard (Navigation)  

### Links
- Knowledge: Active Threat Analytics, Risk Spotter  
- Keywords: UI_customization, risk_dashboard, investigation_workflow  

---

## ## 1197. MS SQL Server (Microsoft - Dynamic Port)

### Support Matrix
- MS SQL Server  

### Workflows
- Add Datasource (Configuration)  
- Manage Data Sources (Navigation)  

### Links
- Knowledge: Dynamic Port Detection, Microsoft Driver  
- Keywords: S-TAP, Microsoft, dynamic_port  

---

## ## 1198. Charts and graphs

### Support Matrix
- Guardium reporting module  

### Workflows
- Create Chart (Reporting)  
- Reports (Navigation)  

### Links
- Knowledge: Data Visualization, Activity Monitoring  
- Keywords: chart, graph, data_trend, anomaly_detection  

---

## ## 1199. Rule Action Entity

### Support Matrix
- All Guardium policy frameworks  

### Workflows
- Create Rule (Configuration)  
- View Actions (Navigation)  

### Links
- Knowledge: Policy Rule Engine, Rule Sequence  
- Keywords: rule_action, sequence_number, policy_execution  

---

## ## 1200. Managing roles and permissions

### Support Matrix
- All Guardium access control systems  

### Workflows
- Manage Roles (Administration)  
- User Management (Navigation)  

### Links
- Knowledge: Access Control, Role‑Based Access  

[End of compressed documentation]

## Guardium Feature Reference

### 1207. Prerequisites for Windows
- **Support Matrix:** Microsoft .NET 4.5 or later  
- **Workflow:** Configuration — Install CAS  
- **Knowledge:** CAS Installation, Disk Requirements  
- **Keywords:** .NET Framework, CAS, Disk Space  

### 1208. About this task
- **Support Matrix:** All Guardium platforms  
- **Workflow:** Configuration — Create Profile  
- **Knowledge:** Profile Management, Managed Units  
- **Keywords:** Configuration Profile, Managed Unit, Scheduling  

### 1209. Show command
- **Support Matrix:** All versions supporting PDF generation  
- **Workflow:** Configuration — Set PDF Fonts  
- **Knowledge:** PDF Configuration, Multilingual Support  
- **Keywords:** show pdf-config, PDF Fonts, Multilingual  

### 1210. GuardAPI example
- **Support Matrix:** Guardium 11.0 and later (API access required)  
- **Workflow:** Administration — User Management  
- **Knowledge:** GuardAPI, API Reference  
- **Keywords:** delete_allowed_db_by_user, API Call, User Mapping  

### 1211. Solr APIs
- **Support Matrix:** Guardium 12.0+  
- **Workflow:** Diagnostics — Solr Monitoring  
- **Knowledge:** Solr Status, System Diagnostics  
- **Keywords:** get_solr_status, get_solr_status_extended, Solr Health  

### 1212. Full SQL - Schema tampering
- **Support Matrix:** All data sources supported for Full SQL  
- **Workflow:** Reporting — Full SQL Analysis  
- **Knowledge:** Full SQL, Schema Tampering Detection  
- **Keywords:** Full SQL, Schema Tampering, Filtered Report  

### 1213. Active Users with no Activity
- **Support Matrix:** All Guardium reporting features (active-reporting required)  
- **Workflow:** Reporting — Inactive Users  
- **Knowledge:** User Activity Monitoring, Reporting Periods  
- **Keywords:** Active Users, No Activity, Inactive Report  

### 1214. Attribute Description
- **Support Matrix:** All policies and reports using attributes  
- **Workflow:** Configuration — Attribute Mapping  
- **Knowledge:** Policy Attributes, Event Attributes  
- **Keywords:** Application User, Execution Time, Policy Fields  

### 1215. Attribute Description
- **Support Matrix:** All attribute-enabled features  
- **Workflow:** Configuration — Attribute Documentation  
- **Knowledge:** Attribute Fields, API Documentation  
- **Keywords:** Application User, GuardAppUser, Average Execution  

### 1216. Log Records
- **Support Matrix:** All GIM-enabled data sources (AWS, Couchbase, Hadoop, DB2 stream mode excluded)  
- **Workflow:** Reporting — Log Details  
- **Knowledge:** Log Data Capture, GIM Limitations  
- **Keywords:** Log Records, SQL Statement, Data Source Types  

### 1217. What to do next
- **Support Matrix:** Guardium Kafka integration (requires existing Kafka cluster)  
- **Workflow:** Not completed — additional information needed

## 1218. Enable/Disable GIM Server Log
Enable or disable the Guardium Inspection Engine Management (GIM) server log.

## 1219. Show Command
Display command details for the Inspection Engine. Use the `max_result_set_size` parameter.

## 1220. Authentication Report
Generate an authentication audit report for Guardium Central Management and managed units. Requires audit policies.

## 1235. Entitlement Optimization What's New
- **Supported in:** Guardium 12.5+  
- **Works with:** Entitlement Optimization feature enabled  
- **Areas:** Configuration → Optimize Entitlements; Navigation → View Entitlement Reports  
- **Key terms:** Entitlement Optimization, Access Control, Compliance, Auditing

## Entitlement Optimization → What's New Tab
- **Supported in:** All appliances with the feature enabled  
- **Area:** Reporting → Weekly Summary  
- **Key terms:** Appliance Enable, Weekly Report, Entitlement Changes

## Vulnerability Assessment Integration

### Configuring Vulnerability Scanner Agents
Supported scanners: Nessus, Qualys, Rapid7. Requires agent installation (except on z/OS).

### CVE Information Reports
Supported in Guardium 12.0+. Provides CVE details, patch status, and security advisories.

## Guardium Feature Reference

### Application Objects Summary
Lists application objects across all supported Guardium platforms.

### Attribute Description
Describes session attributes such as Session ID and Timestamp for supported databases.

### GIM Charts
Monitoring and configuration of GIM client status on Linux, UNIX, Windows. Affect S‑TAP upgrade status.

### Deployment Inventory
Provides an aggregated view of Guardium deployments (Central Manager, Managed Units).

### Edit External S‑TAP Group Tab
Edit the name and configuration of an External S‑TAP group.

### Enable Outliers Detection Cross CM AGG
Enables cross‑aggregator outlier detection when DAM_FAM is enabled.

### Buffer Usage Monitor Report
Monitors buffer utilization for active data processing. Use to tune buffer sizes.

## Datasource Connectivity

### Dynamic Port Detection
- **Components:** SQL Server, Oracle, Db2, MySQL
- **Constraints:** Requires browser service running; not supported on z/OS
- **Workflows:** Configuration — Add Datasource; Navigation — View Ports
- **Knowledge:** Database Connection Architecture, Browser Service
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

### CyberArk Integration
- **Components:** All Guardium-supported databases
- **Constraints:** CyberArk SDK export restrictions apply in some regions
- **Workflows:** Configuration — Install CyberArk SDK
- **Knowledge:** Credential Management, Dynamic Secrets
- **Keywords:** CyberArk SDK, Credential Vault

## Datasource Connectivity

### Redshift Connection Parameters
- **Components:** Redshift
- **Constraints:** None
- **Workflows:** Configuration — Add Datasource
- **Knowledge:** JDBC Connection, Redshift Datasource
- **Keywords:** host, port, database, JDBC URL, Redshift

### CyberArk Integration
- **Components:** All Guardium-supported databases
- **Constraints:** CyberArk SDK export restrictions apply in some regions
- **Workflows:** Configuration — Install CyberArk SDK
- **Knowledge:** Credential Management, Dynamic Secrets
- **Keywords:** CyberArk SDK, Credential Vault

## Reports and Policy Management

### Policy Builder
- **Components:** N/A
- **Constraints:** None
- **Workflows:** Configuration — Create Policy; Monitoring — Review Violations
- **Knowledge:** Policy Enforcement, Violation Management
- **Keywords:** Policy Builder, Violations, Policy Enforcement

### Data Compliance
- **Components:** Guardium 12.2 and later
- **Constraints:** Requires compliance policy configuration
- **Workflows:** Configuration — Data Compliance Setup; Monitoring — Compliance Dashboard
- **Knowledge:** Compliance Policies, Regulatory Requirements
- **Keywords:** Data Compliance, Regulatory, Security Standards

## System Monitoring and Integration

### System Performance
- **Components:** All Guardium units

## Monitoring

### System Utilization
- **Components:** System Utilization; **Workflows:** Monitoring — System Utilization
- **Links:** Knowledge: Performance Monitoring, System Health; Keywords: Unit Utilization, Monitoring Tools

## Maintenance

### Services Status
- **Components:** Services Status; **Workflows:** Maintenance — Services Status
- **Links:** Knowledge: System Health; Keywords: Services Status, Monitoring Tools

## Alert Management

### Alert Builder
- **Components:** Alert Setup; Integration — Security Ticketing; **Workflows:** Configuration — Alert Setup; Integration — Security Ticketing
- **Links:** Knowledge: Alert Configuration, Ticketing Integration; Keywords: Alert Builder, Notification Type, Security Tickets

## Risk Management

### Risky Users - Connection Profiling
- **Components:** Risky Users Report; **Workflows:** Display — Risky Users Report
- **Links:** Knowledge: Access Control, Risk Scoring; Keywords: risky user, Client/Server Access, Connection Profiling

## Data Collection

### Session Filtering
- **Components:** Full SQL Report; **Workflows:** Query — Full SQL Report
- **Links:** Knowledge: Session Management, Data Extraction; Keywords: session_view, start time, Full SQL, SQL reporting

### Data Pull Interval
- **Components:** S-TAP Settings; **Workflows:** Configuration — S-TAP Settings
- **Links:** Knowledge: Data Collection, Continuous Monitoring; Keywords: data_pull_interval, S-TAP, audit table, polling frequency

## Agent Management

### Uninstall GIM Agent
- **Components:** Agent Uninstall; **Workflows:** Maintenance — Agent Uninstall
- **Links:** Knowledge: Guardium Installation Manager, Agent Deployment; Keywords: GIM uninstall, DB server agent, server mode, collector assignment

## Security

### Password Requirements
- **Components:** Password Policy; **Workflows:** Security — Password Policy
- **Links:** Knowledge: Authentication, CLI Security; Keywords: password requirements, cli accounts, guardcli, strong passwords

## Hadoop Integration

### Hadoop Monitoring API
- **Components:** Hadoop Management; **Workflows:** Monitoring — Hadoop Management
- **Links:** Knowledge: API Usage, Hadoop Integration; Keywords: update_rule, policy rule, API parameters, Hadoop monitoring

## SQL Logging

### Full SQL Logging
- **Components:** SQL Logging; **Workflows:** Configuration — SQL Logging
- **Links:** Knowledge: Compliance, SQL Analysis; Keywords: log full details, SQL string, value elements, DB table logging

## Investigation

### Investigation Dashboard Availability
- **Components:** Investigation Dashboards; **Workflows:** Reporting — Investigation Dashboards
- **Links:** Knowledge: Investigative Analytics, Core Management; Keywords: investigation dashboard, core availability, data visibility, core nodes

## Application Security

### SQL Injection Attack Characteristics
- **Components:** SQL Injection Detection; **Workflows:** Detection — SQL Injection Detection
- **Links:** Knowledge: Application Security, Vulnerability Exploits; Keywords: SQL injection, web application, user input, malicious SQL

## Performance Tuning

### Query Optimization Techniques
- **Components:** Query Tuning; **Workflows:** Performance — Query Tuning
- **Links:** Knowledge: Database Internals, Performance Optimization; Keywords: query optimization, data storage, domain data set, performance tuning

## Containerized Applications

- **Vulnerability Scanning:** Containerized apps need security workflows that include vulnerability scanning.  
  **Resources:** Security Assessments, Scanning Tools, Guardium scanner.

## CyberArk Integration

### Permissions Management
- **Supported Databases:** All Guardium‑supported databases.  
- **Constraints:** CyberArk SDK export restrictions may apply in some regions.  
- **Workflows:** Add and remove account permissions.

### Status Reporting
- **Supported Databases:** All Guardium‑supported databases.  
- **Constraints:** None.  
- **Workflows:** View Event Hubs, display Status Icons.

## Datasource Connectivity

### Dynamic Port Detection
- **Supported Databases:** SQL Server, Oracle, Db2, MySQL.  
- **Constraints:** Requires browser service running; not supported on Linux or z/OS.  
- **Workflows:** Add datasource, view ports.

## Guardium Certificates and Commands

### Import Certificates via CLI
- **Certificate Types:** Server, CA, Trusted‑Path.  
- **Constraints:** None.  
- **Workflow:** Import certificate.

## 1391. CAS Template Configuration

- **Supported Databases:** Guardium‑supported databases.  
- **Constraints:** Custom templates can only use built‑in report fields; complex joins need manual SQL.  
- **Workflows:** Define template, generate report.

## 1392. revoke_ignore_stap Command

- **Availability:** Guardium 11.3+.  
- **Constraints:** Requires SYSADMIN role; cannot revoke permanent IGNORE rules.  
- **Workflow:** Policy management – revoke IGNORE S-TAP SESSION.

## 1393. Unexpected Authentication‑Type Rule

- **Support:** All Guardium‑supported database engines.  
- **Constraints:** Baseline connection data required; false positives possible during migrations.  
- **Workflow:** Monitor anamolies based on auth type vs DB type.

## 1394. IMS Attribute Description

- **Version:** IMS 14.1+.  
- **Constraints:** None.  
- **Workflow:** IMS activity reporting.

## 1395. Policy and Correlation Alert Mapping

- **Version:** Guardium 12.0+.  
- **Constraints:** Syslog configuration must allow custom facility/priority.  
- **Workflow:** Alert settings – syslog integration.

## 1396. Data Security User‑DB Association

- **Support:** All Guardium data sources.  
- **Constraints:** Must have SECURITY ADMIN role; deletions are irreversible.  
- **Workflow:** Administration – data security – user‑DB association.

## 1397. Installed Policy Details

- **Support:** All Guardium managed units.  
- **Constraints:** Only units with installed policies can be viewed.  
- **Workflow:** Policy summary overview.

# Guardium Technical Reference

## Creating a Real-Time Alert
The real‑time alert workflow uses Guardium 13.0+ with the Alerter service enabled. It is built from Policies → Real‑Time Alerts → Rule Builder.

## Reducing Monitored Traffic
Filtering rules (Guardium 11.0+) minimize traffic volume. Note that filtering reduces audit completeness, so test in a non‑production environment first.

## Record Values Separately (Quick Parse)
Connector parsers (e.g., Oracle, SQL Server) support the “Record values separately” option, which enables quick parsing. This option does **not** apply to S3, MongoDB, or MySQL plug‑ins.

## AWS MSSQL over JDBC Plug‑ins
Available from Guardium 12.5+. Requires JDBC driver 8.4+ and proper AWS IAM permissions.

## Post‑S‑TAP Configuration Tasks
After S‑TAP installation, Guardium 13.0+ integrates with Ranger to extend Hadoop policy enforcement.

## DB2 for i Group Granted To User Report
This privilege‑reporting workflow (DB2 for i 14.2+) requires Object Authority Manager (OAM) to be enabled.

## GuardAPI Syntax
`register_oauth_client` (Guardium 11.2+) creates OAuth clients. Example: `register_oauth_client --client_name myClient --grant_type client_credentials`.

## Managing Roles and Permissions
The Threat Analytics viewing workflow (Guardium 12.0+, Enterprise license) includes User Management → Assign Roles and Threat Analytics → Outlier Mining.

## Unencrypted Administrative Program
Enforced by security policies (Guardium 9.5+). Generates an incident when an administrative program runs without encryption.

## External Tickets
Ticket integration (Guardium 11.3+) sends Guardium incidents to external systems via APIs like ServiceNow or Resilient.

## Session End
The “Session End” feature (Guardium 12.1+, Admin role required) records the end of a session; use `IGNORE SESSION` to exclude it from reporting.

## Exporting Data
Data export (Guardium 12.2+, requires an Aggregator) compresses and encrypts the exported archive.

## S‑TAP and GIM Dashboard
The Deployment Health dashboard (Guardium 12.3+, with deployment health views enabled) displays S‑TAP and GIM status.

## Upgrading the GIM Client
GIM upgrades (Guardium 12.4+, requires a bundle file) follow the workflow Administration → GIM Upgrade → Install Schedule.

## Outliers Detection APIs
Guardium 12.5+ provides APIs (Aggregator with cross‑CM enabled) for creating, updating, and querying outlier detection models.

## Datasource Connectivity

### Dynamic Port Detection
- **Components:** SQL Server, Oracle, Db2, MySQL
- **Limitations:** Browser service must run; not supported on z/OS
- **Workflows:** Add Datasource, View Ports
- **Knowledge:** Database Connection Architecture, Browser Service
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

### CyberArk Integration
- **Components:** All Guardium-supported databases
- **Limitations:** Export restrictions for CyberArk SDK in some regions
- **Workflows:** Install CyberArk SDK
- **Knowledge:** Credential Management, Dynamic Secrets
- **Keywords:** CyberArk SDK, Credential Vault

## Unauthorized Access

### Monitor Policy Exceptions
- **Components:** All Guardium-supported databases
- **Limitations:** Requires existing policy definitions
- **Workflows:** Create Policy, View Exceptions
- **Knowledge:** Policy Management, Exception Handling
- **Keywords:** Policy, Exception, Audit Trail

### Session-Level Policies
- **Components:** All Guardium-supported databases
- **Limitations:** Additional configuration may be required
- **Workflows:** Create Session Policy, View Sessions
- **Knowledge:** Policy Management, Session Monitoring
- **Keywords:** Policy, Session, Rule

### Using Session-Level Policies
- **Components:** All Guardium-supported databases
- **Limitations:** Policy must be enabled and active
- **Workflows:** Create Session Policy, View Sessions
- **Knowledge:** Policy Management, Session Monitoring
- **Keywords:** Policy, Session, Rule

### Using Activity Profiling
- **Components:** All Guardium-supported databases
- **Limitations:** Profiling must be enabled and configured
- **Workflows:** Create Profiling Policy, View Profiles
- **Knowledge:** Profiling, Anomaly Detection
- **Keywords:** Profiling, Anomaly, Behavior

### Accessing the Data Protection Policies Configurator
- **Components:** All Guardium-supported databases
- **Limitations:** Requires appropriate privileges
- **Workflows:** Create Policy, Data Protection Configurator
- **Knowledge:** Policy Management, Data Protection
- **Keywords:** Policy, Configurator, Data Protection

### Accessing the DPL Activity Builder
- **Components:** All Guardium-supported databases
- **Limitations:** Requires appropriate privileges
- **Workflows:** Create Activity Policy, DPL Activity Builder
- **Knowledge:** Policy Management, Data Protection
- **Keywords:** Policy, Builder, Data Protection

### Accessing the Built-In Reports
- **Components:** All Guardium-supported databases
- **Limitations:** None
- **Workflows:** Built-In Reports
- **Knowledge:** Reporting, Compliance
- **Keywords:** Report, Built-In, Compliance

## Data Protection and Compliance

- **Expanded Support for Custom Sensitivities:** Enable custom sensitivities on all Guardium‑supported databases (requires version 1.1+). Configuration → Enable Custom Sensitivities → Data Discovery.
- **Creating a Datasource Group:** No restrictions. Configuration → Create Datasource Group → Datasource Management.
- **Session‑Level Policies:** May need extra configuration. Configuration → Create Session Policy → View Sessions.
- **Available VA Tests Report:** No limits. Navigation → VA Tests Report.
- **Expand Support for Custom Sensitivities:** Same as the regular custom‑sensitivities feature (requires version 1.1). Configuration → Enable Custom Sensitivities → Data Discovery.

## MSSQL Kerberos Authentication (1433)

- **Support Matrix:** Microsoft SQL Server
- **Workflows:** Configuration → Set Dynamic IP Port to 0
- **Knowledge:** Guardium Datasource Configuration, MSSQL Kerberos Authentication
- **Keywords:** MSSQL, SQL Server, dynamic port, Kerberos, SPN

## SQL Errors Report (Description)

- Shows increased errors that may indicate a SQL injection attack, including client IPs and affected objects.

## Managing Cloned Reports (1448)

- **Workflows:** Command → Edit cloned report

## Smart Card Authentication (1449)

- Keywords: multi‑factor authentication, smart card, U.S. government mandate

## Unit Utilization Timecharts (1450)

- **Support Matrix:** Unit Utilization Metrics (CPU, Memory, I/O)
- **Workflows:** Visualization → Timechart view
- **Limitations:** Supports single‑system or multi‑system aggregation; not real‑time streaming

## Setting Dynamic IP Port for MSSQL (1451)

- **Support Matrix:** Linux (x86, ARM), SELinux enabled
- **Limitations:** Requires reboot after changing `db2_shmem_size`

## Importing a Custom Certificate (1452)

- **Knowledge:** External S‑TAP Architecture, Certificate Management
- **Keywords:** certificate chain, PEM format, PKCS12 import, root CA

## External S‑TAP User Interface (1453)

- **Knowledge:** Docker Integration, S‑TAP Management
- **Keywords:** External S‑TAP instances, deployment status, configuration JSON

## Long‑Term Retention and Reporting (1454)

- **Support Matrix:** Amazon S3, Azure Blob Storage, Google Cloud Storage (compatible)
- **Limitations:** Requires IAM policies for write access

## EMC Isilon Permissions (1455)

- **Support Matrix:** EMC Isilon version 8.x and newer
- **Limitations:** Credential must have appropriate file system permissions

## Extrusion Actions (1456)

- **Entities:** REDACT, GET_SERVER_DATA
- **Keywords:** SELECTIVE_AUDIT, EXTRUSION_THRESHOLD, ENCRYPTION

## Data Exfiltration Setup (1457)

- **Workflows:** Configuration → EXTRUSION_THRESHOLD rule
- **Limitations:** Thresholds apply per session, not per individual request

## Analysis Engine (1458)

- (No additional information provided; stop here.)

## Manage Datasource Credentials

### Update Insights Agent Configuration
- **Support:** IBM Guardium Insights
- **Limitation:** Requires admin privileges
- **Workflow:** Update Agent Parameters
- **Link:** Centralized Configuration Management

### Credential Type Requirements
- **Support:** IBM Guardium supported databases
- **Limitation:** Wallet format varies by database version
- **Workflow:** Set Up Credentials
- **Link:** Secure Credential Handling

## Azure PostgreSQL Configuration

### Dynamic Port Detection
- **Support:** Azure PostgreSQL
- **Workflow:** Add Datasource
- **Link:** Data Source Configuration

### Azure PostgreSQL Integration (Guardium 12.2+)
- **Support:** Azure PostgreSQL instances (public/private cloud)
- **Limitation:** Azure AD auth required; TLS 1.2+ mandatory
- **Workflow:** Add datasource, View/Manage datasources
- **Link:** Guardium Datasource Architecture

## Guardium Auditing and Monitoring

### Investigate Connection Issues
- **Support:** All Guardium versions
- **Link:** Diagnosis Dashboard

### Manage CAS System
- **Support:** Guardium 11.0+
- **Link:** System Health

### Monitor Data Access Permissions (FAM)
- **Support:** FAM-supported NAS/SharePoint
- **Link:** Permission Management

### Generate Full SQL Reports
- **Support:** All Guardium-supported SQL databases
- **Limitation:** Depends on data volume
- **Workflow:** Full SQL By DB User, Record Analysis
- **Link:** SQL Tracing

### SQL Optimization Techniques
- **Support:** All supported databases
- **Limitation:** May require restart for certain settings
- **Workflow:** Parallel Execution, Query Settings
- **Link:** Execution Plan

## Threat Detection and Analytics

### Threat Detection Analytics
- **Support:** All Guardium-supported platforms
- **Link:** GuardAPI Commands, Threat Detection Schema

## Data Management and Threat Detection

### Enable Outliers Detection Aggregation
- **Support:** All Guardium aggregators
- **Link:** Data Mart Transfer

### Execute Incident Generation Process
- **Support:** Guardium V9.0+
- **Link:** GuardAPI Commands

## Incident Management

### Incident Generation
- **Components:** Knowledge, Policy Violations Log
- **Keywords:** `execute_incidentGenProcess_byDetails`, Incident Category, Severity Threshold

## Threat Detection

### View Threat Detection Use Cases
- **Components:** Guardium V10.1.4+, admin role
- **Keywords:** `get_threat_detection_use_case_info`, REST API, Use Case Configuration

## Profile Management

### Replace Active Profile
- **Components:** Guardium V10.5+, existing profile
- **Keywords:** `Replace_active_profile`, GBDI Interface, Profile Name

## Data Streaming

### Stream S-TAP to Edge Gateway
- **Components:** S-TAP V11.3+, Edge Gateway V1.0+, Kubernetes
- **Keywords:** Streaming S-TAP, Edge Gateway, Kubernetes, Kubernetes-based Data Delivery

## Data Source Configuration

### Configure Db2 for z/OS Data Source
- **Components:** Guardium supported databases, z/OS V2.3+, JDBC license file
- **Keywords:** Db2 z/OS, JDBC License, Data Source Configuration

## Policy Configuration

### Suspicious Client Connection Detection
- **Components:** Guardium V11.0+, DNS-resolvable hostname
- **Keywords:** Suspicious Client, Unknown Hostname, Post-Connection Flagging

## Export Monitoring

### Monitor Data Export Status
- **Components:** All Guardium collectors
- **Keywords:** Data Export Status, Successful Exports, Failure Alerts

## Reporting

### Generate Information Security Officer Reports
- **Components:** Audit policy configuration
- **Keywords:** Failed Logins, Terminated Access, Policy Violations

## File Activity Review

### Review SharePoint File Activity
- **Components:** SharePoint 2019+, Guardium V12.0+, SharePoint connector
- **Keywords:** SharePoint File Activities, Activity Details, Connector Setup

## Knowledge, Features, and Reference

### Tuple Parameters in Session‑Level Policies
Combines multiple packet attributes into a single parameter for precise matching.

### Credential Stuffing Attack Detection
Flags repeated login failures from the same source as a potential credential‑stuffing attack.

### Activities Count per Time and Object
Displays activity volume by time ranges and database objects for rapid analysis.

### DML Execution on Administrative Objects
Audits DML verbs (INSERT/UPDATE/DELETE) against objects designated as administrative.

### Object Activity Summary
Provides a concise view of actions on a specific object, including user and IP details.

### Adding a Build Expression on Query Condition
Enables custom functions, substrings, or mathematical logic in query filters.

### Data Archive – All Fields
Archives all global profile fields except templates, PDF footers, and logos.

### Getting Fixes from Fix Central
Downloads product updates and patches via IBM's Fix Central repository.

## Management, Fix Central Interface  
**Keywords:** Fix Search, Download Options, IBM Fix Central  

## System CLI Commands  
**Components:**  
- Support Matrix: Stand‑alone Guardium systems  
- Limitations/Constraints: None  
- Workflows: Maintenance — Patch Installation  
**Links:** Knowledge: CLI Operations, Guardium Maintenance; Keywords: CLI Command, Patch Install, Stand‑alone System  

## GuardAPI Syntax  
**Components:**  
- Support Matrix: All Guardium versions  
- Limitations/Constraints: Requires appropriate permissions  
- Workflows: Configuration — User Management  
**Links:** Knowledge: API Usage, Security Roles; Keywords: GuardAPI, datamart_update_copy_file_info, REST API  

## S‑TAP and Inspection Engine APIs  
**Components:**  
- Support Matrix: Guardium data sources  
- Limitations/Constraints: Requires S‑TAP agent installed  
- Workflows: Management — Role Revocation  
**Links:** Knowledge: Role Management, API Calls; Keywords: revoke_role_from_object_by_Name, Role Removal, Dependency Handling  

## GuardAPI Example  
**Components:**  
- Support Matrix: All Guardium versions  
- Limitations/Constraints: Requires appropriate permissions  
- Workflows: Management — Role Revocation  
**Links:** Knowledge: API Usage, Security Operations; Keywords: revoke_role_from_object_by_id, Role Revocation, Dependency Management  

## Network Mirroring Methods (SPAN, N‑TAP) and Related Inspection Engines  
**Components:**  
- Support Matrix: All Guardium‑compatible network mirroring solutions  
- Limitations/Constraints: Requires compatible S‑TAP versions  
- Workflows: Configuration — Network Mirroring Setup  
**Links:** Knowledge: Network Monitoring, Inspection Engine Setup; Keywords: SPAN, N‑TAP, Inspection Engine, Catalog Entry  

## Addressing Investigation Dashboard Issues  
**Components:**  
- Support Matrix: Guardium Investigation Dashboard  
- Limitations/Constraints: Requires admin privileges  
- Workflows: Troubleshooting — Dashboard Maintenance  
**Links:** Knowledge: Dashboard Operation, Threat Analytics; Keywords: Manual Intervention, Threat Detection Analytics, Emergency Mode  

## DHCP Support for Virtual Machines  
**Components:**  
- Support Matrix: All Guardium‑supported virtual machine platforms  
- Limitations/Constraints: None  
- Workflows: CLI — `store network dhcp`  
**Links:** Knowledge: Network Configuration, DHCP Client; Keywords: DHCP, network dhcp, virtual  

## Compliance Summary  
**Components:**  
- Support Matrix: All Guardium‑supported databases  
- Limitations/Constraints: VIEWER or higher permission required  
- Workflows: Administration — Open Compliance Summary Tab  
**Links:** Knowledge: Data Classification, Compliance Reporting; Keywords: compliance summary, Guardium, policies, reports  

## Risk Spotter  
**See Compliance Summary**  

## Workflow Builder  
**Components:**  
- Support Matrix: All Guardium‑supported versions  
- Limitations/Constraints: None  
- Workflows: Administration — Configure Workflow  
**Links:** Knowledge: Audit Process Automation, Workflow Engine; Keywords: Workflow Builder, steps, transitions  

## Request Rate Report  
**Components:**  
- Support Matrix: All Guardium‑supported collectors  
- Limitations/Constraints: Excessive data warning for >24‑hour ranges  
- Workflows: Reporting — Open Request Rate Report  
**Links:** Knowledge: Performance Monitoring, Data Volume Management; Keywords: request rate, graphical report, time range  

## System CPU LoadA  
**Components:**  
- Support Matrix: All Guardium‑supported collectors  
- Limitations/Constraints: Normalized value, not per‑core utilization  
- Workflows: Monitoring — View System CPU Usage  
**Links:** Knowledge: System Performance, Resource Monitoring; Keywords: System CPU, LoadA, monitoring  

## Risk Spotter (duplicate merged)  

## Vulnerability Assessment Containerization  
**Components:**  
- Support Matrix: Docker containers on Linux, Windows Server containers  
- Limitations/Constraints: Requires container runtime and scanner image  
- Workflows: Administration — Deploy VA Scanner Container  
**Links:** Knowledge: Security Assessments, Containerized Applications; Keywords: VA, container, scanner, security assessment  

## Guardium Administration  
**Components:**  
- Support Matrix: All Guardium‑supported versions  
- Limitations/Constraints: Administrative credentials required for certificate management  
- Workflows: Administration — Manage Certificates  
**Links:** Knowledge: Certificate Management, GUI Security; Keywords: GUI access, certificates, S‑TAP communication  

## Active S‑TAPs Monitoring  
**Components:**  
- Support Matrix: All S‑TAP installations supported by Guardium  
- Limitations/Constraints: None  
- Workflows: Monitoring — View Active S‑TAPs  
**Links:** Knowledge: Real-time Inspection Engine Monitoring; Keywords: active S‑TAP, monitoring

## Threat Management

### Threat Detection Analytics APIs
- **Supports:** Guardium Active Threat Analytics  
- **Prerequisite:** Investigation dashboard must be enabled  
- **Workflow:** *Configuration → enable_threat_finder*  
- **See:** Active Threat Analytics, Investigation Dashboard  
- **Keywords:** Threat Finder, Risk Assessment, Analytics Engine

### Threat Detection APIs
- **Supports:** Guardium Central Manager and Standalone Units  
- **Prerequisite:** None  
- **Workflow:** *Configuration → enable_threat_finder*  
- **See:** Data Protection, Security Intelligence  
- **Keywords:** Threat Detection, Risk Scoring, Data Activity Monitoring

## Guardium Features

### Dynamic Port Detection
- **Supported Databases:** SQL Server, Oracle, Db2, MySQL  
- **Constraint:** Browser service must be running; not supported on z/OS  
- **Workflows:** *Configuration → Add Datasource*; *Navigation → View Ports*  
- **See:** Database Connection Architecture, Browser Service  
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

### Assessment and Hardening
- **Constraints:** Assessment issues can affect STAP configuration, network recognition, and VMXNET driver integration.  
- **See:** STAP Configuration, Vulnerability Assessment  
- **Keywords:** Assessment, Hardening, STAP, VMXNET

## Entitlement Optimization

### Dynamic Port Detection
- **Supported Databases:** All Guardium-supported databases  
- **Constraint:** CyberAr – *(truncated/removed due to incomplete information)*

## CyberArk SDK Export Restrictions

### 1702. REST API Syntax: get_va_summary_key

- This API retrieves a summary key for vulnerability assessment results. It requires a VA deployment and a previously generated API key.

---

## Guardium CLI Commands

### Show Log Object Join Info

- Displays the current object join settings in the Guardium logs. This command is view‑only and does not alter join behavior. Executed with appropriate role privileges.

---

## Features

### Identify Unauthorized Administrative Access to Sensitive Data

- Detects and alerts on unauthorized administrative queries to protected data. Requires admin role with data visibility and may produce false positives from legitimate investigations.

## Data Security Policies
- Enable **Sensitive Data Monitoring** in Configuration → Alerts "Unauthorized Access".
- Keywords: administrative user, sensitive data, alert, policy action.

## Detect Rarely Accessed Tables
- Supported databases: IBM Db2, Oracle, Microsoft SQL Server, MySQL, PostgreSQL.
- Limitation: Accuracy depends on monitoring period; does not include archived schema data.
- Workflows: Configuration → Reports "Rarely Accessed Tables"; Automation → Scheduled Audit.
- Keywords: table, last accessed, data source, Optim Designer.

## View File Activity Reports
- Supported sources: All Guardium-supported NAS and SharePoint.
- Dependency: File Activity Monitoring agents must be installed and configured.
- Workflows: Navigation → Reports "NAS File Activities"; Navigation → Reports "SharePoint File Activities".
- Keywords: NAS, SharePoint, report query, prebuilt reports.

## Outlier Filtering by Server IP
- Supported data sources: All Guardium appliances with Analytic Outliers.
- Consideration: IP filtering may affect query response time.
- Workflows: Navigation → Analytic Outliers Details; Filtering → Server IP.
- Keywords: outlier, server IP, runtime filter, analytic report.

## Exceptions Domain Overview
- Supported engines: All Guardium inspection engines capturing database traffic.
- Caution: Full exception capture impacts performance and storage.
- Workflows: Navigation → Monitored Data "Exceptions Domain"; Analysis → Traffic Exception Details.
- Keywords: exception, traffic detail, SQL exception, inspection engine.

## Centralized Policy Management
- Supported policies: All Guardium security policies and rule sets.
- Risk: Policy inconsistencies without centralized sync across appliances.
- Workflows: Configuration → System "Access Policies"; Management → Centralized Policy Sync.
- Keywords: access policy, centralized management, security audit, Guardium policy.

## IBM COS Archive/Backup Target
- Supported versions: Guardium versions compatible with IBM Cloud Object Storage.
- Prerequisite: Guardium must support IBM COS integration and network connectivity to COS.
- Workflows: Configuration → System "Archive/Backup"; Enable → IBM COS Target.
- Keywords: IBM COS, archive target, backup configuration, data export.

## Enable SP‑Initiated SLO
- Supported IDPs: SAML-based providers supporting SP-initiated logout (e.g., Okta, Azure AD, Shibboleth).
- Requirement: IDP must implement SAML SP-initiated logout profile.
- Workflows: Configuration → System "SAML"; Test → SLO Functionality.
- Keywords: SP‑initiated, single logout, IDP logout, SAML profile.

## External S-TAP SSL Certificate Management
- Supported versions: External S-TAP 1.8.0 and later.
- Requirement: Valid certificate from trusted CA; complete certificate chain.
- Workflows: Workflow → Install SSL Certificate; Steps: Create CSR → Obtain CA‑Signed Cert → Install in Keystore.
- Keywords: External S-TAP, SSL, certificate signing request, CA certificate, encrypted traffic.

## Troubleshoot Scanner Pod Failures
- Supported environments: Kubernetes clusters with Guardium Scanner pods.
- Steps: Investigation → kubectl get pods; Diagnostic → kubectl logs scanner-pod; Remediation → Fix Image Pull Secrets.
- Keywords: CrashLoopBackOff, Scanner pod, kubectl logs, image pull secret.

## File-Based Certificate Restoration
- Supported appliances: All Guardium versions supporting SSL certificate import/export.
- Scope: Restores only SSL certificates and keys stored in the file system.
- Workflows: System → SSL Management → Restore Certificates → Specify Backup File (`last` or `list`).
- Keywords: restore SSL, certificates, certificate keys, GUI/CLI restore.

## Query Rewrite Using WHERE Clauses
- Supported versions: Guardium 11.3 and later with Query Rewrite enabled.
- Limitation: Complex WHERE clauses may lead to unexpected results; ensure proper testing.

## Quality Gates
- Syntax errors prevent policy application
- Workflows: Configuration — System → Query Rewrite → Add Action; Set Parameters — addQualifierFlag, whereText, qrActionId
- Links: Query Optimization, Query Rewrite Actions; Keywords: qrActionId, addQualifierFlag, WHERE clause, query rewrite policy

## Custom Classifier Integration
- Components: All Guardium-supported databases; CyberArk SDK export restrictions apply in some regions
- Workflow: Configuration — Install CyberArk SDK
- Links: Credential Management, Dynamic Secrets; Keywords: CyberArk SDK, Credential Vault

## FamMonitor Configuration
- Components: Windows Server
- Limitation: Requires command line, wizard, or GIM for installation
- Workflows: Installation — Command Line; Installation — Wizard; Installation — GIM
- Links: Server Agent, Real-time Alerts, Connection Blocking; Keywords: FamMonitor, Windows Server, Monitoring Agent

## Event Sequence Analysis
- Components: All Guardium deployments
- Workflow: Visualization — Data In-Sight
- Links: Data Analysis, Event Correlation; Keywords: Guardium, Event Sequence, Visualization

## Data Indexing
- Components: All replica configurations
- Limitation: Data unavailable if all replicas down
- Workflow: Query — Investigation Dashboard
- Links: Redundancy, Core Replication; Keywords: Core Replicas, Data Indexing, Investigation Dashboard

## Threat Detection
- Components: Guardium-supported databases
- Workflow: Reporting — Suspicious Object Names Chart
- Links: SQL Injection, Object Usage Analysis; Keywords: Suspicious Object Names, SQL Injection, Stored Procedures

## Data Management
- Components: Guardium Aggregators
- Workflow: Configuration — Extract Data Mart to Table
- Links: Performance Optimization, Data Accessibility; Keywords: Data Mart, Table Extraction, Aggregator Performance

## Managed Unit Configuration
- Components: Guardium Managed Units
- Limitation: Permissions required
- Workflow: Configuration — Manage Inspection Engines
- Links: User Permissions, Configuration Distribution; Keywords: Inspection Engines, Managed Units, Configuration Management

## Compatibility Checks
- Components: Guardium 12.2.x or later with feature flag enabled; Existing IBM Knowledge Catalog instance required
- Workflow: Integration — Import from Knowledge Catalog
- Links: Integration Requirements, Feature Flags; Keywords: IBM Knowledge Catalog, Guardium Integration, Feature Flag

## Integration Requirements
- Components: FreeTDS versions with OpenSSL and Kerberos support
- Limitation: Specific version and support requirements
- Workflow: Integration — FreeTDS with Guardium
- Links: SSL Support, Kerberos Authentication; Keywords: FreeTDS, SSL, Kerberos

## Hadoop Ecosystem Auditing
- Components: Hadoop components with SSL/TLS, Kerberos
- Limitation: Requires Ranger integration
- Workflow: Auditing — SSL-Encrypted Traffic
- Links: Hadoop Security, SSL/TLS Auditing; Keywords: Ranger, SSL, Kerberos

## Persistent Storage
- Components: Kubernetes environments
- Limitation: Persistent volume configuration required
- Workflow: Deployment — External S-TAP
- Links: Kubernetes Storage, Persistent Volumes; Keywords: External S-TAP, Kubernetes, Persistent Volume

## SMTP Settings
- Components: IBM Guardium SMTP configurations
- Workflow: Configuration — Enable SMTP StartTLS
- Links: SMTP Security, TLS Configuration; Keywords: SMTP, StartTLS, Encryption

## GuardAPI Configuration
- Components: Guardium 12.2.x or later
- Limitation: Requires "Name" parameter
- Workflow: Configuration — GuardAPI datamart_include_file_header
- Links: API Usage, Data Export; Keywords: GuardAPI, CSV Export, Column Headers

## Entitlement Optimization
- Components: Guardium systems
- Limitation: Disables related services
- Workflow: Configuration — Disable FAM Crawler
- Links: Credential Management, Entitlement Extra

## Solr Health Monitoring
**Components:** All Guardium systems with Solr  
**Workflow:** Monitoring — get\_solr\_status\_extended  
**Links:** Knowledge: System Health Checks, Solr Status; Keywords: Solr, Health Check, Extended Status  

## Guardium Data Protection Features
### File Entitlement
**Components:** All Guardium-supported platforms  
**Workflow:** Configuration — Admin Dashboard; Navigation — VA Stats; Monitoring — S-TAP Stats  
**Links:** Knowledge: Data Classification, Entitlement Policies; Keywords: File Entitlement, Admin Dashboard, VA Statistics  

### Guardium Insights Connectivity
**Components:** Guardium Data Protection environments  
**Limitations:** Requires API tokens; limited to supported versions  
**Workflow:** Configuration — Manage Connections  
**Links:** Knowledge: API Management, Integration Protocols; Keywords: REST API, Token-Based Authentication, Guardium Insights  

### CyberArk Backup and Archive Integration
**Components:** All Guardium-supported databases  
**Limitations:** Requires CyberArk SDK export  
**Workflow:** Configuration — Install SDK  
**Links:** Knowledge: Credential Management, CyberArk SDK; Keywords: CyberArk Vault, S3 Bucket, Temporary Credentials  

### File Activity Monitoring
**Components:** Windows and Unix-Linux file servers  
**Workflow:** Configuration — Discover Sensitive Data  
**Links:** Knowledge: Data Classification, Rule Configuration; Keywords: Sensitive Data Discovery, Access Rules, Classification  

### Add to Group Action
**Components:** Guardium Data Protection 12.0 and later  
**Workflow:** Navigation — Tagging Entities  
**Links:** Knowledge: Group Management, Tagging Mechanisms; Keywords: Entity Tagging, Group Management, IP Tagging  

### Risk Spotter
**Components:** All supported Guardium appliances  
**Limitations:** AI algorithm dependent on data volume  
**Workflow:** Monitoring — Dynamic Risk Assessment  
**Links:** Knowledge: AI Algorithms, Risk Factors; Keywords: AI Risk Assessment, Dynamic Scanning, Security Risks  

### Advanced Session-Level Policies
**Components:** Guardium environments with S-TAP installed  
**Limitations:** Requires SR script knowledge  
**Workflow:** Configuration — Advanced Policy Setup  
**Links:** Knowledge: Session Management, SR Scripting; Keywords: Packet Validation, Data Transformation, S-TAP Routing  

### Correct IP Address for Oracle
**Components:** Oracle environments with Oracle Connection Manager  
**Limitations:** Requires understanding of Oracle IP handling  
**Workflow:** Configuration — IP Correction Setup  
**Links:** Knowledge: Oracle IP Handling, IP Correction; Keywords: Guardium IP, Oracle CM, Correct IP Capture  

### Administrative Users and Applications
**Components:** All Guardium-supported platforms  
**Workflow:** Monitoring — Runtime Security Incidents  
**Links:** Knowledge: Security Policies, Runtime Monitoring; Keywords: Admin Tracking, Application Security  

### Database Entitlement Reports
**Components:** All Guardium-supported databases  
**Limitations:** Requires entitlement module activation  
**Workflow:** Reporting — Privilege Snapshots  
**Links:** Knowledge: Entitlement Policies, Reporting Tools; Keywords: User Privileges, Entitlement Reports, Access Verification  

### SQL Injection Detection
**Components:** All Guardium-supported databases  
**Limitations:** Requires activation of SQL injection feature  
**Workflow:** Monitoring — SQL Injection Scanning  
**Links:** Knowledge: SQL Injection, Advanced Detection; Keywords: Stored Procedures, Dynamic SQL, Guardium Detection  

### Running Database Entitlement Reports
**Components:** Guardium Data Protection environments  
**Limitations:** Requires entitlement module  
**Workflow:** Reporting — Entitlement Snapshots  
**Links:** Knowledge: Reporting Mechanisms, Database Security; Keywords: Entitlement Reports, User Privileges, Security Snapshots  

## Datasource Connectivity
### Dynamic Port Detection
**Components:** SQL Server, Oracle, Db2, MySQL  
**Limitations:** Requires browser service running; not supported on z/OS  
**Workflow:** Configuration — Add Datasource; Navigation — View Ports  
**Links:** Knowledge: Database Connection Architecture, Browser Service; Keywords: S-TAP, Collector, JDBC, Browser Service  

### CyberArk Integration
**Components:** All Guardium-supported databases  
**Limitations:** CyberArk SDK export restrictions apply in some regions  
**Workflow:** Configuration — Install CyberArk SDK  
**Links:** Knowledge: Credential Management, Dynamic Secrets; Keywords: CyberArk SDK, Dynamic Secrets

## Credential Vault Management

**Register Guardium units**  
- **Requires**: valid license key, disabled APIs disabled on non-Guardium units  
- **Workflows**: install → register unit, unit → monitoring  

**Monitoring edge gateways**  
- **Supports**: AWS, Azure, GCP, on‑premises edge gateways  
- **Constraints**: Edge Gateway agent required, not for classic collectors  
- **Workflows**: deploy → install edge agent, monitor → policy status dashboard  

## Azure SQL Database Privileges

**Granted to user/role**  
- **Applies**: Azure SQL Database (all editions)  
- **Prerequisites**: Azure AD admin rights, recursion limited to 100 nested roles  
- **Tasks**: grant role, view privileges  

## Administrative Objects Usage (Oracle)

**Query SYS.OBJ$**  
- **Scope**: Oracle DBA permissions required  
**Links**: object permissions, Oracle auditing, SYS.OBJ$, DBA  

## Guardium Portal Configuration

**Configuring the Guardium Portal**  
- **Applies**: Guardium V10.1+.  
- **Needs**: admin privileges, trusted certificates for SSL import  
- **Operations**: reset web port, manage certificates  

## Job Management

**View job history**  
- **Compatible**: all supported Guardium platforms  
- **Links**: job scheduling, Gantt charts  

## Auditing SSL Activity

**Enable SSL auditing**  
- **Coverage**: major databases with SSL/TLS support  
- **Prerequisite**: Ranger integration, possible performance impact  
- **Related**: SSL/TLS auditing, Ranger  

## GuardAPI Commands

**Show system public transfer key**  
- **Version**: Guardium V10.1+  
- **Requirements**: ssh-key access, existing public key  
- **Context**: diagnostic, SSH key verification  

**Create DAMX suspicious connections member**  
- **Version**: Guardium V10.1.4+  
- **Prerequisite**: existing member & valid group name  
- **Category**: GuardAPI, DAMX group management  

## Data Export Management

**Delete export configuration**  
- **Requirement**: export configuration must exist  
- **Restriction**: cannot delete active exports  
- **Related**: export configurations, deletion policies  

## Discovery & Classification

**Unified discovery & classification**  
- **Version**: Guardium V11.0+  
- **Dependencies**: classification policies, additional storage for reports  
- **Purposes**: data monitoring, hazard detection  

## Data Activity

**Monitor activity & enforce least‑privilege**  
- **Version**: Guardium Data Protection V12.0+  
- **Requirements**: user activity tracking enabled, may generate large logs  
- **Focus**: user activity monitoring, privilege enforcement  

## Enhanced Monitoring

**Enhanced data monitoring with classification**  
- **Version**: Guardium (details not fully specified)  
- **Part of**: broader security and compliance workflow (truncated)

## Guardium IPv6 Configuration
**Enable and Assign IPv6 to Managed Devices**

- **Support Matrix:** All Guardium-supported platforms (Linux, Windows, AIX, etc.)
- **Limitations:** Requires IPv6 enabled on central manager, managed units, databases, and S‑TAP agents
- **Workflow:** Configuration – Enable IPv6 on Central Manager → Assign IPv6 to Managed Devices → Assign IPv6 to Databases and S‑TAP Agents
- **Knowledge:** IPv6 Fundamentals, Guardium Network Architecture
- **Keywords:** IPv6, Managed Unit, Central Manager, S‑TAP Agent, Network Configuration

---

## Secrets Management
**Create Database User (Secret User) in AWS RDS with AWS Secrets Manager**

- **Support Matrix:** AWS RDS, AWS Secrets Manager
- **Limitations:** IAM permissions for Secrets Manager required; manual rotation unless configured for automatic rotation
- **Workflow:** Configuration – Add Datasource (Specify Secrets Manager secret)
- **Knowledge:** Database Connection Architecture, AWS Secrets Manager
- **Keywords:** RDS, AWS Secrets Manager, IAM Role, Credential Rotation, Guardium Datasource

---

## Datasource Connectivity
**Dynamic Port Detection**

- **Support Matrix:** SQL Server, Oracle, Db2, MySQL
- **Limitations:** Requires browser service; not supported on z/OS
- **Workflows:** Configuration – Add Datasource; Navigation – View Ports
- **Knowledge:** Database Connection Architecture, Browser Service
- **Keywords:** S‑TAP, Collector, JDBC, Browser Service

---

## Aggregation
**Aggregation**

- **Support Matrix:** All Guardium-supported databases
- **Limitations:** None known
- **Workflows:** Navigation – View Data; Navigation – Export Data
- **Knowledge:** Data Warehouse, Report Offloading
- **Keywords:** Aggregation Appliance, Data Consolidation, Query Performance

---

## Configuring the alerter for S/MIME mail encryption
**Configuring S/MIME Alerter**

- **Support Matrix:** Guardium appliances with certificates
- **Limitations:** FIPS 140‑3 algorithm support on select platforms only
- **Workflow:** Configuration – Email Encryption Setup
- **Knowledge:** Email Alerts, Digital Signatures
- **Keywords:** S/MIME, Certificate, Alert, Digital Signature

---

## Updating a user account
**Edit User Account**

- **Support Matrix:** All Guardium appliances
- **Limitations:** Admin role required to edit other users
- **Workflow:** Configuration – User Management
- **Knowledge:** User Roles, Password Policies
- **Keywords:** User Browser, Reset Password, Role Assignment

---

## Unit utilization and inspection core performance
**Performance Monitoring**

- **Support Matrix:** All Guardium units
- **Limitations:** Inspection core reports limited to premium appliances
- **Workflow:** Navigation – System Reports
- **Knowledge:** Capacity Planning, System Load
- **Keywords:** Utilization Report, Inspection Core, Buffer Usage

---

## What to do next
**S‑TAP Verification Scheduling**

- **Support Matrix:** Guardium 11.2 and later with S‑TAP installed
- **Limitations:** Schedules cannot exceed 24-hour intervals
- **Workflow:** Configuration – Verification Setup
- **Knowledge:** S‑TAP Health, Verification Framework
- **Keywords:** S‑TAP Verification, Schedule, Agent Health

---

## Before you begin
**S‑TAP Installation Prerequisites**

- **Support Matrix:** Linux/UNIX platforms supported by Guardium
- **Limitations:** Requires root access for installation
- **Workflow:** Installation – Pre‑installation Checks
- **Knowledge:** System Requirements, Installer Scripts
- **Keywords:** Database OS, Fix Central, Installer Script

---

## Show command
**SNMP Properties**

- **Support Matrix:** Guardium appliances with SNMP enabled
- **Limitations:** Default community name immutable
- **Workflow:** Navigation – System Configuration > SNMP
- **Knowledge:** SNMP Configuration, Monitoring
- **Keywords:** SNMPv2c, Community, Query, GuardiumSNMP

---

## GuardAPI syntax
**create_kafka_cluster Parameters**

- **Support Matrix:** Guardium API v12.0+
- **Limitations:** MemberList must include at least three nodes
- **Workflow:** Configuration – Kafka Setup > create_kafka_cluster
- **Knowledge:** Kafka Architecture, Guardium API
- **Keywords:** clusterName

## GuardAPI Command Reference

### delete_user_hierarchy_by_user
- **Support Matrix:** Guardium 10.5 and later
- **Limitations/Constraints:** User must be a member of a hierarchy
- **Workflow:** User Management > delete_user_hierarchy_by_user

### discover_streams
- **Support Matrix:** Guardium v10.6+
- **Limitations/Constraints:** Requires cloud account credentials
- **Workflow:** Threat Detection > discover_streams

### list_assessments
- **Support Matrix:** Guardium 11.0+
- **Limitations/Constraints:** Must have assessment view privileges
- **Workflow:** Security Assessment > list_assessments

### list_cas_template_sets
- **Support Matrix:** Guardium 11.3+
- **Limitations/Constraints:** None
- **Workflow:** CAS Setup > list_cas_template_sets

### list_ranger_configs
- **Support Matrix:** Guardium 11.0+
- **Limitations/Constraints:** Requires proper Ranger permissions
- **Workflow:** Ranger Integration > list_ranger_configs

## Groups Usage Report

### Groups Usage Report
- **Support Matrix:** All Guardium deployments
- **Limitations/Constraints:** Report execution limited to 5 minutes
- **Workflow:** Reports > Groups Usage

## Database User Management APIs
- **Support Matrix:** Guardium 9.0 and later
- **Limitations/Constraints:** Requires SYSADM privileges; unsupported on some legacy DB2 versions
- **Workflows:** Create User Mapping, Delete User Mapping, Set Debug Level

## Activity Summary By Client IP

### Dynamic Port Detection
- **Support Matrix:** All Guardium-supported databases
- **Limitations/Constraints:** None
- **Workflow:** Aggregated Activity Monitoring

## Policy Detective

### 1959 Show Command
- **Support Matrix:** Guardium
- **Limitations/Constraints:** None
- **Workflow:** SMTP Authentication Username

### 1960 Show Command
- **Support Matrix:** Guardium
- **Limitations/Constraints:** Enables or disables logging only; requires engine restart after change
- **Workflow:** SQL Parser Errors

### 1961 Parameter Value Description
- **Support Matrix:** Guardium
- **Limitations/Constraints:** Value must be integer between 0 and 2147483647; default is 100,000 ms
- **Workflow:** Solr Search Functionality

### 1962 Threat Detection Analytics APIs
- **Support Matrix:** Guardium 11.1 and later
- **Limitations/Constraints:** Disables threat finder feature only
- **Workflow:** Active Threat Analytics

### 1963 Outliers Detection APIs
- **Support Matrix:** Guardium v11.0 and later
- **Limitations/Constraints:** None specified
- **Workflow:** Policy Analysis Engine

## Feature Flags Management

### Unlock Feature Flags
- **Support Matrix:** All IBM Guardium versions
- **Limitations/Constraints:** None
- **Workflow:** CLI — unlock_feature_flags

### Enable/Disable Feature Flag
- **Support Matrix:** All IBM Guardium versions
- **Limitations/Constraints:** Requires valid admin credentials
- **Workflow:** Feature Flag Configuration

## Guardium Core Features

### Inspection Engine
- **Components:** All Guardium-supported databases
- **Limitations/Constraints:** May impact performance during high transaction volumes
- **Workflows:** Configuration — Activate Inspection Engine; Monitoring — View

## Data Masking and Access Control

### Masked Stored Procedure Execution for MS SQL Server
- **Support:** All versions of Microsoft SQL Server
- **Limitations:** Requires `EXECUTE` permission on masked procedures, does not mask dynamic SQL within procedures
- **Workflows:** 
  - Configuration: Define Masked Procedures
  - Navigation: View Masked Executions

---

## Threat Analytics

### Security Exception
- **Support:** All Guardium versions
- **Limitations:** Requires OS-level firewall permissions, does not log to syslog
- **Workflows:**
  - Configuration: Define Alert
  - Navigation: View Alerts

### SQL Error Monitoring
- **Support:** All Guardium versions supporting Investigation Dashboard
- **Limitations:** Requires `ERROR_5` configuration
- **Workflows:**
  - Navigation: View Errors
  - Configuration: Set Collection

### Data Parsing and Network Traffic Analysis
- **Support:** All database types supported by Guardium (Oracle, SQL Server, Db2, etc.)
- **Limitations:** Engine performance impacted by high network traffic, requires SYSDBA privileges for setup
- **Workflows:**
  - Configuration: Setup Inspection Engine
  - Navigation: View Parse Trees

---

## Features

### Edge Gateway Image Registry Integration
- **Support:** All versions supporting Edge Gateway
- **Limitations:** Requires valid Docker registry credentials, does not support Kerberos authentication
- **Workflows:**
  - Configuration: Register Registry Credentials
  - Navigation: Edge Settings

### QRadar Custom Attribute Naming Restrictions
- **Support:** QRadar versions 7.3.0 and later
- **Limitations:** Attribute names cannot match predefined keys such as "TYPE", "SEVERITY", or "S2A_PLUGIN"
- **Workflows:**
  - Configuration: Custom Attribute Setup

### Diagnostic Data Collection Utility
- **Support:** QRadar consoles and managed hosts
- **Limitations:** Not supported on z/OS hosts
- **Workflows:**
  - Navigation: System Health > Must Gather
  - Configuration: Run Diagnos

### Import Users to User Segments
- **Components:** Guardium version 11.3 or later
- **Constraints:** JSON file must follow schema; segments must exist prior to import
- **Workflows:** Administration→User Segments→Import
- **References:** User Segments Management, JSON Import Guidelines
- **Keywords:** Import Users, User Segments, JSON Schema, Bulk Import, Administration UI

### Export Users to User Segments
- **Components:** Guardium version 11.3 or later
- **Constraints:** One segment exported per file; existing files overwritten
- **Workflows:** Administration→User Segments→Export
- **References:** User Segments Management, Export Guidelines
- **Keywords:** Export Users, User Segments, CSV Export, Administration UI

### Docker Compose Command for Applications
- **Components:** Docker utility
- **Constraints:** Requires docker-compose.yml file; must run from project root
- **Workflows:** Start services: `docker compose up -d`
- **References:** Docker Compose Documentation
- **Keywords:** Docker Compose, `docker compose`, Application, `docker compose up`, Container Management

## Components and Limitations

### Data Export Formats and Thresholds
- **Support:** All QRadar and Guardium versions
- **Limitations:** Export formats limited to CSV and JSON
- **Workflows:** Diagnostic Reports (Administration); Compliance Auditing (Security)

### Data Catalog Access and Export
- **Support:** Guardium 12.0+
- **Requirements:** RBAC permissions for Data Catalog access
- **Workflows:** Export Entries (Configuration); Navigation to Data > Catalog

### Aggregated Data Export/Import
- **Support:** Guardium 11.3+
- **Limitations:** Export files must be CSV; non‑sensitive data only
- **Workflows:** Import Results (Configuration); Navigation to Data > Reports

### Restricted Snapshot Permissions for AWS RDS/Aurora
- **Support:** AWS RDS, AWS Aurora
- **Limitations:** Only automated snapshots are restricted; manual snapshots are unrestricted
- **Workflow:** Apply Classification Policy (Automation)

### Vulnerability Assessment Dashboards
- **Support:** All on‑premises and cloud Guardium 1791 deployments
- **Workflow:** Create Assessment Dashboard (Configuration)

### Guardium VA Workflow
- **Support:** All Guardium‑supported databases
- **Requirements:** Write access to assessment repository
- **Workflows:** Define CVE Queries (Configuration); Run Remediation Scripts (Automation)

### Big Data Intelligence Configuration
- **Support:** Hadoop, Spark, Kafka, Azure Data Lake
- **Limitations:** PEM‑encoded key‑pair files; TLS‑enabled clusters required for streaming
- **Workflows:** Set Up Data Mart (Configuration); Configure Remote Logging (Automation)

### Daily Alert Workflow
- **Support:** Guardium V11.0 and later
- **Workflow:** Daily Alert (Alert)

### Risk Spotter AI Engine
- **Support:** Guardium 11.4+ on any deployment type
- **Requirements:** 30+ days of historical data for model training
- **Workflows:** Run Risk Assessment (Analytics); Active Threat Dashboard (Visualization)

### Object‑Level Auditing
- **Support:** All Guardium‑supported databases
- **Limitations:** Auditing limited to objects identified by classification scans
- **Workflows:** Enable Auditing (Configuration); Real‑Time Auditing Alerts (Monitoring)

### Active Threat Analytics Dashboard
- **Support:** Guardium 12.0+ with Active Threat Analytics module
- **Requirements:** Unique combination of rule and threshold for new threat categories
- **Workflows:** Add Threat Category (Analytics); Create Custom Policy (Policy)

## Operations and Auditing

### Outlier Data Send Control
- **Support:** Guardium Collectors in Multi‑Collector Manager (MCM) environment
- **Limitations:** Not available in standalone collector mode
- **Workflows:** Data Export (Operations); Collector Settings (Configuration)

### Adding Threat Category from Active Threat Analytics Dashboard
- **Support:** Guardium 12.0+ with Active Threat Analytics module
- **Limitations:** Unique rule/threshold combination required
- **Workflows:** Add Threat Category (Analytics); Create Custom Policy (Policy)

nts:**
  - **Support Matrix:** All Guardium versions
  - **Limitations/Constraints:** None
  - **Workflows with different types:** None
- **Links:**
  - **Knowledge:** None
  - **Keywords:** None

## Access Management

### Access Management Enhancements
- **Support Matrix:** Guardium 12.0 and later
- **Limitations/Constraints:** None
- **Workflow:** API — Access Management Configuration
- **Knowledge:** User Management, Security Enforcement
- **Keywords:** access_management, password_expired, guardium_12

---

## Proactive Password Management

### Alerting Rule Actions
- **Support Matrix:** IBM Guardium Data Protection
- **Limitations/Constraints:** None
- **Workflows:** Configuration — Create Alert Rule; Workflow — Multi-Notification
- **Knowledge:** Alert Rule Engine, Notification Channels
- **Keywords:** Alert Actions, Notification Types, Runtime Alerts

### Syslog Messages
- **Support Matrix:** All Guardium-supported databases
- **Limitations/Constraints:** %%RecordsAffected returns no values for alert-only rules
- **Workflows:** Configuration — Syslog Integration; Workflow — View Logs
- **Knowledge:** Syslog Protocol, Log Management
- **Keywords:** Syslog Agents, Event Logging, Runtime Alerts

### Alert Messages
- **Support Matrix:** IBM Guardium Data Protection
- **Limitations/Constraints:** None
- **Workflows:** Configuration — Alert Templates; Workflow — View Messages
- **Knowledge:** Template Engine, Message Formatting
- **Keywords:** Alert Templates, Named Templates, Message Formatting

---

## Data Transfer Options

### Secure Archive and Backup Export
- **Support Matrix:** SCP, SFTP
- **Limitations/Constraints:** None
- **Workflows:** Configuration — Export Archive; Navigation — Backup Transfer
- **Knowledge:** Guardium Data Transfer Mechanisms, Secure Protocols
- **Keywords:** SCP, SFTP, Archive Export, Backup Transfer

---

## Alerting and Audit

### 2137. Alerting tasks for users
- **Support Matrix:** All Guardium-supported versions
- **Limitations/Constraints:** None
- **Workflows:** Query Definition — Correlation Alert; Alert Definition — Custom Class
- **Knowledge:** Alert Management, Custom Alert Classes
- **Keywords:** Alert, Alert Task, sysaudit, Syslog

### 2138. Audit and Report
- **Support Matrix:** All Guardium-supported versions
- **Limitations/Constraints:** None
- **Workflows:** Audit Definition — Data Access; Report — Policy Violation
- **Knowledge:** Audit Records, Report Customization
- **Keywords:** Audit, Policy, Violation, Data Access

### 2141. QWR Exceptions
- **Support Matrix:** All Guardium-supported versions
- **Limitations/Constraints:** Requires License
- **Workflows:** Alert Definition — Syslog; Alert Definition — Hourly
- **Knowledge:** Alert Triggers, Session Management
- **Keywords:** QWR, Exception, Session, Syslog

---

## Configuration and Monitoring

### 2140. LDAP authentication configuration
- **Support Matrix:** Guardium 12.0 and later
- **Limitations/Constraints:** None
- **Workflow:** API — LDAP Configuration
- **Knowledge:** Authentication Mechanisms, Directory Services
- **Keywords:** LDAP, Authentication, Configuration

## Feature Details

### 2142. Monitoring with SNMP
- **Support Matrix:** All Guardium-supported versions
- **Limitations/Constraints:** Requires SNMP agent
- **Workflows:** System Configuration — SNMP
- **Keywords:** SNMP, Agent, Guardiumsnmp

### 2143. Long term retention views and tables
- **Support Matrix:** Guardium 12.2.x and later
- **Limitations/Constraints:** None
- **Workflows:** Reporting — Long Term Retention
- **Keywords:** Views, Tables, Retention

### 2144. Upgrading S-TAP using RPM
- **Support Matrix:** UNIX platforms
- **Limitations/Constraints:** None
- **Workflows:** System Upgrade — S-TAP RPM
- **Keywords:** S-TAP, RPM, Upgrade

### 2146. Data Security - User Hierarchy and Database Associations
- **Support Matrix:** All Guardium-supported versions
- **Workflows:** Data Security Configuration — User Hierarchy; Data Security Configuration — Database Associations
- **Keywords:** User Hierarchy, Database Associations, Datamart, API

### 2151. RestAPI example
- **Support Matrix:** All Guardium-supported versions
- **Limitations/Constraints:** Requires API role
- **Workflows:** Integration — REST API
- **Keywords:** RESTAPI, DELETE, Bearer, ClusterName

## Datasource Connectivity

### Cloudera Manager
- **Support Matrix:** Cloudera Manager
- **Workflows:** Configuration — Add Datasource

### CockroachDB
- **Support Matrix:** CockroachDB
- **Workflows:** Configuration — Add Datasource

### Couchbase
- **Support Matrix:** Couchbase
- **Workflows:** Configuration — Add Datasource

## Policies and Rules

### Policy Rule Actions
- **Support Matrix:** All Guardium-supported databases and systems
- **Workflows:** Configuration — Policy Builder, Installation — Policy Installation
- **Keywords:** Policy Builder, Policy Actions

### Assessment Log
- **Support Matrix:** All Guardium-supported systems
- **Workflows:** Administration — Assessment Management
- **Keywords:** Assessment Log, Admin Role

## User Management

### User Roles
- **Support Matrix:** All Guardium-supported systems
- **Workflows:** Administration — User Management
- **Keywords:** User Roles, Access Control

### Custom Certificate
- **Support Matrix:** All Guardium-supported systems
- **Workflows:** Security — Certificate Management
- **Keywords:** Custom Certificate, Certificate Management

## Firewall and Monitoring

### Firewall Force
- **Support Matrix:** All Guardium-supported systems
- **Workflows:** Configuration — Firewall Management
- **Keywords:** Firewall Force, Network Security

### Log Extrusion Counter
- **Support Matrix:** All Guardium-supported systems
- **Workflows:** Monitoring — Log Extrusion
- **Keywords:** Log Extrusion Counter, Monitoring

## Data Streaming Configuration

### Configure Streaming on Edge
- **Components:** Guardium Data Encryption for ZIP and Office files
- **Requirements:** Guardium v12.1+, no named pipe streaming
- **Workflows:** Enable Edge Streaming, Start/Stop Stream, Manage Certificates
- **Links:** Data Streaming Architecture, Edge Cluster Communications
- **Keywords:** Stream Receiver, Kafka Topic, TLS Certificates, Edge Node

### Assign Edge Nodes
- **Components:** All Guardium-supported cloud services
- **Requirements:** Edge Gateway deployment, no Browser Service
- **Workflows:** Assign Edge Nodes, Load Balancing
- **Links:** Data Streaming Architecture, Edge Gateway Overview
- **Keywords:** Edge Node, Data Stream, Processor Instance, Load Balancing

### Limitations
- **Components:** Edge Gateway (all versions)
- **Constraints:** No query rewrite, App‑User translation, custom ID procedures, or response data features
- **Links:** Guardium Edge Capabilities, Functional Limitations
- **Keywords:** Edge Gateway, Unsupported Features, Functional Constraints, Query Rewrite

### Load Balancing
- **Components:** Edge Gateway v11.3+
- **Workflows:** Define Stream Processors, Traffic Distribution
- **Links:** Data Streaming Workflow, Edge Load Balancing Algorithms
- **Keywords:** Stream Processor, Edge Load Balancing, Data Stream, Configuration Workflow

---

## Alerting

### Failed Logins
- **Components:** Guardium Appliance v12.0+
- **Features:** Alert only; no remediation
- **Workflows:** Alert Thresholds, Failed Login
- **Links:** Alert Mechanisms, Security Policies
- **Keywords:** Failed Logins, Alert Thresholds, 10‑Minute Interval, 5 Attempts

---

## Custom Attributes & Event Correlation

### Limitations
- **Components:** Guardium v9.5+
- **Restrictions:** Custom attributes cannot be used in event correlation
- **Links:** Event Management Framework, Custom Attributes
- **Keywords:** Custom Attributes, Event Correlation, DatabaseName, LEEF Templates

---

## Mutual Authentication

### Two‑Way Certificate Trust
- **Components:** External S‑TAP v10.5, all supported databases
- **Requirements:** Certificate infrastructure
- **Workflows:** Server Certificate Validation, Client Certificate Presentation
- **Links:** Certificate Trust Chains, External S‑TAP Architecture
- **Keywords:** Mutual Authentication, Server Certificate, Client Certificate, Certificate Validation

---

## GIM Server Failover

### Redundant Setup
- **Components:** GIM v3.4+, all Guardium platforms
- **Behavior:** Failover after five consecutive failures
- **Links:** GIM Server High Availability, GIM Client Behavior
- **Keywords:** GIM Server, Failover Mechanism, Connection Attempts, High Availability

## Licensing

- **Procedure:** Requires Guardium v10.0+ support matrix.
- **Limitation:** Maintenance patches need install keys.
- **Workflow:** Configuration – Install License; Configuration – Install Maintenance Package.

## Audit Process

- **Support Matrix:** All Guardium versions.
- **Limitation:** Requires audit‑delete role; deletion must be targeted.
- **Workflow:** Configuration – Create/Modify Audit Processes; Maintenance – Delete Audit Results.

## Investigation Dashboard API

- **Support Matrix:** Guardium v11.4+, API v1.2+.
- **Limitation:** Configuration is API‑only; no restoration.
- **Workflow:** API calls only.

## REST API Configuration

- **Support Matrix:** Guardium API v1.5+, TEST_RESULT_DETAIL supported.
- **Limitation:** Only visibility/detail level is changed; data is untouched.
- **Workflow:** Configuration – Set REST API Parameters; Retrieval – View Setting.

## Multi‑Factor Authentication Settings

- **Support Matrix:** Guardium v11.2+, MFA feature enabled.
- **Limitation:** Display‑only; no configuration through APIs.
- **Workflow:** Monitoring – View MFA Status.

## Edge Data Streaming

- **Support Matrix:** All Guardium‑supported cloud services, Edge Gateway v11.3+.
- **Limitation:** Requires cloud service and Edge deployment.
- **Workflow:** Configuration – Assign Edge Nodes; Monitoring – Traffic Distribution.

## Auditing System (CAS) APIs

- **Support Matrix:** Guardium 11.x+.
- **Limitation:** Requires CAS template set.
- **Workflow:** Query – list_cas_templates.

## Query Rewrite API

- **Support Matrix:** Guardium 12.0+.
- **Limitation:** Specified qrActionId must exist.
- **Workflow:** Configuration – Query Rewrite.

## Role Management

- **Support Matrix:** All Guardium releases.
- **Limitation:** Specified object name must be valid.
- **Workflow:** Administration – Role Management.

## REST API – Remove Datasource from Group

- **Support Matrix:** Guardium 11.3+.
- **Limitation:** Requires valid group ID.
- **Workflow:** Configuration – Datasource Management.

## Big Data Intelligence API

- **Support Matrix:** Guardium 11.0+.
- **Limitation:** Domain must exist in the allowed list.
- **Workflow:** Configuration – Universal Connector.

## Compliance Job Restart

- **Support Matrix:** Guardium 10.1+.
- **Limitation:** Requires admin privileges.
- **Workflow:** Administration – Compliance.

## 2203. Creating an Application ID on CyberArk

**Summary:** Guides creation of a CyberArk application ID required for Guardium–CyberArk credential integration. Requires CyberArk SDK on Guardium appliances. Supports Configuration workflows.

**Links:** Credential Management, CyberArk Integration

---

## 2204. Client IP Address (CLIENT_IP)

**Summary:** Enables rule evaluation based on client IP subnet using the CLIENT_IP system context variable. Applicable to all Guardium releases. Supports Rule Building workflows.

**Links:** Session Rule Conditions, Network Monitoring

---

## 2205. Application Summary

**Summary:** Wizard that creates a policy to monitor application data activity. Requires Guardium 9.5 or later with Application Data Monitoring enabled. Supports Configuration and Compliance Monitoring workflows.

**Links:** Policy Configuration, Compliance Monitoring

---

## 2206. Monitoring Your Organization's Data Compliance

**Summary:** Central hub for data compliance reporting and metrics. Requires Guardium 9.0 or later with compliance hub activated. Supports Reporting workflows.

**Links:** Data Compliance, Reporting

---

## 2207. Plan for Hardware Retirement or Redeployment

**Summary:** Provides inventory and cost analysis to plan hardware retirement or redeployment. Requires Guardium 8.2 or later with inventory data. Supports Administration workflows.

**Links:** Hardware Resource Planning, Cost Optimization

---

## 2208. DDL Distribution

**Summary:** Report group showing distribution of DDL commands by object type. Requires Guardium 8.0 or later with DDL Commands report enabled. Supports Reporting workflows.

**Links:** DDL Activity Tracking, Reporting

---

## 2209. Policy Violations Summary Domain

**Summary:** Domain that summarizes all policy violations captured by Guardium. Requires policy violation data. Supports Compliance Reporting workflows.

**Links:** Policy Violations, Compliance Reporting

---

## Datasource Connectivity

### Dynamic Port Detection

**Summary:** Auto-discovers database listener ports for supported DB platforms. Requires browser service; not supported on z/OS. Supports Configuration workflows.

**Links:** Database Connection Architecture, Browser Service

### CyberArk Integration

**Summary:** Imports database credentials from CyberArk vault. Requires CyberArk SDK; export restrictions may apply. Supports Configuration workflows.

**Links:** Credential Management, Dynamic Secrets

---

### Schema Access

**Summary:** Grants privileges needed for Guardium to read database schemas. Requires CONNECT and SELECT ANY TABLE. Not supported for views‑only schemas. Supports Configuration workflows.

**Links:** User Management, Privilege Escalation

---

### JDBC Driver Compatibility

**Summary:** Ensures JDBC driver matches database version and supports TLS 1.2. Supports Configuration and Administration workflows.

**Links:** Driver Mapping, TLS Configuration

---

### Kerberos Authentication

**Summary:** Enables Kerberos authentication for Oracle, SQL Server, Db2. Requires reachable KDC and SPN registration. Supports Configuration workflows.

**Links:** SPN Registration, Kerberos Ticketing

---

### SSL/TLS Connectivity

**Summary:** Configures encrypted connections using server‑side certificates. Requires certificate management. Supports Configuration workflows.

**Links:** SSL Handshake, Certificate Authority

## Cloud Database Audit

- Enabling native audit for cloud databases (AWS RDS, Azure Database Services, Google Cloud SQL) requires appropriate permissions and may increase CPU usage.
- Configuration: Enable Native Audit.
- Management: Retrieve Object Rules.

## Datasource Connectivity

### Dynamic Port Detection

- Supports SQL Server, Oracle, Db2, MySQL via browser service (not z/OS).
- Configuration: Add Datasource.
- Navigation: View Ports.

## Manage Azure Event Hubs

- Requires Azure service credentials.
- Configuration: Set Up Event Hub Monitoring.

```markdown
# Security Features

## Solr Repair Analysis
- Supports API v12.0+  
- No limitations  
- Use **Administration → Health Check**  

## Configure Database Auditing
- Supports DB2, Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, Cassandra, Hadoop, Sybase ASE, Teradata, Sybase IQ, Informix, SAP HANA, Vertica, Neo4j, MariaDB, Firebird, Informix IDS, DB2 for i, DB2 z/OS, SAP IQ, SAP ASE, Snowflake, Amazon Redshift, Azure Synapse, Google BigQuery, SAP ABAP, SAP BW  
- Auditing overhead; specific DB version minimums  
- **Configuration → Enable Auditing → Set Auto‑Object Limits → Point to Collector**  

## Downloading the Trial and Trial License
- All Guardium products  
- License expires after 90 days; not for production  
- **Licensing → Download Trial License**  

## Workflow Builder
- All platforms with Guardium UI  
- Requires appropriate role permissions  
- **Creation → Custom Workflow, Reporting → Execute Workflow**  

# Vulnerability Assessment

## Tuning a Test
- All vulnerability assessment test libraries  
- Test‑specific tunables documented per test  
- **Tuning → Adjust Severity → Create Exception**  

## DataStax Cassandra Support
- DataStax Enterprise clusters  
- No Kerberos authentication support  
- **Configuration → Add Datasource → Enable Auth**  

# Threat Detection and Monitoring

## Enable Threat Finder
- Central Manager and stand‑alone Collectors  
- Requires periodic scheduler  
- **Threat Finder → Start Analysis**  

## File Activity Monitor for NAS and SharePoint
- Windows NAS devices, SharePoint 2010+ servers  
- Requires FAM agent deployment  
- **Monitoring → Enable File Monitoring**  

## Enable Database Auditing
- All database types supported by Guardium  
- Auditing must be enabled at the database level first  
- **Auditing → Enable Auditing → Set Object Limits → Point to Collector**  
```

## Compressed Documentation

## Reporting and Controlling

### Administrative User Accessing Sensitive Data
All datasources with policy definitions are accessible by privileged users who have been assigned the correct policies. Policy assignment to roles is mandatory. Workflows include *Create Policy → Deploy → Monitor*.

### Creating Data Compliance Thresholds
Thresholds can be defined for any Guardium report by an admin. Creation requires an appropriate admin role. The workflow is *Compliance → Threshold Management → Define Rule*.

## Domain Based on Query Main Entity

### Dynamic Port Detection
SQL Server, Oracle, Db2, MySQL support dynamic port detection, which fails if the browser service is not running and is not supported on z/OS. Workflows: *Configuration → Add Datasource*, *View Ports*.

## Managing query security roles

### Query Security Roles
Roles control access to query data. Default is private; explicit role assignment is required. Workflows: *Configuration → Assign Role*, *View Role Permissions*.

## Guardium Activity domain

### Guardium Activity Tracking
Tracks activity across all supported platforms. No constraints. Workflows: *Audit Logs*, *Activity Types*.

## Attribute Description

### Tuple Group Attribute
Attributes are available for all reports and queries. No limitations. Attribute list includes Client IP, Source Application, DB User, Server IP, Service Name, OS User, DB Name.

## OS Script

### OS Script Execution in CAS
Scripts must be executable by the CAS user and output size is limited by Guardium storage. Workflows: *Create Script*, *Run Script*.

## Enabling SSH key pairs for data archive, data export, data mart

### SSH Key Authentication for Data Tasks
Keys must be generated externally for SFTP archive/export. Workflows: *Import SSH Key*, *Data Archive/Export to SFTP*.

## When to use Edge Gateway

### Edge Gateway Deployment Scenarios
Deploy on Kubernetes, IBM Cloud, AWS, Azure, or on-premises. Not suitable for legacy appliances. Workflows: *Install Edge Gateway*, *Scale Services*.

## Outlier Analysis

### Outlier Detection Workflows
Detects outliers in Threat Analytics enabled deployments. Requires configured mining process; scores are relative. Workflows: *Set Anomaly Threshold*, *Outlier Notification*.

## S3 over CloudWatch Logs

### S3 Over CloudWatch Logs Integration
Requires Guardium Universal Connector patch 1006. No additional constraints. Workflow: *Enable S3 Over CloudWatch Logs*.

## AWS MSSQL over JDBC

### AWS MSSQL and Other DBs via Universal Connector
Universal Connector supports AWS MSSQL, Azure Postgres, Dynamo, Firebase, MongoDB, MySQL.

## Archive Flag

**Components:**  
- **Support Matrix:** Guardium CLI on all supported platforms  
- **Limitations/Constraints:** Requires administrative privileges; read‑only view  
- **Workflow:** Navigation → Show Command → Archive Settings  

**Links:**  
- **Knowledge:** Command Line Interface, Guardium Administration  
- **Keywords:** CLI Command, Archive Flag, Store Archive, Settings Configuration  

---

## Data Source Services

### Dynamic Port Detection  

**Components:**  
- **Support Matrix:** SQL Server, MySQL  
- **Limitations/Constraints:** Requires browser service running; not supported on z/OS  
- **Workflow:** Configuration → Add Datasource → View Ports  

**Links:**  
- **Knowledge:** Database Connection Architecture, Browser Service  
- **Keywords:** S-TAP, Collector, JDBC, Browser Service  

### CyberArk Integration  

**Components:**  
- **Support Matrix:** All Guardium‑supported databases  
- **Limitations/Constraints:** CyberArk SDK export restrictions apply in some regions  
- **Workflow:** Configuration → Install CyberArk SDK  

**Links:**  
- **Knowledge:** Credential Management, Dynamic Secrets  
- **Keywords:** CyberArk SDK, Credential Vault  

---

## Query Rewrite APIs  

**Components:**  
- **Support Matrix:** Guardium V11.0 or later  
- **Limitations/Constraints:** Requires appropriate permissions to use Guardium APIs  

**Workflow:** Configuration → Create QR Replacement Element  

**Links:**  
- **Knowledge:** Query Rewrite Engine, API Integration  
- **Keywords:** SQL Replacement, API, create_qr_replace_element  

---

## Data Mart APIs  

**Components:**  
- **Support Matrix:** Guardium V9.5 or later  
- **Limitations/Constraints:** None specified  

**Workflow:** Configuration → Datamart Export Validation  

**Links:**  
- **Knowledge:** Data Mart Exports, REST API  
- **Keywords:** datamart_validate_copy_file_info, Export, Validation  

---

## GuardAPI Syntax  

**Components:**  
- **Support Matrix:** Guardium V9.0 or later  
- **Limitations/Constraints:** Requires admin privileges  

**Workflow:** Configuration → Disable Detailed Test Logging  

**Links:**  
- **Knowledge:** GuardAPI, Test Result Management  
- **Keywords:** disable_test_result_detail_string_setting, Logging, Test Results  

---

## API Example  

**Components:**  
- **Support Matrix:** All versions of Guardium  
- **Limitations/Constraints:** Requires Hadoop environment  

**Workflow:** Monitoring → Get Health Traffic Status  

**Links:**  
- **Knowledge:** Hadoop, Monitoring API  
- **Keywords:** get_health_traffic_status, Hadoop, API  

---

## REST API Syntax (IP Restriction)  

**Components:**  
- **Support Matrix:** All versions with REST API support  
- **Limitations/Constraints:** Requires valid authentication token  

**Workflow:** Retrieval → IP Restriction Status  

**Links:**  
- **Knowledge:** REST API, IP Restrictions  
- **Keywords:** ip_restriction, GET, REST, API  

---

## REST API Syntax (Quick Search)  

**Components:**  
- **Support Matrix:** All versions with REST API support  
- **Limitations/Constraints:** Requires valid authentication token  

**Workflow:** Retrieval → Quick Search Information  

**Links:**  
- **Knowledge:** REST API, Search Functionality  
- **Keywords:** get_quick_search_info, REST, Search, API  

---

## Group APIs  

**Components:**  
- **Support Matrix:** All versions with group management  

**Workflow:** Retrieval → List HashiCorp Configurations  

**Links:**  
- **Knowledge:** HashiCorp Integration, Group Management  
- **Keywords:** list_hashicorp_config, Guardium, API  

---

## REST API Syntax (Datamart Copy File)  

**Components:**  
- **Support Matrix:** All versions with REST API support  
- **Limitations/Constraints:** Requires valid authentication token  

**Workflow:** Update → Datamart Copy File Information  

**Links:**  
- **Knowledge:** REST API, Data Mart Management  
- **Keywords:** update_datamart_copy_file_info_from_cold_storage, REST, Data Mart  

---

## Query Rewrite APIs (Update Quarantine)  

**Components:**  
- **Support Matrix:** Guardium V11.0 or later  
- **Limitations/Constraints:** Requires appropriate permissions to use Guardium APIs  

**Workflow:** Configuration → Update Quarantine Parameters  

**Links:**  
- **Knowledge:** Query Rewrite Engine, User Management  
- **Keywords:** update_quarantine_allowed_until, Quarantine, User Login  

---

## REST API Syntax (Universal Connector Credential)  

**Components:**  
- **Support Matrix:** All versions with REST API support  
- **Limitations/Constraints:** Requires valid authentication token  

**Workflow:** Update → Universal Connector Credential  

**Links:**  
- **Knowledge:** REST API, Credential Management  
- **Keywords:** ucCredential, PUT, REST, Credential  

---

## Microsoft Azure Unified Discovery  

**Components:**  
- **Support Matrix:** Microsoft Azure  
- **Limitations/Constraints:** Requires valid Azure credentials  

**Workflow:** Discovery → Unified Discovery and Classification  

**Links:**  
- **Knowledge:** Microsoft Azure Integration, Discovery Resources  
- **Keywords:** Azure, Discovery, Classification, Resources  

---

## Custom User/Role Integration  

**Components:**  
- **Support Matrix:** Guardium V9.5 or later  

**Workflow:** Administration → Create Custom User and Role for Integration  

**Links:**  
- **Knowledge:** Guardium IAM Framework, Custom User Management  
- **Keywords:** create_custom_user, create_role, integration_role, custom_permissions  

---

## 2308. GIM management
- **Components:** All versions with GIM installed
- **Limitations:** Requires GIM configured with appropriate permissions
- **Workflows:** Installation – GIM deployments  
**Links:** Knowledge: GIM, Guardium Management; Keywords: GIM, Deployment, Management

## 2309. Audit Only
- **Components:** All versions with Audit Only feature
- **Limitations:** None
- **Workflows:** Audit – Ignore responses; SIN detection  
**Links:** Knowledge: Audit capabilities, pattern detection; Keywords: Audit Only, Session, SIN, Detection

## 2310. Runtime sensitive-object identification
- **Components:** All versions with runtime analysis
- **Limitations:** Requires proper configuration for sensitive data detection
- **Workflows:** Analysis – Runtime sensitive data detection  
**Links:** Knowledge: Runtime analysis, sensitive data identification; Keywords: Runtime, Sensitive object, Identification, Data

## FAM Discovery and Classification
- **Components:** Windows and UNIX/Linux file servers
- **Limitations:** None documented
- **Workflows:** Discovery – Scan file system; Classification – Sensitive data identification  
**Links:** Knowledge: Sensitive data discovery, data classification; Keywords: FAM sensor, UNC path, path, data discovery

## Oracle DataDirect SID Configuration
- **Components:** Oracle databases
- **Limitations:** Local user and LDAP authentication only; Kerberos not supported
- **Workflows:** Configuration – Add Oracle datasource; Authentication – Local/LDAP  
**Links:** Knowledge: Oracle DataDirect, datasource configuration, authentication; Keywords: DataDirect, SID, Oracle, Local user, LDAP

## Runtime Sensitive Object Identification
- **Components:** All supported data sources
- **Limitations:** Requires pattern definition
- **Workflows:** Inspection – Pattern matching; Processing – Sensitive data extraction  
**Links:** Knowledge: Pattern matching, sensitive information detection; Keywords: Runtime, Regex, pattern, Credit card, Email

## Log Only LOGIN_FAILED Sessions
- **Components:** All supported data sources
- **Limitations:** Logs only login failures; other errors ignored
- **Workflows:** Policy – Login failure detection; Action – Log only  
**Links:** Knowledge: Policy configuration, session monitoring; Keywords: LOGIN_FAILED, Session error, Policy rule, Audit log

## Get Correct Service Name for MS SQL Server
- **Components:** Microsoft SQL Server
- **Limitations:** Placeholder name must be known
- **Workflows:** Configuration – Update service name; Resolution – Resolve to actual name  
**Links:** Knowledge: SQL Server service management, configuration parameters; Keywords: MS SQL, Service name, Placeholder, Actual name

## PCI Policy Monitoring
- **Components:** Systems supporting PCI compliance
- **Limitations:** Requires installed PCI policies
- **Workflows:** Administration – Policy installation view; Selection – Choose policy for deployment  
**Links:** Knowledge: PCI compliance, policy management; Keywords: PCI, Policy deployment, Installation view

## User Activity Audit Trail Reporting
- **Components:** All Guardium deployments
- **Limitations:** Three‑part report navigation
- **Workflows:** Reporting – User activity audit trail; Navigation – Report selection; Drill‑down – Third report  
**Links:** Knowledge: Audit reporting, user activity analysis; Keywords: Audit trail, User activity, Report menu, Drill‑down report

## TCP ERROR Logging
- **Components:** All Guardium components
- **Limitations:** Adds detail only to Exception Description field
- **Workflows:** Logging – Capture errors; Storage – Exception description attribute  
**Links:** Knowledge: Error logging, network diagnostics; Keywords: TCP, Error, Exception, Description, Network failure, Logging

## Manage Predefined Data Extraction to File
- **Components:** Guardium systems
- **Limitations:** Disabled by default; requires manual enablement
- **Workflows:** Management – Enable/disable extraction; Scheduling – GuardAPI command execution  
**Links:** Knowledge: Data export, GuardAPI commands; Keywords: Data extraction, File export, GuardAPI, Enable, Schedule

## Custom Comments for Vulnerability Assessment Tests (Workflow)

### Adding and Transferring Custom Comments for VA Tests
- **Components:** All VA test types
- **Limitations:** Requires export/import
- **Workflows:** Addition – Custom Comment Attachment; Transfer – Export/Import Between Systems
- **Knowledge:** VA Test Management, Vulnerability Reporting
- **Keywords:** custom comment, VA test, export, import, Guardium, reporting

## Policy Violation Data

### Log Only Setting
- **Support:** Sniffer parser connectors (e.g., MySQL)  
- **Limitations:** Incompatible with S3 or MongoDB connectors  
- **Workflow:** Configure Log Only → view raw data  

## Replacing GIM Certificates
- **Applicable to:** GIM server and clients  
- **Version Support:** SHA1 and SHA256 certificates  
- **Components:** Security configuration workflow

# Communication Protocols
**Keywords:** SHA1 Certificate, SHA256 Certificate, GIM Communication

## Policy Violation Data
Guardium API Framework handles datasource monitoring via the Manage Datasources configuration workflow. The REST API uses POST to stream configuration changes, requiring HTTP POST requests.

Keywords: API Calls, Datasource References, Credential Management, RESTful Architecture, HTTP Methods, POST Syntax, Endpoint URL, Streaming Configuration

## Hadoop monitoring APIs
The Hadoop ecosystem integrates with Guardium through enabled APIs, which require plugins. Workflows include enabling the APIs and viewing monitoring data.

Keywords: Hadoop Monitoring, API Integration, Hadoop Nodes, Monitoring Metrics, API Calls

## Datasource Connectivity
The `disable_native_audit` command disables cloud datasources' native audit functionality.

Keywords: `disable_native_audit`, cloud datasource, audit disable

## 2370. Outliers detection APIs
Guardium versions 10.1.4+ disable outlier detection via the `disable_outliers_detection_agg` API, which operates on aggregation engines.

Keywords: `disable_outliers_detection_agg`, aggregator, outlier detection

## 2371. REST API syntax
Guardium's REST API disables threat detection use cases via the `disable_threat_detection_use_case` endpoint, requiring a POST request.

Keywords: `disable_threat_detection_use_case`, threat detection, REST POST

## 2372. REST API syntax
To enable outlier detection across central managers, use the `enableOutliersDetectionCrossCMOnAgg` endpoint with a PUT request.

Keywords: `enableOutliersDetectionCrossCMOnAgg`, aggregator, outlier detection

## 2373. Entitlement optimization APIs
Retrieve the expiration date for restored data using the `get_expiration_date_for_restored_day` REST API call.

Keywords: `get_expiration_date_for_restored_day`, expiration date, data restoration

## 2374. Flat Log Process
Retrieve Guardium parameter values with `get_guard_param` on supported platforms.

Keywords: `get_guard_param`, guard parameters, configuration retrieval

## 2375. Assessment APIs
Query threat detection use case information via the `get_threat_detection_use_case_info` endpoint, requiring GET over HTTPS.

Keywords: `get_threat_detection_use_case_info`, threat detection, REST API

## 2376. Datasources example
Modify custom table running timeouts with the `datasource_parameters` customization workflow.

Keywords: `datasource_parameters`, custom table, timeout settings

## 2377. GuardAPI syntax
Register a Guardium unit using the `register_unit` command, specifying `secretKey`, `unitIp`, and `unitPort`.

Keywords: `register_unit`, secretKey, unitIp, unitPort

## 2378. RestAPI syntax
Remove all query rewrite elements with the `remove_all_qr_replace_elements` REST API endpoint.

Keywords: `remove_all_qr_replace_elements`, query rewrite, REST API

## 2379. REST API syntax
Remove custom properties from datasource groups via the `datasource_group_custom_prop_remove` endpoint, requiring a POST request with JSON payload.

Keywords: `datasource_group_custom_prop_remove`, datasource groups, custom properties

## Feature Reference

## Central Management APIs
Supports S-TAP, Managed Units, and Central Managers from Guardium 11.3+. Requires API keys with appropriate permissions. Provides configuration for S-TAP load balancing, association management, and CM backup workflows.

## Diagnostic File Download via FTP
Available on all Guardium-supported platforms. Requires accessible FTP server; files >2GB need segmented download. Configures FTP settings and navigates to download diagnostic tools.

## REST API Endpoint: create_qr_replace_element_byId
Works with all REST-capable Guardium versions. Requires JSON payload with specific schema; HTTPS port 8443 must be open. Part of query rewrite definition configuration.

## REST API Endpoint: DELETE /restAPI/delete_adhoc_policy_analyzer
Available in Guardium 11.0+. Requires admin role; deletes immediately without confirmation. Part of policy analyst API and Guardium REST architecture.

## GuardAPI Endpoint: list_policy_rules
Works with Guardium V10.1.4+. Policy name must be exact match; returns up to 500 rules per call. Used for policy analysis in GuardAPI, Policy Management, and Auditing workflows.

## GrdAPI Endpoint: list_ranger_staps
Supported in all Hadoop environments with Ranger integration. Requires Ranger API access and registered S-TAPs. Part of Hadoop S-TAP management in GrdAPI.

## REST API Endpoint: expire_dates_for_restored_days
Works with all versions having Data Restore functionality. Requires REST API access with proper credentials. Used in data restore analysis workflows involving REST API, restoration, and backup management.

## Configuration Auditing System (CAS) API: list_classifier_policy
Available in all versions with CAS functionality. Returns detailed policy, rule, and action information; may impact performance on large systems. Used in Configuration Auditing System, Policy Classification, and Auditing workflows.

## REST API Endpoint: disable_monitoring_ranger_service
Works with Guardium 10.5+ and Hadoop Ranger integration. Requires admin privileges. Disables monitoring for all Ranger services.

## Guardium Feature Overview

### Feature Management Matrix
- **Components:** Administration workflows differentiate by type: Hadoop Monitoring, Certificate Management, S-TAP Certification, Patch Distribution.
- **Links:** Knowledge includes Hadoop Integration, Venafi API, Certificate Lifecycle Management, Patch Management.

### Integrated Authentication
- **Components:** Mutual SSL authentication disabled; relies on Microsoft Entra ID App Registration.
- **Links:** Knowledge covers Authentication Methods, Entra ID, App Registration.

### CVE Testing
- **Components:** CVE tests supported from Guardium 11.4, requiring internet access.
- **Links:** Knowledge includes Common Vulnerabilities, Guardium Security Intelligence.

### Export Functionality
- **Components:** Export workflow results to CSV, CEF, or PDF formats.
- **Links:** Knowledge includes Export Formats, File Transfer Protocol.

### Certificate Automation
- **Components:** Auto-replace expired target certificates with valid sources.
- **Links:** Knowledge includes Certificate Lifecycle Management, Public Key Infrastructure.

### Alert Templates
- **Components:** Global profile alert message templates must conform to Guardium syntax.
- **Links:** Knowledge includes Alerting System, Message Formatting.

### S-TAP Certification
- **Components:** Allow S-TAP connections to Guardium with valid certificates.
- **Links:** Knowledge includes S-TAP Architecture, Certificate Management.

### Venafi Integration
- **Components:** Central management of certificates via Venafi.
- **Links:** Knowledge includes Certificate Signing, Venafi API, Central Certificate Management.

### Database Monitoring
- **Components:** Monitor database disk usage with fixed threshold at 80%.
- **Links:** Knowledge includes Database Management, Storage Monitoring.

### Hadoop Object Skipping
- **Components:** Skip non-Hadoop objects in Hadoop reports to improve relevance.
- **Links:** Knowledge includes Hadoop Integration, Object Classification.

### Problem Resolution
- **Components:** Resolve common Guardium issues, including K-TAP Live Update and S-TAP reinstallation.
- **Links:** Knowledge includes K-TAP Live Update, S-TAP Installation.

### Post-Deployment Enhancements
- **Components:** Optional steps after Guardium installation, such as language configuration and S-TAP inspection engine setup.
- **Links:** Knowledge includes Language Configuration, S-TAP Installation, Inspection Engine Configuration.

### Patch Distribution
- **Components:** Distribute patches to managed units from the Central Manager.
- **Links:** Knowledge includes Patch Management, Compatibility Verification.

## Patch Management
Distribute and manage patch lifecycles across managed units using aggregators and collectors.

## System Backup and Restoration
Back up and restore stand-alone Guardium systems, ensuring hardware compatibility.

## CLI Administration
Use the `store al` command to configure system parameters via CLI.

## Syslog Alert Timestamp Granularity
Configure timestamp precision for syslog alerts.

## Role Assignment APIs
- **grant_role_to_object_by_Name**: Assign roles by object name.
- **grant_role_to_object_by_id**: Assign roles by object ID.
- **list_associated_stap_mu_groups**: List STAP groups on managed units.
- **list_expiration_dates_for_restored_days**: List expiration dates for restored data.
- **list_qr_condition**: List query rewrite conditions.
- **list_qr_replace_element_byId**: List query rewrite replace elements by ID.
- **register_unit**: Register units in cluster environments.
- **remove_all_from_schedule**: Remove all scheduled actions.
- **remove_classifier_datasource**: Remove data sources from classifiers.
- **remove_datasource_configuration_from_collector**: Remove data source configurations from collectors.

## Ranger Service Management

- **Remove Ranger Service:** Deletes Apache Ranger integration with Guardium. Requirements: Admin privileges; stop service before removal. Accessed via REST API `DELETE /remove_ranger_service`. Related to: External Integrations, Apache Ranger.

## Rule Threshold Management

- **Remove Threshold from Policy Rule:** Removes a threshold from a custom policy rule. Requirements: Admin privileges; rule must allow threshold removal. Not applicable to built-in rules. Accessed via REST API `PUT /remove_threshold_from_rule`. Related to: Threat Detection, Policy Management.

## Job Queue Listener Management

- **Restart Job Queue Listener:** Restarts all queue listeners in Guardium systems with job processing. No parameters. Accessed via API `restart_job_queue_listener`. Related to: Job Scheduling, Background Processing.

## S-TAP Agent Management

- **Restart S-TAP Agents:** Restarts all S-TAP agents on a specified Guardium server. Requires valid database server ID. Accessed via GuardAPI `restart_stap`. Related to: Data Collection, S-TAP Agent Management.

## Audit Process Management

- **Audit Process Management:** Manage audit processes on Linux, Windows, AIX, RHEL, SUSE, Solaris. Requires root/administrator. Includes: Create Audit Process, View Audit Logs. Related to: System Auditing, Log Management, File System Monitoring.

## Data Analysis

## Scan Log Files

- **Scan Log Files for Errors and Warnings:** Scan Oracle log files for specific strings. No restrictions. Useful for: Log Analysis, String Matching.

## CSV Formatting

- **Specify CSV Separator for Output:** Configure CSV separator in Guardium. No restrictions. Related to: CSV Formatting, Data Export.

## Anomaly Detection

- **Stop or Restart Anomaly Detection:** Start or stop anomaly detection from administrative tools. Requires admin privileges. Related to: Anomaly Detection, Monitoring.

## Deployment Health

- **Monitor Unit Utilization:** Monitor appliance health via dashboard. Provides real-time system health alerts. Related to: Unit Utilization, Dashboard Metrics.

## Certificate Management

- **Configure Venafi for GIM Certificates:** Set up Venafi credentials for Guardium Installation Manager. Requires Venafi authentication. Related to: Certificate Authority, GIM Certificates.

## Security Procedures

- **Guardium Public MS-SQL Security System Procedures:** Review security procedures in MS-SQL databases. Requires database roles. Related to: SQL Security, System Procedures.

## S-TAP Installation

- **S-TAP Disk Space Requirements on Windows:** Check free disk space for Windows S-TAP installation. Related to: Disk Management, S-TAP Setup.

## Operator Management

- **Create Operator Subscriptions for Anomaly Detection:** Set up operators for anomaly detection in Kubernetes. Requires CRD definitions. Related to: Operator Lifecycle, Kubernetes Subscription.

## REST API

- **REST API for Change Tracker Events:** Retrieve Guardium change tracker events via REST API. Requires API key. Related to: Event Retrieval, Guardium REST.

- **REST API for Change Tracker Parameters:** Manage change tracker parameters via REST API. Requires API key. Related to: Parameter Retrieval, Guardium REST.

```markdown
## Guardium REST API Reference

### Delete Classifier Action
- **Support Matrix:** All Guardium versions with REST API v1
- **Constraints:** `admin` role required; no confirmation
- **Keywords:** `classifier_action`, `delete`, `admin`, `REST`

### Delete Classifier Policy
- **Support Matrix:** All Guardium versions with REST API v1
- **Constraints:** Policy must not be referenced elsewhere
- **Keywords:** `classifier_policy`, `delete`, `admin`, `REST`

### Delete Classifier Process
- **Support Matrix:** All Guardium versions with REST API v1
- **Constraints:** Process must be active
- **Keywords:** `classifier_process`, `delete`, `admin`, `REST`

### Delete Inactive S-TAPs
- **Support Matrix:** Guardium V11.3 and later
- **Constraints:** `zasadmin` role required
- **Keywords:** `delete_inactive_stap`, `REST`, `ZASAdmin`, `cleanup`

### Disable Persistent Queue
- **Support Matrix:** All Guardium versions with Universal Connector
- **Constraints:** Cannot be re-enabled via API
- **Keywords:** `disablePersistentQueue`, `UC`, `REST`

### Disable Policy Analyzer
- **Support Matrix:** All Guardium versions with Policy Analyzer
- **Constraints:** Must be enabled first; restart required
- **Keywords:** `disable_policy_analyzer`, `restart`, `REST`

### Enable Outliers Detection
- **Support Matrix:** All Guardium versions with Outlier Detection
- **Constraints:** Outlier Detection module must be licensed
- **Keywords:** `enable_outliers_detection`, `outlier`, `REST`

### Get Datasource Custom Properties
- **Support Matrix:** All Guardium versions with REST API v1
- **Constraints:** `cusadmin` role required
- **Keywords:** `datasource`, `custom properties`, `REST`, `cusadmin`

### IP to Alias Overwrites Retrieval
- **Support Matrix:** All Guardium versions supporting IP Aliasing
- **Keywords:** `ip_to_alias_overwrites`, `view`, `REST`

### Get Ranger HDFS Configuration
- **Support Matrix:** Guardium versions supporting Hadoop integration
- **Constraints:** `hdfsadmin` role required
- **Keywords:** `get_ranger_hdfs_config`, `REST`, `integration`

### Assign Latest GIM Bundle
- **Support Matrix:** Guardium Installation Manager v43 and later
- **Constraints:** Bundle must exist on central manager
- **Keywords:** `gim_assign_latest_bundle`, `PUT`, `bundle`, `GIM`

### Register Insights Data Source
- **Support Matrix:** Guardium Insights v1.0.3 and later
- **Constraints:** Pre-generated JSON definition file required
- **Keywords:** `insights_registration`, `POST`, `file`, `registration`

### List Ranger HDFS Configurations
- **Support Matrix:** Guardium versions supporting Hadoop v2.x and later
- **Constraints:** `hdfsadmin` role required
- **Keywords:** `list_ranger_hdfs_config`, `REST`, `integration`
```

## Guardium REST API Operations

### 2522. Reset Validation Summary by Key
**Support:** All versions with REST API  
**Constraints:** API caller role, resets only existing keys  
**Summary:** Deletes specified validation keys.  

### 2523. Restart Cloud Instance
**Support:** AWS, Azure, GCP  
**Constraints:** Requires datasource name, runs on management node  
**Summary:** Restarts the named cloud datasource.  

### 2524. Set Risk Spotter Configuration
**Support:** Risk Spotter enabled (12.0+)  
**Constraints:** JSON body required  
**Summary:** Updates Risk Spotter settings.  

### 2525. Search Data
**Support:** All REST API enabled installations  
**Constraints:** GET only, indexed fields only  
**Summary:** Executes a search query.  

### 2526. Update Datasource by ID
**Support:** All datasources  
**Constraints:** Full HTTPS endpoint, datasource admin role  
**Summary:** Updates a datasource.  

### 2527. Update Datasource Custom Properties
**Support:** 12.0+ with custom properties  
**Constraints:** Endpoint must be `https://[hostname]:8443/restAPI/datasource_custom_prop`  
**Summary:** Updates custom properties.  

### 2528. Update Threshold in Rule
**Support:** Policy Builder 11.5+  
**Constraints:** Endpoint includes hostname/IP and port 8443  
**Summary:** Modifies rule thresholds.  

### 2529. Datasource Builder
**Support:** 12.2+ only  
**Constraints:** Requires API-only account, no UI builder  
**Summary:** Creates datasources via API.  

## Guardium Management Tasks

### Access Reporting APIs
**Support:** All versions with REST API v1  
**Constraints:** `AUDIT_REPORTING` permission required  
**Summary:** Queries reporting permissions.  

### Monitor Table Access
**Support:** Windows servers  
**Constraints:** Requires FAM software, limited by permissions  
**Summary:** Monitors file activity.  

### Remove Unused GIM Bundles
**Support:** All GIM-deployed versions  
**Constraints:** Command line access needed  
**Summary:** Cleans up unused GIM bundles.  

### Datasource Configuration
**Support:** All datasource types  
**Constraints:** Varies by database, consult docs  
**Summary:** Configures datasources.

## Guardium Features

### Generate Security Incident
- **Support:** All Guardium platforms  
- **Prerequisite:** Administrative role  
- **Workflow:** Alert → Generate Incident  
- **Related:** Security Policies, Exception Handling  
- **Keywords:** Security Incident, Unauthorized Access, Exception Message

### Compare Outliers from Database Users with Similar Behavior
- **Support:** All supported databases  
- **Workflow:** Analysis → Compare Behavior  
- **Related:** User Behavior Analysis, Outlier Detection  
- **Keywords:** Outlier, Database User, Stored Procedure, Behavior Analysis

### Exporting Audit Results
- **Support:** All Guardium platforms  
- **Workflow:** Export → CSV, PDF, CEF  
- **Related:** Audit Data Management, Data Formats  
- **Keywords:** Audit Export, CSV, CEF, PDF, Data Handling

### Exception Count
- **Support:** All Guardium platforms (requires licensed feature)  
- **Workflow:** Monitoring → Exception Count  
- **Related:** Compliance Monitoring, Exception Reporting  
- **Keywords:** Exception, Count, Monitoring, Compliance

### Threat Analytics Case for Analysis
- **Support:** All Guardium versions (requires Threat Analytics module)  
- **Workflow:** Analysis → Case Details  
- **Related:** Threat Analytics, Case Management  
- **Keywords:** Threat Analytics, Case, Analysis, Observations

### Managing Query Security Roles
- **Support:** All platforms (requires advanced licensing)  
- **Workflow:** Configuration → Role Management  
- **Related:** Security Roles, Access Control  
- **Keywords:** Query Security, Roles, Access Control, Privileges

### Creating an Assessment
- **Support:** All platforms (requires Assessments module)  
- **Workflow:** Configuration → Create Assessment  
- **Related:** Assessment Planning, Vulnerability Management  
- **Keywords:** Assessment Creation, Vulnerabilities, Data Sources

### Default Certificates
- **Support:** All TLS‑enabled platforms  
- **Workflow:** Configuration → Certificates  
- **Related:** Certificate Management, TLS Configuration  
- **Keywords:** Certificates, Expiration, TLS, Default

### Managing Expiring Certificates
- **Support:** All Guardium‑managed systems (requires Central Manager access)  
- **Workflow:** Management → Certificate Renewal  
- **Related:** Certificate Lifecycle, Central Management  
- **Keywords:** Certificates, Expiring, Renewal, Central Manager

### Deployment Health Topology and Table Views
- **Support:** All supported Guardium deployments (requires monitoring tools)  
- **Workflow:** Monitoring → Health Views  
- **Related:** Deployment Topology, Health Monitoring  
- **Keywords:** Deployment Health, Topology, Table Views, Guardium Architecture

### Configuring Guardium‑S‑TAP Communication by Using an SSL Certificate
- **Support:** Windows, UNIX, Linux, z/OS  
- **Workflow:** Configuration → SSL Communication  
- **Related:** Secure Communication, Network Setup  
- **Keywords:** SSL, S‑TAP, Certificate, Communication

## Scanner Application

### CrashLoopBackOff Investigation Guide
- Describes how to investigate a *CrashLoopBackOff* state for Guardium Scanner pods in Kubernetes. 
- Requires access to pod logs; cannot diagnose external infrastructure problems.
- Key workflows: Diagnostic → Collect Logs, Configuration → Adjust Restart Policy.

### Pods
- Covers Guardium Pods used across all supported Guardium environments.
- Needs Pod management features enabled.
- Main workflow: Management → Pod Operations.

## Scanner Application

## Datasource Connectivity

### DELETE Kafka Cluster
- Deletes a Kafka cluster via the Guardium REST API.
- Supported on all Kafka versions Guardium supports.
- Requires a valid `clusterName` and ensures the cluster isn't actively consumed.
- Workflow: Administration → Remove Cluster.
- Knowledge: Kafka Integration, REST API Endpoints.
- Keywords: clusterName, Kafka Administration, DELETE API.

## Datasource Connectivity

### Dynamic Port Detection
- Enables discovery of DB2, Oracle, MySQL, PostgreSQL, SQL Server, Sybase, Informix, Teradata, and MongoDB ports.
- Requires Browser Service running on Windows; z/OS not supported.
- Workflows: Configuration → Add Datasource; Navigation → View Ports.
- Knowledge: Database Connection Architecture, Browser Service.
- Keywords: S-TAP, Collector, JDBC, Browser Service.

## REST API Operations

### REST API syntax for deleting rules from FAM policies
- Deletes specified rules from File Activity Monitoring (FAM) policies using the Guardium REST API.
- Requires authorization for the API call.
- Workflow: Administration → Remove Policy Rule.
- Knowledge: FAM Policy Management, REST API Operations.
- Keywords: FAM Policy Rule, Delete, REST API, FAM Management.

## Auditing and Reporting

### Audit To-Do List
- **Components:** Guardium Central Management, Standalone Collectors
- **Limitations:** Audit database must be created first
- **Workflows:** Configuration – Generate Audit DB; Navigation – Reports > Audit Process
- **Links:** Audit Process, To-Do List, Data Correlation, Guardium

## Datasource Configuration

### Cloudera Manager
- **Components:** All supported Guardium versions
- **Limitations:** No Kerberos support
- **Workflows:** Configuration – Add Data Source
- **Links:** Data Source Setup
- **Keywords:** Cloudera Manager, Local User Authentication, LDAP

## Knowledge Base

### Auto-discovery Tracking Domain
- **Components:** Guardium 10.5 and later
- **Limitations:** None
- **Workflows:** Navigation – Activity Monitor > Auto-Discovery Tracking
- **Links:** Auto-Discovery, Monitoring
- **Keywords:** Auto-discovery, Tracking, IP Addresses

## Components and Support Matrix

- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** None

## Ignore SQL Errors

- **Support Matrix:** Guardium 11.3 and later
- **Limitations/Constraints:** Applies to span port or network tap sources
- **Workflows:** Configuration — Manage Log Sources

## Active Risk Spotter - Risky Users Scores

- **Support Matrix:** Guardium 11.4 and later
- **Limitations/Constraints:** None
- **Workflows:** Navigation — Risk Assessment > Risky Users

## Data Source Version History

- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** None
- **Workflows:** Navigation — Reports > Data Source Management

## Uid Chain

- **Support Matrix:** Guardium Linux-Unix environments
- **Limitations/Constraints:** Applies to Client/Server Session entities
- **Workflows:** Navigation — Entities > Session Details

## Creating a Test Exception

- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** Exception applies until specified date
- **Workflows:** Configuration — Manage Vulnerability Tests

## Test Detail Exceptions

- **Support Matrix:** Guardium 11.3 and later
- **Limitations/Constraints:** Granular control within test groups
- **Workflows:** Configuration — Manage Test Groups

## Anomaly Detection

- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** Runs at each polling interval
- **Workflows:** Configuration — Manage Anomaly Detection

## Configuring an Azure Target

- **Support Matrix:** Guardium 11.3 and later
- **Limitations/Constraints:** Requires Azure enabled in Guardium
- **Workflows:** Configuration — Manage Archive/Backup Targets

## Creating a New Role

- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** None
- **Workflows:** Configuration — Manage Roles

## Using Central Management Functions

- **Support Matrix:** Guardium 11.3 and later
- **Limitations/Constraints:** Requires Central Management setup
- **Workflows:** Configuration — Central Management

## Central Management Functions

- **Workflows:** Configuration — Synchronize Accounts; Navigation — Monitor Units; Service — Install Policies
- **Keywords:** Guardium Central Manager, Managed Unit, Security Policy, Guardium Portal

## Enabling Enterprise Load Balancing

- **Support Matrix:** Central Manager
- **Limitations/Constraints:** Requires load balancer configuration on managed units
- **Workflows:** Configuration — Enable Load Balancing; Service — Deploy Managed Units

## MustGather CLI Commands

- **Support Matrix:** Collectors, Aggregators, Central Managers
- **Limitations/Constraints:** Requires appropriate OS permissions
- **Workflows:** Service — MustGather Data; Navigation — Diagnostic Data Collection

## Guardium Data Protection Installation Troubleshooting

- **Support Matrix:** Installation Environment
- **Limitations/Constraints:** Platform-specific considerations

## Patch Installation Workflow

### Patch Installation
- Install patches on all supported Guardium platforms using `patch_install`. Requires root/admin credentials and patch bundle location within administrative privileges.

## Data Management

### Configuring Datasource Groups
- Add datasources (SQL Server, Oracle, Db2, MySQL) via browser service on non-z/OS systems. Requires JDBC and Collector access.

## Guardium Feature Reference

### Session-Based Action Rule (Replay Functions)
- Replay transactions with Session Replay action type across all Guardium deployments.

## Policy Analyzer
- Optimize policies using Analyzer insights across all supported Guardium versions.

## Sensitive Data Exfiltration Detection
- Detect unauthorized sensitive data access with Exfiltration Rule across all databases with configured policies.

## Identify Previously Unaudited Sensitive Data
- Discover tagged sensitive data across supported databases for auditing.

## Data Compliance Workflows
- Run compliance workflows using installed templates across all Guardium editions supporting compliance modules.

## PCI/DSS Accelerator
- Generate PCI/DSS reports using PCI module policies on installations with the PCI accelerator.

## Compliance Summary Dashboard
- Access instant security metrics overview via Compliance Summary Dashboard on all Guardium installations.

## Appliance Configuration Settings
- Configure appliance settings with Admin permissions.

nts:
  - **Support Matrix:** Guardium Enterprise deployments
  - **Limitations/Constraints:** Requires configured load balancer
  - **Workflows with different types:** Configuration — Dynamic Load Balancing; Monitoring — Load Balancer Status
- **Links:**
  - **Knowledge:** Load Balancing, HA Architecture
  - **Keywords:** Dynamic Load Balancer, High Availability, Enterprise Deployments

## Centralized Management

### Central Manager Features
- **Components:**
  - **Support Matrix:** All Guardium versions supporting central management
  - **Limitations/Constraints:** Central manager must be licensed
  - **Workflows with different types:** Navigation — Central Manager Overview; Configuration — Central Manager Setup
- **Links:**
  - **Knowledge:** Central Management, Policy Distribution
  - **Keywords:** Central Manager, Policy Propagation, Configuration, Guardium Units

## Maintenance and Administration

### Export Configuration
- **Components:**
  - **Support Matrix:** All Guardium appliances
  - **Limitations/Constraints:** Requires admin role
  - **Workflows with different types:** Procedure — Export Configuration; Backup — Configuration Backup
- **Links:**
  - **Knowledge:** Configuration Management, Export Utilities
  - **Keywords:** Export Configuration, GuardAPI, Configuration Backup

## Data Management

### Simple Search Logging Mode
- **Components:**
  - **Support Matrix:** All supported Guardium versions
  - **Limitations/Constraints:** Affects performance
  - **Workflows with different types:** Configuration — Simple Search Logging; Monitoring — Query Activity
- **Links:**
  - **Knowledge:** Search Optimization, Logging Levels
  - **Keywords:** Simple Search, Logging Mode, Performance, Query Activity

## 2696. Managing GIM clients

- **Components:** All platforms supporting GIM  
- **Limitations/Constraints:** GIM agent must be installed on clients  
- **Workflows:** Update parameters → Client Groups

**Links:** GIM Architecture, Dynamic configuration  

**Keywords:** GIM client, global parameter, dynamic update  

---

## 2728. Activity By Client IP

- **Components:** All supported Guardium platforms  
- **Limitations/Constraints:** Must enable client‑IP resolution (fails for NAT‑masked IPs)  
- **Workflows:** Access Statistics → Activity by Client IP

**Links:** Access statistics, IP‑resolution service  

**Keywords:** Access statistics, client IP, IP‑resolution  

---

## Excessive Errors per period

**Description**  
Shows errors per time slice; flags groups with > N errors in 60 min, broken out by Client IP, Server IP, Server type and DB user.

**Components**  
- **Support Matrix:** All Guardium‑supported databases  
- **Workflows:** Reports → View  

**Links:** Error analytics, threshold alerts  

**Keywords:** Excessive errors, period, client IP, server IP, server type  

---

## Timestamp attribute

**Description**  
Records the exact DB‑server time when a SQL statement executed.

**Components**  
- **Support Matrix:** All Guardium‑supported DB servers  
- **Limitations/Constraints:** Requires access to DB server logs  

**Workflows:** Data Access → Attributes  

**Links:** Data attributes, execution timing  

**Keywords:** Timestamp, execution time, SQL statement, DB server  

---

## SELECT Users query

**Description** (incomplete entry – no usable content)

## Classification Process Results

**Description:** Reports classifier process runs, results, and available features for all roles.  
**Components:** Support Matrix: All Guardium-supported systems; Limitations/Constraints: Requires classification engine setup; Workflows: View > Classification > Results  
**Links:** Knowledge: Data Classification, Process Monitoring; Keywords: Classification, Process, Results, Roles  

---

## FROM Users

**Description:** Object ID uniquely identifies a construct in the Users table and is available only to admin users.  
**Components:** Support Matrix: All Guardium-supported database systems; Limitations/Constraints: Requires admin privileges; Workflows: Administer > Manage Objects  
**Links:** Knowledge: Database Administration, Object Identification; Keywords: Object ID, Admin, Users Table, Unique Identifier  

---

## Access Rule

**Description:** Defines rule metadata and classification context.  
**Components:** Support Matrix: All Guardium-supported databases; Limitations/Constraints: Requires access control setup; Workflows: Configure > Access Control > Rules  
**Links:** Knowledge: Access Control, Rule Management; Keywords: Access Rule, Description, Category, Classification  

---

## CAS for MongoDB

**Description:** CAS Assessment template for MongoDB scans multiple filesystem paths.  
**Components:** Support Matrix: MongoDB supported by Guardium; Limitations/Constraints: Requires CAS setup; Workflows: Configure > Assessment > CAS  
**Links:** Knowledge: CAS, MongoDB Security; Keywords: CAS, MongoDB, Filesystem Scan, Teradata Aster  

---

## Offload Scanning

**Description:** Offloads scanning to the VA scanner to optimize Guardium resources.  
**Components:** Support Matrix: All Guardium-supported databases; Limitations/Constraints: Requires VA scanner setup; Workflows: Configure > Security > Offload  
**Links:** Knowledge: Resource Optimization, Vulnerability Assessment; Keywords: Offload, VA Scanner, Performance  

---

## Planning Archiving

**Description:** Guides archiving, storage capacity planning, and scheduling for long-term audit data preservation.  
**Components:** Support Matrix: All Guardium-supported systems; Limitations/Constraints: None; Workflows: Configure > Archive > Planning  
**Links:** Knowledge: Data Retention, Storage Management; Keywords: Archiving, Storage Capacity, Scheduling  

---

## Default Roles and Applications

**Description:** Lists default roles and associated user interfaces/tools.  
**Components:** Support Matrix: All Guardium deployments; Limitations/Constraints: None; Workflows: Administer > Roles and Applications  
**Links:** Knowledge: Access Management, Role-Based Access; Keywords: Default Roles, Applications, Permissions  

---

## Deployment Health Dashboard

**Description:** Displays data from the entire Guardium deployment, including data availability, latency, and purge status.  
**Components:** Support Matrix: Guardium Data Protection deployments; Limitations/Constraints: Requires dashboard setup; Workflows: Monitor > Dashboards > Health  
**Links:** Knowledge: System Monitoring, Deployment Health; Keywords: Deployment Health, Data Availability, Latency  

---

## PV Storage Recommendation

**Description:** Recommends a multi-node cluster with minimum hardware requirements for Guardium on PV Storage.  
**Components:** Support Matrix: Guardium on PV Storage; Limitations/Constraints: Hardware requirements; Workflows: Deploy > Configuration > Hardware  
**Links:** Knowledge: Performance Requirements, PV Storage; Keywords: PV Storage, Resources, Multi-Node  

---

## Credential Activity Alert

**Description:** Sends a daily alert if Guardium credentials, including LDAP configuration, have changed.  
**Components:** Support Matrix: All Guardium-supported systems; Limitations/Constraints: Alert setup; Workflows: Monitor > Alerts > Credential Activity  
**Links:** Knowledge: Credential Management, Security Alerts; Keywords: Credential Changes, LDAP, Security Alert  

---

## Custom Data Lake Reports

**Description:** Allows building custom reports by duplicating and modifying predefined reports.  
**Components:** Support Matrix: All Guardium-supported systems; Limitations/Constraints: Requires report modification permissions; Workflows: Reports > Custom Reports > Build  
**Links:** Knowledge: Data Lake Management, Report Customization; Keywords: Custom Reports, Data Lake, Query Modification

## Importing from IBM Knowledge Catalog
- Impo

## Threat Management

### Creating Threat Categories from Threshold Alerts
- Supports threshold alerts in Guardium versions that include them.
- **Workflow:** Define Threshold Alert → Create Threat Category
- **Links:** Alerting and Notification, Risk Indicators  
- **Keywords:** Threshold Alert, Threat Category, Risk Management, Security Policies  

## 2805. Security incident policies

- **Workflow:** Create Policy → View Policy Details
- **Links:** Session-Level Policy Templates, Runtime Incident Detection  
- **Keywords:** Guardium Policy, Threat Category, Threshold Alert, Centralized Investigation  

## Inspection Engine Management

### Dynamic Port Detection
- Applies to all supported Guardium databases.
- **Workflows:** Add Inspection Engine (manual) or (automatic)
- **Links:** Inspection Engine Architecture, Dynamic Port Assignment  
- **Keywords:** Inspection Engine, Port, DB2, Oracle  

### CyberArk Integration
- For all supported databases; SDK export restrictions apply.
- **Workflow:** Install CyberArk SDK
- **Links:** Credential Management, Dynamic Secrets  
- **Keywords:** CyberArk, SDK, Vault, Secrets  

### Resolving S-TAP Auto-Start Issues on Linux
- Applies to Linux servers with DB2 or Oracle S-TAP agents.
- **Workflow:** Enable S-TAP Auto-Start
- **Links:** Linux Service Management, S-TAP Agent Configuration  
- **Keywords:** S-TAP, db2tap_10.pid, /etc/event.d/, Auto-Start  

### Managing Kafka Connector Health
- For all Kafka connectors supported by Guardium.
- **Workflow:** CLI — Check Connector Health
- **Links:** Kafka Health Monitoring, CLI Reference  
- **Keywords:** Kafka Connector, Health, CLI Command, Monitoring  

### S-TAP for IBM i APIs
- Requires Guardium V10.6 or later on IBM i systems.
- **Workflow:** CLI — Get Job Process Concurrency Limit
- **Links:** Job Management, Performance Tuning  
- **Keywords:** get_job_process_concurrency_limit, IBM i, Guardium API  

### Connection Profiling List
- For any data source with profiling enabled.
- **Workflow:** Administration — View Profiling List
- **Links:** Profiling, Compliance, Vulnerability Assessment  
- **Keywords:** Slow Query, Grant Failure, CIS Vulnerability, CVE  

### Query Rewrite APIs
- For any Guardium environment with query rewrite enabled.
- **Workflow:** List Quick Search Groups
- **Links:** Policy Management, Query Optimization  
- **Keywords:** Query Rewrite, Quick Search, Groups, API  

## Support for Session‑level Policies
- **Components:** Universal Connector (12.0+) on relational databases
- **Links:** Policy Engine Architecture, Session‑level Access Control, Universal Connector Design  
- **Keywords:** Session‑level Policy, Universal Connector, Guardium 12.0+, CSV mapping, Role‑based access  

## Groups Overview
- **Components:** Member‑by‑ID API
- **Workflow:** create_member_to_group_by_id

## SQL Count
- **Support Matrix:** All Guardium versions
- **Description:** Provides reporting capabilities for SQL Count reports.

## SOX - DB User Activity
- **Support Matrix:** Guardium V9.0 or later
- **Description:** Enables SOX compliance reporting for database user activity.

## Smart Card Parameters
- **Support Matrix:** Guardium V10.2 or later
- **Description:** Configures smart card authentication parameters.

## S-TAP and Inspection Engine APIs
- **Support Matrix:** Guardium V9.5 or later
- **Description:** APIs for restarting UnitPinger and inspection engine processes.

## Log Ingestion Role
- **Support Matrix:** AWS integration with Guardium 12.0+
- **Description:** AWS role for log ingestion with scoped permissions.

## Where to Search
- **Support Matrix:** Guardium Central Manager
- **Description:** Enables file discovery and report review searches.

## NetApp Data ONTAP 7-Mode Permissions
- **Support Matrix:** Guardium 11.3 and ONTAP 7-Mode
- **Description:** File system gathering with Power Users group requirement.

## Configure and Enable Risk Spotter
- **Support Matrix:** Guardium V11.0 or later
- **Description:** Setup for risk analysis and anomaly detection.

## Log SQL Errors
- **Support Matrix:** Guardium V9.0 or later
- **Description:** Logs details of SQL errors, potentially impacting performance.

## Defining a Security Policy to Activate Query Rewrite
- **Support Matrix:** Guardium V8.0 or later
- **Description:** Policy for query monitoring and access control.

## Buffer Usage Monitor
- **Support Matrix:** Guardium V9.0 or later
- **Description:** Monitors system performance and buffer statistics.

## Outstanding Audit Process Reviews
- **Support Matrix:** Guardium V9.0 or later
- **Description:** Reviews uncompleted audit processes with permission checks.

## Defining a CAS-based Test
- **Support Matrix:** Guardium V9.0 or later
- **Description:** Sets up OS-level vulnerability tests using CAS templates.

## Scan Log Files for Errors
- **Support Matrix:** Guardium V9.0 or later with Sybase integration
- **Description:** Monitors Sybase log files for errors requiring accessible sysdevice.

## Atus

### Upgrading Edge Gateway
**Components:** Support Matrix: Edge Gateway 2.0 → 2.1  
**Limitations/Constraints:** Requires admin privileges; patch must be compatible  
**Workflows:** Deployment – Install Patch, Deployment – Run Upgrade Script  
**Links:** Knowledge – Edge Gateway Upgrade Path, Patch Management  
**Keywords:** upgrade, patch, Edge Gateway, version 2.1  

### Download Edge Images
**Components:** Support Matrix: any environment supporting tar archives  
**Limitations/Constraints:** Sufficient disk space for the archive  
**Workflows:** Preparation – Download Image  
**Links:** Knowledge – Docker Image Preparation, Private Registry Setup  
**Keywords:** Edge image, tar archive, private registry, deployment  

### User Access from
**Components:** Support Matrix: all Guardium installations with user‑access monitoring  
**Limitations/Constraints:** None  
**Workflows:** Alerts – Monitor User Access  
**Links:** Knowledge – User Access Monitoring, Credential Abuse Detection  
**Keywords:** user login, IP address, credential abuse, Guardium alert  

### Enable Universal Connector on Collectors
**Components:** Support Matrix: all Guardium collectors  
**Limitations/Constraints:** Requires appropriate licensing  
**Workflows:** Configuration – Enable Universal Connector  
**Links:** Knowledge – Universal Connector Setup, Collectors Configuration  
**Keywords:** Universal Connector, collector, configuration API  

### Intelligent Change Detection
**Components:** Support Matrix: Guardium versions supporting secret management  
**Limitations/Constraints:** None  
**Workflows:** Security – Detect Credential Changes  
**Links:** Knowledge – Credential Encryption, AES‑256 Secret Protection  
**Keywords:** encrypted secret, AES‑256, secret rotation  

### Configuring the HashiCorp Vault
**Components:** Support Matrix: Guardium versions with HashiCorp integration  
**Limitations/Constraints:** Vault server must be reachable from Guardium  
**Workflows:** Deployment – Configure Vault Server  
**Links:** Knowledge – HashiCorp Vault Setup, Secret Management  
**Keywords:** HashiCorp Vault, secret management  

### QRW Force
**Components:** Support Matrix: Guardium with query rewrite engine  
**Limitations/Constraints:** Requires proper IP format  
**Workflows:** Security – Specify WatchClient IPs  
**Links:** Knowledge – Query Rewrite Engine, IP Address Monitoring  
**Keywords:** QRW force, watchClient, IP address, monitoring  

### Hadoop Monitoring APIs
**Components:** Support Matrix: all Hadoop monitoring environments  
**Limitations/Constraints:** API permissions required  
**Workflows:** Data – Manage Hadoop Clusters  
**Links:** Knowledge – Hadoop Monitoring, Guardium API  
**Keywords:** Hadoop API, add cluster, manage services  

### Using Guardium REST APIs
**Components:** Support Matrix: any REST‑client capable environment  
**Limitations/Constraints:** Requires API key or authentication  
**Workflows:** Automation – Execute API Commands  
**Links:** Knowledge – REST API Usage, Guardium API Integration  
**Keywords:** REST API, Guardium commands, API integration  

### Configuration Auditing System (CAS) APIs
**Components:** Support Matrix: Guardium 10.5 and newer  
**Limitations/Constraints:** Requires `clone_extraction_profile` permissions  
**Workflows:** Auditing – Clone GBDI Profile  
**Links:** Knowledge – CAS Cloning, GBDI Configuration  
**Keywords:** clone_extraction_profile, CAS, GBDI, profile cloning  

### Data Mart APIs
**Components:** Support Matrix: Guardium 9.5 and newer  
**Limitations/Constraints:** None  
**Workflows:** Data – Manage Data Marts  
**Links:** Knowledge – Data Mart Management, Extraction Control  
**Keywords:** datamart_set_inactive, data mart, extraction, deactivation  

### Guardium Installation Manager (GIM) APIs
**Components:** Support Matrix: Guardium with GIM installed  
**Limitations/Constraints:** Requires administrative access  
**Workflows:** Diagnostics – Collect Client Diagnostics  
**Links:** Knowledge – GIM Diagnostics, Client Management  
**Keywords:** GIM diagnostics, client diagnostics, Guardium API  

### List Ready Files
**Components:** Support Matrix: Hadoop 2.x, Hadoop 3.x  
**Limitations/Constraints:** Requires HDFS permissions; does not support Kerberos‑encrypted files  
**Workflows:** Configuration → Add Datasource; Monitoring → View Ports  
**Links:** Knowledge – HDFS File Management, Hadoop Datasource Setup  
**Keywords:** Hadoop, ready files, HDFS, monitoring

## Data Source Connectivity

### Edit External S-TAP
- **Support Matrix:** Guardium External S-TAP (all versions)  
- **Limitations/Constraints:** Requires browser service; not supported on z/OS  
- **Workflows:** Configuration – Edit S-TAP Group; Deployment – Activate S-TAP  

### External S-TAP Version Selection
- **Support Matrix:** Guardium 11.3, 11.4 and later  
- **Limitations/Constraints:** Feature availability varies by version  
- **Workflows:** Configuration – Set External S-TAP Version; Compatibility – Verify Supported Features  

### Manage External S-TAP
- **Support Matrix:** All Guardium versions supporting External S-TAP  
- **Workflows:** Configuration – Modify S-TAP Group Settings; Monitoring – Review S-TAP Status  

---

## Guardium Feature Reference

### Host References Report
- **Support Matrix:** Report query capability (any Guardium)  
- **Limitations/Constraints:** Requires custom tables and resolvable hostnames/IPs  
- **Workflows:** Navigation – Host References; Analysis – Custom Queries  

### Number of DBs per Type
- **Support Matrix:** All Guardium-supported database types  
- **Limitations/Constraints:** Defaults to current day unless a custom date range is set  
- **Workflows:** Configuration – Change Date Range; Navigation – System Overview  

### Command Entity
- **Support Matrix:** All command constructs (SQL, CLI, etc.)  
- **Limitations/Constraints:** Parent node identification requires nested statements  
- **Workflows:** Analysis – Command Entity Detection; Configuration – Entity Reporting  

### Default Certificate
- **Support Matrix:** All SSL‑enabled Guardium components  
- **Limitations/Constraints:** Expiration policy is built‑in  
- **Workflows:** Administration – Certificate Management; Security – SSL Configuration  

### Public System Configuration
- **Support Matrix:** All database alteration commands (ALTER DATABASE, ALTER SYSTEM, etc.)  
- **Limitations/Constraints:** Requires administrative privileges  
- **Workflows:** Administration – System Settings; Security – Database Alteration Auditing  

### Pods in CrashLoopBackOff
- **Support Matrix:** Kubernetes environments with Guardium vulnerability scanners  
- **Limitations/Constraints:** Does not affect other services, only scanner health  
- **Workflows:** Troubleshooting – Pod Health Monitoring; Monitoring – Scanner Status  

### Session ID Parameters
- **Support Matrix:** All applications exposing session ID packets  
- **Limitations/Constraints:** Prefixes and postfixes must be non‑overlapping  
- **Workflows:** Configuration – User Indicator Packet Parsing; Monitoring – Session Tracking

## Policy Management

### Dynamic Auditing Policy Creation
- **Components:**
  - **Supports:** Guardium versions with Risk Spotter module
  - **Constraints:** Increases system load when enabled
  - **Workflow:** Configuration → Policy Manager → New Dynamic Auditing Policy
- **Links:**
  - **Knowledge:** Risk Spotter, Audit Policy Lifecycle, Data Activity Profiling
  - **Keywords:** Dynamic Auditing, Real-time Monitoring, Risk Spotter

### Selective Audit Trail
- **Components:**
  - **Supports:** All supported databases
  - **Constraints:** Applies only to session-level policies
  - **Workflow:** Configuration → Policy Manager → Edit Policy → Selective Audit
- **Links:**
  - **Knowledge:** Audit Trail, Logging Optimization
  - **Keywords:** Audit Logging, Session Filters, Log Reduction

### With (WITH)
- **Components:**
  - **Supports:** Guardium 11.3+
  - **Constraints:** None
  - **Workflow:** Configuration → Policy Builder → WITH Options
- **Links:**
  - **Knowledge:** Rule Evaluation, Condition Logic
  - **Keywords:** EXC_MSG, TRACK, DISTINCT, LABEL, SET_TRUST

### Join Entity
- **Components:**
  - **Supports:** Versions supporting SQL

## Data Insights

### Troubleshooting Guardium Data Protection Policies
- **Purpose:** Guide for resolving UI and policy configuration issues in Guardium Data Protection.
- **Support:** All Guardium Data Protection versions.
- **Requirement:** Appropriate user permissions.
- **Location:** Help → Troubleshoot Policy Issues.

### Inspection Engine Tab
- **Purpose:** View and modify inspection engine parameters for real-time data monitoring.
- **Support:** All Guardium versions with inspection engine enabled.
- **Requirement:** Inspection engine must be active.
- **Location:** System Configuration → Inspection Engine → View/Modify Parameters.

## Policies

### Inactive Managed Unit Alert
- **Purpose:** Notify administrators of inactive managed units.
- **Support:** All Guardium Managed Units.
- **Requirement:** None.
- **Location:** Administration → Alerts → Inactive Managed Unit Alert.

## Configuration

### Deploy External S-TAP from Guardium UI
- **Purpose:** Deploy an external S-TAP in Kubernetes environments (Amazon EKS, Azure AKS).
- **Support:** Kubernetes environments with prior S-TAP configuration.
- **Requirement:** Kubernetes setup and prior external S-TAP configuration.
- **Location:** System Configuration → External S-TAP → Deploy.

### Group APIs
- **Purpose:** Manage groups via API.
- **Support:** Guardium V9.5+.
- **Requirement:** API access permissions.
- **Location:** Administration → APIs → Group APIs.

### Datasource Credential Management APIs
- **Purpose:** Manage datasource credentials securely.
- **Support:** Guardium V10.1.4+.
- **Requirement:** API access rights and Cyral licensing.
- **Location:** Administration → APIs → Datasource Credential Management APIs.

## Errors

### None (Bundle Not Found)
- **Purpose:** Handle bundle installation errors in Guardium Installation Manager.
- **Support:** Guardium Installation Manager environments.
- **Requirement:** No downgrades supported; older bundles cannot be installed over newer versions.
- **Location:** GIM → Install Bundle → Select Bundle.

## Tools

### GuardAPI Syntax
- **Purpose:** Reference for GuardAPI syntax and usage.
- **Support:** All Guardium systems supporting GuardAPI.
- **Requirement:** Proper parameter syntax and appropriate access levels.
- **Location:** Help → GuardAPI Syntax → datamart_refresh_metadata.

## Data Sources

### MS SQL Server (DataDirect - Dynamic Port)
- **Purpose:** Configure MS SQL Server datasources with DataDirect driver for dynamic ports.
- **Support:** MS SQL Server.
- **Requirement:** DataDirect driver for dynamic port.
- **Note:** Specific workflows and additional details not provided.

## Features Overview

**Authenticating by using security credentials**
- Supports AWS S3, EC2, RDS
- Requires valid AWS account
- Use Access Key and Secret Key workflows

**FAM domain**
- Supports Guardium Data Protection
- Configure File Discovery and File Entitlement Reports

**GIM client allocation**
- Supports Linux/UNIX platforms
- Configure and update GIM clients

**Restart all managed units**
- Applies to Central Manager and Managed Units
- Requires operational central manager

## Feature Categories

**Custom certificate**
- Configuration: Add Certificate
- Requires existing target keystore

**Deployment inventory**
- Reporting: Deployment Inventory Summary

**Self Monitoring**
- Monitoring: System Health Dashboard
- Available from Guardium 11.0+

**Big Data Intelligence with data marts**
- Integration: Data Mart Export
- Available from Guardium 10.5+ on Hadoop/Cloudera

**Linux S-TAP is not capturing Db2 exit traffic**
- Troubleshooting: Db2 Exit Health Check
- Supported from Linux S-TAP 10.6+

**OUA over JDBC connect**
- Configuration: Enable On-Premises Audit
- Available from Guardium 12.0+ with UConn patch 5002

**Db2 instance name**
- Installation: Database Configuration
- Supported on Db2 for i 7.1 and above

**GIM global parameters**
- Administration: Manage Global Settings
- Available from GIM 10.0+

**Port Protocol Purpose**
- Configuration: Define S-TAP Ports
- Supported from S-TAP 10.5+ for z/OS, IMS

**Assessment APIs**
- Configuration: Vulnerability Assessment Setup
- Available from Guardium 11.3+

**Entitlement optimization APIs**
- Reporting: Entitlement Optimization Dashboard
- Available from Entitlement Optimization 2.0+

**GuardAPI syntax**
- API: delete_export_configuration
- Available from GuardAPI 1.0+

**Guardium universal connector**
- Integration: Universal Connector Setup
- Available from Guardium 12.2+

**Rule APIs**
- Automation: Manage Rule Actions
- Available from Rule API 1.1+

**Customizing the User Interface**
- Administration: Smart Assistant Configuration
- Available from UI Customization 4.1+

## Feature Reference Details

**Datasource Connectivity**
- Supports SQL Server, Oracle, Db2, MySQL
- Requires browser service running (not z/OS)
- Workflow: Add Datasource, View Ports

**Data Source Reporting**
- All supported Guardium datasources
- Navigation: Dashboards, Data Source Summary

**Cloud Database Service Protection**
- Supports AWS RDS, Azure SQL Database, Google Cloud SQL
- Requires native audit integration
- Workflow: Enable Protection, Cloud Service Audits

### Reporting on Data Source Changes
**Components:** Change Audit reports, CDC enablement on sources  
**Limitations:** Requires change data capture enabled  
**Links:** Change Management, CDC Configuration  

### MS SQL Server Dynamic Port Monitoring
**Components:** Dynamic Port Detection, Port Allocation monitoring  
**Limitations:** Requires JDBC driver version 7.0+  
**Links:** SQL Server Dynamic Ports, JDBC Driver Configuration  

### AWS Secrets Manager Integration
**Components:** Secret creation, secret access integration  
**Limitations:** AWS IAM permissions required  
**Links:** AWS Secrets Manager, Datasource Credentials  

### Inactive User/Role Cleanup
**Components:** Inactive Users navigation, Cleanup actions  
**Links:** User Management, Role Management  

### Active Threat Analytics Exclusion List
**Components:** Exclusion List configuration, Threat Analytics monitoring  
**Links:** Threat Analytics Configuration, False Positive Reduction  

### Session Policy Ignore Users
**Components:** Policy creation, Session ignore list  
**Limitations:** Session-level policies only  
**Links:** Session Management, Policy Configuration  

### Detailed Session Logging
**Components:** Full logging configuration, Session audit monitoring  
**Limitations:** May impact performance on high-volume systems  
**Links:** Session Logging, Performance Impact  

### Custom Domains
**Components:** Custom Domains configuration, Domain filtering analysis  
**Limitations:** Requires user-uploaded data files  
**Links:** Custom Domain Management, Data Upload  

### Patch Availability Reporting
**Components:** Available Patches navigation, Patch Management system  
**Limitations:** Requires Internet connectivity for external patches  
**Links:** Patch Management, System Updates  

### Data Warehouse Select Access Reporting
**Components:** Object Field Access reports, Query auditing  
**Limitations:** Requires query auditing enabled  
**Links:** Data Warehouse Auditing, SELECT Auditing  

### API Report Generation
**Components:** Reports via Guardium REST API  
**Limitations:** API tokens required  
**Links:** REST API Usage, Report Export  

### Alerter Configuration
**Components:** Alerter settings, Notification mechanisms  
**Limitations:** Email/SNMP/Syslog must be properly configured  
**Links:** Notification Mechanisms, Alerting Policies  

### Custom Certificate Management
**Components:** Custom certificate handling, Source/target compatibility  
**Links:** System Security Configuration, Certificate Formats

# Guardium Management Overview

## Workflows
- **Migration:** Replace certificates
- **Transformation:** Enable IPv6 in IPv4 deployments

## Authentication
- **Setup authentication sources:** Configure all supported methods

## Time Periods
- **Create time periods** for policies and queries

## Permissions
- **Grant procedures to PUBLIC** with caution

## Monitoring
- **File activity analysis:** Monitor all supported filesystems

## Auditing
- **Audit Apache Solr and Sentry** with correct plugin configuration

## Certificate Management
- **Handle External S-TAP certificates:** Manage CSR workflow

## Diagnostics
- **Run GIM diagnostics** on clients

## Maintenance
- **Remove unused GIM bundles**

## Commands
- **Show purge age period** with `show run_cleanup_orphans_daily`

## Hadoop Integration
- **Add receiver to rule action** via Guardium API

## S-TAP/Z File Management
- **Manage DB users, test exceptions, and IMS access**

## Configuration
- **Map external feeds** on a scheduled interval

## Assessment
- **Find vulnerability assessments** using the Finder screen

## Security
- **Monitor file permissions** on Oracle databases

## Configuration Parameter `file_permissions_monitoring`

Enabling `file_permissions_monitoring` adds file permission checks to Guardium workflows. It integrates with Privilege Management and Oracle Data File Security. Use the `Guardium Agent` to apply the settings.

## Pre‑Set System Parameters

Guardium appliances support a CLI‑only set of system parameters. Changes made via the CLI persist, while the UI provides a read‑only view. Common categories include Installation Parameters and CLI Reference. Refer to the Installation Parameters and CLI Reference documentation for details.

## Archived Data Restoration

All Guardium archive destinations (S3, NFS, local) support data restoration. Ensure sufficient disk space and understand that point‑in‑time granularity is limited to the archive interval. Historical Reporting and Data Retention topics provide additional context.

## Data Archive Configuration

Audit results can be archived, but raw log data is excluded. Archiving jobs run during low‑usage windows and support configurable retention policies. Backup & Recovery and Audit Log Management topics give further guidance.

## Role Based Access Control

Guardium supports all built‑in and custom roles with a fixed permission inheritance hierarchy. Super‑admin rights cannot be overridden. Access Control and User Management documentation explains role definition and assignment workflows.

## Edge Deployment via Terraform

Kubernetes v1.18+ on any cloud provider can be used for edge deployment. Pre‑provisioned persistent storage and properly configured IAM roles for Terraform are required. The Edge Architecture and Infrastructure as Code topics provide background.

## Terraform Bundles for Edge

Same requirements as the general edge deployment via Terraform. On‑premises legacy infrastructures are not supported. Automation Tools and Deployment Prerequisites documentation offer additional setup information.

## S‑TAP Service Management

All supported database platforms allow starting and restarting the S‑TAP service. Root/administrator privileges are required, and a brief interruption in captures may occur during restart. The S‑TAP Service and Agent Lifecycle topics provide operational details.

## Pre‑Installation Requirements

Guardium 11.x and later require internet access for Fix Central, and firewall rules must permit outbound HTTPS. The Software Distribution and Fix Central Access documentation detail the preparation steps.

## GIM Central Installation

Guardium 11.5+ supports centralized Guardium Installation Manager (GIM) installations. The GIM server must be reachable from all target database servers. GIM Architecture and Centralized Deployment topics explain the workflow.

## Client‑Initiated Setup

Guardium 12.0+ appliances allow setup initiated by a client tool. The GUI tool requires local admin browser access to the Guardium instance. Installation Tools and Central Console documentation cover the process.

## Ad‑hoc Audit and Run API

Available on all API‑capable Guardium installations, this API creates one‑time reports that expire after 24 hours. Scheduling is not supported. API Architecture and Report Lifecycle documentation explain usage.

## List External Feed Reports API

Supported from Guardium 11.3 onward, this API lists reports and requires an admin API key. Results are paginated for large installations. API Endpoints and Report Catalog documentation provide additional details.

## Guardium Feature Reference

### 3059. GuardAPI Add/Remove Custom Property
- Components: Support Matrix (11.3+), Limitation (requires string parameters `customProps` and `name`), Workflow (Administration — GuardAPI)
- Links: Knowledge (GuardAPI CLI), Keywords (`add654c5-5d6f-46f1-9c1f-b25495a3f7e4`, `remove_custom_property_from_datasource_by_name`)

### 3062. Oracle Data Source Service Name
- Components: Support Matrix (OD 8.0+), Limitation (service name must be configured), Workflow (Configuration — Oracle Data Source)
- Links: Knowledge (Oracle Configuration, DataDirect Drivers), Keywords (Service Name, JDBC)

### 3063. Sensitive Data Discovery Policy
- Components: Support Matrix (12.0+), Limitation (requires `create_policy` permission), Workflow (Configuration — Define Policy)
- Links: Knowledge (Sensitive Data Discovery), Keywords (policies, rules, sensitive data, discovery)

### 3064. Find Name in SQL Query Alert
- Components: Support Matrix (12.0+), Limitation (requires session-level policy), Workflow (Configuration — Session-Level Policy, Navigation — Policy Builder)
- Links: Knowledge (Policy Builder, SQL Monitoring), Keywords (alert, detection)

### 3067. VA Test Detailed Report
- Components: Support Matrix (Vulnerability Assessment 2023.1+), Limitation (requires VA permission), Workflow (Navigation — VA Dashboard, Configuration — Filters)
- Links: Knowledge (Vulnerability Assessment), Keywords (VA Tests, Filters, Configuration)

### 3069. Table Type Attribute Summary
- Components: Support Matrix (12.0+), Limitation (none), Workflow (Reporting — Table Summary, Navigation — InnoDB/MyISAM Summary)
- Links: Knowledge (Table Types, Database Sizes), Keywords (InnoDB, MyISAM, Counts, Sizes)

### 3070. VA Deployment for Db2 for i
- Components: Support Matrix (12.0, Db2 for i 7.5+), Limitation (requires Db2 for i agent), Workflow (Administration — VA Deployment, Configuration — VA Tests)
- Links: Knowledge (Db2 for i, Vulnerability Assessment), Keywords (VA Tests, Group Users)

### 3071. Test Tuning
- Components: Support Matrix (11.3+), Limitation (requires test modification permission), Workflow (Configuration — Test Tuning, Optimization — Group Exceptions)
- Links: Knowledge (Test Parameters, Exceptions), Keywords (Tuning, Parameters, Exceptions)

### 3072. Tuning a Test (Feature)
- Components: Support Matrix (12.0+), Limitation (requires Tuning permission), Workflow (Configuration — Test Tuning, Optimization — Test Detail Exceptions)
- Links: Knowledge (Test Optimization), Keywords (Test Tuning, Exceptions)

## Guardium Data Management

### File Permissions & Ownership
- **Guardium 12.0+** supports **file permission** and **ownership** checks for Informix 14.10+ and Oracle 19c+. Requires testing permissions. Workflows: *File Permission Checks* (reporting), *Informix Files* (navigation); *File Ownership Checks* (reporting), *Oracle Directories* (navigation).  
- **Sybase** also has file permissions checks under *Diagnostic > Inspect*.

### License Requirements
- **Guardium** mandates a **base license** and optional **append licenses** for all products. Managed under *Administration > License Management*.

## Guardium Central Management

### Cross‑CM Health View
- **All supported Guardium platforms** can create a **health view** aggregating status across multiple CMs. Requires a dedicated Guardium system.  
- Workflow: *Configuration > Health View* (Configuration).  

### Central Management Problem Solving
- Troubleshoot **Guardium Central Manager** issues: must be reachable, check CM health, review HA configuration.  
- Workflow: *Administration > Central Management*.

### Resolving A‑TAP Missing Capture Issues
- Fix **A‑TAP not capturing** on **S‑TAP**: check root access, run diagnostic script.  
- Workflow: *Diagnostic > A‑TAP Script*.

### Oracle 23ai A‑TAP Activation Parameters
- **Oracle 23ai** needs **db_version** and **db_use_instrumented** set to enable A‑TAP.  
- Workflow: *Configuration > A‑TAP Settings*.

## Guardium S‑TAP & Kubernetes Integration

### IBM i S‑TAP Definition
- Define **S‑TAP for IBM i**: ensure network routing, follow *Installation > Define S‑TAP* workflow.  

### Kubernetes External S‑TAP Parameter Tab
- **Parameter tab** for **Kubernetes external S‑TAP**: provide cluster access, see *Installation > Kubernetes Tab* (Table 1).  

### External S‑TAP TAP Tab Settings
- Configure **TAP tab** for **external S‑TAP**: no special constraints.  
- Workflow: *Configuration > TAP Tab*.

## Guardium Activity Reporting

### Enterprise Load Balancer Monitoring Report
- **Enterprise deployments**: can generate *Load Balancing Activity* reports. No constraints.  

### Full SQL Report Time Filtering
- **Full SQL DataSources**: **TimestampUTC** required for time‑based queries on *Fullsql_view*.

# Guardium Functional Reference

## Model, Append Licenses
Append licenses to add or extend Guardium functionality.

## APIs for Database User Management
Guardium user API endpoints support authentication and database mapping.

## Guardium Insights API Documentation
Authorized clients can integrate with the Guardium Insights platform.

## 3092. EF - SQL Detail
View EF SQL detail and SQL statistics for all supported database versions.

## 3093. Data mart APIs
Manage and update data mart settings with API operations.

## 3094. Customer uploads
Configure long-term retention and external application integration.

## 3095. Client time zone (CTIMEZONE)
Filter sessions by client time zone for database name filtering.

## 3096. REQUEST_ERROR example
Monitor SQL errors with session policies.

## 3097. File discovery and classification GIM parameters
Detect and classify files with GIM parameters.

## 3098. Predefined reports
Use and create custom reports from predefined templates.

## 3099. Test Detail Exception
Manage exception records from security assessment results.

## 3100. Access Rule
Define policy actions and logging with access rules.

## 3101. How IP addresses work
Monitor traffic within specified IP address pairs.

## 3102. Cloud deployment
Troubleshoot and resolve cloud deployment issues.

## 3103. Managing access by IP address
Control data stream monitoring by IP address pairs (Guardium v10.6+).

## Monitoring and Reporting APIs
- **Guardium Version:** 12.2.x and later
- **Components:** Enable/Disable Monitoring Streams
- **Workflow:** API Overview → Features → Usage
- **Links:** API Documentation, Risk Analytics
- **Keywords:** enable_disable_monitoring_streams, stream toggling

## Active Threat Analytics and Risk Spotter
- **Supported Versions:** 12.2.x and later
- **Requires:** API access
- **Workflow:** API Overview → Risk Spotter Features
- **Links:** API Documentation, Risk Spotter
- **Keywords:** get_certificates, active threat analytics, risk spotter

## Reports and Report Generation
- **Supported Versions:** All
- **Workflow:** Data Analysis → Unit Utilization Management
- **Links:** Data Analysis, Utilization Metrics
- **Keywords:** reset_unit_utilization_data, metrics management

## Database Cataloging and Management
- **Supported Versions:** All
- **Requires:** Database discovery enabled
- **Workflow:** Database Cataloging → Vulnerability Assessment
- **Links:** Database Cataloging, Vulnerability Assessment
- **Keywords:** catalog databases, manage databases, classification

## Investigation Dashboard Chart Filtering
- **Supported Versions:** All with Investigation Dashboard
- **Workflow:** Chart Filtering → Chart Management
- **Links:** Investigation Dashboard, Chart Management
- **Keywords:** chart filtering, investigation dashboard

## CEF SIEM Integration
- **Integration:** OPTIM to Guardium Interface
- **Requires:** Network connectivity
- **Workflow:** Configuration → Add OPTIM Datasource
- **Links:** CEF, SIEM Integration, Data Correlation
- **Keywords:** OPTIM, CEF, SIEM, Correlation

## Oracle DB2 with DataDirect
- **Supported Versions:** Oracle 19c, 21c
- **Requires:** DataDirect v9 or later
- **Workflow:** Configuration → Add Datasource → Oracle SID
- **Links:** Oracle Database Architecture, DataDirect Drivers
- **Keywords:** Oracle, SID, DataDirect

## Couchbase Account Configuration
- **Supported Versions:** Couchbase 6.5 and later
- **Requires:** Read access to bucket data
- **Workflow:** Configuration → Authentication → Add Couchbase Account
- **Links:** NoSQL Data Sources, Couchbase Architecture
- **Keywords:** Couchbase, Bucket, Account Owner

## Case Reopen in Active Threat Analytics
- **Module Version:** 3.3+
- **Requires:** User permissions
- **Workflow:** Actions → Bulk Actions → Reopen
- **Links:** Case Management, ATLAS UI
- **Keywords:** ATLAS, Bulk, Case Reopen

## Session-Level Policy Creation
- **Supported Databases:** All guarded
- **Requires:** READ_WRITE on Policy Builder for Data
- **Workflow:** Policy Builder for Data → Create New Session Policy
- **Links:** Session-Level Policy Design, Policy Builder for Data Interface
- **Keywords:** Session Policy, Policy Builder

## Quick Parse Configuration
- **Supported Databases:** PostgreSQL, MySQL, Oracle, DB2
- **Options:** QUICK_PARSE, QUICK_PARSE_NO_FIELDS
- **Workflow:** Inspection Engine → Advanced Options → Quick Parse
- **Links:** Database Query Parsing, Inspection Engine Configuration
- **Keywords:** QUICK_PARSE, Shallow Parsing

## Ignoring Sessions
- **Supported Versions:** 12.0 SP1+
- **Workflow:** Policies → Ignore Sessions → Add Criteria
- **Links:** Session Management, Policies, Alert Suppression
- **Keywords:** Ignore Sessions, Session Criteria

## Rule Action Logging
- **Supported Versions:** All
- **Consideration:** Logging impacts storage use
- **Workflow:** Policies → Edit Rule → Actions → Log/Ignored
- **Links:** Policy Rule Actions, Logging Configuration
- **Keywords:** Rule Logging, Ignore Actions

## Topology View
- **Supported Versions:** All UI versions
- **Requires:** Network diagram data populated
- **Workflow:** Visualization → Topology View
- **Links:** System Architecture, Topology Visualization Tools
- **Keywords:** Topology, Network Diagram

## 3118. DW SELECT Object Access
**Support Matrix:** All data warehouse systems supported by Guardium
**Limitations/Constraints:** None
**Workflows:** Reports → Standard Reports → DW SELECT Object Access
**Knowledge:** Data Warehouse Reporting, Object Access Analysis
**Keywords:** Object Access, DW SELECT, Object Names, Access Report

## 3119. Viewing Drill-Down Reports
**Support Matrix:** All supported Guardium reporting modules
**Limitations/Constraints:** Requires pre-configured drill-down relationships
**Workflows:** Reports → Drill-Down → Select Report Link
**Knowledge:** Report Hierarchies, Data drill-down Functionality
**Keywords:** Drill-Down, Guardium Reports, Detailed Data, Linked Reports

## 3120. Attribute Description
**Support Matrix:** All supported Guardium assessment modules
**Limitations/Constraints:** None
**Workflows:** Reports → Assessments → Assessment Results → Details
**Knowledge:** Data Security Posture, Assessments, Attribute Analysis
**Keywords:** Data Protection, Guardium Attributes, Security Assessment

## 3121. Ack Response
**Support Matrix:** All DB2, Oracle, SQL Server connections
**Limitations/Constraints:** Ack Response visibility in detailed reports only
**Workflows:** Reports → DB2, Oracle, SQL → Ack Response Summary
**Knowledge:** Acknowledged Response, Database Query Performance
**Keywords:** Ack Response Time, DB Performance, Query Metrics

## 3122. Event User
**Support Matrix:** All Guardium installations with event logging enabled
**Limitations/Constraints:** Depends on GuardAppEvent:Start implementation
**Workflows:** Configuration → Event Management → Event Settings
**Knowledge:** Event Logging, Audit Trails, User Activity
**Keywords:** Event User, GuardAppEvent, Event Logging, Audit Trail

## 3123. Assessment Result Datasource Entity
**Support Matrix:** All supported Guardium assessment modules
**Limitations/Constraints:** None
**Workflows:** Reports → Assessments → Entity Details
**Knowledge:** Security Assessments, Datasource Evaluation
**Keywords:** Assessment Results, Datasource Entities, Security Evaluation

Matrix:** Guardium Enterprise with feature key enabled.
  - **Limitations/Constraints:** Must be configured through the Policy Builder interface.
  - **Workflows with different types:** Exception Management — Configure Ignore Actions
- **Links:**
  - **Knowledge:** Policy Builder, Custom Exception Handling, Guardium Enterprise Features
  - **Keywords:** ignore, exceptions, policy, actions, Guardium Enterprise

### Create and modify experts
- **Components:**
  - **Support Matrix:** Guardium Enterprise (requires expert feature key).
  - **Limitations/Constraints:** Experts can only be created by users with the Expertise Manager role.
  - **Workflows with different types:** Workflow — Expert Configuration
- **Links:**
  - **Knowledge:** Expertise Framework, Custom Rule Development, Enterprise Roles and Permissions
  - **Keywords:** experts, create, modify, configuration, Guardium Enterprise

### Differences between describe and regular assessments
- **Components:**
  - **Support Matrix:** All Guardium versions supporting assessments.
  - **Limitations/Constraints:** Describe assessments cannot be scheduled; they are ad‑hoc only.
  - **Workflows with different types:** Reporting — Run Describe Assessment
- **Links:**
  - **Knowledge:** Assessment Types, Ad‑hoc vs Scheduled Reporting, Data Discovery
  - **Keywords:** describe, assessment, regular, scheduling, reporting

## Assessment Roles Allowed
- **Support Matrix:** All Guardium products
- **Workflows:** Configuration – Generate Report
- **Links:** Role Management, Security Assessment

## Group Usage Report
- **Support Matrix:** All Guardium products
- **Workflows:** Configuration – Generate Report
- **Links:** Group Management, Dependencies

## Exception Count Report
- **Support Matrix:** All Guardium products
- **Workflows:** Configuration – View Exceptions
- **Links:** Exception Handling, Reporting

## VA Tests Domain
- **Support Matrix:** All Guardium products
- **Workflows:** Configuration – Security Assessment
- **Links:** Vulnerability Assessment, Domains

## Enable IPv6 in New Deployment
- **Support Matrix:** All Guardium products
- **Workflows:** Installation – IPv6 Selection
- **Links:** Network Protocols, Installation

## Request Encrypted Assertion
- **Support Matrix:** All Guardium products
- **Workflows:** Configuration – SAML Integration
- **Links:** SAML, Security, Assertion Encryption

## Predefined Reports from Accessmgr
- **Support Matrix:** All Guardium products
- **Workflows:** Reporting – Run Accessmgr Reports
- **Links:** System Access, Reporting

## Predefined Alerts
- **Support Matrix:** All Guardium products
- **Workflows:** Monitoring – Configure Alerts
- **Links:** Alert Management, Monitoring

## Scheduled Job Exceptions Alert
- **Support Matrix:** All Guardium products
- **Workflows:** Monitoring – Schedule Alert
- **Links:** Monitoring, Scheduled Jobs

## Configuring Long Term Retention
- **Support Matrix:** Guardium 12.2.x and later
- **Workflows:** Configuration – Long Term Retention
- **Links:** Data Archiving, Amazon S3, Retention Policies

## User Interface Troubleshooting
- **Support Matrix:** All Guardium products
- **Workflows:** Troubleshooting – UI Problems
- **Links:** User Interface, Troubleshooting

## Deploy External S-TAP with Helm
- **Support Matrix:** All Guardium products
- **Workflows:** Deployment – Helm Installation
- **Links:** Helm, Kubernetes, Deployment Automation

## Custom Partitioning During Installation
- **Support Matrix:** All Guardium products
- **Workflows:** Installation – Partition Choices
- **Links:** Installation, Partitioning

## Data Mart Extraction API

## Guardium v12.2.2 API Extraction

- API access required for data mart extraction starting in v12.2.2.

## Basel II SQL Error Monitoring

- All Guardium products support Basel II SQL error monitoring, requiring the Basel II module.

## Universal Connector API Integration

- Starting in version 12.0, Universal Connector APIs enable API integration and endpoint management.

## File Activity Investigation Dashboard

- Access and filter file activity data on the dashboard across all supported Guardium file sources.

## Database Entitlement Flat Log Process

- Generate entitlement reports first, then run and schedule flat logs for distribution.

## Guardium User Interface Improvements

- Enhancements apply to all interfaces, affecting navigation and configuration workflows; browser compatibility may impact experience.

## MS SQL Server DataDirect Connectivity

- Configure datasources and test connections using DataDirect drivers after installation.

## Transform Actions and Parameters

- Configure supplemental parameters for data transformation workflows requiring performance considerations.

## Policy Rule Tag Management

- Assign unique tags to rules within policies using policy builder and tagging interfaces.

## Value Change Auditing Setup

- Enable auditing for value changes, noting additional storage requirements, then view changes in history.

## Group Domain Management

- Manage unique members in groups across interfaces.

## Group By SQL Clause

- Use with SELECT statements for aggregation, in conjunction with grouping and HAVING rules.

## Assessment Results Viewing

- Navigate to results after assessments complete to generate reports and interpret findings.

## Vulnerability Assessment Integration

- Add scanners and manage scans across systems with network connectivity.

## Log Exception SQL

### Log Exception SQL
Enables logging of SQL exceptions for all supported database platforms. May significantly increase log size. Access via Monitoring → Exception Logs. Related to SQL Exception Handling and Logging Mechanisms.

## Central Patch Management

### Central Patch Management
Manages patches across all supported Guardium versions. Requires verification of patch compatibility. View installation history under Patch Management → View History and schedule installations under Configuration → Schedule Installations. See Patch Management Practices, Patch History, and Installation Workflows.

## Datasource Connectivity

### Datasource Connectivity
Details not provided.

## Reporting

### Custom Domains
Allows creation of custom domains across all Guardium endpoints and generation of custom reports using the Report Wizard. No known limitations. Related to Entitlement Data Architecture and Report Builder.

## Application Operations

### Application Summary
Provides an overview of application setup prerequisites. Compliance and monitoring are considered post-installation. See Installation Guide and Prerequisite Checklist.

## Certificate Management

### Restore Guardium Insights Certificate
Restores a valid SSL certificate for Guardium Insights 3.3.x and later. Requires valid SSL certificate. See SSL Configuration and Guardium Insights Architecture.

## Module Management

### Centralized GIM Bundle View
Provides a centralized view of GIM bundles for all Guardium units running GIM 11.0.x or later. Requires SSH access to the central manager. See Guardium Installation Manager and GIM Configuration.

## Kerberos Authentication

### Kerberos Support
Supports Kerberos authentication for DataDirect JDBC driver 12.2.x or later and Microsoft JDBC driver 12.2.x or later. No known limitations. See Database Connection Configuration and Kerberos Overview.

## Authentication Methods

### Supported Authentication Methods
Supports local, LDAP, and Kerberos authentication for Guardium Data Protection 12.2.x and later, with limitations for certain modules. See User Authentication Framework and Guardium Security Settings.

## File Discovery and Classification

### View Scan Results
Displays scan results for File Discovery, Entitlement, and Classification (FDEC) modules with no limitations. See File Discovery Process and Classification Results.

## Threat Analytics

### Close Cases in Bulk
Allows bulk closure of active threat cases. Requires administrative privileges and administrative access to the Active Threat Analytics module. See Threat Analytics Workflow and Case Management.

## Policy Violation Reports

### Risky Users - Policy Violation
Generates reports for risky users with policy violations. Requires Risk Assessment feature enabled. See Risky Users Report and Policy Violation Detection.

## Reporting and Export

### Exporting a Report
Supports exporting any report type to PDF or CSV within Guardium Data Protection. Output format may be affected by file size. See Report Generation and PDF/CSV Export.

## Ad-Hoc Audit Processes

### Run Once Now Process
Executes audit processes immediately for all audit process types. Requires prior creation of an audit process. See Ad-Hoc Audit Processes and Audit Process Scheduling.

## System Management

### Central Management
- **Support Matrix:** Central Manager with multiple Managed Units
- **Limitations:** Central Manager must be version 12.0.x or later
- **Workflows:** Monitoring → Central Management, Reporting → Distributed → Create
- **Keywords:** Central Management, Distributed Reporting

## Security

### Assessment Execution
- **Support Matrix:** Any assessment type
- **Limitations:** None
- **Workflows:** Assessments → Run
- **Keywords:** Assessment Lifecycle, Result Retrieval

### File Ownership
- **Support Matrix:** Informix or Sybase databases
- **Limitations:** Requires Informix or Sybase module
- **Workflows:** Security → File Ownership
- **Keywords:** File Ownership, Informix, Sybase

### RBAC
- **Support Matrix:** All Guardium roles
- **Limitations:** Requires proper role definitions and user assignments
- **Workflows:** Configuration → User Role Assignment
- **Keywords:** Access Control, Identity Management

## Monitoring

### System Resources
- **Support Matrix:** Any Guardium appliance
- **Limitations:** Requires System Resources module
- **Workflows:** Monitoring → System Resources
- **Keywords:** System, Root, Disk, Usage

### Edge Gateways
- **Support Matrix:** Edge Gateway installations
- **Limitations:** Requires Edge Gateway module
- **Workflows:** Monitoring → Dashboards & Reports
- **Keywords:** Edge Gateway Performance, Dashboard Visualization

## Remote Operations

### Remote Logging
- **Support Matrix:** All Guardium appliances
- **Limitations:** Requires network connectivity to logging server
- **Workflows:** Administration → Loggers → Remote
- **Keywords:** Remote Logging Configuration, Syslog Setup

## Data Management

### Datasource Connectivity
- **Support Matrix:** SQL Server, Oracle, Db2, MySQL
- **Limitations:** Browser service must be running; z/OS not supported
- **Workflows:** Configuration → Add Datasource, Navigation → View Ports
- **Keywords:** Database Connection Architecture, Browser Service

### Data Archive
- **Support Matrix:** Guardium-supported databases
- **Workflows:** Configuration → Configure Data Archive
- **Keywords:** Audit Result Management

## Scheduler and Automation

### Scheduler Settings
- **Support Matrix:** Guardium Scheduler
- **Limitations:** Improper configuration may affect job execution timing
- **Workflows:** Administration → Scheduler Settings
- **Keywords:** Quartz Scheduler Parameters

## Scheduler Report

### Components
- Schedule jobs via the Administration interface or by API calls (GuardAPI Scheduler Syntax). Requires proper syntax knowledge for API interactions.

### Links
- Knowledge: Job Scheduling, Timing Constraints, API Reference, Job Management
- Keywords: Cron, Scheduling, GuardAPI, Scheduler Call

## Datasource Connectivity

### Amazon DynamoDB
- Supported from Guardium version 12.0. Configuration via the Configuration interface.

### Amazon Redshift
- Supported from Guardium version 12.0. Configuration via the Configuration interface.

### SSL Yes
- Default SSL method for datasources in Guardium version 12.0 and later.

### Name and Description
- Optional field in Guardium version 12.0 and later for scenario setup.

### Log Flat
- May increase storage usage in Guardium version 12.0 and later.

### Log Full Details
- Comprehensive logging may impact performance in Guardium version 12.0 and later.

### Adding Components
- Requires appropriate admin rights in Guardium version 12.0 and later.

### Enable IPv4
- No specific constraints in Guardium version 12.0 and later. Configuration via the Network Settings interface.

### Global Profile
- Changes apply to all users in Guardium version 12.0 and later.

### Run-Time Parameter Operator Default Value
- Fixed time period in Guardium version 12.0 and later. Configuration via the Parameter Setup interface.

m
  - **Limitations/Constraints:** Uses Db2 driver, security considerations
  - **Workflows with different types:** Configuration — Db2 for z/OS Setup
- **Links:**
  - **Knowledge:** Db2 for z/OS, Guardium, Configuration
  - **Keywords:** Db2, z/OS, Driver, Security, Guardium

## 3305. Case management  
Components: Support Matrix = Guardium; Limitations = None; Workflows = Case Management → View Cases, Handle Cases.  
Links: Knowledge = Case Management, Guardium, User Operations; Keywords = Case Management, View, Handle, Guardium.  

## 3306. Parse actions  
Components: Support Matrix = Guardium; Limitations = None; Workflows = Configuration → Parse Action Setup.  
Links: Knowledge = Parse Actions, Guardium, Data Interpretation; Keywords = Parse Actions, NO_PARSE, Configuration, Data Interpretation.  

## 3307. High level workflow for file activity monitoring  
Components: Support Matrix = Guardium; Limitations = None; Workflows = Workflow → File Activity Monitoring.  
Links: Knowledge = File Activity Monitoring, Guardium, GuardAPI; Keywords = File Activity Monitoring, Workflow, Guardium, GuardAPI.  

## 3308. Queries Running  
Components: Support Matrix = Guardium; Limitations = Threshold of 900 seconds; Workflows = Monitoring → Long Running Queries.  
Links: Knowledge = Query Monitoring, Guardium, Long Running Queries; Keywords = Queries Running, Long Running, Monitor, Threshold, 900 seconds.  

## 3309. Managing software with GIM  
Components: Support Matrix = Guardium; Limitations = None; Workflows = Configuration → Software Management.  
Links: Knowledge = GIM, Software Management, Guardium; Keywords = GIM, Software, Manage, Configuration.  

## Datasource Connectivity  

### Dynamic Port Detection  
Components: Support Matrix = SQL Server, Oracle, Db2, MySQL; Limitations = Requires browser service running; not supported on z/OS; Workflows = Configuration → Add Datasource; Navigation → View Ports.  
Links: Knowledge = Database Connection Architecture, Browser Service; Keywords = S‑TAP, Collector, JDBC, Browser Service.  

### CyberArk Integration  
Components: Support Matrix = All Guardium‑supported databases; Limitations = CyberArk SDK export restrictions in some regions; Workflows = Configuration → Install CyberArk SDK.  
Links: Knowledge = Credential Management, Dynamic Secrets; Keywords = CyberArk SDK, Credential Vault.  

## Compliance APIs  

### Data Compliance APIs  
Components: Support Matrix = Guardium platform; Limitations = None documented; Workflows = API Invocation → DataExport, DataMasking.  
Links: Knowledge = Guardium Data Protection Architecture, Data Classification; Keywords = DataExport, DataMasking, API, Compliance.  

## GuardAPI Syntax Reference  

### create_qr_replace_element_byId  
Components: Support Matrix = Guardium ≥ 11.0; Limitations = Requires Long‑type parameter qrActionId; Workflows = Configuration → Query Rewrite Setup.  
Links: Knowledge = Query Rewrite Configuration, GuardAPI Parameter Types; Keywords = qrActionId, replaceFrom, GuardAPI.  

### enable_disable_ip_restriction  
Components: Support Matrix = Guardium ≥ 10.6; Limitations = None; Workflows = Security → IP Restriction.  
Links: Knowledge = Access Control, Guardium Security Configuration; Keywords = IP Restriction, Guardium Login, Security Configuration.  

### grant_role_to_object_by_Name  
Components: Support Matrix = Guardium ≥ 9.5; Limitations = None; Workflows = Configuration → Role Management.  
Links: Knowledge = Role‑Based Access Control, Object Privileges; Keywords = Role, Object Name, Dependencies, GuardAPI.  

### update_insights_agent_config  
Components: Support Matrix = Guardium Insights ≥ 2.2; Limitations = None; Workflows = Management → Agent Configuration.  
Links: Knowledge = Guardium Insights Task Manager, Agent Parameters; Keywords = Insights, Agent, Configuration, GuardAPI.  

### update_utilization_thresholds  
Components: Support Matrix = Guardium ≥ 11.3; Limitations = None; Workflows = Management → Utilization Settings.  
Links: Knowledge = System Utilization Monitoring, Threshold Parameters; Keywords = Utilization Thresholds, GuardAPI, System Settings.  

### SOX DML Distribution  
Components: Support Matrix = Guardium ≥ 11.0; Limitations = Requires DML Distribution module; Workflows = Reporting → Compliance Tracking.  
Links: Knowledge = SOX Compliance, DML Monitoring, Client IP Activity; Keywords = SOX, DML, Client IP, Distribution, Compliance Module.  

### Data Mart Management APIs  
Components: Support Matrix = Guardium Data Marts module; Limitations = Requires data marts configured; Workflows = Configuration → Data Mart Setup, R… (truncated).  
Links: Knowledge = Data Mart Architecture; Keywords = Data Mart, Configuration, API.

## Reporting — Data Mart Queries
**Links:** Data Mart Architecture, Data Mart Management, Reporting APIs  
**Keywords:** Data Mart, Profile, Object Management, API, Reporting  

### GuardAPI: update_insights_agent_config
**Components:** Guardium Insights support  
**Keywords:** Insights Agent, Configuration, GuardAPI  

### GuardAPI: update_utilization_thresholds
**Components:** Guardium management  
**Keywords:** Utilization, Thresholds, GuardAPI  

### Internal Database Management
**Components:** Guardium Internal Database maintenance  
**Keywords:** Internal DB, Performance, Purging, Database  

### Db2 for i Configuration
**Components:** Db2 for i Guardium setup  
**Keywords:** Db2 for i, Guardium Datasource, Configuration  

### Policy ID Attribute
**Components:** Guardium Policy Management  
**Keywords:** Policy ID, Access Policy, Management  

### System Backup Configuration
**Components:** Guardium system backup  
**Keywords:** System Backup, Configuration, Guardium  

### Enterprise S-TAPs changedAlert
**Components:** Enterprise S-TAP monitoring  
**Keywords:** S-TAPs, changedAlert, Central Manager, Alert Management  

### BIG-IP ASM Integration
**Components:** BIG-IP Application Security Manager  
**Keywords:** BIG-IP, ASM, Communication, Integration  

### App. Server User Identification Parameter
**Components:** Guardium Application Server Configuration  
**Keywords:** App Server User, Identification, Parameter  

### GuardAPI: add_approved_stap_client
**Components:** Guardium 11.0+ Stap management  
**Parameters:** stapHost string  
**Keywords:** stapHost, S-TAP Management, GuardAPI  

### GuardAPI: change_tracker_get_params
**Components:** Guardium change tracking  
**Keywords:** Change Tracker, GuardAPI, Parameters  

### GuardAPI: configure_results_archive
**Components:** Guardium results archive  
**Keywords:** Results Archive, Configuration, GuardAPI  

---  

### GuardAPI Syntax: get_stap_tls_config
Retrieves S-TAP SSL settings using `get_stap_tls_config parameter=value`.  

### GuardAPI Command Reference  

**change_to_opensource**  
*Supports:* SQL Server, Oracle, Db2, MySQL  
*Requires:* microsoftDriverString  
*Keywords:* microsoftDriverString, JDBC, SQL Server ODBC, OpenSource Connector  

**delete_hashicorp_config**  
*Supports:* All Guardium databases  
*Keywords:* vault_config_name, API Deletion, Secrets Engine  

**migrate_stap_config**  
*Supports:* All S-TAP configs  
*Requires:* valid parameter=value pairs  
*Keywords:* S-TAP Migration, Config   (truncated)

## Configuration Management

### Update Classifier Rule
- **Components:** All classification rules
- **Constraints:** category and classification parameters required
- **Usage:** Analysis — Update Classification Rules
- **Keywords:** rule_id, category, classification, confidence_score

### Update Datasource Group
- **Components:** All datasource groups
- **Constraints:** None
- **Usage:** Configuration — Manage Datasource Groups
- **Keywords:** group_id, parameters, group_properties

## Datasource Connectivity

### Dynamic Port Detection
- **Supports:** SQL Server, Oracle, Db2, MySQL
- **Constraints:** Requires browser service; not supported on z/OS
- **Procedures:** Add Datasource; View Ports
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

### CyberArk Integration
- **Supports:** All Guardium-supported databases
- **Constraints:** Export restrictions in some regions
- **Procedures:** Install CyberArk SDK
- **Keywords:** CyberArk SDK, Credential Vault

## CyberArk Integration
Guardium's CyberArk integration supports all Guardium-protected databases, but CyberArk SDK export restrictions may apply in certain regions. Configuration involves installing the CyberArk SDK.

## Policy and Reporting

### Query Drilldown Control
Enabling query drilldown on any platform lets you navigate from a policy violation to the underlying query details.

## Collections Management

### Managing Object Audit in One Database
Object auditing can be configured per datasource after enabling object auditing at the database level.

## Datasource Connectivity

### Dynamic Port Detection
For SQL Server, Oracle, Db2, and MySQL, dynamic port detection works when the browser service is running (not supported on z/OS). Configuration is performed during datasource addition; view detected ports via the Ports page.

## Quality Gates
- Audit logging, traffic dropping, flow control, session monitoring
- **Keywords:** Audit Logging, Traffic Dropping, Flow Control, Session Monitoring

## Transform Actions
- Transform SQL requires the **Transform SQL** permission and is supported across all Guardium‑supported database platforms. Workflows involve creating a policy, adding a rule, selecting Transform, and defining a transformation set.
- **Keywords:** mask, hash, obfuscate, transform, policy, Guardium, SQL Guard

## Ignore SQL
- SQL statements are not stored in activity logs; only login/logout events remain logged. Configure via Configuration → Logging Settings → Log Filters → Ignore SQL.
- **Keywords:** ignore, log, sql, traffic, filter, guardium, SQL statements, logging

## Custom Module Integration
- Supported from Guardium V11.0 onward, modules must be signed and require a restart on upgrade. Install via Configuration → Admin → Manage Modules → Install → select .jar/.tar.
- **Keywords:** module, install, jar, tar, guardium, security, integration