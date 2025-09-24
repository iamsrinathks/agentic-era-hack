module "org_policy_customSecureHttpTransport" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/customSecureHttpTransport"
  title       = "Custom Restrict Unencrypted HTTP Requests Policy"
  description = "This custom policy aims to mirror the functionality of the predefined 'Restrict unencrypted HTTP requests' constraint. When you apply the secureHttpTransport constraint, all unencrypted HTTP access to Cloud Storage resources is denied. By default, the Cloud Storage XML API allows unencrypted HTTP access. CNAME redirects only support unencrypted HTTP access."
  expression  = <<CEL
resource.name.startsWith("projects/YOUR_PROJECT_ID")
CEL
}