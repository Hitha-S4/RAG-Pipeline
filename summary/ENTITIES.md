# Permissionstodynamicrolesandcredsfordifferentpaths — ENTITIES

**Category:** entities  |  **Generated:** 2026-07-09  |  **Source:** gdp-12.x-documentation.pdf

---

(No further content)

---

## Infrastructure

### Linux-UNIX S-TAP
**Type:** service
**Description:** Installation workflows for Linux-UNIX S-TAP agents include GIM, RPM, and shell methods.

## Cloud Services

### AWS IAM Role
**Type:** feature
**Description:** Required IAM role for Guardium Cloud services in AWS environments.

```markdown
## Workflows
- **User & Group Management**: Administrative tasks in IBM Guardium for managing access to CyberArk safes.
- **Custom Property Grouping**: Define custom properties to group datasources by attributes like location.
- **S-TAP Installation**: Multiple methods for installing Linux-UNIX S-TAP agents (GIM, RPM, shell).
- **CyberArk Integration**: Set datasource Credential type to "External password" and select "CYBERARK" as location type.

## Agents & Collectors
- **S‑TAP (Software TAP)**: Captures database traffic and forwards it to a Guardium Collector.
- **Collector**: Receives activity data from S‑TAP, applies policies, and stores audit records.

## Policies & Rules
- **Security Policy**: Defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Databases & Datasources
- **License Counter**: Value showing remaining Guardium licenses.

## Certificates & Identities
- **Host Alias**: Required when certificate hostname differs from actual hostname.
- **Guardium Data Platform (GDP) Host**: Hostname for executing deployment commands.

## GUI & Infrastructure
- **Guardium Installation Manager (GIM) Service**: Manages software deployment and monitoring.
- **Guardium CLI / GuardCTL Command**: Utilities for managing database instances and interacting with Guardium services.

## Cloud & Ingress
- **Ingress Configuration**: Optional settings for routing traffic through a load balancer with External‑S‑TAP.

## Entities & Collectors
- **Host Alias**: Placeholder in configuration that must match `gdp.host`.
- **Guardctl Command**: `guardctl is_user_authorized db2inst1` verifies user permissions.

## Knowledge
- **Server.pem File Alignment**: Ensures secure communication with matching certificate hostname.
- **ens32 MAC Address & System Information**: `support execute version` displays system data including MAC address.

## Appliance
- **Support Execute Command**: `support execute version` retrieves system details including MAC address and root passkey.

## Appliance
- **Support Execute Command**: Retrieves system details like MAC address and root passkey.
```

## Overview

- **Security Policy**: Configured rule set defining allowed, logged, alerted, or blocked database activities.
- **Compliance Report**: PDF reports summarizing audit findings and compliance status.
- **Vulnerability Assessment Report**: Analysis of identified security vulnerabilities in monitored data sources.
- **REST API**: Programmatic access to Guardium features for automation and integration.
- **GuardAPI**: Command-line interface for managing Guardium components and querying security data.

## Data Sources

- **Database**: Real-time monitoring and auditing for Oracle, SQL Server, MySQL, and other standard databases.
- **Cloud Datasource**: Supports security monitoring across cloud environments including AWS, Azure, and others.

## Infrastructure

- **KVM Host**: Virtualization host for deploying Guardium virtual appliances.
- **Kubernetes Cluster**: Scalable, resilient environment for hosting Guardium components using container orchestration.

## Cloud Services

- **AWS S3**: Storage for backups, logs, and data assets.
- **Azure Blob Storage**: Secure, scalable object storage solution.

## Agents & Collectors

- **S-TAP (Software TAP)**: Captures database traffic on servers for real-time analysis and policy enforcement.
- **Collector**: Appliance receiving data from S-TAP agents, applying policies, and storing audit records.

## Credentials & Certificates

- **API Key**: Authenticates API requests to Guardium services.
- **TLS Certificate**: Secures communications between Guardium components via TLS encryption.
- **hashicorp**: Authentication and configuration management for infrastructure as code tools.

*Note: Specific details for named entities like `delete_hashicorp_config` and certain tool-specific descriptions were not extracted from the provided content.*

---

## Governance & Compliance

### Exception View
**Type:** database view  
**Description:** SQL view `exception_view` selects AppUsername, ClientHostName, and DBErrorText details of database exceptions for compliance tracking.

---

## Security Components

### Analyzer
**Type:** system component  
**Description:** Identifies sensitive information and applies masking rules to protect data.

---

## Reports & Analytics

### Connection Profiling Report
**Type:** report  
**Description:** Provides insights into database connections and session activities for auditing and security analysis.

---

## Tasks & Maintenance

### Cold Storage Maintenance Logs
**Type:** task  
**Description:** Tracks maintenance tasks associated with long term retention (LTR) processes via a specific Guardium report.  

---

## 184. chgroup users=informix guardium

**Type:** workflow  
**Description:** Change the group ownership of specified files or directories to *informix* and *guardium* for proper permissions and access control.

---

## 185. Oracle example

**Type:** entity  
**Description:** Named entity identified in source; detailed content not extracted.

---

## 186. Guardium REST interface

**Type:** api  
**Description:** Named entity identified in source; detailed content not extracted.

---

## 187. Central API call syntax

**Type:** api  
**Description:** API call syntax includes `api_target_host` parameter to execute on all managed units (`all_managed`), all hosts (`all`), or specific hosts within a group (`group`).

---

## 188. Registry certificate installation

**Type:** configuration  
**Description:** Skips registry certificate installation on cluster nodes in a Guardium environment, enabling automated deployment without manual certificate management.

---

```markdown
## Security & Configuration

### Agents & Collectors
#### S-TAP  
Captures database traffic and forwards it to a Guardium Collector for real-time policy enforcement.  

#### Collector  
Receives activity data from S-TAP agents, enforces security policies, and stores audit records.

### Certificates & Security
#### Client Web Certificates Configuration  
Attaches empty tuple groups to analyzer rules and handles client web certificates for secure operations.  

### Credentials & Certificates

#### Web Certificate Encoding (ISO-8859)  
Uses ISO-8859-1 through ISO-8859-15 character encodings when configuring client web certificates for correct authentication payload handling.

### APIs & Tools

#### GuardAPI: delete_datasource_custom_prop  
Deletes custom properties from a data source.  
**REST Example:**  
```bash
DELETE https://guardium.mycorp.com:8443/restAPI/delete_datasource_custom_prop?datasource_name=prod_mysql_01&property_name=audit_log_path
```

#### GuardAPI: list_rules_with_threshold  
Lists all rules with alert thresholds.  
**Parameters:** `threshold_type` (e.g., "COUNT", "PERCENT").  
Available from version 11.3.

## Infrastructure & Services

### Registry Certificate Installation (Cluster Nodes)  
Option for automatic deployment of registry certificates to managed cluster nodes.

### Guardium Integration with Ranger Log4j  
Forwards Hadoop Ranger audit logs to Guardium via Log4j. Requires `log4j_listen_address` and `appserver_ports` settings.
```

## Databases & Datasources

### Oracle
**Type:** database  
**Description:** Enterprise relational DBMS monitored via Guardium S-TAP agents and policies.

## Credentials & Certificates

### CAS Template
**Type:** configuration  
**Description:** Pre-defined Guardium CAS configuration for securing database credentials and access.

## APIs & Tools

### REST API
**Type:** api  
**Description:** Web interface for programmatic Guardium operations such as template and report management.

### Guardium CLI
**Type:** tool  
**Description:** Command-line utility for Guardium administrative tasks like daily purge and archive configuration.

## Infrastructure

### Guardium Grid
**Type:** infrastructure  
**Description:** Scales multiple Guardium Collectors for high availability and load balancing in large deployments.

## Cloud Services

### Guardium Cloud Service
**Type:** service  
**Description:** Managed, subscription-based service delivering Guardium's database security and monitoring capabilities in the cloud.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** Installs on database servers to capture traffic and send it to a Guardium Collector for analysis.

### Guardium aggregator
**Type:** appliance  
**Description:** Consolidates data from multiple S-TAPs and forwards it to Guardium Collectors.

### Collector
**Type:** appliance  
**Description:** Receives data from S-TAPs or aggregators, enforces policies, and stores audit records.

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

### Backup Policy
**Type:** policy  
**Description:** Governs backup frequency, scope, and storage locations.

## Knowledge & Entities

### create_role
**Type:** api  
**Description:** Creates roles on Guardium standalone or central manager (available since V10.1.4).

### log4j_port
**Type:** configuration  
**Description:** Port number for log4j logging in Guardium.

### krb_protocol
**Type:** configuration  
**Description:** Configures Kerberos settings for Guardium communication.

### enclave_user
**Type:** entity  
**Description:** User defined within Guardium's enclave authentication system.

### Data classification schedule
**Type:** configuration  
**Description:** Schedule for automated data classification tasks.

