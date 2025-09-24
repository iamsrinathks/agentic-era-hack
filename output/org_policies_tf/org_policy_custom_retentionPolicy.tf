module "org_policy_custom_retentionPolicy" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.retentionPolicy"
  title       = "Bucket retention policy is either 3,600 seconds or 2,678,400 seconds"
  description = "Newly created buckets and newly updated buckets must have a retention policy that's either 3,600 seconds or 2,678,400 seconds."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && resource.retentionPolicy.retentionPeriod not in [3600, 2678400]
CEL
}