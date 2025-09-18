module "org_policy_datafusion_instance_event_publish_config_topic" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceEventPublishConfigTopic"
  title       = "Restrict Datafusion Instance Event Publish Configuration Topic"
  description = "Prevents setting a specific event publish topic for Datafusion instances."
  expression  = <<CEL
resource.eventPublishConfig.topic == "projects/project-id/topics/restricted-topic"
CEL
}