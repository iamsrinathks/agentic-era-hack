module "org_policy_custom_labels" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.labels"
  title       = "Buckets must have a label classifying the contents of the bucket"
  description = "Newly created buckets and newly updated buckets must have the label my_annotations.data.source with the SOURCE_IMAGES, SOURCE_TEXT, or SOURCE_VIDEOS key."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE" || type == "UPDATE") && ('my_annotations.data.source' in resource.labels && resource.labels['my_annotations.data.source'] in ['SOURCE_IMAGES','SOURCE_TEXT','SOURCE_VIDEOS'])
CEL
}