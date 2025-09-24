module "org_policy_customUniformBucketLevelAccess" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customUniformBucketLevelAccess"
  title       = "Custom Require Uniform Bucket-Level Access Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Require uniform bucket-level access' constraint. When you apply the uniformBucketLevelAccess constraint, new buckets must enable the uniform bucket-level access feature , and pre-existing buckets with this feature enabled cannot disable it. Pre-existing buckets with uniform bucket-level access disabled are not required to enable it. Note: Some organizations have the uniformBucketLevelAccess constraint enabled by default. To find out whether your organization has the uniformBucketLevelAccess constraint enabled or disabled, contact your organization administrator."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}