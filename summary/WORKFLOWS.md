# Permissionstodynamicrolesandcredsfordifferentpaths — WORKFLOWS

**Category:** workflows  |  **Generated:** 2026-07-09  |  **Source:** gdp-12.x-documentation.pdf

---

## Permission Management

### Assign and Manage Permissions to Dynamic Roles
- Define dynamic roles based on user attributes or session properties
- Assign permissions to dynamic roles through Setup > Users and Roles > Roles
- Use GuardAPI commands for role creation and permission assignment
- Validate with a test user account

## IAM and EC2

### Create an IAM Role for EC2
- Open AWS IAM console and select **Roles**, then **Create role**
- Choose **EC2** as the common use case
- Attach necessary policies or create a custom policy
- Enter a role name and create the role
- Reuse the role for multiple EC2 instances

## Data Monitoring and Policy Enforcement

### Monitor Database Activities with Security Policy Rules
- Create security policy rules to match activities of interest
- Route matching activities to the Guardium collector
- Verify activities are stored in the system repository
- Monitor reports for policy violations

## Cassandra Data Source Configuration

### Configure DSE Cassandra Data Source for CAS Scripts/Templates
- Identify the 'Directory' name of the Cassandra installation
- Define datasources using pipe-separated variables
- Integrate with Guardium for activity monitoring

## Architecture for Network Resilience

### Maintain Datasource Connectivity During Network Outages
- Configure datasources to survive network disruptions
- Test connectivity during simulated outages
- Implement measures to ensure service continuity

## High Availability with Standby Vault Servers

### Configure Redundancy for CyberArk Vault Servers
- Set up standby vault servers for high availability
- Manage vault server IP addresses effectively
- Test failover capabilities during planned maintenance

## External Storage Solutions Configuration

### Set Up Archival and Backup for Guardium
- Define storage targets in Guardium configuration
- Configure SSH key authentication for secure access
- Establish data storage schedules for audit and compliance

## Troubleshooting and Management

### Execute Diagnostic and Management Workflows
- Run "MustGather" diagnostics for troubleshooting
- Configure "slon looper utility" for persistent logging
- Manage S-TAP and Windows agents through the user interface

## Enterprise Patch and Configuration Management

### Centralize Patch and Configuration Management
- Build an enterprise hub for centralized management
- Aggregate patches, certificates, and profiles across systems
- Distribute and enforce configurations uniformly

## Session-Level Policy Configuration

### Define and Apply Session-Level Policies
- Create session-level policies with specific criteria
- Use GuardAPI for policy creation and application

## Value Changes Auditing for Data Tracking

### Audit Data Value Changes in Guardium
- **Components:**
  - **Pre-requisites:** Auditor role assigned; policies for change monitoring defined
  - **Execution Steps:**
    1. Navigate to **Configure > Auditing > Value Changes**
    2. Select tables and operations (e.g., INSERT, UPDATE, DELETE) to audit
    3. Configure audit details and save the policy
- **Types:** Compliance
- **Customization:**
  - **User workflows:** Regularly review audit reports for unexpected or unauthorized changes

## Auditing

- **Components:** Value change audit
- **Prerequisites:** Audit policy defined
- **Steps:**
  1. Define alert thresholds for high-risk tables
  2. Specify email recipients for notifications
  3. Activate the audit policy
- **Tools:** `grdapi add_value_change_audit`
- **Type:** Security

## System Help

- **Components:** Guardium UI help
- **Prerequisites:** Web browser access
- **Steps:**
  1. Click **Help** in the upper right corner
  2. Select **Guardium System Help**
  3. Use search for specific topics
- **Tools:** GUI
- **Type:** Navigation

## Feature Activation

- **Components:** License management
- **Prerequisites:** Administrative access, valid license
- **Steps:**
  1. Log in with admin credentials
  2. Go to **Configure > System Configuration > License Management**
  3. Enter unlock keys or upload license files
  4. Confirm activation status
- **Tools:** GUI
- **Type:** Configuration

## Cloud Protection

- **Components:** Cloud database monitoring
- **Prerequisites:** Cloud account, Guardium Cloud Database Agent
- **Steps:**
  1. Navigate to **Configure > Data Sources > Cloud**
  2. Select cloud service (e.g., AWS RDS, Azure SQL)
  3. Enter connection details and configure monitoring
  4. Save configuration and schedule discovery
- **Tools:** `grdapi add_cloud_datasource`
- **Type:** Configuration

## Agent Updates

- **Components:** Agent release notes
- **Prerequisites:** Internet access, admin permissions
- **Steps:**
  1. Visit Guardium Support Portal Release Notes
  2. Download latest S-TAP, GIM, and CAS agent notes
  3. Review versions, features, and fixes
- **Tools:** Web-based
- **Type:** Knowledge

## Advanced Datasource Setup

- **Components:** Advanced datasource parameters
- **Prerequisites:** Established datasources, admin rights
- **Steps:**
  1. Go to **Configure > Datasources > Advanced**
  2. Adjust connection parameters
  3. Apply changes and test connectivity
- **Tools:** `grdapi update_advanced_datasource_parameters`
- **Type:** Configuration

## AWS Secrets Manager

- **Components:** AWS Secrets Manager datasource
- **Prerequisites:** AWS Secrets Manager enabled, IAM permissions
- **Steps:**
  1. Navigate to **Configure > Datasources > AWS Secrets Manager**
  2. Enter Secret Name and Region
  3. Test and save configuration
- **Tools:** `grdapi add_aws_secrets_manager_datasource`
- **Type:** Configuration

## CyberArk Integration

- **Components:** CyberArk safe management
- **Prerequisites:** CyberArk account, Guardium admin access
- **Steps:**
  1. Navigate to **Configure > Data Sources > CyberArk Safes**
  2. Enter safe details and associate Guardium groups
  3. Assign users/roles to safes
  4. Test and commit access
- **Tools:** `grdapi add_cyberark_safe`
- **Type:** Configuration

## Data Lifecycle

- **Components:** Cloud discovery jobs
- **Prerequisites:** CDA installed, network connectivity
- **Steps:**
  1. Navigate to **Discover > Cloud Discovery**
  2. Add new job, select cloud provider, specify parameters
  3. Set schedule frequency and targets
  4. Submit and monitor job status
- **Tools:** `grdapi create_cloud_discovery_job`
- **Type:** Action

## Datasource Configuration

- **Components:** Custom properties for datasources
- **Prerequisites:** Admin access, existing datasources
- **Steps:**
  1. Go to **Datasources > Manage > Custom Properties**
  2. Create "location" custom property
  3. Assign to relevant datasource groups
  4. Populate location data for each group
  5. Verify with group reports
- **Tools:** `grdapi add_custom_property`, modify_datasource_group
- **Type:** Configuration

## Security Configuration

- **Components:** CyberArk integration for passwords
- **Prerequisites:** CyberArk account, Guardium credentials
- **Steps:**
  1. Navigate to **Setup > External Apps > CyberArk**
  2. Add CyberArk integration details
  3. Configure datasource to use external password from CyberArk
  4. Test connectivity

## Monitoring and Compliance

### Deploy Linux-UNIX S-TAP Agent
- **Pre-requisites:** Supported Linux distribution; GIM or shell access on target host
- **Execution Steps:**
  1. Select installation method (GIM, RPM, or shell script).
  2. For RPM: `rpm -ivh Guardium_Stap_<version>.rpm`.
  3. For Shell: Run `install_stap.sh` with administrative privileges.
  4. Confirm installation via **Health > S-TAP Control**.
- **APIs/Tools:** `grdapi install_stap, validate_stap_agent`

### Monitor Compliance with Custom Properties
- **Pre-requisites:** Custom property "location" assigned to datasources
- **Execution Steps:**
  1. Create a compliance policy focusing on the "location" classification.
  2. Execute compliance check via **Monitor > Compliance > Run Assessment**.
  3. Review results in the Compliance Summary dashboard.
  4. Modify policies based on findings.
- **APIs/Tools:** `grdapi create_compliance_policy, run_compliance_check`

## Administration

### Customize User Navigation Menus
- **Pre-requisites:** Admin role with menu customization privileges
- **Execution Steps:**
  1. Navigate to **Setup > User & Roles > Users/Groups**.
  2. Select a user or group and choose **Menu Customization**.
  3. Drag and drop menu items to desired locations.
  4. Save changes and verify by logging in as the affected user.
- **APIs/Tools:** `grdapi modify_user, set_menu_customization`

## Entity Management

### Create New Datasource
- **Pre-requisites:** Administrator role; datasource details (hostname, credentials)
- **Execution Steps:**
  1. Go to **Datasources > Add Datasource**.
  2. Choose Application Type and provide Name, Hostname, Port.
  3. Enter authentication details and test connection.
  4. Adjust additional settings (e.g., SSL, operating system).
  5. Save and verify datasource appears in the list.
- **APIs/Tools:** `grdapi add_datasource, test_datasource_connection`

## Datasource Configuration

### Configure Couchbase Datasource with Account Field
- **Pre-requisites:** Couchbase Server installed and running; network connectivity verified
- **Execution Steps:**
  1. Log in to the Guardium web interface with admin privileges.
  2. Navigate to **Datasources > Add Datasource** and select **Couchbase**.
  3. Enter the **account** field with the desired user name (e.g., `datasource_owner`) and set the **directory** field to the Couchbase installation directory (e.g., `/opt/couchbase`).
  4. Specify the hostname, port, and credential details for the Couchbase server.
  5. Test connection and save the datasource configuration.
- **APIs/Tools:** `grdapi add_datasource`

## Host Alias Configuration

### Configure Host Aliases for Data Sources
- **Pre-requisites:** Certificate DNS name available; gdp.host value determined
- **Execution Steps:**
  1. Compare certificate DNS name with gdp.host value (see Comment 69).
  2. SSH into Guardium CLI: `ssh cli@a1.corp.com`.
  3. Execute the script: `create_user_hierarchy_api_call.txt` (see Keywords 70/71).
  4. Run `guardcli addHostAlias hostName <value>` for each user hierarchy level.
- **APIs/Tools:** GuardAPI; `grdapi addHostAlias`

## Kubernetes Deployment

### Deploy Vulnerability Scanner Chart
- **Pre-requisites:** Kubernetes cluster provisioned; Helm installed
- **Execution Steps:**
  1. Clone the vulnerability scanner repository.
  2. Navigate to `src/va-scanner` directory.
  3. Customize the chart as required (see Knowledge 74).
  4. Install the chart: `helm install my-scanner ./va-scanner`.
  5. Verify deployment status.
- **APIs/Tools:** Helm CLI: `helm install`; Kubernetes API

## Firewall Configuration

### Remove Existing Jumps to Custom Chains
```bash
iptables -X <custom_chain>
```
Removes iptables jumps to the specified custom chain, cleaning up configuration.

---

### Restart S-TAP Process via Command Line
```bash
guard-config-update --restart stap
```
Restarts the Guardium S-TAP process to apply recent changes or recover from errors.

---

### Create AWS RDS Instance Using CLI
```bash
aws rds create-db-instance --db-name mydb --db-instance-identifier mydb \
   --db-instance-class db.t3.medium --engine mysql --allocated-storage 20 \
   --master-username admin --master-user-password Admin123!
```
Provisions a new MySQL RDS instance with defined attributes for production use.

---

## Certificate Configuration

### Configure Client Web Certificates
1. Import PKCS12 keystore:
   ```bash
   keytool -importkeystore -srckeystore client.p12 -srcstoretype pkcs12 \
          -destkeystore client.jks -deststoretype jks -alias client-cert
   ```
2. Update web server config to reference `client.jks`.

3. Verify TLS connections present the certificate correctly.

---

### Generate Self-Signed Certificate
```bash
openssl req -x509 -newkey rsa:2048 -keyout client.key -out client.crt -days 365 -nodes
```
Creates a self-signed X.509 certificate for development or testing environments.

## Fine-Grained Access Control

Configure FGAC by defining roles and object-level permissions then assigning them to users. Use `grdapi set_access_rule`.

## Rollback Deployments

### General Rollback
Check current version with `kubectl rollout history deployment <name>` and undo to previous version using `kubectl rollout undo deployment <name>`.

### Specific Revision Rollback
List revisions with `kubectl rollout history deployment <name>` and rollback to a chosen revision using `kubectl rollout undo deployment <name> --to-revision=<number>`.

### Disable HPA Before Upgrade
Verify HPA status with `kubectl get hpa <name>` then disable autoscaling with `kubectl scale --replicas=1 hpa <name>`.

## Deployments

### Manual Scaling
Identify the target deployment with `kubectl get deployments` and scale using `kubectl scale --replicas=<count> deployment <name>`.

### Helm Chart Customization
Edit `my-values.yaml` to modify configuration parameters, then save and close the file.

### Namespace Handling
Install a Helm chart with a pre-existing namespace by setting `--set namespace.create=false` in the helm install command.

## Kubernetes Operations

### Delete Deployment
Remove a deployment using `kubectl delete deployment <name>`.

### Package Helm Chart
Package the chart with `helm package ./src/va-scanner -d releases`.

## Data Protection Connectivity

### Verify API Key Secret
- Execute `kubectl get secret va-scanner-credentials -n va-scanner -o jsonpath="{.data.GDP_API_KEY}" | base64 -d`
- Confirm decoded value is present

## Connection Testing

### Test Guardium Reachability
- Follow provided command snippet
- Check for successful connection confirmation

## Cluster Diagnostics

### Check Cluster Status
- Run `kubectl cluster-info`
- Verify version and services appear correctly

## Monitoring

### Monitor Deployment Rollout
- Monitor with `kubectl rollout status deployment/va-scanner-<version> -n va-scanner`
- Ensure all pods show "Running" status

## Resource Monitoring

### Monitor Pod Resource Usage
- Execute `kubectl top pods -n va-scanner`
- Review CPU and memory consumption

## Node Resource Assessment

### Monitor Node Resource Consumption
- Run `kubectl top nodes`
- Observe CPU, memory, and disk utilization

## Repository Management

### Clone Scanner Repository
- Run `git clone https://github.com/Guardium/va-scanner-helm.git`
- Change to `va-scanner-helm` directory

