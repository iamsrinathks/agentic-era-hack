module "org_policy_restrict_instance_stackdriver_monitoring" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceStackdriverMonitoring"
  title       = "Restrict Data Fusion Instance Stackdriver Monitoring"
  description = "Prevents enabling Stackdriver Monitoring for Data Fusion instances."
  expression  = <<CEL
resource.enableStackdriverMonitoring == true
CEL
}