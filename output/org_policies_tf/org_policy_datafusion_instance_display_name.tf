module "org_policy_datafusion_instance_display_name" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceDisplayName"
  title       = "Restrict Datafusion Instance Display Name"
  description = "Prevents setting a specific display name for Datafusion instances."
  expression  = <<CEL
resource.displayName == "restricted"
CEL
}