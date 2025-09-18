module "org_policy_datafusion_restrict_dns_zone_prefix" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.datafusionRestrictDnsZonePrefix"
  title       = "Restrict Cloud Data Fusion DNS Peering Zone Prefix"
  description = "Ensures Cloud Data Fusion DNS peering zones follow a specific naming convention."
  expression  = <<CEL
resource.dnsZone.startsWith("gcp-private-dns-zone-")
CEL
}