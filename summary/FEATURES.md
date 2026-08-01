# Permissionstodynamicrolesandcredsfordifferentpaths — FEATURES

**Category:** features  |  **Generated:** 2026-07-09  |  **Source:** gdp-12.x-documentation.pdf

---

## Permissions for Dynamic Role and Credential Management

**Dynamic Permissions Management**
Guardium 12.x supports role and credential creation on Red Hat Enterprise Linux and Windows Server 2019. Database admin privileges are required; non-relational databases are not supported. Use the Configuration workflow to create roles and the Workflow to grant credentials.

**Hierarchical Path-Based Role Assignment**
Available on all Guardium appliances with Guardium 12.1 and later for HDFS and Active Directory. Supports role hierarchies up to 4 levels. Hierarchies deeper than 4 levels or on legacy systems are not supported. Use the Configuration workflow to assign path roles and the Workflow to validate assignments.

---

## Data Source Connectivity

**Custom URL Connection**
Supported on all Guardium data sources, this feature overrides standard hostname/port settings. Required fallback parameters include hostname and port when omitted. Configure through the Datasource Edit or Add Datasource navigation.

**Amazon ECS Archive Support**
Requires Guardium 12.0 and S3-compatible storage. Configured via the Archive Configuration workflow. Use for data backup and protection with S3 storage.

**Connection Property Formatting**
Applicable to all data source types for custom property configuration. Properties follow JDBC syntax with semicolons separating entries. Configure through the Data Source Properties workflow.

**Data Source Application View**
Allows filtering data sources by application type in all Guardium versions. Use the Data Source Application Filter workflow to manage visibility.

---

## Guardium Feature Reference

**Dynamic Datasource Connectivity with CyberArk Vault**
Supported on all Guardium-supported databases. Optional standby vault required for high availability. Configure through the configuration workflows for primary and standby vault settings.

---

### Windows S-TAP Advanced Configuration
Requires OS administrator privileges for installing Windows S-TAP. Specific parameters affect network drivers and debugging. Configure through the Windows S-TAP configuration workflows.

## Guardium Advanced Security Features

### Attack Detection and Incident Management
- **Support Matrix:** All supported Guardium versions
- **Configuration Requirements:** Policy definition for each feature
- **Key Workflows:** Policy creation, quarantine management
- **Associated Knowledge:** Credential stuffing, quarantine process, query rewrite
- **Relevant Keywords:** S-TAP, Collector, Policy Builder, Incident Manager

### Portal Redesign
- **Support Matrix:** Guardium 12.0 and later
- **Deprecation Note:** Legacy portal page may be removed in future releases
- **Key Workflows:** Portal settings configuration, navigation tree usage
- **Associated Knowledge:** Portal design, authentication methods, multi-factor authentication
- **Relevant Keywords:** Guardium Portal, Legacy Portal, Navigation Tree, SSO

### Report Creation and Fields
- **Support Matrix:** All Guardium versions supporting reporting
- **Feature Constraint:** Field types vary by datasource
- **Key Workflows:** Report definition, report builder navigation
- **Associated Knowledge:** Report formats, field scope, conditions
- **Relevant Keywords:** Report Templates, Conditional Formatting, Data Aggregation

### Cost Analysis in Guardium
- **Support Matrix:** Guardium versions with cost analysis module
- **Configuration Note:** Units may require admin configuration
- **Key Workflows:** Cost dashboard navigation, unit settings configuration
- **Associated Knowledge:** Business value metrics, data governance
- **Relevant Keywords:** Cost Analysis, Executive Dashboard, Financial Metrics

### Apache Cassandra Datasource Configuration
- **Support Matrix:** Guardium 11.3 and later with Apache Cassandra datasources
- **Path Note:** Path may vary by installation
- **Key Workflows:** Datasource addition, connectivity troubleshooting
- **Associated Knowledge:** Configuration files, JCA, alternatives
- **Relevant Keywords:** Apache Cassandra, Datasource Settings, $cs\_home, Troubleshooting

### Informix SSL Support
- **Support Matrix:** Informix datasources with SSL enabled
- **Configuration Note:** Mutual SSL authentication not supported
- **Key Workflows:** SSL settings configuration, Informix properties navigation
- **Associated Knowledge:** SSL protocols, host name/IP configuration
- **Relevant Keywords:** Informix, SSL, Host Name/IP, Mutual Authentication

### AWS Secrets Manager Integration (continued)
- **Support Matrix:** Guardium 11.4 and later
- **Feature Constraint:**  (truncated)

## Guardium SQL Audit Configuration

### SQL Command Selection for Auditing

- **Support Matrix:** Al Guardium-supported SQL databases
- **Limitations/Constraints:** None
- **Workflows with different types:** Configuration — SQL Audit Setup
- **Knowledge:** Auditing Fundamentals, SQL Command Matrices
- **Keywords:** insert, update, delete, audit policy, Guardium UI

## Restricted Guardium API User Roles

### Guardium API Role-Based Access Control

- **Support Matrix:** All Guardium installations
- **Limitations/Constraints:** Requires API version 11.3 or later
- **Workflows with different types:** Security — User Role Configuration
- **Knowledge:** API Security, Role Management
- **Keywords:** restricted_access, API_user, UI_blocking

## AWS Secrets Manager Integration

### IAM Authentication for Secrets Management in Guardium

- **Support Matrix:** Amazon RDS, Aurora, Redshift
- **Limitations/Constraints:** Requires IAM role with secretsmanager:GetSecretValue permission
- **Workflows with different types:** Configuration — IAM Secrets Setup
- **Knowledge:** AWS IAM, Secrets Manager Architecture
- **Keywords:** IAM_role, secretsmanager, alternate_ARN

## Cloud Database Activity Monitoring

### Cloud Data Activity Monitoring and Discovery

- **Support Matrix:** AWS RDS, Azure SQL Database, Google Cloud SQL
- **Limitations/Constraints:** Monitoring agents require VPC connectivity
- **Workflows with different types:** Discovery — Cloud Data Activity Scan
- **Knowledge:** Cloud Data Security, Data Discovery Techniques
- **Keywords:** cloud_monitoring, activity_streams, schedule_running

## Advanced Data Security Policy in Guardium

### Enhanced Threat Detection Policies

- **Support Matrix:** All Guardium versions 11.5 and later
- **Limitations/Constraints:** Policy configuration requires Advanced Data Security license
- **Workflows with different types:** Configuration — Threat Policy Setup
- **Knowledge:** Threat Management, Modern Security Analytics
- **Keywords:** ADSP, threat_detection, user_interface

## Scheduled Database Discovery in Guardium

### On-Demand vs. Scheduled Discovery Workflows

- **Support Matrix:** All supported on-premises and cloud databases
- **Limitations/Constraints:** Scheduling requires scheduler service enabled
- **Workflows with different types:** Automated — Scheduled Discovery
- **Knowledge:** Discovery Engine, Scheduling Mechanisms
- **Keywords:** discovery_processes, on_demand, automation_scheduling

## Vulnerability Assessment Reporting

### Report Chart Types and Integration Guides

- **Support Matrix:** All Guardium-supported databases and operating systems
- **Limitations/Constraints:** None
- **Workflows with different types:** Reporting — VA Result Analysis
- **Knowledge:** Reporting Tools, Vulnerability Scoring Standards
- **Keywords:** chart_types, VA_reports, S-TAP_zOS

## S-TAP Agent Release Notes

### Release Notes for S-TAP and Related Agents

- **Support Matrix:** Linux-UNIX S-TAP, GIM, CAS
- **Limitations/Constraints:** URLs may change with new versions
- **Workflows with different types:** Configuration — Agent Update
- **Knowledge:** Release Management, Agent Configuration
- **Keywords:** S-TAP_release, GIM_updates, CAS_agents

## Guardium Policy Framework

### Database Activity Monitoring Policies

- **Support Matrix:** All Guardium-supported databases
- **Limitations/Constraints:** Policy rules must be carefully crafted to avoid performance impact
- **Workflows with different types:** Configuration — Policy Rule Setup
- **Knowledge:** Policy Architecture, Data Activity Control
- **Keywords:** policy_rules, condition_actions, database_monitoring

# Datasource Connectivity

## Kerberos Ticket Encryption Types
- **Support Matrix:** AES256-CTS-HMAC-SHA1-96  
- **Configuration:** Set Encryption Type  

## Agent Deployment and Compliance Monitoring
- **Support Matrix:** All Guardium platforms  
- **Limitations:** Administrator privileges required for deployment; limited to configured databases for compliance monitoring  
- **Workflows:** Deploy Agents → Open Compliance Summary  

## Environment Management and Data Discovery
- **Support Matrix:** Guardium versions supporting S-TAP  
- **Limitations:** Requires periodic system scans for data discovery  
- **Workflows:** Manage S-TAP Health → Data Classification  

## Central Management Approaches
- **Support Matrix:** Central Manager and Managed

## Security, Compliance, and Automation

### Units
**Limitations/Constraints:** Central Management server requires stable network access to managed units.  
**Workflows:** Administration – Manage Certificates; Navigation – View Deployment Health.  
**Links:** Central Management Architecture, Deployment Health Monitoring; GuardAPI Certificate Commands.

### Secure Audit Repository and Compliance Automation
**Components:** All Guardium appliances.  
**Limitations/Constraints:** External repository requires compatible database engine.  
**Workflows:** Configuration – Set Up Audit Repository; Automation – Schedule Report Distribution.  
**Links:** Audit Repository Integration, Automated Audit Processes; Automated Auditing, Report Distribution Automation.

### HashiCorp Vault Integration for Password Management
**Components:** Guardium datasources compatible with JDBC.  
**Limitations/Constraints:** Vault policies must allow automated password retrieval.  
**Workflows:** Configuration – Add Datasource to Vault; Configuration – Edit Datasource Properties.  
**Links:** HashiCorp Vault Integration, Automatic Credential Provisioning; Password Provisioning, JDBC Datasource Configuration.

### Policy and Rule Configuration for Outlier Detection
**Components:** All Guardium policy engines.  
**Limitations/Constraints:** Outlier detection effectiveness depends on properly grouped users and objects.  
**Workflows:** Configuration – Create User Groups; Configuration – Set Trust Evaluators; Navigation – Policy Management.  
**Links:** Policy Management, Outlier Detection Techniques; User Groups, Trust Evaluators, Outlier Detection, Policy Configuration.

### JDBC Connection Property Syntax
**Components:** All JDBC-compatible datasources in Guardium.  
**Limitations/Constraints:** Incorrect property format causes connection failures.  
**Workflows:** Configuration – Create JDBC Datasource; Testing – Test Connection.  
**Links:** JDBC Connection Properties, Datasource Connectivity; Property Formatting.

### Managing Log Rotation Settings
**Components:** Log management across all Guardium components.  
**Limitations/Constraints:** Minimum log count is 1; maximum is system-dependent.  
**Workflows:** Configuration – Set Log Rotation Count; Maintenance – View Log Files.  
**Links:** Log Rotation Principles, Guardium Maintenance Operations; Log Files Maintenance, Guardium Log Management.

### GuardAPI Function for User Hierarchy Creation
**Components:** All Guardium versions supporting GuardAPI.  
**Limitations/Constraints:** API access requires proper permissions; hierarchy structure must follow Guardium's organizational model.  
**Workflows:** Automation – Execute create_user_hierarchy; Verification – Check User Hierarchy.  
**Links:** GuardAPI Capability, User Hierarchy Management; User Hierarchy Automation.

## Vulnerability Assessment and Management

### VA Scanner Polling Feature
**Components:** All supported Guardium platforms.  
**Limitations/Constraints:** Requires valid ScanPlan configuration; no effect if no ScanJobs exist.  
**Workflows:** Configuration – Set Polling Interval.  
**Links:** CrashLoopBackOff Troubleshooting, VA Scanner Configuration; VA Scanner, Polling.

### Helm Package Generation
**Components:** Helm 3.x and later.  
**Limitations/Constraints:** Requires Chart.yaml with valid version field.  
**Workflows:** Packaging – Generate Helm Chart.  
**Links:** Helm Package Structure, Chart.yaml Fields; releases directory, .tgz.

### SSH API Execution Workflow
**Components:** Guardium CLI enabled systems.  
**Limitations/Constraints:** API call syntax must follow Guardium standards.  
**Workflows:** Administration – Execute API via SSH.  
**Links:** Guardium CLI User Guide, grdapi Command Reference; grdapi, create_user_hierarchy, SSH, Guardium CLI.

### Certificate SAN Inspection
**Components:** All Guardium systems with OpenSSL installed.  
**Limitations/Constraints:** Requires access to server certificate.  
**Workflows:** Security – Inspect Cert SAN.  
**Links:** OpenSSL Command Options, TLS Certificate Components; SAN, Certificate, OpenSSL, Server.

### Create User Hierarchy API
**Components:** Guardium v12.0+.  
**Limitations/Constraints:** Parent and child users must exist beforehand.  
**Workflows:** Administration – Manage User Hierarchy.  
**Links:** Guardium User Model, Hierarchy Concepts; GuardAPI, create_user_hierarchy, userName, parentUserName.

### Support Execute Command Functions
**Components:** All Guardium physical and virtual appliances.  
**Limitations/Constraints:** Requires root privileges for certain commands.  
**Workflows:** Administration – Run Diagnostics.  
**Links:** Guardium Support Execute Catalog, System Commands; version, ens32, root.

## Data Protection and System Management

### Password Expiration Policies
- **Components:** GUI, CLI, GuardCLI users
- **Limitations:** Must validate current password before changing; disabled users cannot change passwords
- **Workflows:** Security Management — Update User Password
- **Links:** User Account Management, Password Security
- **Keywords:** Password Expiration, Validation, Security Levels, GuardCLI

## CAS Templates

### Create CAS Template
**Support:** Guardium V9.5 or later  
**Restrictions:** None  
**Workflows:** `create_cas_template` (Command), POST /services/data/v1/CreateCAS (REST)  
**Related Topics:** CAS Architecture, GuardAPI, REST API  

### Delete CAS Template
**Support:** All Guardium-supported versions  
**Restrictions:** Requires proper API permissions  
**Workflows:** `delete_cas_template` (Command), DELETE /services/data/v1/DeleteCAS (REST)  
**Related Topics:** CAS Management, RESTful Services  

### Add Predefined Data Mart to Profile
**Support:** All current Guardium versions  
**Restrictions:** Profile must exist  
**Workflows:** Add Data Mart to Profile (API)  
**Related Topics:** Data Mart Configuration, API Management  

### Oracle SQL Commands Report
**Support:** Oracle databases  
**Restrictions:** Requires database access  
**Workflows:** Oracle SQL Commands (Report Generation)  
**Related Topics:** SQL Command Analysis, Report Customization  

### Delete Results Archive Configuration
**Support:** Guardium version with API  
**Restrictions:** Results archive must exist  
**Workflows:** `delete_results_archive_configuration` (API)  
**Related Topics:** Results Archiving, API Configuration  

### Create Role
**Support:** Guardium V10.1.4 or later  
**Restrictions:** Central manager required for role creation across units  
**Workflows:** `create_role` (GuardAPI)  
**Related Topics:** Role Management, Access Control  

### Get Solr Status
**Support:** Guardium 10.6 and later  
**Restrictions:** Solr must be installed  
**Workflows:** `get_solr_status` (Command)  
**Related Topics:** Solr Integration, System Status  

### Create API Parameter Mapping
**Support:** Guardium APIs  
**Restrictions:** Correct parameter names and labels required  
**Workflows:** `create_api_parameter_mapping` (GuardAPI)  
**Related Topics:** API Parameter Mapping, Report Results  

### Central Management GUI Version Display
**Support:** Central Management GUI enabled  
**Restrictions:** Post-upgrade refresh required  
**Workflows:** Refresh Version Display (GUI Management)  
**Related Topics:** Version Management, Central Management  

--- 

## Oracle Configuration

## Verify API Key Exists: `78e96f7f-bd96-4816-bfd2-68f8f0d114b8`
- **Components:** REST API, CLI  
- **Support:** Requires API key authentication, not available in legacy versions  
- **Workflows:** Verify API Key, Monitor API Health  
- **Knowledge:** API Security, OAuth  
- **Keywords:** API Key, REST Endpoint, Authentication, Health Check  

## Verify API Key Exists: `9b1081d7-85b3-4e0c-8bbc-5ee822298f1e`
- **Components:** Windows S-TAP, Linux S-TAP, z/OS S-TAP  
- **Support:** Requires correct license, not for virtual appliances  
- **Workflows:** Install GIM Parameters, Verify License  
- **Knowledge:** GIM Setup, License Management  
- **Keywords:** GIM Parameters, License Validation, S-TAP Installation  

## S-TAP Load Balancing Modes
- **Support:** All Guardium S-TAP versions  
- **Workflows:** Configure Load Balancing, Monitor Resource Utilization  
- **Knowledge:** Load Distribution, Managed Units, Resource Management  
- **Keywords:** S-TAP, Load Balancing, Managed Units, Traffic Distribution  

## Audit Logging Configuration for DataStax Cassandra
- **Support:** DataStax Cassandra  
- **Workflows:** Configure Audit, View Audit Logs  
- **Knowledge:** Cassandra Configuration, Logging Formalities  
- **Keywords:** audit_logging, logback.xml, audit_logs  

