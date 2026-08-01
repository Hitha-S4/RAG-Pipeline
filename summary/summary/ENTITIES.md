# IBM Guardium Data Protection — ENTITIES

**Category:** entities  |  **Generated:** 2026-07-13  |  **Source:** gdp-12.x-documentation 2.pdf

---

Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

Policies & Rules

### Security Policy  
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

Databases & Datasources

### Guardium HostSTAP_SQLGUAR  
**Type:** database  
**Description:** Guards data within the SQLGUAR database on host HostSTAP using Guardium policies and auditing.

Credentials & Certificates

### Guardium HostSTAP_SQLGUAR  
**Type:** credential  
**Description:** Stores connection credentials for the SQLGUAR database on host HostSTAP to enable S‑TAP traffic capture.

APIs & Tools

### Parameter Value type Description  
**Type:** api  
**Description:** GuardAPI parameters for S‑TAP configuration include `connect_to_ip` (connection target), `db2_client_offset` (client offset), `db_install_dir` (installation directory), and `intercept_typ` (inspection type).

## Agents & Collectors

### S-TAP (Software TAP)  
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  

### Collector  
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.  

## Policies & Rules

### Security Policy  
*No meaningful content extracted.*  

## Databases & Datasources

### Teradata DB Entitlements  
Data Mart is a component that extracts data for efficient storage, preservation after purge, export from Guardium, and distributed reporting.  

## Credentials & Certificates

### store_sql_credentials  
Saves Oracle DB credentials for S-TAP connection.  

### guardctl  
*No meaningful content extracted.*  

## APIs & Tools

### GuardAPI  
Provides commands to identify and delete GIM bundles that are not in use, reducing disk space waste.  

### GIM  
Various methods to install the S-TAP client include using GIM, RPM, or shell installer, with auto-discovery enabled during installation capable of detecting databases and creating configurations.  

## Workflows & Procedures

### File Activity Monitoring (FAM) Activation  
The File Activity Monitoring feature requires that discovery and classification be enabled and the Investigation Dashboard be available.  

### S-TAP Installation and Activation  
After storing parameters with guardctl, activate A-TAP for a PostgreSQL or Greenplum instance by running guardctl --db-instance=<name> activate or the equivalent shell command with --db-instance, --db-type, and --db-home arguments.  

### Deploy Monitoring Agents  
Various methods to install the S-TAP client include using GIM, RPM, or shell installer, with auto-discovery enabled during installation capable of detecting databases and creating configurations.  

### Discover and Classification  
The File Activity Monitoring feature requires that discovery and classification be enabled and the Investigation Dashboard be available.  

## Features

### Setup  
After connecting a monitoring agent to Guardium, configure FAM for SharePoint by creating and installing a policy; note that the old configuration app is deprecated.

## Entities
### Smart Card Authentication
**Type:** entity
**Description:** Multi-factor authentication via a valid PIV or CAC smart card inserted into a card reader, optionally using the associated PIN.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent
**Description:** Lightweight software installed on database host servers to capture live SQL traffic and stream it to Guardium for policy enforcement, alerting, and audit storage.

### Collector
**Type:** appliance
**Description:** Dedicated Guardium hardware or virtual appliance that receives encrypted traffic from S-TAP agents, applies data‑security policies, aggregates audit records, and stores the final audit data in a tamper‑evident repository.

## Policies & Rules
### Security Policy
**Type:** policy
**Description:** Configurable rule set that determines how database traffic is handled based on user identity, object name, action type, etc., applying actions like allow, log, alert, or block.

## Databases & Data Sources
### Database
**Type:** database
**Description:** Structured data repository (e.g., Oracle, MySQL, SQL Server) protected by Guardium policies via S-TAP monitoring.

### External Datasource
**Type:** datasource
**Description:** User‑defined external system (file, API, or third‑party service) leveraged to import custom data into Guardium for group population or reporting enrichment.

## Credentials & Certificates
### Smart Card Certificate
**Type:** certificate
**Description:** Cryptographic certificate installed on a smart card that authenticates the user's identity to Guardium, enabling multi-factor login for privileged operations.

## APIs & Tools
### GuardAPI
**Type:** api
**Description:** Guardium's REST‑style command interface; `list_adhoc_policy_analyzer` allows administrators to run policy‑analysis queries against managed units by specifying optional `api_target_host`.

### guardctl
**Type:** tool
**Description:** Command‑line utility for managing Guardium agents (A-TAP) on database hosts. Full guardctl functionality in root mode; limited configuration, activation, deactivation, and instrumentation capabilities for designated database users.

## Infrastructure
### Managed Unit
**Type:** service
**Description:** Guardium‑managed server (physical or virtual) hosting S-TAP agents or serving as a Collector, grouped logically for batch administration, policy propagation, and audit data consolidation.

## Cloud Services
### Cloud Connector
**Type:** connector
**Description:** Guardium component that bridges on‑premises infrastructure with cloud data stores (AWS, Azure, GCP) to enable real‑time policy enforcement and audit collection for cloud databases and SaaS platforms.

pe:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

```markdown
## Appliance
A Guardium hardware or virtual appliance receives activity data from S‑TAP agents, applies security policies, and stores audit records.

## Security Policy
A configured rule set defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## S‑TAP (Software TAP)
A software agent installed on database servers captures traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

## Collector
A Guardium appliance that receives activity data from S‑TAP agents, applies security policies, and stores audit records.

## Grant Role to Object by ID
API `grant_role_to_object_by_id` assigns a role to an object using `objectId`, `objectTypeId`, and `roleId`.

## Policies & Rules
*Above snippets duplicate this heading; details already covered under “Security Policy.”*

## Databases & Data Sources
*No additional meaningful content extracted.*

## Agents & Collectors
*Above snippets duplicate this heading; details already covered under “S‑TAP” and “Collector.”*

## Parameter Default Meaning
*No meaningful description provided in source.*
```

## Credentials & Certificates

### Certificate
**Type:** certificate  
**Description:** Digital certificate used for securing communications, such as TLS certificates for encrypting data in transit between Guardium components.

### Credential
**Type:** credential  
**Description:** Stores authentication information required by Guardium processes to authenticate against external systems or services.

---

## APIs & Tools

### enable_special_attributes
**Type:** api  
**Description:** No specific description was extracted for this entry.

## Enable Special Attributes GuardAPI
Restores hidden attributes (e.g., Hive) for all users in Query‑Report Builder; execution displays “Hive … ok”.

### Enable Quick Search API
Enables quick‑search features via GuardAPI; requires a Boolean **all** parameter and takes effect on all managed units.

### Get Job Process Concurrency Limit API
GuardAPI feature that returns the current job‑process concurrency limit; the **api_target_host** parameter specifies the target host for execution.

### Discover Named and Description API
Saves a named classification scenario; optionally reuses or creates a new policy.

### Enforce Admin Access Separation Feature
Strict separation of duties: only the admin user can gain access‑manager capabilities after logging in.

### Delete Allowed DB by Entry ID API
Deletes a DB entry identified by **id** (Long, required) plus **instanceName**, **serverIp**, and **userName**; **api_target_host** defines execution hosts.

### Refresh Quick Search Groups API
Parameters target specific hosts for group synchronization.

### Revoke OAuth Token API
Revokes an OAuth token; requires a valid **token** and **api_target_host**.

### Merge Duplicate Group‑User Feature
If a group referenced by an exported definition already exists on the importing system, the imported definition’s group is skipped, which can cause confusion if the groups serve different purposes.

### API Target Host Parameter
Specifies execution targets for Guardium APIs; valid values are **all_managed**, **all**, **group:<group name>**, and **single**.