### Storage location
**Type:** entity  
**Description:** Physical or virtual destination for backups or archives, defined by host, path, and credentials.

### Custom datasource property
**Type:** configuration  
**Description:** User-defined parameter for datasource connections via Guardium API (available from V11.0).

### testseparator
**Type:** parameter  
**Description:** Delimiter for separating multiple test descriptions in Guardium API commands.

## Workflows & Processes

### Activation workflow
**Type:** workflow  
**Description:** Steps to activate a new Guardium appliance, including initial setup and credential configuration.

### Credential deletion process
**Type:** workflow  
**Description:** Removes a user credential using required `credentialName` and `api_target_host` parameters.

### Central Manager version sync
**Type:** workflow  
**Description:** Synchronizes version information across Central Manager and managed units after upgrades.

### SSH key authentication setup
**Type:** workflow  
**Description:** Adds an SSH public key for passwordless authentication, including insertion and verification commands.

### Solr status check
**Type:** workflow  
**Description:** Uses `get_solr_status` API to check if Solr is enabled, running, or absent on a Guardium system.

### Custom property creation
**Type:** workflow  
**Description:** Adds a custom datasource property using `grdapi`, available from V11.0.

## Entities & Collectors

### IBM Guardium
**Type:** appliance  
**Description:** Comprehensive data security platform providing unified visibility, protection, and remediation for data assets across environments.

### GuardAppEvent
**Type:** entity  
**Description:** Tracks application events (e.g., Start, Released) to manage and log critical actions in the data environment.

### IBM Guardium Data Protection
**Type:** product  
**Description:** Solution offering real-time database security monitoring, policy enforcement, and risk assessment for compliance and data integrity.

## Registry certificate installation
Workflow step in Guardium that ensures secure communication across cluster nodes.

## CLI Command for Network Interface
Displays detailed information about network interfaces, including port names and MAC addresses, on Guardium systems.

## Auto-Install on Database Server OS Upgrade
Boolean parameter controlling whether Guardium modules automatically upgrade when the underlying client operating system versions change.

## Guardctl Authorization Command
Authorizes users within Guardium to integrate S-TAP installations with Guardium user management systems.

## Outlier Analysis
Advanced data monitoring capability within the Guardium platform designed to detect anomalies and unusual patterns in data access and usage.

## delete_assessment_test
API command to remove a specific test from a given assessment in Guardium.

## Threat Detection Use Case: GRANTS
Configuration step to enable the GRANTS threat detection capability in IBM Guardium, which monitors unauthorized privilege usage.

## datamart_copy_file_bundle
Utility to integrate a specific data mart into an existing data mart bundle.

## Configuration for Client Web Certificates
Procedures and workflows for configuring client-side SSL/TLS certificates to authenticate data sources connecting to Guardium.

## Stap Verification Results
Logs and API results that verify the status and validity of the Software TAP (S-TAP) agent's connection and operation on database servers.

## Unit Registration with Central Manager
Process whereby a Guardium unit registers with a central management unit using either IPv4 or IPv6 address.

## Entitlement Optimization
System settings related to the analysis and enforcement of user entitlements, which can be disabled through GuardAPI.

## S-TAP (Software TAP)
Software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

## Collector
Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Security Policy
Configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Oracle Database
Relational database management system developed by Oracle Corporation that supports structured query language (SQL).

## Data Source Plug-ins
Enables integration of various data sources with Guardium Data Protection for ingestion and monitoring.

## Registry Certificate
Artifact used in Guardium for securing communication across cluster nodes.

## Verify API Key
Checks the existence of an API key within Guardium's security framework.

## db2_exit_health_check.sh
Script to verify the health of IBM Guardium DB2 exit integrations, running checks without making changes.

## Enable OPTIM Auditing
Configures OPTIM auditing in Guardium by granting audit roles, adding reports, and enabling the sniffer component.

```markdown
## Enterprise Load Balancing
Distributes load across managed units using entity groups, S-TAP Control, and UI configuration.

### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

### Guardium Insights
Provides advanced analytics and machine learning to detect anomalies and threats based on aggregated data from Guardium collectors.

### Guardium Data Encryption
Secures sensitive data at rest and in transit, ensuring compliance and protecting against unauthorized access.

### Guardium Policy Wizard
An interactive tool that assists users in creating and refining security policies through a guided rule-definition process.

### Guardium Assessment
Automates security assessment checks against industry standards, providing reports and recommendations to improve security posture.

### Guardium CAS
Monitors configuration changes to critical files and system settings, alerting administrators to unauthorized modifications.

### Guardium CAS Policy
Defines what configuration changes to monitor and specifies actions to take when unauthorized changes are detected.

## Policies & Rules
### Security Policy
A rule set that defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

### Access Rule
Determines if a file read/write meets policy conditions.

### Threshold Rule
Flags unusual authentication methods by tracking valid connections.

### Violation Detection Rule
Generates a security incident for repeated failed login attempts, reporting each unique combination of database user and client IP.

## Databases & Datasources
### Datasource Type
### Datastore

## Credentials & Certificates
### Web Certificate

## APIs & Tools
### API Target Host
When registering a managed unit with the central manager, use the hostname instead of the IP address, regardless of IP mode. The hostname is independent and flexible for API execution.

### GIM Schedule Uninstall
Schedules uninstallation of specified modules for a GIM client, allowing precise control over software inventory.

### IAM Permissions
Defines AWS IAM for native audit in Guardium. Requires the DBA to add specific IAM permissions to the AWS console if the system cannot identify its own IP, detailing required parameters and policies.

## Infrastructure
### Guardium System Ownership Transfer
Transfers ownership from a Guardium system that has gone down without expectation of recovery to another system.

## Cloud Services
### Storage Connection String
Emphasizes safeguarding storage connection strings by regularly regenerating them to maintain security for storage accounts.
```

## Monitoring

### Threat Detection Analytics
**Type:** feature
**Description:** Engine that analyzes activity data to identify suspicious patterns and issue alerts.

### Exceptions Domain
**Type:** feature
**Description:** Central place for managing security policy violations and handling exceptions.

---

## User Access Management

### User/Role/Application Domain
**Type:** feature
**Description:** Provides visibility into users, roles, and application access across the enterprise.

---

## Auditing & Reporting

### Session End Attributes
**Type:** feature
**Description:** Timestamps capturing when database sessions terminate for audit purposes.

### DML Execution Audit Workflow
**Type:** feature
**Description:** Reports on DML statement activity by objects and executing users.

---

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** Lightweight agent that monitors database traffic locally and sends data to a Collector.

### Collector
**Type:** appliance
**Description:** Central hub that receives data from S-TAP agents, applies policies, and stores audit records. Supports high availability configurations.

## Workflows & Features

### Token Authentication Workflow
Use a previously obtained access token in REST API calls. Tokens work only on central manager or standalone units, not managed units.

### S-TAP Cluster Setup
Specify IP addresses for each S-TAP instance. Each S-TAP joins only one cluster. Save configuration to enable traffic distribution and redundancy.

### Registry Certificate Installation Management
Skip registry certificate installation on nodes by default for managed unit groups. Override individually with CLI commands for cluster nodes.

## Agents & Collectors

### S-TAP (Software TAP)
A software agent on database servers that captures traffic and forwards it to a Guardium Collector for analysis.

## Policies & Rules

### Security Policy
Configure which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Agents & Collectors

### S-TAP (Software TAP)
The S-TAP agent captures database traffic and user activity on database servers, sending it to a Guardium Collector.

### Collector
A Guardium appliance hardware/software that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Databases & Datasources

### K-TAP (Kernel TAP)
A kernel module alternative to S-TAP; provide more details about its functionality and use cases here.

## Credentials & Certificates

### Kerberos Authentication
Configure secure data source connections using either username/password or a Keytab file with a Kerberos configuration.

## APIs & Tools

### API Key Verification
Provide details about verifying API keys, including best practices for security.

## Infrastructure

### Managed Unit Load Balancing
Balance client traffic across managed units based on load to ensure high availability.

## Cloud Services

### Guardium Cloud Architecture
Summarize key features and operational principles of Guardium's cloud offering.

## Database Type Configuration
A CLI menu selects database types (e.g., MySQL, MSSQL) and configures related parameters, including double-quoted string handling.

## Custom K-TAP Bundle Migration
`export gim_bundle` transfers custom K-TAP modules between GIM servers, requiring target server hostname or IP.

## CLI Tools
CLI commands and prompts configure system settings such as multilanguage PDF support, database type selection, and UID chain processing intervals.

## Patch Application Tool
Manages and applies patches to Guardium components for security and functionality across upgrades.

## Consolidated Installer
Simplifies Windows server deployment of Guardium components, including S-TAP and GIM client.

## Health Check and Patch Application Infrastructure
Performs health checks on central managers and managed units and facilitates patch application to prevent upgrade issues.

