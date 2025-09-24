module "org_policy_customRetentionPolicySeconds" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customRetentionPolicySeconds"
  title       = "Custom Bucket Retention Policy Duration in Seconds Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Bucket retention policy duration in seconds' constraint. When you apply the retentionPolicySeconds constraint, you specify one or more durations as part of the constraint. Once set, bucket retention policies must include one of the specified durations. retentionPolicySeconds is required when creating a new bucket and when adding or updating the retention period of a pre-existing bucket; however, it's not otherwise required on pre-existing buckets. If you set multiple retentionPolicySeconds constraints at different resource levels, they are enforced hierarchically . For this reason, it's recommended that you set the inheritFromParent field to true , which ensures that policies at higher layers are also considered."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}