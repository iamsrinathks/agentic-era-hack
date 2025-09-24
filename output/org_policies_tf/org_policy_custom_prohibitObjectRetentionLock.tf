module "org_policy_custom_prohibitObjectRetentionLock" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.prohibitObjectRetentionLock"
  title       = "Objects cannot have retention configurations"
  description = "Newly created buckets and newly updated buckets cannot have Object Retention Lock enabled."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && resource.objectRetention.mode == 'Enabled'
CEL
}