## S-TAP (Software TAP)
A database server agent capturing traffic and forwarding it to a Collector for analysis and policy enforcement.

## Collector
A Guardium hardware or virtual appliance receiving data from S-TAP agents, applying policies, and storing audit records.

## Security Policy
A rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Data Source
A defined database connection for monitoring, auditing, and protecting data within Guardium.

## Cloud Datasource
Manages cloud-based data sources using Guardium APIs, enabling unified monitoring across on-premises and cloud platforms.

## Excel Datasource
Imports data from Excel files into Guardium for analysis and policy application, integrating external audit logs and reports.

## JDBC Datasource
Uses JDBC protocol to connect and monitor SQL traffic from databases comprehensively.

## Snowflake Datasource
Specialized configuration for Snowflake data warehouses, integrating security and compliance monitoring tailored to Snowflake environments.

## Credential
Stored authentication methods (usernames, passwords, SSH keys) for accessing datasources within Guardium.

## TLS Certificate
Secures communications between Guardium components, ensuring encrypted data transfer between S-TAP agents and Collectors, and within Guardium.

## GuardAPI
Command-line API for programmatic Guardium configuration, management, and querying.

## GuardCLI
Command-line tool executing GuardAPI functions, ideal for automated scripting and batch operations.

## Universal Connector
Ingests logs and data from diverse sources, extending Guardium's visibility beyond traditional databases.

## GUI (Guardium User Interface)
Web-based interface for managing Guardium, providing graphical tools for configuration, monitoring, and reporting.

## CLI (Command-Line Interface)
Text-based interface for scripting and automating Guardium tasks.

## API Manager
Centralized service managing API access, authentication, and authorization, ensuring secure API interactions.

## AWS S3 Archive
Cloud storage service archiving Guardium audit logs and reports, providing scalable and secure long-term data retention.

## Azure Blob Storage
Microsoft Azure's object storage for Guardium audit data and compliance reports, offering high availability and durability.

## Google Cloud Storage
Google Cloud's object storage archiving and backing up Guardium data, integrating seamlessly for data protection and compliance.

```markdown
## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  

### Collector  
**Type:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.  

## Policies & Rules  
### Security Policy  
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.  

## Databases & Datasources  
### Db2 Shared Memory Area  
**Type:** knowledge  
**Description:** The excerpt details offsets within the Db2 shared memory area, differing between pre-8.2.1 and 8.2.1+ versions, which is relevant for low-level system programming or debugging involving Db2's internal memory management.  

## APIs & Tools  
### add_autodetect_task API  
**Type:** api  
**Description:** Excerpt incomplete; appears to detail parameters for adding an autodetect task via API.  

### datamart_copy_file_info command  
**Type:** tool  
**Description:** Excerpt incomplete; describes parameters for the `datamart_update_copy_file_info` command, including `storageClass` for data transfer via SCP using SSH keys.  
```

### 422-424: Licenses
**Type:** entity  
**Keywords:** licenses, remaining  
**Description:** Indicates the number of licenses still available.

### 425‑430: Skips registry certificate installation on cluster nodes
**Type:** entity  
**Keywords:** registry, certificate, installation  
**Description:** Describes a configuration option that bypasses the installation of registry certificates on cluster nodes.

---

### S‑TAP (Software TAP)
**Type:** agent  
**Description:** Captures database traffic on the server and forwards it to a Guardium collector for real‑time analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** Receives data from S‑TAP agents, applies security policies, stores audit records, and provides reporting and alerting capabilities.  

---

### Security Policy
**Type:** policy  
**Description:** Defines rule sets that govern database activity monitoring, specifying what is allowed, logged, or blocked.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic on monitored servers and forwards it to a Guardium Collector.

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** Defines allowed, blocked, logged, or alerted database activities based on user, object, and action criteria.

### Custom Policy
**Type:** policy
**Description:** User-defined rule set that extends standard security policies for specific compliance or business requirements.

### Exclusion Rule
**Type:** rule
**Description:** Ignores or excludes certain database activities from monitoring and logging based on specified conditions.

## Entities & Attributes
**Type:** entity  
**Description:** Constructs that uniquely identify sets of client/server connection attributes, requiring admin role permissions for access and crucial for security constructs within Guardium.

**Type:** attribute  
**Description:** Part of rule definitions, used for data validation or processing tasks.

**Type:** attribute  
**Description:** Records the chain of OS users during Unix privilege escalation events, aiding in tracking the true user behind actions.

**Type:** attribute  
**Description:** Identifies the timestamp associated with audit events, crucial for chronological tracking.

**Type:** attribute  
**Description:** Identifies the IP address of the server involved in database events.

**Type:** entity  
**Description:** Uniquely identifies database systems and manages access permissions.

## Rules & Definitions
**Type:** rule  
**Description:** Part of enhanced Guardium security constructs, defining criteria for monitoring and enforcing actions on database activities.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Datasources
### Database
**Type:** database  
**Description:** Named entity identified in source; detailed content not extracted.

## Entities
### Entities
**Type:** entities  
**Description:** The passage discusses selecting different bundle versions for specific platforms or clients in GIM. It provides steps for clearing the "Show only latest versions" checkbox and selecting the required bundle version.

## Certificates

**Description:** Configures certificates with either company‑unique or machine‑specific common names, ensuring identity verification while maintaining trusted status within the Guardium ecosystem.

---

## APIs & Tools

### CLI Command
**Description:** Displays network settings, hostname, domain, clock date/time, time servers, and unit type on the Guardium system, with options to reboot during initial setup.

---

## Infrastructure

### VM Template
**Description:** Involves cloning Guardium VM templates and configuring each clone by resetting IP parameters such as IP address, GLOBAL_ID, and hostname.

---

## Cloud Services

### Data Archive Job
**Description:** Monitors the status of data archive jobs, integrating with previous archiving procedures to verify outcomes and embed workflows into broader data management processes.

---

## System Command Reference

### store disk reserve
**Description:** Sets the disk space reservation percentages for aggregators and collectors; default values are provided by Guardium, with warnings issued for deviations below these defaults to prevent system instability.

---

## Access and Permissions  

### Access Control
**Description:** Guardium offers detailed access control features, allowing administrators to define roles and assign specific privileges to users or groups, aligning access rights with job responsibilities.

### User Management
**Description:** Manages user accounts by creating, modifying, and deleting them, assigning tailored roles to ensure appropriate access based on job functions, thereby enhancing security and efficiency.

---

## Number Sign 586
`d1df073d-7f58-426a-a568-d`  | **categories:** knowledge, entities  
*Details:* Identifies documentation for the `get_test_case_status` GuardAPI, which retrieves the status of test cases within the Guardium environment.

---

## Agents & Collectors

### S-TAP (Software TAP)
**Description:** Captures database traffic on Unix servers and forwards it to a Guardium Collector for real‑time analysis and policy enforcement, tracking multiple OS users across privilege changes.

### Collector
**Description:** Collects activity data from S-TAP agents, applies security policies, and stores audit records, serving as a central point for data analysis and compliance reporting.

---

## Policies & Rules

### Security Policy
**Description:** A rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria, ensuring compliance and security.

---

## Databases & Datasources

### Oracle  
**Description:** Configures connections and auditing for Oracle database environments.

### CSV  
**Description:** Manages data import/export using comma‑separated values files.

### JDBC  
**Description:** Supports JDBC‑compliant databases (e.g., MySQL, PostgreSQL) for unified data management.

### Informix  
**Description:** Configures connections and auditing for IBM Informix database systems.

### Object Tracking
**Description:** Tracks database objects, creating new fields as needed, and manages structural changes within Oracle systems.

---

## Credentials & Certificates

### User Hierarchy
**Description:** Manages auditing scenarios involving user hierarchies and data sets, focusing on Timestamp, Records Affected, Returned Data, and Full SQL attributes.

---

## APIs & Tools

### IMS DLI Detail Report
**Description:** Monitors IMS DLI activities, detailing attributes such as FULL SQL and SSID for effective service monitoring and reporting.

### Hierarchy Creation
**Description:** Uses `create_user_hierarchy` to define user relationships, exemplified by `create_user_hierarchy userName=ADAMS parentUserName=SCOTT`.

---

### Data Sources & Databases

### Data Source
**Type:** datasource
**Description:** A configured connection to a database or application that Guardium can monitor and audit.

### Database
**Type:** database
**Description:** A collection of organized data, such as Oracle, MySQL, or Microsoft SQL Server, that Guardium can analyze for security and compliance.

# Guardium Data Protection Overview

## Key Concepts

### Database Types
- **Oracle**: Specific database type supported for import.
- **Datasource**: Entity representing a single imported database.

### Sensitive Data Discovery
- Identifies sensitive data during database import.

## Procedures

### Importing Database
- Configures datasource for import.
- Supports specific database types.

## Features

### Policy Builder
- Manages tags and rules.

