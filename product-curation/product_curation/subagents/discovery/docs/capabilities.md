# Security Capabilities and Parameters

| Capability                  | Weight | Description                                   | Why It Matters |
|------------------------------|--------|-----------------------------------------------|----------------|
| VPC-SC (VPC Service Controls) | 5      | Support for VPC Service Controls              | Essential for perimeter security in regulated environments |
| TLS                          | 5      | Transport Layer Security support              | Ensures encrypted data in transit |
| Ingress/Egress Control       | 5      | Control over incoming/outgoing traffic        | Helps prevent data exfiltration |
| ILB Support                  | 4      | Internal Load Balancer support                | Key for secure internal service exposure |
| Encryption at Rest           | 5      | Encrypts data stored on disk                  | Prevents unauthorized data access |
| Encryption in Transit        | 4      | Encrypts data during transmission             | Protects data over networks |
| **CMEK (Customer Managed Encryption Keys)** | 5 | Explicit support for CMEK via Cloud KMS       | Ensures organizations retain control of encryption keys, critical for compliance |
| BYOK / HYOK                  | 4      | Ability to import or host keys externally     | Provides maximum control for highly regulated industries |
| IAM Controls                 | 3      | Fine-grained access controls                  | Ensures only authorized users can act |
| Org Policies                 | 3      | Supports GCP Organization Policies            | Ensures compliance across projects |
| **Custom Org Policies**      | 4      | Ability to define and enforce custom org policies | Enables tailored governance and compliance enforcement |
| **Custom SHA (Security Health Analytics)** | 4 | Ability to define custom SHA detectors and rules | Provides proactive misconfiguration detection aligned to organizational needs |
| DLP                          | 2      | Data Loss Prevention integration              | Detects and protects sensitive information |
| Audit Logging & Monitoring   | 5      | Native integration with Cloud Audit Logs, SIEM, and monitoring tools | Enables traceability, incident response, and compliance reporting |
| Secrets Management           | 4      | Secure storage and rotation of credentials, tokens, and API keys | Prevents credential leakage and enforces least privilege |
| Ease of Threat Modeling      | 4      | Simplicity in assessing threat vectors        | Aids in proactive design |
| Guardrails                   | 4      | Automated prevention measures                 | Helps prevent misconfigurations |
| APIs                         | 3      | Mature and controllable APIs                  | Critical for automation and integrations |
| Private Service Connect (PSC)| 3      | Supports PSC for internal access              | Improves secure service access |
| Service Perimeter Awareness  | 3      | Service Perimeter aware                       | Prevents data leakage across services |
| Threat Modeling Support      | 3      | Supports threat modeling practices            | Important for security by design |
| Zero Trust Readiness         | 4      | Support for identity/context-aware access     | Aligns with modern security models |
| Data Residency Controls      | 3      | Ability to restrict data to specific regions  | Critical for GDPR and data sovereignty |
| Patch & Vulnerability Mgmt   | 3      | Automated patching, CVE scanning, remediation | Reduces exposure to known vulnerabilities |
| Runtime Security             | 3      | Protection for workloads (e.g., container scanning, anomaly detection) | Ensures workloads remain secure after deployment |
| Incident Response Hooks      | 2      | Integration with alerting and response workflows | Improves time-to-detection and time-to-response |
| Supply Chain Security        | 4      | Support for signed artifacts, SBOM, provenance | Protects against tampered dependencies and builds |