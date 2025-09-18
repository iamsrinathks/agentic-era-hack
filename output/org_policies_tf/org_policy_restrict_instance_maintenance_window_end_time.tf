module "org_policy_restrict_instance_maintenance_window_end_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceMaintenanceWindowEndTime"
  title       = "Restrict Data Fusion Instance Maintenance Window End Time"
  description = "Prevents setting a specific maintenance window end time for Data Fusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.window.endTime == "forbidden_end_time"
CEL
}