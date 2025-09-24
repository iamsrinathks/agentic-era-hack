module "org_policy_custom_prohibitBucketLock" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.prohibitBucketLock"
  title       = "Prohibit the use of Bucket Lock"
  description = "Newly created buckets and newly updated buckets cannot have Bucket Lock enabled."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && resource.retentionPolicy.isLocked == true
CEL
}