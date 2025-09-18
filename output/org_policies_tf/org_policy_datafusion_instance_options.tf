module "org_policy_datafusion_instance_options" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceOptions"
  title       = "Restrict Datafusion Instance Options"
  description = "Prevents setting specific options for Datafusion instances."
  expression  = <<CEL
resource.options["option-key"] == "restricted-value"
CEL
}