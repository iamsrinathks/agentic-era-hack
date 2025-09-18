module "org_policy_datafusion_dns_peering_name" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionDnsPeeringName"
  title       = "Restrict Datafusion DNS Peering Name"
  description = "Prevents setting a specific name for Datafusion DNS peering."
  expression  = <<CEL
resource.name == "restricted-name"
CEL
}