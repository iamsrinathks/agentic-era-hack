module "org_policy_datafusion_instance_dataplex_data_lineage_integration_enabled" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceDataplexDataLineageIntegrationEnabled"
  title       = "Restrict Datafusion Instance Dataplex Data Lineage Integration"
  description = "Prevents enabling Dataplex Data Lineage Integration for Datafusion instances."
  expression  = <<CEL
resource.dataplexDataLineageIntegrationEnabled == true
CEL
}