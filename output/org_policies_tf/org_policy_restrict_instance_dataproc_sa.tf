module "org_policy_restrict_instance_dataproc_sa" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceDataprocServiceAccount"
  title       = "Restrict Data Fusion Instance Dataproc Service Account"
  description = "Prevents using a specific Dataproc service account for Data Fusion instances."
  expression  = <<CEL
resource.dataprocServiceAccount == "forbidden-service-account@example.com"
CEL
}