## Helm Installation

### Install va-scanner Chart
- Navigate to repository directory
- Run `helm install va-scanner ./charts/va-scanner`

## Guardium Workflow Reference

### Configure MS SQL Datasource
- Collect hostname, port, authentication details
- Add datasource, test connection, save configuration

### Flatten Groups via API
- Gather group names, identify to flatten
- Execute flatten_groups API
- Confirm flattened structure in UI

### Remove User via REST
- Authenticate to Guardium REST API
- Execute delete_user operation
- Verify removal via reports or UI

### Transform Session Data Policy
- Create policy rule for session transformations
- Set conditions, configure transformation logic
- Test in controlled environment

### Authorize Cloud Service Communication
- Identify Cloud service domain
- Execute authorize_domain command
- Confirm authorization through logs

## Guardium Workflows

### Configure Object Filtering in File Activity Monitoring
- **Purpose:** Define which files or file paths are monitored by the File Activity Monitoring (FAM) feature.
- **Steps:**
  1. Open **File Activity Monitoring** > **Policy Management**.
  2. Click **Create New Policy**, give it a name and description.
  3. In the **Object Filtering** tab, add file pathways with the `+` icon.
  4. Validate policy syntax, then **Save** and **Activate**.
- **Tools:** grdapi `create_policy`, `add_filter_object`.
- **Use Case:** Auditing sensitive data accesses.

### Delete Unused GIM Bundles
- **Purpose:** Clean up the Guardium Installation Manager (GIM) repository by removing bundles that are no longer needed.
- **Steps:**
  1. Run `grdapi gim_list_unused_bundles` to list bundles eligible for removal.
  2. Note the returned bundle IDs.
  3. Execute `grdapi gim_remove_bundle bundle_id=<id>` for each bundle.
  4. Re-run `gim_list_unused_bundles` to confirm removal.
- **Tools:** grdapi `gim_list_unused_bundles`, `gim_remove_bundle`.
- **Use Case:** Freeing storage space and reducing clutter.

### Set Up System Backup Configuration
- **Purpose:** Define how and where system backups are stored and how they are authenticated.
- **Steps:**
  1. Navigate to **Setup > System Backup**.
  2. Click **Configure System Backup**.
  3. Select backup type (local or remote), specify storage path.
  4. Choose authentication method and enter credentials.
  5. Save configuration and verify with a test backup.
- **Tools:** grdapi `configure_system_backup`.
- **Use Case:** Ensuring data can be recovered in case of system failure.

### Manage Classification Process and Rules
- **Purpose:** Maintain and clean up classification policies and rules used for detecting sensitive data.
- **Steps:**
  1. Go to **Data Management > Classification**.
  2. Use `delete_classifier_process` to remove obsolete processes.
  3. Execute `delete_classifier_rule` with `processName` and `ruleName`.
  4. Verify changes with `list_policy_fam_rule`.
- **Tools:** grdapi `delete_classifier_process`, `delete_classifier_rule`.
- **Use Case:** Keeping classification configurations current and relevant.

### Verify Certificate and Network Connectivity
- **Purpose:** Ensure that certificates are valid and that network connectivity between Guardium and its components is functioning.
- **Steps:**
  1. In the Guardium UI, go to **Administration > Certificates**.
  2. Locate the certificate, select **Verify**.
  3. Run `grdapi verify_certificate` with the certificate name.
  4. Test connectivity with `grdapi ping_server host=<hostname>`.
- **Tools:** grdapi `verify_certificate`, `ping_server`.
- **Use Case:** Troubleshooting and ensuring secure communications.

## Guardium Scanner Service Verification

### Verify Network Connectivity for Guardium Scanner Service
- **Purpose:** Confirm that the Guardium Scanner Service can reach the Guardium Data Protection system over the network.
- **Steps:**
  1. Check that the scanner service is running in the `va-scanner` namespace using `kubectl get pods -n va-scanner`.
  2. Perform a TCP connectivity test from the scanner pod to the Guardium host with `kubectl exec -n va-scanner -it <scanner-pod> -- nc -vz <guardium-host> <port>`.
  3. Confirm successful connections (e.g., "Connection to <guardium-host> <port> port [tcp/*] succeeded!").
  4. Verify DNS resolution between environments if using hostnames.
- **Tools:** kubectl, `nc`, `ping`.
- **Use Case:** Troubleshooting deployment issues and deployment health checks.

## Classification Rules

### Delete Classifier Document Rule
- **Purpose:** Remove a document classification rule from the Guardium system.
- **Steps:**
  1. Open a terminal or API client.
  2. Send a DELETE request to `/api/activities/delete_classifier_document_rule`.
  3. Include the rule ID in the request body.
  4. Verify the rule deletion in the Guardium UI.
- **Tools:** REST API `DELETE /api/activities/delete_classifier_document_rule`.
- **Use Case:** Updating and maintaining classification rule sets.

## Monitoring and Troubleshooting

### Monitor Sniffer Buffer Usage
- **Purpose:** Check and manage the usage of the sniffer buffer to ensure efficient data capture.
- **Steps:**
  1. SSH into the Guardium appliance.
  2. Run `/usr/local/guardium/guard_stap/restart_sniffer_buffer_usage`.
  3. Use the `--yes` flag to bypass confirmation prompts.
  4. Check logs for completion and error messages.
- **Tools:** `restart_sniffer_buffer_usage` command.
- **Use Case:** Performance tuning and issue resolution.

## Security Configuration

### Skip Registry Certificate Installation on Cluster Nodes
- **Purpose:** Bypass the installation of registry certificates on cluster nodes during certain operations.
- **Steps:**
  1. Ensure the cluster is set up with nodes and Guardium v9.5 or later.
  2. Follow the specific procedure to skip registry certificate installation as per Guardium documentation.
- **Tools:** Guardium administrative tools and CLI.
- **Use Case:** Streamlining deployment processes in specific environments.

## Consolidated Guardium Configuration

### Ensure Online Nodes Before Installation
* Verify that all cluster nodes are fully operational before proceeding with the installation process.

### Configure Certificate Distribution
* Utilize the `skip_registry_certificate_installation` tool to manage certificate settings across the cluster.

### Skip Registry Nodes During Installation
* Execute the installation process while omitting registry nodes to streamline deployment.

### Validate Certificates Across All Nodes
* Confirm that certificates are correctly installed and recognized on every node in the system.

## Workflow Definitions

### Create CAS Template
* Prepare a JSON definition file detailing the template components.
* Run `guardcli cas create_template --template <file>.json`.
* Confirm successful creation via the Guardium UI.
* For non-CLI methods, use the `create_cas_template` GuardAPI function.

### Delete CAS Template
* Gather the target template's ID.
* Send a DELETE request to `/api/guardapi/delete_cas_template` with `template_id=<ID>`.
* Confirm removal through the API response or UI verification.

## API Access Control

### Manage REST API Availability
* Ensure Guardium version 10.x+ is installed with an admin user and valid SSL certificate.
* Navigate to **System Configuration > Support Tools > REST API Access**.
* Toggle **Enable REST API Access** to the desired state (On/Off).
* Select the protocols (HTTP, HTTPS, or both) and configure the listen port (default 8443 for HTTPS).
* Save changes and restart the appliance for effects to take place.
* Note: GUI only; no API or tools required.

## System Operations

### Resolve Duplicate Identifier Problems
* Locate duplicate Global IDs or Unique Prefix IDs in managed units via the UI or CLI.
* Use **Systems > Managed Units** to identify duplicates.
* Apply the **Update ID** feature or run `guardium update_id` to correct identifiers.
* Recheck for duplicate errors to ensure resolution.

### View Network Interface Information
* Open the CLI on the Guardium system.
* Execute `show network interface inventory` to list all ports and MAC addresses.
* Review the output for detailed network interface data.

## Security Policies

### Define Security and Operational Rules
* Access the Guardium UI or CLI to modify security settings.
* Adjust parameters such as `failover_tls`, `fam_enable`, `firewall_default_state`, `discovery_interval`, and `discovery_port`.
* Apply changes and restart relevant services if necessary.

## Client Compatibility

### Manage OS Version Upgrades
* Enable `auto_install_on_db_server_os_upgrade` in Guardium to automate module updates.
* Monitor OS vendor updates on client systems.
* Verify Guardium module compatibility after OS changes.
* Validate successful post-upgrade installations.

## Data Source Setup

### Add Mandatory and Optional Data Source Attributes
* Access the data source configuration interface.
* Input the required **testDescription** for each data source.
* Optionally set the `datasourceType` using the `--help` flag if needed.
* Save the configuration to apply settings.

## Scheduled Reporting

### Set Up Repeating Reports
* Open **Report Builder** and select an existing or new report template.
* In the report properties, set **Mode** to **Scheduled**.
* Define the recurrence pattern (e.g., daily, weekly, monthly).
* Specify the delivery method and target (email, FTP, file system).
* Configure destination authentication and permissions as required.
* Save and enable the scheduled report.
* Utilize GuardAPI (`schedule_report`) or REST API (`/api/report/schedule`) for API-based scheduling.
* Create templates for frequently distributed reports to streamline sharing workflows.

## Network Settings

### Configure Default Router and DNS
* Determine the correct IP for the default router and DNS servers.
* Set the DNS server with `support store name-server <DNS_IP>`.
* Set the default router with `support store default-router <ROUTER_IP>`.
* Ensure all network configurations align with established topology requirements.

# Compressed Configuration Reference

## Security Configuration
### Create Certificate Signing Requests for Guardium Components
- Log in to the Guardium CLI and use `create csr` with the appropriate options:
  - `external_stap`
  - `gui rfc7468`
  - `mysql`
  - `insights`
- All operations are performed via the `create csr` GuardAPI command.

## Configuration Management
### Schedule Module Uninstallation via GIM
- Requires GIM client and target IP, date/time, and module names.
- Use `gim_schedule_uninstall` API with those parameters.

## Database Discovery
### Discover Databases in Guardium
- Select regions, apply filters, and start discovery from the **Database Discovery** page.

## Active Threat Analytics
### Manage Threat Cases
- Operations include reopening cases, changing threat categories/severities, and logging correct details.

## Session Time Management
### Define Time-Based Session Policy
- Set time range, server ports, and actions for Guardium sessions.

## Data Upload Sources Configuration
### Configure NAS and SharePoint Data Upload Sources
- Enable FAM, provide credentials, and configure monitoring options.

### Configure PCI DSS Data Upload Sources
- Specify PCI Authorized Server IPs and Source Programs.

### Assign Events to Audit Processes
- Create/process audit roles, test with an event.

## SAML Configuration
### Configure SAML Authentication
- Upload IdP metadata or configure manually, map attributes, test connection, and assign roles.

### Implement SAML Metadata Generation
- Generate SP metadata XML and provide to IdP.

## Guardium Administration

### Define Exclusion Client List for Inspection Engines
- **Components:**
  - **Pre-requisites:** Administrator role; clear exemption requirements  
  - **Execution Steps:**  
    1. Open **Inspection Engines > FGAC Settings > Client List**  
    2. Choose **Include** or **Exclude**  
    3. Add client IPs/ranges with annotations  
    4. Apply changes and restart engine if needed  
  - **APIs/Tools:** `grdapi add_exclusion_client`  
- **Types:** Configuration  
- **Customization:** Desktop shortcut to client list configuration page  

### Set Database Type and Connection Parameters
- **Components:**  
  - **Pre-requisites:** Guardium access; database connectivity  
  - **Execution Steps:**  
    1. From CLI select database type (MySQL, MSSQL, Informix, etc.)  
    2. Answer double‑quoted‑string prompt (Y/N)  
    3. Enter hostname/IP and follow remaining prompts (port, auth, etc.)  
    4. Verify connection and save configuration  
  - **APIs/Tools:** CLI menu `setup > tools and views > manage sets > create DB type menu`  
- **Types:** Configuration  
- **Customization:** Script to automate DB type selection and parameter entry  

**Note:** The remaining entries ("Guardium Agent Installation on IBM i", "Verify Installation",  "Deploy External S-TAP in Cloud Pak for Data", etc.) are action‑oriented placeholders without substantive content, so they are omitted per **Quality Gate G4** (no duplicate concepts) and **Noise G5** (drop noise).

## Components

- **Pre-requisites:** Basic familiarity with GuardAPI commands
- **APIs/Tools:** Any valid GuardAPI command; `--help=true` for error examples

## Add Autodetect Task via API

- **Pre-requisites:** Guardium appliance with autodetect module enabled
- **APIs/Tools:** `curl` or any HTTP client; `/autodetect/create` endpoint

## Configure Cold Data Streaming to DMS

- **Pre-requisites:** Guardium appliance with DMS enabled; defined cold storage location
- **APIs/Tools:** GuardAPI `add_cold_storage_config`, `grdapi set_cold_storage_policy`

## Create Datasource Group Reference

- **Pre-requisites:** Administrator access; existing application definitions
- **APIs/Tools:** `create_datasource_groupRef_by_name`

## Add Member to Access Group

- **Pre-requisites:** Administrator role; predefined group and member details
- **APIs/Tools:** `add_member_to_group` Guardium CLI command

## Create Test Exception via REST API

- **Pre-requisites:** Security assessment module enabled; REST API access
- **APIs/Tools:** REST API endpoint `/security_assessment/test_exceptions`; `PUT` request

## Configure Security Assessment Exclusions Workflow

- **Pre-requisites:** Guardium administrator role; security policy configured
- **APIs/Tools:** grdapi `add_assessment_exclusion`, Guardium UI

## Manage Guardium Feature Flags Workflow

- **Pre-requisites:** API_ACCESS permission; feature flag names identified
- **APIs/Tools:** REST API (POST/GET), grdapi `feature_flag_control`

## Enable FIPS Mode with TLS Adjustments Workflow

- **Pre-requisites:** Administrator access; TLS 1.3 currently enabled (if Guardium 12.0/12.1)
- **APIs/Tools:** enable_fips_tls (GuardAPI), TLS Configuration UI

## Detect Repeated Failed Administrative Logins

- **Pre-requisites:** Central Manager hostname verified; Auditing enabled for login events
- **APIs/Tools:** grdapi `create_report`

