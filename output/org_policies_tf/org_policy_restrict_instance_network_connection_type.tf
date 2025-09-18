module "org_policy_restrict_instance_network_connection_type" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceNetworkConnectionType"
  title       = "Restrict Data Fusion Instance Network Connection Type"
  description = "Prevents using a specific network connection type for Data Fusion instances."
  expression  = <<CEL
resource.networkConfig.connectionType == "forbidden_connection_type"
CEL
}