## Schema & Data Types

### Custom Table Data Types
- Lists supported and unsupported data types for Oracle.

## Entities

### Analytic Case
- Single entity containing detailed case information.

## Help & References

### Monitor and Audit Help Book
- Sections: initialization logs, audit trails, access auditing.

## Agents & Collectors

### S-TAP (Software TAP)
### Collector

## Policies & Rules

### Security Policy

## Databases & Datasources

### MySQL Process

## Credentials & Certificates

### Registration and Load Balance

## APIs & Tools

### Central Manager

## Central Manager Setup Instructions

Log into the Guardium command-line interface and execute the following steps to configure a machine as the Central Manager:

1. Set the unit type to **manager** using the appropriate CLI command.  
2. Apply the product key to complete the initial configuration.

## Policies & Rules
### Security Policy
**Type:** policy
**Description:** Defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic and forwards it to a Guardium Collector for analysis and policy enforcement.

### Collector
**Type:** appliance
**Description:** Receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Databases & Datasources
### Oracle
**Type:** database
**Description:** A relational database management system supporting complex queries and transactions.

### MongoDB Cluster
**Type:** database
**Description:** A collection of MongoDB instances forming a replica set for high availability and horizontal scaling.

### Netezza Database
**Type:** database
**Description:** IBM Netezza is a warehouse appliance optimized for analytics with file ownership testing in CAS templates.

## Credentials & Certificates
### Smart Card Authentication
**Type:** credential
**Description:** Uses a smart card and card reader for user identity verification, requiring a web browser with smart card support and a valid PIV or CAC card.

### Registry Certificate
**Type:** certificate
**Description:** Establishes trust between Guardium components, with optional installation on cluster nodes using specific jobs.

## APIs & Tools
### grdapi create_user_hierarchy
**Type:** api
**Description:** Creates a user hierarchy within Guardium, establishing parent-child relationships for organizational and access control.

### Command Line Interface (CLI)
**Type:** tool
**Description:** Manages Guardium system components, including restoring default certificates.

## Infrastructure
### Edge Gateway
**Type:** entity
**Description:** Connects Guardium with external systems.

## Cloud Services

### Long Term Retention (LTR)
**Type:** service
**Description:** Archiving strategy configurable via Central Manager UI to securely retain data over extended periods.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent 
**Description:** Installs on database servers to capture traffic and forward to Collector for real-time analysis.

### Collector
**Type:** appliance 
**Description:** Hardware or virtual appliance receiving data from S-TAP agents, applying policies, and storing audit records.

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** Rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Workflows & Entities

### Request certificate installation on Guardium cluster nodes
**Type:** workflow
**Description:** Copies key files from an external server to managed units and central manager to secure Guardium communication.

### Verify API key exists (STAP_LOADER_BALANCER_NODE_AFFINITY)
**Type:** entity
**Description:** Governs S-TAP agent connection to managed units during load balancing across multiple collectors.

### Verify API key exists (S-TAP installment)
**Type:** entity
**Description:** Steps to safely uninstall S-TAP from specific database servers through Guardium interface.

y insights:** Handles granular monitoring of database activities; supports multiple database types including Oracle and MSSQL; integrates with collectors for data processing and reporting.

---

## **Databases & Datasources**

### Oracle Database
**Type:** database  
**Description:** Oracle's relational database, requiring datasources with fields like *Audit Password* and *Compatibility Mode* for tasks such as Value Change Auditing.

### MSSQL Server
**Type:** database  
**Description:** Microsoft SQL Server supporting Value Change Auditing via datasources with database-specific configuration fields.

### Config
**Type:** configuration  
**Description:** Manages settings for CAS hosts using template sets applied to server hosts, ensuring security compliance and uniformity across environments.

### Policy
**Type:** policy  
**Description:** Security policies comprising rules that enforce compliance with standards like PCI/DSS, handling multiple actions per rule.

Type:** certificate
**Description:** *Named entity identified in source; detailed content not extracted.*  
---

```markdown
## Agents & Collectors
### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.
### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Datasources
### MongoDB Datasource
A named entity identified in source; detailed content not extracted.

## Credentials & Certificates
### certificate
A digital certificate used to verify the identity of Guardium components or to secure communications.

## APIs & Tools
### verify_tap
The `verify_tap` command interface allows immediate verification of S-TAP inspection engines through the S-TAP Status Monitor. Instructions include refreshing the Monitor window and performing on-demand verification for individual engines.
### Token Generator for Linux API
Provides a mechanism to generate authentication tokens for accessing Guardium APIs on Linux platforms.
```

## BCV Command  

**Type:** tool  
**Description:** Command-line utility for managing and configuring backup and change verification tasks in Guardium.  

## Infrastructure  

### Guardium Virtual Appliance  
**Type:** appliance  
**Description:** Virtual machine deployment of Guardium Collector or Aggregator on a hypervisor.  

### Grid Cluster  
**Type:** infrastructure  
**Description:** Group of Guardium appliances acting as a single logical unit for scalability and high availability.  

## Cloud Services  

### Hadoop Cluster  
**Type:** service  
**Description:** Distributed processing framework supported by Guardium for monitoring Hadoop environments.  

### Guardium Cloud  
**Type:** service  
**Description:** Managed cloud-based Guardium functionality via subscription.  

## Certificates  

### Venafi Root CA Certificate  
**Type:** configuration  
**Description:** Root CA used to validate appliance certificates; export and install with `certs apply venafi-root`; restart GUI after installation.  

## Agents & Collectors  

### S-TAP (Software TAP)  
**Type:** agent  
**Description:** Software agent on database servers capturing traffic and forwarding to Guardium Collector for analysis.  

### Guardium Universal Connector  
**Type:** application  
**Description:** Core component ingesting data from various sources within Guardium without exposing architecture.  

### Guardium Collector  
**Type:** appliance  
**Description:** Hardware or virtual appliance receiving S-TAP data, applying policies, and storing audit records.  

## Policies & Rules  

### Security Policy  
**Type:** policy  
**Description:** Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.  

## APIs & Tools  

### REST API  
**Type:** api  
**Description:** Web-based API for programmatic access to Guardium functionality.  

### Command Line Interface (CLI)  
**Type:** tool  
**Description:** Text-based interface for executing Guardium commands via scripts or administration.  

## Infrastructure  

### Guardium Administration Console  
**Type:** service  
**Description:** Web-based interface for configuring, monitoring, and managing Guardium components and policies.  

### Guardium Installation Manager (GIM)  
**Type:** tool  
**Description:** Deploys, manages, and maintains Guardium software components on database servers.  

## Databases & Data Sources  

### Oracle Database  
**Type:** database  
**Description:** Widely used relational database supported by Guardium for monitoring and protection.  

### IBM Db2  
**Type:** database  
**Description:** IBM data management products family supported by Guardium.  

### MySQL  
**Type:** database  
**Description:** Open-source relational database supported by Guardium.  

### Redis  
**Type:** database  
**Description:** In-memory data store supported by Guardium when using A-TAP.  

## Credentials & Certificates  

### API Key  
**Type:** credential  
**Description:** Secure token for authenticating API requests to Guardium services.  

### Keystore Password  
**Type:** credential  
**Description:** Password accessing keystore storing credentials and certificates for secure communications.

```markdown
## System Operations

### Data Transfer
The `store s2c` command sets parameters for data transfer and collector-aggregator communication. It is relevant when setting up an encrypted Syslog host. If `s2c` succeeds, encrypted traffic can be sent to the host with the correct key.

## Policies & Rules

### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Datasources

### Audit Task
Named entity identified in source; detailed content not extracted.

## Agents & Collectors

### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## APIs & Tools

### grdapi create_user_hierarchy
`userName=ADAMS parentUserName=SCOTT`

## Infrastructure

### Load Balancer Search Sequence
Describes how the load balancer searches failover groups in sequence for an available managed unit when an S-TAP or universal connector fails over to a new unit.

## Knowledge & Workflows

### 946. Verify API key exists
Named entity identified in source; detailed content not extracted.
```

## Collector Architecture

**Description:** A Guardium appliance, either physical or virtual, that ingests activity data from S-TAP agents, enforces security policies, and stores audit records.

## Policy Enforcement and Auditing

**Description:** The Collector receives traffic captured by S-TAP software agents on database servers, applies defined security policies, and records compliant or suspicious activities for auditing and compliance purposes.

## Agent-Collector Interaction

**Description:** S-TAP agents installed on database hosts send collected activity streams to the Collector for centralized analysis, policy enforcement, and storage, ensuring consistent security monitoring across distributed environments.

## Key Components

**Description:** The Guardium ecosystem consists of S-TAP software agents, Guardium Collector appliances, and optional Cloud Services, operating together to monitor, protect, and audit database activity.

## Security Policy Management

**Description:** Policies define rules that allow, block, alert, or log database actions based on users, objects, and operations, enforced by the Collector after S-TAP agents forward activity data.

