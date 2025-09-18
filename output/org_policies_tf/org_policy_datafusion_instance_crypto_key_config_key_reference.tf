module "org_policy_datafusion_instance_crypto_key_config_key_reference" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceCryptoKeyConfigKeyReference"
  title       = "Restrict Datafusion Instance Crypto Key Configuration Key Reference"
  description = "Prevents setting a specific crypto key reference for Datafusion instances."
  expression  = <<CEL
resource.cryptoKeyConfig.keyReference == "projects/project-id/locations/location/keyRings/key-ring/cryptoKeys/key-name"
CEL
}