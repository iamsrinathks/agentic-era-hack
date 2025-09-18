package terraform.policies.controls

import test.functions
import input.plan as tfplan

gcp_cloud_storage_labels := {
  "title": "gcp_cloud_storage_labels",
  "description": "ensure labels are set on the google cloud storage bucket",
  "severity": "HIGH",
  "control_id": "gcp_cloud_storage_labels",
  "ticket_id": "123",
  "scope": "rule"
}

deny contains msg if {
  exception_list := functions.load_exceptions(gcp_cloud_storage_labels.control_id)
  some a in tfplan.resource_changes
  a.type == "google_storage_bucket"
  not is_null(a.change.after)
  name := a.name
  address := a.address
  labels := object.get(a.change.after, "labels", {})
  errors := functions.validate_labels_ids(labels)
  count(errors) > 0
  not functions.check_exceptions(a.name, exception_list)
  msg := sprintf("Bucket %s at %s is missing mandatory labels.", [name, address])
}