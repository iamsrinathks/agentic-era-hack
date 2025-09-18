module "org_policy_restrict_instance_display_name" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceDisplayName"
  title       = "Restrict Data Fusion Instance Display Name"
  description = "Prevents setting a specific display name for Data Fusion instances."
  expression  = <<CEL
resource.displayName == "forbidden_display_name"
CEL
}