module "org_policy_datafusion_instance_maintenance_policy_maintenance_window_recurring_time_window_recurrence" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceMaintenancePolicyMaintenanceWindowRecurringTimeWindowRecurrence"
  title       = "Restrict Datafusion Instance Maintenance Policy Maintenance Window Recurring Time Window Recurrence"
  description = "Prevents setting a specific maintenance window recurrence for Datafusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceWindow.recurringTimeWindow.recurrence == "restricted"
CEL
}