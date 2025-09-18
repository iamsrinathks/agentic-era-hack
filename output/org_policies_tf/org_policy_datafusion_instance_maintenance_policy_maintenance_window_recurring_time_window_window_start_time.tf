module "org_policy_datafusion_instance_maintenance_policy_maintenance_window_recurring_time_window_window_start_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceMaintenancePolicyMaintenanceWindowRecurringTimeWindowWindowStartTime"
  title       = "Restrict Datafusion Instance Maintenance Policy Maintenance Window Recurring Time Window Window Start Time"
  description = "Prevents setting a specific maintenance window recurring start time for Datafusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.window.startTime == "2024-12-31T23:00:00Z"
CEL
}