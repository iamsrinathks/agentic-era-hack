module "org_policy_datafusion_instance_dataproc_service_account" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceDataprocServiceAccount"
  title       = "Restrict Datafusion Instance Dataproc Service Account"
  description = "Prevents using a specific Dataproc service account for Datafusion instances."
  expression  = <<CEL
resource.dataprocServiceAccount == "restricted-sa@project-id.iam.gserviceaccount.com"
CEL
}