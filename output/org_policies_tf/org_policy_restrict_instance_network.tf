module "org_policy_restrict_instance_network" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceNetwork"
  title       = "Restrict Data Fusion Instance Network"
  description = "Prevents using a specific network for Data Fusion instances."
  expression  = <<CEL
resource.networkConfig.network == "forbidden-network"
CEL
}