module "org_policy_storage_secure_http_transport" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.secureHttpTransport"
  title       = "Restrict Unencrypted HTTP Access for Cloud Storage"
  description = "This boolean constraint, when enforced, explicitly denies HTTP (unencrypted) access to all storage resources. By default, the Cloud Storage XML API allows unencrypted HTTP access. Note that the Cloud Storage JSON API, gRPC, and Cloud console only allow encrypted HTTP access to Cloud Storage resources."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}