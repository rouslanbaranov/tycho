"""Offline tests for the read-only MCP stdio adapter.

The suite builds a synthetic three-page book with valid strict metadata, publishes
a real section index, and exercises the modern and legacy protocol paths. It does
not test a hosted endpoint, an external SDK, authentication or answer quality.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import mcp_server  # noqa: E402
import section_fts_index  # noqa: E402

MODERN = mcp_server.MODERN_VERSION
LEGACY = mcp_server.LEGACY_VERSION


def quoted(value):
    return json.dumps(value, ensure_ascii=False)


def frontmatter(identity, kind, parent, path, title, summary,
                topic="system-design", body=""):
    parent_value = "null" if parent is None else quoted(parent)
    return (
        "---\n"
        "metadata_version: 1\n"
        "id: " + quoted(identity) + "\n"
        "kind: " + quoted(kind) + "\n"
        "parent_id: " + parent_value + "\n"
        "canonical_path: " + quoted(path) + "\n"
        "title: " + quoted(title) + "\n"
        "topic_ids: [" + quoted(topic) + "]\n"
        'perspectives: ["architecture"]\n'
        "summary: " + quoted(summary) + "\n"
        "route_hints:\n"
        '  questions: ["What does this synthetic page test?"]\n'
        "  prerequisites: []\n"
        "  related_ids: []\n"
        "  excludes: []\n"
        '  keywords: ["synthetic", "mcp"]\n'
        "evidence_scope:\n"
        "  source_ids: []\n"
        "  claim_ids: []\n"
        "  status: unknown\n"
        '  notes: "Synthetic test fixture only."\n'
        "content_review:\n"
        "  status: draft\n"
        "  reviewed_at: null\n"
        "  reviewer: null\n"
        "  proof_uri: null\n"
        'authored_at: "2026-10-23"\n'
        'updated_at: "2026-10-23"\n'
        "source_inspection_date: null\n"
        "content_verified_at: null\n"
        "---\n" + body
    )


class McpServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="tycho-mcp-fixture-")
        cls.root = Path(cls.tmp.name)
        (cls.root / "book").mkdir()
        (cls.root / "schemas").mkdir()
        (cls.root / "generated").mkdir()
        shutil.copy(
            ROOT / "schemas/document-metadata.v1.schema.json",
            cls.root / "schemas/document-metadata.v1.schema.json",
        )
        cls.write_page(
            "README.md", "tycho.book.aaaaaa", "book", None,
            "Synthetic Tycho book",
            "Synthetic book root used only for offline MCP server tests.",
            "# Synthetic book\n\nRoot overview for offline tests.\n",
        )
        cls.write_page(
            "alpha.md", "tycho.page.alphaa", "page", "tycho.book.aaaaaa",
            "Alpha search page",
            "Synthetic page about bounded retrieval and retry policy.",
            "# Alpha search page\n\nOverview discusses bounded retrieval and "
            "snapshots.\n\n## Retry budget {#retry-budget}\nRetry budget "
            "detail with token zebra.\n\n### Nested detail\nNested text stays "
            "in its parent section.\n\n## Caching\nCache stampede and "
            "invalidation notes.\n",
        )
        cls.write_page(
            "beta.md", "tycho.page.betaaa", "page", "tycho.book.aaaaaa",
            "Beta landing",
            "Synthetic page about deployment rollback and landing routes.",
            "# Beta landing\n\nDeployment rollback overview for the landing "
            "page.\n",
        )
        cls.snapshot = section_fts_index.publish(
            cls.root, full=True)["snapshot"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    @classmethod
    def write_page(cls, name, identity, kind, parent, title, summary, body):
        path = cls.root / "book" / name
        path.write_text(
            frontmatter(identity, kind, parent, "book/" + name, title,
                        summary, body=body),
            encoding="utf-8",
        )

    def server(self):
        return mcp_server.TychoMcpServer(self.root)

    def meta(self):
        return {
            mcp_server.META_VERSION: MODERN,
            mcp_server.META_CAPABILITIES: {},
        }

    def request(self, server, request_id, method, params=None):
        return server.handle({
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
            "params": {} if params is None else params,
        })

    def initialize(self, server):
        response = self.request(server, 1, "initialize", {
            "protocolVersion": LEGACY,
            "capabilities": {},
            "clientInfo": {"name": "synthetic-test", "version": "0.0.0"},
        })
        self.assertEqual(response["result"]["protocolVersion"], LEGACY)
        return server

    def call(self, server, name, arguments, request_id=20):
        response = self.request(server, request_id, "tools/call", {
            "name": name,
            "arguments": arguments,
            "_meta": self.meta(),
        })
        return response["result"]

    def test_tool_definitions_are_closed_read_only_and_private(self):
        definitions = mcp_server.tool_definitions()
        self.assertEqual(
            [item["name"] for item in definitions],
            list(mcp_server.TOOL_ORDER),
        )
        for item in definitions:
            self.assertNotIn("handler", item)
            self.assertFalse(item["inputSchema"]["additionalProperties"])
            self.assertTrue(item["annotations"]["readOnlyHint"])
            self.assertFalse(item["annotations"]["destructiveHint"])
            self.assertFalse(item["annotations"]["openWorldHint"])

    def test_legacy_initialize_and_tools_list(self):
        server = self.initialize(self.server())
        response = self.request(server, 2, "tools/list")
        self.assertNotIn("resultType", response["result"])
        self.assertEqual(
            [item["name"] for item in response["result"]["tools"]],
            list(mcp_server.TOOL_ORDER),
        )

    def test_modern_discovery_and_list_cache_fields(self):
        server = self.server()
        discovered = self.request(server, 1, "server/discover", {
            "_meta": self.meta(),
        })
        result = discovered["result"]
        self.assertEqual(result["resultType"], "complete")
        self.assertEqual(result["supportedVersions"],
                         list(mcp_server.SUPPORTED_VERSIONS))
        self.assertEqual(result["capabilities"], {"tools": {}})
        self.assertIn("instructions", result)
        self.assertIn("ttlMs", result)
        self.assertEqual(result["cacheScope"], "public")
        self.assertEqual(
            result["_meta"][mcp_server.META_SERVER]["name"],
            mcp_server.SERVER_NAME,
        )
        listed = self.request(server, 2, "tools/list", {
            "_meta": self.meta(),
        })["result"]
        self.assertEqual(listed["resultType"], "complete")
        self.assertIn("ttlMs", listed)
        self.assertEqual(listed["cacheScope"], "public")

    def test_search_returns_citation_anchor_snippet_and_snapshot(self):
        payload = self.call(self.server(), "tycho_search", {
            "query": "zebra", "limit": 2,
        })["structuredContent"]
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["returned"], 1)
        top = payload["results"][0]
        self.assertEqual(top["section_id"], "retry-budget")
        self.assertEqual(top["anchor"], "retry-budget")
        self.assertEqual(top["snippet"], top["excerpt"])
        self.assertEqual(top["citation"], "book/alpha.md#retry-budget")
        self.assertGreater(top["score"], 0)
        self.assertEqual(payload["snapshot"], self.snapshot)
        self.assertEqual(payload["content_trust"],
                         mcp_server.CONTENT_TRUST)

    def test_no_results_is_not_a_tool_error(self):
        result = self.call(self.server(), "tycho_search", {
            "query": "nothingmatches",
        })
        payload = result["structuredContent"]
        self.assertFalse(result["isError"])
        self.assertEqual(payload["status"], "no-results")
        self.assertTrue(payload["answerability"]["no_confident_answer"])
        self.assertIsNone(payload["answerability"]["answerable"])
        self.assertFalse(payload["answerability"]["confident"])

    def test_read_bounds_and_continuation(self):
        server = self.server()
        search = self.call(server, "tycho_search", {"query": "zebra"})
        key = search["structuredContent"]["results"][0]["section_key"]
        read = self.call(server, "tycho_read", {
            "section_key": key, "offset": 0, "budget_chars": 20,
        })["structuredContent"]
        self.assertEqual(read["status"], "ok")
        self.assertEqual(read["returned_chars"], 20)
        self.assertTrue(read["truncated"])
        self.assertEqual(read["next_offset"], 20)
        self.assertEqual(read["anchor"], "retry-budget")
        tail = self.call(server, "tycho_read", {
            "section_key": key,
            "offset": read["total_chars"] - 5,
            "budget_chars": 100,
        })["structuredContent"]
        self.assertEqual(tail["returned_chars"], 5)
        self.assertIsNone(tail["next_offset"])
        self.assertFalse(tail["truncated"])

    def test_page_map_and_bounds(self):
        page = self.call(self.server(), "tycho_page", {
            "path": "book/alpha.md", "offset": 0, "budget_chars": 40,
        })["structuredContent"]
        self.assertEqual(page["status"], "ok")
        self.assertEqual(page["citation"], "book/alpha.md")
        self.assertEqual(page["sections"][0]["body_offset_start"], 0)
        self.assertEqual(
            [item["section_id"] for item in page["sections"]],
            ["overview", "retry-budget", "caching"],
        )
        self.assertTrue(page["truncated"])
        self.assertEqual(page["returned_chars"], 40)
        tail = self.call(self.server(), "tycho_page", {
            "path": "book/alpha.md",
            "offset": page["total_chars"] - 5,
            "budget_chars": 100,
        })["structuredContent"]
        self.assertEqual(tail["returned_chars"], 5)
        self.assertIsNone(tail["next_offset"])

    def test_page_rejects_traversal_absolute_and_unknown(self):
        for path in (
            "../book/alpha.md",
            "/book/alpha.md",
            "book/../alpha.md",
            "book\\alpha.md",
            "book/alpha.txt",
            "book//alpha.md",
        ):
            with self.assertRaises(mcp_server.ProtocolFailure) as caught:
                self.call(self.server(), "tycho_page", {"path": path})
            self.assertEqual(caught.exception.code, -32602)
        missing = self.call(self.server(), "tycho_page", {
            "path": "book/missing.md",
        })
        self.assertTrue(missing["isError"])
        self.assertEqual(missing["structuredContent"]["status"], "not-found")

    def test_snapshot_pin_mismatch_is_explicit(self):
        result = self.call(self.server(), "tycho_search", {
            "query": "zebra", "snapshot_id": "0" * 64,
        })
        self.assertTrue(result["isError"])
        payload = result["structuredContent"]
        self.assertEqual(payload["status"], "snapshot-mismatch")
        self.assertEqual(payload["requested_snapshot"], "0" * 64)
        self.assertNotEqual(payload["current_snapshot"], "0" * 64)

    def test_unsupported_version_and_missing_metadata(self):
        server = self.server()
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(server, 1, "server/discover", {
                "_meta": {
                    mcp_server.META_VERSION: "1900-01-01",
                    mcp_server.META_CAPABILITIES: {},
                },
            })
        self.assertEqual(caught.exception.code, -32022)
        self.assertEqual(caught.exception.data["requested"], "1900-01-01")
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(server, 2, "tools/list")
        self.assertEqual(caught.exception.code, -32600)
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(server, 3, "server/discover")
        self.assertEqual(caught.exception.code, -32602)

    def test_modern_requires_client_capabilities(self):
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(self.server(), 1, "tools/list", {
                "_meta": {mcp_server.META_VERSION: MODERN},
            })
        self.assertEqual(caught.exception.code, -32602)

    def test_unknown_tool_and_unknown_argument(self):
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.call(self.server(), "missing_tool", {})
        self.assertEqual(caught.exception.code, -32602)
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.call(self.server(), "tycho_search", {
                "query": "zebra", "bogus": 1,
            })
        self.assertEqual(caught.exception.code, -32602)

    def test_ping_era_behavior(self):
        legacy = self.initialize(self.server())
        response = self.request(legacy, 2, "ping")
        self.assertEqual(response["result"], {})
        modern = self.server()
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(modern, 1, "ping", {"_meta": self.meta()})
        self.assertEqual(caught.exception.code, -32601)

    def test_evidence_requires_exactly_one_identifier(self):
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.call(self.server(), "tycho_evidence", {})
        self.assertEqual(caught.exception.code, -32602)
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.call(self.server(), "tycho_evidence", {
                "document_id": "tycho.page.alphaa",
                "claim_id": "claim.example",
            })
        self.assertEqual(caught.exception.code, -32602)

    def test_describe_reports_snapshot_counts_and_limits(self):
        payload = self.call(self.server(), "tycho_describe", {})[
            "structuredContent"]
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["counts"]["documents"], 3)
        self.assertEqual(payload["counts"]["sections"], 5)
        self.assertEqual(payload["limits"]["search_limit"], [1, 20])
        self.assertIn("tycho_page", payload["tools"])
        self.assertIn("semantic, vector or hybrid ranking",
                      payload["not_implemented"])

    def test_stdio_roundtrip(self):
        process = subprocess.Popen(
            [sys.executable, str(ROOT / "scripts/mcp_server.py"),
             "--root", str(self.root)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=str(ROOT),
        )
        try:
            def send(message):
                process.stdin.write(json.dumps(message) + "\n")
                process.stdin.flush()
                return json.loads(process.stdout.readline())

            initialized = send({
                "jsonrpc": "2.0", "id": 1, "method": "initialize",
                "params": {
                    "protocolVersion": LEGACY,
                    "capabilities": {},
                    "clientInfo": {"name": "roundtrip", "version": "0.0.0"},
                },
            })
            self.assertEqual(
                initialized["result"]["protocolVersion"], LEGACY)
            listed = send({
                "jsonrpc": "2.0", "id": 2, "method": "tools/list",
            })
            self.assertEqual(len(listed["result"]["tools"]), 5)
            called = send({
                "jsonrpc": "2.0", "id": 3, "method": "tools/call",
                "params": {
                    "name": "tycho_search",
                    "arguments": {"query": "zebra"},
                },
            })
            payload = called["result"]["structuredContent"]
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(
                payload["results"][0]["citation"],
                "book/alpha.md#retry-budget",
            )
        finally:
            process.stdin.close()
            process.wait(timeout=20)
            stderr = process.stderr.read()
            process.stdout.close()
            process.stderr.close()
        self.assertEqual(process.returncode, 0)
        self.assertNotIn("Traceback", stderr)


if __name__ == "__main__":
    unittest.main()
