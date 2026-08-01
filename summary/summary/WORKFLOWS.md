# IBM Guardium Data Protection — WORKFLOWS

**Category:** workflows  |  **Generated:** 2026-07-13  |  **Source:** gdp-12.x-documentation 2.pdf

---

## Implement Central Management in Existing Installation

### Implement Central Management
- **Components:**
  - **Pre-requisites:** Guardium Central Manager (CM) installed and reachable; existing collector (C) managed by CAS
  - **Execution Steps:**
    1. Log in to the CM GUI
    2. Go to **Manage > Inventory > Collectors**
    3. Locate the collector to be managed and select **Migrate**
    4. Choose the CM instance as the new manager and confirm the migration
    5. Ensure the collector restarts under CM control
    6. Verify that CAS is no longer the managing entity by checking the collector’s **Services** tab
    7. Adjust any service‑specific configurations (e.g., audit policy assignments) in the CM UI
- **APIs/Tools:** None (UI‑driven workflow)
- **Types:** Configuration
- **Customization:** None

## Datasource Configuration

### Configure MS SQL Server Datasource
- **Pre-requisites:** SQL Server running; network connectivity
- **Steps:** 
  1. Gather hostname, port, authentication
  2. Add datasource, select connection type
  3. Enter details, click Test
  4. Save configuration
- **Tools:** GuardAPI, grdapi add_datasource

## Active Threat Analytics

### Use the Active Threat Analytics Dashboard
- **Steps:** 
  1. Open dashboard
  2. Review security breach cases
  3. Investigate as needed
  4. Take appropriate actions
- **Tools:** None

## About This Task

### Complete Prerequisite Tasks for External S-TAP Deployment
- **Pre-requisites:** Kubernetes ready; Guardium UI accessible
- **Steps:** 
  1. Review deployment guide 
  2. Meet prerequisites
  3. Deploy External S-TAP via UI
- **Tools:** None

## Before You Begin

### Convert a Managed Unit to a Kafka Node
- **Pre-requisites:** Clean managed unit
- **Steps:** 
  1. Ensure unit is clean
  2. Run conversion command
- **Tools:** Guardium CLI

## Deactivating A-TAP on Db2 Cluster Nodes

### Deactivate A-TAP During Db2 Cluster Upgrades
- **Pre-requisites:** Admin privileges; nodes identified
- **Steps:** 
  1. Stop Db2 on all cluster nodes
  2. Run deactivate A-TAP commands on each node
- **Tools:** Guardium CLI

## Plan and Organize

### Create a Cardholder Server IPs List
- **Steps:** 
  1. In Plan and Organize, click Overview
  2. Create new Cardholder Server IPs List
  3. Add IP addresses storing cardholder data
- **Tools:** Guardium UI

## Configuring Database Discovered Instance Rules

### Automated Discovery of New Databases
- **Pre-requisites:** Guardium system configured
- **Steps:** 
  1. Enable automatic discovery in settings
  2. Configure inspection engines for Windows and UNIX
- **Tools:** GuardAPI

## Plan and Organize

### Define Custom Properties for Datasources
- **Pre-requisites:** Admin role
- **Steps:** 
  1. Navigate to datasource management
  2. Define or modify properties
  3. Assign properties by name, ID, or group
- **Tools:** GuardAPI

## About This Task

### Install and Configure S-TAP
- **Pre-requisites:** Guardium system IP/host name
- **Steps:** 
  1. Provide IP/host name during installation
  2. Complete configuration steps
- **Tools:** Guardium UI, GuardAPI

## Configuring the Import Process

### Import Users and Roles from LDAP
- **Pre-requisites:** LDAP connection defined
- **Steps:** 
  1. Navigate to Import Config tab
  2. Set up parameters for importing from LDAP
  3. Execute import process
- **Tools:** GuardAPI

## About This Task

### Manage S-TAP Client Filtering
- **Pre-requisites:** "Allow (approve) S-TAP connection to Guardium" enabled
- **Steps:** 
  1. Use CLI command `guardium cli stap approval` or API `grdapi store_stap_approval`
  2. Manage client filtering
- **Tools:** CLI, GuardAPI

## Adding Reports and Alerts for Inspection Engine Changes

### Monitor Inspection Engine Modifications
- **Pre-requisites:** Reports and alerts set up
- **Steps:** 
  1. Access inspection engine change reports/alerts
  2. Review and act on notifications
- **Tools:** Guardium UI

## About This Task

### Enable and Use FamMonitor
- **Pre-requisites:** GIM client running
- **Steps:** 
  1. Verify GIM client functionality
  2. Upload FAM bundle to GIM server
  3. Enable FamMonitor
- **Tools:** Guardium UI, GuardAPI

## Before You Begin

### Install Windows S-TAP
- **Pre-requisites:** Review installation requirements
- **Steps:** 
  1. Verify supported database server/OS versions
  2. Proceed with installation and configuration

## Windows S-TAP Installation
Identify Guardium UI as the tool for Windows S-TAP installation. The installation type is configuration and does not support customization.

## Record Custom Application Events
Enable GuardAppEvent, define event types, attach values, and record events as they occur using the GuardAppEvent API. This is an action that cannot be customized.

## Add a File Record to a Guardium Catalog
Export catalog entries from the source Guardium, transfer the file, then import it on the target Guardium. This is an action using built‑in GUI functions.

## Connect to AWS Secrets Manager Using an IAM Role
In the AWS Management Console, navigate to IAM, locate and select the role that permits Secrets Manager access. This is a configuration using the AWS UI, with no prerequisites beyond an enabled IAM service and a created role.

## Schedule Buffer Usage and Unit Utilization Data Uploads
Open the central manager, schedule the Buffer Usage Monitor Data Upload job, and schedule the Unit Utilization Data Upload job. Verify execution intervals. This is a configuration using the Guardium Scheduler and UI.

## Configure Clevis to Use Tang Servers for Secure Boot Attestation
Identify Tang server addresses, then run `store tang server` with primary and backup addresses. This is a configuration using the `store tang server` command.

## Monitor and Handle Software Installations/Upgrades
Launch the software installation/upgrade via Set up by Client, open the monitoring window via the Success dialog's Show Status link, refresh to confirm success, and use provided options for failures. This is an action using the Set up by Client tool and internal UI.

## Set Up and Run the Vulnerability Assessment Scanner
Ensure assessments are in the scanner's job queue, trigger the scanner, monitor processing, and review results. This is an action using the VA scanner command line or Guardium UI.

## Use Guardium Policy Analyzer with Continuous and Ad Hoc Modes
Open Policy Analyzer from the UI, select Continuous Mode for scheduled analysis or Ad Hoc Mode for on‑demand checks, run the analysis, and review reports. This is an action using the Policy Analyzer UI and scheduler.

## List Guard_Config_Update Parameters, Inspection Engine Names, or SQLGUARD Address
Open a terminal, run `guard_config_update --help` to view parameters, `guard_config_update --list-ie` for inspection engine names, and `guard_config_update --list-sqlguard` for SQLGUARD address. This is a configuration using the `guard_config_update` command‑line utility.

## Configure File Access Rules
Navigate to **Guardium UI > Rules > File Access**, click **Create** to define rules. Full details are not provided in the excerpt, but creation is the expected subsequent step.

## Create External Feed

### Feed Configuration
- Define the feed process through the Guardium UI
- Verify prerequisites and execute the feed to the target database
- **APIs/Tools:** Guardium External Feed UI

## Configure S-TAP
- Define data sources for S-TAP
- Test and verify connections
- Ensure audit server status is operational
- **APIs/Tools:** S-TAP Configuration Guide

## Manage S-TAP Schedules and Sessions

- **Components**  
  - **Pre-requisites:** S-TAP installed; access to S-TAP configuration UI  
  - **Execution Steps:**  
    1. Open the S-TAP management console and select **Schedules**  
    2. Create a new schedule or edit an existing one by specifying start/stop times, recurrence, and target groups  
    3. For session management, navigate to **Sessions** and use the **Start**, **Stop**, and **Refresh** actions as needed  

- **Types:** Configuration  
- **Customization:**  
  - Define role‑based access so only authorized users can modify schedules or sessions  
  - Configure alerts to notify when a session starts or stops unexpectedly

## Purge Data to Reduce Disk Usage Warning
- **Prerequisites:** Backups completed and verified; admin privileges
- **Steps:** Open Guardium UI → Admin > System Settings > Disk Management → Review disk usage → Select Purge Data → Choose categories → Confirm
- **API:** `grdapi purge_data`
- **Customization:** Schedule purge task via CLI for recurring cleanups

## Call GuardAPI from REST Client
- **Prerequisites:** Registered OAuth client; API endpoint
- **Steps:** Register client with `register_oauth_clientGuardAPI` → Obtain access token → Call GuardAPI with token
- **Tools:** `register_oauth_clientGuardAPI`, REST client
- **Customization:** none

## Activate A-TAP for Database Instances
- **Prerequisites:** Guardium installed; database parameters
- **Steps:** Store parameters with `guardctl` → `guardctl --db-instance=<name> activate` to enable A-TAP
- **APIs/Tools:** `guardctl`

Configuration

## Security and Compliance

### Incident Generation Process
1. Define an incident generation job
2. Specify query conditions against policy violations log
3. Set maximum incidents per run (default 5,000)

## Module Management

### GIM Global Parameter Configuration
1. From UI, go to **Manage > Module Installation > GIM Global Parameters**
2. Confirm `gim_auto_certificate_distribution` = **1**
3. Follow standard GIM certificate distribution workflow

## Data Integrity

### Open Datasource Creation Dialog
1. Click icon to open Create Datasource window
2. Use filters to find specific datasource definitions

## Datasource Management

### Configure Discovery Type Rule for Asset Discovery
1. Navigate to the Asset discovery page
2. Create a new discovery type rule
3. Set scan requirements based on criteria such as scan frequency, scope, and target environments
4. Save and activate the rule

## Upgrade Planning

### Pre-Upgrade Checklist
1. Install latest discovery-classification image
2. Extract files to correct repository path
3. Follow deployment instructions

## Certificate Management

### Advanced Upgrade Procedure
1. Verify system health with patched version
2. Archive all system and user data
3. Apply major version upgrade package

## System Monitoring

### Configure Monitoring for CAS Tests
1. Open Assessment Builder
2. Create new test or modify existing
3. Follow CAS-specific configuration workflow

## Alert Configuration

### SNMP Configuration for Alerts
1. Navigate to Alerter configuration settings
2. Select SNMP version (v2c or v3)
3. Enter version-specific configuration details

## External Component Management

### Manage External S-TAP Instance
1. Navigate to External S-TAP management console
2. Use Actions menu to restart the S-TAP service

# Guardium System Management Overview

## Configuration

### Mapping APIs to Reports
Utilize predefined reports linked to GuardAPI functions for immediate setup, or define custom reports and explicitly map them to corresponding API functions for tailored needs. Test the mappings to ensure accurate data correlation.

### Restricting Access by IP
Create an IP allowlist specifying the allowed IP addresses. Apply this allowlist to restrict UI or CLI access based on the determined scope.

### Enabling Load Balancing
Enable load balancing to allow automatic selection of managed units for profile installations. If not enabled, manually select managed units when needed.

### Discovering AWS Cloud DB Services
Configure a Guardium cloud DB service account with AWS permissions. Use this account to discover data streams and assign them to appropriate Guardium collectors.

### Aggregating Audit Data
Schedule daily data export from collectors to the aggregator. The aggregator imports, extracts, and merges files into the internal repository.

## Monitoring

### Monitoring and Resolving System Health Issues
Open the deployment health topology view to identify health issues. Investigate and determine the root cause, correlate findings with system logs, resolve issues following documented procedures, and verify resolution by re-evaluating system health.

### Running the Log Collector
Change to the `log_collector` directory, make `log_collector.sh` executable with `chmod +x log_collector.sh`, and execute the script with `sudo ./log_collector.sh`.

### Managing File Policies
Navigate to the policy or rule view within the Policy Builder for Files to create or edit policies/rules. Alternatively, use Guardium API commands for programmatic management.

## Digital Certificate Management

### Storing Venafi TPP Root CA Certificate
Obtain the Venafi TPP instance root CA certificate and run `store certificate keystore tru <certificate_path>` on the target system.

## Planning File Activity Monitoring

### Preparing to Run FAM
Follow the guide to prepare the environment for file activity monitoring and execute the FAM workflow as outlined in the documentation.

## Discovery

### Configuring Automatic Discovery of Databases
Open the Guardium UI, go to **Administration Center > Discovery**, and enable datasource discovery. Specify frequency and schedule for scans and save the configuration.

## Services Management

### Viewing Guardium Services Status
Open the **Services Status** panel to review the aggregated status of services. Click a service name to view detailed status and properties.

### Enabling Service Debug Logging
Navigate to **Setup > Logging > Service Debug Logging**, select the service, set the log level to `DEBUG`, and apply the changes. Verify the logging state changed in the **Status** column.



## Test Detail Exceptions Management

### List Existing Exceptions
- **Components:**
  - **Pre-requisites:** Access to Test Detail Exceptions menu; valid role
  - **Execution Steps:**
    1. Navigate to **Test Management > Test Detail Exceptions**
    2. The list of all defined exceptions displays automatically
    3. Review the entries; apply filters if needed
    4. Note any IDs for future reference or edits
  - **APIs/Tools:** GUI only
- **Types:** Navigation
- **Customization:**
  - **User workflows:** Export the list for offline analysis or archive



## Create Data Source
- **Components:** Technical name, IP/host, port, service name, optional custom URL  
- **Steps:** Test connection, then save the data source  
- **Tools:** GuardAPI, **Administration** > **Data Sources** > **Add Datasource**  
- **Type:** Configuration  

## Custom Data Compliance Program
- **Steps:** Define objectives, map sources to rules, enforce policies via data‑driven views, validate and refine  
- **Tools:** Policy Builder (no API)  
- **Type:** Configuration  

## Schedule Custom Data Uploads
- **Steps:** Open **Custom Table Builder**, select table, choose **Upload Schedule**, configure frequency and source, save and verify  
- **Tools:** UI only (no API)  
- **Type:** Workflow  

## Start or Stop Application via GuardAPI
- **Steps:** Invoke `start_stop_application`, specify `action` (`START`/`STOP`), `appId`, optionally `api_target_host`, verify response or system state  
- **Tools:** GuardAPI  
- **Type:** Configuration  

## Restore Collector CLI
- **Steps:** Boot collector with ISO, perform initial setup (license, network), run restore using non‑centrally‑managed aggregator, validate functionality  
- **Tools:** CLI only (no API)  
- **Type:** Workflow  

## Archive and Purge Data
- **Steps:** Go to **Manage > Archive & Purge**, select datasets, choose archiving or purging options, confirm, verify in logs  
- **Tools:** grdapi archive_data, grdapi purge_data  
- **Type:** Action  
- **Customization:** Schedule periodic archiving  

## Access Control (Fine‑Grained)
- **Steps:** **Setup > Access Control > FGAC**, define roles and object‑level permissions, assign roles to users, test with restricted account  
- **Tools:** grdapi set_access_rule  
- **Type:** Configuration  

## Scan Log Files for Errors
- **Steps:** Open **Activity Monitoring**, select **Logs**, run error scan on chosen files  
- **Tools:** None  
- **Type:** Knowledge  

## Stop Audit Process
- **Steps:** Locate running audit, use **Stop Audit** in management console, confirm  
- **Tools:** grdapi stop_audit  
- **Type:** Action  

## Prepare for Dashboards
- **Steps:** Identify reporting needs, decide single vs multi‑dashboard, group reports by purpose/criticality, plan layout  
- **Tools:** None  
- **Type:** Navigation  

## Upload Key File
- **Steps:** Choose upload target (central manager or managed unit), navigate to upload interface, select key file, confirm upload and deletion from file server  
- **Tools:** None  
- **Type:** Configuration  

## GuardAPI Delete_Schedule
- **Steps:** Use `deleteschedule`, supply `jobGroup` and `jobName`, optionally `deleteJob` and `api_target_host` for execution control  
- **Tools:** grdapi delete_schedule  
- **Type:** Knowledge  

## Stop Interfering Processes
- **Steps:** Identify processes blocking patch installation, stop them, delete stuck patches  
- **Tools:** None

## Keywords

### QRadar and Guardium Integration
- **Pre-requisites**: QRadar and Guardium installed
- **Steps**: Enable information flow; configure policies; send alerts/reports to QRadar
- **Customization**: Adapt integration to security requirements

### Set Up A-TAP Authorization
- **Prerequisites**: Node setup completed
- **Steps**: Authorize DB users to Guardium group with guardctl
- **Tools**: `grdapi authorize_user`
- **Customization**: Adapt for different database types