## Ingress Annotations for Remote Logging with Rsyslog
- **Support:** Rsyslog  
- **Workflows:** Configure Remote Logging, Troubleshoot Log Delivery  
- **Knowledge:** Rsyslog Configuration, Remote Loggers  
- **Keywords:** remotelog, rsyslog, remote_logging  

## S-TAP Network Latency Monitoring (Guardium 11.0)
- **Support:** Guardium S-TAP 11.0  
- **Workflows:** Configure Latency Monitoring, Monitor Database Performance  
- **Knowledge:** Network Performance, S-TAP Monitoring  
- **Keywords:** stap_network_latency, network_latency, S-TAP_monitoring  

## Disable Outliers Detection API (Guardium Central Manager 12.5)
- **Support:** Guardium Central Manager 12.5  
- **Workflows:** Configure Outliers Detection, Automate API Actions  
- **Knowledge:** Guardium API, Outliers Detection  
- **Keywords:** disable_outliers_detection, cross_central_manager  

## Weekly System Update Summary
- **Support:** Guardium UI  
- **Workflows:** Enable What's New Tab, View System Changes  
- **Knowledge:** System Updates, Weekly Reports  
- **Keywords:** whats_new_tab, system_updates, weekly_summary  

## Query Rewrite Feature (Fine-Grained Access Control Databases)
- **Workflows:** Configure Query Rules, Monitor Database Access  
- **Knowledge:** Access Control, Query Filtering  
- **Keywords:** query_rewrite, fine_grained_access, security_policy  

## Massive Grant Attack Detection (Guardium UEBA 11.0)
- **Support:** Guardium UEBA 11.0  
- **Workflows:** Detect Privilege Abuse, Analyze Behavior Anomalies  
- **Knowledge:** Privilege Management, User Behavior Analysis  
- **Keywords:** massive_grant, privilege_abuse, user_behavior  

## Query Pattern Deviation Detection (Guardium UEBA 11.0)
- **Support:** Guardium UEBA 11.0  
- **Workflows:** Detect Query Anomalies, Generate Security Alerts  
- **Knowledge:** Query Analysis, Unusual Activities  
- **Keywords:** query_pattern, user_query_patterns

## Security Policy Creation
Components include a support matrix for all Guardium policy types, limitations requiring rules to include "Any Field" or "Any User," and distinct workflows for configuration and monitoring. Relevant links cover Guardium Policies and Traffic Monitoring, with keywords such as `security_policy`, `policy_rules`, and `traffic_monitoring`.

## Special Handling for TRANSFORM Actions
### Oracle
Supports SQL Server, Oracle, Db2, MySQL, and PostgreSQL with size limits for transformed payloads (maximum 16 KB). Workflows cover configuration, monitoring, threat prevention, and data obfuscation (SQL Injection Prevention).

### Performance Optimization
Applies to all supported relational databases, limiting one tuple per rule with policy-level aggregation. Workflows include setup, validation, and performance tuning (adjusting Maximum Group Size).

### Authentication Management
Works across Oracle, MySQL, and SQL Server databases with thresholds above zero and a minimum of five valid connections. Workflows cover detection, investigation, and response (enforcing Legacy Protocols).

### Login Auditing
Applies to Windows Server, Linux, Unix, and mainframe platforms without specific limitations. Workflows involve rule creation, reporting, and policy adjustment (refining Brute-Force Thresholds).

### File Access Control
For file servers with monitoring capabilities, rules must include file attributes (e.g., read/write). Workflows cover policy creation, compliance checks, and audit effectiveness.

### Dashboard Customization
Applicable to investigation dashboards with filtering capabilities. Workflows include dashboard customization, data filtering, and user interaction (hover for filter details).

### Violation Reporting
Works with any reporting tool capable of detailed view generation. Workflows include violation reporting, investigation, and reporting (exporting detailed violations).

### SQL Query Logging
Applicable to any SQL-capable database environment, requiring logging of both original and modified SQL strings. Workflows cover logging, analysis, and mitigation (adjusting security controls).

## Query and Report Management
### Oracle SQL Query Examples
Applies to Oracle databases, detailing workflows for querying and report building using the Query-Report Builder.

### Data Governance and Security
Applies to Guardium with unspecified limitations, requiring admin access for data governance and security tasks.

## Configuration Management

### CAS Template Management
- **Support Matrix:** Guardium 11.3+  
- **Constraints:** DBA privileges required for template creation  
- **Workflows:** Administration → Template Creation; Security Management → Configuration Audit  
- **Keywords:** CAS Template Set, Apply Configuration, DBA Permissions, Template Items

## Access Control

### Application Role Management
- **Support Matrix:** Oracle, DB2, SQL Server  
- **Constraints:** Requires role‑based access configuration  
- **Workflows:** Security Management → Role Assignment; Administration → User Permissions  
- **Keywords:** Application Access, Role Browser, Manage Permissions, Configuration Changes

## Cluster Setup

### Registry Certificate Installation
- **Support Matrix:** Linux clusters  
- **Constraints:** Root access needed for certificate management  
- **Workflows:** Installation → Certificates; Maintenance → Cluster Configuration  
- **Keywords:** Registry Certificate, Cluster Nodes, Root Access, Cluster Configuration

## Patch Management System

### Managed Unit Patch Application
Applies patches to Guardium units from version 11.3 onward. Requires admin privileges; patches are unit-specific. Workflows include patch retrieval, application, and verification.

**Support:** Guardium Patch Lifecycle, System Compatibility, Upgrade Procedures  
**Keywords:** Managed Unit, Patch Application, System Upgrade, Automated Deployment

## PDF Generator Configuration

### Multilanguage Support Settings
Enables multilingual PDF output in English, Chinese, and Japanese. Multilanguage flag must be enabled globally. Includes font adjustment workflows.

**Support:** Language Localization, Font Management, PDF Configuration  
**Keywords:** PDF Generator, Multilanguage, Language Pack, Font Support

## Hadoop Service Monitoring

### Ambari-Managed Hadoop Configuration
Monitors Ambari-managed Hadoop clusters. Supports Ambari 2.6 to 3.1. Configuration requires cluster credentials and open port 8080.

**Support:** Ambari Configuration, Hadoop Monitoring, Guardium-Hadoop Integration  
**Keywords:** Ambari, Hadoop Service, Cluster Name, Monitoring Configuration

## Archive Data Transfer

### Secure Archive Protocol Configuration
Transfers archives securely using SCP or SFTP. Requires valid target credentials and open port 22.

**Support:** Secure File Transfer, Archive Protocols, SCP Configuration, SFTP Setup  
**Keywords:** Archive Protocol, SCP Transfer, SFTP Port, Archive Server

## Cold Data Streaming

### Long-Term Data Storage Configuration
Configures cold data storage in S3, Azure Blob, and Google Cloud Storage. Requires pre-created buckets and aligned IAM permissions.

**Support:** Cold Storage Solutions, Data Streaming Protocols, Cloud Storage Integration  
**Keywords:** DataMart, Cold Storage, StorageClass, Streaming API, Object Storage

## Classification Rule Creation

### Custom Classification Rules API
Creates custom classification rules in Guardium versions 11.0 to 12.0. Includes optional confidence score setup and rule validation.

**Support:** Data Classification, Rule Engine, API Configuration  
**Keywords:** Classifier Rule, Rule Category, Rule Type, Confidence Calculation

## Data Mart Transfer Methods

### Secure Data Transfer Techniques
Transfers data mart data using SSH key support. Requires SSH key installation and enabled transfer protocols.

**Support:** Data Transfer Protocols, Secure Copy, SSH Key Management  
**Keywords:** Datamart Copy, SSH Key, Data Transfer, Archive Settings

## Commands and Workflows

### Execute Flat Log Process
Executes flat log process in Guardium. Requires `api_target_host` parameter.

**Support:** Flat Log Analysis, GuardAPI  
**Keywords:** Guardium, Flat Log, Process, Execute

## Configuration for Client Web Certificates

### Host Discovery
Discovers hosts for client web certificates in any Guardium version. Requires ports 80 and 443; supports `Skip host discovery` behavior.

**Support:** Guardium Compatibility  
**Keywords:** Host Discovery, Ports, Configuration, Skip Discovery

## Guardium Configuration and Management

### User Risk Management
Effective after the next Risk Spotter execution, all Guardium versions support a process that categorizes user risk using a Support Matrix, with Limitations/Constraints detailed in User Management workflows.

### Oracle TAP Setup
All supported Oracle versions require the FAMMONITOR_USE_TLS parameter in the [TAP] section of guard_tap.ini to control TLS usage during configuration.

### Dashboard Customization
All Guardium-supported dashboard versions allow node-based customization, but missing node types like ERROR_5 affect data display.

### CPU Utilization Monitoring
Supported Guardium versions can experience high CPU usage from non-sniffer processes; direct observation of sniffer restarts is recommended for accurate monitoring.

### User Hierarchy Setup
Guardium's User Management API supports hierarchical user configuration, requiring appropriate permissions for role assignment and hierarchy establishment.

# Guardium Configuration

### Optional Ingress Annotations (Guardium 12.x, 11.5)
- Requires system admin role.
- Does not apply to cloud-native installations.

### Optional Ingress Annotations (Guardium 11.4, 12.0)
- TCP/IP port must not be in use by other services.
- Reserved ports (e.g., 443, 8443) cannot be used.

### Optional Ingress Annotations (Guardium V10.6 and later)
- Log size settings affect system performance.
- Defaults may be insufficient for high-volume deployments.

### Export MIGRATION Files (Guardium 11.0 and later)
- Export files cannot be imported into a newer major version without intermediate upgrades.

### GuardAPI Functions for Data Sources (All versions supporting REST API)
- API keys required for authentication.

```markdown
## Threat Detection Enhancements

### Enhanced SQL and OS Attack Detection
- **Support Matrix:** All supported Guardium database platforms, versions 12.2.1 and later
- **Workflows:** Configure Advanced Threat Detection; Review Enhanced Threat Reports
- **Knowledge:** XSS Prevention, OS Command Injection Mitigation, SQL Injection Countermeasures, DoS Protection
- **Keywords:** XSS, OS Command Injection, SQL Injection, DoS, Guardium 12.2.1, Vulnerability Scanning, Policy Enforcement, Threat Analytics

---

## Policy Rule Configuration and Management

### Configure for Client Web Certificates
- **Support Matrix:** Guardium collector units
- **Limitations:** Requires provisioned web certificate infrastructure
- **Workflows:** Install Client Certificates; Validate Certificate Trust
- **Knowledge:** Certificate Authority Management, Secure Session Handling
- **Keywords:** SSL, TLS, Client Authentication, Certificate Chain, Guardium Collector, HTTPS, Session Initialization

### Use of Conditional Statements in Policy Rules
```

## Special Guardium Application Handling

## Special Guardium Application Handling

### Batch SQL Statement Processing
- **Support Matrix:** MS-SQL, Sybase databases
- **Limitations/Constraints:** Only last statement status reported for batch
- **Workflows:** Review Last Statement Status, Adjust Batch Processing
- **Knowledge:** Batch SQL Error Handling, Unified Status Reporting
- **Keywords:** MS-SQL, Sybase, Last Statement, Error Reporting

### Unauthorized Access Attempt Detection
- **Support Matrix:** All Guardium-supported database platforms
- **Limitations/Constraints:** Requires baseline password uniqueness audit
- **Workflows:** Detect Shared Passwords, Enforce Unique Passwords
- **Knowledge:** Shared Credentials Risks, Password Security Policies
- **Keywords:** Shared Passwords, Credential Breach, Unique Authentication

### SharePoint File Activity Monitoring
- **Support Matrix:** Guardium with SharePoint monitoring agent
- **Limitations/Constraints:** Requires File Activity Monitoring (FAM) components
- **Workflows:** Configure Policy for FAM, Review File Activity Reports
- **Knowledge:** SharePoint Integration, File Activity Monitoring Techniques
- **Keywords:** SharePoint FAM, Monitoring Agent, File Activity Reports

### Database Reconciliation Support
- **Support Matrix:** MySQL, PostgreSQL, Oracle, SQL Server, Db2, MongoDB
- **Limitations/Constraints:** None
- **Workflows:** Synchronize Database Assets, Reconciliation Validation
- **Knowledge:** Database Synchronization Techniques, Cross-Platform Data Consistency
- **Keywords:** Asset Reconciliation, Database Platforms, Data Consistency

### Supported Database List for Reconciliation
- **Support Matrix:** MySQL, PostgreSQL, Oracle, SQL Server, Db2, MongoDB
- **Limitations/Constraints:** None
- **Workflows:** Select Supported Databases, Confirm Database Integration
- **Knowledge:** Reconciliation Framework, Cross-Database Support
- **Keywords:** Reconciliation, Supported Databases, Platform Support

## User Hierarchy Management

### Create User Hierarchy
- **Support Matrix:** Guardium API
- **Limitations/Constraints:** Parent user must exist; hierarchical depth limited
- **Workflows:** Manage access control hierarchy
- **Knowledge:** User Management, Role-Based Access Control
- **Keywords:** userName, parentU, role inheritance, delegation workflow

## Links

### Federated Guardium Environments with CAS

### Verify API Key Exists

### Verify API Key Status

### Configure Secure Boot Signing

### Oracle A-TAP SSL Setup

### Monitor Large Data Bypasses

## External S-TAP Configuration

### Volume Tab Parameters

### Guardium Tab Parameters

### Ingress Annotations

## Guardium License Management

### License Key Feature Enablement

## Data Source Connectivity

### Disable Quick Search API

## Guardium Features Reference

**Oracle Uid Chain Tracking**
- Support Matrix: Unix S-TAP (Kernel-mode TAP)
- Limitations: Varies by OS; example for AIX
- Workflow: Auditing — Track OS User Changes
- Knowledge: OS User Activity, Privilege Escalation Monitoring
- Keywords: Uid Chain, Kernel-mode TAP, su, AIX

**Encrypted Traffic Session Attributes**
- Support Matrix: All Guardium-supported databases
- Limitations: None
- Workflow: Monitoring — Encrypted Session Analysis
- Knowledge: Encrypted Communications, Session Analysis

## Guardium Vulnerability Assessment Automation

### ServiceNow Ticket Generation
- **Components:** Guardium VA 11.x, ServiceNow Orlando
- **Limitations/Constraints:** API token required, max severity level 3
- **Workflows:** Create Assessment → Activate → Severity Threshold; VA → Notification → ServiceNow Ticket
- **Keywords:** Guardium VA, ServiceNow Token, Severity Levels, Incident Creation

## Guardium Platform Management

### 365. Ingress Annotations
- **Keywords:** Ingress Annotation, Guardium Entity

### 366. Analyzer Logging
- **Keywords:** Analyzer, GDM_FLAT_LOG, Circular Queue

### 367. CLI Command Monitoring
- **Keywords:** Change Tracker, Quartz Thread, CLI

### 368. Syslog TCP Configuration
- **Keywords:** TCP Protocol, Syslog, Guardium GUI

### 369. Support Must_Gather
- **Keywords:** Support Must_Gather, Diagnostic Information

### 370. GuardAPI Functions
- **Keywords:** GuardAPI, Functions, Security Components

### 371. Create Assessment Command
- **Keywords:** Create Assessment, POST Method, Security Assessment

### 372. Create Role API
- **Keywords:** Create Role, RoleName Parameter, API Workflow

## Create Test Detail Exception

All Guardium-supported databases; requires API access; used in Security Testing workflows. Knowledge: Security Testing; GuardAPI REST Service. Keywords: API Version, Security Testing.

## Populate Group From Query

Guardium API; requires read access; used in Populate Group workflow. Knowledge: REST API; Group Management. Keywords: API, PUT request, group, query.

## API Target Host Specification

All Guardium API commands or workflows; none specific; used in Host Management and API Commands workflows. Knowledge: Host Management; API Parameters. Keywords: all, api_target_host, units, central manager.

## Certificate Signing Request Generation

TLS Configuration Workflow; requires certificate authority access; used in TLS Certificates workflow. Knowledge: TLS Authentication; CSR Generation. Keywords: TLS, CSR, client certificate, security.

## Auditing Data Stream Management

Guardium Auditing Workflow; none specific; used in Auditing Setup workflow. Knowledge: Data Auditing; AWS IAM; Data Management. Keywords: Auditing, AWS, IAM policies, data streams.

## Unused Entitlements Management

Compliance and Security Workflows; requires regular review; used in Compliance Monitoring workflow. Knowledge: Entitlement Management; Compliance Trends. Keywords: Unused entitlements, compliance, security, anomalies.

## Risk Spotter Policy for Dynamic Auditing

Guardium Risk Management Workflow; requires Risk Spotter installation; used in Risk Spotter Setup workflow. Knowledge: Risk Management; Dynamic Auditing. Keywords: Risk Spotter, Dynamic Auditing, policy installation.

## Selective Audit Trail Policy Configuration

Guardium Audit Policy Configuration; may increase storage; used in Audit Policy Setup workflow. Knowledge: Audit Trails; Data Compliance. Keywords: Audit trail, selective audit, data processing, storage.

## Session-Level Policy Management

Guardium Policy Building Tools; requires appropriate permissions; used in Policy Building workflow. Knowledge: Policy Management; Session-Level Policies. Keywords: Policy Builder, session-level policies, configuration.

## Criterion Configuration for Wildcards and Regular Expressions

