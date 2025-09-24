module "org_policy_custom_bucketName" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.bucketName"
  title       = "Bucket names must match the specified regular expression"
  description = "Newly created buckets must have a name that matches the specified regular expression. Only letters are allowed in the bucket name."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE") && resource.name.matches('^[a-zA-Z]+$')
CEL
}