### Group Management
- **Action**: Populate Group from Query
- **Prerequisites**: Valid Guardium group and predefined query
- **Steps**: Select group → Populate from Query → Confirm
- **Tools**: `guardapi set_populate_group_from_query_schedule`
- **Customization**: Store queries as reusable templates

## Datasource Configuration

### Configure MS SQL Server Datasource
- **Prerequisites**: SQL Server running; network connectivity verified
- **Steps**:
  1. Gather hostname, port, and authentication method
  2. Add datasource via UI, enter connection details, test, and save
- **Tools**: GuardAPI, `grdapi add_datasource`
- **Customization**: Clone template for repeated setups

## Guardium Product File Transfer
Transfer the Guardium product file to the database server in FTP binary mode, re-downloading if the transfer fails.

## Guardium Assessment Features

### Test Exception Creation
Authorize a test to pass by selecting "Create Test Exception" on the Security Assessment Results screen.

### Search Page Configuration
Search the Guardium search page by item name or partial text, then add the desired item to the current view.

### GuardAPI Health Analyzer
Disable health analyzer features using `guardapi disable_health_analyzer` with the desired parameter and API target host.

### Multi-CM Environment Configuration
Enable outliers detection on any Central Manager; the setting propagates to all managed units and additional CMs.

## 378. Restart UC

### Universal Connector Restart
Log into the Guardium UI, navigate to **System Management > Universal Connector**, and click **Restart UC**; verify status in `uc-logstash.log` and `logstash-plain.log`.

## 379. Enable or Disable S-TAP

### S-TAP Status Management
Enable or disable S-TAP on Windows DB servers via **Manage > Module Installation > Set up by Client**, set `WINSTAP_ENABLED`, adjust startup settings, and save changes.

## 380. Next Discovery and Classification Steps

### Subsequent Scan Configuration
Review preliminary scan results, refine criteria, schedule the next scan, and execute discovery and classification tasks with `grdapi data_discoverer` and `data_classifier`.

## 381. Strict Separation of Duties

### Access Role Assignment
Assign admin and access manager roles, verify limited access, document workflows, and implement periodic audits using `grdapi manage_access_roles` and `manage_admin_capabilities`.

## 382. HashiCorp Vault Integration

### New Credential Definition
Create a new credential definition in Guardium UI, select **HashiCorp Vault**, enter Vault URL, authentication token, and secret path, and save for UC integration with `grdapi add_credential_definition`.

## 383. FreeTDS Version and Support

### TSQL Command
Run `tsql -C` to check FreeTDS version and supported features; no required tools.

## 384. MYSQL Table Privileges

### Database Permissions
Ensure the database login user has SELECT permission on all target tables for data uploads; consider using database tools for hidden tables.

## 385. Post-Restart UC Activation

### UC Post-Restart Steps
Log into the Guardium UI and continue with the next steps after a successful system restart.

## System Management - Universal Connector Restart

**Pre-requisites:** Access to System Management UI  
**Execution Steps:**  
1. Open **System Management > Universal Connector**.  
2. Execute the CLI command `store system restart uc --ensure-management`.  
3. Confirm restart by querying connector logs for `UC_STARTED` entry.  
**APIs/Tools:** CLI `store system restart uc --ensure-management`  
**Types:** Action  
**Customization:** Automate restart via scheduled scripts using the same CLI command.

## GuardAPI - Refresh Quick Search Groups

**Pre-requisites:** GuardAPI access; target hosts defined  
**Execution Steps:**  
1. Open GuardAPI command interface.  
2. Run `refresh_quick_search_groups param1=value1 param2=value2`.  
3. Substitute `param1` and `param2` with identifiers of target hosts.  
4. Execute and observe response for success or errors.  
**APIs/Tools:** GuardAPI `refresh_quick_search_groups`  
**Types:** Keyword

## Deploy Monitoring Agents

**Pre-requisites:** GIM clients installed on target systems  
**Execution Steps:**  
1. Access **Deploy Monitoring Agents** from the Guardium UI.  
2. Select the GIM clients you wish to enable.  
3. Choose **S-TAP** installation for monitored databases.  
4. Start the deployment and wait for the process to finish.  
5. Validate activation through Guardium reports.  
**APIs/Tools:** `grdapi deploy_monitoring_agents`  
**Types:** Feature

## Harden - Add Exceptions to VA Tests

**Pre-requisites:** VA policy configured; access to **Harden** module  
**Execution Steps:**  
1. Open **Harden > Vulnerability Assessment > Assessment Builder**.  
2. Select the relevant test.  
3. Go to **Test Tuning** and add group or detail exceptions.  
4. Save changes and re-run the assessment.  
**APIs/Tools:** `grdapi tune_test`  
**Types:** Workflow

## Group Builder - Add Members

**Pre-requisites:** Guardium UI access; group creation permissions  
**Execution Steps:**  
1. Navigate to **Setup > Tools and Views > Group Builder**.  
2. Select the group to modify.  
3. Choose manual entry, query-based addition, or merge with an existing group.  
4. Input member identifiers or configure query criteria.  
5. Save and verify group membership.  
**APIs/Tools:** `grdapi add_group_member`, `manage_group_builder`  
**Types:** Knowledge

## Kafka - Test OUA Profile Connection

**Pre-requisites:** OUA profile configured; operational Kafka cluster  
**Execution Steps:**  
1. Go to **Setup > Kafka > Profiles**.  
2. Choose the OUA profile to test.  
3. Click **Test Connection**.  
4. Review results and troubleshoot failures if needed.  
**APIs/Tools:** `grdapi test_kafka_profile`  
**Types:** Workflow

## Scan Activation Procedure

**Pre-requisites:** Scan configuration saved  
**Execution Steps:**  
1. Save the scan configuration in the Guardium UI.  
2. Click the **Activation** button post-save.  
3. Schedule **Purge Local Database** as required.  
**APIs/Tools:** `grdapi activate_scan`, `purge_local_database`  
**Types:** Workflow

## Create Guardium User via GuardAPI

**Pre-requisites:** Admin privileges; Guardium system installed  
**Execution Steps:**  
1. Log into Guardium CLI with an admin account.  
2. Execute `store system role create` for the required CLI role.  
3. Run `store system user create` specifying username, password, and assigned role.  
4. Verify CLI access by executing a GuardAPI command.  
**APIs/Tools:** CLI `store system role`, `store system user`; GuardAPI `create_user`  
**Types:** Action  
**Customization:** Assign additional privileges with `assign_granted_privileges`.

## Disable Hostname and Certificate Verification (External S-TAP)

**Pre-requisites:** External S-TAP installed; network bypass support  
**Execution Steps:**  
1. Open the S-TAP client configuration utility.  
2. On the **Security** tab, uncheck **Verify Hostname** and **Verify Server Certificate**.  
3. Save settings and restart the S-TAP service.  
**APIs/Tools:** None  
**Types:** Configuration  
**Customization:** None

## Automate Audit Runs via API

**Pre-requisites:** API user with audit execution rights; configured report templates  
**Execution Steps:**  
1. Identify the task ID for the audit and its report template.  
2. Use a script to call `POST /api/audit/run`.  
3. Include the task ID in JSON format: `{"taskId":"a88c7db9-8274-4663-a2e5-d02e05c1e39f"}`.  
4. Check the API response for confirmation of scheduling.  
**APIs/Tools:** `POST /api/audit/run`  
**Types:** Action  
**Customization:** None

## External S-TAP - Manage SSL/TLS

**Pre-requisites:** Dedicated S-TAP server; valid SSL certificates  
**Execution Steps:**  
1. Generate or acquire SSL/TLS certificates for each deployment scenario.  
2. Import certificates into the S-TAP server via the Administration console.  
3. Validate connectivity and certificate trust using `grdapi verify_certificate`.  
4. Configure client drivers to trust the imported certificates.  
**APIs/Tools:** `grdapi verify_certificate`  
**Types:** Configuration

## Unified Discovery Installation

- **Components:** Access to Connections page; network connectivity to data sources  
- **Execution Steps:**  
  1. Click **Add** on the Connections page.  
  2. Select **Unified Discovery and Classification** from the secondary analyzer list.  
  3. Configure discovery settings for target data systems.  
  4. Execute the initial discovery run and review results.  
- **Types:** Workflow  
- **Customization:** Customize discovery parameters for diverse data environments.  

## Set Up User Activity Reporting

- **Components:** Defined queries and alert policies  
- **Execution Steps:**  
  1. Navigate to **Reports > Query Builder**.  
  2. Create a new query using **Guardium Login** and **SQL Guard Login** entities.  
  3. Save the query and schedule a recurring report.  
  4. Define correlation alerts for failed logins or suspicious activity patterns.  
- **Types:** Configuration  
- **Customization:** Tailor queries and alerts to organizational security policies.  

## Deploy Unified Discovery and Classification

- **Components:** Access to Connections page; network connectivity to data sources  
- **Execution Steps:**  
  1. Click **Add** on the Connections page.  
  2. Select **Unified Discovery and Classification** from the secondary analyzer list.  
  3. Configure discovery settings for target data systems.  
  4. Execute the initial discovery run and review results.  
- **Types:** Workflow  
- **Customization:** Customize discovery parameters for diverse data environments.  

## Policy Violation Management

- **Components:** Policy Violations / Incident Management report access  
- **Execution Steps:**  
  1. Open the **Policy Violations / Incident Management** report.  
  2. Select the violation(s) to assign.  
  3. Click **Assign to Incident** and choose an existing or create a new incident.  
  4. Save the assignment and track progress.  
- **Types:** Action  
- **Customization:** Define custom incident categories for streamlined tracking.  

## Data Guard Configuration and Management

- **Components:** Guardium system running; Guardium CLI access; database server reachable  
- **Execution Steps:**  
  1. Generate a unique UUID for the TAP instance (e.g., `bbb59dac-2525-412a-a600-0ba1d36638b6`).  
  2. Execute `guardctl` with parameters: `--uuid=<UUID>`, `--action=install`, `--db_user=<username>`.  
  3. Store configuration in `/var/db/guard` using `guard-config-store --save`.  
- **Types:** Configuration  
- **Customization:**  
  - **User workflows:** Create Bash alias `tap-setup` to wrap the `guardctl` command.  

## Policy and Access Management

### Fine-Grained Access Control (FGAC)

- **Components:** Administrator role; security policy defined  
- **Execution Steps:**  
  1. Navigate to **Setup > Access Control > FGAC**.  
  2. Define roles and object-level permissions using the FGAC editor.  
  3. Assign roles to user accounts via the **User Management** console.  
  4. Test access with a restricted user account.  
- **Types:** Configuration  
- **APIs/Tools:** `grdapi set_access_rule`

# Compressed Technical Documentation

## Data Collection

### Create Selective_Audit_Table Rule
- Add `ADD` and `UPDATE` actions for monitored tables
- Link to **Policy > Event Correlation** under Application Events API
- **APIs/Tools:** Policy builder UI, Audit Only rule wizard
- **Type:** Configuration

## Reporting

### Configure Datamart Extraction Reporting
- Prerequisites: Guardium 12.2.x+, data collection enabled
- Steps:
  1. Open **Reports > New Report** > **Datamart Extraction**
  2. Select S-Collector, set retention policy
  3. Validate with **System Reports > Datamart Extraction Report**
- **APIs/Tools:** `grdapi create_datamart_report`
- **Type:** Configuration

## Datasource Configuration

### Configure MS SQL Server Datasource
- Prerequisites: SQL Server installed, network connectivity verified
- Steps:
  1. Gather hostname, port, authentication method
  2. Navigate to **Datasources > Add Datasource**, select connection type
  3. Enter details, click **Test Connection**  
  4. Save configuration
- **APIs/Tools:** GuardAPI, `grdapi add_datasource`
- **Type:** Configuration
- **Customization:** Clone datasource template for repeated setup

## Security

### Create Test Detail Exception
- Prerequisites: Access to Security Assessment Results
- Steps:
  1. Click "Create Test Detail Exception" from the screen
  2. Select element type
- **APIs/Tools:** None
- **Type:** Features

## CyberArk Integration

### Deployment Overview
- Prerequisites: Configured CyberArk vault, Guardium datasources
- Steps: Centralize datasource credentials, access control, dependencies, workflows in CyberArk
- **APIs/Tools:** CyberArk deployment tools
- **Type:** Features

## Administration

### Before You Begin (CyberArk)
- Prerequisites: Guardium datasources defined
- Steps: Create or edit CyberArk objectname for each datasource via Setup > Tools and Views > Datasource Definitions
- **APIs/Tools:** None
- **Type:** Knowledge

## User-DB Association

### Map Users to Databases
- **Pre-requisites:** Access manager credentials; user schema defined
- **Execution Steps:**
  1. Log in using the accessmgr role.
  2. Go to **Setup > User-DB Association**.
  3. Enter username and database name.
  4. Verify mapping by testing database access.
- **APIs/Tools:** None
- **Types:** Configuration
- **Customization:** Periodically update associations.

## Security Policy Management

### Configure Amazon ElastiCache Data Source
- **Pre-requisites:** Guardium data source integration; ElastiCache endpoint, credentials, SSL details
- **Execution Steps:**
  1. Open **Data Sources > Add Data Source**.
  2. Select **Amazon ElastiCache**.
  3. Enter endpoint URL, port, and SSL option.
  4. Provide username/password or token.
  5. Verify connection before saving.
- **APIs/Tools:** UI only.
- **Types:** Configuration

## Audit Management

### Create a Custom Audit Report
- **Pre-requisites:** Reporting privileges; existing audit logs
- **Execution Steps:**
  1. Navigate to **Reports > Create New Report**.
  2. Choose **Audit Report** template.
  3. Select data sources and time range.
  4. Add columns from audit fields.
  5. Save and schedule or run the report.
- **APIs/Tools:** Report API for automation.
- **Types:** Configuration

## Data Streams Management

### Add a New Data Stream
- **Pre-requisites:** Streams access; creation permissions
- **Execution Steps:**
  1. Open **Streams** table.
  2. Click **Add** to create new stream.
  3. Enter name, description, and source details.
  4. Save the stream.
- **APIs/Tools:** None
- **Types:** Action
- **Customization:** Save templates for reuse.

## Guardium Configuration and Maintenance

### Exclude False Positives
- Manage exclusions for Active Threat Analytics via GuardAPI and maintain a list of excludes with reasons.

### Enable DAM Outlier Mining
- Enable or disable DAM outlier mining from the central manager view and analyze results for security insights.

### Run a Privacy Set Report
- Execute privacy set reports from the Guardium interface, schedule via compliance workflows, and review results.

### Manage Query Conditions
- Build and test query conditions using GuardAPI, save queries, and develop advanced templates.

### Scale Vulnerability Assessment Scanner Deployment
- Adjust scanner deployment using Helm and kubectl commands, and validate functionality.

### Upgrade Guardium Modules via GIM
- Patch and upgrade Guardium modules through the GIM interface, review GIM_EVENTS report, and verify module operation.

### Stop and Start CAS Agent
- Modify `/etc/inittab` on UNIX hosts and reboot or restart the CAS service.

### Prepare for Guardium System Restore
- Follow the restoration workflow and verify data integrity post-restore.

### Understand Guardium Traffic Flow
- Recognize how Guardium preprocesses and summarizes database traffic for analysis and external SIEM integration.

### Central Manager Health Check
- Apply central manager health check patches, document issues, and follow remediation steps.

## Workflow

### Customize User Workflows
- Integrate health checks into regular maintenance schedules

---

## Guardium Tasks

### Configure MSSQL Datasource
- Gather hostname, port, and authentication method
- Navigate to **Datasources > Add Datasource**, select connection type, enter details, test, save

### Schedule Health Check Patch Scan
- Log in to central manager UI → **System > Maintenance > Health Checks**
- Select **Patch Scan**, choose target version, start scan, review results

### Configure Mutual SSL with Couchbase
- Create SSL client certificate per Couchbase instructions
- Configure Guardium to trust CA, import client certificate, test mutual authentication

### Sequence Export and Import Tasks
- Verify Export finished successfully
- Ensure Aggregator has 2 minutes to complete file transfers
- Initiate Import task from Aggregator

### Utilize Data Grid View
- Open chart in Guardium UI
- Click data grid icon to open detailed table view
- Use column sorting and filtering options

### Use Relative Date Notation
- Click date input field
- Type "NOW" to use current date
- Apply filter or save query condition

### Identify Users via Application Events API
- Implement API calls in application code
- Send connection events to Guardium endpoint
- Analyze events using Guardium reports