Guardium Data Filtering; restricts groups/tuples; supports only = operator; used in Data Filtering Setup workflow. Knowledge: Data Filtering; Regular Expressions. Keywords: Criterion, wildcards, regular expressions, data filtering.

## Special Handling for TRANSFORM Actions

All Guardium-supported databases; TLS 1.3 not supported on Solaris; requires DBA privileges; used in Transform Rule Setup workflow. Knowledge: Sniffer Overload; High Availability. Keywords: TRANSFORM, S-GATE, Traffic Shaping, Guardium Sniffer.

## Special Handling for TRANSFORM in Oracle

Oracle 11gR2 and later; no support for EDITIONS; use DESCRIBE; used in Oracle Transform Setup workflow. Knowledge: Oracle DBMS_METADATA; Guardium Transformation Engine. Keywords: Oracle DBA, Transform, DESCRIBE, Auditing.

## Replay Result Tracking

Guardium versions 11.3 and above; requires replay feature enabled. Knowledge: Replay; Performance Monitoring. Keywords: Replay, Audit Results, Tracking.

```markdown
## Guardium Policy Export

### XACML Export Feature
- **Support Matrix:** Guardium 11.2 onwards
- **Limitations/Constraints:** Prior version policies cannot be imported back into Guardium
- **Workflows:** Export — Export Policies to XACML
- **Knowledge:** XACML Policy Management, Export Process
- **Keywords:** XACML, Export, Policies, Mapping

---

## Oracle Connection Manager

### Access Control and Proxying
- **Support Matrix:** Linux (separate installation)
- **Workflows:** Configuration — Install OCM; Administration — Manage Access Control
- **Knowledge:** Proxy Servers, Oracle Architecture
- **Keywords:** Connection Manager, Proxy Service, Listener, OCM

---

## API get_uc_credential_names

### Retrieve Universal Connector Credentials
- **Support Matrix:** Guardium v12.2.2 and later
- **Workflows:** Configuration — Retrieve Universal Connector Credentials
- **Knowledge:** Universal Connector, Credential Management
- **Keywords:** get_uc_credential_names, Credential List, Universal Connector API

---

## API Parameter: api_target_host

### Set Execution Targets for REST Calls
- **Support Matrix:** All Guardium REST API endpoints
- **Limitations/Constraints:** Valid values include all_managed, all, group:<group name>, and specific host names or IPs
- **Workflows:** Configuration — Set Execution Targets for REST Calls
- **Knowledge:** Guardium REST API Architecture, Managed Unit Groups
- **Keywords:** api_target_host, Execution Target, Managed Unit, Central Manager

---

## REST API: get_ranger_services_status

### Retrieve Ranger Service Status
- **Support Matrix:** Guardium clusters with Ranger integration
- **Limitations/Constraints:** Requires clusterName parameter
- **Workflows:** Configuration — Retrieve Ranger Service Status; Navigation — Monitor Ranger Services
- **Knowledge:** Ranger Service Management, Audit Process Integration
- **Keywords:** get_ranger_services_status, Cluster Management, Ranger API

```

## 432. Configure for client web certificates
## 433. Configure for client web certificates

## Configure for client web certificates
- **Description:** Steps to set up client web certificates for securing connections.

## Luhn Algorithm Integration
## Conditional TRANSFORM Action
## Track Option for TRANSFORM

## Data Transformation and Filtering Features
### TRANSFORM Action Special Handling
- **Description:** Guides on configuring and monitoring data transformation actions, including conditional logic and field masking.

### Chart Filter Management
- **Description:** Configuring and toggling filter sets for data visualization dashboards.

## Oracle-Specific Functionalities
## General Database Security Metrics
## Creating User Hierarchy
- **Description:** How to create and manage user hierarchies using the `grdapi create_user_hierarchy` command.

### Upgrading Guardium with .tgz Files
- **Description:** Instructions for upgrading Guardium systems using the `.tgz` package files from the releases directory.

## Guardium Features

### Dynamic Ring Buffer for K-TAP
- All supported databases can use a dynamic K-TAP ring buffer to handle high traffic without overflow.

### K-TAP Preloaded by Default
- K-TAP kernel module is preloaded on all supported databases; update kernel requires closest K-TAP version.

### S-TAP Load Balancer Node Affinity
- S-TAP can be configured with load balancer affinity to prefer specific collector nodes when internal load balancing is enabled.

### S-TAP with K-TAP Installed
- When both S-TAP and K-TAP are installed, kernel updates require corresponding K-TAP updates for continued operation.

### S-TAP Without K-TAP
- S-TAP can operate without K-TAP, but monitoring is CPU intensive; use when K-TAP cannot be installed.

### Database Monitoring
- Enables dynamic port detection for databases, adjusting to port changes automatically.

## Components Overview

### Database Connectivity
- **Support Matrix:** SQL Server, Oracle, Db2, MySQL
- **Limitations:** Browser service required; unsupported on z/OS
- **Workflows:**
  - Configuration — Add Datasource
  - Navigation — View Ports
- **Links:**
  - Knowledge: Database Connection Architecture, Browser Service
  - Keywords: S-TAP, Collector, JDBC, Browser Service

### Processor Architecture
- **Support Matrix:** RHEL kernel version
- **Limitations:** PETRACE not supported on pSeries LE; kernel patches required
- **Workflows:**
  - Configuration — Check PETRACE support
  - System — Apply Kernel Patches
- **Links:**
  - Knowledge: PETRACE, Processor Compatibility, Kernel Patches
  - Keywords: pSeries LE, Compatibility, Kernel Version

## Guardium Configuration Operations

### Managing HTTP Session Templates
- **Support Matrix:** Guardium v11.0 and later
- **Limitations:** Requires central manager access; supports JSON RPC
- **Workflows:**
  - Configuration — Add Template, Activate Template, Deactivate Template, Remove Template
- **Links:**
  - Knowledge: GuardAPI Syntax, Managed Units, JSON RPC
  - Keywords: session_template, api_target_host, http_session_template

### Quarantine Management
- **Support Matrix:** Guardium v9.5 and later
- **Limitations:** REST API requires admin credentials
- **Workflows:** Management — Delete Quarantine
- **Links:**
  - Knowledge: REST API Integration, Quarantine Functionality, User Access Control
  - Keywords: quarantine, REST DELETE, user_id

### Certificate Configuration for Oracle Discovery
- **Support Matrix:** Oracle Database Inspection Engines
- **Limitations:** discovery_ora_use_port_ranges must be enabled
- **Workflows:** Configuration — Set Port Discovery Parameter
- **Links:**
  - Knowledge: Oracle Inspection Engine, Port Range Discovery, Guardium Configuration
  - Keywords: discovery_ora_use_port_ranges, inspection_engine, Guardium

### Security Policy and Entitlement Optimization
- **Support Matrix:** All Guardium-supported databases
- **Limitations:** Requires policy engine v3.0+
- **Workflows:** Configuration — Enable Entitlement Optimization
- **Links:**
  - Knowledge: Policy Engine, Entitlement Optimization Reports, Risk Assessment
  - Keywords: security_policy, entitlement_optimization, dormant_users

### Risk Assessment and User Management
- **Support Matrix:** Guardium v12.0 and newer
- **Limitations:** Maximum 150 users per category
- **Workflows:** Management — Update Risk Categories
- **Links:**
  - Knowledge: Risk Assessment Metrics, User Activity Windows, Top Risky Users
  - Keywords: Current_Risk, Top_Risky_Users, Watchlist_Users

## Datasource Connectivity

### Dynamic Port Detection
- **Support Matrix:** SQL Server, Oracle, Db2, MySQL
- **Limitations:** Browser service required; unsupported on z/OS
- **Workflows:**
  - Configuration — Add Datasource
  - Navigation — View Ports
- **Links:**
  - Knowledge: Database Connection Architecture, Browser Service
  - Keywords: S-TAP, Collector, JDBC, Browser Service

## Identity Governance Automation

### CyberArk Integration
- **Support Matrix:** All Guardium-supported databases
- **Limitations:** CyberArk SDK export restrictions apply in some regions
- **Workflows:** Configuration — Install CyberArk SDK
- **Links:**
  - Knowledge: Credential Management, Dynamic Secrets
  - Keywords: CyberArk SDK, Credential Vault

## Compliance Automation

### Compliance Monitoring Smart Assistant
- **Workflows:** Setup — Compliance Assistant
- **Links:**
  - Knowledge: Compliance Frameworks, Security Standards
  - Keywords: GDPR, PCI, SOX, Smart Assistant

### Custom Data Compliance Program
- **Limitations:** Requires newer Guardium versions
- **Workflows:** Configuration — Define Controls
- **Links:**
  - Knowledge: Custom Controls, Data-Driven Compliance
  - Keywords: Customization, Policy Builder

## Data Exploration

### Observer Tool
- **Limitations:** Requires large audited datasets
- **Workflows:** Visualization — Data Flow Graph
- **Links:**
  - Knowledge: Audited Data, Transaction Analysis
  - Keywords: Visualizer, 3-D View, Data Transactions

## Visualization

### Dashboard Chart Filters
- **Limitations:** Overrides only general dashboard filters
- **Workflows:** Analysis — Filter Chart
- **Links:**
  - Knowledge: Dashboard Insights, Chart Interactions
  - Keywords: Filter Icon, Specific Filters, Chart Details

## Reporting

### Export Task Results
- **Limitations:** PDF limit 5,000 rows; CSV/CEF

## Guardium Features

### 501. Control Concurrent Logins by User from Multiple IP Addresses
- **Support Matrix:** All versions
- **Limitations/Constraints:** None
- **Workflow:** Security Configuration — Concurrent Login Control
- **Knowledge:** Access Control, Session Management
- **Keywords:** Concurrent Login, User Session, IP Restriction

### 502. Enable GenAI for Integration with Existing Guardium Features
- **Support Matrix:** Versions supporting GenAI
- **Limitations/Constraints:** Requires SOX ticket configuration
- **Workflow:** Configuration — GenAI Integration
- **Knowledge:** GenAI Application, System Enhancement
- **Keywords:** SOX Reconciliation, GenAI Feature, System Integration

### 503. Query Rewrite Permissions in Report Builder
- **Support Matrix:** Versions with Report Builder
- **Limitations/Constraints:** Requires Query Rewrite feature enabled
- **Workflow:** Configuration — Report Permissions
- **Knowledge:** Report Customization, Data Security
- **Keywords:** Query Modify, Report Access, Permission Settings

### 504. Include Healthy Systems Checkbox
- **Support Matrix:** All versions
- **Limitations/Constraints:** None
- **Workflow:** System Health — Dashboard Configuration
- **Knowledge:** System Monitoring, Health Dashboard
- **Keywords:** System Health, Dashboard View, Health Status

### 505. Guardium Dashboard Configuration Tasks
- **Support Matrix:** Versions with dashboard capabilities
- **Limitations/Constraints:** Requires deployment health roles installed
- **Workflow:** Configuration — Dashboard Setup
- **Knowledge:** Health Monitoring, Dashboard Customization
- **Keywords:** Deployment Health, Data Overload, Security Views

### 506. Registry Certificate Installation Skip for Cluster Nodes
- **Support Matrix:** Clustered environments
- **Limitations/Constraints:** None
- **Workflow:** Cluster Configuration — Node Settings
- **Knowledge:** Cluster Management, Certificate Installation
- **Keywords:** Cluster Node, Registry Certificate, Installation Skip

### 507. Generate New Certificate Request in Guardium
- **Support Matrix:** All versions requiring certificates
- **Details:**

## Guardium Monitoring and Diagnostics

### Diagnosing GIM Data Accuracy
- **Support Matrix:** Guardium 11.3 and later
- **Limitations/Constraints:** Requires GIM server and clients to be running
- **Workflows:** Configuration — Run GIM Diagnostics
- **Knowledge:** Guardium Installation Manager (GIM), Central Management
- **Keywords:** GIM client, GIM server, diagnostics, data accuracy

### Secure Configuration of Cloud Pak for Data
- **Support Matrix:** IBM Cloud Pak for Data
- **Limitations/Constraints:** Requires access to IBM Cloud Container Registry
- **Workflows:** Configuration — Mirror Container Images
- **Knowledge:** Cloud Pak for Data Architecture, Container Image Mirroring
- **Keywords:** Cloud Pak, CASE assets, container registry, mirror command

### Firewall Activation Control
- **Support Matrix:** Guardium 12.1 and beyond
- **Limitations/Constraints:** None
- **Workflows:** Configuration — Set Default State
- **Knowledge:** Firewall Management, Policy-Based Activation
- **Keywords:** firewall, activation state, policy rules, Default State

### Group-Based Data Management
- **Support Matrix:** All Guardium-supported databases
- **Limitations/Constraints:** Group size limited to 10,000 members
- **Workflows:** Configuration — Build Groups
- **Knowledge:** Guardium Administration, Data Object Management
- **Keywords:** S-TAP, data groups, policy builder, group membership

### Namespace Specification for Data Ingestion
- **Support Matrix:** IBM Cloud Pak for Data namespaces
- **Limitations/Constraints:** Namespace must exist before starting ingestion
- **Workflows:** Configuration — Set Ingestion Namespace
- **Knowledge:** Namespace Management, Data Ingestion Processes
- **Keywords:** namespace, data ingestion, resources, K8s namespace

---

## Data Guard and Security

### RSA SecurID Certificate Store
- **Support Matrix:** Central manager only
- **Limitations/Constraints:** Certificate must be PEM format
- **Workflows:** Configuration — Store Certificate
- **Knowledge:** RSA SecurID Authentication Manager, SSH Authentication
- **Keywords:** RSA SecurID, PEM, SSH, Central Manager

### Maximum Query Duration
- **Support Matrix:** All supported databases
- **Limitations/Constraints:** Default 180 seconds
- **Workflows:** Configuration — Set Maximum Duration
- **Knowledge:** Query Optimization, TDS Response Packets
- **Keywords:** Max Query Duration, show max_tds_response_packets

### Backup Commands
- **Support Matrix:** Central manager, aggregator, standalone
- **Limitations/Constraints:** System backup removes personal information
- **Workflows:** Configuration — Perform Backup, System — System Backup
- **Knowledge:** Backup Strategy, Data Protection
- **Keywords:** Backup, System Backup, Data Removal

### Parameter Entitlement Optimization
- **Support Matrix:** Guardium UI
- **Limitations/Constraints:** Boolean values required
- **Workflows:** Configuration — Enable Optimization
- **Knowledge:** What If? Tab, Data Generation
- **Keywords:** Parameter, Boolean, What If? Tab

### Store API in Guardium
- **Support Matrix:** Guardium version 10.5 and later
- **Limitations/Constraints:** Requires HTTPS, port 8443
- **Workflows:** Configuration — API Installation
- **Knowledge:** REST API, HTTPS
- **Keywords:** Store API, GET Method, GuardAPI

### Investigation Dashboard
- **Support Matrix:** Guardium UI
- **Limitations/Constraints:** Requires policy configuration
- **Workflows:** Configuration — Identify Outliers
- **Knowledge:** Outlier Analytics, Data Investigation
- **Keywords:** Investigation Dashboard, Outliers, Guardium

### Data Policy Management
- **Support Matrix:** Policy Builder tool
- **Limitations/Constraints:** Advanced policies need SR scripting
- **Workflows:** Configuration — Configure Policies
- **Knowledge:** Data Protection Policies, SR Scripting
- **Keywords:** Data Policies, Policy Builder, SR Script

### MongoDB Ignore Sessions
- **Support Matrix:** Guardium Datasource
- **Limitations/Constraints:** Specific users/noise filtering

## Guardium Technical Overview

### Data Source Auditing and Insight
#### Oracle Audit Record Fields
- **Components:** Oracle DB 12c, 18c, 19c with privileged audit access
- **Workflows:** Audit Extraction, Report Generation
- **Knowledge:** Guardium Agent, InfoSphere Change Data Capture
- **Keywords:** old_value, new_value, transaction_timestamp, audit_log

### Anomaly Detection and Alert Management
#### Correlation Alert Notifications
- **Components:** Guardium 11+, SaaS
- **Workflows:** Enable Alerts, Dispatch Alerts
- **Knowledge:** Anomaly Detection Algorithms, Alert Queuing
- **Keywords:** correlation_alert, anomalous_activity, alert_query, polling_interval

### License and Compliance Monitoring
#### License Utilization
- **Components:** Guardium 11+, Guardium SaaS
- **Workflows:** Activate License, Monitor Usage
- **Knowledge:** License Server, Compliance Framework
- **Keywords:** license_utilization, compliance_status, usage_metrics

## Monitoring and Alerting
- **Monitoring:** License Dashboard
- **Alert:** License Threshold Breach
- **Knowledge Links:** License Allocation, Compliance Reporting
- **Keywords:** licenses_remaining, license_expiry, usage_report, compliance_status

## Platform Information Capture
### Server OS Attribute
- **Support Matrix:** Linux, Windows, AIX, Solaris
- **Limitations:** May fail for virtualized environments without proper hypervisor support
- **Workflows:** Discovery – Server OS Inventory; Utilization – Platform Optimization
- **Knowledge Links:** Device Fingerprinting, Virtualization Support
- **Keywords:** Server_OS, virtual_machine, hypervisor, OS_fingerprint

## API Key Validation
### K-TAP Build Verification
- **Support Matrix:** Kernel versions 3.10 to 5.15
- **Limitations:** Requires kernel source headers; incompatible with patched kernels
- **Workflows:** Build Process – K-TAP Compilation; Verification – Output Inspection
- **Knowledge Links:** Kernel Module Building, K-TAP Architecture
- **Keywords:** ktap_build, kernel_log, compilation_output, build_success

