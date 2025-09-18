module "org_policy_restrict_dnspeering_name" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDnsPeeringName"
  title       = "Restrict Data Fusion DnsPeering Name"
  description = "Prevents setting a specific name for Data Fusion DnsPeering."
  expression  = <<CEL
resource.name == "forbidden_name"
CEL
}