## Incident Management

- Set incident generation threshold and map incidents to users via UI or API.

## Host Verification

- Verify and correct Central Manager hostname from the UI.

## Regulatory Control Setup

- Create controls with multiple requirements using the UI.

## Database Auditing

- Review database-specific prerequisites before setting up audit databases.

## CPU Monitoring

- Rerun scheduled distributed reports via GuardAPI.

## Access Control

- Create user hierarchies using the `create_user_hierarchy` GuardAPI.

## System Features

- Change and display custom images in the Guardium UI from Settings.

## User Management

- Prevent default role access for specific users via User Management.

## Cluster Management

- Acknowledge duplicate alias warnings during cluster alias updates.

## User Interaction

- Manually enter dates in YYYY-MM-DD format for various applications.

## Time Period Management

- Define time periods using the Time Period Builder in Admin Tools.

## Report Configuration

- Set report time frames in Report Builder, considering performance impacts.

## Templating and Security

- Import security definitions from templates, noting ownership and role implications.

## Group Management

### View Group Membership
- Navigate to **Groups > View Details** to see group usage across policies and reports. Use APIs/Tools: None. Streamline access reviews and policy optimizations.

## Datasource Configuration

### Configure Health Check and Upgrade Process
- Go to **Administration > System Settings > Maintenance**. Execute `grdapi install_health_check_patch`, verify with `grdapi get_task_status`, and apply `grdapi install_patch` for upgrades. Schedule checks weekly; automate agent upgrades.

## Access Control

### Configure Fine-Grained Access Control
- Define roles and object-level permissions at **Setup > Access Control > FGAC**, assign roles to users, and test access with a restricted account. Use `grdapi set_access_rule`.

### Implement Fine-Grained Access Control (FGAC)
- Access **Setup > Access Control > FGAC** to create roles, define object-level permissions, assign roles to users, and validate access. Use `grdapi set_access_rule`. Template-based role creation for new departments.

## 329. Check S-TAP service status on Windows

### Check S-TAP Service Status on Windows
- Open **Command Prompt** as Administrator, run `sc query MSSQLSERVER`, and execute `sts reload`. Automate with batch script or PowerShell cmdlet.

## High-Level System Health and Agent Functionality Post-Upgrade

### Verify System Health and Agent Functionality Post-Upgrade
- **Tools:** Guardium UI, S-TAP upgrade scripts
- **Verification Steps:**
  - Use the Guardium UI to check system health status
  - Run S-TAP upgrade scripts and validate successful execution
- **User Workflow:** Include S-TAP upgrade verification in the post-upgrade checklist

## Report Distribution Management
- **Pre-requisites:** Report authoring permissions
- **Execution Steps:** Open report definition interface > add recipients on Distribution tab > schedule frequency > configure receivers/approvals > activate distribution
- **Types:** Configuration
- **Customization:** Individual department reporting schedules

## Report Filtering Mechanism
- **Pre-requisites:** Access to report builder
- **Execution Steps:** Open report > add Guardium Host Name parameter > select hosts > run report
- **Types:** Action

## Ad-Hoc Audit Reports
- **Pre-requisites:** Audit process permissions
- **Execution Steps:** Create Ad-Hoc Report > select Audit Process template > apply runtime parameters > preview > save
- **Types:** Action

## Audit Session Attributes
- **Pre-requisites:** Admin role; audit logs enabled
- **Execution Steps:** Setup > Auditing > Session Attributes > enable attributes > restrict to admins > verify logs
- **Types:** Configuration

## 365. Oracle Time Zone Example
- **Pre-requisites:** Oracle audit records exported
- **Execution Steps:** Identify END_TIME and TIME_ZONE fields > convert timestamps to common zone > correlate SESSION_ID across zones
- **Types:** Knowledge

## 366. CPU Usage Report
- **Pre-requisites:** Aggregated CPU data in audit repository
- **Execution Steps:** Edit report query to retain Date, User Name, Exception Type, Sum Of Exceptions > run > create constant attribute
- **Types:** Action
- **Customization:** Clone report with different thresholds

## 367. Add Group Member to Database
- **Pre-requisites:** Identify database version and patch level
- **Execution Steps:** Edit Group > Members tab > enter version in DB Ver field > specify patches > save
- **Types:** Configuration
- **Customization:** User-defined syntax per platform

## 368. Data Source Template Integration
- **Pre-requisites:** Admin or CAS role
- **Execution Steps:** Select data source > Save > ensure only admins/CAS users can access
- **Types:** Configuration

## 369. License Management Workflow
- **Pre-requisites:** Admin access
- **Execution Steps:** Refresh keys > Delete old keys > Import new keys > verify status
- **Types:** Action
- **Customization:** Automate via scheduled tasks

## 370. Tivoli Storage Manager Configuration
- **Pre-requisites:** TSM configuration file available
- **Execution Steps:** System Backup > select TSM > Import configuration file > Save settings
- **Types:** Configuration

## 371. Edge Gateway Upgrade
- **Pre-requisites:** Current admin rights and upgrade media

## Guardium System Upgrade

### Complete Guardium System Upgrade
- Verify access to admin tools, scripts, and upgrade package
- Review licensing requirements and ensure they are met
- Follow the specific upgrade procedure provided by the vendor
- Use the grdapi command `register_edge_gateway` to register the Edge Gateway to the central management platform

## Guardium Configuration Parameters

### Review and Adjust Load Balancing Parameters
- Ensure access to the Guardium S-TAP Control page
- Review parameters such as `DISK_USAGE_ADJUSTMENT_FACTOR` and `MAX_RELOCATIONS_BETWEEN_FULL_LOAD_COLLECTIONS`
- Adjust values within valid ranges as needed
- Document all parameter changes for audit purposes

## Patch Installation Verification

### Confirm Patch Installation Completion
- Verify that all specified systems have the patch installed
- Initiate synchronization file generation for the backup manager
- Confirm the synchronization process has completed successfully
- Schedule patch installations during low usage periods

## API Key Verification

### Check API Key Existence
- Navigate to System > Tools > Task Status in the Guardium UI
- Search for `api key exists`
- Verify the key validity from the results

## Data Export

### Export Report Definitions
- Ensure administrator access and export permissions
- Navigate to Reporting > Definitions
- Select the definitions to export
- Choose the file format and save the exported file securely

## API Key Management

### Verify API Key Validity via CLI
- Open the Guardium Command Line Interface (CLI)
- Run `guardapi verify_api_key key=78677d83-d5e9-4b05-9162-adc2698d7af5`
- Confirm the verification result

## Install S-TAP

### Install S-TAP on Direct Database Reporting
- Log into the Guardium system with administrator credentials
- Navigate to Datasources and select the reporting database
- Run the CLI command `install_stap host=<hostname> tap_version=<version>`

## Log Management for Db2

### Configure TLS/SSL for Db2 Logging
- Access the Db2 instance management console
- Enable TLS/SSL certificates and keys
- Deactivate A-TAP monitoring as needed
- Restart the Db2 instance to apply changes

## Hadoop Integration

### Configure Hadoop with Guardium
- Access Cloudera Manager
- Select the Cloudera Cluster distribution
- Configure the S-TAP host and settings
- Save the changes

## Rule Management

### Attach Main Rules to Processing Chains
- Access the main rule set management interface
- Select the rules to attach
- Use Hook to Chains to add them to existing chains
- Save the rule configuration

## S-TAP Health Checks

### External S-TAP Deployment
- Configure External S-TAP by opening the configuration wizard, completing the Docker tab with registry key and image details, entering database specifics on the Database tab, specifying Guardium collector information on the Guardium tab, configuring volume settings on the Volume tab, reviewing all settings, and clicking Deploy. The REST API handles External S-TAP configuration.

### Update cacerts.txt with External S-TAP Certificate
- Generate a certificate token with the bq CLI tool, then update the cacerts.txt file with the External S-TAP certificate. Validate the certificate integration using Certificate CLI Commands.

### Reset S-TAP Client Connection
- Open the Choose clients pane in Guardium, select the affected client, and click Reset Connection. Verify the connection status using the monitoring icon. The command for resetting the connection is `grdapi reset_stap_connection`.

### GIM Client Auto-Discovery
- Ensure the GIM client is set to listener mode, restart the GIM service to trigger auto-discovery, and monitor the collector for new GIM client connections. Use `grdapi gim_auto_discovery` for this operation, scheduling it during off-peak hours if necessary.

### S-TAP Monitoring
- Open the Choose clients pane in Guardium, select the affected client, and click Reset Connection to reset an S-TAP client connection. Verify the connection status using the monitoring icon. Use `grdapi reset_stap_connection` for this action.

### Install Patch Using SCP
- Use the `store system patch install scp` command, providing the hostname, path to the patch, and remote system password. Include a wildcard for multiple patch files if needed, and execute the command while monitoring the installation process. This command is used for installing patches via SCP.

## Policy Example for IP Range Matching
- **Components:** Guardium Policy Editor
- **Steps:**
  1. Open Policy Editor and create new rule
  2. Define IP range: `SOURCE_IP: 192.168.0.0/16`
  3. Set actions and conditions
- **Automation:** `grdapi create_rule`
- **Workflow:** Tailor IP range and conditions based on organizational security needs

## Guardium Archive Management
### Create User Hierarchy for Data Access Control
- **Components:** Guardium user accounts
- **Steps:**
  1. Log in to Guardium interface
  2. Execute `grdapi create_user_hierarchy userName=ADAMS parentUserName=SCOTT`
  3. Verify hierarchy in user permissions
- **Tool:** `grdapi create_user_hierarchy`

### Run Vulnerability Assessment (VA) Scanner
- **Components:** VA scanner installed
- **Steps:**
  1. Ensure scanner network connectivity
  2. Run scanner from Guardium console
  3. Schedule scans with other tasks

### Manage Certificates for CAS
- **Components:** CAS on Windows server
- **Steps:**
  1. Access Guardium CLI
  2. Run CLI commands for CAS management
  3. Follow prompts to install/run and configure CAS

### Export CAS Host Definitions
- **Components:** Guardium Data Protection console
- **Steps:**
  1. Navigate to **Manage > Aggregation & Archive > Export**
  2. Select **CAS Hosts**
  3. Choose definitions to export
  4. Click **Export** and save the file

### Configure System Backup/Data Archive
- **Components:** Valid license; storage method configured
- **Steps:**
  1. Select **Admin > Archive Administration**
  2. Choose Archive or Backup configuration
  3. Specify storage method and credentials
  4. Save configuration and schedule archive

## System Login Verification
- **Purpose:** Ensure the Guardium UI URL format `https://<host>:8443` and smart card login functionality.
- **Steps:** Navigate to **System > Login**, check the URL, verify the smart card feature is active, and log in with a valid smart card.

## Licensing Check
- **Purpose:** Retrieve the remaining license count of the Guardium system.
- **Steps:** Run a database query to fetch the license count; the result shows `430` licenses remaining.

## User Exemption from MFA
- **Purpose:** Exempt specific users from multi-factor authentication (MFA).
- **Steps:** Go to **Access Control > Exemptions**, select the user accounts, add them to the exempt list, and save the configuration. Verify the exemption by attempting login without MFA.

## Overload Detection and Mitigation
- **Purpose:** Identify and resolve overloaded systems in the deployment.
- **Steps:** Open **Topology View**, locate nodes marked as overloaded, investigate the root cause (e.g., resource saturation), and apply mitigation steps such as scaling or reassigning resources.

## Enterprise Load Balancing Activation
- **Purpose:** Set up enterprise load balancing to distribute traffic across Guardium nodes.
- **Steps:** Access **GuardAPI: Grid Management > Enterprise Load Balancing**, configure `load_balancer_port`, and point S-TAP instances to the Central Manager via the **S-TAP Control** page.

## S-TAP Service Verification
- **Purpose:** Ensure the S-TAP service is running on Windows systems.
- **Steps:** Open **services.msc**, locate the *S-TAP* service, and verify it is in the `Running` state.

## S-TAP Verification Utility
- **Purpose:** Perform comprehensive verification checks on the installed S-TAP.
- **Steps:** Open the **S-TAP Verification Utility**, review the configuration checks, adjust the verification schedule via **Verification Schedule** settings, and review remediation recommendations for any failures.

## Teradata Exit Library Verification
- **Purpose:** Verify the correct symbolic link to the Teradata exit library.
- **Steps:** Check the symbolic link, create the correct link if necessary, and verify the library connection.

## S-TAP GUI Installation
- **Purpose:** Choose and complete a typical installation of S-TAP via the GUI installer.
- **Steps:** Launch the GUI installer, select **Typical** installation, and complete the setup wizard.

## Custom S-TAP Verification on Windows
- **Purpose:** Perform custom verification steps on Windows S-TAP installations.
- **Steps:** Navigate to **Verify S-TAP on Windows**, identify and execute custom verification steps, and review results.

## Automated S-TAP Startup Configuration
- **Purpose:** Configure automatic checks for S-TAP during system startup.
- **Steps:** Review automatic startup settings, configure `wait_for_db_exec` for periodic verification checks using GuardCtl.

## A-TAP Configuration Persistence
- **Purpose:** Save and persist A-TAP configurations.
- **Steps:** Configure A-TAP parameters and run the `save-active-ataps` command to persist the settings.

## Data Archiving and Purging Setup
- **Purpose:** Configure data purging and archiving policies to manage data retention.
- **Steps:** Navigate to **Setup > Tools and Views > Data Archiving and Purging**, define the purging period, enable purging without archiving if needed, and save the changes using `grdapi set_data_purge`.

## GuardAPI Entity Management
- **Purpose:** Use GuardAPI functions for managing entities in the Guardium system.
- **Steps:** Ensure the Guardium system is operational and API access is enabled, then utilize GuardAPI functions to manage entities (specific steps depend on the function used).

## Security Assessment Workflows

### Create an Assessment
- **Components:** 
  - Guardium V9.5 or later, API access enabled
- **Execution Steps:**
  1. Open `Setup > Security Assessment > Create Assessment`.
  2. Choose the **POST** method for the REST API.
  3. Fill out the required details in the assessment form.
  4. Submit to add the assessment.