## Dynamic Load Balancing Configuration
### Load Balancer Time Interval
- **Support Matrix:** Enterprise Load Balancer 2.x, 3.x
- **Limitations:** Value must be greater than zero seconds; defaults to 30 seconds if set incorrectly
- **Workflows:** Configuration – Load Balancer Params; Monitoring – Event Logging
- **Knowledge Links:** Enterprise Load Balancer, Event Logging Mechanism
- **Keywords:** balancer_time_interval, retry_attempts, internal_event, load_balancer_config

## External S-TAP Management
### Inspection Engine and Collector Configuration
- **Support Matrix:** External S-TAP 1.5 and above
- **Limitations:** Requires network access between S-TAP and collectors
- **Workflows:** Configuration – Inspection Tuning; Management – Collector Assignment
- **Knowledge Links:** Security Inspection Engine, External S-TAP Architecture
- **Keywords:** inspection_engine, collector_management, inspection_parameters, external_s_tap

## Ingress Annotations
### Ingress Customization
- **Support Matrix:** Kubernetes 1.18+, OpenShift 4.5+
- **Limitations:** Annotation values must comply with Kubernetes API specifications
- **Workflows:** Deployment – Ingress Setup; Customization – Annotation Configuration
- **Knowledge Links:** Kubernetes Ingress, API Specification Compliance
- **Keywords:** ingress_annotation, namespace_specification, ingress_configuration, kubernetes_api

## GIM Client Certificate Management
### Certificate Replacement
- **Support Matrix:** GIM 3.4.x and later
- **Limitations:** Must ensure backward compatibility with existing infrastructure
- **Workflows:** Security – Certificate Upgrade; Validation – Security Audit
- **Knowledge Links:** Certificate Management, SHA Algorithm Transition
- **Keywords:** gim_client_certificates, sha1_replacement, security_compliance, certificate_validation

## Certificate Management
### Certificate Replacement for Secure Communication
- **Support:** Guardium clients (GIM, S-TAP®), servers (central manager, aggregators, standalone collectors)
- **Limitations:** SHA1 deprecation requires SHA256 for new certificates; mixed environments need staged migration
- **Workflows:** Configuration – Certificate Replacement; Workflow – Auto‑Renewal; Workflow – Rollback (TLS downgrade)
- **Knowledge Links:** TLS Handshake, GIM Client Communication
- **Keywords:** SHA1, SHA256, TLS, GIM client, Certificate Authority, Re‑issue Workflow

## SNMP Management
### Redundant SNMP Trap Server Configuration
- **Support Matrix:** Guardium centralized managers, aggregators, collectors
- **Limitations:** Single SNMP server defined per appliance; redundancy requires manual fail‑over
- **Workflows:** Configuration – SNMP Setup; Workflow – Fail‑over Testing
- **Knowledge Links:** Trap Mechanism, Event Alarming
- **Keywords:** SNMP, trap server, redundancy, fail‑over

## Certificate Blocklist Management
### Certificate Blocklist for External S‑TAP and CMS
- **Support Matrix:** External S‑TAP modules, CMS appliances
- **Limitations:** External S‑TAP requires manual blocklist upload; CMS relies on integrated GUI/GIM processes
- **Workflows:** Configuration – Certificate Blocklist Upload; Workflow – Remote S‑TAP Update
- **Knowledge Links:** Token Revocation, GUI/GIM Certificate Lifecycle
- **Keywords:** Blocklist, External S‑TAP, CMS, Certificate Revocation List, Venafi

## Encrypted Data Transfer
### Collector‑Aggregator Encryption Setup via Store S2C
- **Support Matrix:** Data collectors, aggregators, Syslog hosts
- **Limitations:** Requires S2C key exchange; Syslog host must support TLS 1.2+
- **Workflows:** Configuration – S2C Key Exchange; Workflow – Syslog Encryption Enablement
- **Knowledge Links:** TLS Connectivity, Data Encryption in Transit
- **Keywords:** S2C, encrypted traffic, collector, aggregator, key management

## DB2 on z/OS Configuration
### Client IP Use for Host Name in Alerts
- **Support Matrix:** DB2 z/OS instances, Guardium inspectors
- **Limitations:** Requires inspection engine restart; older DB2 versions ignore setting
- **Workflows:** Configuration – Sniffer Parameter Change; Workflow – Engine Resta

## API Configuration
### Target Host Specification for API Calls
API target defaults to the local host; groups require membership definitions.

**Links:** REST API Design, Central Management  
**Keywords:** api_target_host, managed units, groups, centralized manager

## Workflow Definition
### Action Summary Tab in Policy Builder
Actions affect only future policy evaluations.

**Links:** Policy Enforcement, Action Types  
**Keywords:** Policy summary, action details, rule workflow, evaluation scope

## Guardium Administration
### Configuring Compliance Types
Must run the Compliance and Application Data Monitoring wizard for each type.

**Links:** Compliance Management, Application Data Monitoring  
**Keywords:** Compliance Type, Wizard, Config Management

## 557. Oracle example
### Viewing and Sharing Reports
No limitations.

**Links:** Report Building, Personalization  
**Keywords:** Report, Customize, Save, Share

## 559. Oracle example
### Runtime Sensitive Object Identifier
No limitations.

**Links:** Runtime Analysis, Object Processing  
**Keywords:** Object Name, Runtime, Identifier

## 560. CPU
### Data Mart Documentation
No limitations.

**Links:** Data Marts, Export Types  
**Keywords:** Data Mart, Enhanced, Extraction, Export

## 561. grdapi create_user_hierarchy
### Client Server / Session Entity Attributes
No limitations.

**Links:** Client Server Parameters, DB2 Attributes  
**Keywords:** Server IP, Client IP, IP Tuple

## 562. of Licenses This value
### Data Security User Hierarchy
No limitations.

**Links:** Data Security, User Roles  
**Keywords:** Hierarchy, Navigate, Select, View

## 563. of Licenses This value
### Data Level Security Requirements
Entities and domains must align.

**Links:** Domain Configuration, Predefined Entities  
**Keywords:** Filtering, Secured Domains, Custom Domains

## 564
### Alert Configuration for Failed Logins
No limitations.

**Links:** Alert System, Failed Logins  
**Keywords:** Alert, Failed, Login, Configuration

## 565
### Data Import from External Datasources
Requires appropriate permissions.

**Links:** External Datasources, API Utilization  
**Keywords:** Import, Populate, Groups, Datasources

## 566. Skips registry certificate installation on cluster nodes
### Skip Certificate Installation on Cluster Nodes
Certmanager or similar tools must be used for certificate management.

**Links:** Kubernetes TLS Certificates, Helm Chart Deployment  
**Keywords:** cs guardium, certmanager, cluster node certificates

## 567
### Verify API key exists
Requires valid user permissions for key generation.

**Links:** All supported Guardium APIs  
**Keywords:** Verify API Key Existence

## 568. Verify API key exists

### Verify API Key Validity
Check if an API key is valid within Guardium.

## 569. `/usr/local/guardium/guard_stap/guardctl db_instance=db2inst1 deactivate`

### Deactivate DB2 Instance
Use `guardctl` to deactivate a DB2 instance on Guardium.

## 570. Plugin values

### Enable A-TAP via GUI
Activate A-TAP encryption through the Guardium GUI on Windows.

## 571. `ps -ef | grep gtwgateway`

### Discover Supported Database Types
List databases using command-line tools on Guardium.

## 572. `chgroup users=informix guardium`

### Configure Informix Group
Add Informix users to the Guardium group using `chgroup`.

## 573. Related tasks

### External S-TAP Overview
Learn about External S-TAP deployment for Guardium traffic monitoring.

## 574. Optional, annotations to specify for ingress

### Configure Ingress Annotations
Specify Kubernetes ingress annotations for Guardium deployment.

## Special Handling of TRANSFORM Actions

### Overview
Manage special TRANSFORM action types in query rewrite definitions.

## Managing Client Web Certificates

### Overview
Configure and verify client web certificates for Guardium systems.

## Enterprise Security Model

### Data Access Control
- Components: Support Matrix (Oracle, SQL Server, Db2, MySQL, PostgreSQL), Limitations/Constraints (No hierarchical inheritance in cloud, requires RBAC), Workflows (Define Role Hierarchy, Access Control Panel)
- Links: Knowledge (NIST RBAC Model, Role Inheritance, Policy Enforcement), Keywords (Data Obfuscation, Role Management, Latest Guardium Versions, Sensitive Data Access)

## SessionLossesMetadata

### Description
Controls metadata when packet losses occur in a session.

### Components
- Components: Support Matrix (Not applicable, system-wide parameter), Limitations/Constraints (Must be enabled before packet loss events, no effect on active sessions), Workflows (Enable/Disable Metadata Capture)
- Links: Knowledge (Guardium Session Management, Network Reliability Monitoring), Keywords (Packet Loss, Session Metadata, Network Auditing, Guardium Parameter)

## Database Auditing and Configuration

### Value Change Auditing Trigger
- Components: Support Matrix (Oracle), Limitations/Constraints (None), Workflows (Create Trigger)
- Links: Knowledge (Database Triggers, Audit Policies), Keywords (Guardium, Oracle, Trigger, Audit)

### Oracle Extraction Log for Data Mart
- Components: Support Matrix (Oracle), Limitations/Constraints (None), Workflows (Export Data)
- Links: Knowledge (Data Mart, Extraction Process), Keywords (Extraction Log, Data Mart, Data Extraction)

### Audit Report Attributes
- Components: Support Matrix (Guardium Reporting), Limitations/Constraints (None), Workflows (Audit Report)
- Links: Knowledge (Audit Attributes, Reporting), Keywords (Audit Attributes, Data Columns, Report)

### Audit Result Distribution
- Components: Support Matrix (Guardium Audit Processes), Limitations/Constraints (None), Workflows (Continuous Distribution)
- Links: Knowledge (Audit Workflow, Continuous Monitoring), Keywords (Audit Continuous, Distribution, Receiver)

### Oracle Data Visualization
- Components: Support Matrix (Guardium version 12.2+), Limitations/Constraints (None), Workflows (Executive Dashboard)
- Links: Knowledge (Data Visualization, Executive Management), Keywords (Executive Dashboard, Security Data, Visualization)

### DB Name/Group and App User/Group Attributes
- Components: Support Matrix (Guardium Reports), Limitations/Constraints (None), Workflows (Attribute Display)
- Links: Knowledge (Report Attributes, Data Grouping), Keywords (DB Name Group, App User Group, Report Column)

### Data Source Connectivity
- Components: Support Matrix (SQL Server, Oracle, Db2, MySQL), Limitations/Constraints (Browser service required for some databases), Workflows (Add Datasource, View Ports)
- Links: Knowledge (Database Connection Architecture, Browser Service), Keywords (JDBC, Browser Service, Data Source)

## Guardium Feature Reference

### RPM Inclusion for Hyper-V Support
- Components: Support Matrix (Guardium Installer 12.0+), Limitations/Constraints (Red Hat Virtualization compatibility), Workflows (Installation)
- Links: Knowledge (Guardium Installer, Virtualization Support), Keywords (Hyper-V, RPM, Virtualization, Red Hat)

### Guardium Fileserver Agent Configuration
- Components: Support Matrix (All supported Guardium versions), Limitations/Constraints (Valid credentials required), Workflows (Configure Fileserver Agent)
- Links: Knowledge (Fileserver Agent, Guardium Authentication), Keywords (Hostname, Username, Password, Authentication)

## Configuration

## GuardAPI Syntax Guidelines
Use double quotation marks for multi-word parameters in API commands.

## Miscellaneous GuardAPI Functions
GuardAPI supports all system configuration tasks across all versions.

## Interceptor Engines Protocol Configuration
Configure protocols for Guardium 11.0+; misconfiguration affects monitoring.

## Auto-Discovery Scan Management
Manage auto-discovery scans in Guardium 12.0+.

## OAuth Client Management
Configure OAuth clients in versions with OAuth support.

## Data Purge Configuration
Export purge configurations using the REST DELETE API (v11.2+).

## Database Configuration
Configure client web certificates for database discovery with admin privileges.

## Security Configuration
Monitor login failure rates for security analysis.

## Policy Configuration
Install and activate data policies immediately in v11.2+.

## Audit Configuration
Handle TRANSFORM actions in data protection policies with special rules.

## Audit Process Integration
Map audit processes to compliance frameworks like PCI-DSS and SOX.

## Database Specific Configuration
Monitor active audit processes for Oracle databases in centralized configurations.

## License Management
Track license availability using the licenses remaining indicator.

orksflows with different types:** Configuration — Install CyberArk SDK
- **Links:**
  - **Knowledge:** Credential Management, Dynamic Secrets
  - **Keywords:** CyberArk SDK, Credential Vault

### Client Web Certificates (Group Population)
- **Components:**
  - **Support Matrix:** All Guardium-supported collectors
  - **Limitations/Constraints:** Requires valid web certificate in PEM format
  - **Workflows with different types:** Provisioning — Add Web Certificate; Navigation — View Certificate Details
- **Links:**
  - **Knowledge:** Certificate Management, Entity Grouping
  - **Keywords:** Web Certificate, PEM Format, Entity Group

### Oracle Monitoring Changes
- **Components:**
  - **Support Matrix:** Oracle databases
  - **Limitations/Constraints:** Requires CAS Changes enabled
  - **Workflows with different types:** Monitoring — Oracle Changes; Navigation — View Changes Details
- **Links:**
  - **Knowledge:** Oracle Environment, Guardium CAS
  - **Keywords:** CAS Changes, Oracle Updates, Monitoring Workflow

### GUI for Scheduled Reports
- **Components:**
  - **Support Matrix:** All Guardium-supported collectors
  - **Limitations/Constraints:** Requires CLI access
  - **Workflows with different types:** Configuration — Scheduled Reports; Navigation — Report Configuration
- **Links:**
  - **Knowledge:** Scheduled Reporting, CLI Commands
  - **Keywords:** CLI Commands, Report Configuration, Distributed Reports

### User Hierarchy API Script Example
- **Components:**
  - **Support Matrix:** All Guardium-supported collectors
  - **Limitations/Constraints:** Requires API access enabled
  - **Workflows with different types:** Provisioning — Create User Hierarchy; Navigation — View Hierarchy Details
- **Links:**
  - **Knowledge:** API Scripting, User Management
  - **Keywords:** API Script, User Hierarchy, create_user_hierarchy

## # Guardium Topic Reference

### Ingress Annotation Configuration
- Explains applying custom settings to ingress resources via annotations.
- Steps: Identify needed annotations → Edit ingress YAML → Apply changes.
- Note: Proper annotations ensure expected ingress behavior across environments.

### Central Manager/Managed Unit Compatibility
- **Support:** All Guardium versions
- **Details:** Older managed units can be managed by newer central managers; optimal performance with matching versions.
- **Workflow:** Configuration → Upgrade Units
- **Knowledge Areas:** Version Compatibility, Upgrade Process
- **Keywords:** Central Manager, Managed Unit, Version Upgrade

### Sniffer Buffer Size Adjustment
- **Support:** Collectors with ≥32GB memory
- **Details:** Requires sniffer process restart post-modification.
- **Workflow:** Configuration → Performance Tuning
- **Knowledge Areas:** Performance Optimization, Memory Management
- **Keywords:** Sniffer, Buffer Size, Collector, Performance Tuning

### Vulnerability Assessment Datasource Assignment
- **Support:** Guardium-supported datasources
- **Details:** Requires appropriate user permissions.
- **Workflow:** Configuration → Assign Datasources
- **Knowledge Areas:** Vulnerability Assessment, Datasource Management
- **Keywords:** Vulnerability Assessment, Datasource, Assignment

### Anomaly Score Interaction
- **Support:** Guardium anomaly detection modules
- **Details:** Only applicable to high-volume events.
- **Workflow:** Entities → Anomaly Scores → Features → Cluster Tab
- **Knowledge Areas:** Anomaly Detection, Scoring System
- **Keywords:** Anomaly Score, Right-Click Menu, High Volume, Cluster Tab

### Character Encoding/Data Format Support
- **Support:** Various encoding standards and data formats
- **Details:** *Incomplete entry—no limitations/constraints or workflows provided.*

