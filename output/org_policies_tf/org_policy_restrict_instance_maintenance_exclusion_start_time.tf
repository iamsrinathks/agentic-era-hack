module "org_policy_restrict_instance_maintenance_exclusion_start_time" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.restrictInstanceMaintenanceExclusionStartTime"
  title       = "Restrict Data Fusion Instance Maintenance Exclusion Start Time"
  description = "Prevents setting a specific maintenance exclusion window start time for Data Fusion instances."
  expression  = <<CEL
resource.maintenancePolicy.maintenanceExclusionWindow.startTime == "forbidden_start_time"
CEL
}