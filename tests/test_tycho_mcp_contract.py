"""Contract checks for the agent-facing MCP tool surface."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))

import mcp_contract  # noqa: E402
import mcp_http_server  # noqa: E402
import mcp_server  # noqa: E402
from jsonschema import Draft202012Validator  # noqa: E402


class McpToolContractTests(unittest.TestCase):
    def test_every_tool_has_a_closed_contract(self):
        self.assertEqual(len(mcp_server.TOOL_ORDER), 11)
        for name in mcp_server.TOOL_ORDER:
            spec = mcp_server.TOOL_SPECS[name]
            self.assertTrue(spec.get("description"))
            self.assertEqual(spec["inputSchema"]["type"], "object")
            self.assertFalse(spec["inputSchema"]["additionalProperties"])
            self.assertTrue(spec["annotations"]["readOnlyHint"])
            for key in ("title", "destructiveHint", "idempotentHint",
                        "openWorldHint"):
                self.assertIn(key, spec["annotations"])

    def test_contract_document_lists_every_tool(self):
        text = (ROOT / "authoring/MCP-AGENT-TOOL-CONTRACT.md").read_text(
            encoding="utf-8")
        for name in mcp_server.TOOL_ORDER:
            self.assertIn(name, text)

    def test_output_schemas_are_valid_json_schema(self):
        for name in mcp_server.TOOL_ORDER:
            schema = mcp_contract.output_schema(name)
            Draft202012Validator.check_schema(schema)
            self.assertEqual(schema["type"], "object")

    def test_every_schema_is_external_and_loadable(self):
        for name in mcp_server.TOOL_ORDER:
            input_schema = mcp_contract.input_schema(name)
            output_schema = mcp_contract.output_schema(name)
            Draft202012Validator.check_schema(input_schema)
            Draft202012Validator.check_schema(output_schema)
            self.assertTrue(
                (ROOT / "mcp/schemas/input" / (name + ".json")).is_file())
            self.assertTrue(
                (ROOT / "mcp/schemas/output" / (name + ".json")).is_file())

    def test_instructions_are_loaded_from_markdown(self):
        onboarding = (ROOT / "mcp/INSTRUCTIONS.md").read_text(encoding="utf-8")
        self.assertIn("# Tycho MCP onboarding", onboarding)
        self.assertEqual(mcp_contract.INSTRUCTIONS, onboarding.strip())
        self.assertEqual(mcp_server.INSTRUCTIONS, onboarding.strip())

    def test_server_and_http_versions_agree(self):
        self.assertEqual(
            mcp_server.SERVER_VERSION, mcp_http_server.SERVICE_VERSION)
        self.assertRegex(mcp_server.SERVER_VERSION, r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
