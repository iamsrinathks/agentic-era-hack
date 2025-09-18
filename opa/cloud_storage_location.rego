package terraform.policies.resource_controls

import input.plan as tfplan

gcp_bucket_in_eu_region := {
  "title": "Ensure GCS Buckets are in EU Region",
  "description": "Ensure that all Google Cloud Storage buckets are provisioned in the EU region.",
  "severity": "HIGH",
  "control_id": "gcp_bucket_in_eu_region",
  "ticket_id": "456",
  "scope": "rule"
}

deny contains msg if {
  some r in tfplan.resource_changes
  r.type == "google_storage_bucket"
  not is_null(r.change.after)
  location := object.get(r.change.after, "location", "")
  not startswith(location, "eu")
  msg := sprintf("Bucket '%s' is not located in the EU region: Current location is '%s'.", [r.name, location])
}