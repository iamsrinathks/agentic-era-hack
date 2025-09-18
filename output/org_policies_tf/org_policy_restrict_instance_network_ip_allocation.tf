module "org_policy_restrict_instance_network_ip_allocation" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceNetworkIpAllocation"
  title       = "Restrict Data Fusion Instance Network IP Allocation"
  description = "Prevents using a specific IP allocation for Data Fusion instances."
  expression  = <<CEL
resource.networkConfig.ipAllocation == "forbidden_ip_allocation"
CEL
}