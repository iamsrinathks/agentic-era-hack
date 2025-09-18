module "org_policy_datafusion_instance_enable_rbac" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceEnableRbac"
  title       = "Restrict Datafusion Instance Enable RBAC"
  description = "Prevents enabling RBAC for Datafusion instances."
  expression  = <<CEL
resource.enableRbac == true
CEL
}