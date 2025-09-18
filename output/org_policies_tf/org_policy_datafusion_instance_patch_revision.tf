module "org_policy_datafusion_instance_patch_revision" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstancePatchRevision"
  title       = "Restrict Datafusion Instance Patch Revision"
  description = "Prevents setting a specific patch revision for Datafusion instances."
  expression  = <<CEL
resource.patchRevision == "restricted-revision"
CEL
}