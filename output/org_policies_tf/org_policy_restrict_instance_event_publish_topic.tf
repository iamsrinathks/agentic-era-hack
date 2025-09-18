module "org_policy_restrict_instance_event_publish_topic" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceEventPublishTopic"
  title       = "Restrict Data Fusion Instance Event Publish Topic"
  description = "Prevents publishing events to a specific topic for Data Fusion instances."
  expression  = <<CEL
resource.eventPublishConfig.topic == "forbidden-topic"
CEL
}