- **APIs/Tools:** REST API (Create Assessment endpoint)
- **Customization:** Save assessment templates for frequent use.

## Security

### Interface Tools for Role and Application Management
- Navigate to **Setup > Users and Roles > Interface Tools** to review and adjust tool access for default roles and applications.  
- Use `grdapi set_interface_tool_permission` for API-based adjustments.  
- **Category:** Configuration

## Guardium System Configuration

### Setup Central Manager
- Log in to the CLI and run `store system unit_type manager`. Apply the product key via GUI or `store license upload`.  
- **Category:** Action

### Install Patch on Managed Units
- In **Configuration > Patch Management**, select units, choose the patch file, schedule installation, and confirm.  
- Available via GuardAPI or Enterprise Hub UI.  
- **Category:** Action

### Skip Registry Certificate Installation on Cluster Nodes
- In **Setup > Cluster Management**, select the node and uncheck *Install Registry Certificates*. Save the setting.  
- CLI alternative: `grdapi cluster_node_set skip_registry_cert=1 node=<node_name>`.  
- **Category:** Configuration

### Disable ORA-017 Error Alerts
- Create a new rule in **Setup > Access Control > Rules** with *Database = Oracle* and *Error = ORA-017*. Set action to *Skip Alert*.  
- CLI alternative: `grdapi create_rule rule_name="Skip ORA-017"`.  
- **Category:** Configuration

### Export Guardium Policies to XACML
- Use **Reports > Policy Export**, select XACML, and click **Export**.  
- CLI alternative: `grdapi export_policies format=xacml`.  
- **Category:** Action

### Buffer Usage Monitor Report
- Background process enabled via `grdapi enable_buffer_usage_monitor`.  
- **Category:** Configuration

## Security Tools

### Verify API Key Exists
- Locate the API key `96d266b6-c9bd-4421-a451-964ffb566b7b` and run the associated API action to confirm updated secrets.  
- **Category:** Action  
- **Subcategory:** Customization – Store API keys securely for automated use.

## Installation Guidance

### Configure Initial Customer Information
- During installation, enter required details on the Customer Information screen, accept defaults as needed, and confirm.  
- Available in the Installation Wizard.  
- **Category:** Configuration  
- **Subcategory:** Customization – Save configuration files for reuse.

## Troubleshooting S-TAP

### Resolve S-TAP Installation Issues
- Edit parameters via the Modify page or GIM (`guard_tap.ini`). Restart S-TAP if issues persist. Escalate to support if needed.  
- **Category:** Action  
- **Subcategory:** Customization – Document changes for audit trails.

## S-TAP Process Control

### Manage S-TAP Restart Modes
- Use mode 0 for standard restart or mode 1 to preserve buffered data. Run the restart command with the appropriate option and verify status.  
- Required when operational needs change.  
- **Category:** Action

## Session Management

### Handle Ignored Sessions
- Add S-TAPs to the verification schedule, clear ignored session settings as needed, and use *Revoke All Ignored Sessions* to reset. Monitor traffic afterward.  
- Available in the Guardium UI.  
- **Category:** Action  
- **Subcategory:** Customization – Schedule regular session cleanups.

## Diagnostic File Management

### Manage Debug Files
- Identify `WINSTAP_DEBUG` files in the S-TAP logs. Use them for troubleshooting critical issues.  
- Requires debug mode enabled.  
- **Category:** Action  
- **Subcategory:** Customization – Archive logs regularly to free disk space.

## S-TAP Statistics Monitoring

- Access S-TAP Statistics report to collect and review system monitoring data.
- Configure alerts based on report thresholds.

## GAM Agent Installation

- Log in as an administrator.
- Run the GAM installation process and follow prompts to complete setup.

## S-TAP Oracle Startup Workflow

- Execute startup and discovery commands after S-TAP installation.
- Handle tasks based on return codes, using Oracle CLI and S-TAP scripts.

## Feature Highlight

### S-TAP Statistics Report Details

- Access detailed S-TAP statistics report to analyze data and identify key metrics.
- Create alerts or additional reports based on observed data patterns.

## A-TAP Management Workflows

### Manage A-TAP During System and Database Upgrades

- Backup configurations.
- Follow the Guardium A-TAP Guide to deactivate before upgrades and reactivate afterward.

## 493. Plugin values

### Check and Save Active A-TAP Instances

- Use `is-active` to check active A-TAP instances.
- Execute `save-active-ataps` to save configurations.

## 495. Related tasks

### Monitor A-TAP Statistics and Traffic Flow

- Monitor the `activated_ataps` parameter for active instances.
- Ensure Guardium appliance and database server are in the same data center or consider load balancing if overloaded.

## Consolidated Reference for Guardium System Operations

## User Workflows

### Schedule Regular Node Job Checks
- Schedule periodic assessments of node job statuses for operational oversight.

## External Key File Deployment

### Transfer Key Files to Managed Units
- Copy key files from an external server to managed units and the central manager.

## Policy Installation

### Deploy Security Rule
- Create, save, and install a security rule using Guardium Policy Builder.

## GIM Bundle Uninstallation

### Remove Bundles via Interface
- Uninstall bundles from client groups through the GIM interface.

## API Key Verification

### Confirm API Key Presence
- Check the existence of an API key in the Guardium API Management section.

## Guardium System Verification

### Check S-TAP Status
- Verify S-TAP online status from the Guardium UI.

## Database Monitoring Configuration

### Set Up SSL for IBM Db2 (Windows)
- Configure SSL for Db2 on Windows via Guardium SSL Management.

## Configure for Client Web Certificates

### Create Cloud DB Service Account
- Add a service account for cloud databases using Guardium CLI or GUI.

## Discover Sensitive Data

### Identify Sensitive Data
- Define sensitive objects, create discovery policies, and run discovery.

## Uninstall Policy

### Remove Policy
- Deactivate and uninstall a policy from the Guardium system.

## Limit Monitoring to Sensitive Objects

### Configure Policy for Sensitive Data
- Define groups, identify sensitive objects, and apply a monitoring policy.

Configuration
- **Customize user workflows** by tailoring group and object definitions for specific monitoring needs.

Configure for Client Web Certificates
- **Steps:** Import certificates via **System > SSL/TLS** → **Client Web Certificates**, validate, save, and restart the collector.
- **Automation:** Use `grdapi import_cert` and batch scripts for bulk imports.

Special Handling for TRANSFORM Actions
- **Action workflow:** Edit TRANSFORM actions in **Policy Builder**, adjust rules, save, and deploy using `grdapi update_policy`.

Special Handling for TRANSFORM Actions
- **Server Groups configuration:** In **Policy Builder**, create or edit a rule, select/define server groups in the **Server Groups** dropdown, and save using `guardapi add_server_group`.

Special Handling for TRANSFORM Actions
- **Session timing:** Adjust data security policies to apply before user authorization, test, and deploy with `grdapi set_policy_timing`.

Special Handling for TRANSFORM Actions
- **Compliance Wizard:** Review actions, document required steps, and generate summaries with `grdapi generate_compliance_summary`.

Special Handling for TRANSFORM Actions
- **Custom compliance program:** Set up via **Data Compliance**, define controls, wizard configuration, validation, and activation with `grdapi create_compliance_program`.

Special Handling for TRANSFORM Actions
- **Dashboard filtering:** Filter charts individually via the **Filter** icon, manage general filters, and save configurations via `grdapi set_chart_filter`.

Special Handling for TRANSFORM Actions
- **Disable Advanced Threat Detection:** Disable globally or per collector, document groups, and use `grdapi disable_advanced_threat_detection`.

## Data Management
### Configure Scan Settings
- **Function:** Schedule data scans on Guardium appliances
- **Steps:** 
  - Open **Data Management > Data Scans > New Scan**
  - Name the scan, select the appliance, define frequency and source
  - Save configuration

## Entity Join Workflow
### Configure Entity Join Condition
- **Prerequisites:** Defined entities, edit permissions
- **Steps:**
  - Open data management interface
  - Add field pairs for join attributes
  - Verify and save join configuration

## S-TAP Management
### Stop IBM Security Guardium S-TAP Service
- **Prerequisites:** S-TAP installed, admin rights
- **Steps:**
  1. Open Windows Services
  2. Stop IBM Security Guardium S-TAP
  3. Verify service stopped in Guardium UI

## S-TAP Monitoring and Configuration
### Verify S-TAP Inspection Engines
- **Prerequisites:** Guardium UI access
- **Steps:**
  - Go to **Monitor > S-TAP Status**
  - Click **Verify Engine** for the desired inspection engine

### Configure Dynamic Ring Buffers for Monitoring
- **Prerequisites:** Admin access, guard_tap.ini writable
- **Steps:**
  1. Open **S-TAP Control**
  2. Set `ring_buffer` to `1`
  3. Save and restart S-TAP if needed

## Configuration Management
### Store GIM Server Certificates Using CLI
- **Prerequisites:** GIM server, keystore credentials
- **Steps:**
  - Run `gim_client_cert_install` for certificates
  - Use `gim_client_cert_install_from_file` for file-based certificates

### Configure Time Server Synchronization
- **Prerequisites:** Access to NTP/custom time server
- **Steps:**
  1. Run `store system time_server <address>`
  2. Restart network service

## 601. Special handling for TRANSFORM actions

### Create custom tables domain
- **Components:** Domain Finder panel
- **Steps:** Open Domain Finder > Click **Create New Domain** > Enter domain name matching custom table name > Save
- **Tools:** Domain Finder UI
- **Type:** Workflow

---

## Accessing Guardium Data Protection

### Access Guardium Data Protection
- **Components:** Web browser, valid credentials
- **Steps:** Navigate to Guardium console URL > Enter username/password > Click **Login**
- **Tools:** Login API, GuardAPI login command
- **Type:** Navigation

---

## Configuring Datasources

### Configure MS SQL Server Datasource
- **Components:** SQL Server hostname, port, authentication method
- **Steps:** Gather connection details > Navigate to **Datasources > Add Datasource** > Select connection type > Enter details > Test connection > Save
- **Tools:** GuardAPI, `grdapi add_datasource`
- **Type:** Configuration

---

## Managing Access Control

### Configure Fine-Grained Access Control
- **Components:** Administrator role, security policy
- **Steps:** Navigate to **Setup > Access Control > FGAC** > Define roles and permissions > Assign roles > Test access
- **Tools:** `grdapi set_access_rule`
- **Type:** Configuration

## Database Patching

### Apply Database Patches
- **Prerequisites:** Administrative access to Guardium system; patch files downloaded
- **Steps:**
  1. Navigate to **Policies > Database Patches**
  2. Upload the patch file or select from media
  3. Schedule the patch installation during low activity periods
  4. Monitor the patch status and verify installation
- **Tools:** `grdapi apply_patch`

## API Key Verification

### Verify API Key
- **Requirements:** Guardium system up and running; API key generated
- **Steps:**
  1. Log in to Guardium UI or use CLI
  2. Navigate to **Report** or **CLI** depending on preference
  3. Run `verify api_key <key_value>`
- **Tools:** GuardAPI `verify api_key`

## Operational Database Upgrades

### Upgrade Operational Databases without OS Changes
- **Prerequisites:** Operational databases running; existing S-TAP installation verified
- **Steps:**
  1. Plan the database software upgrade path
  2. Review S-TAP installation documentation for compatibility
  3. Perform database software upgrade following vendor guidelines
  4. Verify monitoring continuity and S-TAP functionality

## Ingress Configuration

### Configure Ingress Annotations
- **Prerequisites:** Access to ingress controller configuration
- **Steps:**
  1. Identify the required annotations for ingress routing
  2. Use the annotation IDs `b968734a-0b34-471c-98b2-959a7aec5de8` and `e7efac2a-21f7-4465-8871-ff8f6bd7d663`
  3. Apply annotations through ingress configuration files
  4. Validate ingress routing functionality

## GIM Client Installation

### Manually Install GIM Client on Windows
- **Prerequisites:** Administrative access to Windows machine
- **Steps:**
  1. Place GIM installer files in a designated directory
  2. Open command prompt with administrative privileges
  3. Navigate to installer directory and execute `setup.exe`
  4. Follow on-screen wizard instructions to complete installation

## Certificate Examination

### Examine Certificate Contents
- **Prerequisites:** Keystore access with proper permissions
- **Steps:**
  1. Use certificate command `list_certificates` to display keystore contents
  2. Apply filters for specific subsystems (e.g., MySQL) or aliases as needed
  3. Review output to verify certificate validity and details
  4. Document examined certificates for audit purposes

## Data Archiving

### Archive Data to SCP Server
- **Prerequisites:** SCP server access and credentials configured
- **Steps:**
  1. Execute `configure_results_archive` with appropriate parameters
  2. Set intervals for archive and ignore periods
  3. Enter SCP server authentication credentials securely
  4. Verify archive process initiation and status

## Event Hub Configuration

### Configure Event Hub
- **Prerequisites:** Event Hub namespace and policy details
- **Steps:**
  1. Navigate to Event Hub configuration section
  2. Select namespace, policy name, and monitoring name
  3. Enable logging and diagnostic streaming options
  4. Apply configuration and monitor initial streaming activity

## Client Web Certificates

### Configure Client Web Certificates with CSR
- **Prerequisites:** CSR generation access and certificate alias planning
- **Steps:**
  1. Generate Certificate Signing Request (CSR) for client
  2. Identify and enter a one-word alias for certificate identification
  3. Specify certificate subject details accurately
  4. Submit CSR to Certificate Authority for issuance

## Event Hub Using Web UI

### Configure Event Hub Details
- **Prerequisites:** Event Hub configuration access
- **Steps:**
  1. Open Event Hub setup interface
  2. Select appropriate namespace, policy, and name
  3. Configure logging and diagnostic parameters
  4. Save and enable streaming to Event Hub

## Access Policies

### Use Tuple Groups in Access Policies
- **Prerequisites:** Understanding of policy and tuple group concepts
- **Steps:**
  1. Create multiple rules for complex policy requirements
  2. Assign respective tuple groups to individual rules
  3. Test policy functionality with assigned tuples
  4. Document policy structure and tuple group usage

## Alert Configuration

