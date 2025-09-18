module "org_policy_restrict_instance_version" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceVersion"
  title       = "Restrict Data Fusion Instance Version"
  description = "Prevents creating Data Fusion instances with a specific version."
  expression  = <<CEL
resource.version == "forbidden_version"
CEL
}