### Map SR Language Tool
Maps SR language parameters directly to UI counterparts; demonstrates constructing policies using session attributes like **CLIENT_IP** and **SERVER_IP**.

## Agents & Collectors

### S‑TAP (Software TAP)
Software agent installed on database servers that captures traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

### Collector
Guardium hardware or virtual appliance that receives activity data from S‑TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Databases & Datasources

### DB Default Users Enabled Domain
Named entity identified in source; detailed content not extracted.

## Credentials & Certificates

### API Target Host Parameter
Specifies execution targets for Guardium APIs; valid values are **all_managed**, **all**, **group:<group name>**, and **single**.

## APIs & Tools

### Restore Units After Bad Shift API
Restores Guardium units after a failed shift operation; details not extracted.

## Infrastructure

### External S‑TAP Feature
Feature related to remote S‑TAP deployment; details not extracted.

## Cloud Services

### PCI Accelerator Entity
Outlines twelve requirements focused on protecting infrastructure and implementing procedures.

## Groups

### Group Definition Configuration
Groups defined on the central manager and propagated to managed units for centralized management and uniform policy enforcement.

## Audit State

### Saved Data Entity Entity
Captures saved data for a monitored item, includes unique identifier, timestamp, and link to the Change Identifier entity.

## GuardAPI Syntax

### Universal Connector Reboot API
Reboots Universal Connector container from the latest UC image.

## GCP Services

### Required Permissions Entity
Lists detailed permissions (e.g., compute.autoscalers.get, compute.disks.create, iam, storage.buckets) required for the Unified Discovery and Classification engine to operate across GCP resources.

## SR Language

### Example Transformation Entity
Shows transforming an OS user, logging access for a specific DB user, and custom exception handling.

## Remote Loggers

### Syslog Configuration Entity
Enables Guardium to forward system messages via syslog to a remote receiver using the **store remotelog add** CLI; remote loggers are configured through this command.

## Parameter Values

### Requestor Identifier Entity
Used in Guardium REST APIs; identifies the caller (**requestorId**) and specifies execution targets (**api_target_host**).

### Target Specification Entity
Specifies execution targets for APIs; valid values include **all_managed**, **all**, and **group:<group name>**.

## From LDAP

### Group Import Limit Entity
Restricts group member import to a maximum of 5000 rows in IBM Knowledge Catalog versions 12.2.x and later when using Run Once Now.

## Attribute Description

### System Attributes Entity
*Description incomplete; no further details extracted.*

## Guardium Overview

### Mainframe Network Inspection
- The Guardium appliance can function as a z/OS network inspection appliance.
- Central manager capabilities are enabled.
- Network traffic inspection (netinsp) is enabled.

## Parameter Details

### Vulnerability Scanner Image
- **Type:** entity
- Specifies registry, repository, and tag parameters for retrieving the Docker image used by the vulnerability scanner.

## Services & Events

### CAS Service State
- **Type:** entity
- "Client Down" signifies the CAS service has halted on the database server host, necessitating diagnostics and service restart procedures.

### CAS Stopped Event
- **Type:** entity
- Indicates the CAS service has ceased monitoring on the database server host.

## Quality Gates
- G1 Complete sentences only; trimmed fragments.
- G2 Clean titles; descriptive noun phrases.
- G3 Nouns only; removed sentence fragments.
- G4 Merged duplicates; no repeat concepts.
- G5 Skipped noise; removed tables and placeholders.

## Compression
- Merged overlapping items (e.g., "Port number", "Proxy configuration parameters").
- Removed entries with only parameter lists or placeholders.
- Each description limited to 1-2 concise sentences.
- Removed header-only placeholders and repeated content.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S‑TAP agents, applies security policies, and stores audit records.

---

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

---

## Knowledge

### Security Vulnerability Definitions
**Type:** knowledge  
**Description:** Provides details for high‑risk database security issues, including classification, affected systems, CVSS scores, and remediation steps.

### Access by SAPUSER
**Type:** knowledge  
**Description:** Describes audit records for SAPUSER access, including user actions, timestamps, and associated objects.

## Overview

### S-TAP (Software TAP)
**Type:** agent  
**Description:** Captures database traffic on servers and forwards it to a Guardium collector for real‑time analysis, alerting, and policy enforcement.

### Collector
**Type:** appliance  
**Description:** A Guardium hardware or VM appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

---

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** Configures rule sets that define allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

---

## Data Sources & Databases

### AMDAHL // Amdahl data format
**Type:** database  
**Description:** Server Type entries (e.g., Dd2, Oracle, Teradata) paired with Service Names to identify Amdahl data source sessions in Guardium.

---

## Credentials & Certificates

### Attribute Description
**Type:** entity  
**Description:** The Scan Timestamp attribute preserves the original timezone of a scan, ensuring accurate temporal context across collectors.

---

## APIs & Tools

### 415. Guardium universal connector APIs
**Type:** api  
**Description:** `store_maximum_query_duration` configures the timeout for long queries/reports in seconds.

## Infrastructure

### HDFS poll
**Type:** infrastructure  
**Description:** Configurable parameters for HDFS polling include interval, port, user, audit history length, and interval for checking new Ranger audits.

## Cloud Services

### What to do next
**Type:** cloud service  
**Description:** After connecting a cloud provider account, view associated regions and discovered data stores on the Cloud Accounts page.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** Captures database traffic and forwards it to a Guardium Collector for analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** Receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Databases & Datasources

### DB2 Priv Summary
**Type:** feature  
**Description:** Reports DB2 and Sybase database privileges, object roles, sys privileges, public access, and admin roles.

### Databases Discovered Report
**Type:** feature  
**Description:** Lists discovered ports from the Auto-discovery process, each represented by a row.

### Import multiple databases
**Type:** feature  
**Description:** Import multiple database entries for compliance monitoring by clicking Import on the Applications tab.

## Entities

### Deploying External S-TAP manually
**Type:** entity  
**Description:** Deploy External S-TAP using Docker and scripts after obtaining signed SSL certificates.

## APIs & Tools

### gim_remote_activation API/Command
**Type:** api  
**Description:** Requires `connectToCollectorString` (collector IP) and `sharedSecret` (configured during GIM installation) for authentication.

## Features & Entities

### Catalog Import
Import catalog entries from archive files to a target restore server and export catalog entries from the source system.

### Embedded Integrations
Guardium UNIX/Linux systems integrate with Db2 Warehouse.

## Agents & Collectors

### S-TAP
Software agent on database servers capturing traffic and forwarding it to a Guardium Collector.

### Collector
Guardium appliance receiving S-TAP data, applying policies, and storing audit records.

## Policies & Rules

### Security Policy
Configured rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Databases & Data Sources

### Data Sources
Registry of defined database connections with details like type, host, port, user, database, and connection properties.

## System Information

### Number of Restarts
Metric tracking sniffer service restarts; frequent restarts indicate packet loss or malfunction.

### Timestamp
Time attribute associated with a connection, recorded at first request and updated when inactive.

## Parameters & Values

### ProcessID
Long integer identifier specifying the target process in Guardium APIs.

## Tooling & Operations

### Custom Table Builder
Guardium feature for creating custom datasets by uploading data, defining naming conventions, and setting relationships with existing datasources.

*Importing, loading, editing, or saving Guardium groups with >1 million members requires ≥2GB free memory per operation on Linux and UNIX.*

### DB2 z/OS Specific Filtering  
**Type:** attribute & operator  
**Description:** In DB2 for z/OS, Guardium supports filtering with the OPERATOR attribute, allowing matching on ATTRIBUTES for specific DB2 operations.

## Comments
**Type:** configuration  
**Description:** Named entity identified in source; detailed content not extracted.

