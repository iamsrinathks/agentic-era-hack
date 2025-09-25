# Guidelines for Product Curation Discovery

## General Principles
- **Security First**: All new architectures and processes must prioritize security.  
- **Infrastructure as Code (IaC)**: All infrastructure should be maintained via IaC processes using Terraform.  
- **Compliance Adherence**: Ensure compliance with relevant industry standards and regulations.  
- **Preventative Controls**: Preventative controls must be deployed for IaC using GCP native controls (Org policies, custom org policies, SHA).  

---

## Network and Connectivity Requirements
- **Interconnect Usage**: All traffic between connected environments should travel exclusively via interconnect.  
  - In disconnected or development environments, VPN must be used.  
- **Hub and Spoke Architecture**: All product deployments must adhere to a hub-and-spoke architecture, following GCP's project-based isolation principles.  
- **Private Networking**:  
  - All products should be deployed with private IPs only and using private networking.  
  - **Preferred**: Private Service Connect (PSC), as it simplifies connectivity and reduces IP address requirements compared to Private Service Access (PSA).  

---

## Data Security and Encryption
- **Private Networking**: Any product requiring more than a `/24` IP usage should be flagged, as it stresses the available IP ranges on the GCP platform.  
- **Customer Managed Encryption Key (CMEK)**: Must be used at all locations within the GCP environment (via Cloud KMS).  
- **VPC Service Controls (VPCSC)**: All products must comply with and be protected under VPCSC.  

---

## Identity and Access Management
- **Workload Identity**: Mandatory for all Kubernetes-related interactions with GCP products.  
- **Cloud SQL Authentication**:  
  - Only permitted method: **Cloud SQL Auth Proxy sidecar pattern** combined with IAM authentication.  
  - All other authentication methods are strictly prohibited.  

---

## Resilience
- **High Availability (HA)**: Products should support multi-regional capabilities, either via:  
  - Multi-regional deployment, or  
  - Multiple region deployment with failover / disaster recovery (DR).  
- **Backup and Restore**: Any data storage product must:  
  - Allow configuration of backups.  
  - Provide processes for restoring data.  

---

## Discovery Evaluation Criteria
- **Adherence to Guidelines**: New product discovery must strictly adhere to the outlined guidelines.  
- **Security Assessment**:  
  - Conduct a thorough security assessment to identify and mitigate vulnerabilities.  
  - **Mandatory**: CMEK, VPCSC, and compliance.  
- **Networking Requirements**:  
  - Perform a thorough assessment ensuring private connectivity is used.  
  - Any deviation requires review.  
- **Compliance Review**: Verify compliance with relevant industry standards and regulations.  
- **Resiliency and HA Review**: Review the **RPO** (Recovery Point Objective) and **RTO** (Recovery Time Objective) of the product to determine adequacy.  

---

## Note
These guidelines serve as a foundation for evaluating new architectures and processes.  
Specific requirements may vary based on organizational needs and risk tolerances.  
Regular reviews and updates are essential to ensure ongoing compliance and security.  