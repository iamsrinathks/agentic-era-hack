module "org_policy_custom_enforceBucketVersioning" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.enforceBucketVersioning"
  title       = "Buckets must have Object Versioning enabled"
  description = "Newly created buckets and newly updated buckets must have Object Versioning enabled."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && resource.versioning.enabled == true
CEL
}