module "org_policy_datafusion_instance_logging_config_instance_cloud_logging_disabled" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceLoggingConfigInstanceCloudLoggingDisabled"
  title       = "Restrict Datafusion Instance Logging Configuration Instance Cloud Logging Disabled"
  description = "Prevents disabling instance cloud logging for Datafusion instances."
  expression  = <<CEL
resource.loggingConfig.instanceCloudLoggingDisabled == true
CEL
}