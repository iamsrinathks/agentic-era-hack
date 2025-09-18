module "org_policy_datafusion_instance_maintenance_policy_maintenance_exclusion_window_end_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictDatafusionInstanceMaintenancePolicyMaintenanceExclusionWindowEndTime"
  title       = "Restrict Datafusion Instance Maintenance Policy Maintenance Exclusion Window End Time"
  description = "Prevents setting a specific maintenance exclusion window end time for Datafusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceExclusionWindow.endTime == "2025-01-01T00:00:00Z"
CEL
}