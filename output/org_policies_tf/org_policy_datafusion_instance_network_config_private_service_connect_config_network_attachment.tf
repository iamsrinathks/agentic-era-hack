module "org_policy_datafusion_instance_network_config_private_service_connect_config_network_attachment" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceNetworkConfigPrivateServiceConnectConfigNetworkAttachment"
  title       = "Restrict Datafusion Instance Network Configuration Private Service Connect Configuration Network Attachment"
  description = "Prevents setting a specific Private Service Connect network attachment for Datafusion instances."
  expression  = <<CEL
resource.networkConfig.privateServiceConnectConfig.networkAttachment == "projects/project-id/regions/region/networkAttachments/restricted-attachment"
CEL
}