## Database Integration

**Description:** Supported databases like Oracle and Microsoft SQL Server connect to Guardium via S-TAP agents for real-time monitoring and policy application, enhancing data security and compliance.

## Credential Security

**Description:** API keys and SSL certificates secure communication and API access to Guardium services, ensuring encrypted data transmission and authenticated interactions with the Collector.

## Automated Management

**Description:** GuardAPI and GIM tools facilitate command line and GUI management of policies, deployments, and configurations, streamlining security operations across Guardium deployments.

## Infrastructure Deployment

**Description:** Guardium can be deployed in on-premises data centers or cloud infrastructures such as AWS and Microsoft Azure, providing flexibility in security monitoring setups.

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

## Databases & Datasources

### Oracle DB Instance
**Type:** database
**Description:** An instance of an Oracle database that can be monitored by Guardium agents, providing visibility into database activities and security events.

### SQLGuard IP
**Type:** configuration
**Description:** The primary IP address of the Guardium server used by FAM agents for data collection, with optional failover IPs for redundancy.

---

## Credentials & Certificates

### GuardAppEvent Attributes
**Type:** credential
**Description:** Attributes used to set application events in Guardium, including the date parameter format and event value definitions.

### Admin and User Reports
**Type:** entity
**Description:** Predefined report groups within Guardium tailored to admin and user roles, controlling access to specific reports based on user permissions.

### Guardium API Key
**Type:** credential
**Description:** A secret token used to authenticate API requests to the Guardium system. Must be generated and stored securely.

---

## Cloud Services

### Anomaly Detection Polling Interval
**Type:** service
**Description:** The configuration setting for the polling interval of Anomaly Detection in alert systems, crucial for managing alerting workflows and dependencies.

# Guardium Data Security Overview

## Guardium System
IBM InfoSphere Guardium is a centralized data security platform offering discovery, risk assessment, policy enforcement, and audit reporting for heterogeneous data stores.

## Policies & Rules
- **SAP Authorization Policy**: Defines allowed/disallowed SAP transactions based on authorization objects.
- **PCI DSS Compliance Rule**: Built-in rule for monitoring access to cardholder data.
- **User Activity Alert Policy**: Triggers alerts for predefined user activities to detect threats or violations.
- **Data Masking Rule**: Obscures sensitive data in reports while preserving utility.
- **Database Schema Discovery Policy**: Automatically discovers and categorizes database schemas, tables, and objects.

## Entities & Keywords
- **REST API**: API for programmatic interaction with Guardium.
- **GuardAPI**: Command-line and REST API for managing Guardium components and policies.
- **Active Threat Analytics**: Analyzes security events to flag unusual activities.
- **Outliers Detection**: Identifies anomalous database activities as potential breaches.

## Entities
- **TLS Certificates**: Secure communications between clients and servers.
- **HashiCorp Vault**: Manages secrets and protects sensitive data, integrated with Guardium.
- **DevSecOps Engineers**: Integrate security into DevOps processes.
- **Certification Authorities**: Issue and manage digital certificates for TLS.

## Named Entities
- `92e68b29-6fcf-441e-bb59-aef685bc3f54`
- `d5f72d57-9a58-4fbc-a957-9fa74994ef7f`
- `6c6da195-c5f9-4306-83f6-2a6bb4aec445`
- `f0c1c2d6-50a2-44a0-98f5-54992129101d`
- `fda1e2cc-2d14-47ae-8643-31468414dc13`
- `e15d03ba-6c86-4884-80ba-53301bc70929`
- `be6095f1-5f25-428b-86d6-bc3c683e88ac`
- `dd15ec60-20f5-43b4-a242-e1947028c255`
- `7dda92d5-1b75-44f9-9d94-c36af7b78187`
- `591a5110-ba24-4b73-9e8b-daad6cf38868`

## Examples
- **1026. Oracle example**: Internal exception identifier for SQL exception events.
- **1027. Oracle example**: Attributes capturing connectivity details.

## Agents & Collectors  
### S-TAP (Software TAP)  
**Type:** agent  
**Description:** Captures database activity and forwards it to a Collector; requires root access for shared memory permissions, especially on Linux-UNIX.  

---  

## Policies & Rules  
### Security Policy  
**Type:** policy  
**Description:** Defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.  

---  

## Databases & Data Sources  
### Guardium File Server Agent  
**Type:** configuration  
**Description:** Requires hostname, username, and password for authentication with a Guardium file server.  

---  

## Credentials & Certificates  
### Universal Connector Keystore Keys  
**Type:** api  
**Description:** APIs (add, list, remove) for keystore keys management, with a reinstall step for Kafka Universal Connectors.  

---  

## APIs & Tools  
### File Activity Monitoring (FAM) Policies & Rules  
**Type:** api  
**Description:** Manages FAM policies and rules via create_policy, create_fam_rule, and policy_fam_rule_delete; requires Guardium V11.1 or later.  

---  

## Infrastructure  
### Network Static Routes  
**Type:** entity  
**Description:** `store network routes static` command controls outbound traffic through specified routers.  

---  

## Cloud Services  
### Guardium Audit Type Configuration  
**Type:** api  
**Description:** Configures audit types with `access_key_id` and `audit_type` (dataStream or native) parameters.

## Policies & Rules
**Security Policy**  
A rule set that defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Agents & Collectors
**S‑TAP (Software TAP)**  
A software agent installed on database servers that captures traffic and forwards it to a Collector for analysis and enforcement.  
*Note: Guardium’s guard_monitor automatically runs a guard_diag if S‑TAP CPU usage exceeds the configured threshold.*

## APIs & Tools
**Guardium Export Feature**  
In the Guardium External S‑TAP console, lets users download current External S‑TAP deployment information as CSV or PDF for reporting and audits.

---

*All duplicate or placeholder entries from the original content have been removed.*

## Execute Incident Generation Process (REST API)
**Type:** api  
**Description:** The `execute_incidentGenProcess` command in IBM Guardium generates incidents based on policy violation queries. Available as a PUT REST API, it enables automated incident management in Guardium 9.5+.

### Execute Populate Group From Query (API/Command)
**Type:** api  
**Description:** Specifies target hosts (managed units, groups, IPs, or hosts) for the `execute_populateGroupFromQuery` API/command. Controls execution across managed units, groups, IP ranges, or individual hosts.

## Policy & Rules

### Security Policy
**Type:** policy  
**Description:** Guardium policies define which database activities are logged, alerted, or blocked based on rule set criteria such as user, object, and action.



## Features & Workflows

### Unit Utilization View
Named entity identified in source; detailed content not extracted.

### Building Reports and Setting Alerts
Building reports and setting alerts based on defined thresholds in Guardium. The `VA Tests` domain reports on security assessment tests, and the `Alerts` feature uses the `Guardium Login` domain and `Guardium Users Login` entity. More details are available in other sections.

### Scheduling and Automating Tasks
This excerpt provides a high-level overview of the task steps to configure GUI or sniffer certificates, with instructions organized into numbered sections for execution.

### Verifying API Keys
Steps are given to troubleshoot data source profile connection failures by reconnecting the profile. The exact troubleshooting workflow steps are outlined, with the profile itself being the key entity in the process.

### Managing Inactive S-TAP Agents
This excerpt describes building reports and setting alerts based on defined thresholds in Guardium. It mentions using the `VA Tests` domain to report on security assessment tests, and the `Alerts` feature which utilizes the `Guardium Login` domain and `Guardium Users Login` entity. The passage also hints at more details in other sections.

## Agents & Collectors

### S-TAP (Software TAP)  
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

## Policies & Rules

## Databases & Datasources

## Credentials & Certificates

### Web Certificate Configuration
Settings for configuring client web certificates, including CIDR notation for IP address groups, and conditions using LIKE/NOT LIKE. Specifies actions like VERDICT_TERMINATE if criteria are not met.

## APIs & Tools

### delete_ranger_hdfs_config API
Available in Guardium v11.3+, this REST API allows removal of Hadoop HDFS configurations via a DELETE method call, targeting a specific hostname and port 8443.

### create_datasource Command
Command-line utility to define the type of datasource. Use `--help=true` to obtain valid type values.

## Cloud Services

### Cloud DB Service Protection
Configuration for protecting cloud database services, including naming consumer groups to manage data stream views and impact on data streaming.

## Concise Guardium Overview

### Collector  
**Appliance** that receives activity data from S-TAP agents, applies security policies, stores audit records, and provides centralized reporting.

### S-TAP (Software TAP)  
**Software agent** installed on database servers to capture traffic and forward it to Collectors for monitoring, policy enforcement, and auditing.

### Security Policy  
**Rule set** defining which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

### DB2, SQL Server  
**Databases** supported by Guardium for monitoring, access controls, and compliance reporting.

### Credential  
**Authentication details** used by Guardium components to access databases securely.

