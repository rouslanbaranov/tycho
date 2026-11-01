"""Static protocol-compatibility fixtures (E09-01).

Not an MCP client/server network test, auth test, or pinned-SDK conformance run.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "fixtures" / "mcp-compatibility-v1.json"


class CompatibilityFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.cases = {x["name"]: x for x in cls.data["cases"]}

    def test_distinct_revisions_explicit(self):
        self.assertEqual({x["revision"] for x in self.cases.values()},
                         {"2025-11-25", "2026-07-28"})

    def test_modern_discovery_is_not_legacy_initialize(self):
        item = self.cases["modern-discovery"]
        self.assertEqual(item["request"]["method"], "server/discover")
        self.assertEqual(item["headers"]["MCP-Protocol-Version"], "2026-07-28")
        self.assertTrue(item["does_not_need_session"])
        self.assertNotIn("Mcp-Session-Id", item["headers"])

    def test_modern_tool_call_name_and_method_mirrored(self):
        item = self.cases["modern-tool-call"]
        self.assertEqual(item["headers"]["Mcp-Method"], "tools/call")
        self.assertEqual(item["headers"]["Mcp-Name"], item["request"]["params"]["name"])
        self.assertEqual(item["method"], item["request"]["method"])

    def test_modern_request_carries_required_per_request_meta(self):
        for name in ("modern-discovery", "modern-tool-call"):
            item = self.cases[name]
            meta = item["request"]["params"]["_meta"]
            self.assertEqual(meta["io.modelcontextprotocol/protocolVersion"], "2026-07-28")
            self.assertIsInstance(meta["io.modelcontextprotocol/clientCapabilities"], dict)
            self.assertNotIn("initialize", item["method"])
            self.assertTrue(item["does_not_need_session"])

    def test_legacy_initialize_has_legacy_contract(self):
        item = self.cases["legacy-initialize"]
        self.assertEqual(item["request"]["params"]["protocolVersion"], "2025-11-25")
        self.assertEqual(item["request"]["method"], "initialize")
        self.assertFalse(item["does_not_need_session"])

    def test_sample_not_misrepresented_as_real_endpoint(self):
        self.assertIn("illustrative", self.data["requirements"][-2].lower())
        self.assertIn("No actual server", self.data["requirements"][-1])
        self.assertEqual(self.data["scope"].split(",")[0],
                         "Illustrative MCP 2026-07-28 and 2025-11-25 method/metadata shape")


if __name__ == "__main__":
    unittest.main()
