module "org_policy_enforceContBackupConfig" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/enforceContBackupConfig"
  title       = "Enforce continuous backup configuration on AlloyDB clusters"
  description = "Prevent users from disabling continuous backup configuration on cluster creation and update."
  expression  = <<CEL
resource.continuousBackupConfig.enabled == false
CEL
}