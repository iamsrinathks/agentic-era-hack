module "org_policy_datafusion_enforce_private_ip" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.datafusionEnforcePrivateIp"
  title       = "Enforce Private IP for Cloud Data Fusion Instances"
  description = "Requires Cloud Data Fusion instances to be configured with private IP only."
  expression  = <<CEL
resource.networkConfig.privateIpOnly == true
CEL
}