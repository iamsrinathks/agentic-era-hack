module "org_policy_datafusion_dns_peering_domain" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionDnsPeeringDomain"
  title       = "Restrict Datafusion DNS Peering Domain"
  description = "Prevents setting a specific domain for Datafusion DNS peering."
  expression  = <<CEL
resource.domain == "restricted.example.com"
CEL
}