### Set Up GenAI App Node
- Deploy collector with GenAI capability
- Register collector with central manager
- Enable GenAI feature in CM settings
- Configure GenAI query targets

### Enable IP-to-Hostname Alias Discovery
- Run IP-to-Hostname Aliasing discovery job
- Review generated hostname aliases
- Manually edit or accept autogenerated aliases

### Apply Data Activity Monitoring
- Create DAM monitoring policy
- Assign policy to relevant data sources
- Activate policy through Guardium UI

---

## 508. Applying Policy to NAS and SharePoint

### Configure NAS and SharePoint Access Policies
- Open Policy Builder, create new policy targeting NAS/SharePoint file systems
- Define granular filtering criteria, assign policy to data sources

---

## Reporting on Datasources

### Configure Datasource Reports
- Navigate to **Reports > Define Reports**
- Choose **Datasource** as report type
- Select fields to include, configure grouping and filters
- Schedule report delivery and specify format

## Access Control

### Clone DATA SET Access Query
1. Clarify purpose: Query editing for timestamp filtering.
2. Condense actions: Locate existing query, clone, rename, reposition timestamp column, adjust filters, save.
3. Remove stance comment.

## Data Source Configuration

### Modify an Existing CAS Template Set using the CAS Configuration Navigator Panel
1. Clarify purpose: Edit active CAS template.
2. Remove unnecessary prerequisite (CAS host already implied by panel).
3. Shorten actions: Open panel, select template, edit, save, acknowledge restriction.

## Investigation Dashboard Filters

### Launch Investigation Dashboard with Pre‑Filtered Columns
1. Clarify relationship: Columns in report map to dashboard filters.
2. Remove steps, keep purpose and requirement.

## Datasource Configuration

### Configure MS SQL Server Datasource
- In Guardium UI, add a new datasource and select **Microsoft SQL Server**.  
- Enter hostname, port, credentials, and test connectivity.  
- Enable advanced options such as SSL and auto-discovery.  
- Persist with **Save** and automate with `store_datasource` or `grdapi`.  
- Export/import for reuse across collectors.

# Security Assessment Management

## Delete an Assessment
- **Pre-requisites:** Administrator role; confirmation of deletion intent
- **Steps:** Open the Security Assessment Finder → locate the assessment → select **Delete** → confirm

# S-TAP Verification after Installation

## Verify S-TAP Communication with Guardium System
- **Pre-requisites:** S-TAP installed; Guardium reachable; admin credentials
- **Steps:** Log in to Guardium → **Manage > Activity Monitoring > S-TAP Control** → locate S-TAP → confirm status is *Active* and configuration details match

# Access Control Setup

## 695. Delete an Assessment and its Dependencies
- **Pre-requisites:** Administrator role; assessment ID `695`
- **Steps:** Open Ty Assessment Finder UI or run `grdapi delete_assessment` → provide ID `695` → confirm deletion (dependent objects removed)

# Unified Discovery and Classification – Google Cloud Integration

## Link a Google Cloud Project Account
- **Pre-requisites:** Guardium with Unified Discovery and Classification enabled; GCP service account with read permissions
- **Steps:** Log in to Guardium UI → **Integration > Cloud Accounts** → Add Google Cloud Project → run supplied script to pull sensitive data

# Guardium Policies

## View Policy Rules for the IBM i (AS400) Platform
- **Pre-requisites:** Access to Guardium UI; IBM i (AS400) datasource configured
- **Steps:** Open Guardium UI → **Policies** → (additional steps not provided in excerpt)

## Policy Management

### View and Edit Currently Installed Policy
- Open the **Installed Policies** page, select the policy, click **Edit**, make changes, and click **Save**.

## CAS Template Configuration

### Modify CAS Template Set Item
- In **CAS Configuration → Navigator**, select the template set, adjust settings in the panel, and click **Apply**.

## Datasource Profile Management

### Create or Manage Datasource Profiles
- Go to **Datasource Profile Management**, click **Create New Profile**, fill in details, and save for individual profiles or import multiple profiles in bulk.

## GuardAPI Update

### Modify guard_tap.ini Parameters
- Execute `grdapi updateValue` with parameter name and value, specifying Windows/Unix relevance as needed, then verify changes in `guard_tap.ini`.

## Buffer Usage Monitoring

### Enable Buffer Usage Alerts
- In **Reports → Buffer Usage Monitor**, set thresholds, run reports, and diagnose performance.

## File Activity Policies

### Create File Activity Policy for Sharepoint
- In **Policy Builder for Files**, create a new policy, select **Sharepoint**, define rules, and deploy.

## Distributed Reporting

### Generate Distributed Report
- In **Distributed Report Builder**, select central manager/managed units, choose report type, trigger data collection, and download the report.

## System Configuration Modification

### Change System Settings
- Access **System Configuration**, modify parameters, apply changes (requiring a restart).

## Provisioning External S-TAP

### Connect Databases to External S-TAP
- From **External S-TAP management**, select the provisioned instance, click **Connect Database**, and enter connection details.

## Assigning Roles via GuardAPI

### Grant Role by Name
- Use `grant_role_to_object_by_Name` with object name and role details.

## Example: GuardAPI Role Assignment

### Grant Role by ID
- Use `grant_role_to_object_by_id` with object ID and role details.

## Asset Discovery

### Prepare User Account for Discovery
- In **Unified Discovery and Classification**, connect user account to analyzer, initiate discovery, and monitor progress.

# Compressed Technical Documentation

## Running Outlier Detection
**Components:** CM environment setup  
**Execution Steps:** Execute `enable_outliers_detection` with parameters; verify setting propagation.  
**APIs/Tools:** `enable_outliers_detection`

## GuardApp Event Management
**Components:** Access to GuardAppUserStored  
**Execution Steps:**  
1. Start event with sample commands  
2. Assign type, username, string, numeric, and date values  
3. Close event using `SELECT guardappuserreleased FROM dual`.  
**APIs/Tools:** `SELECT guardappuserreleased FROM dual`

## Data Source Management
**Components:** Datasource Profile Management; CSV export enabled  
**Execution Steps:**  
1. Open Datasource Profile Management  
2. Select profiles  
3. Choose **Export to CSV** and confirm.  
**Customization:** Schedule periodic profile exports for backup.

## Redshift Datasource Configuration
**Components:** Access to Redshift cluster; network connectivity  
**Execution Steps:**  
1. Gather Redshift host, port, database name, and JDBC URL  
2. Configure datasource in Guardium with these parameters  
3. Verify connection.  
**APIs/Tools:** `grdapi create_datasource`

## CyberArk Integration
**Components:** Guardium integrated with CyberArk; credentials configured  
**Execution Steps:**  
1. Install CyberArk Application Password Provider  
2. Configure datasource credentials to be managed by CyberArk  
3. Remove hardcoded credentials from Guardium  
4. Schedule periodic credential rotation via CyberArk.  

## Access Drilldown Control
**Components:** Query results; drilldown configuration permissions  
**Execution Steps:**  
1. Run query and select **Advanced Options**  
2. Open **Drilldown Control** panel  
3. Define target reports and map parameters  
4. Save configuration.  

## Remove a Role
**Components:** Administrator privileges; role not assigned  
**Execution Steps:**  
1. Open **Role Browser**  
2. Select role to remove  
3. Click **Delete** and confirm  
4. Review role form for dependencies.  
**APIs/Tools:** `grdapi delete_role`

## Alias Quick Definition
**Components:** Group Builder; alias naming conventions  
**Execution Steps:**  
1. Initiate group creation/population  
2. Use **Alias Quick Definition** option  
3. Provide alias details  
4. Confirm application.  

## Configure TICKET Notification
**Components:** Ticketing system configured with Guardium; alert criteria  
**Execution Steps:**  
1. In Alert Builder, select **Notification type TICKET**  
2. Configure ticket properties and field mapping  
3. Save and activate alert  
4. Test alert to verify ticket creation.  
**APIs/Tools:** `grdapi add_alert`

## Build Audit Processes
**Components:** Audit process templates; auto_execute_suggested_dependencies enabled  
**Execution Steps:**  
1. Define core audit jobs and dependencies  
2. Enable **auto_execute_suggested_dependencies**  
3. Verify dependent job execution  
4. Review documentation for manual interventions.  
**APIs/Tools:** `grdapi auto_execute_suggested_dependencies`

## Hadoop Monitoring APIs
**Components:** Guardium Hadoop Integration package installed; Hadoop clusters running  
**Execution Steps:**  
1. Update policy rules via Guardium interface  
2. Use API to modify rule parameters  
3. Verify updates propagate to Hadoop monitoring  
4. Test rule effectiveness through sample activity.  
**APIs/Tools:** `grdapi update_rule`

## Manage Audit To-Do List
**Components:** Audit task allocation system configured; `u`  
*(Note: Incomplete entry; no further details available for processing.)*

# Security Roles and Permissions

## Assign Security Roles to a Query
1. Open the **Queries** tab in the Guardium UI  
2. Locate the target query, click **Roles** in its row  
3. In the **Assign Security Roles** dialog, select roles from **Available Roles** and click **Add** to move them to **Assigned Roles**  
4. Click **Save**  

*No API or workflow customization exists for this task.*

---

# Audit Database Setup

## Set Up Audit Database for Informix or Sybase
**Prerequisites**
- Database user account with `SELECT`, `INSERT`, `CREATE` privileges  
- Logged into each monitored database with required rights  

**Steps**
1. Verify user permissions on the audit schema  
2. Connect to each target DB and run scripts to create needed tables (`audit_events`, `audit_fields`) and triggers (`audit_insert_trigger`, etc.)  
3. Validate using `DESCRIBE` and `SHOW TRIGGERS`  

**Tools**
- `grdapi create_audit_schema`  
- DB-specific client (`dbaccess` for Informix, `isql` for Sybase)  

**Customization**
- Store reusable script bundles for bulk deployments  
- Automate user sync after schema changes with `guardapi update_user_db`  

---

# 780. Create MS SQL Server Datasource
**Prerequisites**
- SQL Server installed, reachable over the network  

**Steps**
1. Log in to the Guardium UI with an account that has permission to create datasources  
2. Navigate to **Administration > Managed Systems > Datasources**  
3. Click **New Datasource** and select **Microsoft SQL Server**  
4. Fill in host, port, database name, and credentials  
5. Test the connection, then click **Save**  

*The description was cut off—additional configuration options may exist.*

# Data Source Workspace

## 781. Disable SSH MFA for Users

## 783. Configure Restrictive S-TAP Policy

## 788. Configure Slon Looper from Support Information Gathering Page

### Configure Data Source Group

## Access Control

### Create Custom User and Role for Integration

## Transaction Replay and Performance Monitoring

### Implement Data Replay and Monitoring Workflow

# Consolidated Guardium Operations

## Customization
Create templates for recurring replay and logging tasks to streamline repeated workflow setups.

## Import Management
### Delete LDAP Connection
1. Identify the LDAP connection to remove.  
2. Delete the connection—this permanently erases all imported users from that server.  
3. Confirm the deletion.

## Configuration Management
### Set Must Gather Retention Time
1. Go to **Support Information Results** → **Must Gather Retention**.  
2. Choose a retention period (in days) from the dropdown.  
3. Click **Apply** to update the default retention.

## System Administration
### Manage Guardctl
- `guardctl activate <instance>` – starts A‑TAP.  
- `guardctl deactivate <instance>` – stops A‑TAP (returns 0).  

## Reporting
### Verify Archive Status
1. Navigate to **Manage > Reports > Data Management > Aggregation/Archive Log**.  
2. Ensure the **Status** column for every task reads **Succeeded**.

## Security Management
### Create SR Login Dump Configuration
1. Open the SR configuration interface.  
2. Add a new entry for Oracle.  
3. Set the login dump logging pattern to `BEGIN%`.  

## Security Features
### Quarantine Users with Multiple Failed Logins
1. Access policy settings.  
2. Set **Quarantine Users with Multiple Failed Logins** threshold to **5** attempts.  
3. Define quarantine duration as **30 minutes**.  

## Reporting and Integration
### Use Guardium External Feeds
1. In **External Feeds**, configure the target database connection.  
2. Select reports to forward and test the feed.  
3. Enable the feed.

## API Integration
### Manage Universal Connector Credentials via API
Use the Guardium API endpoints for listing, creating, updating, or deleting credentials, authenticating with API keys or tokens, and verifying changes by querying the credentials list.

## Scheduling
### Schedule LDAP User Import
1. Open **Setup > Data Management > LDAP User Import**.  
2. Click **Schedule**, select recurrence (daily, weekly, …) and start time.  
3. Configure retention policies.  

## Two‑Factor Authentication
### Configure Multi‑Factor Authentication with DUO or RSA SecurID
1. Log in as admin → **Setup > System Settings > Authentication**.  
2. Choose **Two‑Factor Authentication** → **DUO** or **RSA SecurID**.  
3. Enter provider‑specific API credentials.  
4. Test authentication, then save.

## 855. Designate a Guardium Appliance as Central Manager
Log into the CLI of the chosen Guardium appliance with `support`. Run `store unit type manager` to make it the Central Manager. Confirm when prompted. Verify with `show unit type`. Set other appliances as Collectors using `store unit type collector`. Restart the Central Manager with `restart`.

## 856. Create a New Alert in Guardium
From Guardium, open **Reports > Alert Builder**. Click **New Alert**, name it, and select an alert type. Define the rule(s) using alert parameters (e.g., `query > events > event_type = 'Failed login'`). Configure thresholds, set up notifications, review, and click **Save** to enable the alert.

## 857. Diagnose and Fix Alert Builder Issues
Open the failing alert's definition in Alert Builder. Verify query conditions against current data. Clone the current audit process, update the clone with correct parameters, test the new configuration, then rename or delete the original faulty process. Reapply the alert and confirm it functions as expected.

## 858. Secure Cloud Databases via Amazon AWS Data Streams
Create a Service Account for Guardium with Data Streams permissions in AWS. In Guardium, go to **Data Management > Cloud Services > AWS** and enable the AWS Cloud DB account. Set **Audit Type** to **Data Streams** for real-time monitoring. Configure Guardium collectors to ingest data from the AWS stream endpoint and validate data flow.

## 859. Implement a Tailored Data Compliance Framework
Define compliance objectives and controls. Create a **Custom Compliance Program** under **Compliance > Custom Programs**. Import or create policy templates, map data repositories, and schedule automated reports. Review initial status, remediate non-compliant assets, and document the program.

## 860. Duplicate a Privacy Set Definition
Go to **Privacy Sets > Manage Privacy Sets** in Guardium. Select the privacy set to clone, click **Clone**, provide a new name, modify parameters, and save. Describe the cloned set for future reference and assign it to specific data domains.

## 861. Deploy an Edge Gateway for Guardium Insights
On the Central Manager, generate the edge installation bundle using `store edge_installation_bundle`. Download the bundle to a secure location. Connect to the Kubernetes cluster via `kubectl`, create the `guardium-edge` namespace, and deploy the bundle with `kubectl apply -f edge_bundle.yaml`. Verify successful deployment.

## Guardium Edge Gateway Deployment

### Deploy Edge Gateway

- **Components:** `generate_edge_installation_bundle`, `kubectl`, `edge_installation_init`
- **Steps:**
  1. Run `generate_edge_installation_bundle` to create the deployment bundle.
  2. Use `kubectl` to apply the bundle with `kubectl apply -f bundle.yaml`.
  3. Initialize the Edge Gateway via `edge_installation_init`.
  4. Validate the deployment by checking the **Edge Gateway** page in the Guardium UI.
  5. Configure data streams to route high‑volume data to the Edge Gateway.
  6. Monitor initial data flow and troubleshoot any connection issues.
- **Customization:** Define resource limits for the Edge Gateway node based on expected traffic.

## Prerequisites for Audit Process Creation
- Guardium installed and data sources defined.

## Create New Audit Process
1. Configure > Auditing > Audit Processes
2. Click **Create New Audit Process**
3. Define scope (databases, tables, records)  
   Set audit criteria (select, insert, update, delete)  
   Schedule the process and attach reports/alerts.

## Managed Units Alert Dashboard
1. Dashboards > Managed Units Alert  
   Review vulnerability test failures, login failures, data traffic volume, error rates.  
2. Investigate red or yellow indicators.  
3. Click a collector to view its health details.

## Refresh Quick‑Search Groups via API
- Prerequisites: Central Manager and target guards connected.  
- Command: `refresh_quick_search_groups` (no parameters).  
- Verify groups appear under **Manage > Quick Search**.

