module "org_policy_restrict_instance_private_instance" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstancePrivateInstance"
  title       = "Restrict Data Fusion Private Instance"
  description = "Prevents creation of private Data Fusion instances."
  expression  = <<CEL
resource.privateInstance == true
CEL
}