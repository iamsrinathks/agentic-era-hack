module "org_policy_restrict_instance_description" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceDescription"
  title       = "Restrict Data Fusion Instance Description"
  description = "Prevents setting a specific description for Data Fusion instances."
  expression  = <<CEL
resource.description == "forbidden_description"
CEL
}