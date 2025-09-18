module "org_policy_restrict_instance_patch_revision" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstancePatchRevision"
  title       = "Restrict Data Fusion Instance Patch Revision"
  description = "Prevents using a specific patch revision for Data Fusion instances."
  expression  = <<CEL
resource.patchRevision == "forbidden_patch_revision"
CEL
}