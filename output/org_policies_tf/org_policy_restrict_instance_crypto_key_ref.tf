module "org_policy_restrict_instance_crypto_key_ref" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceCryptoKeyReference"
  title       = "Restrict Data Fusion Instance Crypto Key Reference"
  description = "Prevents using a specific customer-managed encryption key for Data Fusion instances."
  expression  = <<CEL
resource.cryptoKeyConfig.keyReference == "forbidden_key_reference"
CEL
}