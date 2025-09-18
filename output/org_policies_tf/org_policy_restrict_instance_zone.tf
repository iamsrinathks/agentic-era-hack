module "org_policy_restrict_instance_zone" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceZone"
  title       = "Restrict Data Fusion Instance Zone"
  description = "Prevents creating Data Fusion instances in a specific zone."
  expression  = <<CEL
resource.zone == "forbidden_zone"
CEL
}