### Configure Alerter to Deliver Messages
- **Prerequisites:** Alerter service installed; recipient lists defined
- **Steps (SMTP):**
  1. Open Guardium UI and go to **Configure > Alerter**
  2. Select **SMTP** from the delivery method dropdown
  3. Enter SMTP server details, sender address, and test with **Test Email**
- **Steps (SNMP):**
  1. Select **SNMP** from the delivery method dropdown
  2. Specify trap community and destination host, then validate
- **Steps (Syslog):**
  1. Select **Syslog** from the delivery method dropdown
  2. Set facility level and target system, and confirm
- **Steps (Custom Classes):**
  1. Select **Custom Class** from the delivery method dropdown
  2. Upload Java class files and configure parameters

## Special Handling for TRANSFORM Actions

- **Components:**
  - Pre-requisite: Full backup of `guard_tap.ini` created
  - Execution Steps:
    1. Stop S-TAP service: `stop_stap`
    2. Verify backup: `/usr/local/guardium/guard_tap.ini`
    3. Proceed to query rewrite setup
  - APIs/Tools: `stop_stap`, `cp`
  - Types: Action

## Configure Alerter Message Templates

- **Components:**
  - Pre-requisite: Email template definitions
  - Execution Steps:
    1. Navigate to **Configure > Alerter > Templates**
    2. Create or edit templates
    3. Use placeholders: `%ALERT_DESC%`, `%ALERT_URI%`
    4. Save and assign to alerter profiles
  - APIs/Tools: `store email_template`, GUI wizard
  - Types: Configuration

## Configure Fine-Grained Access Control

- **Components:**
  - Pre-requisite: Administrator role, security policy defined
  - Execution Steps:
    1. Navigate to **Setup > Access Control > FGAC**
    2. Define roles and object-level permissions
    3. Assign roles to user accounts
    4. Test access with a restricted account
  - APIs/Tools: `grdapi set_access_rule`
  - Types: Configuration

## Create User Hierarchy

- **Components:**
  - Pre-requisite: IAM configured; user and parent user exist
  - Execution Steps:
    1. Open User Management interface
    2. Select user and choose **Create Hierarchy**
    3. Enter parent user name
    4. Confirm and save
  - APIs/Tools: `grdapi create_user_hierarchy`
  - Types: Configuration

## Configure Network Settings

- **Components:**
  - Pre-requisite: Verified network connectivity
  - Execution Steps:
    1. Open Global Settings menu
    2. Select **Network Configuration**
    3. Input IP, subnet, gateway, DNS
    4. Save and apply
  - APIs/Tools: `grdapi configure_network`
  - Types: Configuration

## Install Data Security Policy

- **Components:**
  - Pre-requisite: Policy Builder accessible; policy file ready
  - Execution Steps:
    1. Open Policy Builder for Data
    2. Select **Add Policy**, browse and import policy file
    3. Choose **Install** and confirm
  - Types: Action
  - Customization: None

## Configure Data Source Authentication

- **Components:**
  - Pre-requisite: Guardium system configured; data source credentials ready
  - Execution Steps:
    1. Navigate to **Setup > Data Sources**
    2. Click **Add Data Source**, select type
    3. Provide host, port, database, authentication method
    4. Enter user and password
    5. Test connection, save
  - APIs/Tools: `add_datasource`, `modify_datasource`
  - Types: Configuration
  - Customization: Use API for bulk creation

## Enable FIPS Mode

- **Components:**
  - Pre-requisite: System meets FIPS compliance; administrative access
  - Execution Steps:
    1. Access Guardium CLI
    2. Execute `fipsmode enable=1 restart=0`
    3. Verify with `fipsmode status`
  - APIs/Tools: GuardAPI `fipsmode`
  - Types: Action
  - Customization: Schedule as part of audit preparation

## Configure Client Web Certificates

- **Components:**
  - Pre-requisite: CA certificates available; administrative access
  - Execution Steps:
    1. Navigate to **Setup > External Connections > Client Web Certificates**
    2. Import CA certificates
    3. Configure web server
    4. Test with `test_web_certificate`
  - APIs/Tools: `test_web_certificate`
  - Types: Configuration
  - Customization: Automate CA rotation

## Clone Data Source Template

- **Components:**
  - Pre-requisite: Existing data source; administrative access
  - Execution Steps:
    1. Navigate to **Setup > Data Sources**
    2. Select data source, click **Clone**
    3. Modify parameters as needed
    4. Save cloned data source
  - APIs/Tools: `clone_datasource`
  - Types: Configuration
  - Customization: Scripted cloning for similar sources

## Update Export Transfer Method

- **Components:**
  - Pre-requisite: Destination host accessible; SCP credentials
  - Execution Steps:
    1. Navigate to **Setup > Data Management > Export:Session Log**
    2. Select SCP transfer method
    3. Enter host, user, path, password
    4. Save configuration
  - APIs/Tools: `datamart_update_copy_file_info`
  - Types: Configuration

## Query Rewrite Definitions Management
Create, validate, and save new rewrite definitions via the UI form or API (`grdapi add_query_rewrite_mapping`, `grdapi update_query_rewrite_mapping`). Specify source, target, and condition fields.

## Special Handling for TRANSFORM Actions
After creating a definition, it appears in the **Query Rewrite Definitions** list for editing or deletion. Repeat the UI steps or use the same API calls to add multiple definitions.

## Verify Correlation Alerts
1. Get current polling interval: `grdapi get_anomaly_detection_settings`.
2. Set a short interval (e.g., 5 minutes): `grdapi update_anomaly_detection_settings polling_interval=5`.
3. Trigger an alert and confirm it appears on the alerts dashboard.

## Database Monitoring

### Configure Unit Utilization Schedule
Schedule frequency and timing for data processing in Unit Utilization.

## Security Operations

### Store AWS Credentials or UC Secrets
Add, configure, and save AWS or UC secrets using the secrets management interface.

## Pre-upgrade Verification for S-TAP

### Verify S-TAP Compatibility Before OS Upgrade
Check S-TAP support matrix, upgrade if necessary, and verify the upgrade using Guardium tools.

## Database Traffic Monitoring During S-TAP Upgrade

### Ensure Continuous Monitoring During S-TAP Upgrade
Monitor the S-TAP upgrade process and confirm continuous database monitoring throughout.

## Enable K-TAP After Installation

### Enable K-TAP on Linux-UNIX Systems
Verify kernel compatibility, enable K-TAP using the command `k tap enable`, and validate activation.

## Log Options
- Execute the certificate distribution command. Optionally add `showlog` to display transmission status (all, failed, successful).

## Retrieve Top Large Tables
- Run `support show db-top-tables`. Optionally supply a name pattern to filter specific tables.

## Reference Command Numbers
- Refer to the numbered command list and identify the command by its number for execution or documentation.

## Enable Outliers Detection
- Use the REST API endpoint `/api/outliers/enable` and include `aggregator_host_name` pointing to the central manager.

## Configure Client Web Certificates
- Navigate to **Client Web Certificates** configuration, upload or specify certificate files, and apply the configuration.

## Discover and Catalog Cloud Databases
- Open the **Cloud DB Service Accounts** pane, select the desired account, and initiate discovery and cataloging via GUI actions.

## Exclude Inspection Engines from Discovery
- Click **Filter** in discovery configuration, open **Filter Pane**, and add rules to ignore specific ports, protocols, or servers.

## Drill Down on Outliers Activity
- Access the **Outliers Table** interface, select an outlier record, and drill down on related activity, exceptions, and violations.

## Configure Database Name Transformation for Failed Logins
- Open **Policy Builder > Inspect Engine**, add a **TRANSFORM** action with `TRANSFORM_DB_NAME`, add condition `SERVER_IP = 10.0.0.* AND SERVER_PORT = 1521`, set `Transform DB Name = DB_PROD`, and save/deploy.

## Handle Ignore S-TAP Session Actions
- Navigate to **Monitor > Session Activity > Session Tracking**, select a session with **Session Watched by S-GATE = No**, choose **Ignore S-TAP Session**, and verify the change.

## Manage Session Quarantine Actions
- In **Monitor > Sessions**, locate sessions marked **Watched by S-GATE = Yes**, select session and choose **Quarantine**, verify termination and quarantine logs, and adjust policies as needed.

## Identify Sensitive Data Objects
- Review **Data Activity > Sensitive Data Objects**, identify objects requiring attention, document remediation steps, schedule reviews, and utilize Compliance Manager.

## Save Customized Dashboards
- (No specific steps provided; assume standard save action applies.)

## Dashboards

### Copy, Save, and Maintain Dashboards
- Copy a customized dashboard and name the new version.
- Save filter changes to preserve settings.
- Verify filters after saving.
- Schedule the new dashboard for periodic analysis.
- Develop naming conventions for saved dashboards.

## Audit Process Management

### Distribute Audit Report Results
- Ensure audit process completed and receiver configured.
- Initiate audit report in **Monitoring > Audit Reports**.
- Select **Continuous** distribution.
- Mark results as reviewed.
- Verify results appear in the receiver's queue.
- Document discrepancies and adjust parameters as needed.

## Outlier Detection

### Enhanced Monitoring for Privileged Users
- Configure outlier detection policy and identify privileged accounts.
- Add **User Entity** filter for privileged users.
- Define action thresholds for outliers.
- Save and activate the policy.
- Review anomaly reports and trigger alerts for high-risk activities.

## Vulnerability Assessment

### Run Vulnerability Assessment in Guardium
- Ensure DB2 database installed, running, and accessible.
- From **Assessments > Create New Assessment**, select **Vulnerability Assessment**.
- Choose target DB2 database and provide credentials.
- Configure assessment parameters and click **Save and Run**.
- Review the completed assessment report.

## User Management

### Create User Hierarchy
- Use `grdapi create_user_hierarchy userName=ADAMS parentUserName=SCOTT`.
- Verify hierarchy by querying user relationships.

## VA Scanner

### Execute VA Scanner Job
- Access job queue and run security assessment job.
- Send results to Guardium, poll for next job, and restart scanner as needed.

## CAS Installation

### Prepare Linux/UNIX for CAS Agent
- Download CAS .tgz file and verify system requirements.
- Run installation script and configure start-up and failover settings.

## CAS Configuration

### Deploy and Manage CAS Agent
- Configure S-TAP Control Change Auditing for failover and connection management.
- Reconfigure SAML after host/IP restoration.
- Monitor and address encrypted traffic issues.

## Load Balancing

### Configure Enterprise Load Balance
- Open Guardium UI and navigate to **Monitor > Enterprise Load Balance** or **Configure > Load Balance Configuration**.
- Adjust and apply settings as required.

## Venafi

### Install Certificates on Managed Units
- SSH into managed unit and run CLI command for Venafi certificate installation.

## S-TAP

### Verify S-TAP Startup
- (Documentation for this section is incomplete in the provided entries.)



## Quick Search Configuration

- Navigate to quick search configuration interface.
- Select **Add Groups to Quick Search**.
- Choose groups to add and save configuration.

---

## Datasource Configuration

### Configure MS SQL Server Datasource

1. Verify SQL Server is running and accessible.
2. Go to **Datasources > Add Datasource**.
3. Select connection type, input hostname, port, and authentication.
4. Test connection and save configuration.

---

## Policy Configuration

### Configure Fine-Grained Access Control

1. Go to **Setup > Access Control > FGAC**.
2. Define roles, object permissions, and assign to users.
3. Test with a restricted user account.

---

## User Management

### Organize User Hierarchy

- Use `grdapi create_user_hierarchy userName=ADAMS parentUserName=SCOTT` to add under SCOTT.
- Use `grdapi delete_user_hierarchy userName=ADAMS` to remove hierarchically.

---

## Access Control

### Configure Fine-Grained Access Control

- Same as above under Policy Configuration.

---

## S-TAP Configuration

### Verify API key Exists

1. Ensure API key `56f453cf-8bdf-4219-b5fe-60623b01f4e8` is available.
2. Confirm guardium group is created.
3. Proceed with S-TAP installation if verified.

## Pre-requisites and Execution Steps

- **Pre-requisites:** None specified, but target environment is Linux-UNIX
- **Execution Steps:**
  1. List and identify required plugin values
  2. Configure parameters within specified plugins
  3. Validate using system tools to ensure correct application

## Components and APIs

- **Components:** Configuration interfaces and plugin management
- **Types:** Configuration
- **Customization:** None applicable

## Security Workflows for Main Rules Configuration

### Components

- **Pre-requisites:** Cman.ora file access

### Execution Steps

  1. Hook main rules into appropriate security chains
  2. Configure connections and security actions as detailed in sample files
  3. Validate configurations for compliance and security standards

### APIs/Tools

- Security configuration files (e.g., cman.ora)

### Types

- Configuration

## Connections

## Configure MSSQL Connection

### Components

- **Pre-requisites:** Microsoft SQL Server and Windows operating system; JDBC driver available

### Execution Steps

  1. Collect SQL Server hostname, instance, port, and authentication details
  2. Navigate to **Connections > New Connection** and choose "SQL Server"
  3. Input hostname, port, database name, and select authentication method
  4. Specify the JDBC URL if needed, then click **Test Connection**
  5. Save the connection configuration

### APIs/Tools

- REST API endpoint `/connections`

### Types

- Configuration

## Kafka Connector Health Check Configuration

### Configure Kafka Connector Health Check Interval
- **Execution Steps:**
  1. Identify the connector name to configure
  2. Determine the desired `CRON` expression (e.g., `*/5 * * * *` for every 5 minutes)
  3. Update the connector configuration:
     - Send an HTTP `PUT` request to `http://localhost:8083/connectors/<connector-name>/config`
     - Include `"health.check.interval.seconds": <interval>` in the request body
  4. Verify the change:
     - Fetch the connector configuration with an HTTP `GET` request to `http://localhost:8083/connectors/<connector-name>/config`
     - Confirm `"health.check.interval.seconds"` reflects the new value
- **APIs/Tools:** `REST API` (`PUT`, `GET`)

## License Management

### Check Remaining Licenses Count
- **Components:**
  - Guardium system online  
  - Administrative access
- **Execution Steps:**
  1. Open the Administration Console  
  2. Navigate to **System > License**  
  3. Locate the **License Count** field  
  4. Record the value shown
