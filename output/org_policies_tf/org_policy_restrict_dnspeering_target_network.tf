module "org_policy_restrict_dnspeering_target_network" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDnsPeeringTargetNetwork"
  title       = "Restrict Data Fusion DnsPeering Target Network"
  description = "Prevents setting a specific target network for Data Fusion DnsPeering."
  expression  = <<CEL
resource.targetNetwork == "forbidden-network"
CEL
}