## remove_datasource_from_group API
- Prerequisites: Data mart defined and active profile.  
- Command: `remove_datasource_from_group` (no parameters).  
- The command also unschedules the DM if the profile is active.

## Pre‑Installation Checks for Unified Discovery and Classification
1. Verify hardware meets minimum requirements (CPU, memory, disk).  
2. Extract the installation archive; locate the **license** folder.  
3. Review product notices and compliance terms.

## FAM for NAS and SharePoint (LOG ONLY)
- No executable steps documented.

## Define a Discover Sensitive Data Task
1. Open Sensitive Data Discovery.  
2. Select **New Task → Discover Sensitive Data**.  
3. Configure parameters per scenario.  
4. Submit to run discovery.

## Open CAS Configuration Navigator
1. Click **Harden** → **Configuration Change Control (CAS Application)**.  
2. Choose **CAS Template Set Configuration**.  
3. Create or modify CAS Template Sets.

## Import Data from Collector to Aggregator
1. Access **Import Data** in Aggregator.  
2. Select exported Collector files.  
3. Initiate import – data decrypts and merges.  
4. Verify by checking database contents.  
- Optional: `grdapi import_data`.

## Delete Assessment Test (CLI)
`delete_assessment_test assessment_name=<name> test_description=<desc>`  
- Error 1308 if the description is invalid.

## Delete Specific Audit Results via API
Call the delete‑audit endpoint with `ExecutionDateFromString`, `ExecutionDateTo`, `ProcessName`.

## Understanding Policies
Policies contain rule types, categories, classifications, minimum counts, reset intervals, violation values, regular‑expression patterns, special‑pattern tests, and logging mechanisms for flat rules.

## Cloud Database Service Protection
**Guardium supports protection of Azure Event Hubs cloud databases using data streams. Define a cloud DB service account with Data Streams capabilities and enable Guardium collectors to monitor Azure Event Hubs for comprehensive audit trails.**

## Enable Monitoring for Event Hub
**Steps to enable monitoring:**
1. Open the IBM Guardium interface.
2. Navigate to Event Hubs management.
3. Select the disabled hub and click **Enable Monitoring**.

## Fix Central for Guardium Fixes
**Fix Central provides a platform for searching, selecting, ordering, and downloading recommended fixes for IBM products, including Guardium. Multiple delivery options are available to suit different deployment scenarios.**

## Incident Management with LDAP User Import
**Steps to import LDAP users:**
1. Ensure LDAP server configuration is completed.
2. Use CLI command `execute_ldap_user_import` to import user definitions into Guardium.

## S-TAP and Inspection Engine APIs
### Revoke Role from Object by Name
**Execute API `revoke_role_from_object_by_Name` with role name and object name to revoke role and handle dependencies automatically.**

### Revoke Role from Object by ID
**Execute API `revoke_role_from_object_by_id` with role ID and object ID to revoke role and handle dependencies automatically.**

## REST API: Start/Stop Application
**Make a REST POST call to `start_stop_application` API endpoint with `appId` and `action` ('start' or 'stop') to start or stop the specified application.**

## Proactive Vulnerability Management
**Steps to configure vulnerability assessment tracking:**
1. Open **Setup > Tools and Views > Vulnerability Assessment**.
2. Define scanner connections under **Scanners > Add Scanner**.
3. Schedule assessments via **Schedule > Add Schedule**.
4. Enable alerting under **Administration > Alerting > Vulnerability Alerts**.

## Deploy and Manage CyberArk KDC Definitions
Export KDC configuration from CyberArk, import to Guardium, test credential usability.

## Monitor Amazon Neptune Clusters
Add Neptune datasource, enter endpoint and IAM credentials.

## Modify API-Report Assignments
Assign APIs to reports, save and test execution.

## Generate Ordered Exception Records
Execute SQL query to select exception view records within date range, ordered by timestamp.

## Trigger Incident via Query Execution
Run `grdapi execute_incidentGenProcess` with the policy-violation query identifier.

## Add Tagging to Rule Definitions
`grdapi add_classification_rule tag="ComplianceCheck" rule=<RULE_ID>`

## Add Tags to Policy Rules
In policy rule editor, enter tag names, save changes.

## Create NAS File Activity Policies
Define new file activity policy, select NAS, specify hosts, save policy.

## Enable or disable dashboard functionality
In System Settings, toggle dashboard switch, save configuration.

## Configure FGAC
Create roles, assign permissions, map to user accounts, activate and test.

## Remove a Cloud DB Service Account
Delete account from Cloud DB Service Accounts, confirm and verify.

## Manage Inspection Engines on Managed Units
Review permissions, roles, and group memberships for inspection engines.

```markdown
## Security Policy Enhancements
- **Build MS‑SQL Extended Procedures Allowed List**
  - Components:
    - Pre‑requisites: GIM client installed; MS‑SQL instance discovered
    - Execution Steps: 
      1. Setup → Tools and Views → Builder → MS‑SQL Extended
      2. Define privileged stored procedures
      3. Move procedures to **Allowed** group
      4. Apply policy to assessment schedules
    - API: `grdapi set_user_variable`

## Security Workflow Operations
- **Execute Partition Fix During Guardium Install**
  - Components:
    - Pre‑requisites: Installation ISO/package; root/sudo access
    - Execution Steps:
      1. Choose Custom installation
      2. Manually allocate disk partitions matching required sizes
      3. Verify MD5 checksum of patch file after download
      4. Proceed with installation; monitor logs for errors
  - API: No Guardium API (GUI‑driven)

## Access Management
- **Add an Entity to a Guardium Group**
  - Components:
    - Pre‑requisites: Identify target entity (IP, database, user, etc.)
    - Execution Steps:
      1. Guardium Groups → Add to Group
      2. Select entity type, specify identifier
      3. Choose or create a group
      4. Confirm addition, validate membership visibility
  - API: `grdapi add_to_group`

## Session-Level Policy Management
- **Configure Advanced Session-Level Policies**
  - Components:
    - Pre‑requisites: SR script environment set up; policies defined
    - Execution Steps:
      1. Start SR script engine from console
      2. Define new Session‑Level Policy for packet validation
      3. Add data transformation script
      4. Configure routing back to S‑TAP
      5. Activate policy, monitor session metrics
  - APIs: `SR_SCRAPI execute_policy`, `grdapi modify_policy`

## S‑TAP Deployment
- **Deploy External S‑TAP Using an Operator**
  - Components:
    - Pre‑requisites: Kubernetes cluster, CASE operator, IBM Cloud Container Registry access
    - Execution Steps:
      1. Authenticate to IBM Cloud and private registry
      2. Mirror Guardium External S‑TAP images via CASE CLI
      3. Deploy S‑TAP resources with Kubernetes manifests
      4. Validate deployment and reporting to Cloud Pak for Data
  - Tools: CASE CLI (`ibmcloud cr login`, `cloudctl case save`), `kubectl`/`oc`, Kubernetes manifests

## Investigation Dashboard Configurations
- **Enable Investigation Dashboard Feature**
  - Components:
    - Pre‑requisites: (crawler) or FamMonitor running on monitored servers; network connectivity verified
    - Execution Steps:
      1. Verify (crawler) or FamMonitor is active
      2. Ensure server configuration is correct
      3. Enable Investigation Dashboard in Guardium UI
  - API: Guardium UI settings only

## GuardAPI Reference
- **Delete Allowed DB by User Mappings**
  - Components:
    - Pre‑requisites: GuardAPI environment configured; required permissions
    - Execution Steps:
      1. Open GuardAPI console
      2. Run `grdapi delete_allowed_db_by_user` with `userName` parameter
      3. Confirm result
  - API: No additional tools required
```

## Remove Mappings for a User
- **APIs/Tools:** GuardAPI `grdapi delete_allowed_db_by_user`
- **Type:** Action
- **Customization:** Integrate into scripts for automated access cleanup

## Configure MS SQL Datasource
- **Pre-requisites:** SQL Server running, network reachable
- **Steps:** 
  1. Collect hostname, port, auth method
  2. Add datasource, select type, input details, test, save
- **APIs/Tools:** `grdapi add_datasource`
- **Type:** Configuration
- **Customization:** Clone template for repeated setups

## Connect to SaaS/Cloud
- **Prerequisite:** Unified Discovery and Classification enabled
- **Steps:**
  1. Settings → Connections → Add Connection → SaaS/Cloud
  2. Fill credentials, authorize, verify status, save
- **APIs/Tools:** `grdapi add_cloud_connection`
- **Type:** Configuration

## Deploy CAS
- **Pre-requisites:** Guardium installed, network connectivity
- **Steps:** 
  1. Configure CAS Deployment
  2. Select DB Type, OS Name
  3. Enter Hostname, OS Type
  4. Save
- **Type:** Configuration

## View DBCC Execution Report
- **Prerequisite:** DBCC captured, reporting access
- **Steps:** 
  1. View Reports → DBCC Execution
  2. Pick time range or date
  3. Review details, filter as needed
- **Type:** Navigation

## Edit User Account
- **Prerequisite:** Admin role, existing user
- **Steps:** 
  1. User Browser → locate user → Edit icon
  2. Modify role, email, status, etc.
  3. Save changes; for passwords use Immediate Reset
- **Type:** Configuration

## Verify S-TAP Agents
- **Pre-requisite:** S-TAP installed, verification schedule set
- **Steps:** 
  1. S-TAP Verification Schedules
  2. Review/create schedule
  3. Set frequency, target agents
  4. Activate schedule
- **Type:** Action

## Prepare for Linux-UNIX S-TAP
- **Steps:** 
  1. Verify system meets requirements
  2. Download installer from Fix Central or Guardium rep
  3. Identify OS-specific script name
  4. Follow Guardium install guide
- **Type:** Action

## Delete Privacy Set
- **Prerequisite:** No active audit, admin access
- **Steps:** 
  1. Privacy Set Management → select set → delete → confirm
  2. Check affected processes
- **Type:** Configuration

## Open CAS Configuration Navigator
Navigate to Harden > Configuration Change Control > CAS Host Configuration and open the CAS Configuration Navigator to create or modify CAS host configurations.

## Configure NIC Bonding
Log into the server via CLI, execute commands to add a bond interface, add primary and secondary NICs to the bond, and bring the bond interface up.

## Reactivate User Account
Open User Browser, find the disabled account, uncheck the Disabled checkbox, optionally set a new temporary password, and save changes to reactivate the account.

## Adjust Policy Rules for Exceptions
Open Policy Builder, create an exception rule before the failed-login rule, define conditions for exceptions, save and activate the updated policy.

## Show Log Object Join Info
Open Guardium CLI and run `show log object_join_info` to observe the enabled/disabled status in the response.

## Retrieve DB2 for IBM i S-TAP Config
Open Guardium CLI, execute `grdapi get_istap_config datasourceName=<IP>`, and review the returned configuration output.

## Enable Cloud Native Auditing
Navigate to Setup > Cloud Services, enable native audit configuration for supported DBaaS, activate classification and vulnerability assessment modules, and schedule regular audit reviews.

## Install Session-Level Policy
Open Setup > Security Policies, select policy > Install > Session-Level Installation, choose target instances, and confirm installation.

## Remove Correlation Alert
Open Alert Finder, locate alert by name or ID, select > Delete, and confirm removal prompt.

## Create Role
Open Role Browser, click Add Role, enter unique role name, and click Add Role again to confirm.

## Restore Guardium Insights Certificate
Navigate to Configuration > Security > Certificates, select Restore Default Certificate, and confirm operation.

## Complete Audit Process
Ensure custom tables have current data, schedule audit run via Reports > Schedule, verify completion notification, and access results in Audit Process Reports.

## Add Hostname for IP Aliasing
Open Tools > Hostname Aliasing, enter IP and desired alias, save configuration, and test resolution.

# Guardium Technical Documentation

## Data Correlation

Drill into usage metrics and correlate with external logs via **Tools > Data Correlation**. Resolve bottlenecks and verify improvements.

**Types:** Configuration  
**APIs/Tools:** `display_health_topology`, `correlate_data` GuardAPI

## Report Management

Edit time period for a report. Required: an existing time period. Steps: open Setup > Reports > Time Period Builder, select and edit the period, modify dates/interval, click OK.

**Types:** Configuration  
**APIs/Tools:** `edit_time_period` GuardAPI, `/reports/timeperiod/edit` REST endpoint

## GuardAPI Reference

Register an Edge device. Required: device connection and API credentials. Procedure: prepare JSON payload, send POST to `https://<Guardium>/api/registration/registerEdge`, handle response, validate status.

**Types:** Action  
**APIs/Tools:** `registerEdge` GuardAPI, `/api/registration/registerEdge` REST

## Service Account Management

Configure Polar Installation account. Required: IAM access and Polar service enabled. Steps: create service account in IAM, assign Cloud Analyzer roles, store credentials securely, configure Guardium to use account for Polar updates.

**Types:** Configuration  
**APIs/Tools:** IAM Create Service Account, Guardium Cloud Service configuration

## Installation Guides

Install Guardium on a Virtual Appliance. Required: virtual environment and Guardium ISO. Procedure: upload ISO to hypervisor, create VM from ISO, configure network, complete setup wizard.

**Types:** Configuration  
**APIs/Tools:** Hypervisor tools, Guardium setup wizard

## Security Configuration

Configure Runtime Sensitive Object Identifier policy. Required: admin access and an existing policy to copy. Procedure: navigate to Policies > Runtime Sensitive Object Identifier, copy the policy, rename and save, modify conditions/actions/filters per *Creating session-level and advanced session-level policies* guidelines, activate the policy. Optional: save modified policy as a template.

**Types:** Configuration  
**APIs/Tools:** `grdapi modify_policy`  
**Customization:** User workflows: store modified policy as a template for reuse.

## Incident Management

Add comments to an incident. Required: open incident in UI. Steps: double-click incident, select Comments tab, click User Comment, enter text, click Add.

**Types:** Action  
**Customization:** User workflows: create standard comment template for common incident types

## Data Management

Verify purge operation success. Required: completed purge. Steps: open Manage > Reports > Data Management > Aggregation/Archive Log, ensure all activities show Succeeded status.

**Types:** Action  
**Customization:** User workflows: schedule regular purge verification via automated reports

## Email Security

Configure Mail Encryption (S/MIME). Required: certificates for Guardium and recipients, admin access. Steps: obtain and import system and recipient certificates, navigate to Setup > Cryptography > S/MIME Settings, configure signing/encryption options, test encryption with a recipient.

**Types:** Configuration  
**APIs/Tools:** `grdapi set_smime_config`  
**Customization:** User workflows: checklist for onboarding new recipients

## Configuration Management

Export/Import Configuration Profiles. Required: central manager access and profiles to migrate. Procedure: navigate to Definitions > Export Definitions, select Configuration Profile and profiles, export to secure location; on target central manager, go to Definitions > Import Definitions, select exported profile and import.

**Types:** Configuration  
**APIs/Tools:** `grdapi export_definitions`, `grdapi import_definitions`  
**Customization:** User workflows: automate profile synchronization between central managers

## Database Inspection

Configure Inspection Engine Alerts. Required: configured inspection engine and admin access. Steps: open Data Management > Inspection Engine, select engine, go to Reports/Alerts, configure alerts (e.g., policy violations, high activity), set recipients and notification methods, activate monitoring.

**Types:** Configuration  
**APIs/Tools:** `grdapi set_inspection_alert`  
**Customization:** User workflows: define standard alert sets for different database types

## Certificate Management

Verify Certificate Distribution. Required: certificates distributed via Guardium. Procedure: open terminal on central manager, run `comm`.

## Database Connectivity

**Summary:** Verify service connection parameters for Guardium data sources.

### Verify Service Connection Parameters
- **Prerequisites:** Database server running; connection details known
- **Steps:**
  1. Identify Host Name or IP Address
  2. Note Port number (default: 1521)
  3. Obtain Service Name for the target database
  4. Confirm Schema name (if applicable)
  5. Test connection using Guardium UI or CLI: `grdapi test_db_connection`
- **Tools:** grdapi test_db_connection
- **Types:** Configuration
- **Customization:** Store parameter templates for different database types

## QASD Import
Navigate to **Datasources > Add Datasource**, select the connection type, enter the hostname, port, and authentication details for the QASD, test the connection, and save the configuration.

## Admin Users Login
1. Ensure auditing is enabled for the Admin Users group.
2. Go to **Reports > Admin Users Login**.
3. Filter by date range, DB user name, client IP, or source program.
4. Review session start times and counts.

## Query-based Tests
1. Define custom test criteria or select predefined SQL tests.
2. Execute the test in the UI.
3. Review the results.

## Applying Upgrade Patch
1. Access **System Configuration > Upgrade Manager**.
2. Select **Install Patch** and choose the upgrade file source.
3. Follow prompts to complete installation.