## Azure MySQL Flexible Server / PaaS (All Versions - Azure Services)
**Type:** database  
**Description:** Guardium supported datasources matrix references support information for all versions of Azure MySQL Flexible Server/PaaS.

## JDBC Connection Properties
**Type:** configuration  
**Description:** Host Name/IP (required) and Port number (defaults to 443) identify the datasource; Database (required) specifies the database; Connection property lists required JDBC URL parameters.

## Ranger STAPs
**Type:** tool  
**Description:** Named entity identified in source; detailed content not extracted.

## SQL Verb Attribute
**Type:** attribute  
**Description:** Stores the SQL verb (SELECT, INSERT, UPDATE, etc.) used in a statement; earlier versions used different values with Quick Parse Native.

## Centralized Module View (GIM Bundles)
**Type:** service  
**Description:** GIM modules and bundles organize internal components; BUNDLE_GIM groups key modules like GIM, INIT, SUPERVISOR, and UTILS that provide Guardium's core functionality.

## S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

## Collector
**Type:** appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Security Policy
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Source Directory
**Type:** entity  
**Description:** Named entity identified in source; detailed content not extracted.

## Client Port and Database Name
**Type:** entity  
**Description:** Named entity identified in source; detailed content not extracted.

## VSrc IPv4 or IPv6
**Type:** entity  
**Description:** VSrc is the virtual source IP address (IPv4 or IPv6); srcPort and dstPort are integer source and destination ports ranging from 0‑65535.

## DLI‑ online or batch DL/I activity
**Type:** entity  
**Description:** DLI‑ activity monitors IMS online or batch DL/I operations, capturing events from SMF Data Collector and IMS Archived Log Data Collector.

## Audit only
**Type:** entity  
**Description:** Audit only logs the construct that triggered the rule for Selective Audit Trail policies, which by default log nothing; it explicitly selects constructs to log.

## Polar Installation service account
**Type:** entity  
**Description:** Polar Installation service account receives a broad set of permissions across GCP services needed for Unified Discovery and Classification backend operations.

## CEF Field Entity Attribute
**Type:** api  
**Description:** Guardium maps its Entity Attribute fields, including spt, exception, source port, start time, and session UID chain, to corresponding CEF fields.

## Session level criteri
**Type:** api  
**Description:** Named entity identified in source; detailed content not extracted.

## Buffer usage monitor report
**Type:** infrastructure  
**Description:** The buffer usage monitor report and related alerts help diagnose performance issues and configure data processing for unit utilization.

## S-TAP Verification
**Type:** infrastructure  
**Description:** S-TAP (Software TAP) is a lightweight agent that monitors database traffic and reports to the Guardium collector.

## CVE scanner agents
**Type:** cloud-service  
**Description:** CVE scanner agents such as Nessus and Qualys gather information about the Guardium system and send it to their third‑party portal for analysis.

## GIM charts
**Type:** cloud-service  
**Description:** GIM charts summarize GIM client status, versions, and note that older S-TAP/Guardium systems show only Linux-UNIX or Windows OS.

### Description
**Type:** attribute
**Description:** PUBLIC_OBJECTS table contains details of all public group objects.

### FullSQL view
**Type:** view
**Description:** Provides detailed SQL statement information including bind variables, DBMS metadata, and client/server information for each application event.

### Credential & Certificate Attributes
**Type:** attribute
**Description:** Includes ALERT_NOTIFICATION_ID, ALERT_TYPE, and Alert Destination; viewable only by admin role users.

### Hadoop monitoring API
**Type:** api
**Description:** remove_ranger_service removes a Hadoop Ranger service from monitoring within a specified Ambari cluster; requires admin or service admin privileges.

### Logger Queue
**Type:** infrastructure element
**Description:** Represents the amount of SQL data waiting in the logger buffer to be written to the collector's database, indicating system load.

### Full SQL - Data Tampering
**Type:** feature
**Description:** A filtered view of the Full SQL report that focuses on data tampering activities.

### Full SQL - Massive Grants
**Type:** report
**Description:** A filtered version of the Full SQL report, focusing on massive grant results with customizable runtime parameters.

### Risky Users - Connection Profiling List
**Type:** report
**Description:** Displays Connection Profiling List entries for users identified as risky, showing client/server access details.

### Full SQL - Data Tampering
**Type:** feature
**Description:** A filtered view of the Full SQL report that focuses on data tampering activities.

### Attribute Description
**Type:** entity
**Description:** Named entity identified in source; detailed content not extracted.

### REST API syntax
**Type:** api
**Description:** Syntax for GET retrieval of definitions_data_sets; no parameters.

### Policy Rule Violation Entity
**Type:** entity
**Description:** Created each time a policy rule is violated; not all violations are logged based on rule action configuration.

### ObjectsGroup Type is Objects
**Type:** entity
**Description:** Contains details of all public group objects with examples and select command variations.

m Installation Manager involves running the GIM client on the target server; additional prerequisites or steps are required for successful deployment.

## Overview

Guardium Installation Manager (GIM) enables installing, upgrading, and managing agents on individual or grouped servers.

## Credentials & Certificates

### Analyzer Service Account
The Analyzer service account grants the Unified Discovery and Classification cloud analyzer read access to customer data stores, enabling data classification.

### Cross Project Service Account
A service account created per connected GCP account that gathers metadata from the GCP environment for ingestion by Unified Discovery and Classification.

## Reports & Alerts

### External Tickets
The External Tickets section displays details of Guardium-generated tickets that have been sent to external systems (e.g., ServiceNow, Resilient), with a customizable time filter.

## Policies & Rules

### Session End Attributes
Session End Year represents the year component of the session end timestamp; Session ID uniquely identifies each session and is viewable only by admin users; Session Ignored marks whether a session was skipped via the IGNORE SESSION policy action.

## Agents & Collectors

### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Databases & Datasources

### Azure SQL Entitlements
Entitlement configurations that include database owner (`db_owner`) and security administrator (`db_security_admin`) roles, object and column privileges with `GRANT OPTION`, `PUBLIC` privileges, and system privileges.

### Datasource Group
Allows the creation of a collection of datasources that act as a single unit, usable in most Guardium applications.

## Cloud Services

### Outliers Detection APIs
APIs enabling outlier detection, such as `enable_outliers_detection_cross_cm_agg`, which activates outlier detection on aggregator(s) from a central manager.

## Knowledge

### LEEF Parameters
Parameters include LEEF version, vendor string, product string, and a note regarding the vendor-product combination.

### Public DBCC Commands
Includes commands like `ALTER`, `CREATE`, `DROP`.

### Agents & Collectors
**S-TAP (Software TAP)**  
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

**Collector**  
A Guardium appliance (hardware or virtual) that receives activity data from S‑TAP agents, applies security policies, and stores audit records.

### Policies & Rules
**Security Policy**  
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

### Knowledge & Features
**Runtime Sensitive Object Identifier**  
Ensures sensitive objects are dynamically monitored and flagged by the system for immediate attention.

**S-TAP for IBM i APIs**  
`get_istap_status` checks if the IBM i audit server is running and returns details about the audit queue and buffer size, aiding troubleshooting and performance tuning.

**S-TAP (Software TAP)** – continued  
Provides a deep‑traffic view, enabling real‑time enforcement of security rules and policy compliance monitoring.

## Agents & Collectors
### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  
### Guardium Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Data Sources
### Native MySQL Plug-in
A MySQL plug-in that omits the database name from queries sent to Guardium and does not send client source program information for MongoDB.

## Infrastructure
### SSH Key
Named entity identified in source; detailed content not extracted.

## Monitoring & Alerts
### SNMP Agent
A component installed on Guardium systems that provides read-only access to SQL Guard information via SNMP commands.

