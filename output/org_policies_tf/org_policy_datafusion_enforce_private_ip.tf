module "org_policy_datafusion_require_env_label" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.datafusionRequireEnvironmentLabel"
  title       = "Require Environment Label on Cloud Data Fusion Instances"
  description = "Ensures all Cloud Data Fusion instances have an 'environment' label set to 'production'."
  expression  = <<CEL
has(resource.labels.environment) && resource.labels.environment == "production"
CEL
}