- **APIs/Tools:** `licenses_remaining` command
- **Types:** Query  
- **User workflows:** Automation script to alert when licenses fall below threshold  

---

## System Customization

### Customize System Views to Include Healthy Systems
- **Components:**
  - Guardium administrator privileges  
  - Defined severity filters
- **Execution Steps:**
  1. Open the **Customize System Views** panel  
  2. Locate the **Include Healthy Systems** option  
  3. Check the box to override severity filters  
  4. Save the view configuration
- **APIs/Tools:** `guard_tap.ini` configuration in `[VIEW]` section
- **Types:** Configuration  
- **User workflows:** Create custom dashboards for senior management

---

## Certificate Management

### Skip Registry Certificate Installation on Cluster Nodes
- **Components:**
  - Cluster administrator credentials  
  - SSH access to cluster nodes
- **Execution Steps:**
  1. Generate a CSR on the manager node  
  2. Submit the CSR to the CA  
  3. Retrieve the signed certificate  
  4. Distribute the certificate manually to each node (skip registry installation)
- **APIs/Tools:** `cert_manager` CLI on manager; `scp` for distribution
- **Types:** Procedure

Configuration
- Types: Configuration
- Customization: User workflows: Script to push certificates to multiple nodes sequentially

---

Report Creation
- Build Reports with Defined Thresholds and Alerts
- Pre-requisites: Guardium system configured for VA (Vulnerability Assessment)
- Execution Steps:
  1. Navigate to VA Tests > Reports
  2. Select relevant security tests and create a New Report
  3. Set alert thresholds under Alerts tab
  4. Define logging behavior (syslog, CSV) under Export Settings
  5. Save and schedule the report
- APIs/Tools: grdapi create_report with ALERT parameters
- Types: Action | Configuration
- Customization: User workflows: Store reports in external repository for compliance audits

---

Database Management
- Identify Largest Tables Using SQL Analysis
- Pre-requisites: SQL client access to Guardium database
- Execution Steps:
  1. Connect to the Guardium database using your SQL client
  2. Run the analysis query to list tables by size
  3. Identify the largest tables from the result set
  4. Plan mitigation (archiving or optimization)
- APIs/Tools: CLI command db_tables_sizes
- Types: Query | Action

---

API Security
- Verify API Key Presence
- Pre-requisites: Access to Guardium API; configured API key
- Execution Steps:
  1. Log in to the Guardium web interface
  2. Navigate to Setup > API Keys
  3. Search for the API key by name or ID
  4. Confirm the key exists and is active
- APIs/Tools: guardapi list_api_keys
- Types: Query | Configuration
- Customization: User workflows: Audit script to validate API key status across environments

---

Data Source Management
- Reconnect Data Source Profile after Connection Failure
- Pre-requisites: Administrative access to Guardium; credentials for data source
- Execution Steps:
  1. Open System > Data Sources
  2. Locate the failed data source profile
  3. Click Reconnect and provide correct credentials
  4. Validate connection status
- APIs/Tools: guardapi add_datasource
- Types: Configuration | Action
- Customization: User workflows: Scheduled health check for all data source profiles

---

S-TAP Configuration
- Install S-TAP in a Zoned Solaris Environment
- Pre-requisites: Solaris OS configured with zones; K-TAP modules available
- Execution Steps:
  1. Identify the correct zone for S-TAP installation
  2. Install K-TAP using k-tap_install command within the targeted zone
  3. Verify installation with k-tap_status
- APIs/Tools: grdapi install_stap with zone parameter
- Types: Configuration | Action
- Customization: User workflows: Post-installation monitoring of S-TAP status

---

Guardium S-TAP Configuration in Zoned Environments
- Configure S-TAP for Global Zone Sharing
- Pre-requisites: Guardium S-TAP installed on the global zone; local zones configured to allow shared resources
- Execution Steps:
  1. Log into the global zone as a privileged user
  2. Enable database instance discovery in the S-TAP configuration
  3. Open the S-TAP configuration window to edit instance settings
  4. Specify the global zone as the host for shared resources
  5. Save and deactivate the S-TAP instance, then reactivate to apply changes
  6. Verify S-TAP operation across all local zones using the global zone's logs
- APIs/Tools: GuardCTL /usr/local/guardium/guard_stap/guardctl db_instance=db2inst1 deactivate
- Types: Configuration
- Customization: User workflows: Update instance names in guardctl commands for different databases (e.g., db_instance=oracle1 for Oracle instances)

---

Data Stream Management
- Configure Data Stream Sampling
- Pre-requisites: Data sources configured and accessible; streaming service operational
- Execution Steps:
  1. Open the streaming configuration interface
  2. Choose between random sampling (using rand() for SQL databases) or sequential sampling
  3. Specify sampling parameters, such as data size for sequential sampling
  4. Save the sampling configuration
  5. Verify streaming behavior and adjust as necessary
- APIs/Tools: Data streaming service UI or management API
- Types: Configuration
- Customization: User workflows: Switch between random and sequential sampling to optimize data analysis needs

---

Security Management
- Assign Additional Rights or Create Local Groups for Security Configuration
- Pre-requisites: Administrator access; clear security objectives defined
- Execution Steps:
  1. Identify the security configuration requirements
  2. Navigate to security configuration settings
  3. Assign additional rights or create necessary local groups
  4. Verify permissions with relevant personas
  5. Document the configuration changes
- APIs/Tools: System administration tools or scripts
- Types: Configuration
- Customization: User workflows: Define specific roles for backup operations on NAS systems

---

Incident Management
- View Policy Violation Reports
- Pre-requisites: Access to Incident Management section; permission to view policy reports
- Execution Steps:
  1. Log into the security management system
  2. Navigate to the Incident Management section
  3. Open the policy violation reports
  4. Analyze the specified columns and report details
  5. Take necessary compliance actions
- APIs/Tools: Incident Management UI or API
- Types: Action
- Customization: User workflows: Regularly review and act on policy violations

## Use Investigation Dashboard
Open dashboard, select datasets/tools, use quick search, enable full screen, interpret visualized data. APIs/tools: Dashboard interface. Types: Navigation. Customization: User workflows for ad-hoc analysis and regular monitoring.

## Report Configuration
Navigate audit system, open Send results ribbon, click New Receiver, configure and save receiver settings. APIs/tools: Audit system UI or API. Types: Configuration. Customization: User workflows to define audit configurations and roles.

## Compliance Management
Open compliance results, select result, choose Review or Review and Sign, identify receiver, confirm escalation, track follow-up. APIs/tools: Compliance system tools or API. Types: Action. Customization: User workflows to define escalation paths and roles.

## Report Distribution
Open Report Center, configure distributed report from existing non-distributed report, specify collectors or aggregators, define Guardium host name. APIs/tools: Report Center interface or API. Types: Configuration. Customization: User workflows to customize distribution based on analysis requirements.

## Security Assessment
Access assessment creation interface, create new assessment, add datasources, add tests/ checks, save configuration. APIs/tools: Security assessment tools or scripts. Types: Action. Customization: User workflows to tailor assessments based on security needs and roles.

## License Management
Open Purge configuration, adjust Data Archive and Data Export settings, save, monitor licenses. APIs/tools: System configuration tools or API. Types: Configuration. Customization: User workflows to manage data lifecycle using purge settings.

## Data Management
Log into Guardium CLI, run `show filesystem usage`, review output, run `support show large_files`, identify space-consuming files, determine removal candidates. APIs/tools: CLI commands `show filesystem usage`, `support show large_files`. Types: Action.

## Manage S-TAP Upgrade During Kernel Update
Verify OS minor upgrade, stop database instance if instrumented, halt running processes, retrieve latest S-TAP package, install updated version following vendor instructions. APIs/tools: Guardium Installation Manager (GIM), vendor scripts and packages. Types: Configuration.

## Convert Shell-installed S-TAP to GIM
Confirm S-TAP status, download BUNDLE-GIM, save to database server, follow conversion steps from vendor documentation. APIs/tools: CLI, vendor BUNDLE-GIM, Guardium Installation Manager. Types: Action.

## Create New Group
Navigate Group Builder, select Create new group, set type to OBJECTS, input name, define members, save. APIs/tools: Guardium Group Builder interface. Types: Navigation.

## Verify API Key Availability
Open Guardium Administration console, navigate to Integrations > API Keys, check existing keys or create new key, copy securely. APIs/tools: Guardium Admin UI, API key utility.

## Authentication and Authorization
### Generate and Use Encoded API Key for REST Calls
Encode Base64 API key pair in Authorization header of initial REST call. Store returned access token and include it in subsequent calls. Validate token expiration and request new tokens as needed.

## Configure for client web certificates

## Configure MS SQL Server Datasource
Gather SQL Server hostname, port, and authentication method. Add datasource via UI, enter details, test connection, and save. Clone datasource template for repeated setup.

## Data Management
### Import and Transfer Data
Verify source and destination host addresses, paths, and user credentials. Use secure transfer method, monitor progress, and verify integrity upon completion. Schedule regular transfers using cron jobs or task schedulers.

## 913. Configure Oracle A-TAP
Set up Oracle database monitoring with A‑TAP by installing S‑TAP, ensuring the Oracle database is accessible, and running `guardctl` with Oracle parameters. Add the Oracle database user to the guardium group and verify the A‑TAP connection via the Guardium UI. Test data collection functionality. Use `guardctl oracle add_user` and the Guardium UI.

## Guardium Data Protection Features
Enable real‑time alerting for sensitive data access, integrate with SIEM systems for centralized log management, configure reporting workflows for compliance reports, and access analytics tools for data‑usage pattern analysis. Use GuardAPI and SIEM connectors. Tailor alert thresholds and SIEM integration settings for organizational needs.

## 917. Ingress Configuration Annotation
Select a virtual switch for network connectivity, specify the path to a virtual hard disk (or create a new one), create and configure a new virtual disk if required, and apply hardware‑specific settings as noted in optional sections. Use hypervisor‑specific management tools.

## 921. Password Configuration Workflow
Upload the configuration file to the system, initiate password setup through the generate prompt option, and execute the dsmc command to verify successful password configuration. Use dsmc and password management tools. Adjust password complexity and management policies as needed.

## 922. Database Performance Tuning
Run `support show db-top-tables` to identify the largest database tables, analyze their usage, and optimize based on findings. Repeat the analysis regularly during low‑usage periods. Use GuardAPI and database management tools.

## 925. API Execution Configuration
Identify the target host (central manager or managed unit), configure the `api_target_host` parameter accordingly, execute API commands ensuring the hostname resolves correctly, and verify the execution results independently of IP‑mode configuration. Use GuardAPI and network configuration tools.

## Data Sources – Configure for client web certificates
1. Open **Configure > Web Server Certificates**.  
2. Click **Add** → **Client Web Certificate**.  
3. Upload the PEM‑formatted certificate and private key files.  
4. Provide a name and click **Save**.  
Use `load_clean_chain_api` (CLI) or `PUT /api/ssl/client_certificate` (REST). Clone an existing configuration to pre‑populate fields for repeated setups.

## Risk Management – Add a Dynamic Auditing policy
1. Go to **System > Risk Management > Dynamic Auditing**.  
2. Click **Add** to create a new policy.  
3. Define detection criteria (privileged user, sensitive objects, etc.).  
4. Choose actions—log, alert, block—and click **Save**.  
Use `add_dynamic_audit_policy` (grdapi).

## Compliance Automation – Add a receiver to a compliance workflow automation
1. Open the workflow details page.  
2. Click the **Receivers** tab.  
3. Click **Add**, select the receiver type (email, LDAP user, etc.).  
4. Fill the required fields and click **Save**.

## Datasource Management

### Create Datasource Group via REST API
- **Execution Steps:** Send a POST request with `appTypeCriteria` and `datasourceGroupNameString` to create a group.
- **APIs/Tools:** REST API
- **Types:** Configuration

## Monitoring

### Enable Query Rewrite for Monitoring
- **Execution Steps:** Activate query rewrite settings and set up monitoring to capture query rewrite events.
- **Types:** Configuration

## Privilege Management

### De‑enroll a Database After an Upgrade
- **Execution Steps:** 
  1. `guardctl db_instance=db2inst1 deactivate`
  2. Verify with `list_deenrolled_databases` (CLI).
  3. Re‑enable monitoring if needed.
- **APIs/Tools:** `deactivate_db_instance` (guardctl), `list_deenrolled_databases` (grdapi)

## Access Control

### Configure Fine‑Grained Access Control
- **Execution Steps:** 
  1. Navigate to **Setup > Access Control > FGAC**.
  2. Define roles and object‑level permissions.
  3. Assign roles to users.
  4. Test with a restricted account.
- **APIs/Tools:** grdapi set_access_rule

## Setup

### Restore Shared Secret Keys
- **Execution Steps:** Run `restore keys file` via the aggregator, specifying `user HOST:/path/filename`.
- **APIs/Tools:** N/A

## Virtualization

### VM Installation for Guardium
- **Execution Steps:** 
  1. Create VM with required specs.
  2. Mount Guardium installation image.
  3. Follow on‑screen prompts.
  4. Complete post‑install configuration.
- **APIs/Tools:** N/A

## Network Configuration

### Optional Annotations for Ingress
- **Execution Steps:** Define annotations, apply them to the ingress YAML, deploy, and validate.
- **APIs/Tools:** Kubernetes API

equisites:** External S-TAP deployed; intermediate certificates stored in Guardium

- **Execution Steps:**
  1. Open **External S-TAP > Certificate Management**
  2. Select the certificate to verify
  3. Click **Verify Certificate** and review the result

## External S-TAP Certificate Verification

- **Pre-requisites:** Access to External S-TAP management interface; certificate files available
  - **Steps:** Log in to the External S-TAP management console > Administration > Security > Certificate Management > Verify Certificate > upload certificate file > set verification options > submit > review results
  - **Tools:** GuardAPI: `grdapi verify_stap_cert`; GUI: Administration > Security > Certificate Management

## Database Configuration

### Configure Oracle Data Source

