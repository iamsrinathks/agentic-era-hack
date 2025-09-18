module "org_policy_datafusion_instance_maintenance_policy_maintenance_window_recurring_time_window_window_end_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceMaintenancePolicyMaintenanceWindowRecurringTimeWindowWindowEndTime"
  title       = "Restrict Datafusion Instance Maintenance Policy Maintenance Window Recurring Time Window Window End Time"
  description = "Prevents setting a specific maintenance window recurring end time for Datafusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.window.endTime == "2025-01-01T00:00:00Z"
CEL
}