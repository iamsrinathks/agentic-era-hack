module "org_policy_datafusion_instance_enable_stackdriver_logging" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceEnableStackdriverLogging"
  title       = "Restrict Datafusion Instance Enable Stackdriver Logging"
  description = "Prevents enabling Stackdriver Logging for Datafusion instances."
  expression  = <<CEL
resource.enableStackdriverLogging == true
CEL
}