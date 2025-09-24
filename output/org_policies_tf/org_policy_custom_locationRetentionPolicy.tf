module "org_policy_custom_locationRetentionPolicy" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.locationRetentionPolicy"
  title       = "All buckets in US and EU must have a retention policy of 86,400 seconds"
  description = "Newly created buckets and newly updated buckets located in US and EU regions must have a retention policy of 86,400 seconds."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && ((resource.location.startsWith('US') || resource.location.startsWith('EU')) && resource.retentionPolicy.retentionPeriod != 86400)
CEL
}