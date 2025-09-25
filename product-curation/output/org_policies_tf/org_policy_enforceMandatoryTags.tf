module "org_policy_enforceMandatoryTags" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/enforceMandatoryTags"
  title       = "Enforce mandatory tags on AlloyDB cluster resource."
  description = "Prevent users from creation if mandatory tags are not provided. Replace YOUR_TAG_NAME with the tag name."
  expression  = <<CEL
!resource.hasDirectTagKey('YOUR_TAG_NAME')
CEL
}