module "org_policy_restrict_instance_maintenance_window_start_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceMaintenanceWindowStartTime"
  title       = "Restrict Data Fusion Instance Maintenance Window Start Time"
  description = "Prevents setting a specific maintenance window start time for Data Fusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.window.startTime == "forbidden_start_time"
CEL
}