module "org_policy_datafusion_instance_private_instance" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstancePrivateInstance"
  title       = "Restrict Datafusion Instance Private Instance"
  description = "Prevents creating private instances for Datafusion."
  expression  = <<CEL
resource.privateInstance == true
CEL
}