```markdown
## Query Rewrite and Policy Integration
- Guardium query processing features support entities (query rewrite) and access policy rules (security policy). Requires security policy activation.

## Oracle DW SELECT Object-Field Access Reporting
- Reports Oracle database SELECT queries with object-field access. Requires DW SELECT Object-Field Access report configuration.

## Force Deleting an Assessment
- Force delete assessments in Guardium. Cascade effects on dependencies and purges storage results.

## Custom Table Builder Access Control
- Manage custom tables using Table Builder. Requires appropriate permissions for creation and management.

## LDAP Import

### Import LDAP Users and Groups
- Supports Active Directory, OpenLDAP, IBM Tivoli DS. Requires LDAP server reachable and user objectClass `inetOrgPerson`/`organizationalPerson`.
- Configuration (Admin → LDAP → Import) and navigation steps. Keywords: ldap_import, ldap_bind.

### Map LDAP Attributes to Guardium Roles
- Map LDAP attributes to Guardium roles. Limited to standard Guardium role fields.
- Configuration (LDAP Attribute Mapping). Keywords: ldap_role_map, guardium_role.

## Custom Table Management

### Create and Manage User-Defined Tables
- Create tables in all supported databases. Table size limited by database, manual schema changes require restart.
- Configuration (Admin → Tables → Define). Keywords: custom_table, table_schema.

### Import Data into Custom Tables
- Import CSV data into custom tables. Source data must be CSV, limited to 1M rows per operation.
- Configuration (Admin → Tables → Import Data). Keywords: csv_data, import_job.

## Guardium Data Ecosystem

### Enable Solr Auditing in Cloudera
- Explicitly enable Solr auditing in Cloudera environment per documentation.

### Firewall Configuration for External S-TAP
- Configure firewall for external S-TAP deployment with potential performance impact at high traffic.

### GIM Client Discovery and S-TAP Deployment
- Default separate steps for GIM client discovery and S-TAP deployment across all supported systems.

### Aggregator Deployment in Guardium
- Aggregate data in Guardium Central Manager with Aggregator support. Requires central manager appliance.

### Guardium Upgrade Path Considerations
- (Content intentionally omitted as incomplete)
```

## Guardium Anomaly Detection

- **Configure client web certificates**: Supported on all platforms. No constraints.
- ***Special handling for TRANSFORM actions***: Requires SQL parser enabled on SQL Guardium instances.
- ***Oracle example* (report generation)**: No constraints. Keywords: application user, report run.
- ***Oracle example\* (security incident)**: Completing the query requires the Terminated Users group. Keywords: failed login, terminated account.

## 744. Vulnerability Management

- ***Or use the packaged .tgz file***: Supported on Guardium 11.3+. No constraints or limitations mentioned.

# Compressed Documentation

## Workflows with different types
- **Configuration — Permissions Reports**
- **Configuration — Custom Domain Builder**
- **Configuration — Unit Utilization, Visualization**
- **Deployment — Cluster Setup**
- **Troubleshooting — Cloud Deployment**
- **Configuration — API Management**
- **Maintenance — Deactivate Instance**
- **Deployment — Namespace Configuration**
- **Configuration — Hardening → Certificate Validation**
- **Configuration — Search Builder → Save Annotation**
- **Diagnostic — Capture → Run must_gather**
- **Integration — REST API → Create/Manage Template Set**
- **Assessment — Setup → Create Security Assessment**

## Certificate Validation
### DISALLOW_INVALID_CERTIFICATES
- **Works with all Guardium Data Protection versions**
- Terminates secure session on invalid TLS certificates

## annotationB4FB8053‑A5C3‑4912‑912D‑21C04C0A934E
- Saves custom step name and optional conditional logic in Search Builder

## mustGatherF46D3F5B‑F46D‑44B7‑8427‑E4D84E926FE8
- Captures diagnostic data; usable in every Guardium deployment

## casTemplateSetF5F1900C‑1143‑4E18‑AB02‑8AA59263EB5E
- Manages Template Sets via Guardium REST API (v11.3+)

## knowledge799F1E12‑F5C6‑47AD‑BF2F‑CF40F47FE381
- Creates a Security Assessment object for audit processes

## knowledgeFA96E921‑53A8‑4C95‑9E50‑A2C43FCAECB8
*(no description available in the source entry)*

## Data Source Permissions

**Overview:**  
Allows users to share datasources with others and assign permissions.

**Components:**
- **Support Matrix:** All datasources supported by Guardium
- **Limitations/Constraints:** Requires appropriate permissions on datasource
- **Workflow:** Access Management – Share → Assign Permissions

**Links:**
- **Knowledge:** Datasource Permissions, Role-Based Access Control
- **Keywords:** datasource, share, permissions, role assignment, GUI workflow

## Delete HDFS Configuration

**Overview:**  
Removes an HDFS configuration from Guardium.

**Components:**
- **Support Matrix:** Guardium v11.3 and later
- **Limitations/Constraints:** Requires lradmin role and HDFS integration configured
- **Workflow:** Installation – Configure HDFS → Remove Configuration

**Links:**
- **Knowledge:** HDFS Integration, API Management
- **Keywords:** delete_ranger_hdfs_config, REST DELETE, hostname, port, v11.3+

## Security and Compliance Features

### Client Certificate Management

**Overview:**  
Manages client web certificates for Guardium Data Protection.

**Components:**
- **Support Matrix:** Guardium Data Protection v12.0 and later
- **Limitations/Constraints:** Requires Security Certificates module enabled
- **Workflow:** Configuration – Security → Client Certificates

**Links:**
- **Knowledge:** Client Certificate Management, IP Address Management
- **Keywords:** CIDR notation, IP group, group_id, type, client web certificates

## Distributed Reporting

**Overview:**  
Configures non‑distributed reports to be processed on collectors and aggregated centrally.

**Components:**
- **Support Matrix:** All Guardium-supported databases
- **Limitations/Constraints:** Requires a defined non‑distributed report
- **Workflow:** Configuration – Distributed Report

**Links:**
- **Knowledge:** Reporting Architecture, Load Balancing
- **Keywords:** Collectors, Aggregators, Non-Distributed Report

---

**Compressed reference containing only distinct, high‑level concepts.**

## GIM Supervisor Module
Supports supervision and monitoring of Guardium processes across all versions.

## External S-TAP Load Balancer Integration
Configures load balancing for External S-TAP in supported environments with F5 or compatible load balancer.

## IBM Cloud Pak Integration with S-TAP Services
Defines ingress annotations for Cloud Pak for Data on OpenShift ingress controller.

## Data Management and Storage
Throttles S2C load when MAX_S2C_VELOCITY is exceeded; configure threshold for optimization.

## Data Management

### Dynamic Date Range Handling
Set purge parameters using valid date expressions like "NOW -48 Month".

### Custom Certificate Management
Update certificates issued by trusted CA; navigate certificate details for management.

### RSA SecurID Integration
Enable MFA; verify compatible RSA SecurID token during login.

### User-DB Association Management
Associate users at node level in Guardium 12.0 and later versions.

### Advanced Data Security Features
Enable query rewrite, quarantine, and real-time alerting in Enterprise Edition with proper licensing.

### Registry Certificate Management
Not applicable on cluster nodes.

### Amazon S3 Integration
Configure S3 bucket setup in Guardium 12.2.x and later versions.

### Message Template Customization
Edit message templates in Central Manager with global profile access.

### S-TAP Upgrade and Monitoring
Configure real_DB_port for real-time DB port monitoring after upgrade.

## Audit Log Search and Filtering
Search by Date, Time, Type, Execution Term, Host, AUID, Event. No limitations.

## Data Protection Capabilities
Protects all data types. Requires Guardium Agent. Integrates with Security — Real-Time Alerting. Keywords: Alerting, SIEM, Reporting, Analytics.

## External S-TAP Deployment Script
Parameters supported on Linux and Windows. Requires API Permissions. Keywords: --c, Script Parameters, External S-TAP, Deployment.

## Logging and Rotation Configuration
Commands Store System Log, Store System Snmp Location. Requires minimum system privileges. Keywords: Log Rotation, SNMP, Location, Configuration.

## Distributed Report Management
Managed via Guardium Central Manager. Requires Central Manager configuration. Keywords: Remove, Target, Distributed Report, Guardium.

## Data Sensitivity Management
Configures policies for Oracle, DB2, MS SQL, MySQL. Requires Sensitive Data Configuration Module. Keywords: Sensitive, Policy Rules, Risk Spotter, Data Governance.

## Unfinished Excerpt
Not enough information to generate a meaningful entry.

## User Access Patterns
Multiple Client IPs Report: Monitors all IP addresses by default. Keywords: User Access, Client IP, Security Insights.
CPU VA Summary ID: Requires security assessments enabled. Keywords: VA Summary, Security Tests, Admin Access, Test Entities.
Archive Audit Data Daily: Stores audit data daily in one-day chunks. Keywords: Audit Data, Daily Archiving, System Admin, Data Storage.
Integrations Syslog Forwarding: Configured via CLI command. Keywords: Guardium SIEM, Integration Setup, Syslog Parameters, Forwarding.
GIM Parameters Communication: WINSTAP_TAP_IP, WINSTAP_SQLGUARD_IP require manual specification. Keywords: GIM Parameters, WINSTAP_TAP_IP, WINSTAP_SQLGUARD_IP, Host Specification.

## Throttling and Packet Filtering
Store throttle command supports packet filtering from Guardium 12.0. Requires root access. Keywords: store throttle, inspection-core, packet filter, traffic shaping.

## External STAP Certificate Validation
Verify client certificates for external STAP agents only. Requires properly configured keystore with root/intermediate certs. Keywords: keystore_external_stap, SSL trust, client cert validation.

## Trust Management

### Store Keystore External STAP
Support Matrix: Guardium v12.0+  
Limitations: PEM-encoded keystore; ≤5 certificate chain entries  
Configure: Admin > Manage Certificates > Import Keystore  
Related: Vault Integration, Secure Communication, keystore_external_stap, GuardAPI, PEM encoding

## Risk Behavioral Analytics

### Behavioral Analytics Window
Applicable to all centrally managed Guardium platforms  
Requires Behavioral Analytics module  
Configure: Access > Behavior Analytics > Maximum Risk tab  
Visualize: Generate Risk Reports  
Related: Risk Assessment, Security Policies, Data Activity Monitoring, Risk Indicators, User Behavior, Anomaly Detection

## Configure for Client Web Certificates

### Enable/disable Outliers Detection
All S-TAP installations supported  
Disabled via Central Manager only  
Configure: Central Manager > Outliers Detection; Policy > Disable Logging Constructs  
Related: Configuration Management, Security Monitoring, Outlier Analysis

## Special Handling for TRANSFORM Actions

### Policy Combination Errors
Guardium Policy Management Interface supports 
Selective and non-selective audit policies; flat/non-flat log policies  
Errors generated on combination  
Configure: Policy Construction > Selective Audit; Policy Deployment > Install Policies  
Related: Policy Management, Security Frameworks, Error Handling

### Security Threats and Policy Detection
Threat detection limited to defined patterns  
Configure: Policy Construction > Threat Detection; Reporting > Security Summary  
Related: Threat Management, Security Policies, Cross-site Scripting, OS Command Injection, SQL Injection

## Special Handling for Transform Actions

### Audit Process Files Export
Auditing System supports export  
Export results bypass Data Level Security  
Configure: Auditing Process > Export Settings; Reporting > Export Audit Data  
Related: Auditing Processes, Data Export, CSV Format

## Security and Compliance

### Client IP Analysis
All client-server protocols supported  
No limitations  
Configure: Client IP Filtering; Navigation > Reports  
Related: Analyzed Client IP, Client Host Name, S-TAP, Collector, Encryption

### License Reporting
Supported from Guardium 11.x  
No limitations  
Configure: Reporting > License Usage; Navigation > Reports  
Related: License Management, Entities, Licenses, Usage

### Role-Based Access Control (RBAC)
All platforms supported  
Admin role required for creation  
Configure: Admin > Create Role; Navigation > Admin  
Related: Auditor Role, Custom Roles, Auditing, Permissions

### GuardAPI Usage
API v1.0+ supported  
Requires API Key  
Configure: Access Control > API Management; Navigation > Security  
Related: User Account, Password, Authentication, GuardAPI, LDAP Import

### GUI Settings
Guardium 11.3+ supported  
Global Profile access required  
Configure: Global Filters; Navigation > Setup  
Related: Reporting, Auditing, Reports, Audit Processes, Security Assessments

### Load Balancing Verification
Enterprise Load Balancing feature  
No limitations  
Configure: Load Balancer Settings; Navigation > Monitoring  
Related: Load Balancing, Failover Configuration, S-TAP Traffic

### Certificate Retrieval API
REST API v2.0+ supported  
No limitations  
Configure: Certificate Management; Navigation > Security  
Related: Certificate Types, Creation Dates, REST API, Alias, Certificate Body

### Policy Troubleshooting
Supported from Guardium 10.x

## Db2 Exit Library

### Db2 Exit Library Overview
- **Component:** Supports Db2 across versions/platforms
- **Workflows:** Enable Db2 Exit Library, Inspect Db2 Traffic
- **Links:** Guardium Architecture, S-TAP Component
- **Keywords:** Db2 Exit Library, S-TAP, Native Support, Encryption

## Firewall Installed

### Firewall Feature Configuration
- **Component:** Applies to all Guardium-supported platforms
- **Constraint:** Cannot enable both FIREWALL_INSTALLED and QUERY_REWRITE_INSTALLED
- **Workflow:** Set FIREWALL_INSTALLED
- **Links:** Guardium Configuration Framework, Security Features
- **Keywords:** FIREWALL_INSTALLED, guard_tap.ini, Configuration Constraint

## Oracle Client Configuration

### Oracle Client Setup for Connection Manager
- **Component:** Requires Oracle Client 12c or later
- **Workflows:** Oracle Client Setup, Oracle Connection Manager Setup
- **Links:** Oracle Connection Manager Architecture, Oracle Client Installation Guide
- **Keywords:** JDBC, Net_SERVICE_ALIAS, PORT, DBNAME, Oracle Client

## Upgraded Environment Functionalities

### Post-Upgrade Functionalities and Health Checks
- **Component:** All Guardium version upgrades
- **Constraint:** Some features unavailable until all systems upgraded
- **Workflows:** Upgrade All Systems, Apply Health Check Patch
- **Links:** Guardium Upgrade Paths, Health Check Mechanism
- **Keywords:** Upgrade, Central Manager, Health Check Patch

## Health Check Patch Application

### Application of Health Check Patches
- **Component:** Central Managers running Guardium
- **Constraint:** Requires CLI access
- **Workflows:** Apply Patch, Verify Health Checks
- **Links:** Guardium Patch Management, Health Check Process
- **Keywords:** health_check, CLI, Patch Management, Command Guardium CLI

## GUI Security and XSRF

### GUI Security and XSRF Configuration
- **Component:** All Guardium installations with GUI access
- **Constraint:** Requires administrative privileges
- **Workflows:** Set GUI Security, Set XSRF Status
- **Links:** Web Interface Security, XSRF Prevention
- **Keywords:** GUI Properties, STAP_EXCLUDE_IP, XSRF, GUI Security

## Query Rewrite WHERE Condition API

### WHERE Condition API for Query Rewrite
- **Component:** Supports Guardium v10.1.4 and later
- **Workflows:** Add Condition, Query Optimization
- **Links:** Query Rewrite Mechanism, API Integration
- **Keywords:** Query Rewrite API, WHERE Condition, Query Optimization

## TRANSFORM Actions Handling

### Special Handling for TRANSFORM Actions
- **Component:** Guardium systems handling query rewrite
- **Constraint:** SERVICE_NAME not recommended for session-level policies
- **Workflows:** Policy Rules, Session Anomalies
- **Links:** Query Rewrite Strategies, Session Management
- **Keywords:** TRANSFORM Actions, DB_TYPE, SERVICE_NAME, Policy Rules

## Unexpected Database Connections Rule

### Detection of Unexpected Database Connections
- **Component:** All Guardium-supported database types
- **Constraint:** Requires Guardium V11.0 or later
- **Workflows:** Detect Unauthorized Access, Unauthorized Database Access Reports
- **Links:** Database Connection Anomalies, Scoring System
- **Keywords:** AUTH_SEVER_TYPE, Connection Types, Unexpected Connect, Suspicious Activity

## 854. Special handling for TRANSFORM actions

### Dynamic Port Detection
- **Component:** Guardium 11.x, 12.x
- **Constraint:** Requires Valid API token; not applicable for Syntax API versions prior to 10.0
- **Workflows:** Build Alert Rule, Launch Alerts Dashboard
- **Links:** Compliance Monitoring, API Gateway, Notification Framework
- **Keywords:** TRANSFORM, ALERT, Notification, Policy Builder

## Datasource Connectivity

### Configure Port Monitoring with S-TAP
- **Components:** IBM i, Informix, MSSQL, Oracle, PostgreSQL, Sybase, Teradata, DB2
- **Limitations:** Requires S-TAP 10.1 or later; network‑port‑to‑local‑port forwarding not supported on Informix and Sybase
- **Workflows:** Define Port Range; Map Network Port to Local Port  

---

## 887. Out of Scope for Guardium Monitoring

### Dynamic Port Detection
- **Components:** Windows Services, Linux Daemons
- **Limitations:** Requires valid resmon.ini configuration; no monitoring for non‑standard custom services
- **Workflows:** Set resmon.ini; Verify Active Services  

---  

## 888. Port Scanner

### Dynamic Port Detection
- **Components:** All supported platforms
- **Limitations:** Limited UDP/TCP port range in non‑privileged mode; ICMP status not reliable
- **Workflows:** Verify Port  

---  

## 889. Protocol Detector

### Dynamic Port Detection
- **Components:** SQL, NoSQL, LDAP, HTTP, SSL/TLS
- **Limitations:** Accuracy depends on default signature sets; custom signatures required for proprietary protocols
- **Workflows:** Enable Protocol De

# Guardium Features and Configurations

## Identify Unmonitored Services
- Use the Protocol Analyzer and Signature Set to detect unmonitored services and applications on the network.

## Load Balancer Configuration
- Supported on all Guardium appliances with no limitations.
- Configured via Configuration → Load Balancer Settings.