### Certificate  
**Digital certificate** for secure communication between Guardium components (e.g., S-TAP and Collectors).

### GuardAPI  
**CLI** for automating Guardium tasks, managing configurations, and retrieving security/audit information programmatically.

### REST API  
**Web interface** for HTTP-based operations like data retrieval, alerting, and policy management.

### Guardium Appliance  
**Dedicated hardware or VM** optimized for running Guardium software securely.

### AWS Guardium Integration  
**Integration** extending Guardium capabilities to AWS environments for monitoring and compliance of AWS databases/services.

# Consolidated Guardium Overview

## Architecture
### Key Components
**Agent:** S-TAP (Software TAP) installed on database servers to capture and forward traffic to Guardium Collectors for analysis and policy enforcement.
**Collector:** Central appliance (hardware or virtual) that receives data from agents, applies policies, and stores audit records.

## Data Management
### Actions
**VA Summary ID:** Reports available security assessment tests.
**VA Tests Domain:** Enables reporting on security assessments for administrator roles.

## Security Management
### Policies
**Security Policy:** Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Infrastructure Setup
### Configuration Tasks
**CPU Settings:** Defines SQL expressions for Guardium tests, including detailed retrieval and executable SQL statements for custom workflows.
**Oracle Configuration:** Example setups for specific functionality, such as Oracle database interactions.

## Credential Management
### Certificates
**Package Usage:** Provides instructions for using a packaged .tgz file for credential management from the releases directory.

## Tools Integration
### API and Special Handling
**APIs:** Includes specific handling for TRANSFORM actions (1300, 1301, 1302, 1304) and registry certificate installation on cluster nodes (1310).
**Tools:** Supports Oracle examples (1302, 1304) and features like FAM_PROTECT_PRIVILEGED for managing privileged access (1303).

e:** credential  
**Description:** Command to retrieve the registry certificate used by Guardium for authentication and secure communication.

**Database Session Attributes**  
*Key session-level attributes for session-level policy rules include `DB_TYPE` (database type) and `NET_PROTOCOL` (network protocol). `DB_TYPE` is recommended over `SERVICE_NAME` because `NET_PROTOCOL` can vary during a session and is therefore unreliable for consistent policy evaluation.*  

---

## Compressed Guardium Reference

### Cloud Services

**AWS Identity and Access Management (IAM)**
- Manages access to AWS services; required for protecting cloud databases with Guardium features.

### Infrastructure

**Load Distribution**
- Balances S-TAP traffic among secondary Collectors by threading intercepted connections for efficient traffic handling.

**Guardium Managed Receiver (GMR)**
- Securely receives and stores audit data from S-TAP agents, forwarding it to Collectors for processing and analysis.

### Agents & Collectors

**Colletor**
- A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

**S-TAP (Software TAP)**
- A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### APIs & Tools

**API Target Host**
- Configuration property; determines target hosts for API execution (all_managed, all, group:<group name>, or specific host name).

**GRDAPI**
- Guardium REST API; provides programmatic access to Guardium's features and data for automation and integration with external systems.

### Policies & Rules

**Security Policy**
- A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

### Keywords for Policy Creators

**DUAL MODE**
- Configuration option that allows a Guardium appliance to operate in both active and passive modes for load balancing and failover scenarios.

**REGEX**
- Regular expression pattern used in rule conditions to match specific text patterns in query strings or data values.

**SELECTIVE AUDIT TRAIL**
- Policy setting that filters which audit records are captured based on defined criteria, ensuring only relevant activity is logged.

**TIMESTAMP**
- Attribute appended to audit records or query results indicating the exact time an event occurred.

---

*Note: Named entities such as "Data Source Property Update API", "Client Web Certificate Configuration", "GuardAPI Query Load Balancer Map", and "GIM Unassign Client Module Endpoint" were identified but detailed content was not extracted.*

## Entities & Collectors

### Security Policy
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

---

## Policies & Rules

### S-TAP Monitoring Mechanisms Support Matrix
**Type:** configuration  
**Description:** This excerpt introduces the S-TAP monitoring mechanisms support matrix available in Linux-UNIX environments, guiding users to select appropriate setups based on monitoring or blocking requirements. The matrix is essential for configuring S-TAP to match specific operational needs, including supported data types and architectures for effective monitoring.

## Cloud Services

### A-TAP Configuration for Db2
**Type:** cloud service  
**Description:** Configuration parameters required for setting up A-TAP on a Db2 database, including `db_instance`, `db_type`, and `db_version`, to enable auditing and monitoring in cloud environments.

ng intermediate group levels.

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** A rule set that defines database activities to allow, log, alert, or block based on user, object, and action criteria.

---

## Workflows

### Configuring GAM Service Monitoring
**Type:** workflow
**Description:** Set service name, monitoring interval, memory limits, and custom event actions for Windows Guardium services.

### Guardium High Availability Network Configuration
**Type:** workflow
**Description:** Enable/disable HA on interfaces and select active-backup or passive-backup modes via CLI.

---

## Entities

### Audit-Delete Role
**Type:** entity
**Description:** Allows deletion of audit results with tracking in the User Activity Audit Trail; Admin users have same privileges.

### VMWare Tools Installation
**Type:** entity
**Description:** Install via CLI or documentation for VMware integration.

---

## Knowledge Base

### DB2 Error in Diagnostic Log
**Type:** knowledge
**Description:** Error occurs after setting DB2 COMM_EXIT_LIST to Guardium's `libguard` and restarting the DB2 server, critical for troubleshooting.

## Workflows

### Azure SQL and Cosmos Data Source Identification
**Type:** workflow
**Description:** Navigate the Azure dashboard to find Azure SQL and Cosmos data source resource IDs from the URL for API integrations and data source management.

## Policies

### Security Policy
**Type:** policy
**Description:** Defines allowed, logged, alerted, or blocked database activities based on user, object, and action.

## Agents

### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic and forwards it to a Guardium Collector for real-time analysis.

### Guardium Collector
**Type:** appliance
**Description:** Receives traffic from S-TAP agents, applies security policies, and stores audit records.

## Database

### Oracle
**Type:** database
**Description:** Relational database monitoring and protection through Guardium.

## Credentials

### Client Web Certificate
**Type:** credential
**Description:** Authenticates client access to Guardium web interfaces.

## APIs

### grdapi create_user_hierarchy
**Type:** api
**Description:** Creates hierarchical user relationships for role-based access control.

## Infrastructure

### Firewall Permissions
**Type:** configuration
**Description:** Network rules and CLI commands for FPolicy communication with Hitachi storage devices.

## Cloud Services

### Distributed Reports
**Type:** service
**Description:** Sends data from Guardium managed units to a central data mart for unified reporting.

## Agencies & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent deployed on database hosts to capture live database traffic and relay it to a Guardium Collector for analysis and policy application.

### Guardium Collector
**Type:** appliance  
**Description:** A dedicated hardware or virtual device that aggregates traffic data from multiple S-TAP instances, applies security policies, and stores audit trails.

---

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** A collection of enforcement rules that define how Guardium should handle various database activities, such as allowing, logging, alerting on, or blocking specific actions based on criteria like user, object, and operation.

---

## Entities & Keywords

### Audit Process Definition
**Type:** entity  
**Description:** Identifies an audit process by its name and defines the time window (start and end timestamps) for which the audit data should be deleted.

### TRANSFORM Action
**Type:** keyword  
**Description:** Refers to a specific workflow entity identified by UUID `d9d857c7-f4d8-47c6-9b18-6aa04a72791c`, used in data transformation operations within Guardium workflows.

### Suspected Malicious Stored Procedures
**Type:** entity  
**Description:** A predefined report category that identifies potentially harmful stored procedures, configurable through the Guardium UI by selecting receiver options and customization icons.

### Oracle Database Activity Log
**Type:** entity  
**Description:** Represents a log entry from Oracle databases containing fields such as username, source program, timestamps, protocol information, and SQL statements, captured for security auditing.

### Oracle SQL Report by Client IP
**Type:** keyword  
**Description:** A reporting feature that filters and displays SQL activities based on the originating client IP address, useful for tracking external access patterns.

### STAP Verification Attributes
**Type:** entity  
**Description:** Attributes associated with the verification status of S-TAP agents, including primary key, verification result, status, and timestamp, used for auditing agent health.

### Data Mart Extraction
**Type:** keyword  
**Description:** Describes the process of exporting aggregated security data from Guardium into CSV format for external reporting or analysis, optimizing online report performance.

### Access and Audit Rules
**Type:** keyword  
**Description:** Describes hierarchical privilege rules that determine access levels and audit requirements, necessitating higher privileges or exemptions when lower-level policies conflict.

### Guardium S-TAP Installation
**Type:** workflow  
**Description:** The process of deploying or upgrading the S-TAP agent on database servers, supporting both interactive and non-interactive installation modes across various operating systems.

