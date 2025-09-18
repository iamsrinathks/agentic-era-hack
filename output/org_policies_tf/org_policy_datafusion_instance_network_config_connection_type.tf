module "org_policy_datafusion_instance_network_config_connection_type" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceNetworkConfigConnectionType"
  title       = "Restrict Datafusion Instance Network Configuration Connection Type"
  description = "Prevents setting a specific network connection type for Datafusion instances."
  expression  = <<CEL
resource.networkConfig.connectionType == "PRIVATE_SERVICE_CONNECT"
CEL
}