## Threat Diagnostic Dashboards
1. Open the Suspected malicious STP Cases or Suspicion SQL Injection Attacks report.
2. Launch the threat diagnostic dashboard for the selected case.
3. Analyze the threat nature and scope.

## Database and Collector Connectivity Issues

### Enable or Disable Active Alerts
- Navigate to **Protect → Database Intrusion Detection → Alert Builder**.
- Select an alert, clear the **Active** checkbox to disable it globally, then click **Save**.

## Diagnosing the Problem

### Configure MS SQL Server Datasource
- Gather SQL Server hostname, port, and authentication method.
- In Guardium UI, go to **Datasources → Add Datasource** and choose SQL Server as the connection type.
- Fill in the collected details, click **Test Connection**, then **Save**.
- Alternative API: `grdapi add_datasource`.

## Guardium Operations

### Configure MS SQL Server Datasource
*Same steps and API as above.*

## Feature Workflows

### Create Role with Minimal Access
- Open **Setup → Access Control → FGAC**.
- Define a role, assign minimal object-level permissions, and associate it with users.

### Auditor Role with Limited Access
- Follow the same steps as "Create Role" but restrict the role to the Audit Process To-Do List and only specified reports.
- Verify limited access by testing with an auditor user account.

### Export Audit Process Results
- Go to **Administration → Export → Audit Data**.
- Choose the Central Manager as source and Managed Units as target, then schedule and confirm the export of required data types.

### S-TAP Agent Upgrade in Managed Environment
- In the **GIM Setup** of each Managed Unit, navigate to **Upgrades → S-TAP Agents**.
- Select the agents to upgrade, start the upgrade process, and monitor its success.
- For UNIX agents, refer to the platform-specific documentation.

### Certificates Distribution
- Access **Administration → Certificates**.
- Choose **Distribute Certificate**, select target Managed Units, and confirm the distribution.
- Restart the GUI service if required.

### Deploy Policy and Rules
- Use **Policy Builder** to create a new policy with required rules.
- Save and deploy to the targeted Guardium units.
- Validate using the **Policy Status** tab and audit simulations.

### Hadoop Monitoring Configuration
- In **Datasources → Add Datasource**, select Hadoop and input connection parameters.
- Enable monitoring through **Configure → Monitoring**.
- Confirm data collection by running sample queries.

### Verify Backup Success
- Navigate to **Manage → Reports → Data Management → Aggregation/Archive Log**.
- Check the latest backup entry; the status should be "Succeeded" and review the summary statistics.

## Deployment Health Views
*Incomplete prompt fragment; no further content provided.*

## Backing up a Managed Unit

- **Pre-requisites:** Central Manager access; Managed Unit configured in Central Manager; sufficient storage on Central Manager
- **Execution Steps:** 1. Navigate to **Manage > Units > Backup**; 2. Select the Managed Unit; 3. Initiate backup process; 4. Monitor backup status; 5. Verify backup completion
- **APIs/Tools:** CLI command `create-backup`; REST API `backup-managed-unit`
- **Customization:** Schedule regular backups; store backups remotely

pliance Supervision
- **Components:**
  - **Prerequisites:** Guardium system with ClasSup tool enabled
  - **Steps:**
    1. Log into the Guardium UI
    2. Navigate to Manage > Monitoring > ClasSup
    3. Select the ClasSup profile
    4. Set **Match‑Continue** to **Enabled**
    5. Save changes
- **Purpose:** Allows continued monitoring after a match is found
- **API:** `grdapi enable_match_continue`

## Classification Policies

Configure a classification rule to evaluate subsequent rules regardless of outcome.

1. Open the classification policy.  
2. Select the rule to modify.  
3. Enable **Continue on Match**.  
4. Save.

*Type:* Configuration  

*Note:* No APIs/tools required. No user workflows.

## Guardium Portal Configuration

Configure portal settings such as port, SSL certificates, and authentication.

1. Go to **Portal Settings**.  
2. Adjust the web server port.  
3. Import SSL certificates via **Security Settings**.  
4. Set authentication mechanisms.  
5. Apply changes and restart portal services.

*Type:* Configuration  

*Note:* No prerequisites beyond administrative access; no APIs/tools; no user workflows.

## REST API Operations in Guardium

Access Guardium via REST APIs.

- **Add User Hierarchy:** `POST /restAPI/user_hierarchy` with `parentUserName` and `userName`.  
- **Retrieve Reports:** `GET /restAPI/list_all_reports`.  
- **List CAS Hosts:** `GET /restAPI/cas_host?osType=UNX`.  

*Type:* Action  

*Note:* Requires API user credentials and network access; no user workflows.

## Implement Advanced Data Security Monitoring Policy

Enable advanced monitoring for SQL traffic.

1. Navigate to **Setup > Data Security > Monitoring Policies**.  
2. Create a new **Advanced Data Security Monitoring Policy**.  
3. Enable for required SQL traffic sources.  
4. Configure logging, alert thresholds, and notification recipients.  
5. Activate the policy.

*APIs/Tools:* `add_policy`, `modify_policy`, `activate_policy`  

*Type:* Configuration  

*Note:* Customize by cloning for different environments and adjusting thresholds.

## Configure System Backup

Set up system backups.

1. Go to **Administration > System Settings > Backup/Restore**.  
2. Choose backup destination (local, remote, or cloud).  
3. Define backup schedule (daily, weekly, custom).  
4. Review and select data/configuration elements.  
5. Save configuration.

*Note:* No APIs/tools; no prerequisites beyond administrator access; no user workflows.

## Generate User Activity Audit Trail

Generate audit reports of user actions.

1. Open **Reports > User Activity Audit Trail**.  
2. Select **Recent Activity** or **Historical Activity**.  
3. Click **Generate Summary** for third‑party analysis if needed.  
4. Export or schedule the report.

*Note:* Requires audit trail configuration; no APIs/tools; no prerequisites; no user workflows.

## Schedule Predefined Data Extraction to File

Automate data extraction to a file.

```
grdapi schedule_predefined_extraction_to_file
    name="<extraction_name>"
    schedule="* 2 * * *"   # cron-style schedule
```

Verify with `grdapi get_scheduled_extractions`.  

*APIs/Tools:* `schedule_predefined_extraction_to_file`, `get_scheduled_extractions`  

*Type:* Action  

*Note:* Requires predefined extraction jobs and API access; no user workflows.

## Add Custom Comments to Vulnerability Assessment Tests

Add explanatory notes to VA tests.

1. Open the VA test in the Guardium console.  
2. Enter text in the **Comments** section at the bottom.  
3. Save the test.  
4. Export the configuration to include comments.

*APIs/Tools:* None  

*Type:* Customization  

*Note:* Customization workflow includes export/import of test configurations to propagate comments across Guardium instances.

## Use Spotter for System‑wide Risk Visualizations

Visualize system-wide risk data.

1. Open the Spotter dashboard.  
2. Select desired risk visualization tiles (e.g., top risky users, risk trends).  
3. Apply filters for time windows and scope.  
4. Export or schedule the report for daily review.  

*Note:* SPOTTER feature must be enabled; no APIs/tools (UI-only); customized by pinning frequently used tiles to personal dashboards.

## Knowledge & Customized Workflows

### Modify a Privacy Set
**Components:** User has edit role; existing privacy set selected.  
**Steps:** Navigate to *Privacy Sets*, select set, click *Modify*, adjust fields/filters, save and confirm.  
**API:** `grdapi modify_privacy_set`  
**Workflow:** Save modified set as reusable template.

## Knowledge & Features

### Customize Report Display
**Components:** Report view loaded; reporting privileges.  
**Steps:** Open report in edit mode, select format, reorder/rename columns, apply visualization settings, save layout.  
**API:** None (UI‑only)  
**Workflow:** Create reusable report templates.

## Configuration

### Configure ECS/S3 Compatible Target for Archive or Backup
**Components:** Guardium v12.1+; ECS/S3 credentials.  
**Steps:** In UI, enable *ECS/S3 Compatible* option, enter host, keys, bucket, test connection, save and schedule.  
**API:** `add_archive_destination`  
**Workflow:** System‑wide setting; no specific user workflows.

## Knowledge & Workflows

### Re‑populate Entitlement Data after CM Switch
**Components:** New CM active; entitlement reports configured.  
**Steps:** Run collection reports on new CM, verify dashboard, manually refresh if needed, test historical data restoration.  
**API:** `refresh_entitlement_data`  
**Workflow:** Schedule nightly refresh during low usage.

## Features & Workflows

### Enable and Configure Customer Uploads
**Components:** GDPS license; upload files ready.  
**Steps:** Upload files via *Customer Uploads* UI, confirm success, deploy to instances.  
**API:** `upload_customer_file`  
**Workflow:** Automate bulk driver updates with scheduled scripts.

## Action

### Replace Default GIM Certificate (SHA1 / SHA256)
**Components:** Admin access; new certificate files.  
**Steps:** Open *GIM Certificates*, replace with new file, confirm propagation, monitor client logs.  
**API:** `replace_gim_cert`  
**Workflow:** Script quarterly certificate rotation.

## Features

### Support RestAPI `remove_all_qr_replace_elements`
**Components:** REST API access; auth token.  
**Steps:** Send DELETE request to `/api/v1/qr/replacements`, verify removal.  
**API:** `POST /api/v1/qr/replacements?action=delete_all`  
**Workflow:** Integrate into automated policy refresh pipelines.

## Workflows

### Perform In‑Place Upgrade of Unified Discovery and Classification
**Components:** Backup of classification data; compatible Guardium version.  
**Steps:** Download upgrade package, run installer with in‑place option, monitor log, run test classification post‑upgrade.  
**API:** `upgrade_discovery_classification`  
**Workflow:** Standard upgrade path; no user customization.

## Keywords & Features

### Understand Field Descriptions in Oracle Configurations
**Components:** Access to policy editor; Oracle data source.  
**Steps:** Open Oracle definition, locate *Account names* and *Directory* fields, note optional *Directory* defaults to `$ORACLE_HOME`.  
**API:** None (UI‑only)  
**Workflow:** Document custom field usage in SOPs.

## Entities & Workflows

### Manage CyberArk Account Permissions for Guardium
**Components:** CyberArk vault access; Guardium admin credentials.  
**Steps:** Open CyberArk console, find Guardium service account, assign/revoke permissions.

## Features & Workflows

### Define Session‑level Policies
- **Execution Steps:** Navigate to Policies > Create New Policy, choose Session‑level, define conditions, specify actions, activate, and monitor.
- **API:** `grdapi create_session_policy`
- **Customization:** Build reusable rule templates for high‑risk applications.

## Data Protection Workflows

### Creating dashboards and adding reports
- **Execution Steps:** Go to Reports and Dashboards > Dashboards, click New Dashboard, add reports, configure parameters, save, and verify.
- **APIs:** `add_dashboard`, `add_dashboard_report`, `update_report_element`
- **Customization:** Duplicate existing dashboard template for rapid reuse.

### Distribute Configurations
- **Execution Steps:** Access Administration > Distribute Configurations, select configuration type, choose managed units, initiate distribution, monitor progress, and verify.
- **APIs:** `distribute_config`, `apply_configuration`
- **Customization:** None.

### Unregistering a Managed Unit
- **Execution Steps:** Open Administration > Managed Units, locate unit, click Unregister, confirm, and verify removal.
- **API:** `unregister_managed_unit`
- **Customization:** None.

### Distribute Configurations (Repeated)
- **Execution Steps:** Same as above.
- **APIs:** Same as above.
- **Customization:** None.

## Central Manager Redundancy

### Configure Secondary Central Manager
- **Execution Steps:** Install Guardium on secondary system, run Redundancy wizard, select Backup Central Manager, specify primary IP, complete configuration, and verify failover.
- **CLI:** `mgrsetup.sh --backup`
- **Customization:** Clone configuration for additional backups.

## Resolving the Problem

### Enable K-TAP Live Update
- **Execution Steps:** Log in as cli, run `configure ktap --live-update enable`, reinstall S-TAP, and reboot.
- **Tools:** `ktapctl`, `stapctl`
- **Customization:** None.

## What to Do Next

### Blocklist Untrusted Certificate
- **Execution Steps:** Go to Certificates > Blocklist, add certificate hash, apply changes, and restart External S-TAP.
- **CLI:** `mgrctl --ext-stap config blocklist add <hash>`
- **Customization:** Create scripts to automate updates.

## Backing Up a Central Manager

### Backup Procedure
- **Execution Steps:** Access Backup/Restore, choose Central Manager Backup, specify destination, start, and verify completion.
- **CLI:** `mgrbackup.sh`
- **Customization:** Create cron job for automated backups.

## Applying the Upgrade Patch on Managed Units

### Distributed Patch Management
- **Execution Steps:** Upload patch to Aggregator, select Distribute Patch via GUI, choose Collectors, approve, monitor status, and validate.
- **CLI:** `guardium patch install`
- **Customization:** None.

## API `guardapi apply_patch`
**Configures**: Script to drive patch rollout across environments.

## Apply Upgrade Patch Centrally
Upload patch to central manager, select Deploy to Managed Units, confirm deployment, and monitor progress via GUI.

## REST API Examples
Modify request payloads for specific use cases; see individual entries.

## Exception Handling Workflow
Update test detail exception via `update_test_detail_exception` API, verify through Guardium interface.

## User Identification Workflow
Configure User Identification, map users via API or stored procedures, enable Value Change Auditing, and verify with test queries.

## Active Threat Analytics Optimization
Configure exclusion settings to reduce noise and focus on relevant threats.

## Session-Level Rule Scheduling
Set active time ranges for SESSION_START function in policy rules to enforce time-based enforcement.

## Anomaly Detection Management
Stop and restart anomaly detection services via the Guardium web interface.

## OLM Operator Installation
Prepare configuration files, specify location, create subscription using OpenShift CLI, verify installation via OLM dashboard.

## Change Tracker REST API
Retrieve event data via `change_tracker_get_events` endpoint and integrate into reporting systems.

## Change Tracker Parameters API
Retrieve configuration parameters via `change_tracker_get_params` endpoint.

## Change Tracker Configuration

- Configure Change Tracker parameters to control monitoring and reporting.
- Use `GET /restAPI/change_tracker_get_params` to view current settings.

## Delete SNMP Alerting Configurations

- Remove SNMP alert definitions via API.
- **API**: `DELETE /restAPI/delete_alerter_snmp`
- Verify deletion through Guardium UI.

## Delete Inactive S-TAP Agents

- Remove inactive S-TAPs using POST request.
- **API**: `POST /restAPI/delete_inactive_stap`
- Confirm removal by checking Guardium inventory and logs.

## Remove Unused GIM Bundles

- Clean up GIM repositories.
- Steps:
  1. Navigate to **Administration > GIM > Bundles**
  2. Select and remove unused bundles.
  3. Restart GIM services on all units.

## Plan File Activity Monitoring

- Define objectives and configure collectors for FAM.
- Steps:
  1. Identify monitoring goals.
  2. Configure collector agents.
  3. Schedule data collection and review reports.

## Navigate to Scheduling

- Move discovery data to scheduling workflow.
- Steps:
  1. Select **Scheduling** from dashboard.
  2. Import discovery results.
  3. Create schedules for periodic checks.

## Create and Manage Correlation Alerts

- Set up correlation alerts for policy violations.
- Steps:
  1. Add correlation alert in **Activity > Correlation Alerts**.
  2. Define triggering conditions and recipients.
  3. Save and enable the alert.

## Enable Active Threat Analytics

- Deploy ATLAS for threat detection.
- Steps:
  1. Enable ATLAS from **Activities > Active Threat Analytics**.
  2. Configure detection policies and alerts.
  3. Monitor threats from the dashboard.

## Close Exclude Items

- Resolve and close excluded ATLAS cases.
- Steps:
  1. Select items to close in **ATLAS > Items to Exclude**.
  2. Confirm closure and review closed items list.

## Run Security Assessments

- Execute security assessment templates.
- Steps:
  1. Select templates and target data sources in **Assessment > Run Assessment**.
  2. Configure assessment scope.
  3. Review results and prioritize remediation.

## Central Manager Restoration

### Rebuild Central Manager from Backup
1. Boot new hardware with Guardium rescue media.
2. Select **Restore from Backup** and follow the wizard.
3. Verify restored system integrity, network settings, and managed unit enrollment.
4. Use `grdapi restore_system` for automated restores.

## LDAP User Import

### Bring LDAP Users into Guardium
1. Navigate to **Administration > LDAP Integration** and select **Import Users**.
2. Enter LDAP server details and map attributes.
3. Choose synchronization frequency and save the configuration.
4. Use `grdapi import_ldap_users` for automation.

