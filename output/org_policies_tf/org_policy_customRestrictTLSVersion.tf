module "org_policy_customRestrictTLSVersion" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customRestrictTLSVersion"
  title       = "Custom Restrict TLS Version Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Prevent access to Cloud Storage by requests made using Transport Layer Security (TLS) 1.0 or 1.1.' constraint."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}