module "org_policy_custom_IpFilter" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.IpFilter"
  title       = "Bucket IP filter rules must restrict all the public network"
  description = "Newly created buckets must have IP filtering and IP filtering rules must restrict all public network resources."
  expression  = <<CEL
resource.methodTypes.all(type, type == "CREATE") && (!has(resource.ipFilter) || (resource.ipFilter.mode == 'Disabled' || resource.ipFilter.publicNetworkSource.allowedIpCidrRanges.size() > 0))
CEL
}