## Certificate Renewal

### Manage Expiring Certificates
1. Go to **Administration > Certificate Management**.
2. Select expiring certificates and click **Renew**.
3. Upload new certificates or generate new ones.
4. Propagate certificates to all managed units and verify service health.
5. Use `grdapi renew_certificate` and `grdapi distribute_certificate` for automation.

## SSL Configuration for S-TAP

### Enable SSL for S-TAP Connections
1. Navigate to **Configuration > S-TAP > SSL Settings**.
2. Upload the server SSL certificate and private key.
3. Enable **TLS Mandatory** mode and test the connection.
4. Redeploy affected S-TAP agents if needed.
5. Use `grdapi set_ssl_config` and `grdapi test_ssl_connection` for automation.

## Group Membership Reporting

### Examine Group Usage
1. Open **Access Control > Groups > View Membership**.
2. Search for a group and review member lists and usage statistics.
3. Export group details for reporting and audit compliance.
4. Use `grdapi view_group_memberships` for automation.

## LDAP Import Scheduling

### Schedule LDAP User Imports
1. In **Administration > LDAP Integration**, select **Schedule Import**.
2. Set the import frequency and run the immediate sync if needed.
3. Confirm successful imports by checking activity logs.
4. Use `grdapi schedule_ldap_import` for automation.

## Rule Threshold Configuration

### Configure Thresholds for Policy Rules
1. Use the `add_threshold_to_rule` API endpoint.
2. Supply policy rule ID and threshold parameters in the request body.
3. Verify successful addition through the API response.

## Assessment Management

### Delete a Security Assessment Test
1. Use the `delete_assessment_test` endpoint with the assessment description.
2. Submit the request to `https://[host]:8443/restAPI/computed_attribute`.

### Terminate an Audit Process
1. Use the `delete_audit_process` endpoint with the audit process ID or name.
2. Submit the DELETE request to `https://[host]:8443/restAPI/delete_audit_process`.

### Enable Persistent Queue
1. Ensure the persistent queue feature is needed and enabled.
2. Issue a GET request to enable the persistent queue.

# Technical Reference

## Enable Persistent Queue
- Send a GET request to `https://[Guardium hostname or IP address]:8443/restAPI/enablePersistentQueue` to enable the queue and verify the response confirms it is active.

## Enable Quick Search
- Use `PUT https://[Guardium hostname or IP address]:8443/restAPI/enable_quick_search` to activate quick search and confirm success in the response.

## Update Guardium Inspection Module Parameter
- Send parameter updates to `gim_update_client_params` to modify client parameters and receive confirmation of the change.

## Delete FAM Policy Rule
- Delete a policy rule via `DELETE https://[Guardium hostname or IP address]:8443/restAPI/famPolicyRule` and verify removal.

## Uninstall Policy
- Call `policy_uninstall` to uninstall a policy and confirm success from the response.

## Delete Connection Properties
- Invoke `remove_connection_properties` to delete specified connection properties and validate deletion.

## Retrieve Updated Users
- Use `runUniversalConnector` with a specified date to fetch users updated since that date.

## Import LDAP Users to Custom Table
- Submit LDAP users for import using `run_custom_table_ldap_import` and verify completion.

## List Logstash Plugins
- Retrieve available Logstash plugins with `GET https://[host]:8443/restAPI/showLogstashPlugins`.

## Start Istap Monitor
- Activate Istap monitor by sending a PUT request to `https://<guardium_host>/restAPI/start_istap_monitor` with authentication headers.

## Setup Real‑Time Alerts
*Define and save alerts that trigger actions such as email, syslog, or ticketing.*  

- **Execution Steps:** Navigate to **Setup > Alerts > Real‑Time Alerts**, click **Add Alert**, select the policy, define trigger condition(s), choose response action(s), then save.  
- **APIs/Tools:** `grdapi create_alert_rule`, GuardAPI `create_alert_rule`  

---

## Set Unit Type (Federated Setup)
*Assign each appliance as a central manager or managed unit.*  

- **Pre‑requisites:** Central manager appliance provisioned and reachable; network verified.  
- **Execution Steps:**  
  1. Open **Administration Console** on the central manager.  
  2. Go to **Setup > System Configuration > Set Unit Type**.  
  3. Select **Central Manager** for the central node and **Managed Unit** for each managed node.  
  4. Save and restart services.  
  5. Verify roles via **Monitor > System > Unit Status**.  
- **APIs/Tools:** None (GUI only)  

---

## Configure User Accounts (CLI)
*Add and configure user accounts from the command line.*  

- **Pre‑requisites:** Admin credentials; CLI access enabled.  
- **Execution Steps:**  
  1. SSH into the Guardium appliance as admin.  
  2. Run `show login` to list existing accounts.  
  3. Use `user create <username> password <password>` to add new accounts.  
  4. Set authentication methods with `authentication <scheme>` under the user context.  
  5. Validate with `show login`.  
- **APIs/Tools:** `user` GuardAPI commands  

---

## Apply Guardium Policies via REST
*Deploy policies through the REST API.*  

- **Pre‑requisites:** REST API user with `policy:modify` role; host and credentials.  
- **Execution Steps:**  
  1. Build JSON payload for the policy definition.  
  2. `PUT https://[Guardium hostname or IP address]:8443/restAPI/policy` with payload.  
  3. Verify HTTP 200 response and check policy status in the GUI.  
  4. Optionally apply changes with `policy:apply` GuardAPI.  
- **APIs/Tools:** `policy` REST endpoint  

---

## Enable Event Hub Monitoring (Azure)
*Forward data to an Azure Event Hub.*  

- **Pre‑requisites:** Cloud DB Service Account for Azure; event hub provisioned.  
- **Execution Steps:**  
  1. In Guardium, navigate to **Administration Console > Cloud Services > Azure Event Hub**.  
  2. Select the event hub and choose **Assign to Collector**.  
  3. Pick the target collector and confirm assignment.  
  4. Verify events in the **Monitor > Event Hub** dashboard.  
- **APIs/Tools:** None (GUI only)  

---

## Disable Auditing for a Single Database
*Turn off audit logging for a specific DB.*  

- **Pre‑requisites:** DB user with audit control privileges; DB identified.  
- **Execution Steps:**  
  1. Go to **Setup > Access Control > Audit Activities**.  
  2. Find the DB under **Monitored Databases**.  
  3. Choose **Disable Auditing** from the action menu.  
  4. Confirm and verify the audit status.  
  5. Test by running a query; ensure no new audit records appear.  
- **APIs/Tools:** `grdapi disable_audit` (or GUI)  

---

## Create User‑Defined Criteria
*Define custom criteria for policies.*  

- **Pre‑requisites:** Criteria Editor access with `policy:configure` role.  
- **Execution Steps:**  
  1. Open **Policy Builder > Criteria Editor**.  
  2. Click **New Criteria**, give it a clear name.  
  3. Define conditions using available operators and fields.  
  4. Save and assign the criteria to relevant policies.  
  5. Test via **Policy > Scan** on a sample set.  
- **APIs/Tools:** Criteria Editor GUI, `create_criteria` GuardAPI  

---

## Upgrade CyberArk SDK on Managed Unit
*Update the CyberArk SDK on managed units.*  

- **Pre‑requisites:** Latest CyberArk SDK package; central manager GUI access; managed unit credentials.  
- **Execution Steps:**  
  1. On the central manager, open **Administration Console > Patch Management**.  
  2. Upload the CyberArk SDK package.  
  3. Select the desired managed unit(s) for upgrade.  
  4. Execute distribution and monitor progress.  
  5. Verify installation by checking the SDK version on the managed unit.  
- **APIs/Tools:** Patch Management API (`patch_manager`), GUI only  

---

## Handle Missing Steps (Incomplete Documentation)
*Recover when a workflow step is missing.*  

- **Execution Steps:**  
  1. Locate the preceding or following section to infer the missing step.  
  2. Consult the Guardium knowledge base or open a support ticket if needed.  
  3. Document the complete workflow in a local wiki for future reference.  

---

## Navigate to User‑Defined Criteria
*Locate and edit criteria from the GUI.*  

- **Pre‑requisites:** Admin role; criteria already defined.  
- **Execution Steps:**  
  1. Log in to Guardium.  
  2. Go to **Policy Builder > Criteria Editor**.  
  3. Use the filter bar to search by criteria name, select the criterion, and examine/edit it.  
- **APIs/Tools:** Criteria Editor GUI  

---

## Use `delete_assessment_test` GuardAPI
*Remove a test from an assessment via command line.*  

- **Pre‑requisites:** Assessment description name; admin credentials.  
- **Execution Steps:** Open GuardAPI console or use an API client and run  
`delete_assessment_test --assessmentDescription "<description>" <test_name>`  
confirming success.

## Entities

### Configure Managed Units (Federated Architecture)
- **Execution Steps:** Set unit type to **Managed Unit**, provide central manager host/port/credentials, complete registration workflow, validate connectivity, configure data sources.
- **APIs/Tools:** `set_stap_manager`

## Workflows

### Schedule Recurring Jobs (REST API)
- **Execution Steps:** Prepare JSON payload with schedule parameters, POST to `https://[Guardium hostname or IP address]:8443/restAPI/schedule`, capture response ID, verify via `GET /schedule/{id}`, adjust settings via PUT, monitor via **Monitor > Scheduled Reports**.
- **APIs/Tools:** `schedule` REST endpoint

## Access Controls

### Identify Access to Sensitive Data by Unauthorized User
- **Execution Steps:** Create policy in **Threat Protection > Policies > Policy Builder**, add "Privileged User" is "No" and sensitive data tag condition, set action to "Audit" or "Block", activate policy.
- **APIs/Tools:** `create_policy`, `update_policy_condition`, `activate_policy`

## Threat Management

### Enabling and disabling threat detection analytics
- **Execution Steps:** Navigate to **System & Licensing > Analytics > Threat Detection**, enable or disable analytics, click **Save**.
- **APIs/Tools:** `enable_threat_detection`, `disable_threat_detection`

## Reporting

### Activity By Client IP
- **Execution Steps:** Navigate to **Reports > Activities > Client IP**, select reporting period, click **Run Report**, review SQL Verb, Object Name, and session counts organized by Client IP.
- **APIs/Tools:** `create_cip_report`, `view_report`

## Architecture

### Planning archiving, storage capacity, and scheduling
- **Execution Steps:** Assess current storage usage via **System & Licensing > Storage**, estimate future data growth, plan archive strategy via **System & Licensing > Archiving**, schedule data retention policies in **System & Licensing > System Management**.
- **APIs/Tools:** `enable_archiving`, `set_retention_policy`

## Reporting

### Custom reports for long term retention
- **Execution Steps:** Navigate to **Reports > Data Lake > Custom Reports**, click **New Report**, select template, modify query/layout/filters as needed, save custom report to Data Lake.
- **APIs/Tools:** `create_data_lake_report`

## Integration

### Enabling the External S-TAP provisioning UI
- **Execution Steps:** Navigate to **Administration Console > External S-TAP**, click **Enable Provisioning UI**, configure settings, click **Save**, activate.
- **APIs/Tools:** `enable_external_stap_ui`

## API

### REST API syntax
- **Keywords:** `softwareTap`, `update_user_db`

# Compressed Technical Documentation (Markdown)

## Workflows

- **Restart DB instance**
  - **Prerequisites:** DBA access, instance configured for restart
  - **Steps:** AWS Services > Databases → select instance → **Restart** → confirm
  - **Tools:** `rds:RebootDBInstance`

- **Import multiple databases**
  - **Prerequisites:** Spreadsheet with database details
  - **Steps:** Administration Console > Import/Export > Import Databases → upload spreadsheet → confirm import
  - **Tools:** `grdapi import_databases`

## Workflow Automation

### Manage Classification and Vulnerability Assessment
- **Prerequisites:** Vulnerability Assessment menu access
- **Steps:** Assessment > Vulnerability Assessment → select datasources → assign classification or vulnerability assessments → activate
- **Tools:** `grdapi assign_va_process_to_datasource`

## Security

### NetApp Data ONTAP Cluster-Mode Permissions
- **Prerequisites:** Guardium system setup for file system data collection
- **Steps:** Define credential with NetApp Cluster-Mode capabilities → associate with Guardium collector → configure data collection settings
- **Tools:** `grdapi set_netapp_credentials`

## Import/Export

### Import multiple databases (duplicate – see Workflows)

## Reporting

### Remote Data
- **Prerequisites:** Central Manager with managed units
- **Steps:** Reporting > Remote Data → select managed unit → execute report against remote DB
- **Tools:** `grdapi run_report_on_managed_unit`

## Vulnerability Assessment Scanner Deployment

### Deploy and configure the Guardium Vulnerability Assessment (VA) scanner on Kubernetes
- **Prerequisites:**
  - Access to K8s cluster with sufficient resources
  - Guardium central manager reachable from cluster
  - Helm package manager installed
- **Steps:**  
  1. Download Guardium VA scanner Helm chart from Guardium distribution site  
  2. Unpack and review `values.yaml`  
  3. Set `guardiumHost`, `guardiumPort`, `imageTag`, and resource limits in `values.yaml`  
  4. Add Guardium Helm repo: `helm repo add guardium https://guardium.example.com/helm`  
  5. Install scanner:  
     ```bash
     helm install my-vscanner guardium/guardium-va -f values.yaml
     ```  
  6. Verify pods: `kubectl get pods -n guardium-va`  
  7. Log into central manager, verify scanner status as *Connected*
- **Tools:** `helm`, `kubectl`
- **Customization:** Create Helm configuration templates for different versions or topologies; update with `helm upgrade --install`

## Manage AWS Data Streams

### Configure Azure Cloud Database Service Accounts and Event Hubs
- **Prerequisites:** Azure subscription, service accounts, event hub provisioned
- **Steps:** Cloud Services > Configure → select Azure → enter tenant ID, subscription ID, database service → authenticate with service account → configure event hub → save and start data capture
- **Tools:** `grdapi add_aws_datasource`, `grdapi configure_event_hub`
- **Customization:** Template for rapid re‑deployment of new services

## Risk Spotter

### Define and Enable Risk Monitoring Policies
- **Prerequisites:** Security analyst role, risk indicators
- **Steps:** Setup > Monitoring > Risk Spotter → create new policy → add risk indicator conditions → set thresholds and actions → activate and test
- **Tools:** `grdapi add_risk_indicator`, `grdapi enable_policy`
- **Customization:** Adjust thresholds for different activity levels

### Create Dynamic Auditing Policies from Threshold Alerts
- **Prerequisites:** Access to alerts, audit policy framework
- **Steps:** Audit > Policies > Dynamic Auditing → Create Policy from Alert → map alert fields to audit columns → finalize
- **Tools:** (Document does not specify tools)

## Creating Threat Categories from Alerts
- **Pre-requisites:** Existing threshold alerts; case management workspace enabled  
- **Steps:** Locate alert → Threat Management > Categories > New Category → name, description, link alert → assign owners/escalation → test with sample alert  
- **APIs:** `grdapi create_threat_category`, `grdapi associate_alert`  
- **Type:** Workflow  

## Designing Custom Audit Workflows
- **Pre-requisites:** Workflow design toolkit; stakeholder requirements gathered  
- **Steps:** Document process flow → Setup > Workflows > Create Custom → define nodes, transitions, actions (notifications, tickets, exports) → simulate and refine with feedback  
- **APIs:** `grdapi define_workflow_node`, `grdapi set_transition_condition`  
- **Customization:** Import/export templates for reuse across departments  
- **Type:** Workflow  

## Adjusting Trusted Session Logging with LOG_ACCESS_ONLY
- **Pre-requisites:** IGNORE_REQUEST flag enabled; trusted session profiles defined  
- **Steps:** Setup > Auditing > Trusted Sessions → edit profile → enable **LOG_ACCESS_ONLY** → save → restart session service if needed  
- **API:** `grdapi set_trusted_session_option`  
- **Type:** Configuration  

## Testing Query Rewrite Definitions
- **Pre-requisites:** Sample query set; rewrite rule definitions authored  
- **Steps:** Compile query set → Audit > Rules > Query Rewrites → Test Definitions → upload sample file → review match count, rewrite output, performance → refine and repeat  
- **APIs:** `grdapi test_query_rewrite`, `grdapi load_sample_queries`  
- **Type:** Workflow  

