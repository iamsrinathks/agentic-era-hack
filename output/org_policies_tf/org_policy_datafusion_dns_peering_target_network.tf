module "org_policy_datafusion_dns_peering_target_network" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionDnsPeeringTargetNetwork"
  title       = "Restrict Datafusion DNS Peering Target Network"
  description = "Prevents setting a specific target network for Datafusion DNS peering."
  expression  = <<CEL
resource.targetNetwork == "projects/project-id/global/networks/restricted-network"
CEL
}