module "org_policy_storage_restrict_auth_types" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.storage.restrictAuthTypes"
  title       = "Restrict Authentication Types for Cloud Storage"
  description = "The constraint defines the set of authentication types that would be restricted from accessing any storage resources under the organization in Cloud Storage. Supported values are USER_ACCOUNT_HMAC_SIGNED_REQUESTS and SERVICE_ACCOUNT_HMAC_SIGNED_REQUESTS . Use in:ALL_HMAC_SIGNED_REQUESTS to include both."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}