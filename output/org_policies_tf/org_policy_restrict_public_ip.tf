module "org_policy_restrict_public_ip" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictPublicIP"
  title       = "Restrict Public IP for AlloyDB Instances"
  description = "Disallows the creation or update of AlloyDB instances with public IP enabled."
  expression  = <<CEL
resource.networkConfig.enablePublicIp == true
CEL
}