## Deploying Guardium Edge with Terraform
- **Pre-requisites:** Terraform installed; Azure subscription with permissions  
- **Steps:** Create `terraform.tfvars` (region, cluster name, node size) → `terraform init` → `terraform apply -auto-approve` → monitor Azure portal → validate connectivity → integrate with Central Manager  
- **APIs:** `grdapi add_edge_agent`, `grdapi configure_edge_cluster`  
- **Type:** Workflow  

## Enabling Utilization Data Collection
- **Pre-requisites:** Guardium appliances online; data warehouse schema provisioned  
- **Steps:** Setup > Data Processing > Unit Utilization → enable collection → set frequency → map fields to warehouse tables → define alert thresholds → test with simulated load → verify reports  
- **APIs:** `grdapi enable_utilization_collection`, `grdapi set_utilization_threshold`  
- **Type:** Configuration  

## Centralized Guardium Administration Setup
- **Pre-requisites:** Dedicated central manager host; shared secret generated  
- **Steps:** Install Guardium on central manager → Setup > Central Management > Initialize → enter secret → register additional units via Register Unit wizard → group units (e.g., geography) → verify sync/role propagation  
- **APIs:** `grdapi init_central_manager`, `grdapi register_unit`  
- **Type:** Workflow  

## Granting Local Authentication for Any AccessMgr User
- **Pre-requisites:** Admin UI access  
- **Steps:** UI login → Setup > System > Authentication → set **Authentication Method** to **Local** → Save → Restart Guardium service  
- **API:** `grdapi set_authentication_method`  
- **Type:** Action  

## Managing Deployed Assets in the UI
- **Pre-requisites:** Asset already added to Guardium  
- **Steps:** Explore > Assets → select asset → view details → if configuration changed, click **Rescan** to refresh data  
- **API:** `grdapi refre` *(truncated; assumes continuation for refresh)*  
- **Type:** Action

```markdown
## Integrate CyberArk Vault with Guardium
Enter CyberArk URL, connection credentials, and vault name in **Setup > Vaults > New Vault** and test connectivity before activation.

## Add Databases to Guardium Inventory
Navigate to **Databases > Add New Database**, enter hostname, port, credentials, save, and verify appearance in the list.

## Exclude Specific Table Columns
Create an **Exclude table column(s)** function in **Data Protection > Functions > Create Function** and apply to relevant policies.

## Route Cases to Recipients
Assign cases in **Access Management > Cases > Assign Case** to roles, email, user groups, or individual users.

## Suppress SQL Command Logging
Create an **Ignore - SQL commands** rule in **Auditing > Rules > Create Rule** to suppress logging while maintaining other records.

## Apply Tags to Rule Definitions
Click the **Add Tag** icon when creating a rule to define criteria and actions, then save.

## Customize Column Display in Reports
Edit a report, select desired entity attributes for columns, define sort order, and save.

## Install and Configure Containerized VA Scanners
Install the VA scanner container, configure settings, connect to data sources, run, and schedule assessments.

## Restore Archival Data
Move archive files to the target server, import catalog entries via **Import catalog entries**, and verify in **Data Catalog**.

## Restore Non‑Centrally Managed Aggregator
Boot with the ISO, apply the license manually, and verify aggregator operation.

## View Group Membership and Usage
Check **Groups > View Group Details** to see policies, reports, and queries using the selected group.
```

## Configuration Follow‑Up
**Run post‑deployment tasks after installing External S‑TAP.**

---

## Monitoring Agent Deployment
**Automate Guardium GIM client activation and installation.**

---

## Where to search
**Perform discovery, reporting, false‑positive removal, runtime sensitive‑object detection, and audit scheduling.**

---

## Configure and enable Risk Spotter
**Activate required Guardium modules and turn on Risk Spotter.**

---

## Defining a CAS‑based test
**Create a CAS template, define OS‑level checks, run against the DB server, and review results.**

---

## Upgrading Edge Gateway
**Upgrade Edge Gateway from v2.0 to v2.1 using the latest patch and upgrade script.**

---

## Downloading Edge Images
**Download a tar archive of Edge images for private‑registry preparation or Terraform deployment.**

---

## For standard deployment, see *Setting up an Edge Gateway*
**For Terraform deployments, configure the external registry in `terraform.tfvars`.**

---

## Enabling universal connector on collectors
**Enable Universal Connector via the UI or the `grdapi enable_uc` command.**

---

## Creating catalog sources
**Create a catalog source for each service hosted in a private container registry.**

---

## What to do next
**Provision External S‑TAP after creating the custom resource.**

---

## Using Guardium REST APIs
**Call Guardium APIs via RESTful requests from applications.**

---

## Inspection engine configuration
**Configure inspection engines for Linux‑UNIX and Windows environments through the Guardium UI.**

---

## Guardium Data Protection trial for Db2
**Deploy the Guardium trial to connect with a Db2 environment.**

## 1432. Configuring Db2 Exit

Enable Db2 Exit module for S‑TAP to monitor all Db2 database activity. Requires the Db2 Exit module to be available. Use the built‑in GUI to enable the module.

## 1433. Modifying the report display

Switch between chart and tabular views, rename columns, and define conditional coloring. Access the report view and adjust the display settings as needed.

## 1434. Modifying the database version and patch level

Override vulnerability‑assessment failures by adding the correct database version and patch level in **Group Builder**. Navigate to Group Builder, locate the target group, and update the version and patch fields.

## Access Control

Configure Fine‑Grained Access Control (FGAC). Prerequisites: administrator role and a security policy. Steps: go to **Setup > Access Control > FGAC**, define roles and object‑level permissions, assign roles to users, and test with a restricted account. Use `grdapi set_access_rule`.

## Auditing

Create a Dynamic Auditing policy. Prerequisites: administrator access and Risk Spotter configured. Steps: open **Policy Builder > Dynamic Auditing**, select data sources and audit criteria, save and install, then verify status under **Policy Builder**. Use `grdapi create_dynamic_auditing_policy`.

## Data Discovery

Discover and configure AWS data streams. Prerequisites: AWS account credentials and Guardium collector access. Steps: go to **Setup > Data Streams > Discover**, enter AWS credentials and scope, run discovery, select streams, click **Configure**, assign to the collector, and save. Use `grdapi discover_aws_data_streams` and `grdapi configure_aws_stream`.

## Datasource Configuration

Configure an MS SQL Server datasource. Prerequisites: SQL Server running and network connectivity verified. Steps: collect hostname, port, and authentication method, navigate to **Datasources > Add Datasource**, select the connection type, enter details, test, and save. Use `grdapi add_datasource`.

## External S‑TAP

Edit the External S‑TAP group tab. Prerequisites: External S‑TAP installed and admin privileges. Steps: go to **Data Sources > External S‑TAP > Group Tab**, locate the entry, modify hostname, port, credentials, save, and restart the service if prompted. Use `grdapi edit_external_stap_group`.

## Investigations

Investigation Dashboards. Prerequisites: File Activity Monitoring enabled and dashboard access. Steps: open **Investigation > Dashboards**, enable relevant modules, view real‑time alerts, and use the Sankey chart to trace file‑access patterns. Use `grdapi enable_file_activity_monitoring` and `grdapi open_investigation_dashboard`.

## Installation

Physical Appliance installation. Prerequisites: rack space, power supply, and network cables. Steps: rack the appliance, connect power cords, optionally add a secondary network cable, power on, and follow the initial setup wizard.

## Managed Units

Create managed unit groups. Prerequisites: admin access and existing managed units. Steps: go to **Managed Units > Add Group**, enter name/description, select units, save, and verify membership. Perform group actions (updates, backups) via the UI or `grdapi create_managed_unit_group` and `grdapi apply_group_action`.

## Patching

Patch Installation. Prerequisites: backup of current Guardium configuration and a tested patch package. Steps: upload patch via **Administration > Patches**, review compatibility, schedule during low usage, confirm success in **Patches > Installed Patches**, and reboot if required. Use `grdapi install_patch` and `grdapi view_installed_patches`.

## Reporting

Create reports for z/OS. Prerequisites: z/OS data source configured and report template access. Steps: navigate to **Reports > Create New Report**, select *z/OS*, customize queries, define parameters and schedule, then save the report.

## Risk Management

### Using VA with Cloudera
- **Components:** Cloudera environment, VA license
- **Execution Steps:** Open Risk Management > Vulnerability Assessment, select Cloudera, choose components, configure parameters, start scan, review and remediate results.
- **Tools:** `grdapi run_va_scan`, `grdapi cloudera_va_results`

## Session Monitoring

### 1435. Session Inference
- **Feature:** Detects session anomalies automatically
- **Prerequisites:** Guardium collector running, session activity observed
- **Tools:** None
- **Customization:** None

## Tools

### 1437. S-TAP and GIM dashboard
- **Type:** Monitoring dashboard
- **Prerequisites:** S-TAP and GIM agents deployed
- **Customization:** None

## Workflows

### 1436. Configuring an NFS backup
- **Type:** Workflow
- **Prerequisites:** Guardium appliance, accessible NFS server
- **Customization:** None

## File Activity Monitoring

### Configure File Activity Monitoring
- **Steps:** Navigate to Define > File Activity, select Configure File Monitoring, specify source servers, define paths/exclusions/filters, enable monitoring and alerts, save and activate policy.
- **Tools:** `GRA API file_monitor`

## Authentication and Authorization

### Set Up SSO for Guardium
- **Steps:** Go to Setup > Security Settings > SSO, choose LDAP provider, enter host/port/auth details, map LDAP groups to Guardium roles, test login, enable SSO for web/API.
- **Tools:** `grdapi sso_config`

## Customization

### Create Custom Dashboards
- **Steps:** Open Knowledge Portal > Dashboards, click Add Dashboard, provide name/description, drag reports to canvas, configure widget properties, save dashboard, configure access controls.
- **Type:** User workflow

## Compliance Monitoring

### Configure Fine-Grained Access Control (FGAC) in Guardium
- **Steps:** Navigate to Setup > Access Control > FGAC, define roles/object-level permissions, assign roles to users, test access with restricted account.
- **Tools:** `grdapi set_access_rule`

## Discovery and Classification

### Add to Exclusion List (Active Threat Analytics)
- **Steps:** Identify items to exclude, navigate to Tools > Active Threat Analytics > Exclusion List, click Add, enter item details, save list.
- **Tools:** None

## Sample Data Setup

### Configure Access to Db2 Sample Data
- **Steps:** Review guide for network settings, add data source pointing to Db2 sample, validate connectivity, import sample data, set up monitoring policies.
- **Tools:** None

## Workflows

### End a Quarantine with GuardAPI
- **Steps:** Determine quarantine ID, log into Guardium CLI, run `store quarantine end <quarantine_id> <relative_time>`.
- **Tools:** `store quarantine end`

## Installation

### Install Secondary Unified Discovery and Classification Analyzer
- **Steps:** Obtain installation package, execute installation scripts on secondary server, follow on-screen prompts.
- **Tools:** None

## Datasources

- **Clone a Datasource**
  - Select the datasource, click **Clone**, modify parameters, and save.
  - API: `grdapi clone_datasource`

---

## Mapping an External Feed

- **Pre-requisites:** External database accessible, Guardium CLI access.
- **Steps:** Go to **Manage > External Feeds**, select **Add Feed**, choose **External Database**, enter connection details, test and save.
- API: `grdapi map_external_feed`

---

## Knowledge

### Understanding GuardAPI Examples

- No prerequisites, execution steps, or tools required.

---

## Protect Cloud Database Service

### Configuring Native Audit and Guardium Collection

- **Pre-requisites:** Cloud account with native audit enabled, reachable Guardium collector.
- **Steps:** Enable native audit in the cloud console, in Guardium go to **Monitor > Audit Data Sources**, enter audit endpoint URL and credentials, save, and start collector.
- APIs/Tools: `grabapi audit start`, GUI > Monitor > Audit Data Sources

---

## Detect Anomalous Queries

### Setting Up Alerts for Specific SQL Keywords

- **Pre-requisites:** Outlier Detection enabled, keywords to monitor.
- **Steps:** In **Configure > Anomaly Detection > Outlier Detection**, create a keyword group, build a policy rule to generate an alert, save and activate, then test with a query containing a keyword.
- APIs/Tools: `grabapi keyword_alert`, `grdapi outlier_policy`

---

## Install Guardium License

### Activating a New License Key

- **Pre-requisites:** License file, UI access.
- **Steps:** Log in as administrator, navigate to **Administration > License Management > Install License**, upload the .lic file, accept the agreement, confirm installation, and verify status under **Monitor > License Usage**.
- APIs/Tools: `grabapi license install`, `grabapi license status`

---

## Establish Data Retention

### Archiving Guardium Audit Data to External Destination

- **Pre-requisites:** External storage accessible, credentials set.
- **Steps:** Go to **Reports > Long‑Term Retention > Configure Retention**, define a new data stream, select external target and connection details, set retention period and schedule, start initial push, review archival history.
- APIs/Tools: `grabapi retention create`, `grabapi retention status`

---

## Audit Process To‑Do List

### Configure Audit Process To‑Do List

- **Pre-requisites:** UI access, appropriate permissions.
- **Steps:** Open **Audit Process To‑Do List**, review assigned tasks, filter by status/due date/assignee, update status, notes, or reassign, and notify stakeholders.
- APIs/Tools: GuardAPI `audit_process` API, Guardium UI

**Customization:** Create custom filters for recurring audit tasks.

## Configuration
- **User workflows:** Script pre-deployment checks using provided templates
- **Distributed Reporting Prerequisites:**
  - Verify all intended managed units are listed in appropriate group
  - Ensure network connectivity between central manager and each unit
  - Confirm data collection agents are active on all managed units
  - Define required data groups and permission levels

## Catalog and Manage Databases
- **Execution Steps:**
  1. Navigate to **Catalog and Manage Databases**
  2. Select a discovered database instance
  3. Apply or modify classification policies
  4. Configure audit settings and add relevant reports/alerts
- **APIs/Tools:** `grdapi add_database`, `grdapi create_policy`

## Filtering an Individual Chart
- **Execution Steps:**
  1. Select a chart within the dashboard
  2. Apply filters using the filtering pane
  3. Save the filtered view as a new dashboard
  4. Export the filtered chart as needed
- **Customization:** Create custom chart templates with predefined filters

## Remove CyberArk Integration
- **Execution Steps:**
  1. Navigate to **Application Passwords > CyberArk**
  2. Delete the specific CyberArk entry
  3. Validate removal via CLI: `grdapi remove_cyberark`
  4. Ensure no remaining references in policies or reports
- **APIs/Tools:** `grdapi remove_cyberark`

## Cloud Database Discovery Process
- **Execution Steps:**
  1. Open the **Cloud Discovery Wizard**
  2. Select cloud service provider and regions
  3. Authenticate with cloud account credentials
  4. Initiate scan and review discovered instances
  5. Create Guardium datasources for relevant databases
- **Customization:** Automate repetitive discovery tasks using scheduled jobs

## Bulk Reopen Threat Analytics Cases
- **Execution Steps:**
  1. Navigate to **Active Threat Analytics > Cases**
  2. Select multiple cases to reopen
  3. Choose **Reopen Selected Cases** from the action menu
  4. Confirm action and verify status updates
- **Customization:** Implement scripts for regular status reviews

## Session-Level Policy Creation
- **Execution Steps:**
  1. Open **Policy Builder for Data**
  2. Select **Create New Policy** and choose **Session-Level**
  3. Define traffic criteria using session attributes
  4. Add rule actions and exceptions as required
  5. Install policy to relevant collectors
  6. Monitor policy effectiveness
- **APIs/Tools:** `grdapi create_policy`, `grdapi install_policy`
- **Customization:** Develop reusable session filtering templates

## Example Session Ignoring Policy
- **Execution Steps:**
  1. Create two rules: one to ignore trusted IPs, another for all other sessions
  2. Order rules so inclusion follows exclusion
  3. Test on non-production collector
  4. Verify ignored sessions no longer appear in reports
- **APIs/Tools:** `grdapi create_policy`

## Create Distributed Report
- **Execution Steps:**
  1. Define group of managed units for data collection
  2. Open **Distributed Reports** and select **Create New Report**
  3. Choose data type and aggregation parameters
  4. Schedule report execution and distribution
  5. Review aggregated results and export as needed
- **APIs/Tools:** `grdapi create_report`

## Consolidated Guardium Configuration and Administration Guide

### Disabling Universal Connector
- **Prerequisites:** Administrative access to Guardium system
- **Steps:**
  1. Navigate to Universal Connector configuration
  2. Select Disable from the action menu
  3. Confirm deactivation on applicable collectors
  4. Validate connectors show as inactive in UI
  5. Document disabling date and reason
- **Tools:** `grdapi disable_uc`
- **Customization:** Implement UC activation schedules

