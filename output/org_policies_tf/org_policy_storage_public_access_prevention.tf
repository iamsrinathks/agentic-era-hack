module "org_policy_storage_public_access_prevention" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.publicAccessPrevention"
  title       = "Enforce Public Access Prevention for Cloud Storage"
  description = "Secure your Cloud Storage data from public exposure by enforcing public access prevention. This governance policy prevents existing and future resources from being accessed via the public internet by disabling and blocking ACLs and IAM permissions that grant access to allUsers and allAuthenticatedUsers . Enforce this policy on the entire organization (recommended), specific projects, or specific folders to ensure no data is publicly exposed. This policy overrides existing public permissions. Public access will be revoked for existing buckets and objects after this policy is enabled. For more details on the effects of changing enforcement of this constraint on resources, please see: https://cloud.google.com/storage/docs/public-access-prevention."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}