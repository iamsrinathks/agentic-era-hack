module "org_policy_datafusion_instance_version" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceVersion"
  title       = "Restrict Datafusion Instance Version"
  description = "Prevents using a specific version for Datafusion instances."
  expression  = <<CEL
resource.version == "6.8.0"
CEL
}