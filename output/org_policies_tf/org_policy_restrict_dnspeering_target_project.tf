module "org_policy_restrict_dnspeering_target_project" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDnsPeeringTargetProject"
  title       = "Restrict Data Fusion DnsPeering Target Project"
  description = "Prevents setting a specific target project for Data Fusion DnsPeering."
  expression  = <<CEL
resource.targetProject == "forbidden-project"
CEL
}