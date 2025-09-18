module "org_policy_restrict_instance_psc_unreachable_cidr" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstancePscUnreachableCidr"
  title       = "Restrict Data Fusion Instance Private Service Connect Unreachable CIDR Block"
  description = "Prevents using a specific Private Service Connect unreachable CIDR block for Data Fusion instances."
  expression  = <<CEL
resource.networkConfig.privateServiceConnectConfig.unreachableCidrBlock == "forbidden_cidr"
CEL
}