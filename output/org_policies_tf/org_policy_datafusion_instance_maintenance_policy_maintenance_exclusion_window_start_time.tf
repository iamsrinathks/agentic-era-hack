module "org_policy_datafusion_instance_maintenance_policy_maintenance_exclusion_window_start_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceMaintenancePolicyMaintenanceExclusionWindowStartTime"
  title       = "Restrict Datafusion Instance Maintenance Policy Maintenance Exclusion Window Start Time"
  description = "Prevents setting a specific maintenance exclusion window start time for Datafusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceExclusionWindow.startTime == "2024-12-31T23:00:00Z"
CEL
}