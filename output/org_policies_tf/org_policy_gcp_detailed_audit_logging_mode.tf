module "org_policy_gcp_detailed_audit_logging_mode" {
  source      = "terraform-google-modules/org-policy/google"
  constraint  = "customConstraints/custom.gcp.detailedAuditLoggingMode"
  title       = "Detailed Audit Logging Mode for Cloud Storage"
  description = "When Detailed Audit Logging Mode is enforced, both the request and response are included in Cloud Audit Logs. Changes to this feature may take up to 10 minutes to reflect. This Org Policy is highly encouraged in coordination with Bucket Lock when seeking compliances such as SEC Rule 17a-4(f), CFTC Rule 1.31(c)-(d), and FINRA Rule 4511(c). This policy is currently only supported in Cloud Storage."
  expression  = <<CEL
resource.cel_expression_goes_here == true
CEL
}