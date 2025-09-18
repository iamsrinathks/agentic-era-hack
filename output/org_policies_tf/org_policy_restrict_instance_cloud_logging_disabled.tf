module "org_policy_restrict_instance_cloud_logging_disabled" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceCloudLoggingDisabled"
  title       = "Restrict Data Fusion Instance Cloud Logging Disabled"
  description = "Prevents disabling Cloud Logging for Data Fusion instances."
  expression  = <<CEL
resource.loggingConfig.instanceCloudLoggingDisabled == true
CEL
}