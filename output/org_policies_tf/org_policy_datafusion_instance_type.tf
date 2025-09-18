module "org_policy_datafusion_instance_type" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceType"
  title       = "Restrict Datafusion Instance Type"
  description = "Prevents creating instances of a specific type for Datafusion."
  expression  = <<CEL
resource.type == "BASIC"
CEL
}