### Health Check Patches
**Type:** keyword  
**Description:** Pre-upgrade patches that perform system checks to ensure a smooth upgrade process, distinct from regular functional patches.

### Database Server Installation Path
**Type:** entity  
**Description:** Specifies the filesystem path where the Guardium Database Server binaries and related services are installed, typically verified via system commands like `ps` and `grep`.

### Number Sign
**Type:** keyword  
**Description:** Placeholder for an unspecified entity; additional context or content required for a complete description.

---

## Databases & Data Sources

### MongoDB Container Connection
**Type:** datasource  
**Description:** Specifies iptables rule configurations to allow external IP addresses to access a MongoDB container running on port 27017, tailored for scenarios involving External S-TAP deployments.

---

## Credentials & Certificates

## High‑Level Overview of Guardium Categories

### Certificates & Credentials
- **Scanner Connection Debugging** – Troubleshooting workflow for scanner, Guardium server, and assessment connectivity.
- **Registry Certificate Skipping** – Named entity; details not extracted.
- **Sniffer certificate key** – Named entity; details not extracted.

### APIs & Tools
- **grdapi gim_get_modules_running_status** – Lists running modules/bundles; available from Guardium V9.5.
- **grdapi gim_install_bundle** – Named entity; details not extracted.
- **PUT /restAPI/bundles** – REST API for managing bundles; supports versioning from Guardium V9.5.
- **delete_adhoc_policy_analyzer** – Guardium V11.1+ DELETE method for removing ad‑hoc policy analyzers; requires `api_target_host`.
- **delete_ranger_hdfs_config** – Deletes HDFS Ranger configuration; `api_target_host` specifies target.
- **store guarduser_state** – Disables user accounts; view states with `show guarduser_state`.
- **verify_api_key_exists** – Checks for API key existence in Guardium Data Protection.

### Infrastructure
- **Network Redundancy Features** – Details on IP‑high‑availability status and network interface displays indicating redundancy configurations.

### Databases & Data Sources
- **Oracle** – Relational DBMS supporting the “Audit Process Log” report; accessible only to admin users.

### Agents & Collectors
- **S‑TAP (Software TAP)** – Software agent installed on DB servers to capture traffic and forward it to a Guardium Collector for real‑time analysis and policy enforcement.

### Datasets
- **Data source** – Configured data source managed via UI or GuardAPI.

### Credentials & Certificates
- **Shared Secret Key** – Encryption key used for securing communications (excerpt truncated).

```markdown
## Infrastructure

### api_target_host
Specifies the target host for API commands. Use IP or hostname; from a central manager, use managed unit IPs matching the network IP mode. Acceptable formats are hostname or IPv4/IPv6.

## Features & Entities

### CLI Syntax for Network Interfaces
Defines the syntax for configuring secondary network interfaces, including IP assignment, gateway specification, and mutually exclusive IP teaming settings.

## Agents & Collectors

### S-TAP (Software TAP)
Installs on database servers to capture and forward database traffic to a Guardium Collector for analysis and policy enforcement.

### Collector
Aggregates data from S-TAP agents, applies policies, and stores audit records.

## Policies & Rules

### Security Policy
Rule set defining permitted database activities, logging, alerts, and blocks based on user, object, and action criteria.

## Databases & Datasources

### Informix Configurations
Specifies paths and directories for Informix database execution and installation.

## Credentials & Certificates

### Credential Verification
The `update_credential` command returns appliance details: hostname, IP, unit type, Guardium version, and installed patch.

## APIs & Tools

### get_istap_config
Retrieves I-TAP configuration settings via `https://<host>:8443/restAPI/get_istap_config?datasourceName=<IP_or_name_of_server>`.
```

## Guardium Policies
**Type:** policy  
**Description:** Configurable rule set that determines which database activities are allowed, logged, alerted, or blocked based on criteria such as user, object, and action.

## Guardium Databases and Datasources
**Type:** database  
**Description:** Named entity identified in source.

## Guardium Credentials and Certificates
**Type:** credentials  
**Description:** Base64-encoded content of the `va-scanner` secret.

## Guardium Tools and APIs
**Type:** api  
**Description:** kubectl secret inspection command (`kubectl get secret ... -o jsonpath`) for extracting Guardium Data Protection host IP.

## Guardium Infrastructure
**Type:** configuration  
**Description:** HAProxy frontend configuration for SSL termination and Neo4j traffic forwarding with proxy protocol handling.

## Guardium Command and Control
**Type:** commands  
**Description:** iptables chain management for Neo4j traffic, including create, flush, delete, and add rule commands.

## 1820. Use the server.pem file that matches your certificate hostname
**Type:** configuration  
**Description:** Procedure to extract and verify the fingerprint of a certificate from `server.pem` using OpenSSL commands on macOS and Linux.

## Agents & Collectors
**Type:** agent  
**Description:** S-TAP (Software TAP) captures database traffic on database servers and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

## Credentials & Certificates
**Type:** credential  
**Description:** Base64-encoded `va-scanner` secret content.

## APIs & Tools
**Type:** tool  
**Description:** kubectl command to retrieve and decode the `va-scanner` host IP from a Kubernetes secret.

## Databases & Data Sources

### IBM Informix
**Type:** database
**Description:** IBM Informix is a relational database management system (RDBMS) designed for online transaction processing (OLTP) and mixed workload environments, supporting both SQL and NoSQL data models.

## System Information

**ens32 MAC address**
- **Type:** entity
- **Description:** Required for generating secure keys, obtained with `support execute info`.

## Documentation & Reports

**Report Title**
- **Type:** documentation
- **Description:** Placeholder for metadata or configurations.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic to Guardium Collector.

### Collector
**Type:** appliance
**Description:** Receives data from S-TAP, applies policies, stores audit records.

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** Defines allowed, logged, alerted, or blocked database activities.

## Databases & Datasources

### Oracle Autonomous Database Connection
**Type:** datasource
**Description:** Needs wallet file, user credentials, additional password parameters.

## Credentials & Certificates

### set_certificate_host_validation API
**Type:** api
**Description:** GuardAPI command to enable/disable certificate host validation with `enable` and optional `api_target_hostString`.

## APIs & Tools

### set_certificate_host_validation API
**Type:** api
**Description:** Enables or disables certificate host validation via Boolean parameter `enable` and optional `api_target_hostString`.

### CAS Template List API
**Type:** api
**Description:** REST call to list CAS templates by name with Authorization token, returning JSON.

### Assessment API Suite
**Type:** api
**Description:** Manages assessment-related tasks, including deletion of datasources, tests, and results.

### Datasource Management API
**Type:** api
**Description:** Functions to create, delete, and list datasource references by IDs or names.

### Cloud Datasource Management API
**Type:** api
**Description:** Manages cloud datasources, supports streaming and assigning collectors.

### Catalog Entity Management API
**Type:** api
**Description:** Manages data archive and result archive files.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic, forwards to Guardium Collector.

### Collector
**Type:** appliance
**Description:** Receives activity data from S-TAP, applies policies, stores audit records.

## Policies & Rules

### Security Policy
**Type:** policy
**Description:** Configured rule set for allowed, logged, alerted, or blocked database activities.

## Databases & Datasources

### Oracle
**Type:** database
**Description:** *Entity identified in source; content not extracted.*

### MySQL
**Type:** database
**Description:** *Entity identified in source; content not extracted.*

### PostgreSQL
**Type:** database
**Description:** *Entity identified in source; content not extracted.*

### DB2
**Type:** database
**Description:** *Entity identified in source; content not extracted.*

### Informix
**Type:** database
**Description:** *Entity identified in source; content not extracted.*

## Credentials & Certificates

### Credential
**Type:** credential
**Description:** Stored database login details for S-TAP.

### Certificate
**Type:** certificate
**Description:** Authenticates communication between S-TAP and Guardium Collectors.

```markdown
## Credentials & Certificates
### set_certificate_host_validation (API)
Enables or disables certificate host validation. Boolean `enable` controls validation; optional `api_target_hostString` targets specific host.

## Agents & Collectors
### S-TAP (Software TAP)
Software agent on database servers capturing traffic for real-time analysis by Guardium Collectors.

### Collector
Guardium appliance receiving S-TAP data, applying policies, and storing audit records.