## Default Capture
**Description:** Assists the Replay function in distinguishing transactions and capturing values, particularly in prepared statements.

## Credentials & Certificates

## APIs & Tools
**create_qr_action**: Named entity identified in source; detailed content not extracted.  
**diag.bat**: Running this script on Windows S-TAP and other agents gathers comprehensive stats for Guardium diagnostics across multiple Windows agents.  
**IBM Guardium External S-TAP container**: Downloaded from IBM Cloud Container Registry (icr.io) for deployment.  
**revoke_role_from_object_by_Name**: Removes a role from the specified object, handling dependencies automatically.  
**revoke_role_from_object_by_id**: Removes a role from the specified object, handling dependencies automatically.

## Infrastructure

## Cloud Services
**Azure Event Hubs Monitoring**: Guardium supports protection of Azure Event Hubs cloud databases using data streams, enabling real-time monitoring and audit trail generation.

## Agents & Collectors
**S-TAP (Software TAP)**: A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.  
**Collector**: A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
**Security Policy**: A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Datasources
**Azure Event Hubs**: Guardium can protect Azure Event Hubs cloud databases by defining a cloud DB service account with Data Streams and enabling Guardium Collectors to monitor Azure Event Hubs for audit trails.  
**IMS z/OS**: The IMS z/OS - Privileged User Activity report displays access by users in the z/OS IMS Privileged Users group for the last 3 hours.  
**BigData Intelligence Outliers**: Provides one-hour granularity summaries of outliers for Guardium systems with a GBDI datasource, available to all roles.  
**BigData Intelligence Buff Usage**: Monitors buffer usage for Guardium's BigData Intelligence components, helping administrators identify performance bottlenecks and optimize data collection.  
**BigData Intelligence Buff Usage Monitor**: Offers monitoring capabilities for buffer usage in BigData Intelligence environments, aiding in performance tuning and resource management.  
**Attribute Description**: Attribute Description defines a tuple group containing named fields: Client IP, Source App, DB User, Server IP, Service Name, OS User, DB Name.

```
## APIs & Tools
### Assign Security Roles
Assign roles to objects such as policies or report definitions, and use the roles menu for assignment.

### GrdAPI example
Add a Ranger service on Cluster4 (port 5555) on the Ambari server, specifying the S-TAP host; returns ID=0 on success.

## Reports
### S-TAP version
Includes guard_tap.ini contents, kernel module details, A-TAP diagnostics, and database exit hook information for troubleshooting.

### Activity Types Entity
Provides descriptions of aggregation/import/export activities, visible from Aggregation/Archive domain to the admin role.

### Attribute Description
Lists parameters that indicate active status and retention period for audit process results.

## Agents & Collectors
### S-TAP (Software TAP)
Lightweight agent on database servers that captures traffic and forwards it to a Guardium Collector.

### Collector
Guardium hardware or virtual appliance that receives data from S-TAP agents, applies policies, and stores audit records.

## Databases & Datasources
### Informix datasource
Named entity identified in source (details not extracted).  
### DataSourceGroup
Named entity identified in source (details not extracted).
```

## Data Sets & Datasources
### Data Set z/OS Privileged User Activity
The **Data Set z/OS Privileged User Activity** report shows all privileged user accesses to sensitive z/OS data sets within a specified time range, displaying full SQL statements, usernames, and accessed data sets.

### IMS/DATA SET
Context information about data set activity, such as open, close, delete, update, or security violations, is captured for IMS/DATA SET operations.

## Credentials & Certificates
*No content extracted.*

## APIs & Tools
### GuardAPI syntax (set_import)
The `set_import` GuardAPI command is used to start or stop importing data from an aggregator to one or more Guardium collectors.

### GuardAPI syntax (gim_load_package)
The `gim_load_package` GuardAPI command loads software packages from the local filesystem into the Guardium GIM repository; it accepts a filename that can include wildcards.

### GuardAPI syntax (delete_invalid_stap)
The `delete_invalid_stap` GuardAPI command removes invalid S-TAP instances from the Deployment Health Topology view; it is distinct from deleting inactive S-TAP instances and is available starting with Guardium V10.6.

## Agents & Collectors
### S-TAP (Software TAP)
A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules
### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Databases & Datasources
*No content extracted.*

## Credentials & Certificates
*No content extracted.*

## APIs & Tools
### REST API syntax
Disable data streaming and manage feature flags with the disable_datastream command and enable_disable_feature_flag API, introduced in Guardium v12.2.1.

## Infrastructure
### 825. SQL injection detection for stored procedures and dynamic SQL
Guardium SQL injection detection analyzes SQL executed inside stored procedures and dynamically executed statements (EXEC, EXECUTE, EXECUTE IMMEDIATE) beyond standard scanning capabilities.

### 833. After installation of UNIX A-TAP in Oracle cluster
After installing UNIX A-TAP in an Oracle RAC cluster, stop each database instance, activate A-TAP, then restart the database; deactivation also requires stopping the database before running deactivate.

### 834. SAN storage devices
Deploying Guardium on SAN requires preparing SAN configuration information and additional steps to partition and install Guardium OS on SAN storage devices.

### 837. Regular Expressions
Regular Expressions are used with File Activity Monitoring (FAM) discovery and classification on both Windows and UNIX-Linux file servers, installed via GIM parameters.

### DB2 z/IMS/DATA SET
**Type:** database  
**Description:** DB2 for z/OS data sets with computed attributes such as Unit of Work that combines CICS transaction identifiers across IMS, Data Sets, and DB2; Unit of Work ID displayed in hexadecimal; Statement Type reported as Static or Dynamic.

escription:** Configurable rule set defining what database activity to allow, log, alert, or block based on users, objects, actions, and conditions.  

---

## Reports & Monitoring

### Groups Usage Report
**Type:** report  
**Description:** Shows data source and host utilization, including inactive S‑TAPs, server associations, and related application objects.  

### Unified Discovery and Classification
**Type:** feature  
**Description:** Detects data sources across private, public cloud, and SaaS environments, requiring specific hardware/software per provider; see system requirements.  

---

## Features & Workflows

### FAM groups domain
**Type:** feature  
**Description:** Assigns file‑privilege groups to users within the Users domain; only local groups are supported.  

### Public Peer Association
**Type:** workflow  
**Description:** Replicates data using links, log shipping, or snapshots to keep systems synchronized.  

### Best practices for using External S‑TAPs with on-premises databases
**Type:** workflow  
**Description:** Guides deployment of External S‑TAPs with on‑premises and cloud databases, including AWS HA, Google BigQuery setup, and troubleshooting via the Guardium Installation Manager.  

---

## Entities

### Comments Entity
**Type:** entity  
**Description:** A shareable comment attached to Guardium objects, existing only within the admin‑restricted Comments domain.  

### STAP Properties entity
**Type:** entity  
**Description:** Reportable object listing S‑TAP attributes (CPU count, etc.) queryable via Query‑Report Builder.  

### Template Set
**Type:** entity  
**Description:** Collection of item templates sharing a purpose, e.g., monitoring specific DBs on UNIX or Windows; two types: Operating System Only and Database templates.  

### Data User Security – Hierarchy and Associations
**Type:** entity  
**Description:** Links users to databases and servers, enabling layered security roles.  

### Volume tab
**Type:** entity  
**Description:** Configures persistent volumes for the External S‑TAP container: reuse an existing Kubernetes PV or create a new one with size and access mode.  

---

## Agents & Collectors

### S‑TAP (Software TAP)
**Type:** agent  
**Description:** Installs on DB servers to capture traffic and send it to a Guardium Collector for real‑time analysis and policy enforcement.  

