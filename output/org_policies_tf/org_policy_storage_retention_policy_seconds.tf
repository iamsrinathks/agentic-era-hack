module "org_policy_storage_retention_policy_seconds" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.retentionPolicySeconds"
  title       = "Retention Policy Duration for Cloud Storage Buckets"
  description = "This list constraint defines the set of durations for retention policies that can be set on Cloud Storage buckets. By default, if no organization policy is specified, a Cloud Storage bucket can have a retention policy of any duration. The list of allowed durations must be specified as a positive integer value greater than zero, representing the retention policy in seconds. Any insert, update, or patch operation on a bucket in the organization resource must have a retention policy duration that matches the constraint. Enforcement of this constraint is not retroactive. When a new organization policy is enforced, the retention policy of existing buckets remains unchanged and valid."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}