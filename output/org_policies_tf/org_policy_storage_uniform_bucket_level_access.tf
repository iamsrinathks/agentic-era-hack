module "org_policy_storage_uniform_bucket_level_access" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.uniformBucketLevelAccess"
  title       = "Enforce Uniform Bucket-Level Access for Cloud Storage"
  description = "This boolean constraint requires buckets to use uniform bucket-level access where this constraint is set to True . Any new bucket in the Organization resource must have uniform bucket-level access enabled, and no existing buckets in the organization resource can disable uniform bucket-level access. Enforcement of this constraint is not retroactive: existing buckets with uniform bucket-level access disabled continue to have it disabled. The default value for this constraint is False . Uniform bucket-level access disables the evaluation of ACLs assigned to Cloud Storage objects in the bucket. Consequently, only IAM policies grant access to objects in these buckets."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}