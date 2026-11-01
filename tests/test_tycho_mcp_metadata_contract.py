"""Deterministic MCP metadata/onboarding contract checks."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_server  # noqa: E402


class ContractTests(unittest.TestCase):
    def test_every_tool_has_described_input_and_output_schemas(self):
        for tool in mcp_server.tool_definitions():
            self.assertIn("outputSchema", tool, tool["name"])
            for label, schema in (("input", tool["inputSchema"]),
                                  ("output", tool["outputSchema"])):
                missing = []

                def walk(node, path):
                    if not isinstance(node, dict):
                        return
                    for name, value in node.get("properties", {}).items():
                        if "description" not in value:
                            missing.append(path + "/" + name)
                        walk(value, path + "/" + name)
                    walk(node.get("items"), path + "[]")

                walk(schema, label)
                self.assertEqual(missing, [], tool["name"] + " " + label)

    def test_describe_exposes_catalog_and_pagination(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        payload = server._tool_describe({})
        payload = payload.get("structuredContent", payload)
        meta = payload["metadata"]
        self.assertEqual(meta["version"], "tycho-mcp-contract-v1")
        self.assertIn("page", meta["kind"])
        self.assertIn("source-linked", meta["evidence_status"])
        self.assertIn("v11", meta["volume"])
        self.assertIn("pagination", meta)
        self.assertIn("frontmatter", meta)
        self.assertIn("next_offset", meta["pagination"]["page"]["outputs"])
        self.assertIn("tycho_page", meta["output_schemas"])
        self.assertIn("atlas", [x["name"] for x in meta["layers"]])
        self.assertIn("modeling-and-simulation",
                      [x["name"] for x in meta["layers"]])
        self.assertIn("offset-inside-diagram",
                      meta["errors"]["tool_execution"]["codes"])

    def test_layer_aliases_are_explicit(self):
        import section_search
        self.assertEqual(section_search.normalize_volume("atlas"), "v11")
        self.assertEqual(
            section_search.normalize_volume("modeling-and-simulation"), "v12")
        server = mcp_server.TychoMcpServer(root=ROOT)
        payload = server._tool_search({
            "query": "pattern", "volume": "modeling-and-simulation",
            "limit": 1})
        payload = payload.get("structuredContent", payload)
        self.assertEqual(payload["layer"], "modeling-and-simulation")

    def test_page_returns_frontmatter_related_and_next_offset(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        payload = server._tool_page({
            "path": "book/distributed/transactional-outbox-and-idempotency.md",
            "budget_chars": 500,
        })
        payload = payload.get("structuredContent", payload)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["frontmatter"]["id"],
                         payload["document_id"])
        self.assertIn("related_ids", payload["frontmatter"]["route_hints"])
        self.assertTrue(payload["related"])
        self.assertEqual(payload["next_offset"], 500)
        self.assertTrue(payload["truncated"])

    def test_search_exposes_summary_and_related_ids(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        payload = server._tool_search({
            "query": "transactional outbox idempotency",
            "limit": 1,
        })
        payload = payload.get("structuredContent", payload)
        result = payload["results"][0]
        self.assertTrue(result["summary"])
        self.assertTrue(result["related_ids"])


if __name__ == "__main__":
    unittest.main()
