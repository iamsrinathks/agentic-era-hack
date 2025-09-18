module "org_policy_restrict_instance_type" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceType"
  title       = "Restrict Data Fusion Instance Type"
  description = "Prevents creating Data Fusion instances of a specific type."
  expression  = <<CEL
resource.type == "forbidden_type"
CEL
}