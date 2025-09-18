module "org_policy_restrict_instance_options" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceOptions"
  title       = "Restrict Data Fusion Instance Options"
  description = "Prevents setting specific options for Data Fusion instances."
  expression  = <<CEL
resource.options.key == "forbidden_value"
CEL
}