### Collector
**Type:** appliance  
**Description:** Guardium hardware or VM that receives S‑TAP data, applies policies, and stores audit records.  

---

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** Configured rule set determining which DB activities are permitted, logged, alerted, or blocked for specific users, objects, and actions.  

---

## Databases & Data Sources

### Cloud database service protection with native audit
**Type:** service  
**Description:** Integrates Guardium with cloud providers' native audit services for classification, vulnerability assessment, and object auditing directly on cloud databases.

## Guardium Security Overview
A security policy defines which database activities are permitted, logged, alerted, or blocked using user, object, and action criteria.

## Databases & Data Sources
Supported databases include PeopleSoft Financials, Oracle, SAP ASE, DB2, and Sybase. Each requires a Guardium S‑TAP agent on the host or application server to capture activity.

## APIs & Tools
- **disable_riskspotter API** – disables RiskSpotter analytics on a Guardium central manager or standalone system.
- **GrdAPI (HDFS monitoring example)** – enables HDFS monitoring on a Hadoop cluster; requires Hadoop service restart.
- **Database Auto‑discovery** – scans servers for unknown database ports on demand or scheduled.

## Credentials & Certificates
Guardium APIs manage credentials (username/password/SSL certificates) for database connections and external services.

## Infrastructure
- **Managed Units Domain** – a logical grouping of Guardium appliances.
- **Guardium Central Manager** – displays health, configuration, and policy status of managed units.

# Guardium Data Protection Overview

**Guardium Data Protection** is the latest release of IBM's data security platform, providing a unified view for managing appliances, collectors, and data sources across on‑premises and cloud deployments.

## Cloud Services

### Public Data Transfer
A Guardium service that securely backs up, restores, and migrates data for databases hosted in public clouds such as AWS and Azure.

### Guardium API (REST)
An HTTP(S) service exposing all Guardium functions—including policy management, credential handling, MFA, and exception processing—via standardized web calls.

## Agents & Collectors

### S‑TAP (Software TAP)
A software agent installed on database servers that captures traffic and streams it to a Guardium Collector for real‑time analysis and policy enforcement (available since V11.0).

### Collector
A Guardium appliance (hardware or virtual) that receives data from S‑TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
A rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

### Activity Policy
A collection of rules that monitor and enforce security controls across various database activities, providing detailed tracking and reporting.

### Firewall and Latency Policy
A policy that mitigates latency issues during Guardium‑collector reconnections and prevents unwanted traffic spikes.

### FULL SQL Entity
A policy action that fully captures the entire SQL statement logged by Guardium for deep‑dive analysis.

## Databases & Datasources

### Datasource Connection
A connection entry requiring Host/IP, Instance name, and Database fields; defaults to the Master database if the Database field is omitted.

### Endpoint Configuration
Specifies Host, Port, Database/Service name, and Username fields for configuring a database endpoint.

## Credentials & Certificates

### Credential Configuration
Sets Host and Domain names via the `Hostname` and `Domain` commands; values must match DNS registrations.

## APIs

### RetrieveUpdatedUsers GuardAPI
Requires `dcName` and `lastUpdateTime` parameters to fetch updated user information (`6a98c937-a448-4b9c-9fa6-45b42511979b`).

**Captures the complete SQL statement, generated exclusively by Log Full Details policy actions.**

**S-TAP status history domain**  
*Type:* knowledge  
*Description:* Describes the status-history entities and attributes for S-TAP, providing visibility into application‑server installation status.

**Stap Statistics Identifier**  
*Type:* entity  
*Description:* Records the identifier for Stap Statistics, including packet‑drop counts and system‑CPU usage.

**GuardAPI syntax**  
*Type:* entity  
*Description:* Describes the GuardAPI `delete_rule` command, including required rule‑type and rule‑name parameters, and optional `remote` execution options.

**User roles**  
*Type:* entity  
*Description:* Defines Guardium user roles and their access privileges, including assignment to applications or specific components such as queries.

**Field Description**  
*Type:* entity  
*Description:* Details database owners, installation directories, and environment variables like `SYBASE` for UNIX and Windows installations.

**Domain Based on Query Main Entity**  
*Type:* entity  
*Description:* Enables filtering of investigation‑dashboard reports by host, period, and runtime filters for recovery issues.

**Managed units domain**  
*Type:* knowledge  
*Description:* Describes managed units and groups within the Guardium environment for organizational management.

**Template Set entity**  
*Type:* entity  
*Description:* A collection of template items for a specific OS or database; CAS uses it to monitor unique items.

**Discovered Instances domain**  
*Type:* knowledge  
*Description:* Tracks instances discovered by GIM; the Discovered Instances entity records timestamps, hosts, protocols, and port ranges.

**Assessment Log**  
*Type:* entity  
*Description:* Provides timestamped records of assessment executions accessible only to users with appropriate permissions.

---

### S-TAP (Software TAP)  
*Type:* agent  
*Description:* A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

### Collector  
*Type:* appliance  
*Description:* A Guardium hardware or virtual appliance that receives activity data from S‑TAP agents, applies security policies, and stores audit records.

---

### Security Policy  
*Type:* policy  
*Description:* A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

---

### Datasource Description  
*Type:* configuration  
*Description:* Named entity identified in source; detailed content not extracted.

### Datasource ID  
*Type:* configuration  
*Description:* Named entity identified in source; detailed content not extracted.

### Datasource Service Name  
*Type:* configuration  
*Description:* Named entity identified in source; detailed content not extracted.

---

### Apache Cassandra entitlements  
*Type:* credential  
*Description:* Apache Cassandra entitlements cover create privileges, privileges with grant option, and SuperUser roles for managing data.

---

### Configure GBDI data streaming  
*Type:* api  
*Description:* Named entity identified in source; detailed content not extracted.

### jProxy  
*Type:* connector  
*Description:* jProxy is an RPM‑based connector installed on the Guardium collector; it acts as a proxy between the sniffer and the GBDI platform, maintaining the streaming connection.

### Before you begin  
*Type:* tool  
*Description:* Named entity identified in source; detailed content not extracted.

### Add new  
*Type:* workflow  
*Description:* Named entity identified in source; detailed content not extracted.

### REST API syntax  
*Type:* api  
*Description:* The REST API `DELETE` method at `https://[Guardium hostname]:8443/restAPI/delete_sql_configuration` removes an SQL configuration element.

### Guardium Installation Manager (GIM) APIs  
*Type:* api  
*Description:* Named entity identified in source; detailed content not extracted.

### gim_reset_client  
*Type:* api  
*Description:* The GIM API `gim_reset_client` refreshes the connection to a GIM client by disassociating and re‑associating the GIM module, requiring the `clientIP` parameter.

### gim_reset_client (GuardAPI)  
*Type:* api  
*Description:* The GuardAPI `gim_reset_client` command refreshes a GIM client's connection by disassociating and re‑associating the GIM module, requiring `clientIP` for the target client.

### Big Data Intelligence APIs  
*Type:* api  
*Description:* Big Data Intelligence APIs include `reregister_agg_collector`, allowing a collector to be unregistered from its aggregator and registered with a new one; available from Guardium v10.1.4. The API is used for managing collector‑aggregator relationships.

### Log Ingestion Role  
*Type:* role  
*Description:* The Log Ingestion Role enables Unified Discovery and Classification to ingest and process logs from data stores, providing additional insight for classification.

### Log – SQL errors, Result Sets Log in/Log out  
*Type:* workflow  
*Description:* The "Log – SQL errors, Result Sets Log in/Log out" action stops sending activity for a session when a signal is sent to the S‑TAP, ignoring further activity.

## Guardium Core Concepts

### Security Policy
A rule set that allows, logs, alerts, or blocks database activities based on user, object, and action criteria.

