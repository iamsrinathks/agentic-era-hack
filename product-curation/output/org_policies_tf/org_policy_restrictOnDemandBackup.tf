module "org_policy_restrictOnDemandBackup" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/restrictOnDemandBackup"
  title       = "Restrict taking on-demand backup of certain clusters"
  description = "Prevent users from taking on-demand backups for certain clusters. Replace YOUR_CLUSTER_NAME with the cluster name."
  expression  = <<CEL
resource.type == 'ON_DEMAND' && resource.clusterName.contains('YOUR_CLUSTER_NAME')
CEL
}