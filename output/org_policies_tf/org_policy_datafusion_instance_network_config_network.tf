module "org_policy_datafusion_instance_network_config_network" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceNetworkConfigNetwork"
  title       = "Restrict Datafusion Instance Network Configuration Network"
  description = "Prevents setting a specific network for Datafusion instances."
  expression  = <<CEL
resource.networkConfig.network == "projects/project-id/global/networks/restricted-network"
CEL
}