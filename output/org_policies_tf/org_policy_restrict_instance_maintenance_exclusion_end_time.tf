module "org_policy_restrict_instance_maintenance_exclusion_end_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceMaintenanceExclusionEndTime"
  title       = "Restrict Data Fusion Instance Maintenance Exclusion End Time"
  description = "Prevents setting a specific maintenance exclusion window end time for Data Fusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceExclusionWindow.endTime == "forbidden_end_time"
CEL
}