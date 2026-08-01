# Permissionstodynamicrolesandcredsfordifferentpaths — KEYWORDS

**Category:** keywords  |  **Generated:** 2026-07-09  |  **Source:** gdp-12.x-documentation.pdf

---

## Guardium Features and Components

- **A-TAP**: Intercepts database calls made directly on the server.
- **Aggregator**: Consolidates activity data from multiple Collectors.
- **Audit Process**: Analyzes S-TAP data and stores it in the repository.
- **CAS**: Detects and records changes to database objects.
- **Central Manager**: Coordinates audit activities across RAS environments.
- **Collector**: Receives, processes, and stores database activity.
- **Data Privacy**: Masks credentials in database traffic.
- **FAM**: Monitors access to unstructured data files.
- **G-CENT**: Central management console for large deployments.
- **GDPR**: Ensures compliance with EU data protection regulations.
- **GIM**: Remotely deploys and manages S-TAP agents.
- **GuardAPI**: Command-line and REST interface for automation.
- **K-TAP**: Linux kernel module for OS-level traffic interception.
- **Log Buffer Size**: Configures memory buffer for Audit Process logs.
- **Masking Engine**: Applies data masking rules to traffic.
- **MSSQL**: Supports detailed inspection of Microsoft SQL Server.
- **Password ID**: Identifies stored passwords in Guardium.
- **Policy Manager**: Evaluates database activity against policies.
- **Policy Violation**: Alerts on breaches of defined policies.
- **QDBB**: Tracks pending log entries for Audit Process.
- **Query Stream**: Continuous flow of captured database queries.
- **Reconciliation**: Ensures data consistency across components.
- **Remote Path**: References files located outside Guardium.
- **RNG**: Manages reporting and alert distribution.
- **Sanctioned Validation**: Permits authorized security assessments.
- **S-DAQ**: Supports advanced real-time data analysis.
- **S-GATE**: Enforces real-time database access policies.
- **S-TAP**: Captures and forwards database traffic.
- **S-TAP Status**: Reports health and connectivity of agents.
- **Sanitize Credentials**: Removes sensitive authentication data.
- **System Level**: Operates at kernel level for traffic interception.
- **Time Sync**: Synchronizes clocks across Guardium components.
- **User Consent**: Requires authorization for certain operations.
- **Vault**: Secure storage for sensitive data.
- **Whitelist**: Exempts approved entities from monitoring.

## Overview of Guardium Architecture

Guardium coordinates agent-hosted activities across distributed environments. It enables deployment of policies, creation of snapshots, and management of appliances from a central portal, with master-slave relationships determining information flow direction. This simplifies the management of multiple appliances.

## Key Modules and Components

**Aggregator** consolidates activity data from multiple Collectors for enterprise-wide reporting.

**Collector** receives, processes, and stores database activity data forwarded by S-TAP agents.

**S-GATE** enforces real-time database access policies and blocks or masks unauthorized queries.

**S-TAP** captures and forwards database traffic to a Guardium Collector.

**GIM** centrally deploys, upgrades, and manages S-TAP agents across database servers.

**CAS** detects and records changes to database schemas, stored procedures, and object configurations.

**FAM** monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

**K-TAP** intercepts OS-level database socket traffic on Linux servers for Guardium monitoring.

## Supported Databases and Technologies

Guardium supports:

* **CockroachDB**: High-availability distributed SQL database.
* **Couchbase**: NoSQL database requiring inspection engine setup.
* **Datastax Cassandra**: Distributed NoSQL database with specialized drivers.
* **Db2**: IBM relational database requiring inspection agents.
* **ElasticSearch**: Search and analytics engine for datasource configuration.
* **MongoDB**: Document-oriented NoSQL database needing specialized inspection.

## Security and Compliance

Guardium supports GDPR compliance through discovery, masking, and audit trails. It uses Elliptic Curve Cryptography for secure connections and AWS services like IAM roles and EC2 instances for deployment and management.

## Guardium Overview

IBM OpenPages provides a governance, risk, and compliance platform integrated with Guardium for comprehensive data protection insights. Passport Advantage is IBM's program for software distribution offering access to Guardium features and updates, ensuring proper licensing and version control.

## Components and Solutions

Guardium integrates with a Password Vault for secure credentials management, ensuring protected access to datasources and system components. Performance Optimization is a focus area of Guardium, maintaining system efficiency while delivering comprehensive monitoring and reporting capabilities.

## Supported Databases and Services

PostgreSQL, Redis, and RDS (Amazon Relational Database Service) are supported for datasource configuration in Guardium, requiring secure connection settings and query analysis. S3 (Amazon Simple Storage Service) is supported for integration with the FAM module to monitor and secure access to unstructured data in cloud storage.

## Key Guardium Technologies

S-TAP is IBM Guardium's software agent installed on database servers, capturing and forwarding database traffic to a Guardium Collector. Threshold Monitoring allows Guardium to set and report on performance and security thresholds, alerting administrators to potential risks or anomalies.

## Deployment and Configuration

Unix operating systems are supported for Guardium deployments, requiring Inspection Engines and specific configuration settings for comprehensive monitoring. Vault System is IBM's security solution for managing secrets and credentials, integrated with Guardium for secure credentials management.

## Security and Compliance

WAS (IBM WebSphere Application Server) is supported for integration with Guardium to protect application data and transactions. X-Force is IBM's threat intelligence service that can be integrated with Guardium for enriched security insights and proactive defense strategies.

## Monitoring and Reporting

Query Analysis is a core capability of Guardium, enabling parsing, inspection, and auditing of database queries to detect anomalies and non-compliant access patterns. Audit processes involve reviewing and analyzing database activity to ensure compliance with security policies and regulatory requirements.

## Data Protection Measures

Backup procedures are critical for creating copies of Guardium data and configurations to ensure recoverability in case of data loss or system failures. Block actions are enforced by Guardium to prevent unauthorized access or malicious activities within monitored databases, guided by security policies.

## Communication and Encryption

Public Key encryption components are used in Guardium for secure communication between agents and collectors. X-PTZ is Guardium's proprietary protocol for secure communication between S-TAP agents and collectors, ensuring encrypted and authenticated data transmission.

## Data and Infrastructure

Custom attributes allow tailoring Guardium configurations to specific organizational needs. Discovery is an automated process in Guardium to identify and catalog database servers, datasources, and configurations within the enterprise environment.

## Quality Assurance

Validation processes verify Guardium installations and configurations, ensuring they meet security and compliance standards.

```markdown
## Compact Guardium Reference

### Core Components
- **S-TAP**: Captures and forwards database traffic to a Collector.
- **A-TAP**: Kernel-level agent intercepting local application calls on the database server.
- **Collector**: Receives, processes, and stores data from S-TAP agents.
- **Aggregator**: Consolidates data from multiple Collectors for enterprise reporting.
- **K-TAP**: Kernel module for Linux, intercepting socket traffic for monitoring.

### Modules & Features
- **CAS**: Detects and records database schema, stored procedure, and object configuration changes.
- **FAM**: Monitors unstructured data file access on NAS, SharePoint, etc.
- **S-GATE**: Enforces real-time access policies, blocking or masking unauthorized queries.
- **GDPR**: Supports compliance with EU data protection regulations.

### Management & Integration
- **GIM**: Remote deployment, upgrade, and management of S-TAP agents.
- **Kerberos Authentication**: Supports Kerberos for user and system authentication.
- **SSO**: Integrates with external identity providers for single sign-on.
- **Patch Management**: Distributes security updates to S-TAP agents.

### Security & Compliance
- **Security Policy**: Rules governing data access and usage.
- **Vulnerability Assessment**: Identifies and prioritizes security vulnerabilities.

### Infrastructure
- **Appliance**: Physical or virtual Guardium device performing specific functions.
- **Datasource**: Defined connection for database, file system, or other data source.
```

## Core Components
- **A-TAP**: Kernel-level agent intercepting local application database calls on the server.
- **Aggregator**: Guardium appliance consolidating data from multiple Collectors.
- **CAS**: Module detecting changes to schemas, stored procedures, and configurations.
- **Collector**: Appliance receiving, processing, and storing activity data from S-TAPs.
- **FAM**: Module monitoring unstructured data file access on NAS and SharePoint.
- **Guardium**: Suite offering data security and compliance solutions.
- **GIM**: Tool for deploying, upgrading, and managing S-TAP agents remotely.
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic.
- **S-GATE**: Real-time database access policy enforcement and query blocking.
- **S-TAP**: Agent capturing and forwarding database traffic to Collectors.

## Related Concepts
- **JDBC Connection**: Requires hostname/IP, port 2638, database name, and properties for successful datasource connection.
- **CyberArk Integration**: Workflow for creating application objects in CyberArk for Guardium datasource management.
- **Data Protection**: GDPR compliance supported by Guardium through discovery, masking, and audit trails.
- **Installation Management**: GIM facilitates centralized S-TAP agent deployment and management.
- **File Monitoring**: FAM ensures security by monitoring file access across various storage solutions.
- **Encryption and Security**: MongoDB security keyfile and Couchbase TDE configurations highlighted.
- **Oracle and SQL Server**: Paths for Oracle Home Directory and Windows SQL binaries specified.
- **Patch and Policy Management**: Patch Manager and Central Policy Manager roles in centralized patch and policy distribution.

## Guardium Features

**Cost Savings Measurements**  
Guardium can display cost savings in either U.S. dollars or hours, letting executives view financial impact in a metric that best supports business decisions.

**Aggregator Appliance**  
The Guardium Aggregator appliance acts as the central management point for federated management, access control, patching, and metadata repository functions.

## Managing Datasource Credentials  

| Platform | Article |
|----------|---------|
| AWS Secrets Manager | [Managing datasource credentials with AWS Secrets Manager] |
| HashiCorp | [Managing datasource credentials with HashiCorp] |
| Custom properties | [Managing datasource credentials with custom properties] |

These three knowledge articles walk through the procedures for retrieving and applying credentials stored in the three supported secret stores.

**MSSQL Custom Properties via GRDAPI**  
Add `TRANSACTION-ISOLATION-LEVEL` and `MAXDOP` as custom properties to an MSSQL datasource:

```shell
grdapi update_datasource_custom_property name="TRANSACTION-ISOLATION-LEVEL" value="READ_COMMITTED_SNAPSHOT" datasource_type="MSSQL" datasource_id=123
grdapi update_datasource_custom_property name="MAXDOP" value="4" datasource_type="MSSQL" datasource_id=123
```

See the *[Custom Properties Help PAM Document]* for the full list of supported properties and usage examples.

## Apache Cassandra Configuration

- RPM installations place the configuration directory at **/home/cassandra/apache-cassandra-4.x/conf**.  
- For .tar installations the path is **$installpath/conf**.  
- Consult the *[Aster Datasource Configuration]* for settings that also apply to Cassandra.

## Informix SSL Support

Guardium supports encrypted connections to Informix databases via SSL. The **Host Name/IP** field is required when configuring the datasource; mutual SSL authentication is **not supported** for Informix.

## MySQL Configuration Restrictions

- Database names **must be ASCII only**; Unicode names are rejected.  
- The optional environment variable **MYSQL_HOME** may be defined to point at a custom MySQL base directory.  

These restrictions ensure reliable datasource creation and avoid character‑set issues.

## MySQL Log Locations

```text
log_error=/opt/IBM/data/mysql/mysql-error.log
general_log_file=/opt/IBM/data/mysql/localhost.log
```

These system paths indicate where the error and general query logs are stored for a typical MySQL installation.

## rce Configuration
### DataSource Setup
Provide host, port, database name, and credentials to connect Guardium to a database.

## IAM
### Identity and Access Management
AWS service for creating and managing user access to AWS resources.

## Compliance Template
### Policy Blueprint
Pre‑defined set of controls and rules for data governance standards.

## DPDPA
### Digital Personal Data Protection Act
Indian law governing personal data; Guardium offers a compliance template.

## security credentials
### Access Tokens
Tokens that verify identity when accessing protected resources.

## credential type
### Authentication Class
Category of authentication method (local, LDAP, Kerberos, SSL) for data sources.

## parameter set
### Definition List
Grouped collection of fields to configure a data source connection.

## verify patch status
### Verification Process
Confirm a Guardium system patch has been successfully installed.

## A-TAP
### Application TAP
Guardium kernel‑level agent that intercepts database calls made by local applications directly on the server.

## AWS‑Secrets‑Manager
### Secret Management Service
AWS service for storing, managing, and retrieving secrets.

## IAM‑Role‑ARN
### IAM Role Amazon Resource Name
Unique identifier for an IAM role that grants permissions to AWS resources.

## Guardium Security Overview

Guardium employs Kerberos v5 for secure authentication, supporting multiple encryption types to ensure data integrity and confidentiality. It offers S-TAP agents for monitoring database traffic on Linux and UNIX systems, forwarding data to Guardium Collectors for analysis. Guardium's certifications align with NIST standards, ensuring compliance with security and privacy regulations. The product provides granular visibility into Oracle ASM disk group activities and focuses on managing privileged user access. Real-time query policies are enforced using S-GATE, which blocks or masks unauthorized queries. Guardium supports RBAC models and provides REST APIs for automation. It includes features like S-GATE for policy enforcement, Token Ring protocol support, and metadata extensions for datasource entities. Guardium also supports sharded databases, automatic sensitive data discovery, and provides a Smart Assistant for vulnerability assessments.

## Technical Components and Features

- **AES256-CTS-HMAC-SHA1-96**: Encryption standard supported by Guardium for securing data in transit.
- **Aggregator**: Central appliance consolidating data from multiple Collectors for enterprise-wide reporting.
- **A-TAP**: Kernel-level agent intercepting database calls on the same server as applications.
- **CAS**: Detects and logs schema changes, object modifications, and permission changes.
- **Collector**: Receives and processes activity data from S-TAP agents for analysis and reporting.
- **Data-Masking**: Dynamically masks sensitive data in query results based on policies.
- **FAM**: Monitors access to unstructured data on file servers, NAS devices, and SharePoint.
- **GDPR**: Helps compliance with EU regulations through data discovery, classification, and audit.
- **GIM**: Central tool for remote deployment, configuration, and patching of S-TAP agents.
- **K-TAP**: Captures OS-level database traffic without requiring S-TAP on the database server.
- **Query Analysis**: Inspects queries to identify sensitive data exposure or policy violations.
- **SQL Guard**: Real-time inspection and blocking of SQL statements based on rules.
- **S-GATE**: Enforces security policies by inspecting and possibly blocking or masking queries.
- **S-TAP**: Captures and forwards database traffic to a Guardium Collector.
- **Data Classification**: Identifies sensitive data through policy-based rule sets.
- **Deployment Health**: Dashboard view of the operational status of Guardium components.
- **IAM-Role**: Grants permissions to services or users for automation workflows.
- **GuardAPI**: Command-line tool for managing Guardium appliances programmatically.
- **Secure Protocol**: Enforces encrypted communication between Guardium components.
- **Discovery**: Automated process for finding and classifying new databases.
- **Remediation**: Generates reports and takes corrective actions based on findings.
- **Backup-Validation**: Verifies the integrity and availability of database backups.
- **TLS-Configuration**: Specifies TLS settings for encrypted connections.
- **CM-Role**: Manages and orchestrates security policies across distributed collectors.
- **SAML-SP**: Enables Single Sign-On using Security Assertion Markup Language.
- **TLS-Renegotiation**:

on TAP): IBM Guardium kernel‑level agent that intercepts database calls made by local applications directly on the database server.  
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise‑wide reporting.  
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.  
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S‑TAP agents.  
FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S‑TAP agents across database servers.  
KernelTAP(K‑TAP): Linux kernel module loaded on the database server that intercepts OS‑level database socket traffic for Guardium monitoring.  
S‑GATE(Software GATE): Guardium component that enforces real‑time database access policies and blocks or masks unauthorized queries.  
S‑TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  
SSL(Secure Sockets Layer): Encryption protocol used by Guardium for secure communications between agents, collectors, and aggregators.

## A-TAP
IBM Guardium kernel-level agent intercepting database calls by local applications directly on the database server.

## Aggregator
Guardium appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.

## CAS
Guardium module detecting and recording changes to database schemas, stored procedures, and object configurations.

## Collector
Guardium appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

## FAM
Guardium module monitoring and recording access to unstructured data files on NAS, SharePoint, and similar storage.

## GDPR
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

## GIM
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## K-TAP
Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.

## S-GATE
Guardium component enforcing real-time database access policies and blocking or masking unauthorized queries.

## S-TAP
IBM Guardium software agent capturing and forwarding database traffic to a Guardium Collector.

## AES
Symmetric encryption algorithm supported by Guardium for encrypting data at rest and in transit.

## Amazon RDS
Managed database service; Guardium monitors through external collectors and vulnerability assessments.

## AppUser
Guardium non-administrative user account accessing the UI and running predefined reports.

## Audit Store Appliance
High-performance appliance for large-scale audit data retention and long-term analysis.

## AWS
Cloud platform; Guardium supports monitoring of databases hosted on AWS through various methods.

## BPM
Workflow management category; Guardium integrates with BPM systems to monitor access to sensitive data within workflows.

## Cassandra
NoSQL database; Guardium monitors Cassandra clusters via data collectors or agents.

## CentOS
Linux distribution; Guardium supports deployment of Collectors and STAPs on CentOS servers.

## Certificate
Digital certificate; Guardium supports SSL/TLS encryption and certificate-based authentication.

## Change Management
Process tracking and controlling changes to systems; Guardium Change Audit System automates detection and logging of database schema changes.

## Clang
C/C++ compiler; Guardium supports building and deploying agents on systems using Clang.

## Building Agents from Source
Use Clang on supported platforms to compile Guardium agents.

## Time Zone Settings
Configure the appliance's time zone for accurate audit timestamps.

## Common Software Inventory
Guardium integrates with CSI tools to correlate database instances with security patches.

## cURL
Use cURL in scripts for API interactions and data retrieval.

## Cygwin
Run Guardium agents under Cygwin for Windows compatibility.

## Database Activity Stream (DAS)
Send real-time transaction feeds to Splunk or other SIEM systems.

## DataStax
Monitor DataStax Enterprise database activity with Guardium.

## Dapper
Integrate with Dapper to correlate database activity with application traces.

## Distributed File System (DFS)
Monitor DFS share accesses via the FAM module.

## Docker
Monitor databases in Docker containers with host-based agents.

## Encryption
Supports encryption for logs, backups, and data in transit.

## End-of-Header (EoH)
Mark the end of HTTP headers in policy enforcement rules.

## Extract, Transform, Load (ETL)
Extract, transform, and load data between collectors and aggregators.

## First Failure Data Capture (FFDC)
Automatically collect diagnostic data at failure points.

## File Integrity Monitoring (FIM)
Monitor file changes as part of the FAM feature.

## Garbage Collection
Manage JVM heap usage with GC utilities.

## Google Cloud Engine (GCE)
Monitor databases on GCE with Cloud Data Exchange (CDX).

## Git
Manage Guardium source code and releases with Git.

## Helm
Deploy Guardium services on Kubernetes with Helm charts.

## HMAC
Verify data integrity with HMAC in Guardium.

## HTTP Headers
Inspect and filter HTTP headers in Guardium policies.

## Hypertext Transfer Protocol Secure (HTTPS)
Secure UI, API, and service connections with HTTPS.

## iSCSI Boot Firmware Table (iBFT)
Monitor iSCSI storage access integrated with relevant databases.

## Identity and Access Management (IAM)
Integrate with IAM solutions for user provisioning and access control.

## IBM Cloud
Extend monitoring to databases hosted in IBM Cloud environments.

## Java Virtual Machine (JVM)
Run Guardium agents and utilities in a JVM for cross-platform support.

## Key Stretching
Enhance password security with key stretching techniques.

## Logical Volume Manager (LVM)
Deploy on LVM-configured Linux systems and monitor storage.

## Makefile
Compile agents and tools with directives in a Makefile.

## Manifest
Detail software components included in each release.

## Maven
Build and manage dependencies for Java-based components.

## MongoDB
Monitor MongoDB instances with agents or collectors.

## MySQL
Monitor MySQL through S-TAP and CAS features.

## National Institute of Standards and Technology (NIST)
Align with NIST guidelines for data security and privacy.

## OAuth
Secure API access to Guardium REST interfaces with OAuth.

## Oracle Database
Comprehensively support Oracle monitoring, including CAS, S-TAP, and real-time policy enforcement.

## Privacy-Enhanced Mail (PEM)
Support PEM format for SSL/TLS certificates.

## PostgreSQL
Provide monitoring capabilities for PostgreSQL.

## Privileged Account
Track activities and enforce Just-In-Time access for privileged accounts.

## Python
Write CLI and automation scripts in Python for easy deployment and management.

## Query Language
Inspect and block malicious SQL queries with SQL Guard.

## Relational Database Service (RDS)
Support various managed database services across cloud providers.

## Reporting Engine
Generate, schedule, and distribute customizable reports from Guardium data.

## Red Hat Enterprise Linux (RHEL)
Support deployment and monitoring on RHEL systems.

## Overview
- **Linux**: Enterprise-grade Linux distributions such as RHEL, SUSE, and SELinux are supported by Guardium for deploying collectors and S-TAP agents.
- **Security Protocols**: RSA, SHA, TLS, and WebSphere integration provide secure authentication, data integrity, and encrypted communication.
- **Package Management**: RPM is used for software installation and updates on compatible Linux distributions.

## Components
- **A-TAP**: Kernel-level agent that intercepts database calls made by local applications directly on the database server.
- **Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.
- **CAS**: Detects and records changes to database schemas, stored procedures, and object configurations.
- **Collector**: Receives, processes, and stores database activity data forwarded by S-TAP agents.
- **FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
- **GDPR**: Supports compliance with the General Data Protection Regulation through data discovery, masking, and audit trails.
- **GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
- **K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for monitoring.
- **S-GATE**: Enforces real-time database access policies and blocks or masks unauthorized queries.
- **S-TAP**: Software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## IBM Guardium Key Components

### Key Components
- **A-TAP**: Kernel-level agent intercepting local application calls.
- **Aggregator**: Centralizes data from multiple Collectors.
- **Collector**: Receives and stores database activity data.
- **CAS**: Detects changes to database schemas and objects.
- **FAM**: Monitors access to unstructured data files.
- **GIM**: Manages S-TAP deployment and upgrades.
- **K-TAP**: Linux kernel module for OS-level traffic interception.

### Security and Compliance
- **GDPR**: Supports EU data protection regulations.
- **PURVIEW**: Audits privileged user activity.
- **VAULT**: Manages secrets for database access.

### Real-Time Policy Enforcement
- **S-GATE**: Enforces real-time database access policies.
- **S-TAP**: Captures and forwards database traffic.

### Distributed Management
- **VALVE**: Integrates with external secret management.
- **vSAN**: Supports storage layer activity monitoring.
- **vSMP**: Links snapshot actions to data access audits.

## Guardium Components

**A-TAP**: Kernel-level agent that intercepts database calls by local applications on the database server.

**Aggregator**: Appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

**CAS**: Module that detects and records changes to database schemas, stored procedures, and object configurations.

**Collector**: Appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

**FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

**GDPR**: Regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

**GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

**K-TAP**: Kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

**S-GATE**: Component that enforces real-time database access policies and blocks or masks unauthorized queries.

**S-TAP**: Software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Configurable Units

### Components in Helm Chart
Configurable units within the Guardium Deployment Pack (GDP) Helm chart map to Kubernetes deployments or services.

## Concepts

### Context
Environment context used by `kubectl` to interact with a specific Kubernetes cluster, configuration, or namespace.

### Tag
Version identifier attached to a container image, specifying the exact build or release of Guardium components.

## Features

### A-TAP
Kernel-level agent that intercepts database calls made by local applications on the database server.

### Aggregator
Appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

### CAS
Module that detects and records changes to database schemas, stored procedures, and object configurations.

### Centralized Monitoring
Feature for tracking CPU utilization across Guardium-guarded databases.

### Data Ingestion Flow
Process defining how data moves from sources to Guardium collectors and analyzers.

### Data Lake Storage
Large-scale repository used to aggregate and retain security logs and analytics data.

### Decision-Making Logic
Internal logic used by Guardium to analyze patterns and generate alerts for potential security incidents.

### Discovery
Process of identifying databases, applications, and data sources within the environment.

### Entitlement
Licensing mechanism governing access to specific Guardium features.

### Encryption
Protocol ensuring secure transmission of data between HAProxy and Neo4j.

### File Access Audit
API to programmatically retrieve file access audit logs.

### GDPR
EU regulation supported by Guardium for personal data protection through discovery, masking, and audit trails.

### General Data Protection Regulation
Compliance framework supported by Guardium features.

### Grouping
Feature that categorizes sensitive data assets for unified policy management.

### Installer
Tool for deployGuardium appliances and agents.

### Json Web Token
Token format used for authentication and authorization exchanges.

### K-TAP
Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.

### License Key
Identifier issued by IBM to activate Guardium capabilities.

### Limited Free Installation
Option for deploying a minimal Guardium environment at no cost.

### Masking
Technique to obfuscate sensitive information in logs or exported datasets.

### Neo4j
Graph database integrated with Guardium for storing complex relationships and audit data.

### NodePort
Service type exposing a Guardium component on a static port on each cluster node.

## Guardium Keyword Glossary

**ACTIVITY_STREAM(Entity)**: Stream captures real-time database activity for monitoring and analysis.

**AUDIT_PROCESS_WORKFLOW(Workflow)**: Defines sequence of steps for handling audit data, including initiation, execution, and reporting.

**BASE_CIF_WORKFLOW(Workflow)**: Core workflow manages collection, inspection, and forwarding of database activity data.

**BUILD(Ex(S)CIF(Examined, Extracted, Collected, Inspected, Forwarded))**: Transforms raw activity records into actionable intelligence.

**CIF_OUTPUT_WORKFLOW(Workflow)**: Formats and delivers collected data to external systems for analysis or reporting.

**CLIENT_AUTH_PROTOS(Protocols)**: Protocols like TLS/SSL secure client connections to database servers, ensuring encrypted communications.

**DATA_STEWARD(Steward)**: Oversees data integrity, quality, and compliance within an organization.

**DATABASE_ACTIVITY_INSPECTION(Inspection)**: Examines database transactions to detect anomalies, enforce policies, and ensure compliance.

**DATABASE_USER_STRUCTURE(Structure)**: Hierarchical arrangement of database users, roles, and privileges to control access and maintain security.

**DATA_AGGREGATION_WITH_KAFKA(Technology)**: Uses Apache Kafka to collect, aggregate, and process large volumes of database activity data efficiently.

**FAM_COMPONENT(Component)**: Focuses on monitoring and reporting file access activities on network storage devices.

**FILEIZR(Feature)**: Enables comprehensive analysis of file access patterns and anomalies across the enterprise.

**GLOBAL_TAINT_RULES(Rules)**: Predefined or custom rules universally applied to detect and prevent unauthorized data access or leakage.

**HOST_AGGREGATOR_IMPLEMENTATION(Implementation)**: Centralizes data collection from multiple hosts for comprehensive monitoring.

**INGRESS_ANNOTATIONS(Annotations)**: Metadata applied to data entering the system for categorization, prioritization, or security checks.

**KAFKA_CONFIG_PARAMETER(Parameter)**: Configuration setting within Apache Kafka that dictates operational behavior such as replication, partitioning, or security.

**KAFKA_MESSAGE_BROKER(Message Broker)**: Facilitates asynchronous transfer of data between producers and consumers securely and reliably.

**LINUX_SNIFFER(Log Capture)**: Captures and analyzes network traffic on Linux systems, aiding in monitoring database communications.

**DENY_S-TAP(Disable)**: Disables the S-TAP agent, stopping the collection of database activity data for troubleshooting or maintenance.

**FAM_CONTROLLER_PREDEFINED(Predefined)**: Control mechanisms within the File Activity Monitoring module that dictate actions based on predefined threat detection rules.

**FAM_SUPPORT_STATE(Support)**: Current operational status of File Activity Monitoring, indicating if it is fully supported, deprecated, or in development.

**FLEXIBLE_TOLERANCE_PARAMETER(Parameter)**: Adjustable threshold for tolerating minor deviations in database activity patterns without triggering alerts.

**GCF_RETRIEVAL_DATA(Retrieval)**: Process and parameters used to fetch data from Guardium's Central Management database for reporting or auditing.

**GSTP_SPECIFIC_CONFIGURATIONS(Configurations)**: Tailors data processing in Guardium's Stream Processor Technology to specific needs.

**I_TAP_IMPLEMENTATION(Implementation)**: Deploys and configures the Infrastructure Tap for capturing non-database network traffic, enhancing Guardium's monitoring capabilities.

**IP_PROTOCOL_VERSION(Protocol)**: Supports and optimizes network communications requiring IPv4 or IPv6.

**IS_INIT(Initial)**: Flag indicating the initial state of a process or system.

## CAS Build Items

**CAS.B.build_item_env_variable(String, String):** Defines an environment variable for CAS templates, specifying `name` and default `value`.  
**CAS.B.build_item_file(String):** Specifies a required file path parameter in CAS templates.  
**CAS.B.build_item_file_pattern(String):** Defines a file pattern to monitor in CAS.  
**CAS.B.build_item_os_script(String):** Establishes an executable OS script for CAS monitoring.  
**CAS.B.build_item_regkey(String, String):** Sets a Windows registry key with `path` and default `value`.

## GuardAPI Utilities

**GuardAPI.B.build_grdapi_criteria_item(String, String):** Creates a query criteria item with `name` and `value`.  
**GuardAPI.B.is_cmd_empty(String):** Checks if a command string is empty or null.  
**GuardAPI.B.new_boolean(String, String):** Constructs a Boolean parameter with `name` and `value`.  
**GuardAPI.B.new_cmd_obj(String):** Initializes a new GuardAPI command.  
**GuardAPI.B.new_cmd_opt_obj(String, String, String):** Generates a command option with `name`, `type`, and `value`.  
**GuardAPI.B.new_custom_param_obj(String, String):** Creates a custom parameter with `name` and `datatype`.  
**GuardAPI.B.new_gs_string(String, String):** Constructs a string parameter with `name` and `value`.  
**GuardAPI.B.new_numeric_param_obj(String, String):** Forms a numeric parameter with `name` and `value`.  
**GuardAPI.B.new_string_log_param_obj(String, String):** Creates a log string parameter with `name` and `value`.

**Guardium Keyword Glossary**

**A**
- **A-TAP**: Kernel‑level agent that intercepts database calls made by local applications directly on the server.  

**C**
- **CAS**: Module that detects and records changes to schemas, stored procedures, and object configurations.  
- **Collector**: Appliance that receives, processes, and stores activity data forwarded by S‑TAPs.  

**D**
- **Data Discovery**: Service that scans storage for structured and unstructured data assets needing compliance controls.  

**E**
- **Event Alert**: Real‑time notification generated when a rule's condition is satisfied.  

**F**
- **FAM**: Module that monitors and records access to unstructured files on NAS, SharePoint, etc.  

**G**
- **GIM**: Centralized tool for remotely deploying, upgrading, and managing S‑TAP agents.  
- **GDPR**: EU regulation for personal‑data protection; Guardium supports compliance through discovery, masking, and audit trails.  

**I**
- **Analyst**: Role that performs investigative tasks using search, drill‑down, and reporting features.  
- **Analyzer**: Component that evaluates real‑time rule actions and generates response logs.  

**M**
- **Custom Alerts**: Configurable alarms triggered by specific rule matches, anomalous patterns, or threshold breaches.  

**R**
- **Rule Builder (ACL)**: Guardium rule element that grants or restricts privileges for users or groups.  

**S**
- **S‑TAP**: Software agent installed on database servers that captures and forwards traffic to a Collector.

```markdown
### Guardium Overview
Guardium consolidates database, file, and cloud activity monitoring into a unified security platform.

### Core Components
- **Collector Cluster**: Appliances that share workload and ensure high availability.
- **Enterprise License**: Enables multi‑domain, multi‑tenant, and advanced compliance features.
- **GUI Dashboard**: Web interface for interactive analysis of alerts, reports, and data discovery.
- **User Portal**: Self‑service portal for viewing alerts, generating reports, and submitting tickets.
- **Host‑Based Scanner**: On‑demand scan of file shares and databases for sensitive data.
- **HRU**: Composite rule with nested conditions and multi‑level responses.
- **JDBC Proxy**: Captures and forwards JDBC traffic without client‑side S‑TAP.
- **Kernel Mode S‑TAP**: Kernel‑level agent with minimal performance impact.
- **LST**: Records complete database sessions, queries, parameters, and responses.
- **Masking Policy**: Defines which columns are redacted/anonymized per user group.
- **Native Auditing Connector**: Ingests platform‑specific audit logs for centralized analysis.
- **Network‑Level TAP**: Hardware device mirroring traffic into Guardium.
- **OPE**: Oracle PL/SQL parser for detailed session reconstruction.
- **PCI‑DSS**: Supports compliance with payment‑card security standards.
- **Policy Builder**: Wizard for defining rules, actions, and escalation workflows.
- **Policy Exception**: Documented intentional bypass of a rule match.
- **Policy Framework**: Architecture of Policies, Rule Groups, Actions, and Response Plans.
- **Policy Violation**: Breach of a defined rule, triggering alerts or actions.
- **Predefined Policy**: Out‑of‑the‑box policies covering common compliance/security use cases.
- **Record‑Level Masking**: Row‑wise masking based on privileges and sensitivity.
- **Replay Engine**: Reproduces captured sessions for forensic investigation.
- **Resident Rule Set**: Rules loaded in memory for rapid real‑time decisions.
- **Resource Guard**: Limits per‑user/application CPU and I/O consumption.
- **Response Action**: Automatic/ manual response (block, rewrite, alert) to rule matches.
- **Response Plan**: Sequenced set of actions linked to a policy rule.
- **Rule Builder**: Defines rule criteria and links to actions.
- **Rule Violation**: Log of a rule condition being met.
- **S‑TAP Group**: Logical set of S‑TAP agents for uniform deployment/ configuration.
- **SSL**: Guardium can decrypt SSL traffic for inspection while preserving security.
- **Self‑Service Reporting**: Portal for running predefined reports without admin rights.
- **Sensitive Data Scanning**: Fingerprints storage for credit cards, PII, PHI, etc.
- **Sensitivity Score**: ML‑derived risk metric for transactions.
- **Session Guard**: Controls/alters sessions based on user, IP, or connection attributes.
- **Session Hijacking Detection**: Identifies abnormal session reuse or takeover attempts.
- **Session Trace**: Detailed session log from S‑TAP or Kernel‑Level TAP.
- **Shared Secret**: Cryptographic key for Guardium agent‑collector communications.
- **Signature Database**: Known attack patterns, SQL injection signatures, etc.
- **Single Sign‑On**: Enterprise credentials for Guardium GUI access.
- **SQL Rewriting**: On‑the‑fly query modification to enforce policies.
- **Standard Compliance Report**: Pre‑built reports for PCI‑DSS, HIPAA, etc.
- **Structured Data**: Relational or organized formats for automated controls.
- **System Auditing**: Captures OS‑level events alongside database activity.
- **TAP**: Generic term for Guardium agents (S‑TAP, K‑TAP, A‑TAP) capturing activity.
- **Threat Feed**: External threat indicators ingested for enrichment.
- **Threat Intelligence**: Service correlating internal activity with external threats.
- **Time‑Based Policy**: Rules dependent on calendar dates or maintenance windows.
- **Transaction Profiling**: Baseline behavior models for users, apps, or roles.
- **Trust Zone**: Logical separation of trusted/untrusted network segments.
- **Two‑Factor Authentication**: Enforced additional login step for privileged users.
- **User Activity Dashboard**: Real‑time view of high‑risk user actions and access trends.
```

**Installation Manager):** Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  

**K-TAP(Kernel TAP):** Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.  

**NAC(Network Access Control):** Mechanism that Guardium uses to manage and enforce network access policies for databases.  

**S-GATE(Software Gate):** Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  

**S-TAP(Software TAP):** IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  

**UNIX(Unix Mode):** Guardium operating mode optimized for Unix-based database servers.

## IBM Guardium Core Components
- **S-TAP (Software TAP)** captures and forwards database traffic from servers to a Collector.
- **K-TAP (Kernel TAP)** intercepts OS-level socket traffic for Linux database servers.
- **S-GATE (Software Gate)** enforces real-time access policies, blocking or masking unauthorized queries.
- **A-TAP (Application TAP)** intercepts database calls made by local applications on the server. 
- **GIM (Guardium Installation Manager)** remotely deploys, upgrades, and manages S-TAP agents.

## Data Collection and Storage
- **Collector** receives, processes, and stores activity data from S-TAP agents.
- **Aggregator** consolidates data from multiple Collectors for enterprise-wide reporting.
- **Archiver** (implied by context) manages long-term storage of collected data.

## Data Protection and Monitoring
- **FAM (File Activity Monitoring)** monitors access to unstructured files on NAS and SharePoint.
- **CAS (Change Audit System)** detects schema changes to databases.
- **Encryption** transforms data to protect confidentiality.
- **Kerberos** provides network authentication using tickets.

## User Management and Policy
- **roleManagement** creates and manages database access roles and privileges.
- **policy** defines rules for access control and compliance enforcement.
- **user** represents individuals or services with access permissions.
- **role** groups privileges to simplify management.
- **policy** governs allowed and prohibited actions.

## Data Discovery and Protection
- **GDPR** compliance through data discovery, masking, and audit trails.
- **classification** identifies sensitive data types like credit card numbers.
- **sensitive** marks data requiring additional protections.

## Threat Detection and Response
- **anomaly** identifies unusual patterns in database activity.
- **insider** monitors internal user actions for potential threats.
- **threat** encompasses malicious actions targeted at database systems.
- **vulnerability** identifies weaknesses that could be exploited.
- **exception** logs instances where policies are bypassed.

## Reporting and Inspection
- **audit** records activities for compliance verification.
- **report** generates summaries of monitored activities.
- **decision** (possibly **decision log**) documents policy evaluations.
- **privilege** (possibly **privilege check**) verifies access permissions.

## Configuration and Optimization
- **transform** (possibly **data transformation**) modifies data formats during collection.
- **parameter** settings like `rotationFrequency` and `log4j_num_connections`.
- **affinity** (possibly **geographic affinity**) directs data flows for performance or compliance.
- **key** (possibly **encryption key**) secures data transmission.
- **identity** (possibly **user identification**) authenticates users and systems.
- **session** (possibly **session management**) tracks active user connections.

## Integration and Distribution
- **collector** nodes distribute data in a Guardium environment.
- **requester** (possibly **client**) initiates queries or actions against the system.
- **central manager** coordinates activity across multiple Guardium instances.

**Keyword Glossary (A → Z)**  

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.  
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.  
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.  
FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.  
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  
S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  

Application Data(Application Data): Attributes used to uniquely identify and categorize data in SAP and Siebel reports.  
Audit Process Definition(Audit Process Definition): Structured approach involving description, initial task setting, and selection of allowed statuses.  
CPU Utilization(CPU Utilization): Metrics or summary features indicating the percentage of processor capacity used.  
Distributed Report(Distributed Report): Reporting type with Scheduled mode that periodically runs, compiles data, and forwards it centrally.  
Guardium Installation Manager(GIM): Centralized utility facilitating remote deployment, upgrades, and management of S-TAP agents.  
KILL Commands Execution Audit(KILL Commands Execution Audit): Specialized reporting on SQL Verb activity for termination commands.  
Oracle Application Data(Oracle Application Data): Specific attributes for Oracle applications, ensuring precise data tracking.  
Report Aggregation(Segment Aggregation): Function handling data aggregation across varied time zones.  
Report Drill-Down(C Report Drill-Down): Capability to access detailed underlying data from a broader printable report.

## Audit Logging Options
Specifies logging configurations to record database activity and security events.

## Optional Ingress Parameters
Define parameters to control traffic routing, TLS termination, and request handling for services.

## DB2 Instance Monitoring
Example: `guardctl db_instance db2inst1 deactivate` – manages per-instance monitoring.

## Guardctl Command
`guardctl db_instance db2inst1 deactivate` – deactivates a specific DB2 instance.

## IBM Guardium Components

### Agents
- **A-TAP**: Kernel-level agent intercepting local application database calls on the server.
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic.
- **S-TAP**: Software agent on database servers capturing and forwarding traffic to a Collector.

### Management Tools
- **GIM**: Centralized tool for remote deployment, upgrading, and management of S-TAP agents.
- **GDPR**: Compliance support for EU personal data protection regulation.

### Modules
- **CAS**: Change Audit System detecting schema and configuration changes.
- **FAM**: File Activity Monitoring for unstructured data files on NAS and similar storage.
- **S-GATE**: Real-time policy enforcement, blocking, or masking unauthorized queries.
- **TSA**: Threat Services

### Appliances
- **Aggregator**: Centralizes activity data from multiple Collectors for enterprise reporting.
- **Collector**: Receives, processes, and stores database activity data from S-TAP agents.
- **Data Lake**: Scalable repository for structured and unstructured data analytics.

### Security Features
- **Policy**: Rules and actions governing data access, usage, and compliance.
- **Redaction**: Masking sensitive data in query results to protect privacy.
- **Sensitive Data**: Confidential information requiring protection and controls.

### Monitoring and Risk
- **SMD**: System Monitoring Data from database servers for operational insights.
- **Security Score**: Composite metric evaluating overall database security posture.

### Miscellaneous
- **Team**: Group of Guardium users with shared responsibilities and permissions.
- **User Roles**: Defined permissions and capabilities assigned to users.
- **Threat Level**: Quantitative assessment of vulnerability impact on system integrity and data confidentiality.
- **version**: Software version of S-TAP installed on the database server.

## ## Glossary

**A-TAP(Application TAP):** IBM Guardium kernel-level agent that intercepts database calls from local applications running on the same database server.

**Aggregator(Guardium Aggregator):** Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

**CAS(Change Audit System):** Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

**Collector(Guardium Collector):** Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

**FAM(File Activity Monitoring):** Guardium module that monitors access to unstructured data files on NAS, SharePoint, and similar storage systems.

**GDPR(General Data Protection Regulation):** EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

**GIM(Guardium Installation Manager):** Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

**K-TAP(Kernel TAP):** Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

**S-GATE(Software Gate):** Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

**S-TAP(Software TAP):** IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Activity Monitoring Policy
Defines specific database fields to be monitored in audit trails.

## Define(Entity Scope)
Configures which database entities a monitoring rule applies to.

## Incremental Partitioning View
Organizes database views incrementally for efficient querying and access control.

## Main Entity Selection
Selects the defining entity for a report in the creation workflow.

## NIST Cybersecurity Framework
Guides organizations in managing cybersecurity risks for compliance monitoring.

## Oracle Database Instance Service Name
Unique identifier for an Oracle instance in policy creation and enforcement.

## PCI-SS
Regulates credit card data protection and access recording/compliance.

## Protection Monitor Agent
Deploys on database servers to monitor and safeguard data integrity in real-time.

## Session End Date
Captures termination date of a database session for auditing.

## Session Failure Detect
Detects and logs failed database session attempts for security analysis.

## Source Program
Identifies the application code from which database access requests originate.

## Source Program User
Specifies the end-user interacting with the application for database activities.

## Threat Analytics & Exceptions
Aggregates and analyzes threat data, flagging unusual activities for inspection.

## User NamedTuple Group
Named group of user attributes for quick access and analysis within audit reports.

## App
Business application/workload identified by Guardium for auditing.

## Application TAP
Captures database calls made directly by applications on the same server.

## Authentication
Verifies user identity against Guardium's user repository.

## Auto Close Case
Automatically closes cases with no new violations after a set period.

## Auto Detect Policy
Automatically detects and reports new access patterns.

## Auto Detect Sensors
Configures time frames for query analysis in Guardium's Auto Detect feature.

## Auto Discover
Automatically identifies database instances for monitoring.

## Baseline Comparison Version
Serves as a benchmark for comparing current data access patterns.

## Block Source Interface Client
Configuration option in Guardium that blocks specific client interface sources.

## Adaptive Redaction
Dynamically masks query results based on policy evaluations and user attributes.

## Aggregation
Combines multiple attribute values into a single string for complex query logic.

## AODA
Monitors and records data access specific to application instances.

## Array
Quantifies pending data in analyzer/parsing buffers, indicating processing workload.

## Authentication Scope
Describes databases accessed during a session to refine authentication policies.

## audit_archive_location
Specifies the directory path for storing audit archives.

## Backup Encryption
Protects backup files with encryption to ensure confidentiality.

## Backup Validation
Verifies integrity and completeness of database backups for reliable recovery.

## Bandwidth Utilization
Tracks network bandwidth consumed by Guardium traffic for capacity planning.

## Bomberman Installer
Automates deployment of Guardium software updates and patches.

## Cache Hit Rate
Measures ratio of cache hits to total file accesses to optimize performance.

## CAS Rule
Defines privileged operations monitored for unauthorized changes.

## CAS_Audit_Strat

## **GUARDIUM COMPONENTS**  
### Data Auditing & Schema Changes  
***egy(CAS Audit Strategy)*** – Configures attribute defining detail and frequency for schema change auditing.  
***CAS_Unaudited_Modification*** – Count of schema changes occurring without CAS monitoring, exposing gaps in change control.  

### Security & Authentication  
***Certificate Authority*** – Validates SSL/TLS certificates from database servers, ensuring secure connections.  
***Database Focused Authentication*** – Enables authentication rules specific to individual databases.  
***Discretionary Control*** – Fine‑grained permission management beyond default privileges.  
***Hot Sessions*** – Sessions flagged for immediate attention due to high‑risk activities or policy violations.  

### Monitoring & Policy Management  
***Change Threshold*** – Threshold for detecting significant schema modifications.  
***Coarse Granularity*** – Aggregated visibility useful for high‑level monitoring.  
***Custom Function*** – Extends policy functionality with user‑defined logic.  
***Context*** – Allows global policies applicable across multiple database instances.  
***Defer Collection*** – Records events but defers evaluation to reduce performance impact.  
***Dependency Report*** – Overview of object dependencies within a database environment.  
***Export Tool*** – Securely exports audit logs and data extracts.  
***Granularity*** – Controls level of detail in access logs and reports.  
***Granularity Level*** – Determines how granularly access records are captured.  
***Granularity Setting*** – Affects SQL statement parsing and reporting for compliance/security.  

### Deployment & Management  
***AGGREGATOR*** – Consolidates activity data from multiple Collectors for enterprise‑wide reporting.  
***CLI*** – Configures settings unavailable via GUI.  
***COLLECTOR*** – Receives, processes, and stores activity data forwarded by S‑TAP agents.  
***Connector Shutdown Delay*** – Delays MongoDB agent termination to complete pending operations.  
***GIM*** – Central tool for remote deployment, upgrades, and management of S‑TAP agents.  
***K‑TAP*** – Linux kernel module intercepting OS‑level socket traffic for monitoring.  
***RSA*** – Multi‑factor authentication integrated with Guardium.  
***S‑GATE*** – [Incomplete entry – omitted]  

### Storage & Export  
***Data Storage Directory*** – Directory for storing data files of a particular group.  
***Export Archive Location*** – Path where exported audit data is archived.  
***Export Queue*** – Manages export requests across aggregators, ensuring efficient distribution.  

### File & Data Access  
***File Access Frequency*** – Frequency of read operations on monitored files.  
***Fingerprint*** – Standardized SQL query representation for comparison and anomaly detection.  

### JSON & Analysis  
***JSON Payload XML Attribute*** – Namespace within JSON objects relevant for parsing and analysis.  

### Risk & Risk Management  
***Inherent Risk*** – Risk assessment based on data sensitivity rather than external factors.  

---

## Guardium Components
Guardium uses S-TAP and A-TAP agents to capture database traffic. S-GATE enforces real-time access policies. Aggregator consolidates data from Collectors. CAS monitors schema changes. FAM monitors file access. GIM manages S-TAP agents. GDPR compliance features include discovery, masking, and audit trails.

## Data Types
Analyzer processes collected data. Attributes describe recorded queries. Groups manage users, accounts, objects, and commands.

## Authentication
APIToken authenticates REST API requests. ClientID and ClientSecret implement OAuth authentication for API clients.

## Workflow IDs
B60B025D-EC3E-4D64-8CAE-F765F140D93C: Removable disk logging issue.  
BC38E65F-CF69-46C3-BDCB-51060B4E1A7D: Kerberos configuration using username/password or Keytab.  
D3B6080C-DD1D-421A-BF96-3AC59CBFD1B6: Kerberos configuration using username/password or Keytab.

## 672. Configure Kerberos authentication

Explain how to configure Kerberos authentication by specifying either a username/password or a Keytab file.

## 673. Verify API key

In the Workflow Console, verify the API key, group name, and managed unit before scheduling a task.

## 674. Monitor Universal Connector status

Check the Universal Connector connection status in the Workflow Console. An **Active Status** shows successful traffic capture.

## 675. Traffic balancing across managed units

The system monitors load and traffic conditions to proactively balance traffic across managed units for high availability and performance.

## 680. Guardium Monitoring Agent

A Linux-based service that remotely monitors Guardium appliance health, performance, and security. It collects metrics, logs, and diagnostic data, and can trigger alerts or execute remediation scripts without requiring direct admin access. Installed as a Docker container, it supports secure TLS communication with the Central Manager and integrates with SIEM tools for enhanced security monitoring.

## 681. PIM Integration

Integrates with external Privileged Identity Management (PIM) systems to automatically provision and revoke access control for database users and to correlate privileged user activities with audit trails.

tly on the database server.
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.
FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.
S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Guardium Components
### Aggregator
Consolidates activity data from multiple Collectors for enterprise-wide reporting.

### Collector
Receives, processes, and stores database activity data forwarded by S-TAP agents.

### S-TAP
IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

### ATAP
Kernel-level agent that intercepts database calls made by local applications directly on the database server.

### K-TAP
Linux kernel module that intercepts OS-level database socket traffic for monitoring.

### S-GATE
Enforces real-time database access policies and blocks or masks unauthorized queries.

### FAM
Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

### CAS
Detects and records changes to database schemas, stored procedures, and object configurations.

### GDPR
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

### GIM
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## Guardium Features
### Dashboard
Centralized viewing area displaying real-time and historical data through configurable widgets.

### Custom Dashboard
User-created dashboard combining specific widgets, charts, and widgets tailored to specific monitoring needs.

### Data Collector Service
Collects and forwards database activity data from monitored systems to Guardium Collector units.

### CPU Utilization
Processor usage metric showing the percentage of time the Guardium system's CPU is busy processing data.

### Encryption Policy
Configuration specifying whether data transmitted to Collectors should be encrypted.

### Event-Driven HA Model
High Availability configuration where standby systems are triggered by specific events rather than continuous polling.

## Guardium Administration
### Managed Units
Collectors or Aggregators that report to and are managed by a Central Manager.

### Lockdown
Enforces mandatory access control policies on database connections to prevent unauthorized data access.

### Log Archive
Secure repository where archived logs and reports are stored for audit purposes.

### Inactivity Timeout
Session lifespan parameter specifying how long a user session remains active without activity before termination.

### Network Interface Bonding
Technology used in Guardium setups to combine multiple network interfaces for redundancy and bandwidth aggregation.

### GuardAPI
Command-line utility for interacting with and managing various Guardium functions programmatically.

### Group Definition Manager
Guardium tool for defining and managing user groups, roles, and permissions across the environment.

### Integrated Access Management
Capability to integrate with external IAM systems to centralize access control and management.

## Guardium Overview
- **Multiple Interfaces**: Use multiple network interfaces for increased throughput and redundancy in Guardium deployments.
- **Policy Violation Detection**: Alert generated when database activity matches predefined compliance or security rules.
- **Quarantine Security Action**: Restricts access for suspicious users or sessions to prevent data exfiltration.
- **Real-Time Alerts**: Immediate notifications upon detection of critical policy violations or security incidents.
- **Risk Indices**: Composite scores aggregating various risk factors to provide a holistic view of database security posture.
- **Secure Gateway**: Encrypted tunnel between Guardium clients and Collectors/Aggregators to protect data in transit.
- **Self-Monitoring**: Internal functionality monitoring the health and performance of Guardium components and alerting administrators of issues.

## Guardium Components and Features
- **Scheduling**: Configuration specifying when reports are automatically generated, distributed, or stored.
- **Sensitive Data Discovery**: Automated process identifying, classifying, and tagging sensitive data.
- **Snapshot**: Periodic capture of database activity data used for reporting, compliance, or forensic analysis.
- **Token Protection**: Prevents sensitive data from being copied, printed, or transferred out.
- **Transaction Monitoring**: Analyzes and reports on database transactions to detect anomalies or fraudulent activities.
- **Upgrade Path**: Defined sequence of steps for applying software updates to Guardium components.
- **Virtual Appliance**: Deployment option running on virtualized hardware, offering flexibility in resource allocation.
- **Whitelist**: List of permitted IP addresses, user IDs, or database objects with unrestricted access.

## Guardium Deployment and Management
- **A-TAP**: Kernel-level agent intercepting database calls directly from local applications on the database server.
- **Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.
- **CAS**: Detects and records changes to database schemas, stored procedures, and configurations.
- **Collector**: Receives, processes, and stores database activity data forwarded by S-TAP agents.
- **FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
- **Guardium Groups**: Named collections used in policies, reports, and alerts within Guardium.
- **GIM**: Centralized tool for deploying, upgrading, and managing Guardium components.

## Security and Encryption
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.
- **Masking Engine**: Dynamically masks sensitive data in real-time query results to comply with privacy regulations.
- **Non-Relational Data Sources**: Supports monitoring of NoSQL databases, Hadoop, and cloud storage platforms.
- **SSL**: Enforces encrypted data transmission requirements for database connections.
- **TAP**: Generic term for Guardium's data interception technology, including S-TAP, K-TAP, and A-TAP.

## Data Monitoring and Assessment
- **Policy Builder**: GUI component for creating, editing, and managing security policies.
- **S-GATE**: Enforces real-time database access policies and blocks or masks unauthorized queries.
- **Vulnerability Assessment**: Discovers security weaknesses in database configurations and provides remediation recommendations.

## Keyword Glossary

Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.

DN(Distinguished Name): Unique identifier for an entry in an LDAP directory, used in authentication and authorization processes.

ETL(Extract, Transform, Load): Process of collecting data from various sources, transforming it into a structured format, and loading it into a target system, often used in data warehousing.

GUC(Global Unicode Enable): Parameter

## Identity and Access Management
Guardium framework for managing user identities and access rights across database environments.

## K-TAP (Kernel TAP)
Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

## LDAP (Lightweight Directory Access Protocol)
Network protocol for accessing and maintaining distributed directory information services, used by Guardium for user authentication.

## LIF (Certificate Lifespan)
Configuration parameter in Guardium that defines how long a security certificate remains valid before requiring renewal.

## IAM (Identity and Access Management)
Guardium framework for managing user identities and access rights across database environments.

## PAL (Policy Action Log)
Guardium log that records actions taken by security policies, such as blocking or masking queries.

## PG (Primary Group)
Default group assigned to users in LDAP or Active Directory environments, used in Guardium role-based access control.

## RIB (Rules and Information Builder)
Guardium interface for defining and managing data protection policies and alerts.

## LAP (Local Authentication)
Guardium method for verifying user credentials against a local database or file rather than an external directory service.

## NAT (Network Address Translation)
Network technique that maps an IP address space into another, sometimes requiring special handling in Guardium traffic monitoring.

## NGF (Next Generation Firewall)
Advanced firewall that provides application-level inspection and threat protection, often monitored by Guardium for data leakage prevention.

## NS (Network Share)
Location on a network where files can be stored and accessed, monitored by Guardium's File Activity Monitoring.

## OAM (Operations Analytics Module)
Guardium component that provides advanced analytics and reporting on data access patterns and anomalies.

## SFTP (Secure File Transfer Protocol)
Protocol for securely transferring files over a network, monitored by Guardium for data access and transfer policies.

## SLO (Service Level Objectives)
Performance targets for database systems, monitored by Guardium to ensure compliance with operational standards.

## SSO (Single Sign-On)
Authentication process that allows users to access multiple applications with one set of credentials, integrated with Guardium for seamless user access.

## TLD (Top-Level Domain)
Highest level in the domain name hierarchy, sometimes relevant in Guardium's domain-based data classification.

## A-TAP (Application TAP)
IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.

## Aggregator (Guardium Aggregator)
Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

## CAS (Change Audit System)
Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

## Collector (Guardium Collector)
Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

## FAM (File Activity Monitoring)
Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

## GDPR (General Data Protection Regulation)
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

## GIM (Guardium Installation Manager)
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## S-GATE (Software Gate)
Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

## S-TAP (Software TAP)
IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

# Custom Transform Value Matchers

## Built‑in Matcher for Match‑Regex Values

`7842c88b-6691-4e63-b1ec-95d92696e0b7`  
**Categories:** keywords, entities  

This matcher validates **Transform** actions that use a *match‑regex* value. It checks whether the specified regular expression correctly matches the input data according to the documented Guardium regex syntax.

## Built‑in Matcher for Match-With-Or-Ignore Values

`9ff01563-fd6c-4419-b8db-a69de59ee185`  
**Categories:** keywords, entities  

This matcher validates **Transform** actions that use a *match‑with‑or‑ignore* value. It ensures the provided expression adheres to Guardium’s *match‑with‑or‑ignore* rules, confirming that the pattern is constructed correctly and will behave as intended during runtime.

```markdown
## Special handling for TRANSFORM actions

`fe68837a-7ec1-4533-9b7d-bc4bf31ea9fe`
**Knowledge, features, entities**
The Global object in Guardium acts as a central repository for system-wide parameters, enabling interactions like setting specific parameters, listing all available parameters, and iterating over parameter groups to access related details.  

## Special handling for TRANSFORM actions

`49e0c70c-b2a9-4db9-a593-173e6013240b`
**Entities, workflows**
Configure a Guardium Central Manager to oversee Collectors by registering Collectors with certificates and enabling SSH key authentication with required cryptographic strength. Entities involved: Central Manager, Collectors.  

## Special handling for TRANSFORM actions

`1857b25c-39aa-4cc5-b648-78074a612f8f`
**Knowledge, entities**
Guardium inspection engines can be customized using group-based enforcement, where entities such as users and groups are leveraged to tailor security and monitoring protocols according to defined user attributes within the database.  
```



```markdown
## Configure FTP Access via SOCKS5 Proxy

Edit the GUI configuration to add `SOCKS_HOST` and `SOCKS_PORT` parameters to enable FTP access through a SOCKS5 proxy. Add these settings in the SOCKS configuration section of the GUI setup.

## Configure Logging Aggregator with Syslog Receivers

Set up a dedicated logging appliance as a Guardium Aggregator with syslog content receivers. Configure K-TAP to capture log traffic and UDP receivers on port 601 for syslog data.

## Install DB2 FAM Agents

Install DB2 File Activity Monitoring (FAM) agents on AIX and Linux hosts. Use the command `db2fam_user_create` to create the `db2fam` user, ensuring it is non-privileged.
```

### IBM Guardium Components
- **A-TAP**: Kernel-level agent intercepting local application calls directly on the database server.
- **Aggregator**: Appliance consolidating activity data from multiple Collectors for enterprise reporting.
- **CAS**: Module detecting and recording schema, stored procedure, and object configuration changes.
- **Collector**: Appliance receiving, processing, and storing database activity data from S-TAP agents.
- **FAM**: Module monitoring access to unstructured data files on NAS and SharePoint storage.
- **GIM**: Centralized tool for deploying, upgrading, and managing S-TAP agents across database servers.
- **K-TAP**: Kernel module intercepting OS-level socket traffic for database monitoring on Linux.
- **S-GATE**: Component enforcing real-time database access policies, blocking or masking unauthorized queries.
- **S-TAP**: Software agent capturing and forwarding database traffic to a Collector.

### Guardium Configuration Parameters
- **alert_grouping**: Time window in seconds for grouping similar alerts into a single notification.
- **db_connect_string**: Identifier used by Guardium to uniquely communicate with the monitored database instance.
- **install_drive**: Drive letter or mount point where Guardium software components are installed on Windows.
- **java_proxy**: Proxy settings used by Java-based Guardium components for external communications.
- **login_user**: Username and password required for authentication when accessing Guardium interfaces or APIs.
- **primary_collector**: Designated Collector receiving and processing initial data streams from S-TAP agents.
- **report_password**: Password securing scheduled reports in Guardium, ensuring only authorized users can access sensitive data.
- **sensor_datapath**: Directory path where alert and event data files are temporarily stored before processing.
- **short_hostname**: Short form of the system's hostname used by Guardium for simplified identification in reports and logs.
- **ssl_certificate**: Digital certificate enabling secure, encrypted communication for data transmission.
- **target_port**: Network port number on the database server where Guardium's data collection agents listen for incoming traffic.
- **WINSTAP_AUTO_ACTIVATE**: Parameter controlling whether the S-TAP service automatically starts after installation or configuration changes.
- **WINSTAP_CMD_LINE**: Command-line options for the S-TAP service when starting or stopping.
- **WINSTAP_ENABLE_MONITORING**: Flag enabling or disabling the collection of database traffic by the S-TAP agent.
- **WINSTAP_MEM_TIMEOUT**: Timeout value for shared memory connections between the S-TAP and the database.
- **WINSTAP_SETUP_TYPE**: Parameter defining the operational mode of S-TAP (e.g., Monitoring, Blocking, or Both).

### IBM Guardium Architecture Terms
- **AWS Security Token Service (STS)**: IAM service providing temporary, revocable security credentials.
- **Database**: Host requiring IP or hostname and credentials for External S-TAP setup.
- **Guardium**: IBM solution for data activity monitoring, vulnerability assessment, and compliance auditing.
- **GroupID**: Unique identifier assigned to each External S-TAP group for management and reporting.
- **Volume**: Persistent storage for External S-TAP within Kubernetes, supporting data persistence.
- **Directory**: Path on the host for SSL certificates required by External S-TAP for secure connections.
- **Validator**: Component validating the External S-TAP configuration before deployment.
- **Broadcast**: Mode sending incoming database traffic to all configured Collectors.
- **Blocking**: Enforcement mode blocking or masking potentially dangerous SQL commands.
- **Encrypt**: Feature enabling traffic encryption between External S-TAP and Collectors for secure data transmission.
- **TLS**: Protocol used for automatic TLS certificate provisioning in External S-TAP.
- **Authorization**: Control of database access based on user verification within External S-TAP.
- **npm**: Node Package Manager used in installation scripts for External S-TAP on Red Hat OpenShift.
- **MacAddress**: MAC address of the client interface used by External S-TAP for network identification.
- **XWiki**: Platform integration point for Guardium.

### External S-TAP Features
- **Validater**: Validates External S-TAP configuration before deployment.
- **Broadcast**: Sends incoming database traffic to all configured Collectors.
- **Blocking**: Blocks or masks potentially dangerous SQL commands.
- **Encrypt**: Encrypts traffic between External S-TAP and Collectors for secure data transmission.
- **TLS**: Uses TLS for automatic certificate provisioning in External S-TAP.
- **Authorization**: Controls database access based on user verification within External S-TAP.

### Containerization & Storage
- **Docker**: Platform deploying External S-TAP as a Docker container.
- **Volume**: Persistent storage supporting data persistence for External S-TAP in Kubernetes.
- **Directory**: Directory path on the host for SSL certificates required by External S-TAP.

### Miscellaneous
- **Validater**: Component validating External S-TAP configuration before deployment.

## External S-TAP

**Session**: Communication context managed by External S-TAP for query analysis.

**toDB**: Parameter specifying the target database for traffic redirection.

**Table**: Database object type monitored for data access and manipulation.

**Backup**: Mechanism for restoring configuration settings using persistent volumes.

**Single**: Deployment mode where External S-TAP is installed on a single database server.

**Auxiliary**: Secondary components supporting primary functionality.

## A-TAP

**A-TAP**: IBM Guardium kernel-level agent intercepting local database calls.

## Aggregator

**Guardium Aggregator**: Centralizes activity data from multiple Collectors for enterprise-wide reporting.

## CAS

**CAS**: Detects and records changes to database schemas, stored procedures, and configurations.

## Collector

**Collector**: Receives, processes, and stores database activity data from S-TAP agents.

## Encryption

**CommonName**: Attribute in a certificate representing an identity, used during TLS/SSL handshakes.

## Evaluation Modes

**ContinuousThreatEvaluationMode**: Enables real-time monitoring of database activity.

## DB2

**DB2EventStore**: High-performance engine capturing and storing database access events.

## Licensing

**DAMStandardAppendLicense**: Adds functionality to an existing DAM Standard deployment.

**DiskFreeThreshold**: Minimum free disk space before alerts or cleanup actions.

## Event Store

**EventStore**: Central repository aggregating and storing security-relevant events for analysis.

## Data Access Monitoring

**FAM**: Monitors access to unstructured data files on NAS, SharePoint, etc.

## Integration

**Foglight**: Third-party performance monitoring tool integrating with Guardium.

## Secure Communication

**GuardConnect**: Secure protocol used by Guardium appliances for bi-directional data exchange.

## Analytics

**GuardiumInsights**: Cloud-based analytics layer providing dashboards, risk scoring, and compliance management.

## Installation Manager

**GIM**: Tool for deploying, upgrading, and managing S-TAP agents remotely.

## Security Features

**GranularPrivilegeMonitoring**: Captures and reports specific database commands and actions.

**Introspection**: Real-time analysis of application code execution and data transformations.

## Cryptography

**KeySpace**: Range of possible values for encryption keys, determining security strength.

## Licensing

**LicensedFeature**: Functional component enabled through purchase or activation.

**LicenseAgreement**: Legal contract governing Guardium software component usage.

**LicenseKey**: Alphanumeric code unlocking specific Guardium features or capacity tiers.

**LicenseReconciliation**: Process comparing actual system usage against license entitlements.

## Log Management

**LogLimit**: Parameter specifying the maximum number of log entries stored per interval or type.

## Management

**ManagedUnitCount**: Configuration parameter determining the maximum number of monitored servers or instances.

## Data Masking

**Masking**: Technique dynamically hiding sensitive data in query results.

## Memory Management

**MemCacheTop**: Configures the maximum number of parsed SQL statements cached in memory.

## Database Architectures

**MultiInstanceDatabase**: Database system architecture serving multiple schema or tenant boundaries.

## Network Validation

**NetworkValidationCheck**: Pre-deployment verification of network reachability and configuration parameters.

## Authentication

**Passwd**: UNIX/Linux command triggering Guardium's AuthenticationChanges protocol for recording and analysis.

## Policy Management

**PolicyEngine**: Rule-based component evaluating incoming traffic against defined policies.

**ProtocolValidation**: Guardium feature verifying the correctness and compliance of database protocols.

## Guardium Components and Features

**A-TAP (Application TAP)**  
Kernel-level agent intercepting database calls made by local applications directly on the server.

**Aggregator (Guardium Aggregator)**  
Appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

**CAS (Change Audit System)**  
Module detecting and recording changes to database schemas, stored procedures, and object configurations.

**Collector (Guardium Collector)**  
Appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

**FAM (File Activity Monitoring)**  
Module monitoring and recording access to unstructured data files on NAS, SharePoint, etc.

**GDPR (General Data Protection Regulation)**  
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

**GIM (Guardium Installation Manager)**  
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents.

**K-TAP (Kernel TAP)**  
Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.

**RemoteInventory**  
Functionality allowing Guardium to remotely collect configuration data, installed patches, and software versions without installing agents.

**Restore**  
Process of returning Guardium systems to a previous state by re-importing saved configurations, data backups, or archived logs.

**SAM (System Activity Monitor)**  
Measures CPU load and service performance to ensure efficient operations over time.

**SecurityAnalytic**  
Feature providing holistic visibility into security events and anomalies across protected databases and infrastructures through advanced analytics.

**SurroundingQueries**  
Feature in Continuous Threat Evaluation mode capturing a series of SQL statements around a suspected violation for contextual analysis.

**SystemEvents**  
Category within reports capturing non-transactional actions like configuration changes, user login activity, or appliance performance metrics.

**Token**  
Cryptographic value representing user credentials, policy decisions, or request authorization in Guardium's authentication workflows.

## IBM Guardium Terms

CAS(Change Audit System): Detects and records changes to database schemas, stored procedures, and object configurations.  
Collector(Guardium Collector): Receives, processes, and stores database activity data forwarded by S-TAP agents.  
GDPR(General Data Protection Regulation): Supports compliance via discovery, masking, and audit trails.  
GIM(Guardium Installation Manager): Remotely deploys, upgrades, and manages S-TAP agents across servers.  
K-TAP(Kernel TAP): Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.  
S-GATE(Software Gate): Enforces real-time database access policies and blocks or masks unauthorized queries.  
S-TAP(Software TAP): Captures and forwards database traffic to a Guardium Collector.  

## Additional Modules

A-TAP(Application TAP): Kernel-level agent intercepting database calls made by local applications on the database server.  
FAM(File Activity Monitoring): Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
Aggregator(Guardium Aggregator): Consolidates activity data from multiple Collectors for enterprise-wide reporting.  
DataMart(Data Warehouse): Central repository for long-term historical Guardium reporting data used for analysis and compliance audits.  

## Oracle-Specific Terms

AutomaticComplianceEvaluation: Runs predefined compliance tests on a schedule without manual intervention.  
ConnectionQuarantine: Terminates or quarantines suspicious database connections in real time.  
DataLevelEvent: Audit event indicating access to specific data elements based on Data Level Security configurations.  
EventSuppression: Filters out specific events from being recorded or displayed in audit reports.  
GuardiumComplianceSuite: Collection of predefined policies, reports, and assessments for meeting regulatory compliance standards.  
GuardiumEventCollector: Aggregates, processes, and forwards database activity events to the central aggregation layer.  
MergePeriod: Time window over which data from multiple audit sources is combined for reporting.

## Guardium Overview

**AGGREGATOR(Aggregator):** Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

**A-TAP(Application TAP):** Kernel-level agent that intercepts database calls made by local applications directly on the database server.

**CAS(Change Audit System):** Module that detects and records changes to database schemas, stored procedures, and object configurations.

**CLI(Command Line Interface):** Text-based interface for interacting with Guardium features, performing configuration, and executing commands.

**CSTORE(Central Store):** Repository within Guardium where aggregated data, reports, and other collected information are stored for analysis.

**COS(Calculated Outlier Score):** Numeric value representing the likelihood that a user's activity is anomalous, used in Guardium's anomaly detection.

**ENTITIES(Guardium Entities):** Database servers, file systems, and other monitored assets that Guardium tracks for activity and compliance.

**GRID(Guardium Grid):** Distributed architecture in Guardium that allows coordination between multiple appliances for load balancing and failover.

**INVESTIGATE(Investigate):** Feature within Guardium that allows users to examine detailed information about data access events.

**KERNE(Kernel Module):** Low-level software component that provides essential services for the operating system.

**LDAP(Lightweight Directory Access Protocol):** Protocol used by Guardium for external user authentication and authorization.

**MONITORING(Database Monitoring):** Continuous surveillance of database activities by Guardium to detect unusual or suspicious behavior.

**PETRY(Petrify):** Converts data into a read-only format for archival purposes.

**STORE-HUB(Store-Hub):** Centralized storage component in Guardium where data is archived before being processed or sent to an Aggregator.

**SUSPECT_ENTITY(Suspect Entity):** Database objects or users flagged by Guardium for exhibiting unusual or unauthorized activities.

System: The response has been generated and is available.

SYSTEM:GUARDIUM_COMPRESSION

## S-TAP Agents and K-TAP Module

**S-TAP**: IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

**K-TAP**: Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

## Policy Criteria and Wildcards

**LIKE**: Wildcard search operator supported by the STATEMENT criterion in Guardium policies, enabling basic pattern matching in SQL statements.

**WILDCARDS**: Flexible matching characters (e.g., % or *) used in the STATEMENT criterion to broaden search criteria beyond exact match.

## Data and Redaction Mechanisms

**TEXT**: Data type category that includes string, character, and text field types; often a focus for redaction and monitoring in Guardium.

**Regex**: Regular expression pattern matching capability; Guardium supports limited regex patterns for redaction and masking operations.

**TOKEN**: String or numeric value embedded within SQL statements or traffic patterns; used in masking and filtering rules.

**TRANSFORM**: Guardium action type that modifies data in transit, such as redaction, encryption, or masking of sensitive values.

## Guardium Components and Actions

**S-GATE**: Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

**VERDICT_ATTACH**: Guardium S-GATE action that attaches a custom message or payload to policy violations for enhanced logging or alerting.

## Integration and Extensibility

**A-PI (API Gateway)**: IBM Guardium API Gateway enables integration with external applications and services for accessing Guardium functionality programmatically.

**Connector (SMS Connector)**: Guardium component that facilitates communication between the Guardium system and external systems like SMTP servers for alerts.

## Policy and Audit Features

**Alert-Rule (Policy Alert Rule)**: Rule within Guardium that generates alerts when predefined conditions are met during policy enforcement.

**ADR (Custom Audit Data Records)**: User-defined audit records created through Guardium’s custom SQL capabilities to capture database events beyond default monitoring.

**Change-Window (Change Audit Window)**: Time period defined in Guardium CAS for which changes to database objects are audited and reported.

**Certified-Guardium (Certified Guardium Deployment)**: Guardium installation that meets official IBM certification requirements for specific databases or environments.

## Advanced Monitoring and Analytics

**BDA (Big Data Analytics)**: Guardium analysis feature focused on large-scale analytics of security data for identifying trends and anomalies.

**FAM-APP (File Activity Application)**: Specific application or service monitored by Guardium File Activity Monitoring for file access activities.

## Configuration and Management

**Auto-Learn (Automatic Policy Learning)**: Guardium feature that automatically generates baseline policies by analyzing observed database activities.

**Auto-Mask (Automatic Data Masking)**: Guardium capability that dynamically masks sensitive data based on defined policies without manual intervention.

**Export-Profile (Export Configuration Profile)**: Set of parameters and settings in Guardium that can be exported and imported for consistent configuration management.

## Special Modes and Settings

**Helmet-Mode (Guardium Helmet Mode)**: High-security mode that restricts certain functionalities to enhance system protection.

## Guardium Quality Gates

- **Complete Sentences Only**: All descriptions end with full sentences.
- **Clean Titles**: Each heading is a concise noun phrase summarizing its content.
- **Names Are Noun Phrases**: No sentence fragments; each title is a noun phrase.
- **No Duplicates**: No repeated concepts or sections are present.
- **Skip Noise**: Removed artifacts, parameter tables, and placeholders without meaningful content.

## Policy Enforcement

### Operational Mode
Restricts access and enforces strict policy enforcement.

### Multi-Tier Deployment
Architecture with multiple appliance layers for distributed data collection and centralized reporting.

### Intent Rule
Specifies intended behavior or outcome of a policy action, not just criteria.

### Policy Family
Logical grouping of related Guardium policies for easier management.

### Time Window
Time period specified in reports or views to limit displayed data to a specific timeframe.

### Rule Version
Version identifier for a specific iteration of a Guardium policy rule.

## Configuration and Settings

### Import Settings
Function for importing configuration settings from another Guardium appliance or backup.

### Password Reset Token
Temporary token or link for secure password reset.

### Report Parameter
Variable or setting within a report that defines its content, scope, or format.

### Online Keys
Active encryption keys used for real-time data protection and compliance tasks.

### Report View Option
Formats available for viewing reports, such as summary, detailed, or graphical views.

## Monitoring and Alerts

### Notify Mail
Configurable email notification for policy violations or system events.

### Watch Point Definition
Monitored sensitive data element or database object to generate alerts on unauthorized access.

### Notify Mail
Email alerts for policy violations or system events.

### Watch Point
Monitored sensitive data elements or objects to trigger alerts on access.

## Data Protection

### Data Masking
Real-time obfuscation of sensitive data values returned in query results.

### Sensitive Data Classification
Module for automatically identifying and classifying sensitive data in monitored environments.

### SDC Rule
Rule to identify, classify, and report sensitive data.

### SDD Database
Database storing detected sensitive data entries for the Sensitive Data Discovery feature.

## Auditing and Analysis

### Change Audit System
Monitors and records changes to database objects, privileges, and schema definitions.

### Transaction Log Parsing
Parses and analyzes transaction logs to extract detailed activity information.

### Custom Table
User-defined table storing selected attributes from audited database activity for analysis.

### Sensitive Data Discovery Rule
Rule defining how sensitive data is identified, classified, and reported.

## Integration and Authentication

### LDAP Guardium Directory
Integration with LDAP directories for user authentication and authorization management.

### Operator Console
Central interface for administrators to manage, monitor, and control Guardium activities.

### Token Exposure Trigger
Condition triggering alerts when sensitive tokens or keys are exposed or accessed.

### Sensitive Data Discovery Database
Database utilized for storing and managing detected sensitive data entries.

## Threat Detection

### Malicious Data Leakage
Detects and alerts on potential malicious activities resulting in data leakage or unauthorized exfiltration.

### Aggregator
Centralized appliance collecting and consolidating activity data from multiple collectors for enterprise-wide reporting.

### ARM Daemon
Background process communicating with S-TAP agents to forward captured traffic to the collector.

### Asset Lifecycle Rule
Defines the lifecycle of assets from discovery to retirement, including classification and monitoring stages.

### Prerequisite Validation
Verifies that all necessary conditions are met before executing certain actions or tasks.

### User Monitoring Threshold
Threshold for triggering alerts or actions when the number of active users exceeds a specified limit.

### Sensitive Data Classification
Automatically identifies and classifies sensitive data within the monitored environment.

### Sensitive Data Discovery Database
Database for storing and managing detected sensitive data entries.

### Virtual Database Support
Support for monitoring virtual databases to ensure consistent security and compliance.

### S-TAP Administration Console
Web-based interface for managing and monitoring S-TAP agents across multiple database servers.

### VDB Virtualization
Support for monitoring virtual databases for consistent security and compliance.

### Sensitive Data Discovery Rule
Rule configuration for identifying, classifying, and reporting sensitive data.

### Scheduled Job Engine
Component responsible for scheduling and managing automated tasks like scans and reports.

### Static Encryption Key
Long-term encryption key used for securing data at rest and ensuring consistent decryption.

### Email Notification
Configurable notifications for policy violations or system events.

### Negation Condition
Excludes specified criteria from policy rules, reversing match criteria.

### User Count
Threshold setting for triggering alerts when active user numbers exceed a limit.

### Risk Assessment Profile
Aggregates and quantifies risks associated with data assets based on compliance and security criteria.

### Metadata Enforcement Policy
Policy governing access to and usage of metadata associated with monitored databases.

### Sensitive Data Classification
Automatically identifies and classifies sensitive data within monitored environments.

### Prerequisite Check
Verifies necessary conditions before executing specific actions or tasks.

### Time Range
Time period limiting data displayed in reports or views to a specific timeframe.

### User Monitoring Threshold
Triggers alerts when active user numbers exceed specified limits.

### Watch Point Definition
Monitored sensitive data elements or database objects to generate alerts on unauthorized access.

## Guardium Monitoring Components

**A-TAP**: IBM Guardium kernel-level agent intercepting database calls made by local applications directly on the database server.

**Aggregator (Guardium Aggregator)**: Guardium appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.

**CAS (Change Audit System)**: Guardium module detecting and recording changes to database schemas, stored procedures, and object configurations.

**Collector (Guardium Collector)**: Guardium appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

**FAM (File Activity Monitoring)**: Guardium module monitoring access to files on NAS, SharePoint, and similar storage systems.

## Key Guardium Concepts

**GROUP**: Collection of databases, tables, users, and files treated as a single entity for policy assignment, reporting, or auditing.

**HEARTBEAT**: Regular status messages sent by S-TAP agents to the Collector verifying connectivity and operational status.

**INSIDER THREAT**: Malicious or careless internal user actions tracked by Guardium compromising data integrity or security.

**KERBEROS**: Authentication protocol supported by Guardium for secure authentication to monitored database servers.

**OBJECT**: Database schema element (e.g., table, view, index) monitored by Guardium for access and changes.

**PARAMETER**: Configuration setting for S-TAP, Collector, or policy defining behavior (e.g., ignored users, key types).

**PATCH**: Software update for Guardium components fixing bugs, improving performance, or adding features.

**QUIESCE**: Temporarily disabling database activity during maintenance or backup without shutting down the database, supported by Guardium policies.

**REPLAY**: Guardium feature enabling playback of captured session activity for forensic analysis and troubleshooting.

**RETENTION**: Policy defining how long audit data is stored on the Collector before archiving or deletion.

**ROLE**: Job function mapping to specific Guardium policies and access levels for users.

**RULE**: Logic statement defining conditions for Guardium to trigger alerts, masking, or policy enforcement actions.

**S-GATE (Software Gate)**: Policy enforcement point within Guardium blocking or masking queries violating defined rules.

**S-TAP (Software TAP)**: Guardium software agent on database servers capturing and forwarding auditable database traffic to the Collector.

**STAP (Has or is Part Of)**: Relationship between an S-TAP agent and the monitored database server.

**TAP**: General term for the data stream (from S-TAP or K-TAP) collected by Guardium for monitoring.

**TRANSFORM**: Policy action modifying query results before returning them to the user based on transformation rules.

**USER**: Database account whose activities Guardium monitors and controls according to defined policies.

**VULNERABILITY ASSESSMENT**: Automated test evaluating database security posture against best practices and detecting misconfigurations.

**WINDOW**: Time frame in a Guardium policy restricting when certain rules or collections are active.

## IBM Guardium Core Components
**S-TAP**: Captures and forwards database traffic from database servers to a Guardium Collector.  
**K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for Guardium monitoring.  
**A-TAP**: Kernel-level agent intercepting database calls by local applications directly on the database server.

## Data Processing and Storage
**Collector**: Receives, processes, and stores database activity data forwarded by S-TAP agents.  
**Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.  
**UniversalConnector**: Integrates parsers to audit various data source logs and formats without vendor lock-in.

## Policy Enforcement and Auditing
**S-GATE**: Enforces real-time database access policies, blocking or masking unauthorized queries.  
**CAS**: Detects and records changes to database schemas, stored procedures, and object configurations.  
**FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

## Compliance and Security
**GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
**SSL/TLS**: Secures network communications between Guardium components by managing sessions and encrypting payloads.  
**Cipher Suite**: Collection of cryptographic algorithms and protocols used to establish secure communications.

## Deployment and Management
**GIM**: Remotely deploys, upgrades, and manages S-TAP agents across database servers.  
**Export Option**: Saves Guardium objects like policies or logs to external formats for archival or analysis.  
**Patch Installation**: Updates Guardium nodes to introduce new features or fix existing issues.

## Monitoring and Performance
**AIO**: Advanced data processing appliance role for patch installation, query execution, or analytics workloads.  
**Buffer**: Memory allocation allocated for data streams within sniffer monitoring processes.  
**RawUser**: CPU time spent by user processes excluding system and idle times.

## Data Analysis and Reporting
**Attribute**: Specific data element within a database exception view, such as FullSQL or GlobalID, used for detailed analysis.  
**Alias Column**: Target column name used in exported query results to provide readable or transformed column identifiers.  
**Value Column**: Primary data column selected for display or export in reports or analyses.  
**GlobalID**: Unique identifier capturing session or transaction details within exception views for traceability.

## IBM Guardium Components and Capabilities

**A-TAP**: Kernel-level agent that intercepts local application calls on the database server.

**Aggregator**: Guardium appliance that consolidates data from multiple Collectors for enterprise reporting.

**Audited Session**: Captures complete SQL activity, including data read, modified, or deleted, for compliance auditing.

**Backup**: Archiving of configuration and audit data for disaster recovery and long-term retention.

**CAS**: Detects and records changes to database schemas, stored procedures, and configurations.

**Collector**: Receives, processes, and stores database activity forwarded by S-TAP agents.

**Compliance Reports**: Prebuilt templates aligned with standards like PCI-DSS, HIPAA, and GDPR.

**Data Flow Diagram**: Visual representation of traffic interception points from network to Collector.

**Discovery**: Automated identification of databases, platforms, and sensitive data elements.

**eBGP**: External Border Gateway Protocol for routing updates between autonomous systems.

**FAM**: Monitors and records file access on NAS, SharePoint, and similar storage systems.

**Gateway**: Front-end appliance that distributes traffic to Collectors and provides real-time policy enforcement.

**GAM**: Provides granular visibility into sessions, transactions, and query details.

**GIM**: Central tool for remotely deploying, upgrading, and managing S-TAP agents.

**HIPAA**: U.S. health data privacy law supported by Guardium through discovery and monitoring.

**K-TAP**: Kernel module on Linux servers intercepting OS-level database socket traffic.

**LDAP**: Protocol used for user authentication and integration with directory services.

**MTU**: Network packet size affecting S-TAP parameter configurations for performance.

**MQTT**: Lightweight messaging protocol supported for data transmission in constrained environments.

**NIST**: Federal standards body whose guidelines Guardium assists in meeting.

**OSI Model**: Seven-layer framework illustrating data flow in context of S-TAP interception.

**PCI-DSS**: Payment industry standard supported by Guardium for credit card transaction security.

**RESTful API**: HTTP-based interface for programmatic management and data retrieval.

**SCAP**: Automated framework for vulnerability scanning and compliance assessment.

**SHA-256**: Cryptographic hash function supported for secure data storage and transmission.

**SOAP API**: Legacy protocol for web service interactions with Guardium.

**TLS 1.3**: Secure communication protocol supported for encrypted data transmission.

**UFW**: Linux firewall whose configuration may require S-TAP parameter adjustments.

**VLAN**: Network segmentation impacting S-TAP network interface settings.

**WSL**: Linux compatibility layer on Windows affecting S-TAP installation paths and configurations.



Log Data: Recorded activity data analyzed by Guardium for security assessments and compliance evidence.

Mainframe System: High-capacity computing environment audited by Guardium for critical data security.

Detect Malware: Software identified and flagged by Guardium as potential threat to data resources.

Custom Guide: User-authored documentation supplementing official Guardium manuals for organization-specific procedures.

Masking Rule: Data protection method applied by Guardium to conceal sensitive information in outputs.

Maximo Asset Management: Enterprise asset management system monitored by Guardium for user activities.

Guardium Metrics: Quantitative performance indicators tracked by Guardium for system health.

MySQL Database: Open-source relational database monitored by Guardium for query analysis and security.

Network Layer: Infrastructure monitored by Guardium to detect unauthorized access or data movement.

Non-compliance: Violation of regulatory or internal standards detected by Guardium during audits.

Offloading: Delegate processing tasks (e.g., data analysis) to external systems from Guardium for efficiency.

Oracle Database: Database system with advanced auditing features closely integrated with Guardium.

Orchestration Tool: Automated coordination of Guardium tasks and workflows for efficiency.

OS Monitoring: System-level scrutiny provided by Guardium's S-TAP components.

Patch: Software update installed and monitored by Guardium to track changes and impact on security posture.

Peer-to-Peer: Decentralized communication monitored by Guardium to ensure policy compliance.

Performance Monitoring: Continuous tracking of Guardium processes to ensure efficient operation.

Privileged Identity Management: System for managing high-level account accesses, audited by Guardium.

Policy Framework: Enforcement rules for data access and user behavior, created and enforced by Guardium.

PostgreSQL Database: Open-source database system audited by Guardium for security and compliance.

Privilege: Authorization levels assigned to users, tracked by Guardium to detect excess permissions.

Provisioning: Automated deployment and configuration of Guardium agents across target systems.

Query: Individual request to a database analyzed by Guardium for patterns indicative of misuse.

RAW Data: Unprocessed data collected by Guardium before parsing and analysis.

Reconciliation Process: Periodic comparison of Guardium audit findings against external sources for accuracy.

Record Storage: Immutable data format in which Guardium stores session and transaction details.

Host Environment: Linux distribution monitored by Guardium for system and application activity.

Relational Database: Structured data storage system audited by Guardium for query and access compliance.

Reversal: Action to undo or rollback a committed transaction, recorded by Guardium for audit trails.

Revocation: Reversal of previously granted permissions or access rights, tracked by Guardium.

Role Definition: Assigned set of permissions within a database monitored by Guardium for access governance.

Rule: Specific check or condition defined within Guardium policies to trigger alerts or actions.

SaaS: Web-based application services audited by Guardium when accessed by enterprise users.

Solaris Auditing Mechanism: Solaris-specific auditing tool whose logs are integrated within Guardium.

Schema Change: Structural alteration to a database monitored by Guardium's Change Audit System.

Script Command: Executable code used for importing or configuring Guardium components.

Secure Access: Encrypted access method monitored by Guardium for secure connections.

Sensor Device: Passive monitoring point in network or system architecture monitored by Guardium.

External S-TAP Group: Collection of External S-TAP instances managed together for centralized administration and monitoring.

External S-TAP: External S-TAP implementation using the Mac operating system to monitor database traffic.

External S-TAP VM: Virtual machine deployment of External S-TAP capturing database activity in virtualized environments.

PostgreSQL truststore: PostgreSQL container environment variable specifying the path to the truststore bundle for Secure Sockets Layer (SSL) connections.

Guardium Collector/Manager: Name assigned to a Guardium Collector or Manager for identification in network configurations and group management.

## Guardium Modules and Features

### Data Protection and Monitoring
- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **Cas**: Detects and records database schema, procedure, and object changes.
- **FAM**: Monitors access to unstructured data files on NAS and SharePoint.

### Compliance and Auditing
- **GDPR**: Supports compliance with EU data protection requirements.
- **SOX**: Assists with Sarbanes-Oxley Act compliance through auditing.
- **Attacks**: Provides forensic analysis for incident response and audits.

### Configuration and Management
- **Archive path**: Directory for storing archived files.
- **Archive template**: Naming scheme for exported data organization.
- **LogEfficiency**: Optimizes log storage by retaining relevant data.

### Communication and Integration
- **RestAPI**: Enables programmatic interaction with Guardium services.
- **GIM**: Manages remote deployment and upgrades of S-TAP agents.

### Platform and Database Support
- **K-TAP**: Intercepts OS-level database traffic on Linux servers.
- **MSSQL**: Module for monitoring Microsoft SQL Server databases.
- **DB2**: Module for monitoring IBM DB2 databases.

## Guardium Terminology

### Core Components
- **S-GATE (Software Gate)**: Enforces real-time database access policies and blocks or masks unauthorized queries.
- **S-TAP (Software TAP)**: IBM Guardium agent installed on database servers to capture and forward traffic to a Collector.
- **IBM Guardium**: Data security platform including CAS, S-TAP, and other modules.
- **GUARDIUM INSIGHTS MODULE**: Analytics tools for risk scoring, anomaly detection, and compliance reporting.

### Monitoring and Agents
- **UNPD (Unified Network Performance Dashboard)**: Real-time performance monitoring for network traffic analysis.
- **A-TAP (Application TAP)**: Kernel-level agent intercepting database calls by local applications.
- **K-TAP (Kernel TAP)**: Linux module intercepting OS-level database traffic for monitoring.
- **CAS (Change Audit System)**: Detects and records changes to database schemas, stored procedures, and configurations.

### Configuration and Management
- **api_target_host (Parameter)**: Specifies target hosts for Guardium REST API execution.
- **group_name (Group)**: Collection of data sources managed as a unit for policies and reporting.
- **auto_classification (Parameter)**: Enables automatic discovery and categorization of sensitive data.
- **FAM_CLASSIFICATION_LANGUAGE (Language)**: Supported languages for file activity monitoring on Linux servers.

### Security and Compliance
- **KERBEROS_AUTHENTICATION (Authentication)**: Network authentication protocol supported by Guardium.
- **GDPR (General Data Protection Regulation)**: EU regulation supported via discovery, masking, and audit trails.
- **LINUX_KERNEL_MODULES (Modules)**: Loadable components extending OS monitoring capabilities.

### Processes and Reports
- **audit_log (Endpoint)**: `/audit_log` REST endpoint for retrieving logged events with filters.
- **audit_log_api (Feature)**: Exposes audit log data as a service for external querying and processing.
- **audit_log_format (Field)**: Configures output format (JSON, XML) of Guardium audit logs.
- **audit_log_schema (Table)**: Relational schema for storing raw audit records in Guardium's repository.

### User and Policy Management
- **Policy Builder (Data Builder)**: Interface for creating, testing, and managing database activity policies.
- **Activity Types (Activity Types)**: Specific actions tracked in Guardium (SELECT, INSERT, UPDATE, DELETE) for monitoring.
- **Classification Engine (Service)**: Analyzes query patterns and data values for classification.
- **Classification Policy (Rule)**: Configurable rules for data masking or additional auditing.

### Integration and Analytics
- **IBM Guardium insights (Service)**: Cloud-based analytics service for advanced threat analysis and compliance.
- **GET (Verb)**: Excluded as too generic, but standard HTTP method for API calls.
- **IBM (Enterprise)**: Placeholder removed as per exclusions, not specific to Guardium.

## Guardium Overview

### Key Concepts
- **Mem Sniffer**: Memory-based packet capture for high-speed logging without disk I/O.
- **Oracle**: Supported for comprehensive activity monitoring and compliance.
- **Mysql Disk Usage**: Storage consumption metrics for MySQL databases.

### Security and Compliance
- **AC (Risk Assessment)**: Identifies, analyzes, and prioritizes risks.
- **HIPAA**: Provides protection for sensitive patient health information.
- **FIPS**: Ensures cryptographic solutions meet federal security requirements.

### Components
- **CMA (Central Management Appliance)**: Central point for data collection, storage, and reporting.
- **SIR (Service Information Request)**: Generates detailed service information reports.
- **EP (Event Processor)**: Ingests, normalizes, and correlates security events.

### Monitoring and Auditing
- **FAM (File Activity Monitoring)**: Monitors access to unstructured data files.
- **DRP (Data Resource Profile)**: Captures comprehensive database metadata.
- **OCR (Object Configuration Inspection)**: Detects unauthorized modifications to configurations.

### Management and Deployment
- **GIM (Centralized Deployment)**: Deploys, upgrades, and manages S-TAP agents.
- **LF (Live Parsing)**: Performs real-time SQL statement analysis.

### Network and Performance
- **Port Type**: Classifies network ports as TCP or UDP.
- **Probe Timestamp**: Date and time of port discovery scan execution.



## Guardium Overview

### Core Components
- **Collector**: Receives, processes, and stores database activity data from S-TAP agents.  
- **Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.  
- **A-TAP**: Kernel-level agent that intercepts local application database calls directly on the server.  
- **FAM**: Monitors access to unstructured data files on NAS, SharePoint, etc.

### Compliance & Security
- **GDPR**: Supports EU data protection via discovery, masking, and audit trails.
- **S-GATE**: Enforces real-time database access policies, blocking or masking unauthorized queries.

### Deployment & Management
- **S-TAP**: Captures and forwards database traffic to a Collector.  
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic.  
- **GIM**: Remotely deploys, upgrades, and manages S-TAP agents across servers.  
- **CAS**: Detects changes to database schemas, stored procedures, and configurations.  

### Data Handling
- **Raw Data**: Unprocessed information collected before analysis or transformation.  
- **Log Analyzer**: Examines log files and activity records for suspicious patterns.

### Access Control & Performance
- **Masking Rule**: Hides sensitive parts of query results.  
- **Notification**: Alerts users about policy violations or anomalies.  
- **Query Optimization**: Improves database query performance collected by Guardium.

### Miscellaneous
- **Managed Unit**: Logically groups appliances for collective management.  
- **Privilege Escalation Detection**: Identifies unauthorized elevated permissions.  
- **Quarantine**: Isolates compromised accounts or systems to prevent damage.  
- **Uninstall S-TAP**: Procedure to safely remove the S-TAP agent from a server.

## IBM Security Guardium Overview
IBM Security Guardium is a data security and compliance solution that protects data, detects anomalies, and enforces policies across the enterprise. It includes various components and modules designed to monitor, audit, and secure database activities.

## Key Components
### Guardium Appliances
- **Guardium Collector**: Receives, processes, and stores database activity data from S-TAP agents.
- **Guardium Appliance**: Dedicated hardware optimized for data security and monitoring tasks.

### Data Collection
- **S-TAP Agents**: Kernel-level agents that intercept database calls made by local applications directly on the database server.
  - **MySQL TAP**: Specialized for MySQL database servers.
  - **MongoDB TAP**: Specialized for MongoDB instances.
- **Auxiliary Agent**: Extends monitoring capabilities for specific database types or platforms.

### Data Management
- **Aggregator (Guardium Aggregator)**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.
- **Audit Archive**: Securely stores historical audit data for long-term retention and compliance audits.
- **External Store**: Configuration for storing audit data in external databases or storage systems.

### Policy and Monitoring
- **Policy Builder**: Creates, manages, and enforces security policies across databases and applications.
- **Query Analysis**: Examines SQL queries to detect anomalies and provide insights for policy tuning.
- **Query Rewriter**: Modifies SQL statements in real-time to enforce security policies.
- **File Activity Monitoring (FAM)**: Monitors and records access to unstructured data files.
- **File Integrity Monitoring (FIM)**: Detects unauthorized changes to critical system files and directories.

### Authentication and Integration
- **Access Key**: Unique alphanumeric code for authenticating access to IBM Security Guardium services and APIs.
- **GuardAPI**: Command-line interface for scripting access to Guardium functions.
- **Kerberos Protocol**: Network authentication protocol used for secure authentication in distributed environments.
- **OAuth (OAuth 2.0)**: Open standard for access delegation, used for token-based authentication in Guardium APIs.

### Compliance and Auditing
- **Compliance Audit**: Formal assessment of adherence to regulatory standards or internal policies using Guardium audit data.
- **Certification Path**: Establishes trust relationships between certificates in Guardium's security infrastructure.

### Advanced Features
- **Prediction Engine**: Analyzes patterns and predicts potential security risks or compliance issues using machine learning.
- **Realtime Log**: Stream of live audit data for immediate analysis and alerting.
- **CAS (Change Audit System)**: Detects and records changes to database schemas, stored procedures, and object configurations.
- **Oracle Proxy**: Monitors Oracle database traffic regardless of the client application used.
- **Cloud Guardium**: Extends data protection services to cloud databases and workloads.
- **CloudIntercept**: Enables real-time monitoring and policy enforcement in cloud environments.
- **Robotic Process Automation (RPA)**: Integrates Guardium with RPA tools to automate data protection tasks.

### Additional Concepts
- **Data Silo**: Isolated data collection not easily accessible or integrated.
- **No Access**: Permission level explicitly denying access to specific features or data.
- **Non-Relational Database**: Database management system not using the traditional relational model.
- **Remote S-TAP**: S-TAP agent deployed on a database server communicating over the network with a Collector.
- **Masking Server**: Applies data masking rules to protect sensitive information during query responses.
- **Log Rotation**: Manages disk space by archiving and deleting old log files.
- **Enterprise License**: Covers use across multiple servers and environments within an organization.

## Deployment Model

**Security Tokens** authenticate and authorize API requests and user sessions in IBM Security Guardium by acting as cryptographic tokens. Guardium uses these tokens to ensure secure communications between components and users.

**S-gate (Software Guard)** enforces security policies at the application level by inspecting and blocking or masking unauthorized database queries. This component prevents unauthorized access and data exposure through direct application layer controls.

**Self-Registering S-TAP** agents automatically register themselves with a Guardium Collector upon installation, simplifying deployment and reducing manual configuration efforts. This capability streamlines the integration of new data sources into the Guardium ecosystem.

**Service-Level Agreement (SLA)** with IBM Security Guardium outlines the expected level of service, including specified uptime percentages, maximum response times for support tickets, and adherence to defined operational standards. These agreements ensure clients receive reliable and timely services.

**Synergy Instance** represents a single instance within the Virtual Data Pipeline (VDP) infrastructure. Multiple Synergy instances collectively provide the scalable and redundant environment necessary for all VDP instances to operate effectively.

**TAP** is an overarching term for data monitoring components in Guardium, encompassing technologies like S-TAP, K-TAP, and other sensor technologies. These components are essential for collecting and analyzing database activity.

**Threat Analytics** leverages behavioral analysis and machine learning to identify and respond to emerging security threats in real-time. Guardium's Threat Analytics capabilities proactively detect anomalies and suspicious activities to prevent potential breaches.

**User Groups** in Guardium are collections of users sharing common roles, permissions, and access privileges. These groups simplify the management of user permissions and streamline policy enforcement across the platform.

**Vulnerability Assessment** is a Guardium feature that scans databases for security weaknesses, identifying potential vulnerabilities and providing actionable recommendations for remediation. This proactive assessment helps maintain the security integrity of guarded databases.

**Webinar** provides an online seminar experience featuring demonstrations, Q&A sessions, and discussions related to Guardium. These webinars educate users on new features, best practices, and advanced functionalities of the Guardium platform.

**XML Schema** defines the structure and data types used in Guardium XML configuration files for policy definitions and system settings. This schema ensures consistency and validity in the XML files used for Guardium configurations, facilitating accurate policy management.

---

## Miscellaneous Entries

**remote_user (Remote User):** An individual or process accessing Guardium from an external network or location. Remote users interact with Guardium functionalities securely through configured authentication and authorization mechanisms.

**restoration (Restoration):** Refers to the process of recovering data from an archived or backup state back to its operational form within Guardium. This process is crucial for data recovery and business continuity planning in Guardium environments.

## Special Handling for TRANSFORM Actions

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents
FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage
GDPR(General Data Protection Regulation): EU regulation mandating protection of personal data; Guardium supports compliance through discovery, masking, and audit trails
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries
S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector

## Entities

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server
Aggregator: Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations
Collector: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents
FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage
GDPR(General Data Protection Regulation): EU regulation that mandates protection of personal data; Guardium supports compliance through discovery, masking, and audit trails
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers
K-TAP: Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries
S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector

categories: entities
The DEPLOY menu allows guardium users to view and manage the inventory of databases and other servers managed by an aggregator or standalone collector.

`1455.unit_utilization`: This value indicates the number of licenses remaining.

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.
CAS(Change Audit System): Guardium module that detec

## Event Log Entry

**Event ID**: Unique string or number identifying the event.

**Alert Conte**

## Alert Type Primary
Field in Guardium configuration for specifying the primary category or type of an alert condition.

## Antivirus
Feature involving scanning or monitoring for malware or virus activity.

## Any
General parameter indicating the rule or filter applies to any value or condition.

## Any-Application
Parameter indicating all applications are included in database traffic analysis.

## Any-IP-or-Hostname
Parameter indicating any IP address or hostname is included in the rule or filter.

## Any-Operation
Parameter indicating monitoring applies to any database operation or action.

## Any-User
Parameter indicating any user is covered by the rule or filter.

## Appliance
Entity containing and running security monitoring services.

## Archer
Term possibly referring to a specific module, integration, or feature.

## AS-Supporting
Credential associated with an authentication process or policy.

## Audit-Data
Data collected and processed by Guardium during auditing operations.

## Auto
Parameter or setting that automatically selects or applies values based on rules.

## Auto-Accept-New-Appliance
Setting that automatically accepts and integrates new Guardium appliances.

## Auto-Accept-New-Client
Configuration option that automatically accepts new client connections without verification.

## Auto-Commit
Configuration flag that automatically commits transactions without manual submission.

## Auto-Discovery-Automatic
Feature set to automatically discover and include new data assets without manual intervention.

## Auto-Discovery-Manual
Feature requiring manual intervention to discover and include new data assets.

## Auto-Discover-Unupported-Applies-To
Configuration indicating unsupported parameters for automatic discovery.

## Auto-Include
Setting for automatically including new assets, users, or clients in monitoring.

## Auto-Include-Application
Configuration specifying automatic inclusion of newly detected applications.

## Auto-Included
Term indicating entities were automatically included in monitoring.

## Auto-Included-Application
Applications that have been automatically included in monitoring.

## Auto-Included-IP-Hostname
Indicates IP addresses or hostnames were automatically included in monitoring.

## Auto-Log-Archive
Feature enabling automatic log archiving based on criteria or schedules.

## Auto-Reassign-To-Collector
Feature automatically reassigning monitoring tasks or data to another collector.

## Auto-Receivers
Parameter defining automatic allocation of tasks or data to receivers.

## Auto-Remove-Included
Setting allowing Guardium to automatically remove previously included assets.

## Auto-Tap-Installed
Status showing the Software TAP agent has been automatically installed.

## Auto-Tap-Not-Installed
Status indicating the Software TAP agent has not been installed.

## Auto-Tap-Planned
Indicates a planned or scheduled installation of the Software TAP agent.

## Automatic
General term indicating actions or settings occur without user intervention.

## Automatic-Full-Backup
Setting to automatically perform complete system backups on a regular schedule.

## Automatic-Inclusion-Criteria
Definitions or parameters triggering automatic inclusion of entities in monitoring.

## Automatic-Reassign-To-Collector
Function automatically reassigning collected data or logs to another collector.

## Automatic-Self-Backup-Frequency
Configuration specifying the frequency of automatic backups of configuration or data.

## Banner
System message or text displayed at login or within the interface.

## Bypass-List
List of rules or entities that are bypassed or excluded from monitoring or enforcement.

## Cassandra
NoSQL database system, potentially a target for data activity monitoring.

## Case-Sensitivity-*
Configuration options determining whether string comparisons are case-sensitive.

## Certificate
Digital document used for securing communications or authentication.

## Child
Indicates a subordinate element in data structures.

## Cipher
Security algorithm used for encryption or decryption in communications.

## Client
End-user software or systems interfacing with Guardium to send or receive data.

## Cognos-Reporting
Integration or reporting features of Guardium with Cognos, an IBM reporting tool.

## Collection-Type-Constants
Constants used to define types of data collections or operations.

## Collector
Appliance that collects data from S-TAP agents or other data sources.

## Collections
Organized sets of data records or activities monitored by Guardium.

## Compute-*
Parameters or settings related to computation processes.

## Config-Data
Configuration data related to system settings or behaviors.

## Config Generation
Process of creating system configurations in Guardium.

## Consolidate
Feature that aggregates data from multiple sources into a unified view.

## Content Identification
Identifying and classifying the data content monitored by Guardium.

## Controllability
Feature related to the control and management capabilities of Guardium.

## Controller
Control mechanisms or entities within Guardium managing operations.

## Controller Connection
Communication link between Guardium components or modules.

## Controller Connection String Name
Name defining a connection string used in controller interactions.

## Cors
Cross-Origin Resource Sharing policies relevant for web interfaces/APIs.

## Deleted
Data or records removed from Guardium's monitoring.

## Deployment
Method or system used to install and configure Guardium components.

## Deployment Granularity
Configuration defining the granularity level in deployment processes.

## Desired Columns
Feature enabling users to specify desired report columns.

---

## A-TAP
Kernel-level agent intercepting database calls directly on the server.

## Alert-Enabled Function
Feature triggering alerts based on predefined conditions.

## API Gateway
Manages and secures API traffic to Guardium services.

## API Token
Temporary token for authenticating API requests.

## Audit Trail
Chronological record of database activity for compliance.

## Backup Manager
Tool for scheduling, executing, and managing Guardium appliance backups.

## Cascading Deletion
Automatically deletes child records when parent is removed.

## Certificate Management
Manages SSL certificates securing communications.

## Change Management
Tracks and verifies changes to database configurations.

## Conditional Masking
Applies data masking based on specified conditions.

## Database Activitystream
Real-time view of database operations for monitoring and analysis.

## Database User
Identity accessing and interacting with a database.

## Data Steward
Ensures data quality, compliance, and governance.

## Datetime
Data type storing date and time for precise logging/reporting.

## Deployment Manager
Utility for managing deployment and configuration of Guardium components.

## Distributed Session Cache
Distributes session data across multiple appliances for scalability.

## Dynamic Data Discovery
Automatically identifies sensitive data across databases.

## Entitlement Review
Assesses and audits user privileges against database resources.

## Export API
Facilitates export of configuration settings and data.

## File Hash
Unique identifier for files monitored under File Activity Monitoring.

## File Masking
Obscures sensitive data within files to protect privacy.

## File Tokenization
Replaces sensitive data with non-sensitive equivalents in files.

## File Type Identification
Categorizes files based on content for targeted monitoring.

## Gim Install
Process of installing the Guardium Installation Manager.

## Gim Server
Facilitates remote software deployment within Guardium.

## Global Masking
Applies uniform data masking rules across all monitored databases.

## High Availability
Ensures continuous operation and data protection through redundancy.

## Identity Propagation
Preserves user identity across multiple services and systems.

## In-Memory Analytics
Allows real-time data analysis without impacting database performance.

## Informed Consent
Ensures transparent and authorized data processing activities.

## Insider Threat
Security risk from individuals misusing data access within an organization.

## Json
Lightweight data interchange format supported for structured data representation.

## Key Rotation
Security practice of periodically updating encryption keys to enhance security.

## Legacy Application
Older software systems requiring specialized monitoring.

## License Key
Unique identifier authorizing the use of Guardium software.

## Guardium Features and Capacities

- **Log Retention**: Defines how long audit logs are stored before archiving or deletion.
- **Mandatory Access Control**: Restricts data access based on predefined security rules.
- **Masking Policy**: Obfuscates sensitive data for unauthorized viewers.
- **Monitoring Influx**: Ingests large volumes of data from various sources for analysis.
- **Network Protocol**: Supports secure communication protocols like SSL/TLS.
- **Non-Relational Data**: Monitors access and security of NoSQL databases.
- **Object Masking**: Selectively masks sensitive database objects.
- **One-Time Password**: Used for multi-factor authentication during login.
- **Open Source Module**: Integrates third-party software to extend functionality.
- **Oracle Kernel**: Deep monitoring of Oracle database activities.
- **Policy Builder**: Tool for creating and managing data access policies.
- **Post-Mortem Analysis**: Reviews security breaches or compliance failures.
- **Privilege Management**: Manages user permissions for least privilege access.
- **Query Optimization**: Suggests performance improvements for database queries.
- **Query Rewrite**: Modifies SQL queries for data protection.
- **Real-Time Alerting**: Generates immediate notifications for critical events.
- **Registry Key**: Manages application parameters via configuration settings.
- **Role-Based Access Control**: Grants access based on user roles and permissions.
- **Root Cause Analysis**: Identifies underlying causes of security incidents.
- **Rule Set**: Collections of rules addressing specific security or compliance needs.
- **SAM**: Manages service identities and access rights.
- **Schema Drift**: Detects and alerts on unauthorized schema changes.
- **Self-Service Portal**: Enables users to manage access requests and view reports.
- **Session Monitoring**: Tracks user sessions and activities.
- **Shell Command**: Executes administrative tasks via command-line.
- **SQL Exception**: Logs errors from SQL query executions.
- **Statistical Anomaly Detection**: Identifies unusual database activity patterns.
- **System Level Permission**: High-level access affecting system configuration and security.
- **Threat Hunting**: Proactively searches for potential security threats.
- **Time Window**: Defines periods for operations like backups or scans.
- **Token-Based Authentication**: Grants access through temporary tokens.
- **Transaction Monitoring**: Monitors database transactions for integrity and compliance.
- **User Entitlement**: Assigns access rights and feature access to users.
- **Vulnerability Assessment**: Scans databases for security weaknesses.

### Application-Level Features

- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **Aggregator**: Consolidates data from multiple Collectors for enterprise reporting.
- **CAS**: Detects and records changes to database schemas and configurations.
- **Collector**: Receives, processes, and stores database activity data.
- **FAM**: Monitors access to unstructured data files on NAS and SharePoint.
- **GDPR**: Supports compliance with EU data protection regulations.
- **GIM**: Deploys and manages S-TAP agents remotely.
- **K-TAP**: Linux module intercepting OS-level database socket traffic.
- **S-GATE**: Enforces real-time database access policies and blocks unauthorized queries.
- **S-TAP**: Captures and forwards database activity to the Collector.

# Guardium Components Overview

## Monitoring and Recovery

- **Automatic Recovery (Monitoring Automatic Recovery):** The process automatically retries failed detections every 20 minutes; if it cannot resolve the issue, it logs a new status for manual intervention.

## Audit and Compliance

- **CAS Template Items (Compliance Audit System Template Items):** Specific audit checks defined within Guardium's Change Audit System, configurable with runtime parameters for detailed reporting.
- **Data Level Security (DLS):** Controls data visibility based on user roles, ensuring users only access authorized data.
- **Role Hierarchy (Role Hierarchy):** A structured framework defining user roles and their data access levels, utilized by DLS to filter audit results.

## Policy Management

- **Policy Builder (Policy Builder):** Tool for creating and managing audit policies, specifying monitored database activities and responses to violations.
- **Report Builder (Report Builder):** Interface for designing custom reports, including template selection, filtering, and output formatting.

## Logging and Reporting

- **Credit:** Entity that records database server login/logout events, including timestamps and user details.
- **Manual Audit (Manual Audit):** Method for verifying entitlement compliance, assessing single activities or aggregating results into reports.
- **Incident Builder (Incident Builder):** Tool for creating incident events from policy violations, detailing the nature and context of the violation.
- **Table Level Auditing (Table Level Auditing):** Guardium capability to audit database activities at the table level, capturing detailed operational data.

## Data Management

- **Data Sets (Data Sets):** Logical collections of monitored database information used for reporting and analysis, containing summarized audit records.
- **Log Errors (Log Errors):** Errors encountered during data processing, stored with details to aid in troubleshooting.
- **Detected Issues (Detected Issues):** Identified audit findings, stored with unique IDs and severity levels for tracking and resolution.

## Database Traffic Management

- **A-TAP (Application TAP):** Kernel-level agent intercepting local application database calls on the server.
- **S-TAP (Software TAP):** Agent installed on servers that captures and forwards database traffic to a Guardium Collector.
- **K-TAP (Kernel TAP):** Linux kernel module intercepting database traffic at the OS level without needing an S-TAP agent.

## Core Guardium Components

A-TAP intercepts local application database calls on the server.<br>
Aggregator consolidates activity data from multiple Collectors.<br>
CAS records changes to schemas, stored procedures, and configurations.<br>
Collector receives and stores activity data forwarded by S-TAP.<br>
S-GATE enforces real-time access policies and blocks unauthorized queries.<br>
S-TAP forwards database traffic from servers to Guardium.<br>

## Related Concepts

FAM monitors access to unstructured files on NAS/SharePoint.<br>
GDPR compliance supported via discovery, masking, audit trails.<br>
GIM centrally deploys, upgrades, and manages S-TAP agents.<br>
K-TAP intercepts OS-level socket traffic on Linux systems.<br>
WINSTAP_CMD_LINE configures S-TAP via command-line parameters.<br>

## Configuration Parameters

DB2_EXIT_DRIVER_INSTALLED controls Db2 exit driver installation.<br>
Port Number sets TCP communication port between S-TAP and Collector.<br>
Redis Database supports key-value storage with A-TAP configuration.<br>
TAP_TYPE identifies the S-TAP agent type (e.g., swin, wtap, ktap).<br>

## Optional Parameters

DB2_SSL_DRIVER_INSTALLED enables SSL between Db2 and S-TAP.<br>
DB2_TAP_INSTALLED automatically enables when installing on existing Db2 servers without other drivers.<br>
User ID identifies user activity for specific modules.<br>
TAP_GUARD_TCP_PORT specifies ports used to connect S-TAP to Guardium systems.<br>

# Guardium Ingress Configuration Parameters

## Annotations to Specify for Ingress

- **SNMPTRAPSERVER2**: IP address of an alternate SNMP trap server for redundancy in Guardium configurations.
- **SHOWCERT**: CLI command used to list the contents of a keystore, with options to filter by subsystem or alias for targeted retrieval.
- **TCPCRYPT**: Feature that encrypts data over TCP connections using certificate-based authentication, enhancing security for data in transit.
- **TCPCRYPTENABLE**: Command to activate TCP-based crypting, which secures data transmission by encrypting it with certificate-based keys.
- **TCPCRYPTKEYSIZE**: Parameter in Guardium that allows users to set the encryption key size for TCP crypting operations, ensuring robust security settings.
- **TCPCRYPTLOCKTIMEOUT**: Parameter defining the timeout duration for cryptographic locks during encryption processes in Guardium.
- **TCPCRYPTMINHASHSZ**: Parameter specifying the minimum hash size permissible for cryptographic operations within Guardium's TCP crypting framework.
- **TCPCRYPTPRIV**: Feature allowing for private encryption settings in TCP communication, enabling enhanced security measures tailored to specific organizational needs.
- **TCPCRYPTSTATUS**: Command or metric used to report the current status of TCP crypting functions, indicating whether encryption is active or inactive.
- **TCPCRYPTVERBATIM**: Mode in Guardium that disables error handling for encrypted data streams, providing raw encryption output for debugging or specialized processing.

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.  
Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
ARCHIVE(ARCHIVE): Process that stores unalterable copies of database transactions for long-term compliance or historical analysis.  
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.  
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.  
DAP(Discovery and Classification): Guardium feature that automatically finds databases, analyzes data sensitivity, and classifies information assets.  
DAT(DAT): Guardium component that continuously watches database traffic for policy violations or anomalous behavior.  
GDM(Guardium Deployment Manager): Central console for provisioning, configuring, and maintaining Guardium appliances and agents across an enterprise.  
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.  
LG-MAS(LG-MAS): The logical name given to a Guardium system where multiple collectors aggregate data for a global view.  
LD_LIBRARY(LD_LIBRARY): Library loaded by applications to enable dynamic data masking of sensitive columns when accessed by non-whitelisted users.  
ORM(object ORM): Software that bridges the gap between object-oriented code and relational databases, often used in TRANSFORM action workflows.  
S-GATE(S-GATE): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  
S-TAP(S-TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  
SAMA(SAMA): Guardium process that examines database objects and SQL code to identify vulnerabilities and policy deviations before execution.  
SMA(SMA): Analysis technique applied to stored procedures and functions to detect security flaws or policy non-compliance.  
TIM(TIM): Metric calculated by Guardium to quantify the trustworthiness of a user or application based on behavior patterns and compliance adherence.

## Guardium Component Overview

**A-TAP** intercepts database calls from local applications on the server kernel level.

**Activity Log** stores captured database and file activity, query text, and error messages for analysis and reporting.

**Aggregator** consolidates activity data from multiple Collectors for enterprise-wide reporting.

**Appliance** is a pre‑configured, hardened hardware and software bundle designed for specific Guardium functions (Collector, Aggregator, etc.).

**Audit Process** automates the execution of a security assessment and generates an audit report.

**CAS** detects and records changes to database schemas, stored procedures, and object configurations.

**Collector** receives, processes, and stores database activity data forwarded by S-TAP agents.

**Data Level Security** enforces row‑level access controls based on user roles and attribute values.

**DPA** evaluates protection controls for structured data sources.

**Export Data Management** moves raw activity data from Collectors to the Aggregator or external systems.

## Guardium Components
- **Aggregator**: Consolidates activity data from multiple Collectors for enterprise‑wide reporting.  
- **Collector**: Receives, processes, and stores database activity data from S‑TAP agents.  
- **K‑TAP**: Linux kernel module that intercepts OS‑level database socket traffic for monitoring.  
- **S‑Gate**: Enforces real‑time database access policies, blocking or masking unauthorized queries.  
- **S‑TAP**: Captures and forwards database traffic from servers to a Collector.  

## Data Protection Modules
- **File Activity Monitoring (FAM)**: Monitors and records access to unstructured files on NAS, SharePoint, etc.  
- **GDPR**: Supports EU personal‑data protection via discovery, masking, and audit trails.  

## Deployment & Management
- **GIM (Guardium Installation Manager)**: Remotely deploys, upgrades, and manages S‑TAP agents across servers.  
- **Installer**: Handles product installation, initial configuration, and system setup.  
- **License**: Defines usage rights (instances, features) tracked by the Licensing Manager.  

## Monitoring & Logging
- **Log Analysis**: Parses, correlates, and visualizes log entries to spot security incidents or anomalies.  
- **Monitor**: Continuous process that inspects traffic, logs activity, and can block/mask sensitive queries.  
- **Task Scheduler**: Runs predefined jobs at scheduled intervals (exports, audits, etc.).  

## Risk & Compliance
- **Risk Assessment**: Evaluates data‑security posture, highlights gaps, and recommends remediation.  
- **RAR (Risk and Readiness Assessment)**: Measures preparedness against data‑security risks.  
- **Threat Classification**: Prioritizes vulnerabilities using threat intelligence.  
- **Transaction Monitoring**: Tracks end‑to‑end business transactions across multiple calls to detect fraud.  

## Policy & Control
- **Policy**: Rules defining allowed, alerted, or blocked database activity based on user, object, context.  
- **Security Group**: Logical collection of users/roles for consistent policy application.  
- **Separation of Duties**: Requires multiple authorizations for critical actions, reducing insider risk.  
- **Sensitivity Label**: Metadata indicating data classification for automated masking and reporting.  

## Integration & Delivery
- **Management UI**: Web console for configuring components, defining policies, and reviewing reports.  
- **OPSS (Oracle Platform Security Services)**: Integrates Guardium with Oracle security policies at the app layer.  
- **VPN**: Secure tunnel for encrypted data between Guardium components over untrusted networks.  
- **Whitelist**: List of approved users, hosts, or query patterns exempt from alerts/restrictions.  
- **XML Reporting**: Exports audit findings and violations in XML for SIEM/SOAR integration.  

## Non‑Relational Support
- **Non‑Relational Databases**: NoSQL, Hadoop, object stores protected via FAM and specific connectors.

## Centralized Management
**GIM(Guardium Installation Manager)**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## Threat and Compliance Management
**GDPR(General Data Protection Regulation)**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
**GTM(Guardium Threat Management)**: Integrated features for threat detection, vulnerability assessment, and risk scoring within Guardium.  
**WDG(Waterfall Data Governance)**: Governance approach leveraging Guardium data classification and monitoring capabilities for continuous improvement.

## Monitoring and Data Collection
**A-TAP(Application TAP)**: IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.  
**CAS(Change Audit System)**: Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.  
**FAM(File Activity Monitoring)**: Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
**K-TAP(Kernel TAP)**: Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.  
**S-TAP(Software TAP)**: IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  
**WINSTAP(Client TAP)**: Guardium agent installed on Windows workstations to monitor and report privileged user activity.

## Data Aggregation and Reporting
**Aggregator(Guardium Aggregator)**: Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
**Collector(Guardium Collector)**: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

## Policy and Enforcement
**Kerberos(Authentication Protocol)**: Network authentication protocol used by Guardium to verify both user and server identities without transmitting passwords.  
**S-GATE(Software Gate)**: Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  
**SQL(Structured Query Language)**: Standard language for managing relational databases; Guardium inspects traffic to detect anomalies and policy violations.

## Configuration and System Tasks
**NMP(Named Pipe)**: Inter-process communication mechanism monitored by S-TAP on Windows systems; relevant for Oracle ASO traffic.  
**ORA_DRIVER_LEVEL(Driver Level)**: Configuration parameter in guard_tap.ini that specifies the level of Oracle driver support required for ASO and SSL traffic sniffing.  
**UPROC(Unix Process)**: Process running on Unix systems that can be monitored by Guardium for privileged activity and unauthorized actions.

## System Integration and Compatibility
**OSSIM(Open Source Security Information Management)**: Guardium integration that aggregates SIEM data for comprehensive security monitoring.  
**RC4(Encryption Algorithm)**: Legacy symmetric-key encryption algorithm supported by Guardium for backward compatibility with older databases.  
**Syslog(Integration)**: Guardium collects and correlates syslog data to enrich security event monitoring and improve incident response.

## Data Handling and Classification
**MDM(Master Data Management)**: Guardium's capabilities for integrating, validating, and managing data across multiple sources to ensure consistency and accuracy.  
**VDB(Versioned Database)**: Database where multiple versions of data coexist, managed by Guardium to apply policies based on data versioning.

## Utility and Support Tools
**db2inst1(DB2 Instance)**: Example of a database instance name used in commands for configuring K-TAP or S-TAP on DB2 servers.  
**informixoltp(Database Type)**: Example of a specific database type monitored by Guardium, indicating OLTP workloads.  
**install_path(Installation Directory)**: Directory where Guardium appliances or components are installed; crucial for configuration paths.  
**ksh(Bourne-Again Shell)**: Shell environment on Unix systems where Guardium diagnostic and configuration commands are executed.  
**96a697c490(Identifier)**: Example of a UUID used to uniquely identify a particular Guardium entity, such as a policy or configuration.

## IBM Guardium Components Overview

- **A-TAP(Application TAP)**: Kernel-level agent for intercepting local application database calls.
- **Aggregator(Guardium Aggregator)**: Consolidates data from multiple Collectors.
- **CAS(Change Audit System)**: Detects and logs database schema changes.
- **Collector(Guardium Collector)**: Receives, processes, and stores activity data.
- **FAM(File Activity Monitoring)**: Monitors access to unstructured files.
- **GDPR(General Data Protection Regulation)**: Ensures compliance with personal data protection.
- **GIM(Guardium Installation Manager)**: Manages S-TAP agents remotely.
- **K-TAP(Kernel TAP)**: Linux module for intercepting OS-level traffic.
- **S-GATE(Software Gate)**: Enforces real-time access policies.
- **S-TAP(Software TAP)**: Captures and forwards database traffic.

## Guardium Aggregator
Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

## Change Audit System
Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

## Collector
Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

## Functional Authorization Manager
Guardium module that maps functional roles to database privileges and monitors compliance with least privilege policies.

## File Activity Monitoring
Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

## General Data Protection Regulation
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

## Guardium Installation Manager
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## Kernel TAP
Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

## License Manager
Guardium component that tracks and enforces license usage for S-TAP, Collectors, and other Guardium components.

## Policy Builder
Guardium UI component used to create, edit, and manage security policies that enforce access controls and monitor activity.

## Processor Utilization Levels
Guardium setting that defines thresholds for CPU usage alerts and controls how often unit utilization data is processed.

## Real-Time Alerts
Guardium feature that triggers immediate notifications when policy violations or anomalous behavior are detected.

## Resource Monitoring Levels
Guardium configuration that sets thresholds for memory, disk space, and other system resources, triggering alerts when exceeded.

## Role-Based Access Control
Guardium security model that grants users permissions based on predefined roles aligned with job functions.

## Security and Compliance Center
Guardium UI hub that centralizes security policy management, compliance reporting, and audit evidence.

## Security Policy Builder
Guardium UI tool for defining rules that govern database access, data masking, and auditing.

## Sensitivity Level Settings
Guardium parameters that define thresholds for ranking data sensitivity and controlling masking or blocking actions.

## Session Recording Option
Guardium policy rule option that enables logging of entire database sessions for later analysis and compliance reporting.

## Setting Up Approval for S-TAP Installation
Guardium process that defines trusted client IP ranges or hostnames for automated S-TAP deployment.

## SQL Guard
Guardium component that captures and analyzes database queries in real-time for policy enforcement and anomaly detection.

## System Backup Manager
Guardium UI that guides users through steps to create schedule and configure system-wide backups.

## System Health Dashboard
Guardium UI view that displays real-time health metrics for all managed Guardium components.

## System Resources Health Indicator
Guardium metric that aggregates disk space, memory, and CPU usage to provide an overall health score.

## Unit Health Indicator
Guardium health metric calculated from CPU, memory, disk, and network usage to assess processing unit status.

## User-Defined Roles
Guardium security feature that allows administrators to create custom roles beyond the built-in administrative, read-only, and approver roles.

## View Status in Monitor > Reports > Data Management > Restored Data
Guardium location to verify successful database restores; accessed after initiating a restore operation.

## Vocabulary
Guardium terminology reference that provides formal definitions for all product-specific terms and components.

## IBM Guardium Components and Features

### Monitoring Agents
- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **S-TAP**: Software agent on database servers capturing and forwarding traffic.
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic.
- **AppRole**: Authentication role for token-based Vault access based on policies.
- **UniversalConnector**: Kafka Connect plug-in streaming database activity to external systems.

### Core Modules
- **CAS(Change Audit System)**: Detects and records schema, stored procedure, and object configuration changes.
- **Collector**: Receives, processes, and stores database activity data.
- **Aggregator**: Consolidates data from multiple Collectors for enterprise-wide reporting.
- **FAM(File Activity Monitoring)**: Monitors access to unstructured data files on NAS, SharePoint, etc.
- **S-GATE(Software Gate)**: Enforces real-time database access policies, blocking or masking unauthorized queries.

### Data Protection and Compliance
- **GDPR**: EU data protection regulation supported by Guardium discovery, masking, and audit trails.
- **Guardium Data Protection**: Comprehensive suite for database activity monitoring, vulnerability assessment, and data privacy.
- **Backup Collector**: Central storage for archiving audit data from other Collectors.

### Deployment and Management
- **GIM(Guardium Installation Manager)**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents.
- **Vault**: HashiCorp tool for securely storing sensitive data like API keys and credentials.
- **Appliance**: Physical/virtual hardware running Guardium software to process and store audit data.

### Traffic Management and Analysis
- **P-CAP(Packet Capture)**: Default method for installing K-TAP on Linux-UNIX systems, capturing raw network packets.
- **Classifier**: Parses and categorizes database traffic into defined types.
- **Adaptive Analytics**: Uses machine learning to detect anomalous behavior and insider threats.
- **Audit Process**: Series of steps for collecting, analyzing, and reporting database activity for compliance and security.

### Additional Features
- **Approvals**: GUI feature allowing administrators to approve or deny access requests.
- **Cloud Collection**: Ingesting database activity data from cloud-based data services.
- **Cloud Deployment**: Guardium setup hosted entirely on cloud infrastructure.
- **BI Tool Support**: Compatibility with business intelligence tools for auditing queries and data access.

## Interface
Guardium web-based management console for configuring and monitoring.

## Column Masking
Security feature that hides column values based on user privileges.

## Column Validity Check
Rule type to ensure column values meet defined criteria.

## Configured Sources
Interfaces or systems defined within Guardium for data collection.

## Connection Shadowing
Transparent capture of encrypted database traffic.

## Consumer Group
Grouping of users/roles with similar access policies.

## Continuous Learning
Machine learning process adapting threat models based on ongoing analysis.

## Data Encryption
Methods to ensure data confidentiality at rest or in transit.

## Data Source Alias
Aliased representation of a physical data source for easier reference in policies.

## Deduplication
Mechanism to remove duplicate entries from audit logs.

## Discovery
Automated process to identify and catalog databases for monitoring.

## Dynamic Real-Time Policies
Policies that adjust rules on-the-fly based on detected threats.

## Entity Classification
Assignment of data types or roles to facilitate targeted monitoring.

## Exception Handling
Process for managing audit log exceptions and errors.

## FAM Collector
Collector optimized for file activity monitoring.

## File Activity Monitoring
Capturing and analyzing access to unstructured data.

## Filter Rule
Conditional expression for including or excluding data from analysis.

## Full SQL Recording
Logging complete SQL statements for forensic analysis.

## Global Settings
Central configuration menu in Guardium web interface.

## Guardium Appliance Architecture
Hierarchical layout of Guardium components: Collectors, Aggregators, Central Manager.

## Guardium Installation Manager
Central management tool for deploying, configuring, and updating Guardium components.

## Hadoop Support
Monitoring and auditing activities in Hadoop Distributed File System.

## Hot Standby
Secondary appliance ready to take over operations in case of failure.

## Identity Testing
Verification of user credentials and privileges during database connection.

## Inline Policy
Real-time enforcement of actions on monitored database traffic.

## Insider Threat Detection
Analytics and behavior monitoring to flag malicious insider activities.

## Inspection Engine
Core component parsing database traffic for analysis and security enforcement.

## Interface (GUI)
Web-based management console for configuration and monitoring.

## JSON Logging
Logging format for structured data output.

## KSTAP
Kernel-level TAP specific to Solaris systems for intercepting database traffic.

## Log Forwarding
Capability to send audit logs to external systems for storage or analysis.

## Managed Agent
TAP or STAP directly controlled and configured by a Guardium Central Manager.

## Manual Policy
Policies defined by administrators rather than automated learning systems.

## Masking Policy
Rule set to obscure sensitive data in audit logs or during reads.

## Multi-Tiered Deployment
Hierarchical structure of Guardium components managing different database layers.

## Network Segmentation
Defining and monitoring database traffic within distinct network segments.

## NoSQL Database Support
Auditing and securing NoSQL database operations.

## Object Masking
Policy-driven concealment of specific database objects from unauthorized users.

## One-Time Password
Temporary password for privileged access to Guardium interfaces or data.

## Oracle Audit Vault
Integration with Oracle's Audit Vault for enhanced audit data management.

## Outlier Detection
Statistical analysis identifying abnormal activities.

## Policy Builder
GUI tool for creating and editing Guardium policies.

## Privileged User
User account with elevated permissions requiring enhanced monitoring.

## Real-Time Alerting
Immediate notifications triggered by policy violations during data access.

## Remote Deployment
Process of installing and configuring Guardium agents on remote database servers.

## Role-Based Access Control
Restricting system access based on user roles and responsibilities.

## SaaS Deployment
Cloud-based deployment model where Guardium services are provided as a service.

## Schema Change Monitoring
Feature to detect and log alterations to database schemas or objects.

## Secondary Aggregator
Redundant Aggregator for failover in a multi-tiered deployment.

```markdown
Active Directory Source(Identity store): IBM Guardium data source that connects to an Active Directory server to retrieve user and group identity information.
BISO(Business Impact Security Officer): Role in Guardium responsible for translating business impact into security controls and audit requirements.
Data Security Posture(Entity): Guardium metric that quantifies the overall health of data security based on compliance, risk, and activity scores.
Entitlement Report Parameter(Filter): Control that narrows entitlement report results by specifying users, roles, or permissions.
FAM(IBM Guardium File Activity Monitoring): Module that monitors access to unstructured files on network‑attached storage and cloud repositories.
Guardium Key Lifecycle Manager(Encryption Manager): Tool for creating, rotating, and managing encryption keys used to protect sensitive data in Guardium‑monitored databases.
Guardium Reconciliation Report(Entity): Report that compares configuration data from Guardium with actual state in target databases to detect drift or inconsistencies.
Guardium Risk Assessment(Evaluation): Automated process that scores the security risk of each monitored database based on configuration, vulnerabilities, and activity patterns.
Guardium Sequence Builder(Automation): Drag‑and‑drop interface for creating custom workflows that chain Guardium actions (e.g., alerts, quarantines, reports).
Guardium Topology Top‑Down(User Perspective): View in Guardium that starts with the central manager and shows downstream collectors and databases in a hierarchical layout.
Guardium UI(User Interface): Web‑based console for configuring, managing, and reporting on Guardium data protection activities.
Guardium Unified Dashboard(Dashboard): Single pane that aggregates key metrics from collectors, aggregators, and central managers into one view.
Guardium View(User Interface): Customizable panel within the Guardium UI that displays data such as alerts, reports, or compliance status.
Identity Source(Application): Data source within Guardium that supplies user, group, and role information for privilege‑usage analysis.
Kernel TAP(Linux Agent): Guardium component (K‑TAP) that runs in the kernel to capture OS‑level database traffic on Linux platforms.
Kerberos Authentication(Protocol): Authentication method supported by Guardium for secure connection to monitored database servers.
Kerberos Credential Caching(Caching): Guardium option that stores Kerberos tickets locally to reduce repeated authentication overhead.
Kerberos Encryption(Encryption): Guardium feature that decrypts and inspects Kerberos‑encrypted database traffic.
KVDM(Kerberos Virtual Data Module): Guardium module that normalizes and presents Kerberos‑protected data in audit reports.
Log‑Parser(Log Analyzer): Guardium utility that parses unstructured log files (e.g., syslog, Windows Event logs) and converts entries into structured audit records.
MySQL Process ID Mapping(Feature): Guardium capability that correlates MySQL session IDs with underlying OS process IDs for accurate activity tracking.
Network Traffic Analyzer(Feature): Guardium component that parses raw packet captures to identify database‑specific protocol details beyond S‑TAP captures.
Object Type Enumeration(Knowledge): Process of mapping database object categories (e.g., table, view, stored procedure) to Guardium’s internal type codes.
Orchestrator(Action): Guardium workflow step that triggers external systems (e.g., SIEM, ticketing) based on policy violations detected in real time.
Privilege Abuse Detection(Feature): Guardium rule set that flags usage of granted privileges inconsistent with baseline behavior or policy definitions.
Query Builder(Feature): Guardium UI element that assists u
```

te): Common attribute in Guardium reports that shows the database name and groups similar values into a single column.
Database Server Port(Port): Identifies the TCP/IP port used by a database server for client connections; used in Guardium policies and alerts.
DataRisk Manager(Risk Management Package): IBM security platform that integrates with Guardium to provide advanced risk assessment and data governance capabilities.
DB User Name(Username): Attribute that captures the database user name associated with each activity record; essential for user‑level reporting.
DB2 K‑TAP(Kernel TAP): Guardium kernel module for IBM DB2 databases that captures and forwards SQL traffic without impacting performance.
DB2 S‑TAP(Storage TAP): Light‑weight agent installed on DB2 database servers that captures SQL statements in real time for monitoring.
Delete User(Security Action): Guardium action that removes a user account from the system or disables it after detecting suspicious activity.
DMZ(Demilitarized Zone): Network segment that separates an internal network from external networks; Guardium may deploy collectors in the DMZ for secure data collection.
E‑TAP(Event TAP): Alternative to S‑TAP that captures database events from the audit log rather than intercepting live traffic.
Encrypt TAP(Encryption TAP): Guardium sensor that captures encrypted database traffic by pairing with an encryption key manager.
Encryption(Key Management): Process of converting data into a secure format that can only be read with the correct decryption key; Guardium supports encryption for data at rest and in transit.
Enrichment(Feature): Guardium capability that augments raw SQL activity data with contextual information such as application name, host name, or user role.
Error Code(Error Identifier): Numeric or textual code returned by a database server indicating the result of a SQL statement; captured by Guardium for troubleshooting.
Examination(Filtering): Guardium process that applies user‑defined criteria to session or activity data to isolate relevant records.
Export Archive(Log Export): Functionality that packages Guardium reports or raw data into a file for transfer to external systems or long‑term storage.
External Log Collector(Reporting): Guardium component that ingests log data from non‑database sources (e.g., web servers) for unified analysis.

## Attribute Naming

**Database Name**: Attribute in Guardium reports that consolidates database names to simplify reporting.

## Monitoring

**Database Server(Infrastructure)**: Physical or virtual server hosting databases; monitored by S-TAP or A-TAP agents.  
**A-TAP(Application TAP)**: IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.  
**S-TAP(Software TAP)**: IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Data Management

**Data mart(Data warehouse)**: Subset of a data warehouse focused on a specific business line or team.  
**Destination Target(Entity)**: The final repository or system to which Guardium data is exported for further processing or storage.

## Features

**Decryption(Feature)**: Guardium capability to decrypt encrypted traffic for inspection.  
**File Activity Monitoring(Feature)**: Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
**GDPR(General Data Protection Regulation)**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
**S-GATE(Software Gate)**: Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  
**SVM(Security Vulnerability Management)**: Process of identifying, classifying, and mitigating vulnerabilities in security systems; Guardium includes features for vulnerability assessment.  
**Value Change Auditing(Feature)**: Feature in Oracle Guardium that provides audit capabilities for changes made to database values.

## Administration

**Default Data Source(Concept)**: Predefined source from which Guardium imports data in the absence of specified sources.  
**Extraction Log(Report)**: Log file generated by Guardium detailing the status and details of data extractions.  
**GuardAPI(Rest API)**: Guardium's command-line interface for automating tasks and integrating with external systems.  
**Guardium Aggregator(Aggregator)**: Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
**Guardium Collector(Collector)**: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.  
**Guardium Installation Manager(GIM)**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
**Installation Manager(GIM)**: See Guardium Installation Manager.

## Reporting

**Indirect client IP(Application)**: Client IP address obtained through proxy or NAT devices; Guardium can track and report these IPs.  
**Logging(Log)**: Process of recording Guardium events and activities for audit and analysis purposes.  
**Logins(LGU)**: Entity in Guardium representing user logins, tracked for security monitoring.  
**Remote User Address(Network)**: IP address or hostname representing a remote user's location; used in query construction and filters.

## Tools

**Review/Sign(Feature)**: Guardium functionality separate from the audit process, focusing on reviewing and signing off on audit results.  
**Runtime Parameter(Feature)**: Parameter used in query execution that is defined or evaluated at the time the query runs; supports dynamic query construction.

## Virtualization

**Virtual Machine Activity(Feature)**: Monitoring and recording of activities within virtual machine environments; relevant for virtualized database servers.  
**vTAP(virtual TAP)**: Virtual machine that performs similar functions to S-TAP, intercepting traffic in virtualized environments.

## Central Manager
Guardium appliance that coordinates distributed Collector and Managed Unit installations.

## cert
Digital certificate used to encrypt communications between Guardium components and external systems.

## CLI
Tool for executing Guardium administrative functions and retrieving state information via text commands.

## Collector
Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

## Compliance Policy
Built-in or custom policy within Guardium designed to enforce industry regulations such as PCI-DSS, HIPAA, or GDPR.

## DPIF
Configurations that define how traffic should be parsed, categorized, and monitored by S-TAP.

## Entitlement
Feature that monitors and records activities of privileged database users with elevated permissions.

## Field-Level Inspection
Fine-grained monitoring that captures and reports access to specific columns within tables.

## G-IM
Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

## GDPR
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

## Global Policy
Policy automatically applied to all instances in a Central Manager environment unless overridden.

## Granular Policy Association
Ability to apply policies selectively to specific database instances, users, or groups.

## High Availability
Configuration ensuring continuous Guardium operation through automatic failover and replication.

## Host Name
Unique identifier assigned to each Guardium appliance and collector in the network.

## LDAP
Standard protocol used by Guardium for authentication against a directory service.

## MFA
Security process requiring two or more verification factors for access to Guardium features.

## MySQL
Support for auditing and monitoring MySQL database instances and capturing their activity.

## NIST
Structure within Guardium for implementing cybersecurity best practices, following NIST Cybersecurity Framework.

## OpenID
Authentication protocol supported by Guardium for user login, particularly with external identity management systems.

## PCI-SSC
Framework for guarding against credit card data breaches; Guardium provides tools to help meet its requirements.

## Policy Rule
Specific condition or directive within a policy that defines when alerts and actions should be triggered.

## Privileged Account
Special access levels that allow comprehensive control over system settings and high-level monitoring.

## RBA
Administrative framework granting users permissions based on assigned roles.

## Risk
Facility for assigning severity levels to violations to aid in risk prioritization.

## Role
Defined set of permissions determining what actions a user can perform.

## SAML
Protocol for exchanging authentication and authorization data between an identity provider and Guardium.

## S-GATE
Component enforcing real-time database access policies and blocking or masking unauthorized queries.

## Scheduling
Automation feature for running regular jobs such as purging reports, updating licenses, or exporting data.

## SGATE
Software implementation of Guardium's security policies controlling database access in real time.

## S-TAP
Software agent installed on database servers that captures and forwards database traffic to a Collector.

## SSL
Security protocol ensuring encrypted communications between Guardium components, often configured for LDAP connections.

## TLS
Act of decrypting encrypted traffic from a client before passing it to the database within Guardium.

## User
Active security session within Guardium granted to an authenticated individual.

## Virtualization
Compatibility of Guardium agents with virtual environments, allowing monitoring of instances on VMs.

## VMware
Support for Guardium to monitor activity on VMware-hosted virtual systems.

## Whitelist
List of specific commands, queries, or users exempt from normal policy evaluations and monitoring.

## X-Force
Integration of IBM X-Force threat intelligence into Guardium for enhanced detection of sophisticated threats.

## AutoML
Feature that automatically generates machine learning models for anomaly detection without user configuration.

## Cascade Filter
Conditional

### Guardium Rule Types and Components
- **Data Access Rule**: Nests filters to create complex access policies based on context.
- **SQL Crawling**: Automated process to verify policy rules by executing queries against databases.
- **A-TAP (Application TAP)**: Kernel-level agent that intercepts database calls made by local applications on the server.
- **K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for monitoring.

### Guardium Modules and Features
- **FAM (File Activity Monitoring)**: Monitors access to unstructured data files on NAS, SharePoint, etc.
- **CDP (Continuous Data Protection)**: Encrypts and masks data in motion and at rest.
- **GDPR**: Support for EU's personal data protection regulation via discovery, masking, and audit trails.
- **QRW Translation**: Real-time query rewriting to mask sensitive data based on policies.
- **S-GATE**: Enforces real-time database access policies, blocking or masking queries as needed.

### Guardium Agents and Collectors
- **S-TAP (Software TAP)**: Agent installed on database servers to capture and forward traffic to a Collector.
- **macOS-S-TAP**: S-TAP agent specifically for macOS systems.
- **TAP Classification**: Categorizes S-TAP agents as Primary (full monitoring) or Surrogate (limited monitoring).

### Centralized Tools and Services
- **GIM (Guardium Installation Manager)**: Remotely deploys, upgrades, and manages S-TAP agents across servers.
- **Guardium Aggregator**: Consolidates data from multiple Collectors for enterprise-wide reporting.

### Guardium Security and Compliance
- **Transparent Pass-Through (TP2)**: Mode to allow unencrypted traffic flow without logging for performance tuning.
- **Entitlement Analysis**: Maps user permissions to roles to detect excessive privileges.
- **User Behavior Analytics (UEBA)**: Applies machine learning to detect insider threats through activity pattern analysis.
- **Privileged User**: Identity type for users with elevated permissions, enabling advanced monitoring and controls.

### Guardium Compliance and Data Protection
- **Data Classification**: Identifies and categorizes sensitive data across the enterprise.
- **ACPC (Active Policy Control)**: Enforces data access policies in real-time.
- **Secure Copy**: Encrypted file transfer mechanism for moving audit data between appliances.
- **BDE (Big Data Engine)**: Monitors interactions with big data platforms like Hadoop and Spark.
- **COR (Correlation Rule)**: Identifies security incidents by analyzing patterns across multiple events or logs.

## Guardium Features and Integrations

**DCC (Distributed Compliance Checklist)**: Guards against compliance violations in distributed systems.  
**DLP (Data Loss Prevention)**: Prevents data exfiltration.  
**ECS (Elastic Cloud Server)**: Monitors cloud databases.  
**ENCR (Encryption)**: Encrypts data at rest and in transit.  
**ETL (Extract Transform Load)**: Monitors data pipeline movements.  
**HANA (SAP HANA)**: Detects unauthorized access.  
**HC (Hardening Checklist)**: Enhances database security.  
**K8S (Kubernetes)**: Monitors database interactions in containers.  
**LDAP (Lightweight Directory Access Protocol)**: Monitors user directory access.  
**MFA (Multi-Factor Authentication)**: Enforces strong access controls.  
**OAM (Operational Audit Management)**: Manages audit processes.  
**PHI (Protected Health Information)**: Secures health data.  
**REST (Representational State Transfer)**: Secures RESTful APIs.  
**SSH (Secure Shell)**: Protects database sessions.  
**URL (Uniform Resource Locator)**: Enforces policies on web interactions.  
**VM (Virtual Machine)**: Monitors virtualized environments.  
**VMware**: Secures databases in VMware infrastructure.  
**WAN (Wide Area Network)**: Secures data transfer across networks.  
**WS (Web Service)**: Monitors web service APIs.  

**FAI (Failed Login Attempts)**: Tracks failed access attempts.  
**FEAT (Features)**: Specific Guardium capabilities.  

**DLL (Dynamic Link Library)**: Supports S-TAP deployment.  
**PRO (Process)**: Monitors system processes.  
**PRVT (Privilege)**: Manages privileged access.  

**MC (Memory Cache)**: Improves data processing efficiency.  
**ME (Memory Encryption)**: Encrypts memory contents.  

**ITRC (IBM Technical Review Committee)**: Ensures quality of security assessments.  
**NO (Publish Notification Option)**: Sends alerts and reports.  

**NIST (National Institute of Standards and Technology)**: Supports compliance frameworks.  

**PaaS (Platform as a Service)**: Monitors PaaS environments.  
**QB (Quarter 1)**: Supports quarterly reporting.  

**HIDS (Host-Based Intrusion Detection System)**: Host-level intrusion monitoring.  
**RACF (Resource Access Control Facility)**: Secures z/OS databases.  

**RSYS (Remote Syslog)**: Integrates with SIEM systems.  

**SDM (Structured Data Monitoring)**: Protects structured databases.  
**STORE (Store)**: Represents monitored databases.  

**TB (Transparent Block)**: Encrypts data blocks at storage.  
**TS (Tabular Stream)**: Efficient data format for querying.  

**UDF (User-Defined Function)**: Monitors custom database functions.  
**XDR (Xamarin Development Reference)**: Integrates with Xamarin for mobile security.

## Guardium Features

**A-TAP**: Kernel-level agent that intercepts database calls made by local applications directly on the database server.  
**Aggregator**: Appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
**CAS**: Module that detects and records changes to database schemas, stored procedures, and object configurations.  
**Collector**: Appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.  
**DataLake Connector**: Component that securely transfers log files and activity data to customer-managed data lakes.  
**FAM**: Module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
**GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
**GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
**K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for Guardium monitoring.  
**S-GATE**: Component that enforces real-time database access policies and blocks or masks unauthorized queries.  
**S-TAP**: Software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.  

## Key Components

**ASE**: CyberArk solution that automates privileged account credential management for applications and services.  
**CAFM**: Guardium module for monitoring file activity on certified applications such as ERP and CRM systems.  
**CIM**: Standard framework for describing management information; used by Guardium to normalize log data from heterogeneous sources.  
**CSF**: Set of guidelines for improving cybersecurity risk management; Guardium mappings help align with frameworks like NIST.  
**DAP**: Collection of metadata about a data source within Guardium, including sensitivity, criticality, and compliance status.  
**DBPROT**: Feature set that provides real-time monitoring, auditing, and protection of database activity.  
**EORA**: Central repository for storing and managing orchestration workflows across the enterprise.  
**GDM**: Tool for collecting, aggregating, and consolidating data from various Guardium collectors into a unified view.  
**GIM_CLIENT**: Component of the Guardium Installation Manager that resides on database servers and handles S-TAP agent installation and lifecycle.  
**GLM**: (incomplete entry, skipped as noise)

Lifecycle Management: Guardium framework for centralized configuration and security policy enforcement across all appliances.

GRT (Guardium Readiness Tool): Utility that assesses an organization's readiness for Guardium implementation and provides deployment recommendations.

ICS (IBM Cloud Security): IBM suite of cloud-native security services, including Guardium capabilities for hybrid cloud environments.

ITO (Information Trust Officer): Role responsible for data governance, compliance, and security using Guardium.

LDAPI (LDAP Interface): Guardium configuration option enabling LDAP directory services authentication.

MDR (Monitoring Data Repository): Central Guardium database storing and indexing all collected security and compliance data.

NAK (Not Acknowledged): Status indicating unsuccessful job or process completion in Guardium.

OOP (Object Oriented Programming): Programming paradigm for Guardium extensibility, such as custom report development.

PAT (Port Address Translation): Network technique mapping database server ports to collector ports for secure traffic forwarding in Guardium.

QBE (Query By Example): Guardium feature allowing template-based log data searching instead of complex queries.

RBAC (Role-Based Access Control): Guardium security mechanism assigning permissions based on user roles.

SFE (Structured File Export): Guardium function exporting collected log data in structured formats like CSV or XML for external reporting.

TAM (Threat and Anomaly Management): Guardium module detecting and responding to security threats by analyzing database activity patterns and anomalies.

UCI (Unified Configuration Interface): Centralized CLI and GUI managing configurations, policies, and system settings across Guardium appliances.

A-TAP (Application TAP): IBM Guardium kernel-level agent intercepting database calls by local applications directly on the server.

Aggregator (Guardium Aggregator): Guardium appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.

ASO (Oracle Advanced Security Option): Oracle database feature encrypting data, supported by Guardium S-TAP for capturing encrypted traffic.

CAS (Change Audit System): Guardium module detecting and recording database schema, stored procedure, and object configuration changes.

Centrify (Centrify Agent): Lightweight software integrating non-LDAP directory services with Guardium privilege management.

Collector (Guardium Collector): Appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

FAM (File Activity Monitoring): Guardium module monitoring and recording access to unstructured data files on NAS, SharePoint, etc.

GDPR (General Data Protection Regulation): EU personal data protection regulation supported by Guardium through discovery, masking, and audit trails.

GIM (Guardium Installation Manager): Centralized tool for remote S-TAP agent deployment, upgrades, and management across database servers.

Guardium Appliance (Guardium Appliance): Physical or virtual machine provided by IBM for running the Guardium software suite and related services.

Guardium Cloud Pak (Guardium Cloud Pak): IBM product offering Guardium components integrated with the IBM Cloud Pak platform.

Gzipped File (Unzipped File): Compressed diagnostic dump requiring extraction before analysis.

GUI (Graphical User Interface): Web-based or desktop interface for Guardium configuration and monitoring tasks.

HostOS (Host Operating System): Underlying OS on which Guardium S-TAP or Collector is installed.

IBM Guardium (IBM Guardium): IBM's database activity monitoring and data security platform.

IBM i (IBM i): IBM's operating system for Power Systems servers, supported by Guardium for database monitoring.

IBM z/OS (IBM z/OS): Mainframe operating system supported by Guardium for auditing database access.

Installation Status (Installation Status): Indicator showing S-TAP agent installation, running state, or required action.

K-TAP (Kernel TAP): Linux kernel module intercepting OS-level database socket traffic for Guardium monitoring.

OS-Level Monitoring (OS-Level Monitoring): Guardium feature collecting data directly from OS-level sockets without database-specific hooks.

Packets (Packet Capture): Intercepted and recorded data flows by S-TAP for analysis in Guardium.

Protocol Type (Protocol Type): Database communication protocol used by Guardium, such as Oracle, MSSQL, Teradata.

Query (Monitored Query): SQL statement inspected by Guardium S-TAP against policy rules.

Report (Generated Report): Summary or detail document generated by Guardium from monitored activity data.

Resilience (Resilience of S-TAP): Ability of S-TAP to continue operating under failure conditions like database restarts or network dropouts.

S-GATE (Software Gate): Guardium component enforcing real-time database access policies, blocking or masking unauthorized queries.

S-TAP Application (S-TAP Application): Applications, scripts, or services relying on database connections monitored by Guardium S-TAP.

Secure Shell (SSH): Protocol used for remote command execution and file transfer during S-TAP installation.

Signatures (Signature Libraries): Predefined patterns of malicious or risky database behavior used by Guardium for policy enforcement.

lation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

## Guardium Components

**A-TAP (Application TAP)**: Kernel-level agent intercepting local application database calls on the server.

**Aggregator**: Central Guardium appliance consolidating activity data from multiple Collectors.

**CAS (Change Audit System)**: Module detecting and recording changes to database schemas, stored procedures, and objects.

**Collector**: Appliance receiving, processing, and storing database activity data from S-TAP agents.

**FAM (File Activity Monitoring)**: Module monitoring and recording access to unstructured data files on NAS, SharePoint, etc.

**GDPR**: EU regulation on personal data protection supported by Guardium through discovery, masking, and audit trails.

**GIM (Guardium Installation Manager)**: Tool for remote deployment, upgrading, and management of S-TAP agents across servers.

**K-TAP**: Linux kernel module intercepting OS-level database socket traffic for monitoring.

## Guardium Features

**Activity-Monitoring-Observable**: Event recording database session activity for compliance and analysis.

**Alert**: Notification triggered by predefined policy conditions in Guardium.

**Alert Policy**: Set of rules defining conditions for generating alerts.

**Audit Archive**: Feature archiving audit data for long-term retention and compliance.

**Audit Build Audit**: Process creating audit records from monitored database activities.

**Audit Trail Audit**: Continuous record of database actions for compliance and forensic analysis.

**Audit Window**: Time period for collecting and processing audit data.

## Guardium Security

**Authentication**: Verifying identity of users or processes accessing Guardium resources.

**Authorization**: Granting or denying privileges to authenticated users based on policies.

**Encryption (TLS)**: Protocol securing communications between client and server applications; used by Guardium for encrypted data transport.

**Windows Credential Guard**: Microsoft feature protecting credentials with virtualization-based security; Guardium can integrate to monitor access where enabled.

## Core Components
- **Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.
- **Collector**: Receives, processes, and stores database activity data forwarded by S-TAP agents.
- **S-GATE**: Enforces real-time database access policies and blocks or masks unauthorized queries.
- **S-TAP**: Captures and forwards database traffic to a Guardium Collector.

## Agents
- **A-TAP**: Intercepts database calls made by local applications directly on the database server.
- **K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for monitoring.

## Modules & Features
- **CAS**: Detects and records changes to database schemas, stored procedures, and object configurations.
- **FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
- **GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents.
- **GDPR**: Supports EU data protection regulation via discovery, masking, and audit trails.
- **Redaction**: Real-time data masking technique that removes sensitive values from query results.

## Other
- **Watchlist**: Tracks specified database objects and generates alerts when activity occurs on them.

## Glossary

- **Aggregator(Guardium Aggregator)**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.
- **A-TAP(Application TAP)**: Kernel-level agent that intercepts database calls from local applications on the server.
- **ASO(ALT Security Offering)**: Monitors encrypted database traffic using ASO or SSL/TLS protocols.
- **bf60d6ae(Build Fix 60D6AE)**: Specific software build patch.
- **Cas(Change Audit System)**: Detects and records changes to database schemas, procedures, and configurations.
- **Collector(Guardium Collector)**: Receives, processes, and stores database activity data from S-TAP agents.
- **Collection Limit Rate**: Maximum relocations allowed after a full policy and assessment load.
- **DAM(Database Activity Monitoring)**: Monitors database transactions in real-time for anomalies.
- **DLM(Data Lifecycle Management)**: Manages data retention, archiving, and deletion policies.
- **FAM(File Activity Monitoring)**: Monitors access to unstructured data files on NAS and similar storage.
- **Gdpr(General Data Protection Regulation)**: EU regulation supported by Guardium for data protection compliance.
- **Gim(Guardium Installation Manager)**: Deploys, upgrades, and manages S-TAP agents remotely.
- **Grouping**: Aggregates similar data sources, servers, or policies for management.
- **I-Am-Cluster-Node Registry**: Disables registry certificate installation on cluster nodes.
- **Oracley-Cli(Oracle Call Interface)**: API for accessing Oracle databases, monitored by Guardium.
- **Protocol**: Rules for data exchange between devices, e.g., LDAP, HTTP, FTP.
- **Ras(Remote Access Server)**: Enables remote management and monitoring of database activity.
- **S-Gate(Software Gate)**: Enforces real-time access policies and blocks unauthorized queries.
- **Stapling**: Attaches S-TAP agents to databases for data collection.
- **Threshold(Alert Threshold)**: Configurable limit that triggers alerts when exceeded.
- **Udm(User Defined Monitor)**: Custom monitoring definitions created by users.
- **Vulnerability Assessment**: Scans databases for vulnerabilities and generates risk scores.

## IBM Guardium Components

### Monitoring & Data Protection
- **A-TAP**: Kernel-level agent intercepting local application database calls.  
- **FAM**: Monitors access to unstructured files on NAS/SharePoint.  
- **K-TAP**: Linux kernel module for OS-level socket traffic capture.  

### Compliance & Governance
- **GDPR**: Supports EU personal data protection via discovery, masking, audits.  
- **Cas**: Audit system detecting schema, procedure, and object changes.  

### Deployment & Management
- **GIM**: Central tool for remote S-TAP deployment, upgrades, and management.  
- **S-TAP**: Database server agent capturing traffic for Clusters.  

### Infrastructure & Optimization
- **Collector**: Processes and stores activity data from S-TAP agents.  
- **Aggregator**: Consolidates Collector data for enterprise-wide reporting.  
- **MgAs5rvOneAccessAgent**: Microgateway agent enabling real-time access control.  

### Specialized Features
- **MTU**: Network optimization for efficient packet sizes.  
- **VGs**: Groups multiple database instances for unified management.  

### Networking & Protocols
- **Natural Language Processing**: AI analysis of SQL queries for risk detection.  
- **Masking Engine**: Dynamic obscuring of sensitive data in query results.

## Guardium Components

**A-TAP**: Kernel-level agent intercepting local application database calls on the server.

**Aggregator**: Appliance consolidating activity data from multiple Collectors.

**CAS**: Module detecting and recording schema, stored procedure, and object configuration changes.

**Collector**: Appliance receiving, processing, and storing activity data from S-TAP agents.

**FAM**: Module monitoring and recording unstructured file access on NAS, SharePoint, etc.

**GuardAPI**: REST API for automating Guardium tasks and integrating with external systems.

**GDA**: Tool automating Guardium installation, configuration, and provisioning.

**GIM**: Centralized tool for remote S-TAP agent deployment, upgrades, and management.

**Insider Threat Module**: Extension analyzing user behavior to detect malicious insider activity.

**K-TAP**: Linux kernel module intercepting OS-level database socket traffic.

**S-GATE**: Component enforcing real-time database access policies and blocking unauthorized queries.

**S-TAP**: Software agent on database servers capturing traffic and forwarding to Collectors.

## Security & Compliance

**Audit logging options**: Definition of logged actions and events for compliance and forensics.

**Categories**: Logical groups for S-TAP agents or data sources facilitating management and reporting.

**Disconnect on Invalid Certificate**: Terminates connections with invalid or unrecognized certificates.

**External S-TAP**: Agent monitoring database traffic from outside the monitored server.

## Kernel TAP
Linux kernel module that monitors database traffic at the kernel level.

## Plugin values
Configuration settings for S-TAP plugins that enable specific monitoring capabilities or database support.

## SQLNET parameters
Oracle network parameters to enable and configure Kerberos authentication.

## API Authorization
Permission granted to an API to access specific Guardium resources.

## Access Control List
List of permissions defining which users/groups can access Guardium resources or actions.

## Active Directory Federation Services
Microsoft identity provider enabling Guardium user authentication via Azure.

## Agentless Scan
Guardium feature performing database vulnerability scans without local agents.

## Agent Scanner Retry Count
Parameter specifying retry attempts before marking an agent-based scan as failed.

## Alert
Notification generated by Guardium when a predefined condition is triggered.

## Anomaly Detection Mode
Guardium setting determining how anomaly detection algorithms monitor activities.

## Appendix
Supplementary information at the end of Guardium documents or reports.

## Architecture
Centralized management and reporting environment used by Guardium.

## Applicable Version
Guardium version or module where a feature or setting is applicable.

## Archive Path
Directory path where Guardium stores archived data or logs for retention.

## ASAP
As Soon As Possible, indicating priority or urgency level for Guardium tasks.

## Assessment
Systematic evaluation of database security, policies, or compliance posture in Guardium.

## ATL VM Manager
Virtual machine environment used by Guardium for centralized management and reporting.

## AUTHENTICATION
Process of verifying user identities before granting Guardium access.

## AUTHORIZATION
Granting or denying access rights to Guardium functions or data based on roles.

## AUTHZ
Authorization process determining user access and actions in Guardium.

## AWS
Amazon Web Services platform supported by Guardium for cloud database security.

## AWS IAM
Amazon Web Services IAM integrated with Guardium for access and permission management.

## B-TAP using ESSID
Method of deploying B-TAP agents using Extended Service Set Identifiers for network segmentation.

## Baseline Mode
Guardium feature establishing baseline profiles of normal database activity.

## Bulk Insert/Delete Statistics
Parameter tracking volume and frequency of bulk data insert/delete operations for performance monitoring.

## BV Ruler Report
Detailed report assessing and summarizing security and compliance aspects in Guardium.

## CAS
Change Audit System module detecting and recording database schema and object changes.

## CDM Version
Version of Cloud Data Management software integrated with Guardium for cloud database management.

## Cert Target ID
Identifier assigned to a certificate issued by Guardium's certificate authority for validation.

## Change Control
Guardium feature logging and controlling changes to database objects, configurations, and access.

## Check for Older Version
Option evaluating and installing updates or patches if outdated software components are detected.

## CLI Compliance Inclusion By Default
Command-line parameter configuring default compliance settings during Guardium deployment.

## Collect
Guardium command collecting and importing database audit data into the central repository.

## Compare SSG
System Security Guide reference document for configuring security best practices and compliance standards.

## Construct NA Code
Technical identifier used in Guardium's Data Classification module to categorize data entities.

## Guardium Components and Modules
**Collector**: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.  
**Aggregator**: Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
**S-TAP**: Software agent installed on database servers capturing and forwarding traffic to a Collector.  
**A-TAP**: Kernel-level agent intercepting database calls made by local applications directly on the server.  
**FAM**: Module monitoring and recording access to unstructured data files on NAS, SharePoint, etc.  
**GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  

## Guardium Configuration and Management
**GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across servers.  
**GROUPING**: Mechanism in reports and policies to aggregate data based on IP address, user name, or data type.  
**K-TAP**: Linux kernel module intercepting OS-level database socket traffic for monitoring.  
**KERBEROS**: Network authentication protocol supported for authentication and auditing of secured databases.  

## Security and Compliance
**S-GATE**: Component enforcing real-time access policies and blocking or masking unauthorized queries.  
**DES**: Symmetric-key algorithm referenced for encryption of electronic data.  
**CAS**: Module detecting and recording changes to database schemas, stored procedures, and object configurations.  
**api_target_host**: Parameter specifying target host or IP address where an API executes.  

## Data Discovery and Classification
**classifier**: Categorizes database traffic and classifies data based on content.  
**classifier_classification_type**: Defines classification types like PII, PCI, or custom categories.  
**auto_discovery**: Automatically detects database servers and ports for scanning or monitoring.  
**discovery_disruptive_mode**: Indicates whether discovery scans may impact performance or availability.  

## Monitoring and Auditing
**real_time_monitoring**: Continuous monitoring of database activity as it occurs.  
**profile**: Collection of settings defining how Guardium collects and processes data for specific environments.  
**dynamic_sampling_rate**: Controls sampling rate during classification based on data volume or needs.  
**range_sampling**: Samples data within specified ranges for partial analysis.  

## Data Access and Sampling
**create_datasource**: Command creating a new datasource object, requiring valid type values.  
**delete_datasource_groupRef_by_id**: Removes reference to a datasource group, requiring appId, datasourceId, and objId.  
**disable_sampling**: Turns off data sampling in classification, requiring full data evaluation.  
**required_parameters**: Essential parameters needed for API commands, such as API target host or template set label.  

## API and Reporting
**request**: API call or user request performing specific functions within Guardium.  
**report**: Aggregated data from Conduct Risk Reports on data access and usage.  
**rest_api**: Web service interface accessing Guardium functionalities via HTTP protocols.  
**rest_template**: Predefined structure ensuring correct parameter passing and response handling.  

## Error Handling and System Tables
**guardium_error_table**: Stores error logs and messages from Guardium processes and modules.  
**is_parameter_changed**: Flag indicating whether a configuration parameter has been altered.  
**hadoop_hdfs_config**: Settings for integrating Hadoop Distributed File System data sources.  
**scheduler**: Manages timing and execution of jobs, scans, and automated tasks.

## Access Analyzer
Evaluates user permissions against data sensitivity to identify excessive rights.

## Administrative Role
Internal user type with full system configuration and management privileges.

## APACHE
Open-source HTTP server; Guardium monitors web service access with S-TAP or S-GATE.

## Archive
Moves older audit data from primary to secondary storage for long‑term retention.

## Assessor
Creates and configures security assessments, including test selection and severity.

## Audit
Reviews recorded activity logs and assessment results to verify compliance and identify violations.

## AUDITOPRT
Port number used for audit data transfer between S-TAP and Collector.

## Authorization Change
Monitors schema object grants, revokes, or privilege modifications.

## Backup
Exports policies, assessments, and configuration to preserve state before upgrades or migrations.

## Baseline
Initial activity patterns recorded for a database; used as reference for anomaly detection.

## Blocked
Result flag indicating a query was automatically denied by S-GATE based on a policy rule.

## Bot
Automated program interacting with databases; Guardium flags bot‑style query patterns.

## Cell Analysis
Inspects individual database records to evaluate row‑level access patterns.

## Centrally Managed
Configuration mode where S-TAP agents receive settings from a Collector.

## Change
Alters to database objects, configurations, or permissions monitored by CAS module.

## Collector
Appliance receiving, processing, and storing database activity from S-TAP agents for reporting.

## Compliance
Alignment with regulatory standards (GDPR, HIPAA, PCI‑DSS) tracked via assessment results.

## Configuration Drift
Detectable deviation from approved Guardium appliance or S-TAP settings over time.

## CRAWLER
Automatically discovers new database servers and services in the network.

## DATETIME
Column data type representing date and time; Guardium reports include DATETIME fields for timestamps.

## DISTRIBUTED
Guardium deployment spanning multiple Collectors/Aggregators for enterprise‑wide aggregation.

## Encryption
Protects data in transit or at rest; Guardium monitors encrypted SQL traffic via S-TAP kernel modules.

## Entity
Distinct database object (table, view, procedure, file) tracked for analysis or protection.

## Event
Singleton occurrence of a monitored action recorded in Guardium activity logs.

## Exclusion
Filter applied to ignore benign activity or false‑positive detections.

## Export
Writes collected audit data or assessment results to external files or systems for archiving.

## External Channel
Secure conduit (e.g., TLS) for transmitting data to aggregators or external SIEMs.

## File
Structured or unstructured data object on filesystems; monitored by File Activity Monitoring module.

## GATE
Rule governing database access; synonymous with policy or rule.

## GIM
Tool for deploying S-TAP agents, patches, and updates from a single console.

## Guardium
IBM security analytics solution that discovers, classifies, and protects structured and unstructured data.

## HIDDEN
Classification flag for data that should not appear in reports (e.g., encrypted values).

## Hive
Apache Hive data warehouse; Guardium monitors HiveQL queries with S-TAP or S-GATE.

## Hot(job)
Active monitoring job.

## LDAP
Directory service protocol for integrating with external identity providers for authentication/authorization.

## MODE
Policy configuration setting (Monitor, Block, Terminate) determining enforcement behavior.

## NVARCHAR
Variable-length Unicode character data type supported for monitoring string values.

## ON-THE-FLY
Real-time processing of database activity without pre‑scheduled jobs.

## READ ONLY
Access mode allowing data access but blocking modifications, deletions, or write operations.

## S-GATE
Enforces real‑time database access policies and blocks or masks unauthorized queries.

## S-TAP
Software agent on database servers capturing and forwarding traffic to a Collector.

## SELF-DEFINED
User‑created rules, groups, or policies not based on default templates.

## SESSION
Contextual boundary for a logical unit of work defined by login and logout events.

## TRANSFORM
Modifies or restructures captured data for reporting or compliance purposes.

## violation
Database incident breaching policies, rules, or compliance standards; tracked and reported by Guardium.

## Terms

**HTML** – Markup language for web reports that Guardium can export.

**ICU** – International Components for Unicode library supporting multilingual reporting.

**Import** – Ingest external data (policy sets, assessment definitions) into Guardium.

**Incident** – Notable event flagged by Guardium that requires investigation.

**IP** – Network address; Guardium logs client and server IPs.

**Job** – Scheduled task such as daily assessments or nightly archiving.

**JSON** – Data interchange format used by Guardium APIs.

**Key** – Credential for encryption, authentication, or signing within Guardium.

**License type** – Edition of Guardium installed (Standard, Premium, Data Risk Analyst).

**Linux** – Operating system supported by native S‑TAP and K‑TAP.

**Login** – Authentication event captured by Guardium (source address, user ID, timestamp).

**Macro** – Pre‑defined set of policy rules for rapid deployment.

**Masking** – Dynamic hiding of sensitive data based on policy rules.

**NETEZZA** – IBM analytic database platform; Guardium monitors admin privileges and SQL traffic.

**Netflow** – Network metadata protocol; Guardium correlates Netflow with database activity.

**NON‑ROOT** – Guardium installation mode without privileged OS credentials.

**Normal** – Default classification for routine authorized activity.

**Object** – Database artifact (table, view, procedure) monitored by Guardium.

**ODBC** – Open Database Connectivity driver; Guardium captures ODBC traffic.

**One‑Time Password** – Secure login method; Guardium integrates with MFA for OTP events.

**ORA** – Oracle database; Guardium extensively monitors Oracle.

**Origin** – Source of database activity (application name, program source) recorded in logs.

**Overhead** – Performance impact of Guardium monitoring (CPU or I/O load).

**Owner** – Database user who owns an object; included in Guardium reports.

**PATCH** – Software update package for Guardium components (S‑TAP, Collector, Aggregator).

**PDF** – Document format; Guardium can export reports, assessment results, or audit logs.

**PLACEHOLDER** – Temporary variable in Guardium query templates supplied at runtime.

**Policy** – Set of Guardium rules defining normal, risky, or prohibited activity.

**PostgreSQL** – Open‑source relational database; monitored with S‑TAP on Linux and K‑TAP elsewhere.

**Privilege** – Database authorization monitored and audited by Guardium.

**Provider** – External system supplying identity data (LDAP, Active Directory) for user provisioning.

**QUERIES** – Feature storing recent SQL statements for forensic analysis.

**Query** – Individual SQL statement executed against a database; logged by Guardium.

**Retain** – Guardium configuration specifying how long audit data is kept.

**Revoke** – Statement removing privileges; recorded by Guardium for compliance.

**Rule** – Individual condition within a Guardium policy dictating allow, block, or alert actions.

**SAP** – Enterprise ERP software; Guardium monitors SAP transactions (ABAP, JDBC).

**SCAN** – Automated vulnerability assessment by Guardium’s Database Vulnerability Assessment engine.

**Schema** – Logical container for database objects; Guardium assesses schema changes over time.

**Sensitizer** – Persona defining data classification labels and sensitivity levels.

**Service** – Guardium endpoint representing a monitored database instance used in policy targeting.

**Shadow User** – Account masquerading as another user; Guardium detects anomalous behavior.

**Signature** – Pre‑defined pattern of activity indicating a known attack or violation.

**SQL** – Standard language for relational database access; all monitored activity is represented in SQL.

**Standard** – Pre‑packaged Guardium policy collection (e.g., PCI‑DSS, GDPR) for quick compliance setup.

**System** – Generic term for the overall Guardium deployment (appliances, agents, integrated components).

**Table** – Structured collection of rows and columns; primary object type for access monitoring.

**Task** – Guardium work item such as assessment creation, report generation, or configuration change.

**TEMP** – Temporary storage location used by Guardium during intermediate report processing.

## Test
Individual verification step within a Guardium security assessment evaluating a specific control or vulnerability.

## Token
Short‑lived credential issued for API authentication; Guardium APIs can require a bearer token in requests.

## User
Database user; Guardium personnel include Admin, Assessor, Sensitizer, and Auditor roles for system operation.

## Vulnerability
Weakness in database configuration, patch level, or permission model identified by Guardium scans.

## Windows
Microsoft OS; Guardium supports S‑TAP agents on Windows servers for SQL Server and other database instances.

## A‑TAP
IBM Guardium kernel‑level agent that intercepts database calls made by local applications directly on the database server.

## Aggregator
Guardium appliance that consolidates activity data from multiple Collectors for enterprise‑wide reporting.

## ASLHEAPSZ
DB2 configuration parameter multiplied by 4096 to determine the Guardium default packet buffer size.

## CAS
Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

## Collector
Guardium appliance that receives, processes, and stores database activity data forwarded by S‑TAP agents.

## DB2_ASLHEAPSZ
Calculated value used by Guardium for packet buffering, derived by multiplying the DB2 ASLHEAPSZ setting by 4096.

## FAM
Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

## GDPR
EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

## GIM
Centralized tool for remotely deploying, upgrading, and managing S‑TAP agents across database servers.

## K‑TAP
Linux kernel module loaded on the database server that intercepts OS‑level database socket traffic for Guardium monitoring.

## S‑GATE
Guardium component that enforces real‑time database access policies and blocks or masks unauthorized queries.

## S‑TAP
IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Auditing_native_Cassandra
Enables native audit logging for Cassandra/DataStax within Guardium, creating an appender pipe for audit data configurable via GIM.

## AES
Symmetric encryption algorithm used for securing data in Guardium reports and logs.

## ALERT
Mechanism in Guardium that notifies administrators of security violations and policy breaches in real time.

## AmazonS3
Cloud storage service supported by Guardium for archiving and exporting audit data.

## APPLIANCE
Physical or virtual device that runs the Guardium software for data protection and compliance monitoring.

## ARC
API endpoint used to retrieve and manage Guardium backups, including archiving and restoring configurations.

## API_KEY
Authentication token required to access Guardium RESTful services, generated via the Guardium portal.

## ASN1
Data encoding format used in Guardium for structured data representation, especially in policy definitions and reports.

## AUC
Monitoring metric in Guardium representing the number of active database user sessions at any given time.

## AIA
Internal auditors granted permission to access Guardium audit reports and compliance features.

## ACTIVE_USER_COUNT
Monitoring metric in Guardium representing the number of active database user sessions at any given time.

## A-AES
Symmetric encryption algorithm used for securing data in Guardium reports and logs.

## Additional Columns
Audit Process Builder feature listing Events and Additional Columns on the Edit task window for specific task types.

## Audit Process Builder
Step‑by‑step configuration of an audit task, showing its structured nature.

## Oracle Example
`2181`  |  **Description:** Sorting query results enables ascending or descending order for reporting.  

## Session Attributes
`2182`  |  **Description:** Session Start, End, and Timestamp distinguish session phases.  

## CPU View
`2183`  |  **Description:** Navigate the DB Entitlements tab for entitlement reports.  

## grdapi create_user_hierarchy
`2184`  |  **Description:** Sort statements by DB2 z type (static vs. dynamic).  

## Security Assessment
`2185`  |  **Description:** Run a script, connect a datasource, and launch assessments.  

## VA Scanner
`2186`  |  **Description:** Standalone tool from Guardium v12.2 for vulnerability scans.  

## License Remaining
`2187`  |  **Description:** Command‑line parameter to show remaining licenses.  

## Runtime Parameter
`2188`  |  **Description:** NOW -48 Month identifies unpurged data days.  

## Custom Certificates
`2189`  |  **Description:** Check expiration and target system changes with keywords.  

## CLI Update
`2190`  |  **Description:** CLI commands refresh copy file data and ensure integrity.  

## Keyword Features
`2191`  |  **Description:** Licenses feature provides remaining license count.  

## Enterprise Reporting
`2192`  |  **Description:** CPU role in aggregate reporting across Collectors.  

## Workflow Knowledge
`2193`  |  **Description:** Entities and workflows tied to hierarchical user management.  

## Hierarchical Keywords
`2194`  |  **Description:** Keywords enrich entities in user‑group hierarchies.  

## Additional Details
`2195`  |  **Description:** Continuation of hierarchical license information.

## Licenses
Indicates remaining license count.

## Skips registry certificate installation on cluster nodes
Variants of a feature that skips adding registry certificates to cluster nodes.

## Evaluation Class
Policy component that evaluates data values and applies conditional logic.

## A-TAP
Kernel-level agent that intercepts database calls from local applications on the server.

## Aggregator
Appliance that aggregates activity data from multiple Collectors for enterprise reporting.

## CAS
Module that detects and records changes to database schemas, stored procedures, and configurations.

## Collector
Appliance that receives, processes, and stores database activity from S-TAP agents.

## File Activity Monitoring (FAM)
Module that monitors access to unstructured data files on NAS, SharePoint, etc.

## GDPR
EU data protection regulation supported by Guardium through discovery, masking, and audit trails.

## GIM
Centralized tool for deploying and managing S-TAP agents across database servers.

## K-TAP
Linux kernel module that intercepts OS-level database socket traffic.

## S-GATE
Component that enforces real-time access policies and blocks or masks unauthorized queries.

## S-TAP
Software agent that captures and forwards database traffic to a Collector.

## WORM
Storage mode preventing alteration or deletion of audit data for compliance.

## Database Monitoring and Protection
- **auto_schema**: Automatically detect and classify new schema changes.
- **auto_violation_effective_date**: Set future activation date for policy violations.
- **binary_policy**: Enforce binary-level access controls on database objects.
- **blocklist**: Restrict IP addresses, users, or commands.
- **byte_manipulation**: Mask sensitive data at the byte level during transmission.
- **cassandra**: Monitor Cassandra NoSQL databases.
- **capture_live_traffic**: Capture real-time database traffic for immediate analysis.
- **catalog**: Manage protected data assets and access policies.
- **column_encryption**: Protect sensitive data within database columns.
- **custom_rule_group**: Manage complex compliance requirements with user-defined rule groups.
- **data_discovery**: Scan databases and file systems for sensitive data.
- **data_quality**: Ensure accuracy and consistency of monitored data.
- **delta_data**: Track incremental changes in database records.
- **dependency_analysis**: Identify dependencies between database objects and applications.
- **dml_exclusion_list**: Exclude specific DML operations from monitoring.
- **duplicate_detection**: Identify duplicate records across multiple sources.
- **force_transfer**: Force immediate transfer of accumulated activity data.
- **full_sql**: Log complete SQL query details for comprehensive audit trails.
- **g2n_mapping**: Associate internal identifiers with human-readable names.
- **gdm**: Focus on data lifecycle and governance.
- **global_role**: Apply permissions across all managed systems.
- **group_builder**: Construct and manage groups of database objects, users, or activities.
- **guardium_insider_risk**: Detect insider threats by correlating user behavior.
- **hashi**: Integrate with HashiCorp Vault for secure credential management.
- **high_availability**: Ensure continuous monitoring without single points of failure.
- **host_alias**: Map hostnames to IP addresses for easier management.
- **http_header**: Inspect and log HTTP headers.

## Advanced Analysis and Reporting
- **auto_scheduling**: Automatically schedule data collection tasks.
- **baz**: Placeholder for custom user-defined keywords.
- **binlog**: Monitor MySQL binary logs for data integrity and auditing.
- **cim**: Aggregate activity data from various sources for unified analysis.
- **coa**: Provide insights for optimizing database security settings.
- **csp**: Summarize compliance status across monitored databases.
- **deep_inspection**: Perform detailed security assessments at the packet level.
- **email_template**: Notify administrators about policy violations or system events.
- **event_trigger**: Initiate specific actions based on real-time event detection.
- **exception_policy**: Define exceptions to standard security rules.
- **fuzzy_matching**: Identify variations of sensitive data through approximate matching.
- **graph_analytics**: Visualize and analyze complex data relationships using graph theory.
- **real-time_analysis**: Detect and respond to anomalies immediately.
- **report_template**: Generate standardized reports on security and compliance.

## Data Protection and Governance
- **auto_schema**: Automatically detect and classify new schema changes.
- **binary_policy**: Enforce binary-level access controls on database objects.
- **blocklist**: Restrict IP addresses, users, or commands.
- **byte_manipulation**: Mask sensitive data at the byte level during transmission.
- **column_encryption**: Protect sensitive data within database columns.
- **data_discovery**: Scan databases and file systems for sensitive data.
- **data_quality**: Ensure accuracy and consistency of monitored data.
- **delta_data**: Track incremental changes in database records.
- **dependency_analysis**: Identify dependencies between database objects and applications.
- **dml_exclusion_list**: Exclude specific DML operations from monitoring.
- **duplicate_detection**: Identify duplicate records across multiple sources.
- **force_transfer**: Force immediate transfer of accumulated activity data.
- **full_sql**: Log complete SQL query details for comprehensive audit trails.
- **g2n_mapping**: Associate internal identifiers with human-readable names.
- **gdm**: Focus on data lifecycle and governance.
- **global_role**: Apply permissions across all managed systems.
- **group_builder**: Construct and manage groups of database objects, users, or activities.
- **guardium_insider_risk**: Detect insider threats by correlating user behavior.
- **hashi**: Integrate with HashiCorp Vault for secure credential management.
- **high_availability**: Ensure continuous monitoring without single points of failure.
- **host_alias**: Map hostnames to IP addresses for easier management.
- **http_header**: Inspect and log HTTP headers.

## Workflow and Task Management
- **auto_schema**: Automatically detect and classify new schema changes.
- **auto_scheduling**: Automatically schedule data collection tasks.
- **auto_violation_effective_date**: Set future activation date for policy violations.
- **auto_violation_effective_date**: Set future activation date for policy violations.
- **binary_policy**: Enforce binary-level access controls on database objects.
- **blocklist**: Restrict IP addresses, users, or commands.
- **byte_manipulation**: Mask sensitive data at the byte level during transmission.
- **cassandra**: Monitor Cassandra NoSQL databases.
- **capture_live_traffic**: Capture real-time database traffic for immediate analysis.
- **catalog**: Manage protected data assets and access policies.
- **column_encryption**: Protect sensitive data within database columns.
- **custom_rule_group**: Manage complex compliance requirements with user-defined rule groups.
- **data_discovery**: Scan databases and file systems for sensitive data.
- **data_quality**: Ensure accuracy and consistency of monitored data.
- **delta_data**: Track incremental changes in database records.
- **dependency_analysis**: Identify dependencies between database objects and applications.
- **dml_exclusion_list**: Exclude specific DML operations from monitoring.
- **duplicate_detection**: Identify duplicate records across multiple sources.
- **email_template**: Notify administrators about policy violations or system events.
- **event_trigger**: Initiate specific actions based on real-time event detection.
- **exception_policy**: Define exceptions to standard security rules.
- **failed_login_attempts**: Detect suspicious login attempts based on thresholds.
- **file_association**: Map file types to specific protection policies.
- **file_discovery**: Locate and identify files containing sensitive data.
- **firewall_mode**: Block unauthorized database access attempts in real-time.
- **force_transfer**: Force immediate transfer of accumulated activity data.
- **format_conversion**: Convert activity data into different formats for compatibility.
- **frictionless_authentication**: Seamlessly authenticate users while maintaining security.
- **full_sql**: Log complete SQL query details for comprehensive audit trails.
- **fuzzy_matching**: Identify variations of sensitive data through approximate matching.
- **g2n_mapping**: Associate internal identifiers with human-readable names.
- **gdm**: Focus on data lifecycle and governance.
- **global_role**: Apply permissions across all managed systems.
- **group_builder**: Construct and manage groups of database objects, users, or activities.
- **guardium_insider_risk**: Detect insider threats by correlating user behavior.
- **hashi**: Integrate with HashiCorp Vault for secure credential management.
- **high_availability**: Ensure continuous monitoring without single points of failure.
- **host_alias**: Map hostnames to IP addresses for easier management.
- **http_header**: Inspect and log HTTP headers.

## Guardium Components and Modules

### Monitoring and Data Capture
- **A-TAP (Application TAP)**: Kernel-level agent intercepting local application database calls.
- **Collector**: Receives, processes, and stores activity data from S-TAP agents.
- **Aggregator**: Consolidates data from multiple Collectors for enterprise reporting.

### Data Governance and Compliance
- **CAS (Change Audit System)**: Tracks schema, stored procedure, and object configuration changes.
- **FAM (File Activity Monitoring)**: Monitors unstructured data file access on NAS and SharePoint.
- **Vulnerability Assessment**: Scans for security weaknesses and configuration drift.
- **GDPR**: Supports compliance via discovery, masking, and audit trails.

### Deployment and Management
- **GIM (Guardium Installation Manager)**: Remotely deploys and upgrades S-TAP agents.
- **S-TAP (Guardium S-TAP)**: Captures and forwards database traffic to a Collector.
- **SVE (System Validation Engine)**: Validates Guardium component integrity and audit accuracy.
- **Stap Status API**: Checks agent health and version programmatically.

### Security Enforcement
- **Guardium S-GATE**: Real-time database firewall blocking malicious queries.
- **Oracle TNS Listener**: Monitors Oracle connection attempts.
- **SQL Redaction**: Masks sensitive data in query results.
- **Policy Builder**: Defines granular access rules for S-GATE enforcement.

## Guardium Core Concepts

### Key Guardium Products
- **Guardium**: Centralized platform for database security, monitoring, and compliance.
- **Access Token**: Short-lived credential for API authentication.
- **Collector**: Guards data ingestion and processing nodes.
- **S-TAP**: Kernel-level agent installed on database servers to capture traffic.

### Monitoring Modules
- **FAM**: Monitors unstructured file access on network storage.
- **K-TAP**: Linux kernel module for intercepting socket traffic.
- **A-TAP**: Agent for monitoring local application database calls.

### Policy and Enforcement
- **S-GATE**: Enforces access policies and blocks unauthorized queries.
- **Dynamic Policy**: Rule-based system for real-time monitoring actions.
- **Policy**: Configurable rules defining monitoring behaviors.

### Data Management
- **SQL Guard**: Enforces SQL-based access controls.
- **Change Audit System**: Tracks schema and object configuration changes.
- **Incomplete Transaction Logging**: Logs partial transactions for analysis.

### Security Features
- **Exclusion List**: Specifies objects or patterns to ignore in monitoring.
- **Extrusion Prevention**: Blocks unauthorized outbound data exports.
- **Redaction Engine**: Masks sensitive data in logs based on policies.
- **RESTful**: Web service architecture for Guardium API communication.

### Threat Detection
- **Active Threat Analytics**: Analyzes user behavior to categorize threats by severity.
- **Behavioral Analytics Window**: UI tool for viewing risk indicator weights.
- **Collective Threat Analytics**: Aggregates threat intelligence across deployments.

### Compliance and Integration
- **GDPR**: Supports EU personal data protection compliance.
- **SQL Injection**: Monitors for database attack attempts.
- **STIX**: Structured language for representing threat intelligence.
- **VPN**: Provides encrypted data exchange across networks.

### Management Tools
- **GIM**: Centralized management of S-TAP agents across environments.
- **Vulnerability Assessment**: Systematic identification and quantification of vulnerabilities.

### Data Discovery and Analysis
- **Discovery Scan**: Automated assessment of data sources for sensitive data.
- **Data Access Pattern Analysis**: Identifies anomalies in access sequences.
- **Discovery Scan**: Identifies and classifies sensitive data across sources.
- **Enrichment Process**: Enhances logs with contextual user information.

### Risk Management
- **Risk Indicator Weight**: Scores importance of risk factors in analytics.
- **Supersedence Policy**: Defines policy configuration precedence.

CAS(C-TOOL): Record changes to Guardium settings.  
Client IP: Source IP of database request.  
CPU: Central Processing Unit usage metric.  
grdapi(commodity API): CLI for Guardium management.  
Kerberos: Authentication protocol supported by Guardium.  
RegEx(Regular Expression): Pattern matching for policies.  
SGATE: Enforces real-time access policies.

A-TAP: Kernel agent intercepting local DB calls.  
Aggregator: Consolidates Collector data for reporting.  
CAS(Change Audit System): Detects schema and object changes.  
Collector: Receives and stores database activity data.  
FAM(File Activity Monitoring): Monitors unstructured data access.  
GDPR: EU data protection regulation.  
GIM(Guardium Installation Manager): Deploys and manages S-TAP agents.  
K-TAP(Kernel TAP): Kernel module intercepting OS socket traffic.  
S-GATE(Software Gate): Enforces access policies in real time.  
S-TAP(Software TAP): Agent capturing and forwarding traffic.

## Guardium Data Format

**Adobe Structured Markup** – Data format used by Guardium to describe system objects and their relationships in policy definitions.

## Data Assessment & Monitoring

**audit(audit)** – Process of reviewing and analyzing system logs and database activity to ensure compliance with security policies.  

**CAS(Cloud Access Security)** – Integration with cloud services to monitor and secure access to cloud data.  

**cloud(cloud data source)** – Remote data source hosted on cloud platforms (AWS, Azure, Google Cloud).  

**Data-Masking(Data Masking)** – Obfuscates sensitive data in query results or reports.  

**DDE(Database Data Encryption)** – Monitors and enforces database encryption at rest and in transit.  

**Encryption(Encryption)** – Converts plaintext to ciphertext to protect data from unauthorized access.  

**Encryption(Encryption)** – Converts plaintext data into ciphertext to protect it from unauthorized access.  

## File & Transfer

**file-file transfer(File Transfer)** – Moves Guardium data files to/from external systems or storage.  

**FPE(File-based Policy Enforcement)** – Enforces policies on unstructured data in NAS or SharePoint.  

**Grant(Grant)** – Permission to perform actions on database objects.  

**password(pw_encrypt)** – Encrypts passwords in Guardium configurations.  

**ReadReplica(Read Replica)** – Synchronized copy of a database for load distribution.  

**STS(STS)** – Guardium version with limited extended maintenance.

## Connectivity & Authentication

**JDBC(Java Database Connectivity)** – Java API for database connectivity.  

**Kerberos(Kerberos)** – Network authentication protocol supported by Guardium.  

**OpenJDK(OpenJDK)** – Open-source Java Development Kit supported by Guardium.  

**RSA(RSA SecurID)** – Multi-factor authentication using one-time passwords.  

**Windows(Windows)** – Supported OS for deploying S-TAP agents on database servers.  

## Architecture & Deployment

**ACMS(Central Manager)** – Coordinates Collector and Enforcer activities in enterprise deployments.  

**ACA(Advanced Correlation Alert)** – Generates alerts by correlating events across multiple sources.  

**ACS(Access Control System)** – Defines and enforces database and file system access policies.  

**AG(Administrative Groups)** – Logical grouping of Guardium appliances for management and policy assignment.  

**AIP(Application Interface Program)** – Not defined in this set; skip.  

**ELB(Elastic Load Balancer)** – Distributes application traffic across multiple targets (AWS).  

**IX(JDBC)** – See **JDBC(Java Database Connectivity)**.  

## Storage & Retention

**PERM(Permanent Storage)** – Non-volatile storage for audit data and configuration settings.  

## Database Support

**Informix(Informix)** – IBM database supported by Guardium for activity monitoring.  

**MySQL(MySQL)** – Open-source RDBMS supported by Guardium.  

**hx(HXDB)** – IBM Guardium Hadoop Database – supported Hadoop cluster.  

## Integration & Management

**IAM(IAM)** – Identity and access management for Guardium services.  

**IAM(IAM)** – Identity and access management for Guardium services.  

**LTS(Long-term Support)** – Guardium versions with extended security updates.  

## Application & Web Integration

**Rails(Rails)** – Monitors database activity from Ruby on Rails applications.  

**WebLogic(WebLogic)** – Java EE application server supported by Guardium.  

## Networking & Protocols

**NFS(Network File System)** – File access protocol monitored by Guardium's FAM module.  

**SFTP(SFTP)** – Secure file transfer protocol supported by Guardium.  

**TCP/TCP Traffic(TCP Traffic)** – Monitored by S-TAP agents to capture database interactions.  

**TLS(TLS)** – Secure data transmission protocol supported by Guardium.  

## Security & Identity

**Schema(Schema)** – Logical database structure tracked by Guardium's CAS module.  

**SSO(Single Sign-On)** – Not explicitly listed; use **SAM(SAM)**.  

**SAM(SAM)** – Security Assertion Markup Language for SSO and authentication.  

**User(User)** – Managed through Guardium's access controls.  

## Development & Extensibility

**SDK(SDK)** – Software development kit for custom Guardium integration and automation.

## Guardium Key Concepts

**um**: Proprietary interface for automating configuration and reporting via scripts or external tools.

**B-AUDIT**: Stores immutable audit records in write-once storage for forensic and compliance analysis.

**CAS**: Former IBM data security portfolio, now part of Guardium's advanced data protection features; also monitors and reports database schema, configuration, and object changes.

**CEP**: Real-time analysis of data streams to detect patterns; used by Guardium for policy and alert management.

**CISO**: Executive role responsible for enterprise-wide information security; Guardium reports help fulfill CISO requirements.

**DLP**: Detects and prevents unauthorized data transfers from databases and file servers.

**DRDR**: Features for failover, redundancy, and synchronized backups across data centers.

**DWH**: Large-scale data repository for analytics; Guardium integrates to protect and monitor warehouse activities and access.

**EOM**: Period after which Guardium product receives no technical support or software updates; critical for compliance planning.

**EP**: User-defined classification of database objects, files, or user accounts for consistent security policies.

**ETL**: Data warehousing process; Guardium monitors ETL jobs for compliance and data integrity.

**FFDC**: Automatic collection of diagnostic information upon Guardium service failures, aiding root cause analysis.

**FIM**: Detects unauthorized modifications to critical files and system binaries.

**GRD**: Standalone executable for deploying or upgrading Guardium components on database servers.

**HSB**: Redundant Guardium appliance configured to take over instantly if the primary unit fails, ensuring continuous security.

**i2**: AI/ML engine that analyzes behavior patterns to proactively detect vulnerabilities and threats.

**IDF**: Alerts generated when audited data does not conform to expected structures, flagging potential tampering.

**ING**: Configuration that defines a set of database servers sharing common policies and patch levels.

**JSON**: Lightweight data-interchange format used in Guardium APIs and web service interactions.

**KTT**: Support unit focused on knowledge preservation, remote troubleshooting, and proof points.

**lshstat**: Command-line utility in Guardium to display real-time health metrics of monitored database instances.

**LRR**: Stores real-time monitoring data for immediate access and analysis.

**MGS**: Top-level Central Manager in multi-tier Guardium deployments managing subordinate AGs and Collectors.

**MIB**: Guardium-specific MIB files for SNMP integration, enabling network monitoring tools to collect security metrics.

**ML**: AI techniques for predictive threat detection, risk scoring, and automated policy refinement.

**nfdump**: Log format produced by Guardium's network sniffing for capturing and analyzing packet data.

**ODBC**: Standard SQL API supported by Guardium for database client monitoring and policy application.

**OM**: Dashboard and reporting tools designed for day-to-day security operations and incident response.

**OP**: Rules that define real-time blocking or alerting actions based on detected security violations.

**OOB**: Approach to database monitoring by intercepting traffic outside the normal application path, reducing performance impact.

**QF**: Temporarily stores events during network disruptions, ensuring no data loss.

**RDS**: Techniques for downsampling or summarizing audit data to improve storage efficiency without losing insights.

**RG**: Groups database users by job function, simplifying privilege auditing and policy assignment.

**S3**: AWS storage service; Guardium can export audit logs to S3 buckets for long-term retention and analysis.

**SDK**: Collection of Guardium APIs, sample scripts, and development tools for custom integration projects.

**SH**: Data sanitization feature that irreversibly removes sensitive files while maintaining audit records.

**SIEM**: Enterprise security monitoring platforms; Guardium augments SIEMs with database-specific intelligence.

**SL**: Parameter in Guardium discovery profiles defining how long discovered database credentials remain valid.

**SMA**: Lightweight agent that reports server-level metrics like CPU, memory, and disk usage to AGs.

**SNARE**: Third-party tool that integrates with Guardium to forward system log events.

**SPL**: Declarative syntax for defining complex access control policies using logical operators.

**SQS**: AWS messaging service; Guardium producers/consumers can integrate for event-driven workflows and alerts.

**SSM**: Secures backup and archival storage devices by enforcing policy-based access.

**TAP**: Proprietary protocol for capturing and decoding database traffic without inlining.

**TERR**: (Incomplete entry, omitted)

## Guardium Reporting and Components Compressed

### Log Overview
Guardium's **compact log format** condenses alerts and incidents into concise lines for rapid response.

### Time Management
**TOD (Time of Day)** restricts policy actions to scheduled windows, enabling maintenance and blackout periods.

### Security Foundations
**TPM (Trusted Platform Module)** hardware securely handles key exchange and digital signing for Guardium operations.

### User Behavior Monitoring
**UAA (User Activity Analysis)** profiles user behavior and detects anomalies across systems.

### User Interface
**Web Interface** provides a web-based console for configuration, policy management, and monitoring.

### Integration and Automation
**Web Services** expose SOAP/REST APIs for integrating Guardium with external systems and automation workflows.

### Data Masking
**XDM (X-Force Data Masking)** dynamically masks sensitive data based on predefined rules.

### Application Monitoring
**A-TAP (Application TAP)** is a kernel-level agent that intercepts database calls from local applications on the server.

### Enterprise Consolidation
**Aggregator (Guardium Aggregator)** consolidates activity data from multiple Collectors for enterprise reporting.

### Schema Tracking
**CAS (Change Audit System)** detects and logs changes to database schemas, stored procedures, and configurations.

### Database Agents
**Collector (Guardium Collector)** receives, processes, and stores activity data from S-TAP agents.

### Database Support
**DB2** (IBM's relational database) is supported for monitoring and securing data access.

### Data Activity Control
**DAM (Data Activity Monitoring)** provides real-time visibility into database transactions for policy enforcement and auditing.

### File Access Monitoring
**FAM (File Activity Monitoring)** records access to unstructured data on NAS and SharePoint.

### Compliance
**GDPR (General Data Protection Regulation)** support includes discovery, masking, and audit trails.

### Deployment Management
**GIM (Guardium Installation Manager)** remotely deploys and manages S-TAP agents across servers.

### Protocol Monitoring
**HTTP** and **HTTPS** traffic can be monitored for database applications accessing data via web interfaces.

### Insider Threat Detection
**IR (Unauthorized Insider Risk)** identifies suspicious activities by privileged users.

### Kernel Monitoring
**K-TAP (Kernel TAP)** loads on Linux servers to intercept OS-level database socket traffic.

### Authentication Integration
**LDAP** integrates with Guardium for user authentication and authorization.

### Multi-Channel Support
**Mac (Multi-Access Channel)** monitors database access through various connection methods.

### Custom Policies
**MYP (My Policy)** defines user-created monitoring and response policies.

### Network Security
**Net (Network)** monitors data in transit across protocols and interfaces.

### Privileged User Management
**PIM (Privileged Identity Management)** monitors and controls privileged user access.

### Open-Source Support
**PostgreSQL** is supported for comprehensive security monitoring.

### In-Memory Data Monitoring
**Redis** in-memory data stores are monitored for access patterns.

### Web Service Monitoring
**REST** APIs are monitored to secure API-based database interactions.

### Operating System Support
**RHEL (Red Hat Enterprise Linux)** supports Guardium deployments.

### Software Agents
**S-TAP (Software TAP)** captures and forwards database traffic to Collectors.

### Application Support
**SAP** database activities are monitored.

### File Sharing Protocol
**SMB** file sharing protocol is monitored for database interactions.

### Query Monitoring
**SQL** queries are monitored to enforce security policies.

### Secure Communications
**TLS (Transport Layer Security)** encrypts communications between Guardium components.

### Traffic Interception
**TAP (Terminal Access Point)** is a generic term for traffic interception points.

### Data Modification
**Transform (TRANSFORM)** modifies data in transit, such as redacting fields for compliance.

### Virtualization Support
**VMware** environments are monitored to protect virtual database infrastructures.

### Web Application Security
**WAF (Web Application Firewall)** integrates with Guardium to protect database-driven web applications.

## Guardium Components Overview

### Key Modules and Features
- **A-TAP (Application TAP)**: Kernel-level agent intercepting
  local application calls on the database server, enabling direct
  monitoring of database activities without network traffic.
- **Aggregator**: Central Guardium appliance for consolidating
  activity data from multiple Collectors, facilitating enterprise-wide
  reporting.
- **CAS (Change Audit System)**: Detects and logs schema,
  stored procedure, and configuration changes, aiding compliance
  and change management.
- **Collector**: Receives, processes, and stores database activity
  data forwarded by S-TAP agents, centralizing raw data for analysis.
- **FAM (File Activity Monitoring)**: Monitors access to unstructured
  data files on NAS and SharePoint, extending Guardium's visibility
  to file systems.
- **GDPR Compliance**: Built-in features supporting discovery,
  data masking, and audit trails to aid in GDPR compliance.
- **GIM (Guardium Installation Manager)**: Manages remote deployment
  and updates of S-TAP agents across networked database servers.

### Key Concepts
- **K-TAP**: Linux kernel module for OS-level database socket
  traffic interception, enhancing monitoring efficiency and accuracy.
- **S-GATE**: Enforces and enforces real-time database access
  policies, capable of query blocking, and data masking.
- **S-TAP**: Database server agent capturing and forwarding traffic
  to a Guardium collector, central to traffic monitoring and policy
  enforcement.

These components and concepts work in concert to provide
comprehensive database and file activity monitoring, aiding
in security, compliance, and operational efficiency.

## Remotely Deploying, Upgrading, and Managing S-TAP Agents

### Guardium Installation Manager
Centralized tool for **remotely deploying, upgrading, and managing S-TAP agents** across database servers.

## K-TAP (Kernel TAP)
**Linux kernel module** that intercepts OS-level database socket traffic for Guardium monitoring.

## S-GATE (Software Gate)
Guardium component that **enforces real-time database access policies** and blocks or masks unauthorized queries.

## S-TAP (Software TAP)
**IBM Guardium software agent** installed on database servers that captures and forwards database traffic to a Guardium Collector.

## A-TAP (Application TAP)
**IBM Guardium kernel-level agent** that intercepts database calls made by **local applications directly on the database server.**

## Access Policies (Guardium Access Policies)
Rules that define what actions are permitted or denied for specific users, groups, or roles when accessing database objects or performing operations.

## Aggregator (Guardium Aggregator)
Guardium appliance that consolidates activity data from **multiple Collectors** for enterprise-wide reporting.

## APACHE-ACCESS (javax.servlet.http.HttpServletRequest)
Interface that provides methods to retrieve information from **HTTP request headers**, used for detecting SQL injection in Apache-based web applications.

## Audit Settings (Guardium Audit Settings)
Configuration parameters that control what database activity is logged, how it is stored, and how long logs are retained.

## Audit Activity Reports (Guardium Audit Activity Reports)
Predefined or custom reports that summarize database access events, user activity, and **policy violations** over a specific time period.

## Backup Policies (Guardium Backup Policies)
Rules that determine how often Guardium data is backed up, where backups are stored, and how long backups are retained for disaster recovery.

## C-CRYPT (Java Cryptography Extension)
A set of APIs and tools for encryption, decryption, and secure key management used in securing **sensitive data** handled by Guardium.

## CAS (Change Audit System)
Guardium module that detects and records changes to **database schemas, stored procedures, and object configurations.**

## CCPA (California Consumer Privacy Act)
California state law regulating the collection, use, and disclosure of personal information; Guardium helps organizations achieve compliance through monitoring and masking capabilities.

## Central Manager (Guardium Central Manager)
A server that coordinates and distributes policies, configurations, and updates to multiple Guardium appliances in a distributed environment.

## CIS Benchmarks (Database CIS Benchmarks)
Security configuration standards for various database platforms (e.g., Oracle, SQL Server); Guardium assesses compliance against these benchmarks.

## Compliance Policies (Guardium Compliance Policies)
Predefined rules and checks that help organizations meet regulatory requirements (e.g., PCI DSS, HIPAA) by identifying risky database behaviors.

## DB Audit Owner (Guardium DB Audit Owner)
Product‑specific keyword referring to a user or application responsible for managing database‑level auditing configurations.

## DB Server (Specific Database Server)
A named database server being monitored by Guardium, such as **PROD_DB1, DEV_DB2**, etc.

## DLP (Data Loss Prevention)
Technology that prevents sensitive data from unauthorized transfers; Guardium includes DLP features for file activity monitoring.

## Encrypted Traffic Decryption (Encrypted Traffic Decryption)
Guardium's capability to decrypt and inspect **encrypted database traffic** for policy enforcement and threat detection.

## Event Correlation (Guardium Event Correlation)
Process of analyzing and linking multiple security events to identify patterns indicative of attacks or policy violations.

## File Analysis (File Analysis)
Component that examines file attributes, permissions, and content to identify **sensitive or regulated data** stored on monitored file systems.

## File System Monitor (Guardium File System Monitor)
Guardium module that tracks access to files and directories, detecting potential data leakage or misuse.

## File Types Detected (File Types Detected)
List of file extensions or MIME types identified by Guardium as containing **sensitive data** (e.g., .csv, .xls, .pdf).

## GDPR (General Data Protection Regulation)
EU regulation requiring protection of personal data; Guardium supports compliance via **discovery, masking, and audit trails.**

## GIM (Guardium Installation Manager)
Centralized tool for **remotely deploying, upgrading, and managing S-TAP agents** across database servers.

## Group Details (Group Details)
Specific information about a Guardium group, including **member entities, owner, and associated policies.**

## Group Users (Group Users)
List of users or roles assigned to a particular group in Guardium for **collective policy application.**

## Public Key Infrastructure (PKI)
Framework for managing digital certificates and public-key encryption used by Guardium for secure communication.

## Remote S-TAP (Remote S-TAP)
**Software TAP agent** installed on a remote database server that communicates with a Guardium Collector over a network.

## REST API (Guardium REST API)
Programmatic interface for automating Guardium tasks, retrieving reports, and managing policies using HTTP requests.

## Rule Builder (Guardium Rule Builder)
GUI tool for creating and modifying policies **without SQL or specialized programming knowledge.**

## Security Roles (Guardium Security Roles)
Predefined roles (e.g., auditor, administrator) that determine user permissions for accessing Guardium features.

## Sensitive Objects (Sensitive Objects)
Database tables, columns, or stored procedures containing high-risk data (e.g., PII, financial transactions) targeted by Guardium's monitoring policies.

## Tokenization (Tokenization)
Technique used by Guardium to transform **sensitive data** into non-sensitive tokens while preserving data format for safe storage or transmission.

## TLS/SSL (TLS/SSL)
Protocols for establishing encrypted links between clients and servers; Guardium enforces these protocols for database connections.

## User Behavior Analytics (User Behavior Analytics)
Guardium module that analyzes user activity patterns to detect anomalies and potential insider threats.

## Access Management
Guardium user role authorized to manage user accounts and role assignments.

## API Key
Unique identifier for authenticating to Guardium's REST API.

## Archive Operator
Guardium role responsible for configuring and executing data archiving.

## Audit Process
Scheduled task that collects, processes, and stores database activity data.

## Clients
Database servers configured to communicate with a Guardium Collector.

## Command Line Interface (CLI)
Text-based interface for executing commands and automating tasks.

## Connector
Database-specific agent facilitating communication between Collector and traffic.

## Data Encryption Key (KEK)
Key used to encrypt sensitive data during transmission and storage.

## Encrypted File Encapsulation
Process of encrypting archived files to protect data during storage/transfer.

## Encryption Service
Component managing encryption keys and facilitating secure data encryption.

## File Mask
Function that obfuscates or alters specific data values in database logs.

## GUI
Web-based graphical interface for configuration and monitoring.

## Key Management (keyctl)
Guardium module providing tools for managing encryption keys and certificates.

## Protocols and Security Features

### Licensing and Deployment
- **License Server**: Centralized system managing and validating Guardium software licenses.
- **Aggregator**: Consolidates activity data from multiple collectors for enterprise-wide reporting.

### Monitoring and Data Collection
- **A-TAP**: Kernel-level agent intercepting local database calls.
- **Collector**: Receives, processes, and stores database activity data from S-TAP agents.
- **FAM**: Monitors direct file access on NAS and similar storage systems.
- **FILE-ACTIVITY-TRACKING**: Records file access using NTFS auditing on Windows.

### Compliance and Auditing
- **Cas**: Detects and records changes to database schemas and configurations.
- **Protocol-Negotiation**: Automatically determines database protocol type.
- **S-TAP-Proxy**: Intermediate agent enabling load balancing and geo-distributed monitoring.
- **S-TPS-DB2**: Tool for deploying and managing DB2-specific S-TAP installations.
- **S-Cloud-Collector**: Specialized for collecting data from cloud-based database services.

### Security and Enforcement
- **Network Access Control ACLs**: Regulates network traffic and access permissions.
- **Object Privilege**: Controls user actions on specific database objects.
- **Policy Distortion**: Modifies existing security policies to meet compliance needs.
- **Revoke Role**: Removes roles or privileges from users to enforce policies.
- **Secure Execution**: Restricts unauthorized command execution on database servers.
- **Shared Secret**: Encrypts file names and protects data integrity.

### Specialized Components
- **GDPR**: Supports EU data protection regulations through discovery, masking, and compliance audits.
- **GIM**: Central tool for managing S-TAP agents remotely.
- **Guardium-Internal**: Accessible only from within the Guardium appliance.
- **IRIX-ATAP**: Variant of A-TAP for IRIX systems.
- **KERNEL-TAP**: Linux kernel module enabling S-TAP monitoring.
- **Linux-Unmanaged**: S-TAP operation mode without central management.
- **PCI-DSS**: Helps meet payment card data security standards.
- **SaaS-External-STAP**: Monitors databases in Software-as-a-Service environments.
- **Session-Tracking**: Tracks user sessions, including login/logout events.
- **Solaris-SR**: Specific considerations for Solaris operating system versions.
- **TLS Protocol**: Encrypts data in transit between database servers and Guardium components.
- **User Hierarchy**: Organizes users and roles hierarchically for permission management.

### User and Role Management
- **Real-Time Alerts**: Immediate notifications of security rule violations.
- **Revoke Role**: Removes predefined roles or privileges from users or groups.
- **Schema Change ChangeAudit**: Tracks database schema modifications for compliance.
- **Stored Procedure**: Monitors precompiled database commands for auditing.
- **SQL Guard SQLGuard**: Legacy component for database monitoring and policy enforcement.
- **Unified-User-Alias**: Normalizes user identities across different databases and platforms.
- **VMware-vMotion**: Guidelines for deploying S-TAP on VMs using vMotion technology.

A-TAP(Application TAP): IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.  
Aggregator: Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.  
CAS(Change Audit System): Detects and records changes to database schemas, stored procedures, and object configurations.  
Collector: Receives, processes, and stores database activity data forwarded by S-TAP agents.  
Configuration Pipeline: Validates, transforms, and applies S-TAP configuration settings on database servers.  
Database Protocol: Network protocol Guardium monitors (e.g., Oracle TNS, MS SQL TDS, MySQL).  
FAM(File Activity Monitoring): Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; supported via discovery, masking, and audit trails.  
GIM(Guardium Installation Manager): Remotely deploys, upgrades, and manages S-TAP agents across database servers.  
IaaS: Aggregates and correlates activity from multiple monitored database connections into a unified session view.  
K-TAP(Kernel TAP): Linux kernel module that intercepts OS-level database socket traffic for Guardium monitoring.  
LAP(Log Analyzer Processor): De-duplicates, normalizes, and enriches raw log entries before persistence.  
Monitor(Inspection Engine): Parses, analyzes, and enforces policies on database traffic in real time.  
Network Interface: Physical or logical NIC on the Collector for traffic ingestion.  
PAT: NATs traffic to specific Inspection Engines.  
S-GATE: Enforces real-time database access policies and blocks or masks unauthorized queries.  
S-TAP(Software TAP): Captures and forwards database traffic to a Guardium Collector.  
SAQ(Sampled Access Query): Periodically samples SQL statements for deep analysis while reducing storage overhead.  
SGDB(Single-Group Data Builder): Aligns raw data into unified security event records.  
Task API: Creates, updates, and triggers Guardium scheduled tasks programmatically.  
TCPDT(TCP Directed Traffic): Redirects traffic from specific source IPs/ports to designated Inspection Engines.  
VERIFICATION Hash: Cryptographic hash to validate Integrity of Inspection Engine binaries.

## Configuration Backups and Forensic Dumps

## WebSphere Application Server
JDBC connections Guardium monitors; specific parameters may be required.

## XML Exporter
Service that serializes security alerts and anomalies into XML payloads.

## Access Control List
Ruleset defining database user/application access permissions.

## Teradata BTEQ
Batch query utility; Guardium FAM monitors executed SQL.

## SQL CASE Construct
Conditional logic within queries; monitored for sensitive data exposure.

## Custom Inspect Tool
User-defined inspection tool via Guardium API to extract hidden data.

## CSV File Format
Tabular data format; FAM records accesses to CSV files on file shares.

## DBCC Command
SQL Server integrity validation command; captured by Guardium.

## Delimited File
Files separated by specific delimiters; FAM tracks accesses.

## Inspection Engine Encapsulation
Process hiding sensitive columns during inspection.

## ETL Process
Data warehousing process; Guardium FAM records all phases involving protected data.

## Password Expiration Policy
Parameter controlling password change frequency; configurable via Guardium.

## Inspection Engine Filter
Clause restricting query/dataview results to specific criteria.

## Database Group
Collection of users, applications, or objects managed together.

## Hexadecimal Encoded Data
Guardium decodes hexadecimal data in activity logs.

## Conditional IF-ELSE Logic
Programming construct in stored procedures; Guardium records execution paths.

## Fixed Time Interval
Time unit for scheduling tasks within Guardium automation framework.

## SQL JOIN Operation
Combines data from multiple tables; Guardium audits queries involving joins.

## JSON Data Format
Lightweight data interchange format; FAM monitors JSON file and API accesses.

## Key Management System Integration
Supports integration with external services storing encryption keys.

## LIMIT Clause
Restricts number of rows returned by a query; Guardium logs statements containing LIMIT.

## Logon Event
Marks initiation of a database session; Guardium records logon events.

## Lookup Table Access
Monitors accesses to static reference datasets.

## Masking Policy Definition
Obfuscates sensitive data in audit logs or reports per column/table.

## Pattern Matching Technique
Identifies data fitting specific patterns; used in data discovery.

## Pattern Matching Search Criterion
Finds data subsets based on defined patterns (regular expressions).

## Quoted Text Field
Text fields enclosed in quotation marks; Guardium distinguishes quoted data.

## Range Boundary Specification
Specifies minimum and maximum values for numeric columns.

## Permission Revocation
SQL statement revoking privileges; audited by Guardium.

## CRONTAB Schedule
Time-based job scheduler used by Guardium for automating tasks.

## Query Selectivity Analysis
Attribute of query predicates indicating result set narrowing; analyzed by Guardium.

## Database Session Context
Scope of user interactions with a database; Guardium correlates activities.

## Data Shape Analysis
Statistic describing data column distribution; used for data classification.

## SQL Auditing
Logs, analyzes, and enforces policies on SQL activity.

## SSL/TLS Protocols
Cryptographic protocols ensuring secure communications; recorded by Guardium.

## Subset Data Partition
Portion of data constrained by criteria; Guardium audits queries involving subsets.

## Superuser Account Monitoring
Separately monitors activity of database accounts with unrestricted access.

## Stored Procedure SWITCH Statement
Control structure selecting execution paths; reported by Guardium.

## Transparent Data Encryption Integration
Manages TDE keys with external KMS.

## Transaction Auditing
Audits boundaries and rollbacks of SQL transaction units.

## SQL UNION Operation
Combines results from multiple SELECT statements; audited for data leakage.

A-TAP(Application TAP): Kernel-level agent intercepting calls from local applications to the database.
Aggregator(Guardium Aggregator): Central appliance aggregating data from multiple Collectors.
CAS(Change Audit System): Detects changes to schemas, procedures, and objects.
Collector(Guardium Collector): Receives, processes, and stores data from S-TAP agents.
CSV(Comma-Separated Values): Data format used for export/import in Guardium.
DB2(Database 2): IBM RDBMS supported by Guardium.
DSN(Data Source Name): Identifier linking Guardium to specific databases.
ExploitUtilities(Exploit Utilities): Tools for testing vulnerabilities in databases.
FileTypes(File Types): Configuration specifying handling of file types.
GDPR(General Data Protection Regulation): EU regulation for personal data protection; supports compliance.
GIM(Guardium Installation Manager): Deployed remotely to manage S-TAP agents.
HadoopHadoop Integration: Monitors data processed in Hadoop environments.
JSON(JavaScript Object Notation): Data format supported for import/export in Guardium.
K-TAP(Kernel TAP): Linux kernel module intercepting socket traffic.
MD5(MD5 Hash): Generates checksums for data integrity verification.
NTLM(NT LAN Manager): Windows authentication protocol supported by Guardium.
OpenLDAPOpenLDAP Support: Integrates with OpenLDAP for user management.
Password Policy(Password Policy): Enforces password complexity and expiration.
PBCAClient(PB Secure Client): Secure communication between Guardium and databases.
PostgresPostgreSQL Support: Monitors PostgreSQL instances.
QR-Query Routing: Routes SQL queries to specific resources based on rules.
RSA(RSA Encryption): Secures data in transit and at rest.
S3000(Series 3000): Guardium appliance model with specific capabilities.
SchemaScanner(Schema Scanner): Discovers and catalogs database schemas.
SP(Security Provider): External system for authentication/authorization.
STAP(Software TAP): Captures and forwards database traffic to a Collector.
TeradataTeradata Integration: Monitors Teradata databases.
UbuntuUbuntu Linux: Supported OS for Guardium components.
Versions(Version Manager): Tracks software versions across Guardium components.
VirtualHost(Virtual Host): Represents a logical database instance on a physical server.
WindowsWindows Support: Comprehensive support for Microsoft SQL Server.

```markdown
A-TAP: Kernel-level agent intercepting local database application calls.
Acceptor: Central appliance receiving aggregated data for enterprise reporting.
Actions: Configurable tasks or policies triggered by Guardium events.
Aggregator: Appliance consolidating data from multiple Collectors.
Alert Definitions: Custom notifications for security events or policy violations.
Audit Trail: Comprehensive log of database activities and system events.
Backup: Copy of system configurations, policies, and collected data.
Bypass: Exclusion of sessions or users from Guardium monitoring.
Cache: Storage for session information to optimize monitoring performance.
CAS: Module detecting changes to schemas, procedures, and objects.
Centralized Management: Managing and enforcing policies across environments.
Centralized Control: Single interface for managing multiple database servers.
Change: Change Audit System module for schema and object changes.
Collector: Appliance receiving data from S-TAP agents for analysis.
```

## Guardium Collector
Receives, processes, and stores database activity data from S-TAP agents.

## Compliance Reporting
Generates reports and evidence for regulatory standards and internal policies.

## Connection Data
Specifies database access details for monitoring.

## Database (FAM)
Monitored target system for data access and usage.

## Data Classification
Categorizes data by sensitivity and regulatory requirements.

## Data Discovery
Identifies and classifies sensitive data across the enterprise.

## Data Masking
Obscures sensitive data while allowing use for testing/development.

## Database Instance
Specific database software installation on a server.

## Data Redaction
Automatically removes/modifies sensitive data in query results.

## Data Retention Policy
Defines storage duration for collected data before archiving/deletion.

## DLP Integration
Enhances data breach detection and prevention with third-party solutions.

## Encryption Support
Monitors and protects encrypted database communications and data.

## Event Monitoring
Captures and analyzes specific database events based on policies.

## External S-TAP
Deployed on separate server from database for distributed monitoring.

## Failover Configuration
Standby appliance takes over in case of primary system failure.

## Field Extraction
Parses and extracts specific fields/values from logs/network traffic.

## Grouping Definitions
Categorizes database users/servers/activities into logical groups.

## GUI
Graphical interface for configuring settings and monitoring activities.

## Health Checker
Evaluates health and performance of connected database servers/appliances.

## Inspection Engine
Captures and analyzes database traffic for anomalies and policy enforcement.

## Inspection Engine Agent
Facilitates communication between database and Guardium system.

## Integration Options
Variety of methods/APIs for connecting with other security tools/platforms.

## Interface (GUI)
Provides graphical interaction with the Guardium system.

## Job Scheduling
Automates data collection, analysis, and reporting tasks.

## Key Authentication
Uses cryptographic keys to authenticate communications between components.

## Load Balancing
Optimizes performance by distributing monitoring tasks across appliances.

## LDAP/LDAP Authentication
Authenticates users and manages access via LDAP directories.

## License Management
Manages and renews software licenses for continuous operation.

## Log Management
Collects, stores, and analyzes system logs from the Guardium system.

## MFA Support
Enhances security with multi-factor authentication methods.

## Masking Definitions
Custom rules for masking sensitive data in query results/reports.

## Monitoring Data
Data collected on database activities and user behaviors for analysis.

## MySQL (FAM)
Monitors and protects MySQL databases.

## Network Configuration
Configures network settings and policies for traffic monitoring.

## Data Normalization
Standardizes data formats/values for consistency in reporting/analysis.

## OpenLDAP (Authentication)
Integrates with OpenLDAP for user authentication and access control.

## About
Data loss prevention (DLP) in Guardium identifies and protects sensitive data across databases and file systems to prevent unauthorized exposure or exfiltration.

## Terms
- **External Data Source (EDS):** Non-database repositories like flat files, Hadoop clusters, or web services monitored by Guardium collectors.
- **Guardium Installation Manager (GIM):** Central tool for deploying, upgrading, and configuring S-TAP agents on database servers.
- **Investigative Query (Wallarm):** Tool for deep forensic analysis by drilling into specific data events.
- **LDAP Integration:** User authentication and group management from LDAP servers.
- **Linux unified key setup (LUKS):** Disk encryption for Linux systems supported by Guardium for secure data storage.
- **Log collector storage management:** Configuration and management of storage for log collectors within Guardium.
- **Log server:** System responsible for aggregating and storing logs from Guardium agents.
- **Message Authentication Code (MAC):** Cryptographic checksum ensuring data integrity and authentication in communications.

## Guardium Components

### Activity Log
Log Activity in Guardium continuously monitors and records database connections, queries, and associated activities for security and compliance audits.

### Network Tap (N-TAP)
Hardware or software device placed at a network junction to intercept and duplicate traffic for monitoring purposes without affecting performance.

### Policy Builder
Graphical interface for creating and managing policies that define how database access is monitored and controlled.

### Query Builder
Tool for constructing complex SQL queries for reporting and analysis, providing a user-friendly interface for defining query conditions.

### Report Builder
Suite of tools for creating, scheduling, and distributing compliance reports, including customizable templates for regulatory standards.

### S-TAP Health Check
Feature that monitors the status and performance of Software TAP agents to ensure correct capture and forwarding of database activity data.

### Vulnerability Assessment
Process of identifying, quantifying, and prioritizing security vulnerabilities in databases and associated applications to mitigate risks.

### Whitelist
Predefined list of safe data, commands, or IP addresses exempt from monitoring or alerting, reducing false positives in security reports.

### Additional Components
- **A11 (Network Acceleration)**: IBM DataAccelerator component that speeds up query processing for data-intensive workloads.
- **ASIB (Encryption API for z/OS)**: Enables monitoring of encryption keys and data access in z/OS environments.
- **ATH (Action)**: Type of Inventory item representing actions performed in a system.
- **AUDIT_STREAM (Guardium Audit Stream)**: Streams audit data to external systems for compliance or analysis.
- **ATTR (Attribute)**: Specific characteristic or property of an entity in Guardium.
- **ATTRIBUTES (Attributes)**: Collection of properties describing an entity's characteristics.
- **AUX_TABLE (Oracle AWT Auxiliary Table)**: Auxiliary table used in Oracle Automatic Workload Repository.
- **BEST_LIMITING (Best Limiting Traps)**: Algorithm for selecting the most efficient traps in anomaly detection.
- **C-API (Custom APIs)**: Programming interfaces for integrating custom solutions with Guardium.
- **CLUSTERING (Clustering Algorithm)**: Technique used in anomaly detection to group similar data points.
- **CRAZY (Simulator)**: Internal tool or feature used for testing Guardium components.
- **CRM (Customer Relationship Management system)**: Business system where FAM can monitor file activities.
- **CSAF (Common Standard Audit File)**: Standard format for audit data exchange.
- **CUR (Date Range)**: Specific date range used in reporting and data filtering.
- **DB2_BINIAL_COUNTS (Internal)**: Internal processing mode for handling DB2 bind variable counts.
- **DB2_DIAG (Table)**: Captures DB2 diagnostic messages and errors.
- **DB2_SYSTEM_NOTIFICATIONS (Table)**: Captures system-level notifications and events from DB2.
- **DEBUG_LEVEL (Integers)**: Specifies the depth of debugging detail for Guardium components.

## IBM Guardium Modules

**FAM (File Activity Monitoring)** monitors access to unstructured data files on NAS, SharePoint, and similar storage.

**GDPR** compliance is supported via discovery, masking, and audit trails.

**GIM (Guardium Installation Manager)** remotely deploys, upgrades, and manages S-TAP agents across database servers.

**K-TAP** is a Linux kernel module that intercepts OS-level database socket traffic.

**S-GATE** enforces real-time database access policies and blocks or masks unauthorized queries.

**S-TAP** captures and forwards database traffic to a Guardium Collector.

## Guardium Components

**A-TAP (Application TAP)** intercepts database calls made by local applications on the server.

**Aggregator** consolidates activity data from multiple Collectors for enterprise-wide reporting.

**CAS (Change Audit System)** detects and records changes to schemas, stored procedures, and object configurations.

**Collector** receives, processes, and stores database activity data.

**Configurator** defines policies, classifications, and configuration settings.

**Control Center** centrally monitors and controls Guardium appliances.

**Data Collector** captures raw traffic and forwards it for analysis.

**Guardium Appliance** runs the Guardium software suite.

**Guardium Cloud** offers cloud-based deployment.

**Guardium XFF** extends functionality with custom integrations.

**Guardium License Manager** ensures license compliance.

**Guardium Monitoring Agent** collects system metrics.

**Guardium Patch Manager** applies updates and hotfixes.

**Guardium Policy Builder** visually designs protection policies.

**Guardium REST API** interacts programmatically with Guardium.

**Guardium View** provides predefined reporting dashboards.

**HDFS (Hadoop Distributed File System)** audits access to big data environments.

**HEC (HTTP Event Collector)** forwards events to Splunk.

**JRE (Java Runtime Environment)** is required for Java components.

**JDBC (Java Database Connectivity)** monitors JDBC applications.

**Kerberos** enables secure network authentication.

**LDAP** supports user authentication and authorization.

**Log Manager** manages log file retention policies.

**Monitoring Agent** tracks system resource usage.

**Netezza** is supported for auditing data warehouse access.

**NGINX Ingress Controller** monitors web access in Kubernetes.

**OAuth** supports secure API and application access.

**OpenID Connect** provides single sign-on authentication.

**Perimeter Analysis** detects unusual traffic patterns.

**Policy Agent** enforces data access policies.

**Policy Builder** creates and implements protection policies.

**Policy Exception** exempts specific operations from policies.

**Policy Violation** triggers alerts when policies are breached.

**Privilege Escalation** detects unauthorized privilege increases.

**Remote Collector** collects data from distributed locations.

**Resource Monitor** tracks appliance performance metrics.

**S3 (Amazon Simple Storage Service)** audits access to cloud storage.

## Object Storage and Security

- **Secure Sockets Layer (SSL)**: Encryption protocol supported by Guardium for securing data in transit between components.
- **Sensitivity Analysis**: Method for assessing the impact of data classifications on access control and auditing requirements.
- **Shell S-TAP**: Variant of S-TAP that focuses on monitoring shell and command-line access alongside database traffic.
- **Shell User**: User account type monitored by Shell S-TAP for non-interactive access to database servers.
- **SIEM (Security Information and Event Management)**: Platform for aggregating and analyzing security event data, integrated with Guardium for unified threat management.
- **Single Sign-On**: Authentication mechanism supported by Guardium for seamless access across multiple systems using a single set of credentials.
- **SQL Guard**: Guardium component that analyzes and monitors SQL queries and activities in real-time.
- **SQL Injection**: Security vulnerability detected and mitigated by Guardium policies and alerts.
- **SQL Server Database**: Microsoft relational database supported by Guardium for comprehensive auditing and compliance solutions.
- **SQL Tuning**: Guardium feature that provides insights and recommendations for optimizing database query performance.
- **Structured Query Language**: Database query language universally supported by Guardium for monitoring and protecting data access.
- **TLS (Transport Layer Security)**: Cryptographic protocol supported by Guardium for encrypting communications between components.
- **User Behavior Analytics**: Guardium module that profiles normal user behavior to detect anomalies indicative of security threats.
- **Vulnerability Assessment**: Automated feature of Guardium that scans for and reports on database vulnerabilities and misconfigurations.
- **Web UI (Guardium Web UI)**: Graphical interface for managing Guardium policies, reports, and system settings through a web browser.
- **Workflow Engine**: Component that automates policy enforcement and response actions based on detected threats.

## Acronyms and Terms

- **CAS (Change Audit System)**: Guardium module that tracks changes to database schemas, objects, and configurations.
  - **CAS Host Group**: Logical grouping of CAS hosts for unified policy enforcement.
  - **CLI (Common Language Interface)**: Guardium command-line interface used for managing CAS entities.
  - **Data Collector**: CAS component that gathers activity data from monitored database servers.
  - **Host Alias**: Friendly name used to identify a CAS host within the Guardium environment.
  - **Host Identification**: Process of uniquely identifying a database server for CAS monitoring.
  - **Kernel Component**: Guardium driver or module loaded into the database server's kernel for transparent monitoring.
  - **Legacy Agent**: Older versions of CAS agents that may lack support for newer features.
  - **Log File**: Text file where CAS records audit trails, errors, and operational logs.
  - **Monitor Profile**: Set of rules and thresholds used by CAS to determine which activities to capture.
  - **ORA (Oracle)**: Database platform supported by Guardium CAS for auditing Oracle environments.
  - **Policy Engine**: Core logic in CAS that evaluates monitored activities against defined policies.
  - **Policy Template**: Predefined set of CAS policies for common compliance frameworks.
  - **SQL Guard IP**: IP address of the SQL Guard unit used for communication in a Guardium cluster.
  - **SQLGuard Host ID**: Unique identifier for a host in a Guardium SQL Guard deployment.
  - **S-TAP (Sender TAP)**: Agent deployed on database servers to capture and stream activity data to CAS Collectors.
  - **Secure Shell (SSH)**: Network protocol used for secure command execution and file transfers within CAS.
  - **System Panel**: Administrative UI component in CAS for visualizing configuration and status.
  - **User Privilege Audit**: CAS feature that logs and monitors privilege escalation and misuse.

- **Compliance Repository**: Centralized database in CAS storing predefined compliance policy templates.
- **Security Event**: Recorded incident of unauthorized or policy-violating activity by CAS.
- **Kerberos Token**: Authentication token used for securing communications in Guardium environments.
- **Integration Toolkit**: Guardium-provided SDK for integrating third-party security tools with CAS.
- **Silent Deployment**: Remote installation method for CAS agents without user interaction.
- **Self-Service Portal**: Web interface in CAS enabling users to request and review audit reports.
- **Policy Builder**: GUI tool within Guardium for designing and configuring CAS policies.
- **Activity Stream**: Real-time flow of captured database activities processed by CAS Collectors.
- **Event Queue**: Internal CAS buffer where unprocessed security events are temporarily stored.
- **Session Audit**: CAS capability to monitor and report on individual database user sessions.
- **Change Management Integration**: Feature enabling CAS to feed audit data into external change management systems.
- **Tagging Mechanism**: CAS feature allowing categorization of monitored data based on pre-defined tags.
- **Nested Groups**: Hierarchical structure in CAS for organizing hosts and policies for complex environments.
- **Watchdog Service**: Automated self-recovery process in CAS to ensure continuous monitoring.
- **Export API**: Guardium interface for exporting CAS audit logs in various formats.
- **Import API**: Guardium interface for importing predefined policies or configurations into CAS.
- **Policy Linking**: CAS mechanism for associating multiple policy templates with a single host group.
- **Credential Vault**: Secured storage within CAS for managing database credentials securely.
- **Agentless Monitoring**: CAS feature allowing monitoring of certain databases without installing agents.
- **Certificate Revocation List (CRL)**: File containing revoked certificates used to verify the validity of web certificates monitored by CAS.
- **Activity Pattern**: Regular expression used within CAS to define specific sequences of monitored activities.

## Guardium Components Overview

### Key Components
- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **Aggregator**: Consolidates activity data from multiple Collectors.
- **CAS**: Detects and records changes to database schemas and objects.
- **Collector**: Receives and processes database activity data.
- **FAM**: Monitors access to unstructured data files.
- **GIM**: Central tool for deploying and managing S-TAP agents.
- **K-TAP**: Linux kernel module intercepting OS-level database traffic.
- **S-GATE**: Enforces real-time database access policies.
- **S-TAP**: Captures and forwards database traffic to Collectors.

### Monitoring Modules
- **File Activity Monitoring (FAM)**: Focuses on unstructured data file access.
- **Change Audit System (CAS)**: Tracks schema, stored procedures, and object changes.

## IBM Guardium Overview
**CAS**: Detects and records schema, stored procedure, and configuration changes.
**Collector**: Receives, processes, and stores database activity from S-TAP agents.
**FAM**: Monitors access to unstructured data files on NAS, SharePoint, etc.
**GDPR**: EU data protection regulation; Guardium supports compliance with discovery, masking, and audit trails.
**GIM**: Central tool for deploying, upgrading, and managing S-TAP agents across servers.
**K-TAP**: Linux kernel module that intercepts OS-level database socket traffic.
**S-GATE**: Enforces real-time database access policies and blocks or masks unauthorized queries.
**S-TAP**: Agent installed on database servers that captures and forwards traffic to a Collector.
## Guardium Data Protection Features
**Amortization**: Allocates resources based on observed usage patterns to optimize utilization.
**Anomaly Learning**: Establishes baseline "normal" behavior and detects deviations indicating potential threats.
**Application Layer Protocol Violations**: Monitors for malformed SQL or invalid transaction sequences.
**Audit**: Reviews security-relevant events to ensure compliance with policies and regulations.
**Audit Trail**: Chronological record of system activities within Guardium.
**Backlog Inspection**: Analyzes pending tasks or data awaiting processing by Guardium systems.
**Blacklist**: Prohibits or flags entities, patterns, or behaviors for special attention.
**Client Certificate**: Authenticates clients to servers for secure access control.
**Database Query Rewriter**: Masks sensitive data or enforces masking policies in SQL queries.
**Exception Handling**: Manages unusual or unexpected events like unauthorized data access attempts.
**File Path Inclusion**: Configures specific directories or file types for File Activity Monitoring.
**Granularity of Result**: Sets the level of detail in reports and monitoring of data access and policy violations.
**Hash**: Securely stores and compares data values such as passwords or dataset identifiers.
**High-Risk Attributes**: Identifies table or column characteristics posing higher security risks requiring stricter controls.
**Highest Hit Count**: Prioritizes alerts based on the most frequently accessed or violated objects or queries.
## Backup and Monitoring
**Incremental Backup**: Backs up only changes since the last backup, reducing storage needs.
**Invalid SQL**: Detects and logs syntax errors or prohibited operations.
**Kernel-Level Interception**: Captures database activities at the OS level without impacting performance.
**Login Attempt**: Monitors authentication efforts to detect brute force attacks or misuse.
**Malicious Request**: Identifies intentionally harmful operations or policy violations.
**Mask**: Obfuscates sensitive information like PII while allowing data processing.
**Non-Compliance**: Failing to meet regulatory requirements, identified through audits.
**Outlier Detection**: Identifies unusual patterns or activities deviating from established norms.
**Policy**: Rules governing monitoring, alerting, and response to security events or access patterns.
**Query Rewrite Function**: Modifies SQL queries in real-time for masking or performance optimization.
**Real-Time Monitoring**: Continuous observation of database activities to detect and respond to incidents.
**Risk Score Calculation**: Determines risk levels based on violations, behavior, and configurations to prioritize alerts.
**Role-Based Access Control (RBAC)**: Assigns permissions based on user roles to access data or perform actions.
**Rule**: Conditions that trigger actions like logging, alerting, or blocking when matched.
**Sensitivity Score**: Classifies data sensitivity levels to prioritize security measures.
**Session Monitoring**: Tracks user sessions to analyze behaviors and identify risks.
**Session Recording**: Captures complete database sessions for analysis and investigation.

```markdown
## Guardium Components and Features

### Data Monitoring
- **A-TAP(Application TAP)**: Intercepts database calls made by applications on the server.
- **Aggregator(Guardium Aggregator)**: Centralizes activity data from multiple Collectors.
- **Collector(Guardium Collector)**: Receives, processes, and stores database activity data.

### Data Protection
- **Data Masking**: Obscures sensitive data.
- **FAM(File Activity Monitoring)**: Monitors access to unstructured data files.
- **GDPR(General Data Protection Regulation)**: Supports compliance with EU data protection laws.

### Management Tools
- **GIM(Guardium Installation Manager)**: Manages S-TAP agents remotely.
- **CAS(Change Audit System)**: Detects and records changes to database schemas and configurations.
- **S-GATE(Software Gate)**: Enforces real-time database access policies.

### Additional Tools
- **SNMP(Simple Network Management Protocol)**: Supports Guardium's network monitoring capabilities.
```

## 2607. Number sign
REST API for configuring system backups added in Guardium v11.4, supporting POST method.

## 2608. Number sign
REST API endpoint for deleting external registry entries, available from Guardium v12.2.2.

## 2609. Number sign
`api_target_host` format requires IPv4 or IPv6 IP addresses.

## 2610. Number sign
REST API for F5 data deletion management, available from Guardium v9.5.

## 2611. Number sign
`get_ip_restriction_config` GuardAPI includes `api_target_host` for execution.

## 2612. Configure for client web certificates
API permissions and steps for enumerating NetApp shares.

## 2613. Configure for client web certificates
Feature for integrating client web certificates in data discovery workflows.

## 2614. Special handling for TRANSFORM actions
Action keyword for daily alert notifications in rule management.

## 2615. Special handling for TRANSFORM actions
Workflow element for importing CSV data into the system.

## 2616. Special handling for TRANSFORM actions
Feature components for data transformation behaviors.

A-TAP: IBM Guardium kernel-level agent intercepting database calls made by local applications directly on the database server.
Aggregator: Guardium appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.
CAS: Guardium module detecting and recording changes to database schemas, stored procedures, and object configurations.
Collector: Guardium appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.
FAM: Guardium module monitoring access to unstructured data files on NAS, SharePoint, and similar storage.
GDPR: General Data Protection Regulation requiring protection of personal data, supported by Guardium via discovery, masking, and audit trails.

oos unit

`02aa094b-c6b9-44d9-9b16-4dd346bd98fa`  |  **categories:** keywords, entities

Specifies the number of characters considered a string when resolving SQL group functions.

---

## 2680. SQL groups unit

`474340b1-064c-4e19-a474-4b30081433d8`  |  **categories:** keywords, entities

Defines the character count that determines a string when processing SQL group functions.

---

## 2681. SQL groups unit

`0583c580-343e-40ad-a6a5-b288a7ea668d`  |  **categories:** features, entities

Explains how to configure the string length threshold for SQL group functions within Guardium's SQL processing engine.

---

## 2682. SQL processing time limits

`9fc776dd-b349-4e9e-990d-a6f9c9e9b8b5`  |  **categories:** features, entities

Specifies parameters to control the maximum time allowed for SQL processing before it is considered a performance issue.

---

## 2683. SQL processing time limits

`9c9bb92e-a685-4e6f-95da-bba4ee0ce3d5`  |  **categories:** keywords, entities

Defines limits on the duration of SQL query execution to prevent long-running queries from impacting system performance.

## Guardium Custom Policy Translation Warning Limit
Explains how to control the volume of warning messages produced during the custom SQL policy translation process in SQL Guard.

## SQL Guard Onboarding URL - 2680
Provides the URL that users must navigate to begin the onboarding process for SQL Guard, facilitating initial system setup.

## SQL Guard Onboarding URL - 2681
Describes the web address where users can access resources and steps necessary for initiating the SQL Guard onboarding process.

## SQL Guard Onboarding URL - 2682
Specifies the location online where new users can start configuring SQL Guard, guiding them through initial setup procedures.

## SQL Guard Onboarding URL - 2683
Identifies the specific webpage that serves as the starting point for new users to register and configure SQL Guard within their system.

## Stop Vulnerabilities between Web Server and Database - 2684
Describes a purpose-built solution designed to prevent security vulnerabilities from occurring between web servers and databases, enhancing overall system security.

## Stop Vulnerabilities between Web Server and Database - 2685
Details a technology or service aimed at mitigating the risks of vulnerabilities found between web servers and their associated databases.

## The FAM for SAN parameter can be changed at Guardium Portal - 2686
Specifies that the File Activity Monitoring for SAN (Storage Area Network) setting can be adjusted through the Guardium Portal interface.

## The FAM for SAN parameter can be changed at Guardium Portal - 2687
Indicates that modifications to the FAM for SAN configuration can be made via the administration interface of the Guardium system.

## The FAM for SAN parameter can be changed at Guardium Portal - 2688
Highlights the flexibility of the Guardium system in allowing the FAM for SAN parameters to be configured or adjusted from the Guardium Portal.

## The FAM for SAN parameter can be changed at Guardium Portal - 2689
Explains the capability to modify FAM for SAN configurations directly from the management interface of the Guardium system, reflecting its adaptability.

## The FAM for SAN parameter can be changed at Guardium Portal - 2690
Notes that the Guardium Portal provides the functionality to change FAM for SAN settings, allowing administrators easy access to configuration tools.

## Core Components
**S-TAP**: Guardium agent on database servers capturing traffic and forwarding to Collectors.

**Collector**: Appliance receiving, processing, and storing data from S-TAP agents.

**Aggregator**: Central appliance consolidating data from multiple Collectors for enterprise reporting.

## Supporting Modules
**CAS**: Detects and records changes to schemas, procedures, and configurations.

**FAM**: Monitors access to unstructured files on NAS, SharePoint, etc.

**GDPR**: Supports EU data protection compliance.

## Deployment and Management
**GIM**: Central tool for deploying and managing S-TAP agents.

**Guardium GUI**: Web interface for configuration and audit reporting.

## Monitoring and Alerting
**Kernel TAP(K-TAP)**: Linux kernel module intercepting socket traffic.

**CPU Utilization**: Percentage of CPU cycles used by Guardium processes on S-TAP agents.

**Real-Time Alerting**: Generates alerts immediately on policy violations.

## Data Handling
**Checkpoint File**: Persists CAS state across restarts.

**Ship Data**: Transfers audits from Collectors to Aggregators.

## Roles
**Investigator**: Views audit data without configuration permissions.

## IDENTITY
201d-9a2e-0f252d2a3eba

Descriptor for profiling a database user across multiple connections.

## MONITORING TYPE
3c2b-d648-4af7-999e


## PARAMETERS

## User Activity Audit Trail Reporter
The charting function in Guardium allows users to select data series and plotting options such as line, bar, histogram, and conditional formatting to visualize database activity trends and anomalies.

## Data Mart CPUs
To modify the datamart definition, select All Datamart CPUs, which is the default when creating a datamart; click Commands, and choose Add, Stats, or Set Parallelism.

Universal Connection Framework: IBM framework enabling unified access to heterogeneous data sources, integrated with Guardium for comprehensive data visibility.

XML(eXtensible Markup Language): Markup language for encoding documents in a human‑ and machine‑readable format; used by Guardium for configuration and report generation.

GDPR(General Data Protection Regulation): EU regulation requiring personal data protection; Guardium supports compliance through discovery, masking, and audit trails.

GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S‑TAP agents on database servers.

K‑TAP(Kernel TAP): Linux kernel module loaded on the database server to intercept OS‑level database socket traffic for Guardium monitoring.

S‑GATE(Software Gate): Guardium component that enforces real‑time database access policies and blocks or masks unauthorized queries.

S‑TAP(Software TAP): IBM Guardium agent installed on database servers; captures and forwards database traffic to a Collector.

## Guardium Overview

**S-TAP** (Software TAP) captures and forwards database traffic from database servers to a Guardium Collector.  
**A-TAP** intercepts database calls made by local applications directly on the server.  
**K-TAP** kernel module intercepts OS-level database socket traffic on Linux systems.  

**Collectors** receive, process, and store activity data.  
**Aggregators** consolidate data from multiple Collectors for enterprise-wide reporting.

## Data Management & Protection

**FAM** monitors access to unstructured data files on NAS and SharePoint.  
**CAS** detects and records changes to database schemas, stored procedures, and object configurations.  
**Vulnerability Assessment** scans configurations and reports security weaknesses.  
**GDPR** compliance features include discovery, masking, and audit trails.

## Deployment & Management

**GIM** remotely deploys, upgrades, and manages S-TAP agents.  
**W-TAP** monitors web application database interactions.  
**API_KEY** authenticates API requests to Guardium services.

## System Components

**GUARDIUM AGGREGATOR** consolidates activity data.  
**POLICY MODIFICATION** changes the rules and conditions of security policies.  
**DRY_RUN** validates policies without enforcing actions.  

**Report Archive** stores completed reports.  
**Certificate Enforcement** requires valid TLS certificates from database servers.  
**Configuration Revision** tracks version numbers of configuration sets.

## Security & Compliance

**Data Classification** assigns sensitivity levels to data.  
**Data Retention Period** defines how long activity data is stored.  
**Incident** records security events as policy violations.  
**Insider Threat** detects suspicious internal user activities.

## Monitoring & Resolution

**Event Queries** are generated by Guardium's event monitoring system.  
**Extraction Time** is the timestamp of data extraction for reports.  
**File Size Limit** caps the size of agent log files.  

**Incidents** record detected security violations.  
**Keyword Search** allows searching reports and data with specific terms.  
**Job Status** indicates the state of scheduled tasks.

## System Settings

**Installation Guide** provides system setup procedures.  
**Licensing** applies valid licenses to Guardium components.  
**Logical Datasource** abstracts representation of database servers.  

**Maximum Retry Limit** caps connection attempts.  
**Network Interface** defines the communication path for appliances.  
**Number of Retries** sets the attempts before connection failure.

## Data Protection

**Operating Mode** configures appliance state (active/passive).  
**Operational Status** reflects the health of Guardium components.  
**Port Number** is the network port for Guardium services.

## Appliance
IBM Guardium server that provides centralized data security and monitoring functions.

## A-TAP
IBM Guardium kernel-level agent that intercepts database calls made by local applications directly on the database server.

## Aggregator
Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

## CAS
Guardium module that detects and records changes to database schemas, stored procedures, and other object configurations.

## Collector
Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

## Conditional Expression
Query statement in Oracle tools that evaluates fields against constants or runtime parameters to filter results.

## CPU
Central processing unit responsible for executing instructions and performing calculations within a system.

## Database Name
Name of the database for the session; specific to MSSQL or Sybase, may include application context for Oracle.

## Having Conditions
Query clause that filters grouped records based on specified conditions, often involving aggregation functions.

## Intermediary Calculation Result
Transient result of a computation or data transformation used internally by developers or analysts.

## Kernel TAP
Low-level software module integrated into the OS kernel to capture and redirect specific system calls or events.

## Linux Kernel Module
Loadable component of the Linux kernel that extends functionality without rebooting, used for drivers, file systems, or security features like K-TAP.

## Modules
Reusable packages of functionality in software systems, encompassing interchangeable components that perform specific tasks or services.

## Oracle(SOB) example
Specific examples or configurations relevant to Oracle databases, illustrating features, functionalities, or operational details.

## Parameter
Value passed to a function, procedure, or query to dynamically alter behavior or influence the outcome of operations.

## Report Result Data Row
Specific row within the table "REPORT_RESULT_DATA_ROW" holding the results of audit processes conducted by Guardium.

## Transform
Operation within Guardium's data processing pipeline that modifies, filters, or manipulates data based on predefined rules or conditions.

## Entities

### Technical Components

- **A-TAP(Application TAP)**: Kernel-level agent intercepting database calls from applications on the server.
- **Aggregator(Guardium Aggregator)**: Consolidates activity data from multiple Collectors for comprehensive reporting.
- **CAS(Change Audit System)**: Detects and logs changes to database schemas and objects.
- **Collector(Guardium Collector)**: Receives, processes, and stores database activity data from S-TAP agents.
- **CPU(Central Processing Unit)**: Tracks STAP verification details within Guardium.
- **FAM(File Activity Monitoring)**: Monitors and logs access to unstructured data files.
- **GCD(Guardium Central Directory)**: Repository for policies and configurations across Guardium appliances.
- **GIM(Guardium Installation Manager)**: Central tool for managing S-TAP deployments and upgrades.
- **GDPR(General Data Protection Regulation)**: Compliance framework supported by Guardium's data protection features.
- **Kernel Module**: Software component loaded into the OS kernel (e.g., K-TAP for OS-level traffic interception).
- **K-TAP(Kernel TAP)**: Linux kernel module intercepting database traffic.
- **License(License Value)**: Indicates available Guardium licenses for S-TAP deployments.
- **Log(Log Entry)**: Records database activities (user, source, SQL statements, etc.).
- **MySQL(MySQL Information Schema)**: Used for generating entitlement reports in Guardium.
- **PAT(Port Address Translation)**: Maps private IP/ports to public ones for network configurations.
- **Protocols(Database Protocols)**: Supported protocols include Oracle, MySQL, etc.

### Software and Services

- **Protocols(Database Protocols)**: Oracle, MySQL, etc.

### File Formats

- **CSV(Comma-Separated Values)**: Used for exporting data mart extractions for reporting.

# IBM Guardium Key Concepts

## Core Components
- **A-TAP**: Kernel‑level agent capturing database calls made by local applications.
- **Aggregator**: Central appliance merging activity data from multiple Collectors.
- **Collector**: Receives, processes, and stores activity data from S-TAP agents.
- **S‑GATE**: Real‑time policy enforcement that blocks or masks policy‑violating queries.
- **S‑TAP**: Software agent installed on database servers to forward traffic to a Collector.
- **K‑TAP**: Kernel‑level tap operating on Linux hosts to intercept socket traffic.
- **WS‑Management**: Web Services protocol potentially integrated for system management.

## Monitoring & Compatibility
- **Database**: Any structured data store (e.g., Oracle, PostgreSQL) that Guardium can monitor and secure.
- **FAM**: Monitors unstructured file access on network shares.
- **SQL**: Captured as part of database activity logs.
- **Oracle**: Specific DB platform supported; illustrative examples use it.

## Compliance & Governance
- **GDPR**: EU personal‑data regulation; Guardium supports discovery, masking, and audit trails.
- **SRC**: Indicates the application that initiated a transaction in the activity log.
- **Version**: Identifies a specific Guardium release (e.g., 11.2).

## Management & Automation
- **GIM**: Tool for remote deployment, upgrade, and management of S‑TAP agents.
- **U‑APM**: Profiles user behavior to detect anomalies.
- **Verify API Key**: Validates API credentials before use.
- **Path**: Directory where a database engine is installed.

## Workflow & Reporting
- **Categories**: Tags for classifying audit records and workflows.
- **Sign Off**: Allows reviewers to digitally approve audit results.
- **ADD_SUB_FILTER**: Configures API target host for specific communication paths.

## Technical Details
- **ADD_DEVICE_ID**: Unique identifier for a monitored device.
- **ALERT_ADAPTER_SYNCHRONIZATION**: Keeps configurations consistent across server types.
- **ALLOWED_SOURCE_PROGRAMS**: Whitelist of approved connection applications.

## Optional Modules
- **CAS**: Detects changes to database objects and configurations.
- **TRANSFORM**: Modifies audit data output before storage or display.

## DB2 Activity Monitoring Enforcement
`enforce(string)` controls whether DB2 activity monitoring is enforced based on specified rules.

## Syslog Audit Message Filter
`audit_syslog_message(filter(string))` custom filters syslog messages for audit purposes.

## System Component Availability
`availability(string)` indicates the status of a system component as operational or unavailable.

## UUID Example
`b12fd085-15a5-49ca-a7fa-e702eef3b548(string)` is an example UUID used in documentation.

## Block Policy Enforcement
`block_policy_enforcement(string)` enables or disables enforcement of blocking policies across monitored databases.

## Certificate Configuration
`certificate_configuration(mode(string))` configures certificate settings for secure communication between Guardium components.

## Client Authentication Mode
`client_auth_mode(string)` determines the method of client authentication used by Guardium services.

## Client Lockout Count
`client_lockout_count(string)` specifies the maximum number of failed authentication attempts before locking a client.

## Client Lockout Duration
`client_lockout_duration(string)` defines the duration a client remains locked out after exceeding failed attempts.

## Client Session Timeout
`client_session_timeout(string)` sets the interval after which inactive client sessions are terminated.

## Cluster Manager IP
`cluster_mgr_ip(string)` is the IP address of the central management node in a high-availability cluster.

## Database Manager ID
`clh_database_manager_id(string)` integrates database management tools with Guardium's monitoring framework.

## Components Allowed
`components_allowed(api_target_host(string))` specifies which Guardium components can communicate with the designated host.

## Config Parameter Completion
`config_parameter_completion(string)` enhances Guardium's auto-completion of database configuration parameters.

## Date and Time Type
`date_and_time_type(string)` is the data type for fields requiring precise date and time entries.

## Default Group
`default_group(string)` applies default settings when no specific group is selected.

## Describe Guidance
`describe_guidance(string)` provides contextual guidance on using specific Guardium features or commands.

## Discovery Policy Delay
`discovery_policy(delay_in_seconds(integer))` sets the time delay before a database discovery policy becomes active.

## Discovery User IP Mode
`discover_db_user_ip_mode(string)` determines how database user IP addresses are handled during discovery.

## DNS Domain
`dns_domain(string)` is the domain name used for DNS queries affecting Guardium's network operations.

## Execution Mode
`execution_mode(string)` defines the operational mode for executing certain Guardium processes.

## Failover Mechanism
`failover(string)` enables Guardium systems to switch to standby components during failures.

## Filter Type
`filter_type(string)` specifies the type of filter used to refine data views or reporting within Guardium.

## Force Option
`force(string)` overrides default behaviors or constraints in Guardium operations.

## GRDAPI Command Interface
`grdapi(id(string))` is the primary command interface for executing Guardium-related tasks and retrieving system information.

## Group Member Application Context
`group_member(source_application(string))` identifies individuals added to a monitoring group with a specific application context.

## Hadoop Cluster Identifier
`hadoop_cluster(string)` identifies and monitors Hadoop cluster activities within Guardium.

## Sensitive Data Indicator
`has_sensitive_data(boolean)` indicates if a dataset contains sensitive information requiring additional protections.

## High Availability Mode
`high_availability_mode(string)` enables high availability features in Guardium deployments.

## Host Name
`host_name(string)` is the system name used for network identification and management within Guardium.

## Ignored Processes
`ignored_processes(string)` lists processes Guardium should ignore when monitoring database activities.

## Include File Sizes
`include_file_sizes(integer)` includes file size information in reported data.

## Intervals to Skip
`intervals_to_skip(integer)` specifies the number of iterative intervals to skip in scheduled tasks or data collection.

## IR Application Identifier
`ir_application(string)` identifies applications integrated with Guardium's identity reconciliation features.

## Identity Reconciliation SGID
`ir_sgid(string)` manages and audits group memberships in identity management systems.

## Internal Resource Index
`iri(string)` uniquely identifies internal resources within Guardium databases.

## Data Caching Flag
`is_cached(boolean)` indicates if specific data or results are temporarily stored for faster retrieval.

## Real User Session
`is_real_user(boolean)` determines if the session or user context represents a genuine end-user activity.

## Kernel Timestamps
`kernel_timestamps(boolean)` enables or disables kernel-level timestamps in data capture processes.

## Legacy Group
`legacy_group(string)` refers to older, still supported but deprecated, group configurations.

## Limit Records
`limit(integer)` sets the upper boundary for records returned or operations performed.

## List TAP String
`list_tap_string(string)` outputs a comma-separated list of database server types monitored by a specific S-TAP agent.

## Local Adapters Count
`local_adapters(integer)` specifies the number of local data adapters configured for processing data streams.

## Logical Name
`logical_name(string)` is the logical identifier used to reference entities or components within Guardium systems.

## Log File Prefix
`log_file_prefix(string)` prefixes log file names for organizational purposes.

## Mobile Configuration
`mobile(string)` sets configuration or feature settings related to mobile access capabilities of Guardium.

## Monitoring Time
`monitor_time_in_seconds(integer)` defines the active duration for specific monitoring activities.

## Non-Sensitive Data Indicator
`non_sensitive_data(boolean)` indicates datasets that do not contain sensitive information.

## Normal Mode
`normal_mode(string)` sets the standard operational mode without enhanced security features.

## Number Sign Token
`number_sign(string)` indicates that the line or section should be skipped or is irrelevant in configuration files.

## Operating System Type
`operating_system_type(string)` defines the OS environment for deploying or managing Guardium components.

## OS User
`os_user(string)` specifies the operating system user context under which certain operations run.

## Guardium Components and Concepts

### Core Modules
- **A-TAP**: Kernel-level agent intercepting database calls by local applications.
- **Aggregator**: Consolidates activity data for enterprise-wide reporting.
- **CAS**: Detects and records changes to database schemas and objects.
- **Collector**: Receives, processes, and stores database activity data.
- **FAM**: Monitors access to unstructured data files on NAS and SharePoint.
- **GDPR**: Supports compliance with EU personal data protection regulations.
- **GIM**: Deploys, upgrades, and manages S-TAP agents across database servers.
- **K-TAP**: Linux kernel module intercepting OS-level database socket traffic.
- **S-GATE**: Enforces real-time database access policies.
- **S-TAP**: Captures and forwards database traffic to a Collector.

### API and Interface
- **API**: Interacts with external systems for configuration and report generation.
- **Assessment**: Evaluates security configurations against defined rules.
- **AssessmentDescription**: Unique name for each assessment created in Guardium.
- **AuditRule**: Specifies what database activities to audit with conditions and severity.

### Discovery and Management
- **AutoDiscovered**: Entities automatically identified during discovery.
- **CassandraStore**: Uses Apache Cassandra for scalable storage of Guardium data.
- **CDC**: Detects and captures changes to data in databases.

### Configuration and Operation
- **partial_deploy**: Partially deploys configurations without full reboots.
- **password**: Handles sensitive authentication information securely.
- **paused**: Indicates temporarily halted processes or components.
- **periodic**: Refers to regularly scheduled operations.
- **reachability**: Evaluates network accessibility from the Guardium environment.
- **redundancy_mode**: Configures redundancy and failover capabilities.
- **resource_utilization**: Measures resource usage by Guardium services.

### Security and Communication
- **rotation_frequency**: Frequency of log file or data record rotation.
- **runtime**: Active running state or session duration.
- **schema_name**: Database schema monitored by Guardium.
- **schedule**: Defines timing and recurrence of tasks.
- **server_status**: Indicates operational health and performance.
- **source_application**: Context for data sessions or transactions monitored.
- **source_ip**: Originating IP address for data requests or transactions.
- **src_ip_mode**: Mode specifying handling of source IP addresses in Guardium operations.
- **ssl_ciphers**: Set of encryption algorithms for secure communication.
- **ssl_enabled**: Enables or disables SSL for data encryption.
- **ssl_private_key**: Private key for SSL certificate configuration.
- **ssl_trusted_certs_dir**: Directory path for trusted certificates used in SSL validation.
- **stateful_inspection**: Enables detailed inspection of data flows for continuous security monitoring.

### Logging and Monitoring
- **store_last_n_days**: Retention period for logs or data records in days.
- **support**: Contact information for technical support issues.
- **suppress_api_errors**: Suppresses error messages from API calls.
- **term_name**: Unique identifier in Guardium's terminology database.
- **timeout_in_seconds**: Time limit for operation or session expiration due to inactivity.
- **trace_mode**: Activates detailed logging and diagnostics.

### Miscellaneous
- **unmanaged_host**: Host system monitored but not centrally managed by Guardium.
- **user_defined**: Custom sequence number for ordering or prioritizing entries in reports or configurations.

## Guardium Core Components
**Collector**: Guardium appliance that receives, processes, and stores database activity data.
**Gateway**: Acts as a policy enforcement point, controlling and analyzing database traffic.
**STAP**: Kernel or software agent installed on database servers to monitor traffic.

## Monitoring Features
**Command Monitoring**: Inspects SQL syntax and parameters for policy violations.
**Query Monitoring**: Observes and logs SQL queries for activity analysis and compliance.
**File Activity Monitoring (FAM)**: Monitors access to unstructured data files on NAS, SharePoint, etc.

## Security & Encryption
**Encrypted Communication**: Secure data transmission using TLS/SSL protocols.
**Certificate Management System (CMS)**: Imports, exports, and verifies SSL certificates.
**S-GATE**: Enforces real-time access policies and blocks unauthorized queries.

## Modules & Tools
**CAS Module**: Tracks schema modifications, stored procedures, and privilege changes.
**Evaluator**: Processes audit logs and applies scoring algorithms to identify violations.
**Policy Builder**: GUI tool for creating and managing security policies.

## Management Infrastructure
**Central Manager**: Orchestrates policy distribution and compliance reporting.
**Scheduler**: Triggers automated tasks like scans, reports, and policy updates.
**Risk Manager**: Assigns risk scores to assets based on detected threats and vulnerabilities.

## Configuration Parameters
**STAPConfiguration**: Defines S-TAP agent interactions, including encryption and protocols.
**URL Parameter**: Defines endpoints for API requests, including base URLs for Guardium services.

## Additional Features
**Assessment**: Automated testing framework for evaluating security posture.
**FAM Scheduler**: Defines scan recurrence, exclusions, and resource allocation for FAM.
**Top K**: Ranks and displays most frequent database activity patterns.

## Guardium Core Concepts

**A-TAP** intercepts local database calls for visibility.  
**Aggregator** consolidates data from Collectors for enterprise reporting.  
**CAS** detects and records database schema and object changes.  
**Collector** receives, processes, and stores activity data from S-TAPs.  
**Egress** refers to traffic leaving Guardium bound for external systems.  
**FAM** monitors access to unstructured data files on file shares.  
**GFIM** performs deep inspection of database traffic for policy enforcement.  
**HDFS** monitoring uses GIM agents to track Hadoop cluster activity.  
**HTTPS**, **LDIF**, **OWASP**, **REST**, **TLS** support secure communications and identity management.  
**PIM** controls privileged user access to databases.  
**RFID** and **USB** monitoring via FAM track physical device interactions.  
**S-GATE** enforces real-time access policies and blocks unauthorized queries.  
**S-TAP** captures and forwards database traffic to a Collector.

## Guardium Components

**ADGUARD** manages data protection activities across systems.  
**API** enables third-party integrations and automation.  
**CLI** provides text-based administration of Guardium appliances.  
**CP-RA** alerts on high CPU/RAM usage impacting performance.  
**CTI** tracks custom business transactions within applications.  
**DB2 Audit Configuration** defines audit settings for DB2 subsystems.  
**DIA** monitors SQL interactions directly from application servers.  
**EXT** transforms raw audit data into structured records for analysis.  
**FAM-DB2** provides visibility into file-level changes affecting databases.  
**FSA** offers context-aware monitoring of file operations.  
**G-EVAL** evaluates events against policies to flag suspicious activity.  
**GEF** enhances performance with parallel processing and load balancing.  
**HIPAA** compliance supported through audit and access controls.  
**IPM** captures DB2 z/OS event logs when kernel taps are not available.  
**JVM** runs Java-based Guardium components like custom transaction rules.  
**KPA** installs custom kernel patches for deep activity monitoring.  
**LDW** monitors data interactions in real-time for immediate visibility.

ure capturing and analyzing database interactions as they occur. 

MHA (Multilink Homogenization Agent): Guardium tool harmonizing multiple data warehouse sources into a unified, queryable format.

NCENT (Nascent Centers): Group of Guardium assets representing early-stage deployment sites reporting into the central aggregator.

OAP (Overtime Activity Profile): Guardium tool identifying abnormal user behaviors by tracking session lengths and access patterns outside normal working hours.

PAT (Protocol Analysis Tool): Guardium utility for parsing and interpreting database protocol traffic to extract actionable insights.

PCAUD (Physical Capture): Guardium method for logging database activity by directly monitoring storage I/O when other methods are unavailable.

PIE (Program Instrumentation Engine): Guardium's backend component compiling custom policies into executable code for real-time enforcement.

PLAN (Plan Cache): Structured storage of SQL execution plans maintained by Guardium for performance trending and anomaly detection.

QAP (Query Analysis Platform): Backend architecture analyzing query patterns for performance tuning and data usage insights.

RACF (Resource Access Control Facility): IBM security management system Guardium integrates with to enforce access policies for z/OS databases.

SROP (Single Row Optimization Processor): Guardium technique reducing redundancy in captured SQL statements by consolidating similar queries with different literals.

SSO (Shadow Structure Observer): Guardium monitoring component tracking file system interactions using kernel modules to map file operations to database activities.

STRACE (System Trace): Linux diagnostic tool used by Guardium to capture system calls as part of real-time database monitoring.

SYSADM (System Administrator): DB2 role with highest authority over database creation, schema alterations, and security policies.

SYSCTRL (System Control): DB2 administrative authority allowing certain operational tasks like stopping or starting the database.

SYSMAINT (System Maintenance): DB2 role responsible for operations like backup, restore, and reorganization without full SYSADM authority.

TG-PW (Truncated Group Password): Guardium mechanism truncating lengthy group names or passwords to a fixed length for policy enforcement compatibility.

TOF (Time of Flight): Guardium metric measuring delay between event logging at the database server and its visibility in Guardium reports.

UDF (User-Defined Function): Custom functions created within databases that Guardium can audit to detect unauthorized usage or sensitive data exposure.

USR2 (Signal USR2): Linux signal used by Guardium to trigger custom actions or scripts during runtime.

XIDS (Index Usage): Guardium metric capturing frequency and context of index accesses to optimize query performance and identify missing indexes.

YAML (YAML Ain't Markup Language): Guardium uses YAML for external configuration files, such as policy definitions or appliance clustering settings.

Z-WAT (Z/OS Windowed Audit Trail): Guardium feature providing real-time analysis of DB2 z/OS audit logs with context-aware parsing.

Z12 (Java 12): Version of Java supported by Guardium for executing custom applications and scripts in monitored environments.

Z13 (Java 13): Version of Java supported by Guardium for modern application environments and extended library support.

Z14 (Java 14): Version of Java supported by Guardium for advanced features and performance improvements in Java-based integrations.

G1-G3: Technical Concepts and Configurations

A10-CFG-Server (Oracle Example): Oracle example for configuring Guardium audit logging and reporting.

AALG (Audit Log): Guardium component that records database activity, access attempts, and system events for compliance and security monitoring.

AH-FMIT (Attributes for K-TAP Part): Configuration parameters related to the K-TAP monitoring mechanism in Guardium.

Api-Health-Check (Verify Certificates): Process to verify SSL/TLS certificates and disconnect connections if certificates are invalid.

Bidi-TCP-Intercepted-Ports (Number Sign): Setting to specify TCP ports for intercepting bidirectional traffic in various Guardium components.

CAS (Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

Crawler-Traffic (Oracle Example): Example of traffic patterns and attributes relevant to FAM (File Access Monitor) crawlers in Guardium.

Datastore (FAM): A configuration entity used to define the license expiration date for each data source monitored by Guardium.

Di-Queue-Length (Skips Registry): Attribute to monitor the queue length of the Di (logger) component, indicating backlog and performance.

Di-Rate (Skips Registry): Attribute representing the rate of logger (Di) activity, used for performance monitoring and tuning.

Dropped-Bytes (Skips Registry): Attribute indicating the number of bytes dropped by the logger (Di) component, used for troubleshooting and log integrity checks.

Execute-FlatLogProcess (Verify Certificates): GuardAPI command to process flat logs and verify associated certificates as part of security and compliance checks.

Fam-Crawler-Traffic (Oracle Example): Traffic characteristics and monitoring considerations specific to FAM crawlers for unstructured file data.

Flat-Log-Process (N-Skips): Process to handle and analyze flat log files within Guardium, configurable with options like the number of steps to skip.

G-Engine (Oracle Example): Component or engine responsible for executing specific tasks or processes in Guardium, often referenced in examples and configurations.

GuardAPI (List All Reports): Guardium's command-line interface API to list all available reports, facilitating automated reporting and monitoring.

Guardium-Aggregator (Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting and analysis.

Guardium-Collector (Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

agent that intercepts database calls made by local applications directly on the database server
CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations
Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents
Data Virtualization(IBM Data Virtualization): IBM solution that enables organizations to create a unified, logical view of data across disparate sources without moving the data
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers
Hashing(HMAC): Hash-based message authentication code used by Guardium for secure data transmission verification
HDFS(Hadoop Distributed File System): Scalable and fault-tolerant storage system for big data; Guardium monitors access via FAM
HIPAA(Health Insurance Portability and Accountability Act): US law mandating data privacy and security for health information; Guardium helps compliance
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring
List-All-Reports(GuardAPI): GuardAPI command to retrieve a comprehensive list of all reports available within the Guardium environment
Netezza(IBM Netezza): Data warehousing appliance; Guardium secures and monitors Netezza environments
Partial-Parameter-Value(N-Skips): Description of syntax allowing specifying partial parameter values and configurations, often used in advanced Guardium settings
Privilege Analysis(ROLES): Guardium module analyzing database user roles and privileges for non-compliant access
RESTful API(Guardium REST API): Web-based interface for programmatically controlling Guardium functions
Rogue-Analyst(Malicious Insider): Guardium user profile representing malicious insiders who deliberately misuse their access privileges
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries
Secure-Communication(Verify Certificates): Feature in Guardium ensuring communication integrity through certificate validation and protocol verification
Server-Certificate-Validation(Verify Certificates): Process to validate server-side certificates during SSL/TLS handshake in Guardium components
Splunk(Search Processing Language): Data analytics platform; Guardium integrates with Splunk for SIEM capabilities
S-TAP-Server-Certificate(Verify Certificates): Definition of the certificate used by the S-TAP agent on database servers for SSL/TLS communications
Tcp-Intercepted-Ports(Number Sign): Configuration setting defining TCP ports intercepted by various Guardium agents for traffic monitoring
UI(User Interface): Web-based interface for administering Guardium installations
VDB(Virtual Database): Logical data source in Guardium representing multiple physical databases
Vulnerability Discovery(Vulnerability): Guardium module scanning database systems for misconfigurations and vulnerabilities

Aggregator(Guardium Aggregator): Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.

AuditLog(Audit Logging Options): Options for configuring and managing database audit logs within IBM Guardium.

CAS(Change Audit System): Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

Collector(Guardium Collector): Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

DatabaseTAP(Oracle Example): Specific implementation of Guardium TAP technology for monitoring Oracle database traffic.

FAM(File Activity Monitoring): Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

GuardAPILibrary(GuardAPI Syntax): Library of Guardium's RESTful API functions, including endpoints and parameter specifications.

HostSpec(Host Specification): Parameter defining the target host for API execution, using a managed unit or central manager identifier.

K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

RiskSpot(Risk Spotter): Guardium feature that identifies and assesses potential risks in database activity.

S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## IBM Guardium Components

- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **Aggregator**: Appliance consolidating data from multiple Collectors.
- **CAS**: Module detecting changes to schemas, procedures, and objects.
- **Collector**: Appliance receiving, processing, and storing activity data.
- **FAM**: Module monitoring access to unstructured data files.
- **GDPR**: Regulation ensuring personal data protection; Guardium supports compliance.
- **GIM**: Tool deploying, upgrading, and managing S-TAP agents remotely.
- **K-TAP**: Kernel module intercepting OS-level database socket traffic.
- **S-GATE**: Enforces real-time access policies, blocking or masking unauthorized queries.
- **S-TAP**: Agent capturing and forwarding database traffic to a Collector.

## Parameters and Features

- **api_target_host**: Target host for API execution (hostname or IP).
- **GDP_HOSTNAME**: FQDN of SSL certificate for secure server connections.
- **DNS**: Service discovery DNS name identifying Guardium services.
- **ELK**: Integrated log management platform for centralized analysis.
- **FIM**: Module monitoring file system integrity and unauthorized access.
- **HDFS**: Extended monitoring for Hadoop Distributed File System.
- **IAM**: Integration with identity and access management systems.
- **Immuta**: Integration for dynamic data masking and governance.
- **SQL Query Shaping**: Real-time query transformation for compliance.
- **rds_instance_id**: Identifier for AWS RDS instances.

## Identifier of an AWS RDS instance monitored by Guardium for access control and auditing

## S-Auditor(Structured Auditing)
Guardium component that captures, normalizes, and stores SQL audit records from supported database engines.

## S-Filter(API Rate Limiting)
Feature within S-GATE enabling fine-grained throttling of database client application connections.

## SQL-Shaping-Policy
Predefined set of rules applied by S-GATE to transform SQL queries based on context, security posture, and compliance needs.

## SSL(Transport Layer Security)
Encryption protocol; guarded database traffic is monitored via decrypted inspection without breaking SSL.

## Slow Query
Database query exceeding defined latency thresholds; Guardium logs and alerts on slow queries with potential performance or injection risks.

## stap_status_listener
Process responsible for monitoring S-TAP agent status, capturing run-time metrics, and forwarding health data to the collector.

## synthetic_user_guest
Placeholder user identity used by Guardium during service account interactions to capture audit data without exposing real credentials.

## syslog_facility_audit
Configuration setting that directs Guardium audit logs to the operating system's audit facility for compliance and correlation with OS events.

## transactionAbortion_detected
Feature identifying and flagging incomplete or aborted database transactions for investigation in fraud detection or data integrity use cases.

## v10_3(FreeMarker Template Language)
Guardium uses FTL version 10.3 for dynamically generating data visualization templates in activity reports.

## whitewall_rule
Guardium rule configuration that suppresses (white-lists) specific queries or database activity deemed normal or safe.

## sse_implementation
Guardium's software-based security enclave running in user space rather than kernel space for enhanced visibility and policy enforcement.

## guardium_v11_upgrade_tool
CLI utility provided in Guardium V11 to prepare legacy systems for in-place upgrade processes.

## Managed File Transfer (MFT)
Guardium offers file activity monitoring extensions for MFT platforms like IBM Sterling, ensuring compliance visibility across file-based data pipelines.

## A-TAP(Appliance TAP)
IBM Guardium software module that monitors traffic on physical database appliances without requiring kernel changes.

## Appliance
Self-contained Guardium hardware or virtual machine designed for specific data protection functions.

## BOP(Business Object Processing)
Guardium feature that analyzes business logic and relationships in database queries for risk assessment.

## CAS(Change Audit System)
Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

## Collector
Guardium appliance responsible for receiving, parsing, and storing monitored database activity data from S-TAP agents.

## DLP(Data Leak Prevention)
Guardium module focused on detecting sensitive data movement across databases and applications.

## FAM(File Activity Monitoring)
Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

## Guardium
IBM's enterprise data security platform that provides database activity monitoring, vulnerability assessment, and compliance capabilities.

## HDFS(Hadoop Distributed File System)
Distributed storage system supported by Guardium for monitoring access to Hadoop data.

## Hive
Guardium's ability to monitor SQL-like queries executed against Hadoop's Hive data warehouse system.

## HSM(Hierarchical Storage Management)
Guardium's support for monitoring data movement between primary and secondary storage systems.

## Integer
Whole numbers supported by Guardium's policy rule conditions and alerts.

## JDBC(Java Database Connectivity)
Standard Java API supported by Guardium for intercepting database connections in Java applications.

## Kerberos
Network authentication protocol supported by Guardium for secure database access monitoring.

## Netezza(ERTA/Netezza)
Guardium's monitoring capabilities for IBM Netezza data warehouse appliances.

## OAuth
Guardium's support for monitoring API traffic authenticated using the OAuth protocol.

## OpenSSL
Cryptographic library supported by Guardium for encrypting database connections (e.g., SSL/TLS).

## Oracle(Oracle Database)
Primary relational database management system (RDBMS) supported by Guardium for comprehensive activity monitoring.

## PCAP(Packet Capture)
Packet capture format used by Guardium for storing and analyzing network traffic data.

## PGP(Pretty Good Privacy)
Encryption standard supported by Guardium for securing database links through data masking and tokenization.

## PKI(Public Key Infrastructure)
Guardium's ability to integrate with enterprise PKI systems for certificate management and SSL deployment.

## PostgreSQL(PostgreSQL)
Open-source relational database supported by Guardium for monitoring SQL-level database activity.

## Redshift
Amazon Web Services (AWS) data warehousing service supported by Guardium for monitoring data queries and access.

## Schema
Logical database structure monitored by Guardium for detecting unauthorized modifications or access.

## SFTP(Secure File Transfer Protocol)
Guardium's support for monitoring encrypted file transfers that may contain sensitive data.

## SSL/TLS
Cryptographic protocols monitored by Guardium for encrypting database connections and API traffic.

## Sybase(Sybase ASE)
Supported relational database brand monitored by Guardium for transaction logging and access control.

## TAP
General term referring to Guardium's monitoring points that intercept database protocol traffic.

unstructured data files on NAS, SharePoint, and similar storage.  
GDPR(General Data Protection Regulation): EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.  
GIM(Guardium Installation Manager): Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
HCX(Hybrid Cloud Extension): VMware service that simplifies workload migrations and extensions between on-premises data centers and cloud environments.  
Informix(Informix Dynamic Server): IBM's high-performance, scalable relational database for OLTP and mixed workloads, supporting multiple instances.  
K-TAP(Kernel TAP): Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.  
P-PCI(Payment Card Industry): Set of security standards designed to ensure that companies that accept, process, store, or transmit credit card information maintain a secure environment; Guardium helps achieve PCI compliance.  
S-GATE(Software Gate): Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.  
S-TAP(Software TAP): IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

## Guardium Overview

### Core Components
- **S-TAP**: Captures and forwards database traffic to a Guardium Collector.
- **K-TAP**: Linux kernel module that intercepts OS-level database socket traffic.
- **S-GATE**: Enforces real-time access policies and blocks/masks unauthorized queries.
- **GIM**: Centralized tool for remote deployment, upgrades, and management of S-TAP agents.

### Data Protection & Compliance
- **GDPR**: Supports compliance with EU data protection regulations via discovery, masking, and audit trails.
- **DPPM**: Provides data‑loss‑prevention capabilities and privacy compliance tools.
- **PBKDF2**: Secure password hashing algorithm used by Guardium.

### Deployment & Integration
- **Cloud Support**: Compatible with AWS, Azure, GCP, and Kubernetes (CRDs, CSI, CNI, ISTIO).
- **KMS & HSM**: Manages encryption keys for data‑at‑rest protection.
- **CI/CD**: Integrates with AWS services like EC2, S3, SES, and IAM roles.

### Monitoring & Access Control
- **File Activity Monitoring**: Detects unauthorized file changes and configuration modifications.
- **RBAC**: Controls user permissions based on roles.
- **MFA**: Enforces multi‑factor authentication for privileged access.

### Performance & Management
- **Autoscaling**: Uses AWS ASG to adjust Guardium collector capacity.
- **SSD & Storage**: Optimized for high‑performance storage solutions (NFS, LV, CNS).
- **TTM**: Aims to reduce time‑to‑market for security deployments.

## Install Namespace #####
Set `INSTALL_NAMESPACE=va-scanner` so all Helm commands target the correct Kubernetes namespace.

## Report Titles #####
9c8da0a5-271f-4d60-b9e3-609685499bea – categories: knowledge
473d35d0-6b62-4716-b9ea-8f2e1203b99c – categories: features, keywords
84f09df7-dd39-49d8-b234-da9e5d292b92 – categories: knowledge
886dc3c1-6fd6-4bb4-ad55-2eb0d4f5d341 – categories: knowledge
a6e42f99-8d05-49f2-8ef3-2d7c6eb0512a – categories: knowledge, features
5f77e9e5-d537-4864-bddb-10aa6c89dc30 – categories: keywords, knowledge
e88b427b-5ccc-4683-896a-8a7946943a8b – categories: keywords
e1a86228-2339-4368-bc9b-9b8dd4205f78 – categories: entities, keywords, knowledge
a9ad8e96-1099-4dfd-b29a-6bda777b88bb – categories: knowledge, features
ee7d7877-0fd0-4c67-a7cf-fbab64f23f85 – categories: keywords

## Guardium Components #####
A-TAP – intercepts local application calls on DB servers.
Aggregator – consolidates activity data from collectors.
CAS – detects schema, proc, config changes.
Collector – receives, processes, stores activity data.
FAM – monitors access to NAS/SharePoint files.
GDPR – supports EU personal data protection laws.
GIM – remote deployment/management of S‑TAP agents.
K‑TAP – Linux kernel module for socket traffic interception.
S‑GATE – enforces real‑time access policies.
S‑TAP – captures and forwards DB traffic.
access_manager – defines data‑access permissions.
API – external integration for automation.
audit_process – collects, aggregates, stores audit data.
Central_Manager – oversees collectors and provides unified view.
DB2_ASM – monitors DB2 storage management.
E‑DB – high‑performance, Guardium‑protected databases.
encryption – protects data at rest and in transit.
FIM – monitors system‑file integrity.
FIM – monitors system‑file integrity (duplicate).

## IBM Guardium Overview
### Core Components
- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **Collector**: Receives, processes, and stores activity data from S-TAP agents.
- **GuardAPI**: CLI and REST API for automation and data retrieval.
- **Guardium Assurance Program**: Certification for compliance and security.
- **policyInspection**: Analyzes security policies for conflicts and non-compliance.
- **nativeSQL**: API parameter for raw SQL queries.

### Security Features
- **DirectPass**: Protocol for forwarding S-TAP traffic without proxies.
- **passwordlessAuth**: Authentication using tokens or certificates instead of passwords.
- **secure_sql**: Configuration to enhance SQL operation security.
- **Oauth**: Standard for access delegation to user accounts on HTTP services.

### Compliance & Regulation
- **GDPR**: EU regulation supported via discovery, masking, and audit trails.
- **MACOSX**: Monitoring and auditing file activities on macOS.
- **NIST**: Standards and guidelines followed for robust security postures.

### Database Integration
- **MongoDB**: NoSQL database support for real-time monitoring.
- **policies**: Predefined rules and conditions for data access and monitoring.

### Monitoring & Management
- **FAM**: Monitors access to unstructured data files on NAS and SharePoint.
- **QUICK_SQL**: Configuration setting for optimizing SQL query handling.
- **SAP**: Comprehensive monitoring and security for SAP environments.
- **REST**: Web service protocol for simplified interaction with Guardium services.

### Architecture
- **Aggregator**: Centralizes activity data from multiple Collectors.
- **DistributedScan**: Parallel scanning technique for databases.
- **log_collector**: Aggregates system and security event logs for analysis.

### Operating System Support
- **Windows**: Comprehensive monitoring and data protection across Windows environments.
- **zOS**: Guardium solution for IBM mainframe environments.

### Incident Management
- **REIM**: Feature focused on incident management and rapid security alert response.

## Guardium Components and Features

### Core Components
**Appliance(Guardium Appliance)**: Dedicated hardware or virtual device running the Guardium software suite for data collection, aggregation, and analysis.  
**Collector2(Guardium Collector)**: Appliance that receives, processes, and stores database activity data from S-TAP agents.  
**S-GATE(Software Gate)**: Enforces real-time database access policies, blocking or masking unauthorized queries.  
**S-TAP(Software TAP)**: IBM Guardium agent on database servers that captures and forwards traffic to a Collector.  
**App(TAP)(Application TAP)**: Kernel-level agent intercepting local database calls directly on the server.

### Security and Authentication
**Auth(Multi-Factor Authentication API2)**: API for configuring two-factor authentication for user access.  
**Cert(SSL Certificate)**: Digital certificate for secure encrypted connections between Guardium components.  
**Kerberos(Authentication)**: Supported authentication protocol using tickets for secure node communication.

### Data and Monitoring
**scanengine(Scan Engine)**: Module for executing database vulnerability and configuration assessments.  
**Class(Classification)**: Assigns categories to data identifying sensitive information based on rules and patterns.  
**File(File Monitoring)**: Tracks file access or manipulation events for auditing unstructured data usage.  
**Intelligence(Threat Intelligence)**: Assesses risk by correlating activity data with sources to identify threats.

### API and Integration
**RESTAPI(REST API)**: Web-based protocol for interacting with Guardium services using HTTP methods and JSON.  
**Sma(Sma)**: Microservice handling specific functional areas like policy enforcement or data collection.  
**Conn(Database Connection)**: Communication link between Guardium components and database servers for data collection.  
**Filter(Query Filter)**: Criteria to narrow down query results based on attributes like time, user, or activity type.

### Configuration and Management
**Config(Parameter)**: Adjustable settings for customizing Guardium behavior, such as report settings or security policies.  
**Composite(Parameter)**: Combines multiple attributes or conditions into a single API query or operation.  
**Data(Retention Policy)**: Setting defining how long audit data is retained for compliance and administration.  
**Group(User Group)**: Collection of users with common roles and permissions for streamlined management and access control.

### Descriptive Tags and Parameters
**Label(Parameter)**: Descriptive tag for categorizing or organizing data, policies, or reports.  
**Key(Parameter)**: Identifier for specifying or authenticating API requests.  
**Hour(Parameter)**: Refines reports or queries to a specific hour of the day.  
**Userpassword(userpassword)**: API parameter for providing credentials to authenticate with Guardium services.

## Log2
A file that records all actions, errors, and warnings performed by Guardium components, essential for monitoring system health and troubleshooting.

## Mask
A security feature in Guardium that hides sensitive data from unauthorized views while allowing administrators to decrypt it when necessary.

## Network
Defines the network settings within Guardium, such as IP addresses, ports, and protocols for communication between components.

## NonStop
A feature in Guardium that ensures uninterrupted audit and monitoring of database activity without breaks.

## Object
A specific element within a database, such as tables, procedures, or views, that Guardium can monitor and report on for security and compliance.

## Obj
A general term for any item within Guardium's data model, which can include data sources, reports, or configurations.

## OMNI
A feature that enables Guardium to collect and monitor database activity from various platforms and cloud services under a single interface.

## Param
An input value required by a Guardium API to execute a function, such as specifying the name of a database or the type of report.

## Plan
A structured approach defined within Guardium to ensure organizational policies and data handling practices meet regulatory and industry standards.

## Policy2
A defined set of rules within Guardium that dictates how data access should be monitored, controlled, and reported to ensure security and compliance.

## Profile
A configuration set within Guardium that defines how data should be collected from specific data sources.

## Prog
Refers to the execution of scripts or software routines within Guardium for automated tasks, such as compliance checks or data imports.

## Query1
The process of requesting specific data from a database through Guardium, often to generate reports or alerts based on specific criteria.

## Recon
The process of comparing data between different Guardium components to ensure consistency and accuracy across the system.

## Repl
The copying of data or configurations between Guardium components to ensure redundancy and availability of data.

## Req
A request initiated by users or systems to execute a specific action or retrieve information from Guardium, such as running a report.

## Resp
The output returned by Guardium following an API call or command, containing the requested data or confirmation of the action taken.

## RestAPI
The interface through which external systems interact with Guardium, enabling functions like configuration updates and data retrieval.

## Restore
A process within Guardium to recover lost or corrupted data by restoring from a backup copy of the system or database.

## Role
A predefined set of permissions within Guardium that grants users the ability to perform specific actions or access certain information.

## ROT13
An encryption method occasionally used in Guardium to obfuscate data temporarily, often for testing or educational purposes.

## Sample
A subset of data used to test Guardium policies and configurations before applying them to production environments.

## Schedule
A predefined timetable within Guardium that dictates when certain actions or reports should run, automating routine tasks.

## Search
The ability to find specific entries or activities within Guardium's collected data using keywords, filters, or advanced queries.

## Secure
The practice of converting information into a code to prevent unauthorized access, especially during data transmission within Guardium.

## Select
The action of choosing a specific report template or dataset to be generated or exported within Guardium.

## Session
A period during which a user interacts with Guardium, including activities like logging in, running queries, and viewing reports.

## Set
A group of parameters or values passed together to a Guardium function to perform a complex action, like configuring multiple policy settings at once.

## Srv
A reference to a database or application server monitored by Guardium, providing data about its activity and access.

## SSL
A protocol used by Guardium to establish encrypted connections, ensuring that data transferred between components is secure.

## STAP
IBM Guardium Software TAP Agent: The software agent installed on database servers that captures and forwards database traffic to a Collector.

## Summary
An overview of key insights or findings from a Guardium report, providing a high-level view of data security or compliance status.

## Tenant
A security feature in multi-tenant environments where each client’s data and configurations in Guardium are logically separated.

## Terminology
A term used within Guardium documentation or interfaces to describe functions, components, or features related to data protection.

## Theme
The visual design scheme applied to the Guardium user interface, which can be customized for branding or accessibility.

## Time
A temporal attribute used in Guardium APIs to filter or format reports based on specific dates or time ranges.

## Tix
The combination of alerts, reports, and notifications generated by Guardium to inform users of activities, threats, or compliance issues.

## Token
An authentication credential used by Guardium APIs to authorize access to endpoints and ensure secure API interactions.

## Trace
A detailed logging mode in Guardium that captures extensive data about operations and performance for in-depth analysis.

## Trigger
A condition or event within Guardium that, when detected, automatically initiates predefined actions such as alerts.

## Guardium Components

**Universal Connector API**: Manages external system integration, collecting data from various sources into Guardium.

**User**: An account that performs tasks ranging from reporting to configuration management within Guardium.

**Violation**: Detected when data access or manipulation breaches defined policies, flagged for review.

**Application Whitelisting**: Security feature that permits only predefined applications to access databases, blocking all others.

**Workflow**: Series of automated steps within Guardium for processes like data classification or compliance reporting.

**Export**: Data can be exported from Guardium in XML format for transferable representations of reports or logs.

## Guardium Storage & Management

**Short Term Archive (ATS)**: Temporary storage tier for recent activity data before long-term archiving.

**Authorization Failure Threshold**: Locks user accounts after a specified number of failed authorization attempts.

**Azure Storage Account**: Credential identifier for accessing Microsoft Azure storage services used by Guardium.

**Built-in Aggregator**: Default Appliance role for initial data processing before forwarding to a central Aggregator.

**Cache Expiration Period**: Duration after which cached query results are invalidated and recomputed.

**Central Repository Status**: Shows whether configuration settings' central repository is active and synchronized.

## Communication & Security

**CSV Output Format**: Option to export report data for downstream processing in comma-separated values format.

**DB Role Mapping**: Maps database roles to Guardium user roles to enforce least privilege access controls.

**Deployment Mode**: Determines whether Guardium is deployed in a standalone or centralized architecture.

**Distributed Search Mode**: Enables cross-Apolla query execution for federated searches across multiple Collector appliances.

**Email Notification List**: List of email addresses receiving alerts and reports generated by Guardium.

**UTF-8 Encoding Format**: Character encoding for data exchange between Guardium components, supporting internationalization.

**Engagement Score**: Numeric value representing user interaction frequency with Guardium reports, used in workflow prioritization.

**Escalation Limit**: Maximum failed login attempts before escalating to a security administrator.

## Resource Allocation & Monitoring

**Hugepage**: System resource allocation setting for high-performance workloads.

**File Permission Mask**: Controls default permissions for files created by Guardium processes.

**Heartbeat Interval**: Frequency at which database clients send status updates to the Guardium Collector.

**High Priority Rule**: Ensures specific security policies are evaluated before others in the processing queue.

**HSM Host**: Network address of the Hardware Security Module storing encryption keys for database credentials.

**Session Timeout Period**: Duration of inactivity after which user sessions are automatically terminated for security.

## Authentication & Automation

**Single Sign On**: Authentication method allowing users to access Guardium using external identity provider credentials.

**Split Query Max Px Count**: Maximum parallel query execution threads for large query distribution.

**SSH Public Key**: Public key for authenticating administrative access to Guardium appliances without password use.

**Stored Procedure Pattern**: Regular expression for identifying stored procedures of interest for monitoring activity.

**SYSLOG Server**: Network host receiving log messages from Guardium for external SIEM integration.

**Token Validity**: Length of time an authentication token remains valid before renewal.

**Validation Interval**: Time between successive checks of database connectivity health.

**Vulnerability Assessment Schedule**: Cron expression defining when automated vulnerability scans are executed.

**Web UI Timeout**: Session inactivity period after which the Guardium Web UI logs out the user for security.

## Key Guardium Modules

**Application TAP (A-TAP)**: Kernel-level agent intercepting local application database calls on the database server.

**Guardium Aggregator**: Appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.

**Change Audit System (CAS)**: Module detecting and recording changes to database schemas, stored procedures, and object configurations.

**Guardium Collector**: Appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

**File Activity Monitoring (FAM)**: Module monitoring and recording access to unstructured data files on NAS, SharePoint, etc.

**GDPR**: EU regulation requiring personal data protection; Guardium supports compliance via discovery, masking, and audit trails.

**Guardium Installation Manager (GIM)**: Tool for remote deployment, upgrading, and managing S-TAP agents across database servers.

**Ke...**

## Kernel Monitoring

A-TAP: Kernel-level agent intercepting local application calls directly on the database server.  
K-TAP: Linux kernel module intercepting OS-level socket traffic on the database server for Guardium monitoring.

## Data Collection

Collector: Appliance receiving, processing, and storing database activity forwarded by S-TAP agents.  
Aggregator: Appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.  

## Policy Enforcement

S-GATE: Component enforcing real-time database access policies, blocking or masking unauthorized queries.

## Discovery and Management

Auto-Discovery Process: Systematic method locating and registering databases and file storage.  
auto-discover-hadoop: Auto-discovery task type identifying Hadoop instances.  
auto-discover-datalakes: Auto-discovery task type identifying data lakes.  
auto_discovery_task_type: Defines nature of auto-discovery tasks (e.g., auto-discover-hadoop).  

GIM: Centralized tool deploying, upgrading, and managing S-TAP agents remotely.  

## User and Activity Monitoring

DB_USER: OS-to-database account mappings maintained via `list_db_user_mapping`.  
FAM: Module monitoring access to unstructured data files on NAS, SharePoint, etc.  

## Configuration and Assessment

RDS: Integration extending native monitoring to Amazon RDS databases.  
CAS: Detects and records schema, stored procedure, and object configuration changes.  
metadata: Descriptive information about database objects used by Guardium assessments.  

## Risk and Compliance

risk_score: Numeric severity of anomalous behavior or policy violations.  
risk_score_threshold: Determines when alerts or actions trigger based on risk scores.  
risk_encode: Standardizes risk scores for reporting and alerts.  

## Reporting and Visualization

Guardium Search: Built-in functionality finding policies, reports, or settings.  
guarspotlight: Dashboard displaying real-time activity and compliance status.  
Spotlight Dashboard: Customizable view of health, performance, and risk levels.  

## Data Export and Integration

prot_export_gsb: Exports protocol-specific logs for advanced analysis.  
prot_list: Shows supported database protocols Guardium can monitor.  
prot_load_module: Loads specific protocol modules for monitoring different databases.  

## Utility and Diagnostics

guarddrill: Automated assessment and reporting application.  
sanity_check: Diagnostic test ensuring all Guardium components function correctly.  

## User Mappings and API

`list_db_user_mapping`: GuardAPI retrieving OS-to-database user mappings.  
`list_param_mapping_for_function`: Returns parameter mappings for specific API endpoints.  
`list_tasks_for_auto_discovery`: REST API endpoint retrieving auto-discovery scheduled tasks.

# Guardium Glossary (Compressed)

## Core Components
**Application‑App**: Guardium UI for alerts, reports, and assessments.  
**A-TAP**: Kernel‑level agent intercepting DB calls.  
**Abac**: Attribute‑based access control.  
**Access‑Admin role**: Manages users, roles, authentication.  
**Admin role**: Full privileges for configuration and policies.  

## Authentication & Integration
**ADFS**: SSO via REST API.  
**Alias credential**: Alternate login without exposing real credentials.  
**Id‑Vault**: Encrypted credential store.  
**Identity‑Provider**: LDAP, AD, SAML integration.  

## Data Handling & Security
**Encrypted‑Password**: Runtime‑decrypted passwords.  
**In‑Line Enforcement**: Real‑time SQL blocking by S‑TAP.  
**Insight‑DB**: Embedded analytics for anomaly detection.  
**Key‑Store / Key‑Vault**: Secure key and secret management.  
**Control‑Policy**: Real‑time security enforcement rules.  

## Discovery & Management
**Discover**: Scans network for data sources.  
**Discover Data Sources**: Automatic data source detection.  
**GIM**: Remote agent deployment & validation.  
**Uninstaller Log**: Records of removed agents/software.  

## Reporting & Auditing
**Adhoc query**: One‑off user‑initiated queries logged for audit.  
**Audit workflow**: Automated enforcement tasks triggered by violations.  
**Command History**: Record of CLI/UI actions for forensic use.  
**Event Stream**: Continuous security‑event feed to analytics.  

## Monitoring & Performance
**Blade**: Physical host for S‑TAP installation.  
**BYOD**: Policy for personal devices accessing corporate DBs.  
**Client‑IP**: Source IP in API requests.  
**Connection Pool**: Shared DB connections monitored by Guardium.  
**DB‑User**: Application database account used for connections.  

## Security Models
**Ability‑Based Access Control (Abac)**: Rights based on user attributes.  
**Fail‑Open**: Allows traffic if rules cannot be enforced.  
**Gatekeeper (not listed)**: *N/A*  

## External Integrations
**ArcSight**: SIEM platform for alert ingestion.  
**Enterprise APM**: Feeds performance metrics to APM tools.  
**ArcSight integration**: Alerts fed to SIEM.  

## Configurations & Options
**Default Password**: Initial common password for new users.  
**Discover Data Sources**: Scans for target DBs.  
**DSN Name**: ODBC/JDBC identifier for data sources.  
**Legacy Mode**: Compatibility flag for older drivers.  
**Listen Port**: Network port for DB listener traffic.  

## Miscellaneous
**Guardium Rate (G‑Rate)**: Rate of activity records processed.  
**Host Header**: Routes web‑service requests.  
**JSON API**: REST interface returning JSON.  
**Policy‑Distribution Manager (GIM)**: Centralized agent management.

## Log Retention
Policy specifying how long activity records are kept on the collector before archiving or deletion.

## Lookup Table
Static reference data (e.g., IP‑to‑region mapping) that Guardium policies can reference for dynamic decisions.

## Masked View
Database view that dynamically obscures sensitive column values based on Guardium masking policies.

## Meta Tag
User‑defined label attached to a data source or object to enable policy grouping and reporting.

## MongoDB Atlas
Cloud database service supported by Guardium’s native connector for monitoring and masking.

## Network Protocol
Parameter specifying the database communication protocol (e.g., TCP/IP, SSL) monitored by S‑TAP.

## Network Segment
Subnet or VLAN range used by Guardium policies to apply rules selectively.

## Non‑Production
Tag applied to environments (dev, test) indicating that activity data should be handled differently (e.g., less stringent enforcement).

## Node Host
Hostname used by Guardium components for internal communication, independent of IP mode.

## Object Level
Granular permission control in Guardium policies targeting individual tables, views, or stored procedures.

## One‑Time Token
Short‑lived credential generated by Guardium UI for temporary API authentication.

## OS User
Captured username from the operating system side of database connections; used in session classification.

## Passphrase
Longer string than a password used for client authentication to Guardium services (e.g., API client secret).

## Peer Group
Logical collection of data sources sharing similar security requirements, managed together in Guardium policies.

## Policy Exception
Rule that overrides a standard control policy for specific users, hosts, or time windows.

## Policy Scope
Definition of the data source, user, and resource set a Guardium rule applies to.

## Query Plan
Execution strategy the database optimizer generates; Guardium can collect and analyze these plans for performance forensics.

## Raw Log
Unprocessed activity record exported from Guardium for external correlation or archival.

## Reconcile Users
Guardium operation that synchronizes user accounts between the appliance and external identity stores.

## Revocable Credential
Credential type that can be invalidated or regenerated without redeploying agents.

## Rotate Key
Periodic process in Guardium to replace encryption keys protecting stored activity data.

## Self Service Portal
Web interface allowing end users to view their own activity summaries and request access changes.

## Service Account
Dedicated non‑human user account created for integration tools; often granted limited Guardium permissions.

## Session ID
Unique identifier assigned by Guardium to each monitored database session for correlation across collectors.

## Sharding‑Aware
Guardium feature that tracks distributed queries across multiple database shards.

## Single Point of Failure (SPOF)
Risk assessment term; Guardium mitigates SPOF by distributing collectors and aggregators geographically.

## SSL Offload
Configuration where TLS termination is handled outside Guardium (e.g., by a load balancer) before traffic reaches the collector.

## Stop List
List of database objects or commands that Guardium automatically excludes from monitoring or policy evaluation.

## Sudo User
Non‑root account granted privileged access via sudo; Guardium can log the original OS user when sudo is employed.

## Syslog
Standard protocol for forwarding log messages; Guardium integrates with syslog servers for centralized logging.

## Target Host
Parameter in Guardium APIs defining the collector or aggregator receiving the request.

## TLS Version
Supported encryption protocol version (e.g., TLS 1.2, TLS 1.3) configured for secure Guardium communications.

## Transaction Window
Time‑bounded period during which Guardium evaluates policy actions; used for “time‑based” access controls.

## User Group
Collection of user accounts in Guardium sharing the same roles and policy permissions.

## Virtual Host
Domain name resolved to multiple backend servers; Guardium can monitor per‑host activity independently.

## Window Size
Configuration parameter for TCP packet analysis in S‑TAP, balancing performance and capture depth.

## Alerts per Exception (AP)
Tracks how often specific exceptions are triggered across the database environment.

## Application TAP (A‑TAP)
IBM Guardium kernel‑level agent that intercepts database calls made by local applications directly on the database server.

## CA siteMinder
Web access management solution that integrates with Guardium for unified identity and access control.

## Certificate Administrative UI
Web‑based interface within Guardium for managing SSL certificates used by Guardium components.

## Change Database Password (GuardAPI)
GuardAPI command that allows DBAs to programmatically change the password of a database user account.

## Dex API
Interface allowing external applications to interact with specific Guardium search and query functionalities.

## DISA STIG
Defense Information Systems Agency Security Technical Implementation Guide; compliance standard partially supported by Guardium.

## Domain Name
Alphanumeric hostname that uniquely identifies a computer or set of services within DNS.

## Enable Reverse DNS Resolution
Parameter that instructs Guardium to resolve IP addresses to hostnames for richer reporting.

## Gdm Decryptor
Guardium component that handles encryption and decryption for secure data transmission.

## Hierarchical Recursive Queries
SQL queries that include subqueries referencing themselves, supported by advanced Guardium data analysis.

A-TAP(Application TAP): Kernel-level agent intercepting database calls by local applications on the server.
Aggregator: Consolidates activity data from multiple Collectors for enterprise reporting.
CAS: Detects and records changes to database schemas, stored procedures, and configurations.
Collector: Receives, processes, and stores database activity data from S-TAP agents.
FAM: Monitors and records access to unstructured data files on NAS and similar storage.
GDPR: EU regulation for protecting personal data; Guardium supports compliance through discovery, masking, and audit trails.
GIM: Remote deployment and management of S-TAP agents on database servers.
K-TAP: Linux kernel module intercepting OS-level database socket traffic for monitoring.
S-GATE: Enforces real-time database access policies, blocking or masking unauthorized queries.
S-TAP: Software agent capturing and forwarding database traffic to a Guardium Collector.
Unified Connector: Enables data ingestion from SaaS and cloud sources into Guardium for unified discovery and classification.
acquisitionTimeStamp: Timestamp when resource data was acquired (PerfMon Resource).
archivePostProcessorName: Name of the post-processor applied during data archiving (Parameter).
awssh: AWS Secure Shell storage metric (PerfMon Resource).
awsuserCpu: Percentage of CPU used by user processes (PerfMon Resource).

## REST API Parameter Types
- **bool**: Boolean parameter type for API input fields.
- **Integer**: Integer parameter types such as `bootIndex`, `clientProcessId`, and `health-analyzer-resync-count`.
- **String**: String parameter types including `clientApplicationName`, `clientBatchType`, `encryptedPassword`, `format`, and `host`.
- **DataSource**: Data source parameter for API calls targeting specific data.

## Backup Configuration Parameter
- **clearOnChange**: Backup configuration parameter specifying deletion of old data upon change.

## VM Injector Parameter
- **host**: Host system attribute specifying the target host for operations.

## Thread Pool Processor
- **inventoryDataManager**: Specialized thread for managing Guardium configuration inventories.

## PerfMon Resources
- **ipmi**: Intelligent Platform Management Interface hardware monitoring metric.
- **javaUsedHeap**: Memory usage metric for Java heap spaces.
- **javaUsedNonHeap**: Non-heap memory consumption by Java processes.
- **kafkaReplicaLagTime**: Replication delay measurement for Kafka messaging systems.
- **memory**: General memory usage metric for performance monitoring.
- **numOfDiskReads**: Count of disk read operations performed.

## Size Parameters
- **max**: Maximum value constraint for size-related parameters.
- **min**: Minimum value constraint for size-related parameters.

## File System Metric
- **netVsiz**: Network file system size metric.

## Guardium Health Analyzer Metrics
- **analyze-interval**: Interval between health analysis executions.
- **audit-cycle**: Cycle frequency for audit evaluation in health analysis.
- **clean-suspicious-interval**: Interval for clearing suspicious events in health analysis.
- **cluster-resync-waited**: Wait time for cluster resynchronization in health analysis.
- **clusternode-delayed-upsert**: Delayed data upsert latency in clustered health analysis.
- **cpu-usage**: CPU usage monitor in Guardium Health Analyzer.
- **cpu-usage-background**: Background GPU usage metrics for health analysis.
- **disk-io**: Disk I/O metric monitored by Guardium Health Analyzer.
- **disk-usage**: Disk space usage tracking for health evaluation.
- **endpoint-name**: Named endpoint configuration in Health Analyzer.
- **first-clustered-run**: Initial run indicator for clustered health evaluations.
- **heartbeat**: Health monitoring heartbeat signal for system status checks.
- **infocomm-msg**: Informational messages generated during health analysis operations.
- **job-policy**: Policy definitions for scheduled health analysis jobs.
- **job-status**: Status indicator for currently running or scheduled health jobs.
- **memory-usage**: Memory consumption metrics captured by Health Analyzer.
- **node-health**: Health status of individual nodes within a Guardium cluster.
- **resync-count**: Count of resynchronization events during health data consolidation.
- **sql-compile-latency**: Time taken to compile SQL statements in health analysis reports.
- **sql-exec-latency**: Execution latency for SQL statements monitored by health analysis tools.
- **table-eviction**: Frequency and conditions for eviction of unused database tables.
- **table-hitrate**: Hit rate metric indicating table utilization within health analysis.
- **table-lifetime**: Retention period of tables during health evaluation processes.
- **total-mem**: Total memory resources allocated for health analysis operations.
- **wait-io**: I/O wait times measured during health monitoring activities.
- **wait-lock**: Lock wait durations recorded during health analysis operations.
- **wait-proc**: Processor wait times captured in health monitoring metrics.
- **wait-rcache**: Cache read wait times logged in health analysis data.

## Additional Metrics
- **clientBatchType**: Parameter defining the batch type of the client request.
- **clientProcessId**: Process ID parameter identifying the client process.

## Guardium Architecture
- **A-TAP**: Kernel-level agent that intercepts local application calls on the database server.
- **Aggregator**: Central appliance that consolidates activity data from multiple Collectors, enabling enterprise-wide reporting.
- **CAS**: Module that detects and records changes to database schemas, stored procedures, and object configurations.
- **Collector**: Appliance that receives, processes, and stores activity data forwarded by S-TAP agents.
- **FAM**: Module for monitoring and recording access to unstructured data files on NAS and similar storage.
- **S-GATE**: Enforces real-time access policies, blocking or masking unauthorized queries.
- **S-TAP**: Software agent installed on database servers that captures traffic and forwards it to a Collector.

## Data Protection and Compliance
- **GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.
- **Guardium Risk Management Features**: Identify risky users, track policy violations, and spot risks using watchlists and risk spots.

## Management Tools and APIs
- **GIM**: Tool for remote deployment, upgrade, and management of S-TAP agents across database servers.
- **K-TAP**: Linux kernel module for intercepting OS-level database socket traffic on Linux systems.
- **ListColdStorageMaintenanceConfig**: Command to list cold storage maintenance configurations from version 12.2.1 onward.
- **PUT_METHOD**: HTTP method used for updating classifier document rules via REST API.
- **ProxyAPI**: Manages proxy services via REST or GuardAPI commands for operations like setup and reload.

## Cloud and Compute
- **Analyzer**: Reads data from various sources for Unified Discovery and Classification in cloud environments.
- **AutoscaleSettings**: Configurations for autoscaling virtual machine scale sets in Azure.

## Enterprise-Wide Reporting
- **CAS(Change Audit System)**: Detects and records changes to database schemas, stored procedures, and configurations.
- **Collector(Guardium Collector)**: Receives, processes, and stores database activity data from S-TAP agents.
- **Feature Flags(various)**: Enable or disable experimental features and custom workflows.
- **GDPR(General Data Protection Regulation)**: Supports compliance with EU data protection requirements through discovery, masking, and audit trails.
- **GIM(Guardium Installation Manager)**: Centralized tool for deploying, upgrading, and managing S-TAP agents.
- **K-TAP(Kernel TAP)**: Linux kernel module intercepts OS-level database socket traffic.
- **S-GATE(Software Gate)**: Enforces real-time database access policies and blocks or masks unauthorized queries.
- **S-TAP(Software TAP)**: Captures and forwards database traffic to a Guardium Collector.

## Additional Topics
- **api_target_host(parameter)**: Specifies the target host(s) for Guardium API commands.
- **Base64(ASCII PEM)**: Encoding format for certificate files exported from Guardium.
- **Guardium Data Fabric**: Manages data across hybrid environments.
- **Hadoop(cloud data)**: Configurations for monitoring Hadoop clusters.
- **HTTP (client Offsets)**: Configures database client connection parameters for optimal performance.
- **keywords(database interception)**: Technologies for capturing and analyzing database session data.
- **Managed Units(Clusters)**: Individual database servers or applications monitored by Guardium.
- **parameter(default values)**: Preset settings that can be overridden by user configuration.
- **procedural steps(certificate)**: Workflow for exporting certificates in PEM format.
- **SQL errors(Anomaly Detection)**: Reports for detecting and reporting SQL errors.
- **UNIX(operating systems)**: Monitoring features for UNIX environments.
- **Windows(environment)**: Guardium support for Windows platforms.

## Guardium Overview
Guardium is IBM's database activity monitoring and data security platform. It provides real-time monitoring, threat detection, and compliance reporting.

## Components
- **K-TAP**: Linux kernel module that intercepts OS-level database socket traffic for Guardium monitoring.
- **S-TAP**: Software agent installed on database servers, capturing and forwarding database traffic to a Guardium Collector.
- **S-GATE**: Enforces real-time database access policies, blocking or masking unauthorized queries.
- **UC**: Enables Guardium to ingest and process logs and events from various non-database sources.

## Parameters and Concepts
- **api_target_host**: Specifies the target host for executing API commands in distributed environments.
- **auto_gather_data**: Controls whether system data is automatically gathered during classification.
- **central_manager**: Primary Guardium appliance in a distributed setup, managing other appliances and enforcing policies.
- **description_based_group**: Group defined by a descriptive name rather than a numeric ID.
- **enable_logging**: Activates detailed logging for troubleshooting and auditing.
- **guardium_agent**: General term for software components monitoring database activities.
- **host_name**: Specifies the hostname of a database server or Guardium appliance.
- **kernel_module**: Software module extending the Linux kernel's capabilities, such as K-TAP.
- **login_source**: Specifies the source from which a user logs into Guardium.
- **managed_units**: Group of Guardium appliances managed collectively by a central manager.
- **role_based_access**: Security mechanism controlling user permissions based on defined roles.

## API
IBM Guardium provides a REST API for web service interactions. API calls include:
- `ipToAliasSelected`: Indicates whether an IP address should be resolved to its alias.
- `S-TAP_STATUS`: Checks the operational status of the S-TAP agent.
- `classifier_gather_data`: Determines if the classifier process gathers system data.
- `performance_profile`: Optimizes system performance by adjusting resource usage.
- `policy_violation`: Event triggered when a database access request does not comply with policies.
- `query_monitoring`: Continuously monitors database queries to detect anomalies.

ACCELERATOR(IBM z Systems Accelerator): Enhances database performance by offloading query processing to specialized hardware.
ACL_LUA(Access Control List Lua): Enables dynamic policy creation using Lua scripts for fine-grained database access control.
ACTIVE_ACTIVE_CLUSTER(Guardium Active-Active Cluster): Provides high availability through synchronized data replication across two Guardium appliances.
AI_INSIGHTS(Guardium AI Insights): Utilizes machine learning to detect anomalous database activity and potential threats.
ALERTER(ALERTER Service): Sends notifications based on predefined or custom alert conditions set within Guardium.
ANALYTICS_ENGINE(Analytics Engine): Analyzes database activity data for reporting, compliance metrics, and actionable insights.
API_KEY(Guardium API Key): Secures RESTful API access, ensuring only authorized clients can invoke services.
ARCHIVE_IN_PROGRESS(Guardium Archive in Progress): Indicates ongoing processing of data files for export or long-term storage.
ASYNC_MODE(Asynchronous Processing Mode): Allows Guardium to run data collection and analysis tasks in parallel without blocking other operations.
AUDIT_DATA_AUDIT(Audit Data Audit): Ensures the integrity, completeness, and compliance of audit data collected by Guardium.
AUTO_REFRESH(Auto-Refresh Interval): Frequency at which Guardium dashboards and reports automatically refresh with fresh data.
AUTH_INTERFACE(Authorization Interface): Validates and enforces user permissions for database access within Guardium.
BACKUP_CONFIG_FILE(Backup Configuration File Path): Specifies the location of configuration backup files for system recovery purposes.
BASH_SCRIPT(Bash Script Execution): Supports execution of custom Bash scripts for database monitoring and compliance tasks.
BATCH_MODE(Batch Processing Mode): Processes audits or exports in large batches for improved efficiency and reduced system load.
BERLIN_MODE(Berlin Mode): Optimizes Guardium deployment for German language interfaces and compliance requirements.
BINARY_LOG_PARSER(Binary Log Parser): Parses binary log files from databases to extract actionable security insights.
BIND_INTERFACE(BIND Network Interface): Configures network interfaces for Guardium to listen for incoming S-TAP agent data.
BLOCKED_QUERIES_COUNT(Blocked Queries Count): Tracks the number of SQL queries blocked by access control policies in Guardium.
BRUTE_FORCE_DETECTION(Brute Force Detection): Alerts on malicious access attempts through repeated login attempts.
CACHE_POLICY(Cache Policy Configuration): Determines how Guardium caches frequently accessed data to enhance performance.
CHANGE_SIGNIFICANCE_LEVEL(Change Significance Level): Sets thresholds for considering database changes significant for audit purposes.
CLIENT_TLS_CERTIFICATE(Client TLS Certificate): Encrypts traffic between clients and Guardium's REST API using digital certificates.
COMMAND_CENTER(Command Center): Centralized management console for orchestrating security policies and audits across Guardium appliances.
COMPATIBILITY_MODE(Compatibility Mode): Enables Guardium to operate with older versions of databases or operating systems.
CONFIG_FILE_PATH(Configuration File Path): Defines the storage location of critical configuration settings on Guardium systems.
CONNECTION_MONITOR(Connection Monitor Service): Monitors real-time status and performance of database connections within Guardium.
CONTAINERIZED_DEPLOYMENT(Containerized Deployment): Deploys Guardium services using container technologies like Docker for scalability and isolation.
CONTEXT_AWARE_ACCESS_CONTROL(Context-Aware Access Control): Adapts database access permissions based on contextual factors like user location or access time.
DATA_MASKING_RULE(Data Masking Rule Definition): Controls how sensitive data is obscured or redacted in reports and logs.
DATABASE_CHANGE_HISTORY(Database Change History Table): Logs schema modifications, including additions, deletions, and alterations to database structures.
DATABASE_USER_GROUP(Database User Group): Facilitates simplified management of permissions and audit policies for grouped database users.
DATA_DISCOVERY_ENGINE(Data Discovery Engine): Scans data repositories to identify and classify sensitive information according to policies.
DEFAULT_DBA_ROLE(Default DBA Role): Preconfigured role for standard database administrator tasks within Guardium.

## Guardium Concepts

### Authorization and Roles
Database administrators are assigned specific permissions to manage database security.

### Reporting Modes
**Delta Reporting Mode**: Logs only changes since the last report, reducing storage needs.

### Deployment Specifications
**Deployment Type Specification**: Uses identifiers like *Standalone* or *Distributed* to adapt Guardium's operational mode.

### Policy Frameworks
**Detection Policy Framework**: Defines logic and criteria for identifying security anomalies.

### Alert Management
**Duplicate Alarm Suppression**: Prevents multiple alerts for the same event within a set timeframe.

### Diagnostic Parameters
**Dump File Location**: Specifies where Guardium generates dump files for troubleshooting.

### Operational Modes
**Eager Mode**: Prioritizes data analysis tasks to reduce latency.

### Data Integration
**Elasticsearch Cluster**: Distributed setup for storing and searching security logs.

### Credential Security
**Encrypted Password**: Stored in an encrypted format to protect credentials.

### Event Analysis
**Event Correlation Engine**: Correlates disparate events to detect compromise patterns.

### Reporting
**Exception Report**: Highlights policy-violating activities or access attempts.

### External Integration
**External Audit Trigger**: Initiates audits based on external system triggers.

### Authentication Monitoring
**Failed Authentication Attempts**: Logs count of failed login attempts.

### Federated Architecture
**Guardium Federation Gateway**: Facilitates secure data sharing across Guardium environments.

### Auditing
**Fine-Grained Auditing**: Audits specific actions on database objects based on detailed criteria.

### Network Security
**Firewall Rule Configuration**: Controls traffic based on source, destination, and protocol.

### Compliance Verification
**Formal Verification Process**: Automated checks verify database configuration correctness.

### Fraud Detection
**Fraud Detective Module**: Uses analytics to detect fraudulent transactions.

### System State
**Full Backup State**: Complete backup of configurations, audit data, and settings.

### Alert Severity
**Fuzzy Logic Engine**: Rates severity of security alerts using fuzzy logic.

### Audit Overview
**Global Audit Status**: Displays collective audit status across all instances.

### Data Querying
**GraphQL API Support**: Enables flexible data retrieval through GraphQL queries.

### User Management
**Group Membership Manager**: Manages user group memberships from directory services.

### Connection Handling
**Handshake Timeout Setting**: Defines maximum wait time for successful S-TAP handshakes.

### Operational Oversight
**Health Check Module**: Periodically checks operational health of connections and applications.

### Power Management
**Hibernate Mode**: Minimizes background processes to conserve resources.

### High Availability
**High Availability Mode**: Ensures continuous operation through redundancy and failover.

### API Configuration
**API Target Host**: Specifies target host(s) for API execution.

### Data Platform Support
**Big Data Platform**: Monitors and protects Hadoop and NoSQL datasets.

### System Coordination
**Central Manager**: Coordinates and controls managed units in Guardium.

### Command Interaction
**CLI**: Command Line Interface for text-based Guardium interaction.

### Data Access
**Datasource Credentials**: Securely stores credentials for data source access.

### Output Formatting
**Flag Terse**: Modifies command output to be more concise.

### Policy Definitions
**Guardium Compliance Policies**: Predefined and customizable policies for regulatory adherence.

### Data Protection Suite
**Guardium Data Protection**: IBM's platform providing database monitoring, vulnerability assessment, and encryption.

### Logical Grouping
**Guardium Group**: Logically groups appliances for simplified administration.

### Automation API
**GuardAPI**: API for automating tasks, data retrieval, and configuration management.

### On-Demand Scans
**Guardium Inspector**: Performs on-demand data scans and reports via CLI.

### Local Accounts
**Local User**: User accounts defined directly on Guardium appliances.

### Appliance Roles
**Managed Unit**: Guardium appliances under central manager control.

### Monitoring Policies
**Monitoring Policy**: Defines what database activity is monitored.

### Network Configuration
**Network Mode**: Configures network settings for Guardium appliances.

### On-Demand Assessment
Guardium feature using GuardAPI to run immediate security scans on demand.

### Process Level Monitoring
Monitor database activity at the application and process level for detailed tracking.

### Purge
Operation to permanently delete data from the Guardium repository, freeing storage.

### Reporting API
Guardium interface for programmatically generating and retrieving audit reports.

### Response Cache
Mechanism to temporarily store API responses, improving performance.

### Schema Discovery
Automated process that identifies and catalogs database structures.

### Sendfile
Secure file transfer protocol used within Guardium.

### SSL Cert Trust Store Path
Location on Guardium appliances where trusted SSL certificates are stored.

### Stop Solr
GuardAPI command to halt Solr indexing services.

### Token
Security artifact for authenticating API requests or sessions.

### Unique Rule Name
Policy rules must have distinct names to prevent conflicts.

### Upload
Action of transferring files or data to a Guardium appliance.

### Validate
Command to verify the correctness of configurations or data formats.

### View Adhoc
Functionality to create and run temporary custom database activity views.

## Guardium Components

**A-TAP**: IBM Guardium kernel-level agent intercepting database calls made by local applications directly on the database server.

**Aggregator**: Guardium appliance consolidating activity data from multiple Collectors for enterprise-wide reporting.

**Catalog Manager**: UI component managing catalog entities such as catalogs, schemas, tables, views.

**CAS**: Guardium module detecting and recording changes to database schemas, stored procedures, and object configurations.

**Collector**: Guardium appliance receiving, processing, and storing database activity data forwarded by S-TAP agents.

**Custom Parameter**: User-defined variable configuring Guardium features or integrations.

**Data Domain**: Logical grouping of data objects in Guardium for classification and access control.

**Data Steward**: Role responsible for overseeing data quality, metadata, and governance in Guardium.

**FAM**: Guardium component monitoring file access on databases, NAS, and SharePoint.

**GCN**: Syntax format for GuardAPI commands and options.

**Global Group**: Guardium entity aggregating users or assets across multiple domains.

**Header Authentication**: Method of identity verification using HTTP headers.

**Infrared Alert**: Guardium notification mechanism using physical indicators or devices.

**INQUA Query**: Advanced query in Guardium's INQUA analyzer for pattern detection.

**Kernel Inspection Tool**: Software package inspecting kernel-level database interactions.

**Log Manager**: Guardium role handling log data storage, retention, and archiving.

**mySQL Database**: Open-source relational database supported by Guardium.

**Oracle Database**: Relational database system supported by Guardium.

**Performance Accelerator**: Guardium feature optimizing data retrieval and analysis speed.

**Policy Information Term Aggregator**: Compiled view of applicable policies for an object.

**Privilege Manager**: Guardium role overseeing data access permissions.

**Process Snapshot**: One-time capture of Guardium process statistics for diagnostics.

**Query Snapshot**: Preservation of query results at a specific point in time.

**RAinder**: Logical grouping of databases or servers for centralized management.

**REP**: Predefined set of SQL queries and reports for data analysis.

## Visualizations in Guardium

### Architectural Style and Protocols
- **REST (Representational State Transfer)**: Architectural style for communicating with Guardium services via HTTP.
- **SAML (Security Assertion Markup Language)**: Standard for exchanging authentication data between Guardium and identity providers.
- **SCIM (System for Cross-domain Identity Management)**: Protocol for automating user provisioning in Guardium.
- **Secure Shell (SSH)**: Network protocol for secure data exchange with Guardium instances.

### Security and Compliance
- **Revocation Verification**: Guardium process confirming the invalidation of compromised credentials.
- **WLAN (Wireless Local Area Network)**: Network technology requiring monitoring by Guardium's wireless security controls.
- **EU GDPR (General Data Protection Regulation)**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

### Components and Tools
- **API Target Host**: Specifies where an IBM Guardium API runs, accepting values all_managed, all, and group:<name>.
- **Archive File Path**: Parameter in Guardium Utilities that indicates the path to archive files for database backups or migrations.
- **CAS (Change Audit System)**: Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.
- **Collector**: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.
- **GIM (Guardium Installation Manager)**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
- **K-TAP**: Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.
- **License Key**: Unique cryptographic code enabling Guardium features, controlling scalability and feature access.

### Monitoring and Performance
- **SQL (Structured Query Language)**: Language for interacting with databases monitored by Guardium.
- **Throttle Query Execution**: Preventing overloading by restricting query rates in Guardium.
- **TRE (Timestamped Report Element)**: Component of Guardium reports with timestamped information.
- **Urchin User Interface**: Web-based GUI for managing Guardium features and settings.
- **VPC (Virtual Private Cloud)**: Isolated network environment in cloud infrastructure for Guardium deployment.
- **XML Output**: Extensible markup format for exporting data from Guardium.

### Maintenance and Administration
- **Rollback Security Rules**: Reverting Guardium policies to prior states.
- **Swirl Analytics**: Guardium component analyzing repeated patterns in database activity.
- **Table Masking**: Process concealing sensitive data within table output while preserving structure.
- **Uyp (Upon Y-technology)**: Turkish term for "Upon Y-technology," used within local documentation.
- **Whitebox Testing**: Comprehensive testing approach involving Guardium internals.
- **XYP Credential**: Enhanced credential type for secure authentication in Guardium.

## Monitoring Application Processes

Specify the application processes for targeted monitoring.

## Processing Approach

Set whether Guardium inspects traffic in real-time or in batches.

## Protocols

Supported database protocols include Oracle, MySQL, and MSSQL.

## Query Rewrite

Guardium feature that modifies queries for compliance.

## Query Rewrite Condition

Rule defining criteria for applying query rewrites.

## Query Rewrite Expression

New query definition after a rewrite condition is met.

## Query Rewrite Internal ID

Unique identifier for managing query rewrite operations.

## RAW Request

Captured unprocessed database requests for analysis.

## RDB Names

List of relational databases targeted by Guardium operations.

## Request Source

Origin of database requests, such as specific users or applications.

## Report Builder

Guardium UI tool for designing custom reports.

## Report Title

Identifier for reports within the Guardium platform.

## Request Causer

Source or reason for abnormal database activity.

## Sensitive Object

Flagged database objects containing high-value data for enhanced monitoring.

## Server CPU

CPU of the physical server hosting the Guardium Collector.

## Server Memory

Total installed RAM on the Guardium Collector infrastructure.

## Sensor Protocol

Protocol used by Guardium sensors when forwarding data.

## Template

Predefined configuration for rapid S-TAP or policy deployment.

## Timer Interval

Configurable pause in milliseconds between Guardium reporting cycles.

## Tune Interval

Setting that adjusts the frequency of performance tuning activities.

## Type Field

Classification of queried data type crucial for AQL parsing.

## Update Policy

Command to modify existing Guardium security or monitoring policies.

## Upload Path

Directory location where Guardium stores uploaded files.

## User Filter

Condition restricting monitoring scope to specific user accounts.

## Validation Validation

Test confirming the integrity of Guardium policies, S-TAP configurations, or connections.

## Whitelist

Exclusion list that ignores specified activities or users during monitoring.

## Shared Secret

Authentication string between the central manager and managed units.

## Stap Host

Parameter specifying the S-TAP host for data collection revocation or ignore.

## Unified Discovery and Classification

IBM product offering data discovery and classification for structured and unstructured data.

## Version 1.1

Latest release of Unified Discovery and Classification with new features and enhancements.

## API Target Host

Guardium unit executing API requests, accepting IP addresses or hostnames.

## Entity

Component within the Guardium system such as managed units, collectors, or S-TAP.

## Feature

Distinct functionality provided by Guardium like vulnerability assessment or activity monitoring.

## Keyword

Search term for finding information in documentation or data sources.

## Managed Unit

Guardium system managed by a central manager for centralized data collection.

## Central Manager

Guardium appliance orchestrating data collection across multiple managed units.

## Default Value

Initial setting applied when no explicit value is provided for a parameter.

## Release Notes

Document detailing product version changes, improvements, and fixes.

## Privileges

Authorizations for users or roles to perform actions on database objects.

## GUI

Graphical user interface for interacting with Guardium features and configurations.

## A-TAP

Kernel-level agent intercepting database calls made by local applications.

## Aggregator

Guardium appliance consolidating activity data from multiple Collectors.

## CAS

Guardium module for detecting and recording changes to database configurations.

## Collector

Guardium appliance receiving, processing, and storing database activity data.

## GIM

Centralized tool for deploying, upgrading, and managing S-TAP agents.

## Guardium API REST Service

Web interface for interacting with Guardium programmatically using REST.

## Guardium Cloud Platform

Infrastructure for deploying Guardium services in public clouds.

## Guardium Insider Threat

Feature set for monitoring insider threats and data exfiltration attempts.

## Guardium PQM

Methodology and tools supporting governance, risk assessment, and compliance for Guardium.

## MongoDB Connector

Official plug-in extending Guardium support to MongoDB deployments.

# Guardium Components and Features

## Security Protocols
- **MongoDB SSL**: Encrypts traffic between MongoDB instances and Guardium agents.

## Database Architectures
- **PDB**: Oracle multitenant component for individual monitoring by Guardium.

## Access Enforcement
- **S-GATE**: Enforces real-time database access policies, blocks/masks unauthorized queries.
- **SGATE-LIGHT**: Simplified S-GATE for resource-limited environments.
- **SGATE-XL**: Enhanced S-GATE with complex policy support and high throughput.

## Web Activity
- **WAM**: Records user actions and security events in web-based database applications.

## API Parameters
- **api_target_host**: Host name or IP for API commands (Collector, Central Manager, Managed Unit).
- **api_user**: Authenticated user executing Guardium API requests.

## Automation
- **auto_discovery_process**: Automatically detects and registers new database instances (requires process_name parameter).

## Metadata
- **categories**: Tags for classifying Guardium components or functionality.
- **custom_property**: User-defined attributes for extended tracking or reporting.

## Compliance
- **data_compliance_status**: Indicator for enabled data compliance features.

## Purging Operations
- **default_purge_batch_size**: Pre-configured batch size for data purging (modifiable via API).
- **purge_batch_size**: Number of records processed per iteration in data deletion jobs.
- **purge_job_schedule**: Schedule for automatic data purging jobs.

## Filtering
- **query_string**: Text filter for narrowing API results by query patterns or error messages.

## Real-Time Analysis
- **real_time_analysis**: Processes and evaluates database activity in real-time.

## Data Sources
- **shared_datasource**: Accessible by multiple applications or user groups.

## Diagnostic Tools
- **support_tool**: Provides diagnostics, log collection, and configuration auditing for Guardium.

## Monitoring Techniques
- **A-TAP**: Kernel-level agent intercepting local application database calls.
- **FAM**: Monitors access to unstructured data files on NAS and similar storage.
- **GIM**: Centralized tool for Guardium software management across servers.
- **K-TAP**: Linux kernel module capturing OS-level database traffic.
- **S-TAP**: Captures and forwards database traffic to Guardium Collector.

## Database Support
- **Netezza**: Supported for monitoring privileged user activities and enforcing access controls.

## General Knowledge
- **CIDR**: IP address allocation and routing method used in Guardium.
- **GDPR**: EU regulation supported by Guardium for personal data protection.
- **GIM**: Centralized web interface for Guardium software installation and maintenance.

Analyzer: Service account that reads file systems and data stores to enable the Unified Discovery and Classification cloud analyzer to identify data types and sensitivities.

api_target_host: Parameter that specifies the target host name or IP address for the API execution.

CAS: Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.

Collector: Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

Data-Masking: Guardium feature that dynamically obscures sensitive data values returned to applications in real time.

FAM: Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

GDPR: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

GIM: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

kernel TAP: Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

Ranger: Apache open-source framework that provides centralized security administration for Apache Hadoop ecosystems.

REST API: Application programming interface that enables interaction with Guardium services using HTTP requests.

S-GATE: Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

S-TAP: IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

Vault-Integration: Guardium capability that integrates with external key management systems to protect encryption keys.

## Guardium Core Components

**Asset**: Entity holding sensitive data that Guardium monitors for vulnerabilities and compliance.  
**Auth (Single Sign-On)**: User logs in once to access multiple applications, supported by Guardium for streamlined security management.  
**CAS (Change Audit System)**: Logs schema changes, configuration updates, and object modifications to maintain audit trails and detect unauthorized alterations.  
**Collector**: Appliance that receives, stores, and processes data from S-TAP agents, centralizing activity logs for analysis.  
**Def (Definition)**: Predefined set of rules or configurations in Guardium, such as a sensitivity scan or data classification policy.  
**Group**: Collection of managed units or collectors that facilitates centralized control and configuration management.  

## Data Protection Features

**FAM (File Activity Monitoring)**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.  
**Guardium Data Protection**: Comprehensive solution by IBM with data discovery, classification, access control, and monitoring capabilities.  

## Installation and Deployment

**GIM (Guardium Installation Manager)**: Tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.  
**K-TAP (Kernel TAP)**: Linux kernel module that intercepts OS-level database socket traffic for low-overhead Guardium monitoring.  

## Policy Enforcement and Monitoring

**Insights_Push**: API call to securely transmit Guardium data to the Insights platform for analysis and reporting.  
**S-GATE (Real-Time Policy Enforcement)**: Enforces real-time database access policies and blocks or masks unauthorized queries.  
**S-TAP (Software TAP)**: Software agent on database servers that captures and forwards database traffic to a Guardium Collector.  

## Security and Compliance

**GDPR**: EU regulation for protecting personal data; Guardium supports compliance via discovery, masking, and audit trails.  
**Remote Shell**: Configuration parameter that controls whether Guardium agents use secure shell connections for communication.  

## Monitoring and Alerts

**Response Time Threshold**: Configuration setting that defines the maximum acceptable response time for database queries before alerting or blocking.  
**Universal Deployment Model**: Flexible Guardium architecture enabling deployment across diverse database environments and platforms.  



```markdown
## Guardium Core Components

### Asset
Entity holding sensitive data that Guardium monitors for vulnerabilities and compliance.

### Auth (Single Sign-On)
User logs in once to access multiple applications, supported by Guardium for streamlined security management.

### CAS (Change Audit System)
Logs schema changes, configuration updates, and object modifications to maintain audit trails and detect unauthorized alterations.

### Collector
Appliance that receives, stores, and processes data from S-TAP agents, centralizing activity logs for analysis.

### Def (Definition)
Predefined set of rules or configurations in Guardium, such as a sensitivity scan or data classification policy.

### Group
Collection of managed units or collectors that facilitates centralized control and configuration management.

## Data Protection Features

### FAM (File Activity Monitoring)
Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

### Guardium Data Protection
Comprehensive solution with data discovery, classification, access control, and monitoring capabilities.

## Installation and Deployment

### GIM (Guardium Installation Manager)
Tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

### K-TAP (Kernel TAP)
Linux kernel module that intercepts OS-level database socket traffic for low-overhead Guardium monitoring.

## Policy Enforcement and Monitoring

### Insights_Push
API call to securely transmit Guardium data to the Insights platform for analysis and reporting.

### S-GATE (Real-Time Policy Enforcement)
Enforces real-time database access policies and blocks or masks unauthorized queries.

### S-TAP (Software TAP)
Software agent on database servers that captures and forwards database traffic to a Guardium Collector.

## Security and Compliance

### GDPR
EU regulation for protecting personal data; Guardium supports compliance via discovery, masking, and audit trails.

### Remote Shell
Configuration parameter that controls whether Guardium agents use secure shell connections for communication.

## Monitoring and Alerts

### Response Time Threshold
Configuration setting that defines the maximum acceptable response time for database queries before alerting or blocking.

### Universal Deployment Model
Flexible Guardium architecture enabling deployment across diverse database environments and platforms.
```

## Terms and Concepts in IBM Guardium

**Login (SSO)**: Guardium's single-point login allows seamless user access across services with one authentication instance.

**Managed (Managed Units)**: Guardium entities controlled by a Central Manager ensure synchronized configurations and aggregated reporting.

**Port**: The specific network port used by Guardium components like S-TAP and Collectors for data transmission, essential for firewall configuration and connectivity.

**Radius Regex**: Regular expression feature in Guardium for complex string pattern matching, particularly useful in advanced classification and filtering.

**Regex**: Short for Regular Expression, enabling precise data filtering, masking, and search criteria within policies and reports.

**S-GATE (Software Gate)**: Real-time feature that blocks or masks queries based on policy violations to enhance data protection.

**S-TAP (Software TAP)**: An agent-based module capturing and forwarding transactional data to Collectors for monitoring or masking.

**SSL**: Supports Secure Sockets Layer encryption to protect data-in-transit between agents, collectors, and appliances, ensuring secure communications.

**CAS (Change Audit System)**: Detects and records changes to database schemas, stored procedures, and object configurations.

**Collector (Guardium Collector)**: Appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.

**File Activity Monitoring**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage systems.

**GIM (Guardium Installation Manager)**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

**GuardAPI**: Interface for programmatically performing administrative tasks and retrieving data in Guardium.

**Guardium Kernel Driver (GKMD)**: Part of the K-TAP framework residing in kernel space to capture database traffic for monitoring.

**api_target_host**: Specifies target hosts for API execution on the central manager, managed units, or groups of managed units.

**File Activity Module**: Provides detailed monitoring of file access activities within the FAM module.

**A-TAP (Application TAP)**: Intercepts database calls made by local applications directly on the database server.

**Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.

**GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance via discovery, masking, and audit trails.

**Policy**: Set of rules defining legitimate database activities, triggering alerts or actions on violations.

**SSL**: Cryptographic protocol securing communications between Guardium components, protecting data in transit.

## IBM Guardium Components
- **S-TAP**: IBM Guardium agent installed on database servers to capture and forward database traffic.
- **S-GATE**: Enforces real-time access policies and masks/blocks unauthorized queries.
- **K-TAP**: Kernel module for intercepting OS-level database traffic on Linux.
- **A-TAP**: Kernel agent intercepting database calls from local applications.
- **GIM**: Centralized tool for remote deployment and management of S-TAP agents.
- **Aggregator**: Central appliance consolidating activity data from multiple Collectors.
- **Collector**: Receives, processes, and stores activity data from S-TAP agents.
- **CAS**: Detects and records changes to database schemas, procedures, and configurations.
- **FAM**: Monitors access to unstructured data files on NAS, SharePoint, etc.

## Compliance and Security
- **GDPR**: EU regulation supported by Guardium through discovery, masking, and audit trails.

## APIs and Configuration
- **API**: Web service interface for interacting with Guardium using HTTP methods.
- **api_target_host**: Specifies target Guardium appliances for API execution.
- **classify_init**: API to initialize classification process.

## Guardium Overview

**ol_center**: Central appliance hosting all Guardium services.

**credential_deletion**: API used to remove client credentials from Guardium Data Encryption.

**crypto_sdk**: Library for transparent encryption and decryption before data transfer to Guardium.

**discover_api**: Enables setup of data sources and user credentials for data discovery.

**dm_manager**: Tool for managing DB2 data activities within Guardium.

**enhanced_profiler**: API to optimize data classification performance and sensitivity.

**entity_ranger_config**: Parameter specifying HDFS Entity Ranger service host location.

**error_detection**: Policy for identifying and reacting to unusual database activity.

**filemasking**: Feature protecting data at rest by masking sensitive information in non-production environments.

**filter_object_rule_data**: Parameter specifying new value for filter object in update_filter_object_rule_data API.

**hadoop_monitoring**: Guardium capability to monitor file access on Hadoop Distributed File Systems.

**key_vault_exchange_azure**: Feature integrating with Azure Key Vault to manage cryptographic keys.

**keystore_manager_api**: API for managing cryptographic keys stored in Guardium Data Encryption.

**ml_model_config**: Procedure for importing and configuring machine learning models in Guardium.

**password_management_api**: API for managing user credentials within Guardium Data Encryption.

**policy_mgmt_api**: API for modifying and deploying security policies in Guardium.

**re_image_api**: Parameter for replacing an image in the update_policy API.

**risk_manager_api**: API for managing risk assessment processes in Guardium Data Protection.

**safe_guard**: Policy defining safe query patterns for automated profiling.

**sql_stream_data**: API endpoint for streaming SQL queries for real-time analysis or logging.

**taint_based_monitoring**: Feature tracking data flow from sources to sinks for security auditing.

**test_parameters**: API for testing and validating configuration parameters in Guardium.

**token_authorization**: Authentication method requiring a bearer token in Guardium APIs.

**user_privilege_management**: Feature for administering user roles and permissions within Guardium Data Encryption.

**uuid_assignment**: API for assigning or modifying UUIDs associated with data sources or entities in Guardium Data Encryption.

## Guardium Features

**A-TAP API**: Interface for deploying and configuring Guardium's kernel-level agent.

**Activity Stream**: Audit trail of user and system actions logged for compliance and forensics.

**Alert**: Notification generated when a rule or policy is violated.

**App Group**: Logical container for organizing related database objects and assets.

**App Registration**: Configuration defining application-specific parameters for database connections.

**Attraction Area**: Policy construct defining commands or activities subject to specific controls.

**CC8C5B55-391A-482C-BEE0-BB577517B50E**: Unique identifier for a user permissions report in Slack.

**Cloud Accounts Page**: Portal for managing cloud service integrations in Guardium's UI.

**Confluence Account**: Atlassian platform monitored by Guardium for access auditing.

**Datenbankaufrufe**: Database calls intercepted by A-TAP (German).

**GIM Configuration**: Settings controlling S-TAP agent behavior within Guardium Installation Manager.

**Guardium Aggregator**: Central node receiving and aggregating monitoring data.

**Guardium Collector**: Process storing and managing audit data.

**Guardium Installation Manager**: Tool for remote deployment and updates of Guardium agents.

**HIPAA**: Regulatory standard supported by Guardium's policy and reporting features.

**IBM Guardium**: Brand name for the data security and compliance platform.

**Installierungsprozess**: German term for the installation process, often scripted in Guardium workflows.

**Kerberos**: Network authentication protocol supported by Guardium for secure communications.

**LLMNR**: Protocol sometimes monitored by Guardium.

**Managed Units**: Appliances collecting data and reporting to a central Aggregator.

**OAuth**: Authorization framework managed by Guardium APIs for secure API access.

**Onboard**: Initializing a new agent or collector in Guardium.

**PCI**: Payment Card Industry standards enforced by Guardium's policy and reporting features.

**Plug-In**: Extensible modules adding functionality, such as new database support.

**Policy Builder**: UI component for creating and editing policy rules.

**Report Title**: Identifier for a specific audit report or data extraction task.

**S-TAP Management**: Interface for deploying, monitoring, and troubleshooting S-TAP agents.

**Sensitive**: Classification level indicating high-risk data requiring protection.

**SSL**: Cryptography protocol supported by Guardium.

**Vulnerability Assessment**: Automated scan identifying vulnerabilities in the environment.

## Key Security Weaknesses
**Vulnerability Assessment**: Guardium's process for automatically discovering and reporting database security weaknesses.  
**Encryption Protocols**: Guardium supports SSL/TLS for secure communication between agents and collectors.  
**Privilege Management**: Authorization (privileges) granted to users/roles that enable specific database operations.

## Guardium Components

**A-TAP**: Guardium's kernel-level agent intercepts database calls from local applications on the database server.

**Aggregator**: Consolidates activity data from multiple Collectors for enterprise-wide reporting.

**CAS**: Detects and records changes to database schemas, stored procedures, and object configurations.

**Collector**: Receives, processes, and stores database activity data forwarded by S-TAP agents.

**Data Subject Rectification**: Updates personal data in the database to correct inaccuracies or incomplete information.

**Delete Audit Trails**: Audits actions taken to permanently remove personal data, ensuring compliance with deletion requests.

**FAM**: Monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.

**GDPR**: EU regulation requiring protection of personal data; Guardium supports compliance with discovery, masking, and audit trails.

**GIM**: Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

**K-TAP**: Linux kernel module intercepts OS-level database socket traffic for Guardium monitoring.

**POST**: HTTP method used by the IBM Guardium REST API for creating or modifying resources.

**REST API**: Web service interface for programmatically interacting with IBM Guardium using HTTP methods and JSON payloads.

**S-GATE**: Enforces real-time database access policies and blocks or masks unauthorized queries.

**S-TAP**: Software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.

**Subject Rights Enforcement**: Implements mechanisms to honor data subject rights such as access, rectification, and deletion.

**api_target_host (Execution Target)**: Hostname or IP address for API execution, including all, central manager, managed units, and groups.

**clientIp (Client IP)**: Mandatory parameter specifying the client's IP address originating the API request.

**lb-num-mus (Managed Units Count)**: Parameter indicating the number of managed units in deployment.

**use_discovery (Automatic Discovery)**: Installation flag that enables automatic discovery of databases during S-TAP deployment.

**job_queue (Job Execution Target)**: Parameter relevant when queuing jobs for execution on Guardium appliances.

## Guardium Overview

Guardium's job queue system enables queuing and managing jobs across its appliances. The network IP mode defines host specifier string formats and compatibility. IP Conformity ensures IP addresses or ranges match the configured IP mode. Hostnames serve as alternative identifiers for managed units during API execution. Managed units are Guardium appliances or agents installed on database servers to collect activity data. Schedules specify where jobs should run. The aggregator consolidates reports and data from collectors. Cancelling or removing jobs halts or deletes them from the queue. Scheduled job errors occur if servers are unreachable. Scans on non-responsive servers may fail. Guardium appliances execute jobs and cancellations. API role access controls who can manage jobs and features. Parameters like "file" are required for file uploads.

## Guardium Components

A-TAP intercepts local database calls on the server. The Aggregator consolidates data from collectors. CAS detects database changes. Collectors receive and store activity data. FAM monitors unstructured file access. GDPR compliance is supported. GIM manages S-TAP agents. GLBA assistance is provided. GOS refers to backup servers. K-TAP intercepts OS-level socket traffic. Kerberos enhances security. Kragen enables data discovery and policy enforcement. LogAPI accesses audit logs. OG Analyzer provides advanced analytics. Guardium can be restarted with the restart command. SGATE enforces access policies. S-TAP captures and forwards traffic. VA scans for vulnerabilities. The X-XSS-Protection header enables XSS filtering.

## Trails

### Guardium Installation Manager (GIM)

Centralized tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.

### K-TAP (Kernel TAP)

Linux kernel module loaded on the database server that intercepts OS-level database socket traffic for Guardium monitoring.

### S-GATE (Software Gate)

Guardium component that enforces real-time database access policies and blocks or masks unauthorized queries.

### S-TAP (Software TAP)

IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.