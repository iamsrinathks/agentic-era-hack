module "org_policy_datafusion_instance_network_config_ip_allocation" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceNetworkConfigIpAllocation"
  title       = "Restrict Datafusion Instance Network Configuration IP Allocation"
  description = "Prevents setting a specific IP allocation for Datafusion instances."
  expression  = <<CEL
resource.networkConfig.ipAllocation == "restricted-ip-range"
CEL
}