module "org_policy_custom_disableLegacyStorageClass" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.disableLegacyStorageClass"
  title       = "Buckets cannot use legacy storage classes"
  description = "Newly created buckets and newly updated buckets must use Standard storage, Nearline storage, Coldline storage, or Archive storage."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && resource.storageClass in ['STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE']
CEL
}