module "org_policy_customRestrictCmekCryptoKeyProjects" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customRestrictCmekCryptoKeyProjects"
  title       = "Custom Restrict CMEK Crypto Key Projects Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Reject requests to Cloud Storage if the request includes a customer-managed encryption key and the key does not belong to a project specified by the constraint. Similarly, reject requests that create or rewrite an object if the object would be encrypted by the bucket's default encryption key and that key does not belong to a project specified by the constraint.' constraint."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}