module "org_policy_restrict_instance_psc_network_attachment" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstancePscNetworkAttachment"
  title       = "Restrict Data Fusion Instance Private Service Connect Network Attachment"
  description = "Prevents using a specific Private Service Connect network attachment for Data Fusion instances."
  expression  = <<CEL
resource.networkConfig.privateServiceConnectConfig.networkAttachment == "forbidden_attachment"
CEL
}