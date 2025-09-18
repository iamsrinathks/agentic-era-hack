module "org_policy_datafusion_dns_peering_target_project" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionDnsPeeringTargetProject"
  title       = "Restrict Datafusion DNS Peering Target Project"
  description = "Prevents setting a specific target project for Datafusion DNS peering."
  expression  = <<CEL
resource.targetProject == "restricted-project-id"
CEL
}