## Policies & Rules
### Security Policy
Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## APIs & Tools
### api_target_host Parameter
Specifies Guardium API call targets: `all_managed`, `all`, or `group:<group name>`. Defines execution scope across managed units, central manager, or specific groups.
```

### add_oracle_datasource
**Type:** api  
**Description:** Registers an Oracle database as a data source with Guardium. Requires the database host, port, SID, service name, and credentials.

## Agents & Collectors
### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## APIs & Tools
### REST API: Set Universal Connector Data Timeout
The `setUniversalConnectorDataTimeout` function sets the data timeout for the Universal Connector. Requires Guardium hostname or IP address, POST method. Related to IBM Guardium Data Protection.

### REST API: Stop ISTAP Monitor
`stop_istap_monitor` stops monitoring for a specified datasource. Requires `datasourceName` parameter. Manages data source connections and monitoring activities.

# Guardium Reference

## Security Policy
A rule set that defines database activity handling based on user, object, and action.

## S-TAP (Software TAP)
Installs on database servers to capture traffic for real-time analysis.

## Collector
A Guardium appliance that receives, analyzes, and stores activity data.

## Security Policy
Defines allowed, logged, alerted, or blocked database activities by user, object, and action.

## HDFS
Apache Hadoop Distributed File System instance for storage.

## API Target Host Specification
Specifies the target host(s) for API commands, using hostname, IP address, or group.

## Infrastructure  

### GUI Access Configuration  
Settings for configuring access to the Guardium GUI, including IP address assignments, network ports, and host name configurations for system administrators and users.  

## Cloud Services  

### Guardium Data Protection on AWS  
Integration of Guardium Data Protection within the AWS environment, leveraging AWS services for data storage, monitoring, and compliance, with support for EC2 instances and S3 buckets.  

## Agents & Collectors  

### S-TAP (Software TAP)  
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  

### Collector  
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.  

## Policies & Rules  

### Security Policy  
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.  

## Databases & Datasources  

### API Target Host  
Named entity identified in source; no detailed content extracted.  

### Get Fields Titles API  
Retrieve column name mappings via the `getFieldsTitles` API. Specify `rows` and `pivotBy`; explore `inputTZ` for valid values.  

### Update Datasource  
Update a datasource using parameters like `id`, `importServerSSLcert` (0/1), `KerberosConfig`, and `newName`. Each parameter modifies a specific aspect of the datasource configuration.  

### Connect Cloud Accounts  
Connect Azure or Google Cloud Project accounts to Unified Discovery and Classification. Parameterize the integration by specifying subscriptions, projects, user permissions, and roles.  

## Asset Management  

### Asset Inventory  
A system function that displays sensitivity information for on‑premises assets and cloud/SaaS applications. The **Asset inventory** page can be opened from the main menu and shows vulnerability and sensitivity data for each listed asset.  

## Reporting & API  

### Report Title (2047)  
REST API **GET** service **list_datasource_by_name** – retrieves the definition of a datasource by name. Available from Guardium V9.5 onward.  

### Report Title (2048)  
REST API **GET** service **list_policy** – returns the list of policy names in Guardium. Extends to **list_policy_fam_rule** for detailed file‑activity monitoring (FAM) rule checks.  

### Report Title (2049)  
Header-only excerpt – only part of the REST API workflow is described.  

### Report Title (2050)  
Parameter **api_target_host** – specifies the host where an API executes. Valid values: managed unit host name or IP, **central manager** host name or IP, or a group name (managed units only).  

### Report Title (2051)  
The **Universal Connector** GET REST API lets you manage its configuration. The `enable_metrics` parameter accepts `0` (false) or `1` (true); `api_target_host` defines which hosts execute the request.  

### Report Title (2052)  
Demonstrates execution of the **api_target_host** parameter. The API can run on the **central manager** or any listed **managed units**; host names/IPs are supplied as arguments. Example: run on `cm_host` and `mu_host01`.  

### Report Title (2053)  
Parameters for extracting audit data from cloud databases in IBM Guardium. `region` is required for AWS; `primaryCollector` identifies the collector that performs the extraction. Introduces entities such as **cloud databases** and **collectors** and product‑specific terms.  

## Agents & Collectors  

### S-TAP (Software TAP)  
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  

### Collector  
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.  

## Policies & Rules  

### Security Policy  
A security policy consists of rule sets that determine which database activities are monitored, logged, or blocked based on user criteria.

## Credentials & Certificates
### Kerberos Authentication Setup
**Type:** configuration
**Description:** Modify `krb5.conf` with realm and domain info, update `/etc/hosts`, and verify KDC settings for secure database access.

## APIs & Tools
### API to List Auto-Discovery Processes
**Type:** api
**Description:** Guardium API endpoints list active auto-discovery processes, including SQL injection and STP cases, via specific process IDs.

### list_group_by_desc Command
**Type:** api
**Description:** Accepts `api_target_host` and `desc` parameters to query target hosts based on group descriptions.

## Infrastructure
### Unified Discovery and Classification Setup
**Type:** tool
**Description:** Install script from tar file and run `pre-install.sh` to check prerequisites for unified data discovery.

## Databases & Data Sources
### GDPR Data Databases Chart
**Type:** database
**Description:** Lists sensitive databases by data type and quantity to prioritize GDPR compliance efforts.

## Keywords
### Purge Reports Details
**Type:** keyword
**Description:** Scheduler log entries include detailed sections for purge jobs with metadata on job configuration and execution.

## Knowledge
### API Target Host Parameter
**Type:** knowledge
**Description:** `api_target_host` determines API execution target, accepting values like 'all_managed' or 'group:<group name>'.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent
**Description:** Captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Type:** appliance
**Description:** Receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
**Type:** policy
**Description:** Defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Workflows & Entities
### SMART_CARD_MAPPING_REGEX Configuration
**Type:** workflow
**Description:** Configure using `store property value SMART_CARD_MAPPING_REGEX "<regex>"` to map smart card user information correctly.

## Entities & Keywords
### API Target Host Parameter
**Type:** entity
**Description:** Specifies target hosts (managed units, central manager, or group) for API execution.

### SaaS Application Connection
**Type:** entity
**Description:** Connection process for SaaS applications via Unified Discovery and Classification interface.

### Sensitivity Identifier Sub-Type
**Type:** entity
**Description:** Lists identifier-type sensitivities on Asset inventory page, referenced for examples or further details.

### Trial Sign-Up Instructions
**Type:** entity
**Description:** Steps for signing up for Guardium Data Protection trial, including material download, installation, and license activation.

### VM Configuration Post-Installation
**Type:** entity
**Description:** Configure network settings using commands to set IP address, network interface, resolver, and routes.

## Knowledge & Features
### GET REST API Method for runUniversalConnector
**Type:** knowledge
**Description:** Enables/disables metrics and specifies execution targets via `GET /restAPI/runUniversalConnector`.

### Data Mart Entry Parameters
**Type:** knowledge
**Description:** Required "Name" parameter followed by optional parameters like `extracted_date_max_limit`, `initial_start`, `time_granularity`, and `linesPerFile`. `extracted_date_max_limit` can take values `<`, `>`, or `:` with a timestamp in various formats.

## Agents & Collectors
### S-TAP Configuration
**Configuration Setting:** `S_TAP_CONFIG`
**Description:** Controls the behavior and settings of the S-TAP agent installed on the database server.

## Policies & Rules
### Update Classifier Policy
**Command:** `update_classifier_policy`
**Description:** API command to modify classification policies using parameters like `policyName` and `classification`.

## APIs & Tools
### Update Cloud Datasource
**Command:** `update_cloud_datasource`
**Description:** API command requiring `cloudTitle` to update cloud datasource configurations.

## Infrastructure
### API Target Host
**Setting:** `api_target_host`
**Description:** Determines the target for API execution, including managed units and central managers.

## Cloud Services
### Update Ranger HDFS Config
**Command:** `update_ranger_hdfs_config`
**Description:** Configures HDFS monitoring by specifying `ldLibraryPath` for JVM library location.

## Cloud Services
### Cloud Account Configuration
**Feature:** Cloud Account Management
**Description:** Manages cloud accounts within the Unified Discovery and Classification UI.

## Databases & Datasources
### Ambari Server Configuration
**Configuration:** SSL and Connection Settings
**Description:** Configures SSL and SSL-enabled user interface port for secure Ambari server connections.

## Credentials & Certificates
### Confluence Read-Only Permissions
**Credential:** Confluence Account
**Description:** Specifies read-only access permissions for Confluence data types and users.

## Infrastructure
### SSL Configuration for Ambari Server
**Configuration:** SSL Settings
**Description:** Enables SSL and defines the user interface port for secure communication with the Ambari server.

## Knowledge
### Sensitive Information Types
**Types:** HIPAA, PCI, SG, UEN, SSN
**Description:** Identifies sensitive information types categorized as Personal or Financial in the asset inventory.

## Guardium CLI Command

**list_ranger_configs**  
Lists all Apache Ranger configurations (clusters) on a Guardium appliance, independent of IP mode.

## GuardAPI

**store_sql_credentials**  
Stores database connection credentials securely.  
*Required fields:* `password`, `stapHost`.

## Keywords

**api_target_host**  
Specifies the target host for an API. It accepts either a hostname or an IP address, and its behavior is independent of the IP mode configuration. On managed units, the command runs only on the host identified by `api_target_host`. The hostname remains agnostic to IP mode when applied to a registered unit.