### Agents & Collectors
#### S-TAP (Software TAP)
A software agent installed on database servers to capture traffic and forward it to a Guardium Collector.

#### Collector
A Guardium appliance that receives data from S-TAP agents, applies security policies, and stores audit records.

### Databases & Data Sources
Named entities that provide environment details for assessments. Specific content not extracted.

### Attributes
#### Client IP/Src App/DB User/Server IP/Svc. Name/OS User/DB Name
A bundled attribute group for reporting on connection and user fields.

### APIs & Tools
#### Query Rewrite API (create_qr_add_where)
Adds a WHERE clause to a query rewrite action. Available from Guardium V10.1.4.

## Infrastructure

### Internet Protocol modes
**Type:** feature  
**Description:** Guardium supports IPv4, IPv6, or dual-stack networking; administrators select the mode via the configuration UI.

## Features & Keywords

### Public MS-SQL Security
**Type:** feature  
**Description:** The Public MS‑SQL Security System Procedures group contains objects such as the MS SQL Security System Procedures.

## Agents & Collectors
**Agent (S-TAP)** – Software installed on database servers to capture traffic and send it to a Guardium Collector.  
**Collector** – Hardware or virtual appliance that receives agent data, enforces policies, and stores audit records.

## Policies & Rules
**Security Policy** – Rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Credentials & Certificates
**Uid Chain** – Credential storing the user‑identity chain for client/server sessions, omitting first and last entries.  
**Uid Chain Compressed** – Space‑efficient compressed form of the UID chain with the same exclusions.

## APIs & Tools
**REST API** – Provides HTTPS endpoints (port 8443) for Guardium configuration such as Multi‑Factor Authentication and data purging.

## Databases & Datasources
### Scan Entity
Named entity representing scan configuration attributes.

## Infrastructure
### STOP_SOFT_DISCARD
Revoke soft discard enforcement for specific sessions.
### Scan Entity
Entity defining file‑server attributes for scan operations.

## APIs & Tools
### test_exception (GET)
Retrieves exception results for a test.
### test_exception (PUT)
Updates test‑exception results.
### REST API DELETE – Schedule Removal
Delete a job schedule via DELETE /restAPI/schedule.
### REST API PUT – Enable Big Data Intelligence
Enable Big Data Intelligence via PUT /restAPI/bigDataInterface.
### REST API GET – Multi‑Factor Authentication Configuration
Retrieve and manage MFA settings via GET /restAPI/configure_mfa.
### REST API PUT – Update Test Exception
Update test‑exception results via PUT /restAPI (hostname/IP + port 8443).
### user_hierarchy
Return the complete user hierarchy.
### SOFT_DISCARD
Feature that temporarily suppresses policy enforcement for sessions.
### Stop soft discard (STOP_SOFT_DISCARD)
Revokes a soft discard for individual sessions.
### STOP_SOFT_DISCARD
Feature revoking soft discard for sessions.

## 1205. REST API syntax
Manage data streams at POST /restAPI/datastream (categories: keywords, knowledge, entities).

## 1206. REST API syntax
Manage policies at POST /restAPI/policy (related to keywords and entities).

## 1207. REST API syntax
Manage query rewrite actions at POST /restAPI/qr_action (keywords and entities).

## 1208. REST API syntax

Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent
**Description:** A lightweight client installed on database servers to intercept and forward database traffic to a Guardium Collector for analysis and policy enforcement.

### Guardium Installer (Installation Manager)
**Type:** tool
**Description:** A command‑line utility that automates Guardium software and configuration deployment across hosts, such as installing components, applying patches, or updating security credentials.

### CAS Host History
**Type:** configuration
**Description:** Stores a historical record of host configurations managed by CAS (Configuration Auditing System), enabling comparison of past and current settings for compliance verification.

### Collector
**Type:** appliance
**Description:** The centralized Guardium appliance that receives, analyzes, and archives database activity data from S-TAP agents, enforcing security policies and generating audit reports.

Policies & Rules

### Security Policy
**Type:** policy
**Description:** A set of rules defining permissible and prohibited database actions for users, applications, and objects; applied in real‑time by the Guardium engine.

### App User Name Entity
**Type:** entity
**Description:** Stores the username associated with an application event, providing context for auditing and policy decisions when direct application identification is not available.

Rules

### 1231. FROM Users
**Type:** rule
**Description:** Filters events where the source table is **Users** and the *City* column equals **Los Angeles**, returning only matching rows for audit or alert purposes.

## Databases & Data Sources
**Named Pipe Database Pipe** – entity describing Pipe name, Port Max, Port Min.  
**IBM Knowledge Catalog Data Source** – synchronizes Guardium groups with assets from an IKC instance.

## Agents & Configuration
**Import External Data Sources** – entity imported from source.  
**Guardium Universal Connector APIs** – start/stop/status/modify MongoDB filters.  

## Agents & Collectors
**S-TAP (Software TAP)** – software agent capturing database traffic to a Collector.  
**Collector** – appliance receiving, analyzing, and storing S-TAP activity data.

## Policies & Rules
**Security Policy** – rule set allowing, logging, alerting, or blocking database actions.

## Keywords & Features
**List of allowed connections** – feature including Create Context, Create Database Link, Create Function, Create Statistics, Create Type, Create User.

## Workflows & Operations
**Deploying CyberArk on your Guardium system** – workflow to define CyberArk datasource, controls, dependencies, and process flows.

## Configuration & Management
**Configure actions** – adjust analyzer settings or activate sessions.  

## Databases & Data Sources
**Db2** – data source configured with Host, Port, Database name (including schema), DataSource URL, TableName, ColumnName.

## Attributes & Entities
**Attribute Description** – Guardium Job domain attributes: End Time, Guardium Job Description, Process ID, Process Run ID, Queue Time.

## APIs & Tools
**Universal Connector Policies** – created/managed like other Guardium policies for data ingestion.  
**Universal Connector** – service ingesting heterogeneous data into Guardium, functioning as any other source integration.

## Cloud Services
**Universal Connector** – enables ingestion from cloud-based sources.

## Reports

### BigData Intelligence Classification Process Log
**Description:** Provides insights into classifier process logs, detailing the domain's structure and attributes for monitoring classification tasks.

## Entities

### Scheduled Jobs
**Description:** Lists all currently scheduled jobs; job details are not available.

## Agents & Collectors

### S-TAP (Software TAP)
**Description:** Software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Description:** A Guardium appliance (hardware or virtual) that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
**Description:** Configured rule set defining permitted, logged, alerted, or blocked database activities based on user, object, and action criteria.

## APIs & Tools

### Guardium Installation Manager (GIM) APIs
**Description:** Programmatic control over GIM functions, enabling tasks such as assigning, canceling, listing, removing, and updating GIM operations.

### Investigation Dashboard APIs
**Description:** Administrators can enable, disable, or configure features and parameters of the Investigation Dashboard for specific auditing needs.

## Databases & Data Sources

### IMS Object
**Description:** Identified named entity; detailed content not extracted.

## Credentials & Certificates

### DB Users Mapping List
**Description:** Maps database users to email addresses for real-time alert notifications on policy violations.

## Reports & Dashboards

### Runtime Sensitive Object Identifier entity
**Description:** Identified named entity; detailed content not extracted.

### Command Entity
**Description:** Identified named entity; detailed content not extracted.

## Infrastructure

### Command Entity
**Description:** Identified named entity; detailed content not extracted.

### SQL errors
**Description:** Logs SQL errors, result sets (if extrusion rules are used), and filters SQL commands at the Sniffer level.

## Cloud Services

