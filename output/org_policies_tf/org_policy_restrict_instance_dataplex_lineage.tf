module "org_policy_restrict_instance_dataplex_lineage" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceDataplexLineage"
  title       = "Restrict Data Fusion Instance Dataplex Data Lineage Integration"
  description = "Prevents enabling Dataplex Data Lineage integration for Data Fusion instances."
  expression  = <<CEL
resource.dataplexDataLineageIntegrationEnabled == true
CEL
}