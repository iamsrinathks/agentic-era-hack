module "org_policy_datafusion_instance_network_config_private_service_connect_config_unreachable_cidr_block" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceNetworkConfigPrivateServiceConnectConfigUnreachableCidrBlock"
  title       = "Restrict Datafusion Instance Network Configuration Private Service Connect Configuration Unreachable CIDR Block"
  description = "Prevents setting a specific Private Service Connect unreachable CIDR block for Datafusion instances."
  expression  = <<CEL
resource.networkConfig.privateServiceConnectConfig.unreachableCidrBlock == "restricted-cidr-block"
CEL
}