### Server IP/Svc
**Description:** Aggregates server IP, service name, and database user into a tuple group; see Tuple groups for more details.

## Public Credentials Related

**Description:** Includes Guardium Audit Types, Self-Monitoring, and examples like `allowed_role`, `LDAP_config`, and `Turbine_user_group_role`.

## Public Peer Association

**Description:** Manages relationships between Guardium components such as links, replications, and data snapshots. Commands facilitate these associations.

## Deploy External S-TAP from the Guardium UI

**Description:** Deploy External S-TAP using Kubernetes on Amazon EKS or Azure AKS from the Guardium UI.

## Use Existing Persistent Volume

**Description:** Select "Use existing persistent volume claim" and provide the name of the pre-existing claim when installing External S-TAP.

## Inspection Engine Tab

**Description:** Administrators can view or adjust parameters related to the Guardium inspection engine, which parses and evaluates database activity.

## Group APIs

**Description:** Enables creating, listing, and deleting groups, hierarchical groupings, members, and aliases within Guardium.

## Reporting and Report Generation APIs

**Description:** Provides API capability to create Guardium policies, such as `create_policy`, supporting parameters like `baselineDesc`, `categoryName`, and `ruleSetDesc` for policy customization.

## policy\_install GuardAPI Example

**Description:** `policy_install` GuardAPI command installs one or more specified Guardium policies by name, applying them to the monitored database environment.

## remove_ranger\_service GrdAPI Example

**Description:** `remove_ranger_service` GuardAPI removes a designated Hadoop service (e.g., HDFS) from monitoring, confirming the action with a success message.

## Configuration Vault Password

**Description:** Configuration requiring a vault password includes parameters for the vault password, IP address list, group name, application IDs, safe names, and folder names.

## Outliers Data

**Description:** Shows the latest timestamp received from collectors for outlier detection, indicating data continuity and collection health to the aggregator.

## LOG Exception Action

**Description:** The `LOG` exception action records unauthorized activities for auditing purposes.

## Discovered Instances Domain
**Entity** capturing GIM-discovered instances, details about entities and attributes.

## FAM Domain
**Entity** capturing file entitlement reports, details about file access privileges.

## PIM Session Entity
**Component** integrating Privileged Information Management with Guardium DAM for privileged access control.

## Installed Rule Action Attribute
**Attribute** specifying rule actions (logging, alerting, blocking) matching monitored events.

## Server Host
**Network report** including logical partition hostname, client IP, and server IP.

## Agents & Collectors
**S-TAP** (agent) - captures database traffic, forwards to Guardium Collector for analysis.
**Collector** (appliance) - receives activity data, applies policies, stores audit records.

## Policies & Rules
**Security Policy** - rule set defining allowed, logged, alerted, or blocked database activities.

## Databases & Datasources
**Db2 for i** - IBM relational database for IBM i OS, optimized for ERP, transaction processing, business intelligence.

## Credentials & Certificates
**Access Key ID & Secret Access Key** - legacy AWS authentication; Access Key ID identifies account, Secret Access Key signs requests (must remain confidential).

## APIs & Tools
**Entitlement Optimization APIs** - RESTful interfaces for automated entitlement data management, license usage optimization, and external system integration.

## Infrastructure
**K-TAP Status** - system status showing successful loading and functioning of Kernel TAP module for Unix-Linux real-time monitoring.

## Cloud Services
**GuardAPI Syntax** - command-line interface for Guardium, enabling scripted/interactive querying/modification of settings (e.g., `get_mfa_configuration`).

## Agents & Collectors
**S-TAP (agent)** - captures database traffic, forwards to Guardium Collector for analysis and policy enforcement.
**Collector (appliance)** - receives activity data, applies security policies, stores audit records.

## Policies & Rules
**Security Policy** - rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Entities
**Guardium Login domain** - records all user login and logout events.
**Parser Error entity** - details parsing errors including Construct Id, DB Protocol, Error Id, Error Type, SQL Session Id, Timestamp.
**Sniffer Packets Throttled** - counts total connections ignored due to rate limits since inspection engine start.
**S-TAP Statistics** - provides S-TAP agent statistics.
**IPv6 Migration** - feature enabling exclusive IPv6 operation in existing Guardium deployments.
**System var disk usage** - indicates /var partition occupancy on Guardium appliance.
**add_receiver_to_rule_action GuardAPI** - adds receiver to rule action with parameters actionName, classDestinationString, fromPolicy, notificationTypeString, ruleDesc, alertUserLoginNameString.
**clevis_bind server parameter** - specifies tang server IP for clevis binding.
**enable_datastream** - enables cloud data source streaming, no parameters required.
**S-TAP/Z Files** - configurations and reports for mainframe Guardium S-TAP environments, including default DB users, test exceptions, IMS data access.
**Unified Discovery and Classification** - supports SAP HANA, provides encrypted (SSL) connections for on-premises data sources.
**Data Lake Reports** - provides SQL access and customizable reports for long-term retention data on central manager.
**Clone, modify, or delete datasource** - workflow for cloning/modifying/deleting existing datasource definitions.

### S-TAP (Software TAP)
**Type:** agent  
**Description:** Captures database traffic on servers and forwards it to Guardium Collectors.

### SNMP Collector
**Type:** appliance  
**Description:** Receives SNMP traps from Guardium appliances and forwards them to SIEM systems.

## Policies & Rules

### Multiple Failed Login Rule
**Type:** policy  
**Description:** Quarantines users after a configured number of consecutive authentication failures.

### IMS Object Access Monitoring Filter
**Type:** rule  
**Description:** Time window and filters for IMS object access monitoring.

### Attribute Description (Group Type Entity)
**Type:** rule  
**Description:** Specifies the group type and creation timestamp for categorization.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent  
**Description:** A software agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real‑time analysis and policy enforcement.

## Policies & Rules
### Security Policy
**Type:** policy  
**Description:** A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## APIs & Tools
### GuardAPI syntax
**Type:** api  
**Description:** The syntax for GuardAPI commands, including parameters required for operations such as deleting audit process results.

## Databases & Datasources
### IBM IMS Database
**Type:** database  
**Description:** Captures the IMS database descriptor (DBD) name accessed by application programs via DL/I calls.

## Infrastructure
### CAS Host Configuration
**Type:** configuration  
**Description:** Identifies the host where CAS is installed, including host name, OS type, and CAS version.

appliance  
**Description:** A Guardium hardware or virtual appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** A rule set that allows, logs, alerts, or blocks database activities based on user, object, and action criteria.

## Databases & Datasources

### Teradata 20
**Type:** database  
**Description:** Support added for Azure PostgreSQL Flexible Server/PaaS, ensuring compatibility across all versions.

### AWS RDS
**Type:** datasource  
**Description:** Connection details include the port number of the AWS data center where the RDS instance resides.

### IBM Guardium Data Protection
**Type:** datasource  
**Description:** Session End Date captures the session's end date.

### Guardium Host
**Type:** datasource  
**Description:** Guardium Host Name serves as the identifier for the Guardium host.

### Analytic Source
**Type:** datasource  
**Description:** Analytic Source Entity describes the origin system on which a security case occurred.

### Host ID
**Type:** entity  
**Description:** Host ID represents the host name or IP address of the monitored database server.

### Attribute
**Type:** entity  
**Description:** Includes Mount Event, Mount Time, and Request Count for tracking mount events.

### Field
**Type:** entity  
**Description:** Represents a unique database field encountered by Guardium among all schemas for that collector.

## Infrastructure

### Guardium Roles
**Type:** entity  
**Description:** Identifies specific Guardium roles within the system.

### Global Profile
**Type:** configuration  
**Description:** The Global Profile page sets defaults for all Guardium users.

## Cloud Services

