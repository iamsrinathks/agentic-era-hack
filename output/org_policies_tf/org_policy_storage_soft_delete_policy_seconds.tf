module "org_policy_storage_soft_delete_policy_seconds" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.softDeletePolicySeconds"
  title       = "Soft Delete Policy Retention Duration for Cloud Storage Buckets"
  description = "This constraint defines the allowable retention durations for soft delete policies set on Cloud Storage buckets where this constraint is enforced. Any insert, update, or patch operation on a bucket where this constraint is enforced must have a soft delete policy duration that matches the constraint. When a new organization policy is enforced, the soft delete policy of existing buckets remains unchanged and valid. By default, if no organization policy is specified, a Cloud Storage bucket can have a soft delete policy of any duration."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}