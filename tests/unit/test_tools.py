# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
from unittest.mock import MagicMock

from app.agent import save_product_name
from app.subagents.security.org_policy_writer import write_org_policy_tf


def test_save_product_name() -> None:
    """Unit test for the save_product_name tool."""
    mock_tool_context = MagicMock()
    mock_tool_context.state = {}

    result = save_product_name("test_product", mock_tool_context)

    assert result == {"status": "success"}
    assert mock_tool_context.state["user:product_name"] == "test_product"


def test_write_org_policy_tf() -> None:
    """Unit test for the write_org_policy_tf tool."""
    mock_tool_context = MagicMock()
    output_dir = os.path.join(os.getcwd(), "output", "org_policies_tf")
    # Ensure the output directory is clean before the test
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    multi_file_tf_string = """
=== org_policy_one.tf ===
resource "google_organization_policy" "policy-one" {
  name   = "organizations/123456789/policies/custom.policy-one"
  parent = "organizations/123456789"
  spec {
    rules {
      allow_all = "TRUE"
    }
  }
}
=== org_policy_two.tf ===
resource "google_organization_policy" "policy-two" {
  name   = "organizations/123456789/policies/custom.policy-two"
  parent = "organizations/123456789"
  spec {
    rules {
      deny_all = "TRUE"
    }
  }
}
"""
    result = write_org_policy_tf(multi_file_tf_string, mock_tool_context)

    assert result["status"] == "complete"
    assert "SUCCESS: Wrote" in result["message"]
    assert os.path.exists(os.path.join(output_dir, "org_policy_one.tf"))
    assert os.path.exists(os.path.join(output_dir, "org_policy_two.tf"))

    with open(os.path.join(output_dir, "org_policy_one.tf")) as f:
        assert "custom.policy-one" in f.read()

    with open(os.path.join(output_dir, "org_policy_two.tf")) as f:
        assert "custom.policy-two" in f.read()

    # Clean up the created files and directory
    shutil.rmtree(output_dir)