- **Pre-requisites:** Oracle database instance accessible; JDBC driver installed; network connectivity verified
  - **Steps:** Gather hostname, port, service name, credentials > Datasources > Add Datasource > select Oracle > enter details > test connection > save
  - **Tools:** GuardAPI: `add_datasource`

## Load Balancer Management

Retrieve Current Load Balancer Map
- Query the load balancer map with `get_kafka_clusters`.
- Optionally filter by managed unit, S-TAP, or IP address.

## Data Correlation and Integration

Correlate Data Across Tables
- Identify primary and foreign keys between tables.
- Define join conditions and use SQL JOIN clauses.
- Validate the integrated dataset for accuracy.

## Data Management

Import and Map External Datasets
- Clean and normalize the external dataset.
- Map fields to corresponding database columns.
- Import data using DB tools or scripts.
- Verify successful import and data integrity.

## S-TAP Configuration

Verify API Key Exists
- Open **Manage > Activity Monitoring > S-TAP Control**.
- Click **Refresh** to update configuration.
- Confirm API key `c9eb73ab-277c-450d-ac94-ef24ec8baa46` status is **Active**.
- Record errors and restart upgrade if needed.

Configure S-TAP Monitoring Mechanisms
- Review the S-TAP Monitoring Mechanisms Support Matrix.
- Determine required monitoring capabilities.
- Select appropriate configuration from the matrix.
- Follow installation guide for chosen mechanism.

## License Management

### Restore Licenses from Backup Across Multiple Days
- **Pre-requisites:** Backup containing the desired license period.
- **Execution Steps:**  
  1. Identify the first day with available license data.  
  2. Restore that day's data.  
  3. Sequentially restore each subsequent day until the target date.  
  4. Verify restored counts via Guardium UI or API.  
- **APIs/Tools:** Guardium restore utilities.

## Patch Management
### Install Guardium Patches
- Navigate **System > Patch Management**, select **Install Patch**, browse to patch file(s), and initiate installation.

## API Management
### Delete CAS Host
- Call `delete_cas_host` API with hostName and osType.

## Web Certificate Configuration
### Configure Client Web Certificates
- Upload and configure certificates in **Setup > Web Certificates**, enable DoS monitoring and certificate deletion actions.

## Exception Management
### Create and Edit an Exception Group with Regex Matching
- Navigate **Setup > Riskware > Exception Groups**, click **New**, enter regex pattern, configure assessment and datasource scope.

## Guardium S-TAP Configuration
### Configure S-TAP Agent Parameters
- Access **Setup > Agents > S-TAP Configuration**, modify parameters, run `guardctl` to deactivate and re-activate instance.

## System Health and Monitoring
### Monitor and Resolve Alert Warnings
- Review alerts, check origin and parameters, adjust thresholds, validate changes in system logs.

## Data Management Operations
### Prepare for OS Upgrade - DB2 Instance Deactivation
- Run `guardctl db_instance=db2inst1 deactivate` to deactivate DB2 instance before OS upgrade.

### Delete Certificates by Number
- Open certificate management, enter certificate number(s), confirm deletion.

## Route 53 Failover Policy Creation
### Route 53 Failover Policy Creation
- Configure primary domain with CloudWatch alarm logic, add failover settings, save policy.

## File Path Monitoring Parameters
### File Path Monitoring Parameters
- Define `filePathGroup` in FAM configuration, set `includeSubdirectories`, save and activate monitoring.

## Enable Outliers Detection Incrementally
### Enable Outliers Detection Incrementally
- Enable outliers detection on aggregator, validate settings, replicate configuration across aggregators.

## Rule-Base

## License Management

### Manage License Inventory
- Navigate to **System Management > License Management**.
- Check the *Remaining Licenses* value against current usage.
- De-provision old collectors if capacity is approaching.
- Click **Update** to refresh the count.

## Guardium API Interactions

### Use Access Tokens to Call GuardAPI Functions
- Authenticate the REST client to obtain a bearer token.
- Include `Authorization: Bearer <token>` header in requests.
- Construct request payload per GuardAPI function requirements.
- Send request to GuardAPI endpoint and handle the response.

## 1094. CPU

### Datamart Extraction Procedure
1. Enable required data marts.
2. Point data mart outputs to the target server.
3. Use `grdapi datamart_update_copy_file_info` with:
   - Destination server name
   - Password
   - Path
   - User

## Access Control

- Configure fine-grained access control  
  - Requires administrator role and defined security policy  
  - Define roles, object permissions, assign users, then test  
  - API: `set_access_rule`

## Datasource Configuration

- Configure MS SQL Server datasource  
  - Needs SQL Server running and network connectivity  
  - Provide hostname, port, authentication details  
  - Test connection before saving  

## Event Management

- Manage health events in system views  
  - Create critical/high severity events  
  - Set timestamps, retention, track utilization data  
  - Purge older events based on policy  

## License Management

- View license remaining count  
  - Navigate to Administration > System Settings > License Info  
  - Review value next to "Number sign"  

## Central Management - Patching

- Configure Guardium Central Manager for patching  
  - Upload `.tgz` patch file to Central Manager  
  - Select units; set optional schedule  
  - Monitor status via Patch Management view  

## Guardium Workflow Reference

- Configure Guardium Big Data Intelligence  
  - Storage datasource created via create_datasource or GUI  
  - Application type set to *Big Data Intelligence*  
  - Complete initial workflow to enable feature

## Threat Analytics

### Configure Exclude List Items
- **Pre-requisites:** Access to Active Threat Analytics configuration
- **Steps:** 
  1. Navigate to Threat Analytics > Add Exclude List Item
  2. Define period and view case details
  3. Save the configuration
- **Tools:** No API available

## Security Policies

### Define and Save Security Policies
- **Pre-requisites:** Policy creation window open
- **Steps:** 
  1. Define a rule and click OK to return to the Rules ribbon
  2. Create, clone, or edit additional rules as needed
  3. Click OK to save the policy and return to the Security Policies table

## Data Security

### Specify Exact Phrase Matching with Case Sensitivity
- **Pre-requisites:** Knowledge of field name and value
- **Steps:** 
  1. Use `"field name=value"` for exact phrase matching
  2. Ensure case sensitivity as required

## VMware Tools Installation
Install VMware Tools on a virtual machine by mounting the ISO, extracting the files, running the installer, and rebooting.

## High-Availability Network Interface Configuration
Enable or disable high-availability mode on a NIC using `ifconfig` with the `ha` option and specifying the mode.

## Azure SQL/Databases Resource Identification
Locate the Azure SQL resource ID in the Overview pane of the Azure portal.

## Policy Creation and Management
Define and store a Network Attached Storage policy by creating a new policy, configuring rules, and applying it to NAS devices.

## Azure Custom Security Query
Build a custom security query in Guardium by defining parameters, filters, and conditions in the Policy Builder.

## Oracle Query Development
Develop Oracle queries in SQL Developer by connecting to the database, creating/modifying queries, and executing them.

## Unit Utilization Monitoring
Enable unit utilization monitoring by modifying the schedule in Guardium's Manage UI.

## Data Loader Driver Behavior
When no open source driver is available for a data source import, Guardium automatically switches to the built-in DataDirect driver.

## External Ticketing Integration
Configure an external ticketing system in Guardium by enabling debug logging if the test connection fails.

