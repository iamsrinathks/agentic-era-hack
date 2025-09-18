module "org_policy_restrict_instance_maintenance_recurrence" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceMaintenanceRecurrence"
  title       = "Restrict Data Fusion Instance Maintenance Recurrence"
  description = "Prevents setting a specific maintenance window recurrence for Data Fusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.recurrence == "forbidden_recurrence"
CEL
}