## grdapi apply_rules_on_discoveredinstances Troubleshooting
- Must be run on the primary host for managed S-TAP units.
- Troubleshooting workflow includes Configuration → Apply Rules and Troubleshooting → API Execution.

## Transform Action Frequency Assessment
- Supported on all Guardium installations.
- Requires Rule Activation logs and is used for Configuration → Rule Analysis and Reporting → Rule Frequency.

## Detect Clear-Text Passwords
- Available on all Guardium Data Protection versions.
- Requires network traffic monitoring and is configured under Configuration → Security Settings with alerts for clear-text detection.

## Oracle Data Join Workflow
- Applicable to Oracle databases.
- Requires external source connectivity for Configuration → Data Correlation and Integration → External Sources.

## Oracle DB User Activity Report
- Supported on all Guardium installations with Oracle.
- Generates hourly reports under Reporting → User Activity.

## Report Customization and Navigation
- Available on all Guardium installations.
- Allows Configuration → Report Settings and Navigation → Drill-Down.

## Assessment Log Attributes and Severity
- Supported on all Guardium installations.
- Requires Assessment Log TypePredefined entity and is used for Configuration → Assessment Settings and Analysis → Severity Interpretation.

## CPU Monitoring and Analysis
- Available on all Guardium installations.
- Requires monitoring configuration for Monitoring → CPU Usage and Analysis → Performance Metrics.

## Entitlement Reports
- Use the packaged .tgz file from the releases directory.
- Requires a product key and is configured under Installation → Import .tgz and Configuration → Enable Entitlement Reports.

## Licensing and Licenses
- Available on all Guardium products.
- Monitors license usage under Monitoring → License Usage and Configuration → License Management.

## Roles and Permissions
- Available in Guardium versions 11.5 and higher.
- Requires admin role and is managed under Security → API Key Management.

## Database Interaction
- Supported on all Guardium versions.
- Requires root user permissions for Configuration → Environment Variables and Debugging → Database Settings.

### Dynamic Trust Level Scoring
- **Components:**
  - **Support Matrix:** All supported Guardium rule types
  - **Limitations/Constraints:** Initial encounter rule cannot set a trust level
  - **Workflows with different types:** Configuration — Rule Management; Navigation — Session Reports
- **Links:**
  - **Knowledge:** Session Reporting, Rule-Based Trust Scoring
  - **Keywords:** Trust Level, Score Threshold, Automated Alert, Suspicious Activity

### SQL Injection Detection
### Volume and Type Assessment
- **Components:**
  - **Support Matrix:** All Guardium policy violation logs
  - **Limitations/Constraints:** Requires historical data for comparison
  - **Workflows with different types:** Configuration — Policy Management; Navigation — Report Analysis
- **Links:**
  - **Knowledge:** Risk Assessment, Threat Severity
  - **Keywords:** Policy Violation, Volume Analysis, Risk Gauge, SQL Injection Threat

### Oracle Data Source Reporting
### Version History Integration
- **Components:**
  - **Support Matrix:** All Oracle data sources in Guardium
  - **Limitations/Constraints:** Requires integration with version control systems

## Guardium Modeling and Versioning
**Components:** Guardium hosts  
**Workflows:** System Setup → Attribute View  
**Links:** System Identification, Compliance Management  

## Session Lifecycle Interpretation
**Components:** All session types in Guardium  
**Workflows:** Session Management → Session Details  
**Links:** Session Monitoring, Lifecycle Interpretation  

## Session Time Zone Challenges
**Components:** Oracle session data  
**Workflows:** Time Zone Adjustment → Session Records  
**Links:** Time Zone Handling, Oracle Sessions  

## CPU Extraction Scheduling
**Components:** Guardium data mart bundles  
**Workflows:** Data Mart Management → Extraction Reports  
**Links:** Data Mart Extraction, Latest Extracts Inclusion  

## IMS Object Entity Attributes
**Components:** IMS environments with CAS  
**Workflows:** Entity Setup → Database Management  
**Links:** Entity Differentiation, Reporting  

## CAS Host Management
**Components:** CAS configurations in Guardium  
**Workflows:** Host Management → API Access  
**Links:** External Management, Role-Based Access  

## Datasource Connectivity
### SQL Server 2019 Dynamic Port Detection
**Components:** SQL Server 2019  
**Workflows:** Add Datasource → View Ports  
**Links:** Database Connection Architecture, Browser Service  

### CyberArk Credential Integration
**Components:** Guardium-supported databases  
**Workflows:** Install CyberArk SDK → Credential Vault Management  
**Links:** Credential Management, Dynamic Secrets  

## Default LDAP Authentication Parameters
**Categories:** Features, Keywords  



This compressed version retains each distinct concept while eliminating redundancy and extraneous details, adhering to the provided guidelines.

## Client Web Certificates

### Overview
- All supported Guardium versions; no limitations; workflows: Install Certificates, View Certificates
- Related to SSL/TLS Configuration, Certificate Management; client certificates, SSL, security, trusted hosts

## Encrypt Parameter Values for Security

### Components
- GuardAPI environments requiring encrypted parameters
- Requires matching key and system’s shared secret
- Workflows: Set Shared Secret, Run encrypt_value

### Links
- Security Best Practices, API Authentication
- Parameter Encryption, Shared Secret, API Key, GuardAPI

## Manage Catalog Entries

### Components
- All Guardium instances with catalog functionality
- Requires permissions; file must exist for delete_entry_location
- Workflows: Add Entry, Remove Mapping

### Links
- Catalog Management, Reporting Framework
- delete_ef_mapping, delete_entry_location, ReportName, File Management

## Utilize Session-Level Policy Examples

### Components
- Guardium UI, SR language programmers
- No limitations; workflows: Session Policies, Policy Examples training

### Links
- Policy Configuration, SR Language Reference
- Transform Actions, Policy Examples, SR Language, Guardium UI

## View Advanced Policy Rule Options

### Components
- Versions supporting advanced rule options
- Require clicking “Show advanced options”
- Workflows: Create Rules, Clone Rules

### Links
- Rule Management, Policy Auditing
- Log Rules, Audit Trail, Rule Ribbon, Advanced Options

## Oracle Dashboard Management

### Components
- Oracle Guardium instances
- Requires role permissions for dashboard access
- Workflows: Create Dashboard, Investigate Data

### Links
- Oracle Integration, Reporting Tools
- Dashboards, Reports, Investigate Dashboard, Report Access

## Deploy Configuration Auditing System

### Components
- Linux/UNIX and Windows servers
- Requires CAS prerequisites; .tgz file from releases directory
- Workflows: Deploy CAS, CAS Setup

### Links
- CAS Documentation, Operating System Compatibility
- CAS Installation, Configuration Auditing System, Linux/UNIX, Windows, Releases Directory

## License Monitoring Feature (v12.2+)

### Components
- Guardium v12.2 and later
- Periodic evaluations limited to selected units
- Workflows: Weekly Checks, License Alerts

### Links
- License Management, Security Governance
- License Count, Periodic Evaluations, Deviation Identification, Security Metrics

## License Dashboard Metrics

### Components
- All versions with dashboard functionality
- No limitations; workflows: License Usage, License Thresholds alerts

### Links
- Dashboard Customization, Security Operations
- License Usage, Alerting, Security Governance

# License Metrics 

## Verify API Key Exists 

# Custom Evaluation Report 

# Namespace for Cloud Pak for Data 

# Number Sign Listener 

# Number Sign API Call 

# Oracle Web Client Certificate 

# Client Web Certificate for Appliance and Self-Managed 

# Oracle Custom Report JAR Integration

## Datasource Connectivity

### Oracle Encrypted Traffic Capture
- **Components:** Oracle Database 11gR2 and later
- **Limitations:** Requires Oracle Net Services SSL/TLS; no TDE key lookups
- **Workflows:** Configuration – Enable SSL for Oracle; Navigation – View Traffic Details
- **Links:** Oracle Net Services, SSL Configuration, Data Encryption
- **Keywords:** Oracle SSL, Encrypted Traffic, Db Traffic, Net Services

### FIPS Mode Configuration
- **Components:** Guardium 12.0 and later
- **Limitations:** Configure during installation; reinstallation required for later changes
- **Workflows:** Configuration – Install Guardium; Post-Installation – Validate FIPS Mode
- **Links:** FIPS 140-2, Security Hardening, Installation Best Practices
- **Keywords:** FIPS Mode, Security Policy, Appliance Reinstall, Compliance

### Load Balancing and Data Handling
- **Components:** All Guardium-supported databases
- **Limitations:** Requires Collector High Availability; in-memory cached data not redistributed
- **Workflows:** Configuration – Load Balancing Settings; Performance – Tune Data Collection
- **Links:** High Availability, Performance Tuning, Data Streams
- **Keywords:** Collector HA, Load Balancing, Data Stream Optimization, Performance Metrics

### Federated Guardium Configuration
- **Components:** Guardium 11.0 and later
- **Limitations:** Central manager on dedicated appliance; identical software versions on managed units
- **Workflows:** Configuration – Federated Setup; System Management – Execute CLI Commands
- **Links:** Centralized Management, Managed Units, CLI Administration
- **Keywords:** Federated Guardium, Central Manager, Managed Units, CLI Commands

### Cloud Storage Datasource Configuration
- **Components:** FTP, Amazon S3, IBM COS (Guardium 12.1 and later)
- **Limitations:** Requires valid credentials and network access; path formats vary by provider
- **Workflows:** Configuration – Add Datasource; Navigation – Manage Datasources
- **Links:** Cloud Integration, Datasource Setup, Storage Networking
- **Keywords:** Datasource, Cloud Storage, FTP Path, Amazon S3, IBM COS

### Hierarchical Group Flattening
- **Components:** Guardium V9.5 and later
- **Limitations:** Only flattens hierarchical relationships; requires system downtime
- **Workflows:** Administration – Flatten Groups; Data Management – Group Management
- **Links:** Group Hierarchies, Data Organization, Administrative APIs
- **Keywords:** Flatten Hierarchical Groups, Child Groups, Parent Group, API Execution

### Policy Rule Actions
- **Components:** All Guardium releases
- **Limitations:** Actions cannot be changed after rule creation; requires full policy rebuild
- **Workflows:** [Incomplete – additional workflow details needed]

## Guardium Features and Configurations

### Workflows and Rule Configuration
- **Components:** Policy Management, Rule Configuration
- **Links:** Data Access Policies, Rule Actions, Security Policy Management

### Traffic Pattern Analysis
- **Components:** Regular expression evaluation for Traffic Analysis
- **Limitations:** Performance impact, requires regex expertise
- **Links:** Data Pattern Recognition, Regular Expressions, Traffic Monitoring

### Transform Actions
- **Components:** Transform Actions, Audit Transform Rules
- **Limitations:** Requires predefined rules, no encryption support
- **Links:** SQL Verb Usage, Audit Configuration

### Oracle User Timestamp Reporting
- **Components:** Oracle Audit Trail Reports
- **Limitations:** 30-day purge, requires audit trail retention
- **Links:** Oracle Audit Trail, User Management

### SQL Verb Reporting
- **Components:** SQL Verb Audit Reports
- **Links:** Command Auditing, Periodic Reporting

### Session Aggregation and Summarization
- **Components:** Session Count Reports
- **Limitations:** Increased processing time, requires unique identifiers
- **Links:** Session Auditing, Report Optimization

### Session Entity Tracking
- **Components:** Session Entity, Client-Server Interaction
- **Links:** Data Sessions, Monitoring Capabilities

### License Tracking
- **Components:** License Count Reports
- **Links:** License Management, Subscription Models

### Selective Audit
- **Components:** Selective Audit Rules
- **Links:** Network Traffic Optimization, Security Policies

### Audit-Delete Accountability
- **Components:** Audit-Delete Role, Deletion Activities
- **Links:** User Roles, Audit Trail

### S-TAP Agent Shell Upgrade
- **Components:** KTAP Update, Shell Upgrade Workflow
- **Links:** S-TAP Installation, Live Upgrade

### Web Certificate Configuration
- **Components:** Client Web Certificates
- **Links:** Client Web Certificates, Security Configuration

## Knowledge Base Summary

### Guardium Data Protection
- **Investigation Dashboard:** Configurable feature requiring system settings enablement. Supports data visualization and dashboard configuration.
- **API Endpoint:** Disables Risk Spotter; requires admin-level API key (Guardium API v1.2+).
- **Archive Storage:** Configurable with S3, FTP, SCP, Azure Blob. FTP requires passive mode. Configured via protocol selection and connection testing.

### Clustering & Monitoring
- **Clustering Engine:** Reassigns user scores during scheduled maintenance windows in all clustering environments.
- **Unit Utilization Levels:** Configurable schedules for Guardium Central Manager and standalone environments; requires specific access permissions.

### Security & Integration
- **Close Firewall Parameter:** Configurable via policy rule actions (value 0-10).
- **Data Source Import:** Supports Data Direct driver; substitute if unavailable (versions 10.5+).
- **F5 Big-IP ASM Integration:** Requires shared SSL certificates. Configured through identity propagation handling.

### Database Management
- **Oracle Feature Reference:** Covers OpenSSL connections, listener job status, license tracking, user-DB associations, policy installation monitoring.
- **FPolicy Configuration:** Setup for Hitachi devices via CLI commands, including firewall permissions.

### Additional Notes
- All entries require specific system access permissions and may have particular configuration steps or limitations.

## Guardium Feature Reference

**10xx. Guardium Data Privacy Features**

- **1020. chgroup users=informix guardium**
  - Supports all Guardium platforms (Linux, Unix, Windows).
  - Requires Informix client tools; used for user management configuration.

- **1021. Teradata Exit vs K-TAP**
  - Compatible with Guardium S-TAP 11.x+ on Teradata 15.x+.
  - K-TAP unnecessary if only Teradata is monitored; affects performance tuning.

- **1022. Set Cloud Pak for Data Namespace**
  - Applicable to IBM Cloud Pak for Data 3.x+.
  - Database host must be reachable from Guardium collector for external S-TAP configuration.

- **1023. Kubernetes Ingress Annotations (Optional)**
  - For Kubernetes with Guardium API management.
  - Not applicable outside Kubernetes environments.

- **1024. CLI Flag for Static Data Export**
  - Supported on Guardium 12.2+ for CLI operations.
  - Sets `next_export_static` flag; used in static export monitoring.

- **1025. Client Web Certificates Configuration**
  - Requires Guardium 12.0 CP1+ and valid certificates.
  - Enables outliers detection workflows with central managers.

- **1026. Oracle Exception Example**
  - Applies to Oracle 11gR2+.
  - Handles specific exception types based on database conditions for reporting.

- **1027. Skip Registry Certificate on Cluster Nodes (Optional)**
  - For Guardium 12.0 CP1+ on Kubernetes.
  - Skips registry certificate installation for selected features.

- **1028. Verify API Key**
  - For Guardium 12.0+.
  - Ensures API key validity and proper configuration for security.

### Guardium Feature Reference

- **1029. Optional Annotations for Ingress**
  - Not applicable; requires network agents.
  - Configures ingress annotations for network connectivity.

- **1030. Oracle Object_Join Example**
  - For Oracle databases.
  - Provides example SQL for object join reporting.

- **1031. Guardium Db2 for i S-TAP Related Tasks**
  - Supports IBM Db2 for i with S-TAP installed.
  - Generates activity reports for compliance.

- **1032. Configure Client Web Certificates**
  - Applies to all supported Guardium appliances.
  - Configures valid client web certificates for secure web interactions.

## TAPs - i-S-TAP

### Dynamic Port Detection
- **Support Matrix:** MySQL 5.0‑5.1, MySQL 6.0
- **Limitations/Constraints:** Not supported on MySQL 5.7+, MariaDB, limited to information‑schema query
- **Workflows with different types:** Configuration — Add Datasource; Navigation — View Ports
- **Knowledge:** Database Connection Architecture, Browser Service
- **Keywords:** S-TAP, Collector, JDBC, Browser Service

### Health Analyzer APIs
- **Support Matrix:** Guardium 11.0 and later
- **Limitations/Constraints:** Requires system‑monitoring role
- **Workflows with different types:** Configuration — Enable Disk Monitoring; Configuration — Enable Database Monitoring
- **Knowledge:** Proactive Monitoring, Thresholds and Alerts
- **Keywords:** Health Analyzer, Disk Health, DB Health

### CPU
- **Support Matrix:** All Guardium‑supported platforms (Linux, Solaris, HP‑UX, AIX, Windows)
- **Limitations/Constraints:** None documented
- **Workflows with different types:** Monitoring — System Health; Configuration — Enable CPU Metrics
- **Knowledge:** System Performance, Resource Utilization
- **Keywords:** CPU Utilization, Guardium Agent, Performance Dashboard

### Verify API Key Exists
- **Support Matrix:** Guardium REST API
- **Limitations/Constraints:** Key must be generated in GUI; API‑only creation unsupported
- **Workflows with different types:** Administration — API Key Management; Configuration — Enable API Access
- **Knowledge:** REST API Authentication, Security Tokens
- **Keywords:** API Key, Verify, Admin Portal, GuardAPI

## Number Sign (Command‑line tools)

### Number Sign
- **Support Matrix:** Linux/Unix command line
- **Limitations/Constraints:** Requires guardctl binary; not available on Windows
- **Workflows with different types:** Security — List i‑S‑TAP Functions; Security — Restart i‑S‑TAP Functions; Security — Set i‑S‑TAP Functions
- **Knowledge:** Guardctl Utility, CLI Administration
- **Keywords:** guardctl, i‑S‑TAP, Function Management