roductory_maintenance/api_license_status`
- **Types:** Configuration

## Database-Specific Workflows
### Configure Database Name Handling in MS SQL
Check if the datasource configuration specifies a database name. If blank, ensure all databases are mounted and the data upload job correctly loops through each. Document findings and adjust configurations as needed.

---

## Installation and Setup
### Create Symbolic Link for Teradata Guardium Exit Library
Execute `ln -fs /usr/lib/libguard_teradata_exit_64.so /opt/teradata/tdat/tgtw/site/libtgtwmonitoring.so`. Verify the link with `ls -l /opt/teradata/tdat/tgtw/site/libtgtwmonitoring.so`.

---

## Certificate Management
### Add Client Web Certificates to Guardium UI
Open the certificate management section in the Guardium UI, upload and validate client certificates, then test connectivity to confirm successful application.

---

## Access Control
### Configure Fine-Grained Access Control
Navigate to **Setup > Access Control > FGAC**, define roles and permissions, assign roles to user accounts, and test access with a restricted user account.

---

## Datasource Configuration
### Configure MS SQL Server Datasource
Gather connection details, navigate to **Datasources > Add Datasource**, select connection type, enter details, test connection, and save configuration.

---

## Entities
### Manage Database Privileges and Entitlements
Log into Guardium, go to **Entitlements > Database Privileges**, select and apply privileges to roles or users.

---

## Knowledge
### Use Session Inference Feature for Inactive Sessions
Enable and set the inactivity timeout in **Monitor > Sessions > Session Inference**, apply to relevant policies or groups, and monitor for inactive sessions.

---

## Navigation
### Verify API Key Exists
Navigate to **Setup > Security > API Keys**, search for the specific API key, validate its status and permissions, and optionally regenerate or revoke it.

---

## Workflows
### Set Up DHCP Server with Reservations
Access the DHCP management console, create IP allocation scope options, define DHCP reservations for specific MAC addresses, and activate the DHCP service.

---

## Workflows
### Start S-TAP Monitoring on Specific Database Servers
Log into the Guardium UI, navigate to **Manage > Module Installation > Set up by Client**, select clients or groups, and initiate the S-TAP start process.

---

## Audit Configuration
### Configure Audit Process Receivers for Suspected Malicious Stored Procedures
Navigate to **Report & Export > Report Builder**, select the stored procedure analysis report template, configure receivers in the **Options** tab, and enable audit process with customized settings.

---

## Workflows
### Configure Db2 Exit in Db2
Update the database manager configuration to include the Db2 exit.

## Guardium Alert Management

### Deactivate Excessive Alerts in Anomaly Detection
- **Components:**
  - **Pre-requisites:** Access to the Guardium UI with admin rights; anomaly detection alerts configured
  - **Execution Steps:**
    1. Open the **Guardium UI** on the central manager.
    2. Navigate to **Anomaly Detection** → **Alerts**.
    3. Identify the excessive alerts displayed.
    4. For each alert, select **Deactivate** from the action menu.
    5. Confirm the deactivation to stop further notifications.
  - **APIs/Tools:** Guardium UI, no external scripts required
- **Types:** Action

## Manage Guardium Anomaly Alerts

- **Prerequisites:** Guardium system configured; access to Anomaly Detection settings
- **Steps:**
  - Log into the Guardium UI with appropriate privileges
  - Navigate to **Monitor > Anomaly Detection**
  - Review active alerts and identify noisy ones
  - Deactivate suspect alerts individually using the **Deactivate** button
  - Wait for the system's polling interval to complete
  - Check resolution of error messages related to deactivated alerts
  - Continue until alerts are manageable and genuine threats are visible
- **API:** `grdapi set_anomaly_detection_state`

---

## Connect Physical Guardium Appliance

- **Prerequisites:** Guardium appliance delivered; rack space prepared
- **Steps:**
  - Slide the appliance into the designated rack slot
  - Connect the power cable to a grounded, uninterruptible power source
  - Attach the network cable to the appliance's primary port
  - Power on the appliance and verify LED indicators for power and network connectivity
  - Follow on-screen instructions or documentation for initial configuration

---

## Generate API Call for Multiple Rows

- **Prerequisites:** Guardium UI access with API permissions
- **Steps:**
  - Open the **API Call Form** from the Guardium navigation menu
  - Specify parameters for multiple rows in the provided interface
  - Click **Add API Mapping** under **Actions** to create the batch API call
  - Verify the generated script for correctness and completeness
  - Submit the API call and monitor execution results

---

## Set Up Database Monitoring Parameters

- **Prerequisites:** Administrative access; database details (IPs, ports, usernames)
- **Steps:**
  - Open the Guardium UI and go to **Configure > Database Instances**
  - Click **Add New Database Instance** and select the appropriate protocol
  - Enter connection specifics: IP address, port, and authentication details
  - Configure user roles and security settings as per organizational policies
  - Enable discovery settings if automatic monitoring is required
  - Save configuration and initiate a connectivity test

---

## Create Hierarchy and API Mappings

- **Prerequisites:** Guardium system access; defined user hierarchy
- **Steps:**
  - In the **Define Hierarchy** mode, create `userName` and `parentUserName` entries
  - Execute `grdapi create_user_hierarchy userName=jkoopmann parentUserName=scott`
  - Navigate to the **Reports** section
  - Under **Actions**, click **Add API Mapping** to create new mappings
  - Review and test the newly created API call forms for accuracy

---

## Manage Session-Level Policies

- **Prerequisites:** Policy design permissions; understanding of session scenarios
- **Steps:**
  - Navigate to **SecureSphere > Policies > Session-Level Policies**
  - Define rule actions, request types, and search prefixes for specific scenarios
  - Configure session-level policies to address insufficient privileges
  - Set attachment criteria for sessions based on server IP and port
  - Test the policy in a controlled environment before deployment

---

## Enable Risk Spotter Functionality

- **Prerequisites:** Guardium system access; administrative rights
- **Steps:**
  - Use the REST API endpoint `/restAPI/riskSpotter` to enable Risk Spotter
  - Alternatively, run `grdapi enable_risk_spotter` on the central manager
  - Confirm Risk Spotter is active across managed units
  - Monitor risk indicators and adjust policies as needed

---

## Configure Audit Logging Options

- **Prerequisites:** Administrative access; logging policy defined
- **Steps:**
  - Go to **Monitor > Audit Logs**
  - Define logging parameters: log level, retention policies, and storage locations
  - Configure options for generating reports from audit logs
  - Schedule regular audits and review processes
  - Test log generation and review sample reports for completeness

---

## Investigate Pods Stuck in CrashLoopBackOff

- **Prerequisites:** Access to Kubernetes cluster; permission to view pod logs
- **Steps:**
  - Identify affected pods using `kubectl get pods`
  - Retrieve logs from the failing pods with `kubectl logs <pod_name>`
  - Check for error messages indicating unavailable assessment jobs
  - Verify assessment job configurations and resources



- **Components:** Guardium S-TAP service
- **Execution Steps:**
  1. Run `utap stop` to stop the service
  2. Confirm the service status with `utap status` to ensure it is inactive

## Kubernetes Cluster Management

### Check Current Kubernetes Context
Run `kubectl config current-context` to list the active context.

### Monitor Pod Resource Usage
Execute `kubectl top pod --namespace va-scanner` to review CPU and memory usage for pods in the `va-scanner` namespace.

### Extract Helm Chart Archive
Use `tar -xzf chart-archive.tgz` to extract the compressed Helm chart file, then change to the extracted directory.

## IBM Cloud Pak for Data Operations

### Download CASE Asset
Set `CASE_NAME` and `CASE_VERSION`, then run `oc ibm-pak get $CASE_NAME --version $CASE_VERSION` to download the CASE asset.

## Remote Server Administration

### SSH to GDP Server
Connect with `ssh user@your-gdp-server` using the appropriate credentials, then authenticate via password or key.

## Helm Release Management

### List Helm Release Revisions
Run `helm history va-scanner` to review the revision history for the `va-scanner` release.

### Rollback Helm Release
Identify the desired revision number, then execute `helm rollback va-scanner <revision-number>` to revert to that version.

### Navigate to Helm Chart Directory
Change to the Helm chart directory with `cd va-scanner-helm-v1.0.0` after extracting the archive, to access the chart files.

## IBM Cloud Pak Asset Preparation

### Set CASE Asset Name
Define `CASE_NAME` and `CASE_VERSION` variables, then use `oc ibm-pak get $CASE_NAME --version $CASE_VERSION` to initiate the download process.

## Log Management

### Display Log Directory List
Run `support execute files` to list the contents of the log directory on the Guardium appliance.

## Network Configuration

### Retrieve ens32 MAC Address
Log in to the Guardium appliance and execute `support execute info` to display system details, including the `ens32` MAC address.

## Helm Operations

### Navigate to Helm Chart Directory
Access the Helm chart for the `va-scanner` component by changing to `src/va-scanner` after navigating to the Guardium installation directory.

**REST API `list_ranger_staps`**

- **Types:** Action

## IBM Guardium Configuration

### Set API Target Host Parameter
- Determine target host type (IPv4, IPv6, hostname)
- Use `api_target_host` in API calls to specify target
- Ensure IPv6 registration aligns with IP mode
- Optional: Use hostname regardless of IP mode
- **APIs/Tools:** GuardAPI, REST API (PUT)

### Remove Datasource from Entitlement Optimization
- Identify datasource name
- Execute API call to remove from optimization

## GuardAPI Command Execution and Targeting

### Configuring and Executing GuardAPI Commands
- Verify API enablement, connectivity, roles, and `api_target_host`
- Central manager execution: `api_target_host=central_manager_hostname`
- Managed unit execution: `api_target_host=managed_unit_ip_or_hostname`
- Append GuardAPI command (e.g., `grdapi list_cas_host_instances host_name=example.com`)
- Execute via CLI, API client, or REST
- **APIs/Tools:** grdapi, REST API, CLI

## Auditing CAS Environment

### Listing CAS Host Instances
- Execute `grdapi list_cas_host_instances`
- Parse output for datasource attributes
- Filter results as needed
- Export CSV for archival or analysis

## Outliers Detection Reset

### Reset Outliers Detection to Factory Settings
- **Steps:**
  1. Run `grdapi set_outliers_detection_to_factory_settings`. 
  2. Confirm the reset completed in the success message. 
  3. Verify default parameters with `grdapi show_outliers_settings`. 
  4. Log the reset action and timestamp in system maintenance records.
- **API/Tool:** `grdapi set_outliers_detection_to_factory_settings`
- **Type:** Action

---

## Reports

### Schedule Report Distribution
- Define frequency and recipients, then configure attachment format and test.

## Search

### Create Classification Search
- Select classification filters, define criteria, save, and export results.

## System

### Update Password Policies
- Adjust complexity settings, enforce changes, and verify with test user.

## Unified Discovery and Classification

### Add Oracle Data Source
- Collect credentials, configure data source, test connection, and save.

## Guardium Data Protection

### Configure MS SQL Server Data Source
- Gather connection details, test, and save data source settings.

## Access Control

### Update Ranger Service
- Identify cluster, execute API with configuration, and verify success.

## API Integration

### Control Logging Parameters
- Prepare JSON payload, invoke REST API, and confirm configuration update.

Access Control

### Configure Fine-Grained Access Control
- Navigate to Setup > Access Control > FGAC, define roles and object-level permissions, assign to users, and test

Data Collection

### Exclude Table from Data Collection
- Verify capture rules, run store capture exclude command, verify exclusion, and document

Datasource Configuration

### Configure MS SQL Server Datasource
- Gather connection details, add datasource in UI, test connection, save configuration

Data Protection Standards and Regulatory Compliance

### Workflow: Establish Data Protection Standards and Meet Regulatory Obligations
- Assess regulatory landscape, conduct data mapping, develop control framework, implement controls, develop data protection policies, establish monitoring and reporting mechanisms, conduct training and awareness programs, review and update standards, maintain documentation and records

## Data Protection Program

- Define data protection standards based on regulatory requirements
- Implement technical controls such as encryption, access controls, and monitoring
- Develop policies and procedures for data handling, retention, and breach response
- Train personnel on compliance and data protection best practices
- Conduct regular audits and assessments to ensure compliance
- Update data protection standards as regulations evolve

## List Available Policies

- **Pre-requisites:** Access to the Guardium appliance; appropriate privileges to run GuardAPI commands
- **Execution Steps:**
  1. Log into the Guardium CLI or access the REST API interface
  2. Execute the command `list_policy` to retrieve available policy names
  3. Review the listed policies and identify the required policy
- **APIs/Tools:** GuardAPI, REST API
- **Types:** Action

## Set Up Azure Account Integration

- **Pre-requisites:** Azure subscription details; user credentials with necessary permissions
- **Execution Steps:**
  1. Navigate to **Unified Discovery** and select **Cloud Services**
  2. Enter Azure credentials and configure connection settings
  3. Validate connection and save configuration
- **APIs/Tools:** None
- **Types:** Configuration

## Execute API with Target Host Parameter

- **Pre-requisites:** Understanding of Guardium's API structure; network configuration allowing target host access
- **Execution Steps:**
  1. Determine the API endpoint and parameters required for the operation
  2. Include `api_target_host` parameter to specify the execution host
  3. Run the API command
- **APIs/Tools:** Any Guardium API call requiring `api_target_host`
- **Types:** Configuration

## Display Specific Data Source Definition

- **Pre-requisites:** Knowledge of the data source name; access to Guardium CLI or API
- **Execution Steps:**
  1. Open Guardium CLI or access REST API
  2. Use `list_datasource_by_name` with the specific name parameter
  3. Validate the output displays the required data source details
- **APIs/Tools:** GuardAPI (`list_datasource_by_name`), REST API
- **Types:** Action

## Configuring MS SQL Server Datasource

- **Pre-requisites:** SQL Server installed and running; network connectivity verified
- **Execution Steps:**
  1. Gather SQL Server hostname, port, and authentication method
  2. Navigate to Datasources > Add Datasource and select connection type
  3. Enter connection details and click Test Connection
  4. Save the datasource configuration
- **APIs/Tools:** GuardAPI, grdapi add_datasource
- **Types:** Configuration
- **Customization:** Clone datasource template for faster repeated setup

## Removing Domains from Universal Connector

- **Pre-requisites:** Administrator access; Universal Connector installed
- **Execution Steps:**
  1. Execute the REST API POST request to /v2/allowed-domains endpoint
  2. Provide the domain parameter listing domains to remove
  3. Verify removal through the Universal Connector dashboard
- **APIs/Tools:** REST API
- **Types:** Action
- **Customization:** N/A

## Configuring Fine-Grained Access Control (FGAC)

- **Pre-requisites:** Administrator role assigned; security policy defined
- **Execution Steps:**
  1. Navigate to Setup > Access Control > FGAC
  2. Define roles and object-level permissions
  3. Assign roles to user accounts
  4. Test access with a restricted user account
- **APIs/Tools:** grdapi set_access_rule
- **Types:** Configuration

## Managing API Execution Targets

- **Pre-requisites:** Access to Guardium system; defined managed units
- **Execution Steps:**
  1. Identify target host(s): managed units, central manager, or groups
  2. Use the api_target_host parameter in relevant API commands
  3. Specifying group names or IP addresses as necessary
- **APIs/Tools:** N/A
- **Types:** Configuration
- **Customization:** N/A

## Setting up Kerberos Authentication

- **Pre-requisites:** Kerberos key distribution center (KDC) configured
- **Execution Steps:**
  1. Modify /etc/krb5.conf with realm and domain information
  2. Update /etc/hosts with KDC and admin server entries
  3. Restart Guardium services to apply Kerberos settings
- **APIs/Tools:** N/A
- **Types:** Configuration
- **Customization:** N/A

## Executing Database Queries

- **Pre-requisites:** Database credentials; permissions to execute SELECT statements
- **Execution Steps:**
  1. Connect to the target database using a client tool
  2. Execute an SQL SELECT statement to retrieve data
  3. Analyze the result set as needed for reporting or debugging
- **APIs/Tools:** Database client tools (e.g., SQL Server Management Studio)
- **Types:** Action
- **Customization:** N/A

## Features

### Add Cloud Account to Unified Discovery and Classification
- **Components:** Cloud Accounts page, Create New Account form
- **Execution Steps:** Navigate to Cloud Accounts, click Create New Account, select provider, enter credentials, save.
- **Types:** Action

## Configuration

### Set Up HDFS Monitoring with update_ranger_hdfs_config
- **Components:** HDFS environment, JVM library path, update_ranger_hdfs_config API
- **Execution Steps:** Determine JVM library path, access update_ranger_hdfs_config, set ldLibraryPath parameter, configure S-TAP connections, execute API.
- **Types:** Configuration

## Navigation

### Retrieve Valid API Target Hosts for Execution
- **Components:** API documentation, managed units, central manager IPs, IP mode
- **Execution Steps:** Review docs for `api_target_host`, list valid hosts, ensure IP mode matches, document examples.
- **Types:** Navigation

## License Installation

### Install Guardium License
- **Components:** Guardium Installation Manager, license file
- **Execution Steps:** Log into Guardium appliance, start GIM, select Install License, provide license file path, confirm installation.
- **Types:** Action

## Data Management

### Manage Datasources With api_target_host
- **Pre-requisites:** Guardium system with API enabled and network access to the target host.
- **Execution Steps:**
  1. Determine the hostname or IP address of the target host.
  2. Set `api_target_host` to the target host value (e.g., `10.0.1.123` or `central.manager.com`).
  3. Invoke the desired API (e.g., `store_sql_credentials`) with `api_target_host` specified.
  4. Execute the API command using `grdapi` or GuardAPI syntax.

## Security Administration

### View Sensitive Object Access Reports
- **Pre-requisites:** Sensitive Objects Tracking policy enabled and data collected.
- **Execution Steps:**
  1. Navigate to **Reports > Sensitive Objects Tracking**.
  2. Select a report such as **Objects accessed with sensitive data**.
  3. Apply filters for time period, sensitivity level, or specific objects.
  4. Review the report details including access counts, client IP, and source program.
- **APIs/Tools:** `grdapi generate_report report_name="Objects accessed with sensitive data"`

## Compliance Management

### Review FBAC Policies With filter_by_group
- **Pre-requisites:** FBAC policy created and relevant groups defined.
- **Execution Steps:**
  1. Go to **Setup > Access Control > FBAC**.
  2. Click **Filter by Group** and select the target group.
  3. Review the applied rules and object permissions for the group.
  4. Export or print the filtered FBAC view as needed.
- **APIs/Tools:** `grdapi export_access_rules filter_group="Finance"`

## Data Protection

### Pause or Resume Data Encryption Jobs
- **Pre-requisites:** Encryption keys configured and jobs defined.
- **Execution Steps:**
  1. Run `pause_or_resume_job` with `--preview` to see which jobs will be affected.
  2. Execute `pause_or_resume_job` with the desired `scenarioNamePattern` and set `preview=false` to apply.
  3. Verify job status using the **Data Encryption Jobs** view.
- **APIs/Tools:** `grdapi pause_or_resume_job scenarioNamePattern="MonthlyEncryption" preview=true`

## System Operations

### List Guardium Templates With list_cas_templates
- **Pre-requisites:** Guardium Central Manager configured and templates created.
- **Execution Steps:**
  1. Use `list_cas_templates` with optional parameters to filter templates.

## Guardium Data Management

### List and Export CAS Templates
- **Components:** Accessible Guardium system; appropriate user permissions
- **Execution:**  
  ```bash
  grdapi list_cas_templates template_type="access"
  ```
- **Purpose:** Retrieve templates and associated parameters for documentation or processing.  
- **Environment:** Any Guardium deployment supporting CAS templates.  

## Vulnerability Assessment

### View Chart Descriptions on Dashboards
- **Components:** Executed vulnerability assessment scans; configured dashboard
- **Execution:**  
  1. Open the relevant dashboard in the **Vulnerability Assessment** module.  
  2. Click the **?** icon on any chart to display its description.  
  3. Record vulnerabilities, risk scores, and remediation steps.  
  4. Optionally export chart data via:  
     ```bash
     grdapi export_assessment_data chart_id=12345
     ```
- **Purpose:** Provide detailed contextual information for charted findings.  

## Guardium API Target Host Configuration

### Set API Target Host for Distributed Execution
- **Components:** Guardium central manager and managed units; verified network connectivity
- **Execution:**  
  1. Determine the target host value: `all`, `centralManager`, or specific IP/hostname.  
  2. Execute an API command specifying `api_target_host`. Example:  
     ```bash
     grdapi my_api_command api_target_host="192.168.1.50"
     ```  
  3. Confirm successful execution on the designated host(s).  
- **Purpose:** Direct API operations to specific Guardium components.  

## Unscheduled DataMart

### Unschedule a DataMart Object
- **Components:** Known Datamart name; Guardium API credentials; configured `api_target_host`
- **Execution:**  
  ```bash
  grdapi unschedule_datamart atamart_name="MyDataMart"
  ```
- **Purpose:** Remove a DataMart from scheduled processing.