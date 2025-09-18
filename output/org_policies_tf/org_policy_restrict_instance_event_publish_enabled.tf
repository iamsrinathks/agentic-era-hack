module "org_policy_restrict_instance_event_publish_enabled" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceEventPublishEnabled"
  title       = "Restrict Data Fusion Instance Event Publish Enabled"
  description = "Prevents enabling event publishing for Data Fusion instances."
  expression  = <<CEL
resource.eventPublishConfig.enabled == true
CEL
}