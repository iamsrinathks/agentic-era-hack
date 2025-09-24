module "org_policy_customRestrictNonCmekServices" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customRestrictNonCmekServices"
  title       = "Custom Require Customer-Managed Encryption Keys (CMEK) for New and Rewritten Objects Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Require new and rewritten objects to be encrypted using customer-managed encryption keys , and require new buckets to set a Cloud KMS key as the default encryption key.' constraint."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}