### Windows S-TAP Client Setup via GIM
- **Prerequisites:** Guardium Installation Manager accessible; client system identified
- **Steps:**
  1. Open Guardium Installation Manager on central manager
  2. Select Client Setup and choose Windows S-TAP agent
  3. Specify target client system details
  4. Configure connection parameters in `update_stap_config`
  5. Initiate installation and monitor progress
  6. Verify S-TAP status on client system
- **Tools:** GUI-based installation, `grdapi update_stap_config`
- **Customization:** Create automated installation scripts for batch deployments

### Creating and Managing Investigation Dashboards
- **Prerequisites:** Access to Investigation Dashboard module; required data sources
- **Steps:**
  1. Open Investigation Dashboard from main GUI menu
  2. Select New Dashboard and provide a meaningful name
  3. Add required reports using the Add Report dialog
  4. Apply filters for specific entities or time ranges
  5. Organize layout using available widgets and save configuration
  6. Share dashboard with relevant stakeholders through permissions
- **Tools:** None specific required
- **Customization:** Develop standardized dashboard templates

### Managing Scan Permissions
- **Prerequisites:** Audit policy permissions; access to Scan Permissions UI
- **Steps:**
  1. Navigate to Scan Permissions configuration section
  2. Review existing permission assignments
  3. Modify group assignments based on current access needs
  4. Add new data sources to relevant permission groups
  5. Test permissions by performing sample scans
  6. Document any changes and notify affected teams
- **Tools:** `grdapi manage_scan_permissions`
- **Customization:** Establish regular permission review schedules

### File Discovery, Entitlement and Classification Scan Permissions
- **Prerequisites:** None specified
- **Steps:**
  1. Define Scan Permissions for FDEC on NAS and SharePoint servers
  2. Configure access rights according to organizational policies
- **Tools:** None
- **Types:** Configuration

### Exception Management Workflow
- **Prerequisites:** None specified
- **Steps:**
  1. Enable the Ignoring exceptions policy
  2. Specify exceptions to be ignored in session policies
- **Tools:** None
- **Types:** Configuration

### LDAP Data Enrichment Workflow
- **Prerequisites:** None specified
- **Steps:**
  1. Select a custom table for LDAP import
  2. Import existing table definition
- **Tools:** None
- **Types:** Workflow

### Distributing Custom Tables
- **Prerequisites:** Central guard manager configured
- **Steps:**
  1. Define custom tables centrally
  2. Distribute custom tables and data to managed units
- **Tools:** None
- **Types:** Workflow

### Scheduled Job Exceptions Alert
- **Prerequisites:** Scheduled jobs configured
- **Steps:**
  1. Set up alerts for every 10 minutes on scheduled job exceptions
  2. Include assessment jobs in the alert criteria
- **Tools:** None
- **Types:** Feature

### Profile Synchronization Workflow
- **Prerequisites:** Guardium UC profiles configured
- **Steps:**
  1. Detect changes in storage credentials
  2. Reinstall profiles referencing updated credentials
- **Tools:** None
- **Types:** Workflow

### Deploy External S-TAP with Helm
- **Prerequisites:** Kubernetes and Helm installed
- **Steps:**
  1. Use Helm charts to deploy External S-TAP
  2. Manage deployment within Kubernetes environment
- **Tools:** Helm
- **Types:** Workflow

### Delete Audit Process Result
- **Prerequisites:** GuardAPI access
- **Steps:**
  1. Execute `delete_audit_process_result` command
  2. Specify execution date range and audit process name
- **Tools:** GuardAPI
- **Types:** Action

### Configuring Text Datasources
- **Prerequisites:** None specified
- **Steps:**
  1. Configure custom properties for datasources
  2. Work with existing datasources
- **Tools:** None
- **Types:** Workflow

### Investigation Dashboard for Files
- **Prerequisites:** File activity data available

## S-TAP Management Workflow

### Configure S-TAP Management Requirements
- **Pre-requisites:** Administrator credentials; active Guardium host
- **Steps:**
  1. Log in to Guardium with admin rights
  2. Navigate to **Configuration > S-TAP**
  3. Select **Management Settings**
  4. Define required parameters and save changes
- **Types:** Workflow

## Guardium Administration Guide

### Access GuardAPI for Task Automation
- Use **Policy Builder** to run GuardAPI commands for automating tasks and searching.

### Restore Guardium Insights Certificate
- Under **Notifications → Certificate Management**, restore alerts via the wizard.

### View FDEC Scan Results
- In **Discovery and Classification**, select **View Scan Results** for detailed FDEC scan outcomes.

### Close Multiple Cases Bulk
- In **Active Threat Analytics**, select and bulk close cases, confirming status updates.

### Bulk Reopen Closed Cases
- From **Active Threat Analytics**, select closed cases, reopen them, and validate status changes.

## Guardium Administration

## Venafi Integration
**Create a Venafi Instance**
- Requirements: Venafi portal access, Guardium admin rights
- Steps:
  1. Go to **System > Venafi > Instances**
  2. Click **Add Instance**, choose **Venafi**
  3. Enter portal URL, authentication details, and certificate settings
  4. Save the configuration

## Policy Change Monitoring
**Policy Changes Alert**
- Requirements: Enabled policy, monitoring feature active
- Steps:
  1. Navigate to **Reports > Policy Changes**
  2. Click **Schedule**, set frequency to **Daily**
  3. Configure email or other notification recipients
  4. Save to enable alerts

## Distributed Group Management
**Groups with Grouped Installation Manager (GIM)**
- Requirements: GIM client installed, administrator rights
- Steps:
  1. Create/edit a **GIM group** under **System > Groups**
  2. Add managed units to the group for batch processing
  3. Use the group for updates via **System > GIM > Update**
  4. Verify installation status across the group
- CLI: `grdapi gim_create_group`

## S-TAP Certificate Management
**S-TAP Connection Approval**
- Requirements: Registered S-TAP instance, certificates prepared
- Steps:
  1. Access **S-TAP > Manage > Certification**
  2. Find the pending certificate, review details
  3. Click **Approve** to authorize the connection
  4. Verify successful connection status

## Guardium Operations

### Manage AWS Data Streams
- **Steps:**
  1. Log into Guardium and go to **Data Sources > Manage AWS Streams**.
  2. Enter AWS Access Key, Secret Key, and Region.
  3. Validate credentials and configure stream parameters (batch size, polling interval).
  4. Save the configuration.
- **API:** `grdapi manage_aws_data_streams`

### Create a Role
- **Steps:**
  1. Open command-line and run `grdapi create_role <role_name>`.
  2. Verify with `grdapi list_roles`.
- **API:** `grdapi create_role`

### Export Audit Results
- **Steps:**
  1. Navigate to **Audit > Manage > Export**.
  2. Select report, choose CSV or JSON format, specify destination path, click **Export**.
- **API:** `grdapi export_audit_results`

### Manage Central Patch Distribution
- **Steps:**
  1. Go to **Setup > Central Patch Management**.
  2. Upload patches via UI or CLI: `grdapi import_patch <file_path>`.
  3. Assign patches to systems and initiate distribution: `grdapi distribute_patches`.
- **APIs:** `grdapi import_patch`, `grdapi distribute_patches`

### Manage Proxy API Settings
- **Steps:**
  1. Access Guardium CLI and run `grdapi proxy list`.
  2. Add or modify proxies: `grdapi proxy add name=<proxy_name> host=<host> port=<port>`.
  3. Validate with `grdapi proxy list`.
- **API:** `grdapi proxy`

### Manage Session-Level Policies
- **Steps:**
  1. Go to **Setup > Access Control > Session Policies**.
  2. Click **New Policy**, define session conditions (user, time, database).
  3. Set actions (allow, deny, monitor) and save/activate the policy.
- **API:** `grdapi create_session_policy`

### Perform Sensitive Data Discovery
- **Steps:**
  1. Navigate to **Key Management > Sensitive Data Discovery**.
  2. Select datasource, define discovery rules (patterns, PII types).
  3. Start the discovery process and monitor results.
- **API:** `grdapi start_discovery`

### Query Enterprise Search
- **Steps:**
  1. Open **Enterprise Search** from dashboard.
  2. Select domain, specify search criteria (entities, attributes), and execute query.
  3. Review results and refine using filters or advanced options.
- **API:** `grdapi run_enterprise_search`

### Troubleshoot AWS Data Streams
- **Steps:**
  1. In **Data Sources > Manage AWS Streams**, select problematic stream.
  2. View status and logs for errors, reconfigure parameters if needed, and restart stream.
- **API:** `grdapi troubleshoot_aws_stream`

## Manage GIM Bundles

### Distribute GIM Bundles
- **Steps:**
  1. Log into GIM UI as admin.
  2. Go to **Bundles > Distribute Bundles**.
  3. Choose target managed units and bundle version, click **Distribute**.
- **API:** GUI only, no GuardAPI equivalent

## Policies Schedules

### Define Policies Schedules
- **Steps:**
  1. Ensure Policy Manager role and schema access.
  2. (Steps incomplete in source excerpt; cannot complete this block)

## Guardium Management Overview

### Configure Central Manager for Deployment Health
- **Set up central manager for deployment health views:**  
  1. **Pre-requisites:** Central Manager installed and deployment health enabled.  
  2. **Execution:** Go to **Setup > Deployment Health**, configure aggregation and data sources, then verify UI rendering.  
  3. **Tool:** `grdapi set_deployment_health_config`

### Define Use Case Scenarios
- **Create a new scenario in Guardium:**  
  1. **Pre-requisites:** Scenario builder license and edit permissions.  
  2. **Execution:** Click **Plus** on Scenario homepage, define parameters, then save.  
  3. **Tool:** Guardium UI

### Manage Authentication Credentials
- **Create and manage authentication credentials for data sources:**  
  1. **Pre-requisites:** Data source profiles configured and admin rights.  
  2. **Execution:** Navigate to **Credentials > New**, enter user credentials, assign to profiles, test, and save.  
  3. **Tool:** Guardium UI

### Fine-Tune Policy Schedules
- **Fine-tune policy schedule configurations:**  
  1. **Pre-requisites:** Policy Manager role and existing schedules.  
  2. **Execution:** Select **Policies > Schedules Advanced**, adjust timing, recurrence, and target settings, then save.  
  3. **Tool:** Guardium UI

### Audit and Ignore Session Transformation Rules
- **Audit and ignore session transformation rules:**  
  1. **Pre-requisites:** Policy Manager role and audit policy defined.  
  2. **Execution:** Go to **Policies > Session Actions**, add rules based on conditions, activate the policy.  
  3. **Tool:** `grdapi add_session_action`

### Aggregate Data and Restart S-TAP
- **Run GuardAPI aggregation and restart S-TAP commands:**  
  1. **Pre-requisites:** GuardAPI credentials and reachable Guardium system.  
  2. **Execution:** Execute `aggregation` with `target=guardium` and `execution=run`; run `restart_stap` specifying the S-TAP host.  
  3. **Tool:** GuardAPI commands

### Upload GIM Modules
- **Upload and import GIM modules:**  
  1. **Pre-requisites:** GIM server accessible and admin credentials.  
  2. **Execution:** In GIM UI, select **Modules > Upload**, choose the module file, and click **Import**.  
  3. **Tool:** GIM GUI (no GuardAPI equivalent)

### Scan and Refine Results
- **View and refine scan results:**  
  1. **Pre-requisites:** Scanner tool configured and data source profiles defined.  
  2. **Execution:** Run a scan via **Scan > Results**, apply user-defined filters, analyze findings, and remediate.  
  3. **Tool:** Guardium UI

### Build Custom Dashboards
- **Build custom dashboards and add reports:**  
  1. **Pre-requisites:** Dashboard designer role and data sources available.  
  2. **Execution:** Select **Dashboards > Create**, add reports via drag-and-drop, configure widgets, save, and share.  
  3. **Tool:** Guardium UI

### Deploy Edge Images
- **Push Edge images to private registry:**  
  1. **Pre-requisites:** Docker installed and Edge tar archive downloaded.  
  2. **Execution:** Load image with `docker load -i <archive_file>`, tag and push to registry using `docker push <registry>/<image>:<tag>`.  
  3. **Tool:** Docker CLI

### Fine-Tune External S-TAP
- **Configure group settings for External S-TAP:**  
  1. **Pre-requisites:** External S-TAP deployed and network connectivity.  
  2. **Execution:** Open **Advanced Tab** in S-TAP settings, define group criteria, load balancing, and preferences, then save.  
  3. **Tool:** Guardium UI

### Identify Missing Archive/Export Days
- **Identify days lacking archived or exported data:**  
  1. **Pre-requisites:** Data archiving and export jobs configured.  
  2. **Execution:** Query **Archive/Export Logs** for missing date entries, use **View > Days** to see gaps.  
  3. **Tool:** Guardium UI

## Empty Data Days Identification
Detect and react to days with no archived/exported data.  
- **Pre-requisites:** Archive and export jobs configured and scheduled  
- **Steps:** Open query builder against `ArchiveReport` and `ExportLog` tables, filter for NULL dates, generate report, trigger alerts for missing data days.  
**Type:** Workflow

## SQL Audit Queries
Extract executed queries (RecordType = 1) for audit or performance analysis.  
- **Pre-requisites:** Guardium configured for audit logging; permissions to query `events` table  
- **Steps:** Log in with an account that can access `events`, run `SELECT * FROM events WHERE RecordType = 1;`, optionally add filters for time range, hostname, etc.  
- **Action:** Run via SQL client, no extra tools required.  
- **Customization:** Save as recurring audit report; schedule with task plan.  
**Type:** Action

## Policy Evaluation Insights
Get policy evaluation events (RecordType = 3).  
- **Pre-requisites:** Guardium functional; permissions to access `events` table  
- **Steps:** Open SQL client, run `SELECT * FROM events WHERE RecordType = 3;`, filter by `PolicyName`, `EvalResult`, etc.  
- **Action:** SQL-only query, no APIs required.  
- **Customization:** Create report template for compliance audits.  
**Type:** Knowledge

## Session Insight
Get session termination events (RecordType = 5).  
- **Pre-requisites:** Access to Guardium events data with privileges  
- **Steps:** Connect to Guardium database, run `SELECT * FROM events WHERE RecordType = 5;`, refine by time, user, host as needed.  
- **Action:** SQL interface only.  
- **Customization:** Build logout audit report using this filter.  
**Type:** Knowledge

## Datamart Ingestion
Insert a query into a datamart.  
- **Pre-requisites:** Predefined datamart; query ready in SQL/CSV format  
- **Steps:** In Guardium UI, go to **Datamarts**, select target, click **Add Query**, paste/upload definition, confirm, allow system to process schema adjustments.  
- **Action:** Performed via Guardium UI, no CLI needed.  
- **Customization:** Automate batch loading via scheduled tasks or external scripts.  
**Type:** Configuration

## Knowledge Retrieval
Locate group usage across Guardium artifacts.  
- **Pre-requisites:** Permissions to view policies, reports, queries  
- **Steps:** In UI, go to **Search → Advanced Search**, select **Group**, enter name, choose entities (policies, reports, queries), execute search, review results.  
- **Action:** UI search functionality, no APIs.  
- **Customization:** Save search for periodic reviews.  
**Type:** Knowledge

## Cycle Management
Restart Guardium Managed Units.  
- **Pre-requisites:** Administrative privileges on Central Manager  
- **Steps:** Open Central Manager dashboard, navigate to **Managed Units → Actions → Restart**, select units, confirm.  
- **Action:** Performed via Central Manager UI.  
**Type:** Action

## License Maintenance
Install Guardium license keys.  
- **Pre-requisites:** Valid `.lic` files; Central Manager access  
- **Steps:** From Central Manager UI, select **License**, click **Install License Keys**, upload files, confirm installation, verify status.  
- **Action:** Performed via Central Manager UI.  
- **Customization:** Document steps for new deployments.  
**Type:** Action

## Monitoring Policy
Configure policy actions.  
- **Pre-requisites:** Policy defined; permissions to manage policies  
- **Steps:** Go to **Policy → Actions**, select action (email alert, system command), set parameters, save.  
- **Action:** Can be done via UI or `grdapi set_action`.  
- **Customization:** Tailor actions per policy type (high‑risk vs. informational).  
**Type:** Configuration

## Instance Management
Delete a CAS instance.  
- **Pre-requisites:** Access to CAS Configuration Navigator; appropriate permissions  
- **Steps:** Open **CAS Configuration → Navigator**, locate instance, click **Delete Instance**, confirm removal.  
- **Action:** Performed via CAS Configuration UI.  
- **Customization:** Establish process for archiving data before deletion.  
**Type:** Action