## Guardium Data Protection Features

### Oracle Example
- **Support:** GIM 3.0 and later; GIM agent required on managed module
- **Workflows:** View GIM Modules; Schedule Module Actions
- **Knowledge:** GIM Module Lifecycle, Module Status Reporting
- **Keywords:** GIM Modules Heartbeats, Scheduled Actions

### Configure Client Web Certificates
- **Support:** Any browser supporting HTTPS; Guardium GUI
- **Limitations:** Root CA must be imported into Guardium trust store
- **Workflows:** Security Settings; Import Certificates
- **Knowledge:** HTTPS Configuration, SSL/TLS, Trust Store

### grdapi gim_get_modules_running_status
- **Support:** Guardium V9.5 or later
- **Workflow:** Diagnostic — Check Running Modules
- **Knowledge:** Guardium Module Architecture, System Health Checks
- **Keywords:** gim_get_modules_running_status, API, Diagnostic

### Guardium Cloud Pak for Data Namespace
- **Support:** Guardium Integrated Cloud; requires Cloud Pak instance ID
- **Workflow:** Configuration — Set Cloud Pak Namespace
- **Knowledge:** Cloud Pak Integration, Namespace Management
- **Keywords:** Namespace, Cloud Pak, f8122424-4e5e-4265-a217-1e96209e05af

### External S-TAP npipe Configuration
- **Support:** S-TAP 8.3 or later; all Guardium-supported databases
- **Limitations:** npipe URL must point to valid pipe
- **Workflow:** Configuration — External S-TAP Settings
- **Knowledge:** S-TAP Configuration, External S-TAP Communication
- **Keywords:** npipe, External S-TAP

### grdapi delete_data_params
- **Support:** Guardium V12.2 or later
- **Limitations:** fips_go auto restarts S-TAP; compatibility_check needs central manager
- **Workflow:** Configuration — FIPS Settings
- **Knowledge:** FIPS Mode Management, Guardium Cluster Management
- **Keywords:** delete_data_params, fips_go, auto_restart, version check

### grdapi create_fam_rule
- **Support:** Guardium 12.x and later for Windows and Unix/Linux
- **Limitations:** Scanner must be initialized and enabled
- **Workflows:** FAM Rule Setup, Scanner — FAM Crawler
- **Knowledge:** File Activity Monitoring, Policy Management
- **Keywords:** fam_actions, fam_notifies, FAM Policy

### Guardium Vulnerability Assessment
- **Support:** Production and nonproduction; proper entitlement required
- **Workflow:** Assessment — Vulnerability Scan
- **Knowledge:** Vulnerability Management, Entitlement Models
- **Keywords:** Vulnerability Assessment, entitlements, production use

### Managed Scanners for Production Environments
- **Support:** Guardium Data Protection deployed via SaaS
- **Limitations:** Central manager scanner cannot be used for production
- **Workflow:** Workflow — Scan Planning
- **Knowledge:** Guardium Data Protection Deployment, Scanner Management
- **Keywords:** Keystore, Scanner Pods

### FAM Scanner Troubleshooting
- **Support:** All Guardium-supported scanners
- **Limitations:** Requires correct server and scanner connections
- **Workflow:** Troubleshooting — Connectivity Issues
- **Knowledge:** FAM Scanner Configuration
- **Keywords:** scanners entity, connectivity issues

### Windows File Activity Policy Scan
- **Support:** Guardium 12.x and later
- **Limitations:** Requires registered Windows server with file agent enabled
- **Workflow:** Configuration — FAM Windows Scan
- **Knowledge:** File Activity Policy Configuration
- **Keywords:** Windows Scan, file agent

### Guardium Cold Catalog Schema for Iceberg Tables
- **Support:** Guardium V12.2 or later
- **Limitations:** Trust store usage optional for TLS
- **Workflow:** Configuration — Cold Catalog Setup
- **Knowledge:** Data Retention Policies, Iceberg Table Management
- **Keywords:** cold_catalog_protocol, schema_iceberg_json, Iceberg tables

### System Static Reports Command
- **Support:** Guardium V1.4 or later
- **Workflow:** Reporting — Static Reports
- **Knowledge:** Reporting Innovations, Static Data Handling
- **Keywords:** System Static Reports, reporting feature

### Guardium Policy Session-level Actions
- **Support:** All Guardium-supported databases
- **Workflow:** Policy — Create Rule
- **Knowledge:** Policy Rule Functions, Security Configuration
- **Keywords:** session_level

## l_policy

- **Description:** Manages Linux policy configuration for Guardium.
- **Support Matrix:** Guardium 11.3 and later.
- **Capabilities:** Supports rule-based packet validation and security actions.
- **Usage:** Set policies, configure validation rules, define actions (e.g., alert, block).

## Validate Packets

- **Description:** Validates network packets against configured security policies.
- **Support Matrix:** Guardium 11.3 and later.
- **Configuration:** Use `l_policy` to define validation criteria.
- **Actions:** Alerts or blocks packets that do not comply with policies.

## Security Actions

- **Description:** Configurable actions taken when packets violate security policies.
- **Support Matrix:** Guardium 11.3 and later.
- **Types of Actions:**
  - **Alert:** Generates an alert for violation.
  - **Block:** Blocks the packet from further processing.
  - **Log:** Logs the violation for audit purposes.
- **Configuration:** Define actions in `l_policy` under respective rule sets.

## Incremental Configuration

### Clone Policy and Filter Configuration Parameters
- **Components:**
  - **Support Matrix:** All Guardium versions supporting cloning
  - **Limitations/Constraints:** Requires 'clone' configuration setting
  - **Workflows with different types:** Configuration — Clone Settings
- **Links:**
  - **Knowledge:** Clone Settings, Policy Management

The incremental configuration parameter `clone` determines whether Guardium includes all child objects of a policy or filter when cloning. If set to **0**, Guardium clones only the specified policy; if set to **1**, it includes all child objects.

### Required Initialization for External Build Scripts
- **Components:**
  - **Support Matrix:** All Guardium versions supporting external builds
  - **Limitations/Constraints:** Must be placed in the specified directory
  - **Workflows with different types:** Build Configuration — Initialize Scripts
- **Links:**
  - **Knowledge:** Build Script Directory, External Builds

To use a custom build script, the script file must be placed in the Guardium installation directory. This path ensures that the Guardium build process recognizes and executes the script during system initialization and updates.

## Authorization Management

### MongoDB Path Permission Configuration
- **Components:** MongoDB 4.0+, dynamic and static roles/credentials
- **Support Matrix:** All Guardium deployments
- **Limitations:** Requires specific path permissions
- **Workflows:** Security - Set Permissions
- **Links:** Knowledge: Path Permissions; Keywords: MongoDB, static and dynamic roles/credentials

## Datasource Connectivity

### MongoDB Dynamic Port Detection
- **Components:** MongoDB
- **Support Matrix:** All non-z/OS environments
- **Limitations:** Requires browser service running
- **Workflows:** Configuration - Grant Read and List Capabilities, Navigation - View Ports
- **Links:** Knowledge: Database Connection Architecture; Keywords: Dynamic Port Detection

## System Log Configuration

### Guardium Log Management
- **Components:** All Guardium appliances
- **Limitations:** Log rotation limits by system resources
- **Workflows:** Administration - Configure Logs
- **Links:** Knowledge: Log Rotation; Keywords: logrotate, Guardium

## Auto-Scaling Configuration

### Kubernetes Auto-Scaling
- **Components:** Kubernetes environments
- **Limitations:** Requires Kubernetes API access
- **Workflows:** Configuration - Enable Auto-Scaling; Set Min/Max Replicas
- **Links:** Knowledge: Kubernetes, Replicas; Keywords: Auto-Scaling, MinReplicas, MaxReplicas

## Database Connectivity & Management

### Oracle PI Command Execution
- **Components:** Oracle databases
- **Support Matrix:** All Oracle versions
- **Limitations:** Requires GuardAPI syntax; uses password and stapHost for secure connections
- **Workflows:** Configuration - Run PI Command
- **Links:** Knowledge: GuardAPI Syntax; Keywords: Guardium, Oracle, GuardAPI

### Guardium REST API Custom Data Management
- **Components:** Guardium 11.3+
- **Limitations:** tableName parameter mandatory
- **Workflows:** Configuration - Manage Custom Data
- **Links:** Knowledge: REST API; Keywords: Guardium RE

## Database Security Management

### Datasource Connectivity
- **Components:** SQL Server, Oracle, Db2, MySQL, PostgreSQL, SAP HANA
- **Requirements:** Network connectivity between Guardium and target databases; TLS/SSL encryption mandatory for PostgreSQL and SQL Server
- **Workflows:** Add Datasource; View Active Sessions
- **Architecture:** S-TAP, Collector, JDBC, Thin Client, Connection Pooling

### Assessment Automation
- **Platforms:** All Guardium-supported platforms
- **Requirements:** Valid Guardium assessment engine
- **Workflows:** Create Assessment; Run Assessment; Generate Report
- **Concepts:** Assessment Lifecycle, Test Design, Result Analysis

### User and Role Management
- **Platforms:** All Guardium deployments
- **Privileges:** Administrative for role hierarchy changes
- **Workflows:** Create User; Assign Role; Review Permissions
- **Concepts:** Privileged Access Management, Role-Based Access Control

### OAuth Integration
- **Version:** Guardium V10.6 and later
- **Workflows:** Register OAuth Client; Generate Token; Define Scopes
- **Standards:** OAuth 2.0 Specification, Token Lifecycles, Scope Management

### Policy Lifecycle Operations
- **Version:** Guardium V11.0 and newer
- **Requirements:** Validated policy syntax; Active S-TAP agents
- **Workflows:** Create Policy; Validate Policy; Install Policy; Update Policy
- **Concepts:** Security Policy Framework, Rule Evaluation, Compliance Standards

### Cloud Datasource Management
- **Platforms:** Amazon RDS, Azure SQL Database, Google Cloud SQL
- **Requirements:** [Content truncated, original has truncation point here]

# Guardium Cloud Data Sources
The Guardium Cloud Access module adds workflows for integrating, streaming, and monitoring cloud data sources.

## Catalog Entity Management
Manage catalog entities: create, archive, and retrieve with search optimization.

## Alerter Functionality
Configure alerts, set thresholds, and define automated response actions.

## Universal Connector Export Profiles API
POST `/restAPI/universal_connector_export_profiles` to manage export profiles.

## API Summary Parameters
GET `/restAPI/api_summary` includes `maxResultsNum`, `summarySortedBy`, and `timeResolution`.

## API Parameter Options
GET `/restAPI/parameter_options` returns valid options for API calls.

## Automated Vulnerability Scanning
Security workflows for vulnerability scans on supported databases.

## Audit and Data Mapping APIs
Create audits and map parameters to integrate compliance data.

## Populate Members for Group API
GET `/restAPI/populateMembersForGroup` with `cronString` for scheduling.

## Update Rule Command Parameters
POST `/restAPI/update_rule` to customize rule parameters.

## Hadoop and Apache Ranger Integration
POST `/restAPI/hadoop_ranger_commands` for security and data access control.

## Network Traffic Rules
Configure network monitoring rules; requires browser service.

## Updated DML Monitoring
Reports executed DMLs on sensitive objects across supported databases.

## GuardAPI Execution
**Reset Unit Utilization Data Command**  
Supports Guardium v12.2.2+. Requires `hostName` and `resetDate` parameters. Resets utilization metrics via Configuration or API workflows.

## Rule Configuration  
**Advanced Update Rule Parameters**  
Works across all supported platforms. Requires concurrency control and transaction management. Configured via Configuration workflows.

## Firewall Configuration  
**UNIX and Windows Firewall Settings**  
Unified across Guardium. No changes needed if defaults remain. Configured via Configuration workflows.

## Risk Scoring  
**Risk Assessment Parameters**  
Supported by versions with `riskspotter_set_config` API. Configured via Configuration or API workflows.

## Datasource Configuration  
**Custom Datasource Parameters**  
All datasources supported. Severity values via `--help=true`. Managed via Configuration or API workflows.

## Sensitive Object Detection  
**Outlier Detection Sensitive Groups Command**  
All supported outlier algorithms. Requires technical steps. Configured via Reports or API workflows.

## Data Access and Security  
**Restart Data Compliance Services via API**  
Guardium 11.x+. Requires `API_TOKEN`. Not for pre-11.0. Managed via POST /guardium/restAPI/restart_compliance.

**RBAC Role Assignment API**  
Guardium 10.6+. Needs `member_of_user_roles` permission. Roles comma-delimited. Managed via POST /guardium/rest/v1/user_roles.

## Guard Sender Monitor Troubleshooting  
Applicable to all Guardium versions. No relevance to S-TAP. Managed via troubleshooting workflows.

## MongoDB Atlas Credential API  
Guardium 11.3+. Requires IBM Key Protect vaults. Managed via POST /guardium/rest/v2/mongodb/atlas/credentials.

## Hostname and IP Mode Consistency  
All Grid environments. No special constraints. Managed via System Settings navigation.

## set_certificate_host_validation GuardAPI  
Guardium V10.6+. Requires admin role. Managed via grdapi set_certificate_host_validation enable=true.

## Security and Data Transmission Parameters  
Unix Guardium appliances. No constraints. Managed via configuration workflows.

## API Configuration

### API Target Host Parameter
- **Components:** REST API endpoints of Guardium Universal Connector
- **Limitations/Constraints:** IP mode must match `api_target_host` value
- **Workflows:** Configuration — API Setup; Navigation — API Documentation
- **Links:** Knowledge — REST API Architecture, Host Naming Conventions  
  **Keywords:** `api_target_host`, IP Addressing Modes, Universal Connector API

## Limitations/Constraints ###

Requires ``calculateConfidenceScore`` parameter  
REST API — ``update_classifier_document_rule`` workflow

## Report Title ###

`98484261-3873-4955-9d37-5e91e728671d` | **categories:** features, entities  
- **Support Matrix:** Guardium File Activity Monitor  
- **Limitations/Constraints:** None  
- **Workflows with different types:** File Activity Monitor Management

## Report Title ###

`1499a596-e733-48a0-af3f-880bebc9e39c` | **categories:** features, entities, keywords  
- **Support Matrix:** Risk Management in Guardium  
- **Limitations/Constraints:** None  
- **Workflows with different types:** Risk Assessment Workflow

## Report Title ###

`824772fd-e129-4d3d-ad5f-59645155cd5a` | **categories:** features, entities  
- **Support Matrix:** Guardium API  
- **Limitations/Constraints:** None  
- **Workflows with different types:** API Integration — Report Creation

## Modify Guardium Parameters ###

**Support Matrix:** All Guardium‑supported databases  
**Limitations/Constraints:** Requires connection to Guardium Central Manager  
**Workflows with different types:** Configuration — Modify Parameter, Automation — Scheduled Jobs

## REST API Usage ###

**Support Matrix:** Guardium v11.3 and later  
**Limitations/Constraints:** Requires API access privileges  
**Workflows with different types:** Configuration — API Invocation, Monitoring — REST Calls

## S‑TAP Agent Management ###

**Support Matrix:** Guardium v9.5 and later  
**Limitations/Constraints:** Requires suitable user permissions  
**Workflows with different types:** Troubleshooting — Agent Restart, System Management — Agent Control

## OAuth Token Revocation ###

**Support Matrix:** Guardium OAuth Integration  
**Limitations/Constraints:** Requires token validity checks  
**Workflows with different types:** Security — Token Invalidation, Configuration — OAuth Setup

## Basel II Compliance Reports ###

**Support Matrix:** All Guardium‑supported databases  
**Limitations/Constraints:** None  
**Workflows with different types:** Navigation — Basel II Compliance Reports

## ALERT_VERB_NUM_LIMIT ###

**Support Matrix:** All Guardium‑supported systems  
**Limitations/Constraints:** Valid values 1‑50, default 10  
**Workflows with different types:** Configuration — Alert Management

## Register Internal OAuth Client ###

**Support Matrix:** Guardium REST API  
**Limitations/Constraints:** Requires ``getEncrypted`` and ``grant_types`` parameters  
**Workflows with different types:** Configuration — OAuth Registration

## Test Solr Hardware Requirements ###

**Support Matrix:** Guardium API  
**Limitations/Constraints:** None  
**Workflows with different types:** Configuration — Solr Setup

## Auto‑Commit Control ###

**Support Matrix:** All supported databases  
**Limitations/Constraints:** Requires value 0 or 1  
**Workflows with different types:** Configuration — Replay Setup

## Update Catalog Entry Locations ###

**Support Matrix:** Guardium version 9.5 or later  
**Limitations/Constraints:** None  
**Workflows with different types:** Configuration — Catalog Update

## Mass Update STAP Configuration ###

## Guardium Technical Reference

### STAP Settings
**Components:** All Guardium-supported systems; no limitations.  
**Configuration workflow:** STAP Management.  
**Related knowledge areas:** Guardium API, STAP Settings, Host Management.

### Data Reporting and Management
**REST API response:** JSON format; requires credentials and is incompatible with native DB views.  
**Intended workflows:** API integration, data retrieval; debugging and log inspection.  
**Related knowledge areas:** Data Serialization, JSON Schema, REST Principles.

### Configuration Management
**Customize CAS template workflow:** enable_cas, view CAS status.  
**Related knowledge areas:** CAS Framework, Security Templating.

