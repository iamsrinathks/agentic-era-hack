module "org_policy_datafusion_instance_enable_stackdriver_monitoring" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceEnableStackdriverMonitoring"
  title       = "Restrict Datafusion Instance Enable Stackdriver Monitoring"
  description = "Prevents enabling Stackdriver Monitoring for Datafusion instances."
  expression  = <<CEL
resource.enableStackdriverMonitoring == true
CEL
}