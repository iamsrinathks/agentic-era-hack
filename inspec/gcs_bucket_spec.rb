describe google_storage_bucket(name: bucket-name) do
  it { should exist }
  its('location') { should cmp 'europe-west2'.upcase }

  its('storage_class') { should eq "STANDARD" }
  its('labels') { should include("key" => "value") }
  its('retention_policy.retention_period') { should cmp 1000 }
end

describe google_storage_bucket(name: "nonexistent") do
  it { should_not exist }
end
