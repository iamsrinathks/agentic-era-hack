module "org_policy_datafusion_instance_description" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceDescription"
  title       = "Restrict Datafusion Instance Description"
  description = "Prevents setting a specific description for Datafusion instances."
  expression  = <<CEL
resource.description == "restricted"
CEL
}