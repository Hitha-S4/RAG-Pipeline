# IBM Guardium Data Protection — KEYWORDS

**Category:** keywords  |  **Layer:** 3 (distilled)  |  **Source:** gdp-12.x-documentation

---

**Abac (Attribute-Based Access Control):** Rights granted based on user attributes rather than fixed roles.
**A-TAP (Application TAP):** Kernel-level agent that intercepts database calls made by local applications directly on the server.
**Aggregator:** Guardium appliance that consolidates activity data from multiple Collectors for enterprise-wide reporting.
**Alert Grouping:** Time window in seconds for combining similar alerts into a single notification.
**API Key:** Credential that authenticates programmatic requests to Guardium services.
**ArcSight:** SIEM platform that can ingest Guardium security alerts.
**Audit Process:** Guardium service that analyses S-TAP data and stores results in the activity repository.
**Audit Workflow:** Automated sequence of enforcement tasks triggered by policy violations.
**Bluejay:** Guardium component that guarantees data integrity and consistency across all appliance nodes in a HA cluster.
**Bunker Device:** IBM-provided physical device for secure backup and restoration of critical Guardium configuration data.
**Bunker Gateway:** Secure channel that allows Guardium appliances to upload backup data to a Bunker Device.
**BYOD:** Policy framework for monitoring personal devices that access corporate databases.
**CAS (Change Audit System):** Guardium module that detects and records changes to database schemas, stored procedures, and object configurations.
**CASPAS:** IBM Guardium Central Assessment, Protection and Security Service for automated compliance reporting.
**Central Manager:** Guardium component that coordinates audit activities and manages all collectors and aggregators across an enterprise deployment.
**CAS Template Items:** Specific audit checks within the Change Audit System configurable with runtime parameters.
**Client Lockout Count:** Maximum failed authentication attempts before a client account is locked.
**Client Session Timeout:** Interval after which an inactive client session is automatically terminated.
**Collector:** Guardium appliance that receives, processes, and stores database activity data forwarded by S-TAP agents.
**Command History:** Record of all CLI and UI actions retained for forensic review.
**Connection Pool:** Set of shared database connections monitored by Guardium.
**Control Policy:** Real-time security enforcement rules evaluated against every captured database request.
**CSV:** Comma-Separated Values format used by Guardium for exporting policy violations, audit data, and reports.
**Custom Property:** User-defined attribute on a data source or object enabling policy grouping and extended reporting.
**Data-Masking:** Guardium feature that dynamically obscures sensitive data values returned to applications in real time.
**Data Level Security (DLS):** Controls data visibility based on user roles so users only access authorised data.
**Data Privacy:** Guardium capability that masks credentials and sensitive values in database traffic.
**DB-User:** Application database account used for connections; captured in activity logs.
**Default Purge Batch Size:** Pre-configured number of records deleted per purge iteration, modifiable via API.
**Discover:** Automated process that scans the network to identify and register database instances.
**DNS Domain:** Domain name used for DNS queries affecting Guardium network operations.
**FAM (File Activity Monitoring):** Guardium module that monitors and records access to unstructured data files on NAS, SharePoint, and similar storage.
**Failover:** Mechanism that automatically switches Guardium processing to standby components during a failure.
**FGAC (Fine-Grained Access Control):** Guardium capability for object-level permission policies targeting specific tables, views, or stored procedures.
**G-CENT:** Guardium central management console designed for large-scale deployments.
**GDPR:** EU personal-data regulation; Guardium supports compliance via data discovery, masking, and audit trails.
**GIM (Guardium Installation Manager):** Centralised tool for remotely deploying, upgrading, and managing S-TAP agents across database servers.
**GuardAPI:** Command-line and REST interface for automating Guardium operations and integrations.
**Guardium Rate (G-Rate):** Rate at which activity records are processed by the Guardium platform.
**High Availability:** Guardium configuration where multiple Collectors and an Aggregator provide redundancy and continuous operation.
**Id-Vault:** Encrypted credential store used for secure secret management within Guardium.
**IM (Infrastructure Management):** Guardium component that monitors health and performance of deployed agents and Collectors.
**Incident Builder:** Tool for creating incident events from policy violations with contextual detail.
**Insider Threat Detection:** Guardium module that analyses privileged-user activity and alerts on potential malicious insider actions.
**Inspection Engine:** Guardium component deployed on database servers to capture and forward traffic; configurable per database type.
**Java Secure Socket Extension (JSSE):** Java security extension used by Guardium for encrypted transport between components.
**K-TAP (Kernel TAP):** Linux kernel module installed alongside S-TAP that intercepts OS-level database socket traffic.
**Kerberos Authentication:** Network authentication protocol supported by Guardium for authenticating users and services.
**Log Buffer Size:** Memory buffer size configuring how many Audit Process log entries are held before flushing.
**Log Retention:** Policy specifying how long activity records are retained on the Collector before archiving or deletion.
**Lookup Table:** Static reference data (e.g., IP-to-region mapping) that Guardium policies can query for dynamic decisions.
**Manual Audit:** Human-driven method of verifying entitlement compliance by assessing individual activities or aggregating results.
**Masked View:** Database view that dynamically obscures sensitive column values using Guardium masking policies.
**Masking Engine:** Guardium subsystem that applies data masking rules to captured traffic.
**Meta Tag:** User-defined label attached to a data source or object to enable policy grouping and reporting.
**Mirror Configuration:** Duplicate Guardium environment used for disaster recovery, testing, or sandboxing.
**MongoDB Atlas:** Cloud database service supported by Guardium's native connector for monitoring and masking.
**MSSQL:** Microsoft SQL Server database platform; Guardium supports detailed inspection of its traffic.
**Network Appliance:** NAS, SAN, or other storage device that Guardium's FAM module can monitor.
**Network Segment:** Subnet or VLAN range to which Guardium policies can be selectively applied.
**Node Host:** Hostname used by Guardium components for internal communication independent of IP addressing.
**Object Level:** Granularity in Guardium policies targeting individual tables, views, or stored procedures.
**Office 365:** Microsoft cloud suite whose email, OneDrive, and SharePoint usage Guardium can monitor for DLP.
**One-Time Token:** Short-lived credential generated by the Guardium UI for temporary API authentication.
**OS User:** Operating-system username captured from database connections; used in session classification.
**Out-of-Band Rules:** Guardium firewall policies operating independently of the database engine to block or mask queries at the network layer.
**Passphrase:** Longer credential used for client authentication to Guardium services (e.g., API client secret).
**Password ID:** Identifier for stored passwords within Guardium's credential management system.
**Peer Group:** Logical collection of data sources with similar security requirements managed together in Guardium policies.
**Policy Builder:** Guardium tool for creating and managing audit policies specifying monitored activities and violation responses.
**Policy Exception:** Rule that overrides a standard control policy for specific users, hosts, or time windows.
**Policy Manager:** Guardium component that evaluates captured database activity against installed security policies.
**Policy Scope:** Definition of the data source, user, and resource set to which a Guardium rule applies.
**Policy Violation:** Event recorded when monitored activity matches a defined Guardium policy rule and is deemed non-compliant.
**Predefined Templates:** IBM-supplied configuration examples for common Guardium use cases (PCI-DSS, GDPR, HIPAA, SOX).
**Primary Collector:** Designated Collector that receives and processes initial data streams from S-TAP agents.
**QDBB:** Guardium internal queue that tracks pending log entries for Audit Process consumption.
**Query Plan:** Database execution strategy that Guardium can collect and analyse for performance forensics.
**Query Stream:** Continuous flow of captured database queries processed by the Guardium pipeline.
**Ranger:** Apache open-source framework providing centralised security administration for Hadoop ecosystems; integrates with Guardium.
**Raw Log:** Unprocessed activity record exported from Guardium for external correlation or archival.
**Reconciliation:** Guardium process that ensures data consistency across components and synchronises user accounts with external identity stores.
**Remote Path:** Reference to a file or directory located outside the Guardium appliance.
**Report Builder:** Guardium interface for designing custom reports with template selection, filtering, and output formatting.
**REST API:** HTTP-based interface for programmatic interaction with Guardium services.
**Revocable Credential:** Credential type that can be invalidated or regenerated without redeploying agents.
**RNG (Report and Notification Gateway):** Guardium component managing report scheduling and alert distribution.
**Role Hierarchy:** Structured framework defining user roles and data access levels used by DLS to filter audit results.
**Rotate Key:** Periodic Guardium process to replace encryption keys protecting stored activity data.
**S-DAQ:** Guardium subsystem supporting advanced real-time data analysis of captured traffic.
**S-GATE:** Guardium component enforcing real-time database access policies and blocking or masking unauthorised queries.
**SGATE-LIGHT:** Simplified S-GATE variant optimised for resource-limited environments.
**SGATE-XL:** Enhanced S-GATE supporting complex policies and high-throughput environments.
**Sanctioned Validation:** Guardium feature that permits authorised security assessments without triggering policy violations.
**Sanitize Credentials:** Guardium operation that removes sensitive authentication data from captured traffic before storage.
**Self Service Portal:** Web interface allowing end users to view their own activity summaries and request access changes.
**Service Account:** Dedicated non-human account created for integration tools with limited Guardium permissions.
**Session ID:** Unique identifier assigned by Guardium to each monitored database session for cross-collector correlation.
**Sharding-Aware:** Guardium capability to track distributed queries across multiple database shards.
**Single Point of Failure (SPOF):** Risk term; Guardium mitigates SPOF by distributing collectors and aggregators geographically.
**SSL Offload:** Configuration where TLS termination occurs outside Guardium (e.g., at a load balancer) before traffic reaches the Collector.
**S-TAP (Software TAP):** IBM Guardium software agent installed on database servers that captures and forwards database traffic to a Guardium Collector.
**S-TAP Status:** Real-time health and connectivity indicator for deployed S-TAP agents.
**Stop List:** Set of database objects or commands Guardium automatically excludes from monitoring or policy evaluation.
**Sudo User:** Non-root account granted privileged access via sudo; Guardium logs the original OS user when sudo is used.
**Support Tool:** Guardium utility providing diagnostics, log collection, and configuration auditing.
**Syslog:** Standard protocol for forwarding log messages; Guardium integrates with syslog servers for centralised logging.
**System Level:** Refers to Guardium components operating at kernel level for low-overhead traffic interception.
**Table Level Auditing:** Guardium capability to audit database activities at the table level with detailed operational data.
**Target Host:** Parameter in Guardium APIs identifying the Collector or aggregator that should receive the request.
**Time Sync:** Guardium mechanism that synchronises clocks across all components to ensure consistent timestamps.
**TLS Version:** Supported encryption protocol version (e.g., TLS 1.2, TLS 1.3) configured for secure Guardium communications.
**TRANSFORM:** Guardium action type that modifies audit data output before storage or display.
**Transaction Window:** Time-bounded period during which Guardium evaluates time-based policy actions.
**U-APM (User Activity Profile Manager):** Guardium module that profiles user behaviour to detect anomalies.
**User Consent:** Guardium control requiring explicit user authorisation before certain sensitive operations can proceed.
**User Group:** Collection of user accounts sharing the same Guardium roles and policy permissions.
**Vault:** Secure external storage (e.g., HashiCorp Vault, CyberArk) integrated with Guardium for credential and secret management.
**Virtual Host:** Domain name resolved to multiple backend servers; Guardium can monitor per-host activity independently.
**WAM (Web Activity Monitor):** Records user actions and security events in web-based database applications.
**Whitelist:** List of approved entities (users, IPs, applications) exempted from Guardium monitoring or policy evaluation.
**Window Size:** S-TAP configuration parameter for TCP packet analysis balancing capture depth and performance.
**WINSTAP_AUTO_ACTIVATE:** S-TAP parameter controlling whether the Windows agent service starts automatically after installation.
**WINSTAP_CMD_LINE:** Command-line options passed to the Windows S-TAP service on start or stop.
**WINSTAP_ENABLE_MONITORING:** Flag enabling or disabling database traffic collection by the Windows S-TAP agent.
**WINSTAP_MEM_TIMEOUT:** Timeout for shared-memory connections between the Windows S-TAP and the monitored database.
**WINSTAP_SETUP_TYPE:** Parameter defining the Windows S-TAP operational mode (Monitoring, Blocking, or Both).
