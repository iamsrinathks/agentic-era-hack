module "org_policy_restrict_dnspeering_domain" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDnsPeeringDomain"
  title       = "Restrict Data Fusion DnsPeering Domain"
  description = "Prevents setting a specific domain for Data Fusion DnsPeering."
  expression  = <<CEL
resource.domain == "forbidden.domain"
CEL
}