### Update Custom Table from LDAP
**Required version:** Guardium 11.2+.  
**Related knowledge areas:** REST API Usage, Custom Table Management, LDAP Integration.

### Guardium Datasource Group Update
**Metadata impact:** Only metadata updated; no member data sources modified.  
**Related knowledge areas:** API Syntax, Group Attributes, Asset Scanning Basics.

### Asset Discovery and Scanning Constraints
**Key limitation:** No data source list → no asset connections; without Guardium integration → only network port scans.  
**Related knowledge areas:** Asset Discovery Methods, Guardium Integration Points.

### Basel II Compliance Reports
**Limitation:** Static report definitions; customization requires policy changes.  
**Related knowledge areas:** Financial Regulations, Basel II Framework.

### Supported Platform Types for Inspection Engines
**Insight:** Platform type determines compatible engines.  
**Related knowledge areas:** Database Protocols, Inspection Engine Architecture.

### Guardium Syslog TCP Port
**Configuration impact:** Requires root privileges; port conflicts auto-resolved.  
**Related knowledge areas:** Syslog Standards, TCP Configuration.

### Datasource Connectivity
**setOAuthTokenExpirationTime:** Adjusts expiration time.  
*Related knowledge:* OAuth Authentication, Token Management.  
**set_entitlement_datasource_parameter:** Requires entitlement extraction enabled.  
*Related knowledge:* Entitlement Process, Data Source Optimization.  
**set_ktap_debug:** Enables debug mode.  
*Related knowledge:* System Debugging, ktap Processes.  
**stop_istap_monitor:** Stops monitoring via datasourceName parameter.  
*Related knowledge:* Monitoring Processes, Data Source Management.  
**set_api_target_host:** Accepts `all_managed`, `all`, or `group:<group name>`.  
*Related knowledge:* API Targeting, Guardium Architecture.

## Guardium Feature Reference

### API Execution on Target Hosts
- **Support Matrix:** Guardium Central Manager, Managed Units
- **Limitations:** Strict formatting for `api_target_host` parameter
- **Workflows:** GuardAPI command `list_datasource_groups`, REST API `GET /api/target_hosts`
- **Knowledge:** Host Management, REST API Execution

### Datasource Parameter Management
- **Support Matrix:** IBM Guardium V11.0 and later
- **Limitations:** Manual intervention required for custom data mart file processing
- **Workflows:** Configuration — Data Mart File Processing
- **Knowledge:** Data Source Configuration, Data Integrity

### Guardium Insights Certificate Management
- **Support Matrix:** Guardium Data Protection GUI, Guardium V11.4+
- **Limitations:** Certificates must be in PEM format
- **Workflows:** Administration — Add Certificate
- **Knowledge:** Certificate Management, S-TAP Configuration

### Privilege Management via GuardAPI
- **Support Matrix:** All Guardium-supported databases
- **Limitations:** Requires ADMIN role
- **Workflows:** Security — Revoke Access
- **Knowledge:** Role-Based Access Control, Privilege Revoke

### Scheduled Group Population
- **Support Matrix:** Guardium V11.3 and later
- **Limitations:** Cron-style syntax for scheduling frequency
- **Workflows:** Scheduling — Populate Group
- **Knowledge:** Group Management, Query-Based Population

### Hadoop Policy Profile Management
- **Support Matrix:** Guardium V11.0 and later
- **Limitations:** Policy and rule names are case-sensitive
- **Workflows:** Policy Management — Uninstall Rules
- **Knowledge:** Policy Framework, Hadoop Security Controls

### Certificate Installation for S-TAP
- **Support Matrix:** Guardium Linux-UNIX, S-TAP V11.4 and later
- **Limitations:** Requires root access on target system
- **Workflows:** Installation — Certificate Deployment
- **Knowledge:** S-TAP Configuration, Secure Deployment

## Catalog and Report Management

### Update Catalog Entry or Archive Locations
- **Support Matrix:** Guardium 9.5 and later
- **Limitations:** Requires catalog entry management permissions
- **Workflows:** Single Update — file name; Bulk Update — path, hostname
- **Knowledge:** Guardium REST APIs, Catalog Data Lifecycle

### Retrieve and Configure QR Rewrite Actions
- **Support Matrix:** Guardium V10.1.4 and later
- **Limitations:** Requires valid action ID; no SDK export needed
- **Workflows:** API Call — list_qr_replace_element_byId
- **Knowledge:** Query Rewrite Architecture, RESTful Governance API

### Apply Unit Registration for Configuration
- **Support Matrix:** All Guardium platforms supporting central management
- **Limitations:** Requires registration tokens; IPv6 support independent of IP mode setting
- **Workflows:** Configuration — Register Managed Unit
- **Knowledge:** Guardium Security Token Framework, IPv6 Addressing in Guardium

### Manage HashiCorp Configuration View API
- **Support Matrix:** Guardium V11.4 and later
- **Limitations:** Requires Enterprise Security License
- **Workflows:** Configuration — View Configurations
- **Knowledge:** HashiCorp Vault Integration, Enterprise Security Features

### Modify Stap Host Ignore API Parameters
- **Support Matrix:** Guardium All Versions
- **Limitations:** Ignored hosts cannot be excluded from all policies
- **Workflows:** Security Policy

## 1242. Report Title  

### Dynamic Host Specification via api_target_host  
- **Components:**  
  - **Support Matrix:** `all`, `central-manager`, `<host>`, `<group>`  
  - **Limitations/Constraints:** IP mode must match; `all-managed-units` applies only to managed units  
  - **Workflows:** Administration — Set API Target Host; Monitoring — Validate Host Reachability  
- **Links:** API Parameter Conventions, Guardium Deployment Architecture  

## Datasource Connectivity  

## Gateways and Standalone Installation  

### Gateways and Standalone Installation  
- **Components:**  
  - **Support Matrix:** Red Hat Linux 6/7/x86\_64, AIX, Solaris, VMware  
  - **Limitations/Constraints:** No upgrade from V9.1; minimum 32 GB RAM required  
  - **Workflows:** Installation — Deploy Guardium  
- **Links:** ISO Files, Upgrade Paths  

## Shared Drive Access Permissions  

## Guardium Installation Manager (GIM)  

### Guardium Installation Manager (GIM)  
- **Components:**  
  - **Support Matrix:** All Guardium‑supported platforms  
  - **Limitations/Constraints:** Silent install not supported on Windows; DVD install requires mapped drive  
  - **Workflows:** Installation — GIM Installation  
- **Links:** Guardium ISO, Guardium Deployment  

## API - printFailoverGroupInfo Flag  

### API - printFailoverGroupInfo Flag  
- **Components:**  
  - **Support Matrix:** All Guardium API interfaces  
  - **Limitations/Constraints:** Overridden by Save CSV workflow; append mode not supported on all connectors  
  - **Workflows:** Configuration — View Report  
- **Links:** API Output, failover_group Parameter  

## Shared Drive Access Permissions  

## cronString and AppendParameter Workflow  

### cronString and AppendParameter Workflow  
- **Components:**  
  - **Support Matrix:** All Guardium APIS  
  - **Limitations/Constraints:** Cron syntax required; append incompatible with specific connectors  
  - **Workflows:** Scheduling — Run Query  
- **Links:** cron Syntax, Query Scheduling  

## Permissions for api_target_host Parameter  

### Permissions for api_target_host Parameter  
- **Components:**  
  - **Support Matrix:** All Guardium Platforms  
  - **Limitations/Constraints:** Requires FQDN/IP; role restrictions for REST API users  
  - **Workflows:** Execution — API Call  
- **Links:** API Authentication, Roles and Permissions  

## S-TAP Configuration for Ranger Audit  

### S-TAP Configuration for Ranger Audit  
- **Components:**  
  - **Support Matrix:** HDFS 2.6.0+, Ranger 0.5‑0.7  
  - **Limitations/Constraints:** rangerHdfsUser needs krb5; stapHostName needs network access  
  - **Workflows:** Configuration — HDFS Connector  
- **Links:** Kerberos Setup, HDFS Integration  

## Feature Flags in Guardium  

### Feature Flags in Guardium  
- **Components:**  
  - **Support Matrix:** Guardium 12.2.1+  
  - **Limitations/Constraints:** Managed only via specific APIs  
  - **Workflows:** Management — Feature Control  
- **Links:** Feature Flag Design, Guardium APIs  

## api_target_host Parameter Scope  

### api_target_host Parameter Scope  
- **Components:**  
  - **Support Matrix:** All Guardium Managed Units  
  - **Limitations/Constraints:** Values limited to `local`, managed units, logical groups  
  - **Workflows:** Administration — Remote Execution  

---

**Guardium Data Protection Configuration**  
- **Reset VA Summary Data** – Clears the vulnerability assessment summary across all supported Guardium databases. Requires API permission.  
- **Connect Google Cloud Accounts** – Integrates GCP projects with Unified Discovery & Classification; role creation needed for the connection.  
- **List Guardium Policies** – Enumerates all policies defined in Guardium across installations.

## API Target Host Parameter
Specifies IP address or hostname of a Guardium managed unit for any Guardium REST API call that uses **api_target_host**. IP mode (IPv4 or IPv6) must match registration of the target unit with the central manager.

## Add Cloud Account
Adds a cloud account for Unified Discovery and Classification. Requires admin-level credentials for the cloud provider and supports only service accounts. Navigate to *Cloud Accounts → New* and supply **Account Type** and optional **Custom Tags**.

## Ambari Server SSL Settings
Enables HTTPS for Apache Ambari 2.6+ to secure communication with Guardium agents. Upload a CA-signed cert on the *Advanced* page under *Settings → Ambari SSL* (Port 8442). Mutual SSL is not supported.

## OAuth V2 APIs
Create and manage OAuth 2.0 clients for API access. Register a client, obtain **Client ID** and **Secret Key**, use **Access Token**/Refresh Token flows. Requires Guardium Data Protection v1721+ and OAuth client configuration.

## Security Roles
Defines user permissions to Guardium functionality. Each role combines **Privileges** (system operations) and **Access Lists** (targeted objects).

## Guardium Components and Monitoring

### Service Principal Integration
Supports Guardium v12.0+ with limited create permissions for unified discovery assets. Workflow: Configuration → Security Settings → Roles → New. Links: RBAC, Data Classification, App Registration, Service Principal.

### Compliance Dashboards
Guardium compliance dashboards require Chart Description permission and admin view. Workflow: Reporting → Dashboard → Chart Details or Configuration → Dashboard → Edit. Links: Compliance Reporting, Dashboard Customization.

### Hostname Management
Supported on all monitored Guardium units, handling mixed IPv4/IPv6 with required DNS mapping. Workflow: Registration → Host Details or Navigation → Sources → IP/Hostname. Links: IP Mode Configuration, DNS Management.

### Custom Table Upload
Available from Guardium V9.5+. Requires proper permissions and size limits. Workflow: Data Management → Custom Table Upload or Configuration → Data Source Assignment. Links: Custom Table Management, REST API Integration.

## Security Workflows

### STAP Agent Approval
Requires approver role; batch processing may need scripts. Workflow: Security Administration → STAP Review or Approval Process. Links: Security Configuration, S-TAP Management.

## Db2 Privileges Reporting

### Table Level Privileges
Supported on all IBM Db2 platforms with no limitations. Workflow: Reporting → Db2 Table Level Privileges. Links: Data Access Control, Privilege Management.

### Database Level Privileges
Supported on all IBM Db2 platforms with no limitations. Workflow: Reporting → Db2 DB Level Privileges. Links: Data Access Control, Privilege Management.

## Guardium CLI and Configuration

### Ranger Configs
Supported on all Guardium appliances with no limitations. Workflow: Command → list_ranger_configs. Links: Apache Ranger, Security Configuration.

### System Parameters
Configuration supported on Guardium UNIX and Windows platforms with parameter-specific constraints. Workflow: Configuration → Guardium Parameters. Links: System Logging, Buffer Management.

### Reporting Capabilities
Privileged Access Monitoring supported on IBM Guardium with platform-specific support. Workflow: Reporting → Privileged Access Monitoring. Links: Auditing, Sensitive Data Access.

### Log Settings
Supported on IBM Guardium with no limitations. Workflow: Configuration → Log Settings. Links: Data Privacy, Audit Logging.

### Query Rewrite Commands
Supported on all Guardium appliances with no limitations. Workflow: Command → grdapi list_qr_action. Links: Query Rewrite, API Usage.

### License Installation
Supported on Guardium Trial with 90-day limitation. Workflow: Installation → Trial License. Links: Software Licensing, Product Activation.

## Guardium Package Management

### GIM Agent Packages
Supported on Windows, Linux, UNIX, z/OS requiring entitlement key and GUI for supported OS. Workflow: Installation → Deploy Package or Configuration → Update Agent Settings. Links: Guardium Installation Manager, Package Repository.

### ISO Prompts and Procedures
Supported on Guardium 11.x, 12.x, 13.x with no limitations. Workflow: Configuration → Advanced Partitioning. Links: Guardium Installation ISO, Advanced Partitioning.

## Guardium Reference Documentation

### Vulnerability Assessment Entry
Vulnerability assessment chart components include a support matrix for Guardium 11.x‑13.x, no limitations, and access chart description workflows. Knowledge links cover the Vulnerability Assessment Dashboard, chart customization, and keywords include Chart Description, Vulnerability Assessment, and Dashboard.

### ISO Files Entry
ISO file partition configuration entry covers Guardium 11.x‑13.x support, no constraints, and ISO selection installation workflows. Knowledge links reference Guardium ISO Files and Partition Configuration, and keywords are ISO File, Partition, and Installation.

### CAS Audit Templates Entry
CAS audit templates management entry supports Guardium 11.x‑13.x, requires the CAS feature enabled, and includes update CAS templates configuration workflows. Knowledge links point to CAS Audit Templates and API Integration, with keywords CAS Template, Update API, and CAS Management.

### Solr Connectivity Entry
Solr connectivity and hardware requirements entry supports Guardium 11.x‑13.x, requires Solr installed, and includes Solr connectivity testing workflows. Knowledge links cover Solr Connectivity and Hardware Requirements, with keywords Solr Connect, Solr Requirements, and API Test.

### API Target Host Entry (1314)
API target host parameter entry supports Guardium 11.x‑13.x, requires a valid host, and includes target host specification workflows. Knowledge links reference API Execution and Target Hosts, with keywords API Target Host, Execution Scope, and Host Specification.

### API Target Host Entry (Revised for Clarity)
API target host parameter entry supports Guardium across all API versions, requires IP mode matching network configuration, and includes network target specification workflows. Knowledge links cover API Architecture and IP Mode Configuration, with keywords IP_ALL_MANAGED_UNITS, guardium, rest_api, and client_ip.

### API Target Host Entry (Duplicate)
Duplicate entry for API target host parameter usage—omit.

### Access Management Commands Entry
Role-based access control entry supports Guardium 11.3+, requires accessmgr role, and includes configure access controls and review access logs workflows. Knowledge links reference Role-Based Access Control and Guardium Security Administration, with keywords accessmgr, guardapi, role, and user_management.

### RESTful API for Edge Data Entry
Guardium data upload service entry supports Guardium v12.2+, requires multipart/form-data POST, and includes upload edge data and integrate with Guardium workflows. Knowledge links cover REST API Design and Guardium Edge Analytics, with keywords edge_data, http_post, file_upload, and rest_api.

### Update Rule Command Entry
Policy rule modification entry supports Guardium v9.5+, requires rule_desc and from_policy parameters, and includes update rule and review rule changes workflows. Knowledge links point to Data Protection Policies and GuardAPI Reference, with keywords update_rule, guardapi, policy_rule, and put_method.

## User Account Change Tracking
Supports Guardium v10.1.4 and newer. Requires a timestamp parameter for historical queries. Workflows include User Management - Review Changes and Security Administration - Audit User Accounts. See **User Account Auditing** and **Guardium APIs** for more information. Keywords: `retrieve_updated_users`, `timestamp`, `rest_api`, `user_audit`.

## Web Application Security
Applies to browsers supporting CSP-like headers. Set `X-XSS-Protection` header value to `"1; mode=block"` for active XSS protection. Workflow includes Security Configuration - Enable XSS Protection and Web Application Testing - Validate Security Headers. See **Cross-Site Scripting Prevention** and **Web Security Headers**. Keywords: `xss_protection`, `security_header`, `web_application`, `http_header`.

## Enterprise Single Sign-On
Available in Guardium v11.0 and later with Kerberos integration. Requires `kerberos.conf`, username, and password. Workflow includes Authentication - Configure Kerberos and Security Integration - Enable Single Sign-On. See **Kerberos Authentication** and **Single Sign-On Solutions**. Keywords: `kerberos`, `conf_file`, `username`, `password`.

## Managing User Accounts
Supported by Guardium v9.0 and newer. Requires appropriate administrative roles for user manipulation. Workflow includes Administration - Manage Users and Security - Enforce User Policies. See **User Administration** and **Guardium Security**. Keywords: `guardapi`, `user_management`, `roles`, `security_policies`.

## Role Assignment
Available in all Guardium releases. Requires Securityadmin or higher. Workflow includes Administration - Users & Password Policies - Manage Users. See **Role-based Access Control**, **User Accounts**, and **Security Administration**. Keywords: `set_user_roles`, `Securityadmin`, `admin role`, `CLI command`.