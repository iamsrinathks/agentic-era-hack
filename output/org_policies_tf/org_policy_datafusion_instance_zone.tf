module "org_policy_datafusion_instance_zone" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceZone"
  title       = "Restrict Datafusion Instance Zone"
  description = "Prevents deploying Datafusion instances in a specific zone."
  expression  = <<CEL
resource.zone == "restricted-zone"
CEL
}