module "org_policy_datafusion_enforce_dns_description" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.datafusionEnforceDnsPeeringDescription"
  title       = "Enforce Description for Cloud Data Fusion DNS Peering"
  description = "Requires Cloud Data Fusion DNS peering configurations to have a specific description prefix."
  expression  = <<CEL
resource.description.startsWith("Managed by Org Policy")
CEL
}