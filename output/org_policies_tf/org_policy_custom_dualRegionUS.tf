module "org_policy_custom_dualRegionUS" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.dualRegionUS"
  title       = "Buckets must be located in a dual-region"
  description = "Newly created buckets and newly updated buckets must be located in a dual-region composed of the us-east1 and us-east4 regions."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && ('US-EAST1' in resource.customPlacementConfig.dataLocations && 'US-EAST4' in resource.customPlacementConfig.dataLocations)
CEL
}