### CAS Templates
**Type:** feature  
**Description:** CAS Templates Changes alert tracks modifications to CAS templates daily.

### QueryPCI Admin Users
**Type:** feature  
**Description:** Imported names in Guardium are truncated after 64 characters.

## Agents & Collectors

### S-TAP (Software TAP)
**Type:** agent  
**Description:** Captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** Receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Entities & Attributes

### Parser Errors Domain
**Type:** entities  
**Description:** Describes entities and attributes related to parser errors.

### Session Entity
**Type:** entities  
**Description:** Represents each client/server database session, capturing detailed session-specific information.

### Attribute Description - Object/Command
**Type:** entities  
**Description:** Combines an object value with a SQL verb to represent operations on database objects.

### Attribute Description - Object Field
**Type:** entities  
**Description:** Represents an 'Object/Field' combination, specifying object values with field values.

### Access ID
**Type:** entities  
**Description:** Uniquely identifies a set of client/server connection attributes, accessible only to users with the admin role.

### Execution Date (Audit Process)
**Type:** entities  
**Description:** Specifies the execution date field for the audit process result.

### Process Type / Queue Time
**Type:** entities  
**Description:** Guardium Job domain attribute defining job type and queue entry time.

### SQL Entity
**Type:** entities  
**Description:** Stores metadata for complex SQL clauses associated with a specific SQL statement instance.

## Overview

A Guardium hardware or virtual appliance receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Policies & Rules

### Security Policy
A configured rule set that defines which database activities are allowed, logged, alerted, or blocked based on user, object, and action criteria.

## Entities & Knowledge

### Assessment Tests Entity
### Expiration Days
### FULL SQL Timestamp Value
### FULL SQL Bind Variable Values
### Predefined Groups
### Virtual Image
### create_member_to_group_by_id
GuardAPI command that creates a group member by ID; requires parameters `id` (integer) and `member` (string), which must be unique within the group.
### delete_stap_inspection_engine
GuardAPI command that removes an inspection engine; requires parameters `sequence` and `stapHost`, verified with `list_inspection_engines`.
### enable_advanced_threat_scanning
GuardAPI syntax that enables threat detection scanners for the current system or all managed units.
### Exporting audit results
### Investigation dashboard
### modify_guard_param
### Attribute Value
Attribute Description for field values includes a 'Value' attribute from the logged construct.
### Policy ID
Uniquely identifies each access policy, enabling precise reference and management of individual policies.
### Message Text
Entity that stores the text of the message for threshold alerts.
### DB Protocol Exception
Captures debug information printed via the EXCEPTIONs mechanism.
### Event Release Value Num
Holds a numeric value associated with a released event, as set by GuardAppEvent.
### Logger Dbs
*Header-only entry; no meaningful content to extract.*

## Agents & Collectors

### S-TAP (Software TAP)
An agent installed on database servers that captures database traffic and forwards it to a Guardium Collector for real-time analysis and policy enforcement.

### Collector
An appliance that receives activity data from S-TAP agents, applies security policies, and stores audit records.

## Databases & Datasources

### Logger Dbs Monitored
*Named entity identified in source; detailed content not extracted.*

## Certificates & Credentials

### External S-TAP SSL certificates
SSL certificates used by External S-TAP deployment scripts to enable secure communication during deployment.

## APIs & Tools

### GuardAPI: delete_sql_configuration
Removes an SQL configuration from a collector or aggregated set.

### GuardAPI: enable_big_data_interface
Enables Big Data Intelligence on the Guardium system with the required parameter `ds_host` specifying the hostname of the Big Data storage location.

### GuardAPI: enable_outliers_detection
Enables outlier detection with configurable parameters.

### GuardAPI: update_ranger_hdfs_config
Configures the ldLibraryPath for Hadoop integration with Ranger HDFS.

### GuardAPI: update_threshold_in_rule
Updates rule thresholds; the command syntax requires parameters.

## Infrastructure

### K-TAP statistics
*Named entity identified in source; detailed content not extracted.*  
Lists all files in its installation directory as part of troubleshooting monitored database traffic.

## Cloud Services

### Integrating universal connector with HashiCorp Vault
*Named entity identified in source; detailed content not extracted.*  
Enables secret management across systems by integrating HashiCorp Vault with Guardium Universal Connector.

## Policies & Rules
### Security Policy
**Type:** policy  
**Description:** Configured rule set that defines allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

## Agents & Collectors
### S-TAP (Software TAP)
**Type:** agent  
**Description:** Software agent on database servers that captures traffic and forwards it to Guardium Collector for real-time analysis and policy enforcement.
### Collector
**Type:** appliance  
**Description:** Guardium hardware or virtual appliance that receives data from S-TAP, applies policies, and stores audit records.

## Databases & Datasources
### HDFS Name Node
**Type:** datasource  
**Description:** Guardium S-TAP connects to this HDFS NameNode IP/hostname to monitor Hadoop data access.

## Credentials & Certificates
### Clevis Bind Configuration
**Type:** credential  
**Description:** GuardAPI command that binds a Clevis configuration for secure encryption of sensitive data within Guardium workflows.

## APIs & Tools
### GuardAPI Command: restart_stap
**Type:** api  
**Description:** Restarts S-TAP agent to apply recent configuration changes without disrupting monitoring.
### GuardAPI Command: set_import
**Type:** api  
**Description:** Starts or stops import of aggregator data to collector; requires *state* parameter set to "START" or "STOP".
### GIM Module Upload
**Type:** tool  
**Description:** Uploads and imports Guardium Installation Manager (GIM) modules to the GIM server to ensure system components are up-to-date.

## Agents & Collectors

### S-TAP
**Type:** agent  
**Description:** Captures database traffic on servers and forwards it to a Guardium Collector for analysis and policy enforcement.

### Collector
**Type:** appliance  
**Description:** Receives, analyzes, and stores audit data from S-TAP agents.

### S-TAP (IBM i)
**Type:** agent  
**Description:** Interfaces and methods for interacting with the Software TAP agent on IBM i systems.

---

## Policies & Rules

### Security Policy
**Type:** policy  
**Description:** Rule set defining allowed, logged, alerted, or blocked database activities based on user, object, and action criteria.

---

## Databases & Data Sources

### User‑DB Association
**Type:** database  
**Description:** Links database users to Guardium monitoring entities for tracking activity and access control.

### Session Updates Table
**Type:** table  
**Description:** Records incremental changes to active user sessions, including login status and authentication events.

---

## Infrastructure

### Internal Database
**Type:** infrastructure  
**Description:** Core database used by Guardium to store configuration and audit data.

---

## Cloud Services

### Guardium Universal Connector
**Type:** entity  
**Description:** Integrates external data sources with Guardium.

---

## Credentials & Certificates

### Operating System User (OS_USER)
**Type:** entity  
**Description:** Identifies the OS user involved in database sessions for policy application.

### Port‑Protocol Function
**Type:** configuration  
**Description:** Lists port numbers, protocols, and functions for Guardium components' communication.

---

## APIs & Tools

### clone_policy API
**Type:** api  
**Description:** Duplicates an existing security policy with a new name and optional modifications.

## Guardium REST API

The Guardium REST API allows administrators to clone existing policies for streamlined configuration.

## Tools

### User-DB Association
**Type:** tool  
Named entity identified; no additional details were extracted.

### S-TAP for IBM i APIs
**Type:** tool  
Named entity identified; no additional details were extracted.

### PortProtocol Function
**Type:** tool  
Named entity identified; no additional details were extracted.

### Component roles
**Type:** tool  
Named entity identified; no additional details were extracted.

### Related concepts
**Type:** tool  
Named entity identified; no additional details were extracted.