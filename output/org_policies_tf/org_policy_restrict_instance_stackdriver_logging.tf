module "org_policy_restrict_instance_stackdriver_logging" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceStackdriverLogging"
  title       = "Restrict Data Fusion Instance Stackdriver Logging"
  description = "Prevents enabling Stackdriver Logging for Data Fusion instances."
  expression  = <<CEL
resource.enableStackdriverLogging == true
CEL
}