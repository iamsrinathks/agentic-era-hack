module "org_policy_customSoftDeletePolicySeconds" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customSoftDeletePolicySeconds"
  title       = "Custom Soft Delete Retention Duration Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Soft delete retention duration' constraint. When you apply the softDeletePolicySeconds constraint, you specify one or more durations as part of the constraint. Once set, the bucket soft delete policy must include one of the specified durations. softDeletePolicySeconds is required when creating a new bucket and when adding or updating the soft delete retention duration ( softDeletePolicy.retentionDuration ) of a pre-existing bucket; however, it does not otherwise affect pre-existing buckets. If you set multiple softDeletePolicySeconds constraints at different resource levels, they are enforced hierarchically . For this reason, it's recommended that you set the inheritFromParent field to true , which ensures that policies at higher layers are also considered."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}