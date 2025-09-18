module "org_policy_restrict_instance_enable_rbac" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceEnableRbac"
  title       = "Restrict Data Fusion Instance RBAC"
  description = "Prevents enabling Role-Based Access Control (RBAC) for Data Fusion instances."
  expression  = <<CEL
resource.enableRbac == true
CEL
}