module "org_policy_datafusion_instance_event_publish_config_enabled" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceEventPublishConfigEnabled"
  title       = "Restrict Datafusion Instance Event Publish Configuration Enabled"
  description = "Prevents enabling event publishing for Datafusion instances."
  expression  = <<CEL
resource.eventPublishConfig.enabled == true
CEL
}