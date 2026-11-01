"""Offline tests for the local HTTP MCP container wrapper.

The fixture is a synthetic two-page book and a real FTS5 index. The tests use
the standard library HTTP client against a loopback server; no container,
external SDK, network service or hosted deployment is required.
"""
import hashlib
import http.client
import json
from pathlib import Path
import shutil
import sys
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))

import mcp_http_server  # noqa: E402
import mcp_server  # noqa: E402
import route_index  # noqa: E402
import section_fts_index  # noqa: E402

META = {
    mcp_http_server.META_VERSION: mcp_http_server.MODERN_VERSION,
    "io.modelcontextprotocol/clientCapabilities": {},
}
TOKEN = "test-token"


def frontmatter(identity, kind, parent, path, title, summary, body):
    parent_value = "null" if parent is None else json.dumps(parent)
    return (
        "---\n"
        "metadata_version: 1\n"
        "id: " + json.dumps(identity) + "\n"
        "kind: " + json.dumps(kind) + "\n"
        "parent_id: " + parent_value + "\n"
        "canonical_path: " + json.dumps(path) + "\n"
        "title: " + json.dumps(title) + "\n"
        'topic_ids: ["system-design"]\n'
        'perspectives: ["architecture"]\n'
        "summary: " + json.dumps(summary) + "\n"
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


class HttpMcpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="tycho-http-fixture-")
        cls.root = Path(cls.tmp.name)
        (cls.root / "book").mkdir()
        (cls.root / "schemas").mkdir()
        (cls.root / "generated").mkdir()
        shutil.copy(
            ROOT / "schemas/document-metadata.v1.schema.json",
            cls.root / "schemas/document-metadata.v1.schema.json",
        )
        (cls.root / "book" / "README.md").write_text(
            frontmatter(
                "tycho.book.aaaaaa", "book", None, "book/README.md",
                "Synthetic Tycho book",
                "Synthetic book root used only for HTTP tests.",
                "# Synthetic book\n\nOverview for HTTP tests.\n",
            ),
            encoding="utf-8",
        )
        (cls.root / "book" / "alpha.md").write_text(
            frontmatter(
                "tycho.page.alphaa", "page", "tycho.book.aaaaaa",
                "book/alpha.md", "Alpha HTTP page",
                "Synthetic HTTP search page about retry and caching.",
                "# Alpha HTTP page\n\nOverview of bounded HTTP retrieval.\n\n"
                "## Retry budget {#retry-budget}\nRetry budget detail with "
                "token zebra.\n\n## Caching\nCache stampede notes.\n",
            ),
            encoding="utf-8",
        )
        cls.snapshot = section_fts_index.publish(
            cls.root, full=True)["snapshot"]
        route_payload = route_index.canonical_scan(cls.root)
        (cls.root / "generated" / "route-index.v1.json").write_text(
            json.dumps(route_payload, sort_keys=True),
            encoding="utf-8",
        )
        cls.application = mcp_http_server.TychoHttpApplication(
            cls.root, token=TOKEN)
        cls.httpd = mcp_http_server.build_server(
            cls.application, "127.0.0.1", 0)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(
            target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.thread.join(timeout=10)
        cls.tmp.cleanup()

    def request(self, method, path, payload=None, auth=True, headers=None,
                expect_json=True):
        connection = http.client.HTTPConnection(
            "127.0.0.1", self.port, timeout=15)
        request_headers = {"Content-Type": "application/json"}
        if auth:
            request_headers["Authorization"] = "Bearer " + TOKEN
        if headers:
            request_headers.update(headers)
        body = None if payload is None else json.dumps(payload)
        connection.request(method, path, body=body, headers=request_headers)
        response = connection.getresponse()
        raw = response.read().decode("utf-8")
        connection.close()
        if not expect_json:
            return response.status, raw
        return response.status, json.loads(raw) if raw else None

    def mcp(self, request_id, method, params, headers=None):
        return self.request(
            "POST", "/mcp",
            {"jsonrpc": "2.0", "id": request_id, "method": method,
             "params": params},
            headers=headers,
        )

    def test_health_and_authentication(self):
        status, health = self.request("GET", "/health", auth=False)
        self.assertEqual(status, 200)
        self.assertEqual(health["status"], "ok")
        status, _ = self.request("GET", "/search?q=zebra", auth=False)
        self.assertEqual(status, 401)
        status, _ = self.request("POST", "/mcp", {
            "jsonrpc": "2.0", "id": 1, "method": "server/discover",
            "params": {"_meta": META},
        }, auth=False)
        self.assertEqual(status, 401)

    def test_discovery_tools_and_search_call(self):
        status, discovered = self.mcp(1, "server/discover", {"_meta": META}, {
            "MCP-Protocol-Version": mcp_http_server.MODERN_VERSION,
            "Mcp-Method": "server/discover",
        })
        self.assertEqual(status, 200)
        self.assertEqual(
            discovered["result"]["supportedVersions"],
            [mcp_http_server.MODERN_VERSION],
        )
        status, listed = self.mcp(
            2, "tools/list", {"_meta": META},
            {"Mcp-Method": "tools/list"})
        self.assertEqual(status, 200)
        self.assertEqual(len(listed["result"]["tools"]), 11)
        status, called = self.mcp(3, "tools/call", {
            "_meta": META,
            "name": "tycho_search",
            "arguments": {"query": "zebra", "limit": 2},
        }, {
            "Mcp-Method": "tools/call",
            "Mcp-Name": "tycho_search",
        })
        self.assertEqual(status, 200)
        result = called["result"]
        self.assertFalse(result["isError"])
        payload = result["structuredContent"]
        self.assertIn(
            payload["status"], ("ok", "no-results", "no-confident-answer"))
        self.assertEqual(payload["snapshot"], self.snapshot)
        if payload["returned"]:
            self.assertEqual(
                payload["results"][0]["citation"],
                "book/alpha.md#retry-budget",
            )
        status, context = self.mcp(4, "tools/call", {
            "_meta": META,
            "name": "tycho_context",
            "arguments": {"question": "retry budget", "max_chars": 4000},
        }, {
            "Mcp-Method": "tools/call",
            "Mcp-Name": "tycho_context",
        })
        self.assertEqual(status, 200)
        result = context["result"]
        self.assertFalse(result["isError"])
        bundle = result["structuredContent"]
        self.assertEqual(bundle["tool"], "tycho_context")
        self.assertIn("notice", bundle)
        self.assertLessEqual(bundle["returned_chars"], 4000)

    def test_search_book_health_and_readiness(self):
        status, search = self.request("GET", "/search?q=zebra&limit=2")
        self.assertEqual(status, 200)
        self.assertIn(
            search["status"], ("ok", "no-results", "no-confident-answer"))
        status, book = self.request(
            "GET", "/book/alpha.md", expect_json=False)
        self.assertEqual(status, 200)
        self.assertIn("# Alpha HTTP page", book)
        status, index = self.request(
            "GET", "/book", expect_json=False)
        self.assertEqual(status, 200)
        self.assertIn("<title>Tycho book</title>", index)
        status, ready = self.request("GET", "/ready", auth=False)
        self.assertEqual(status, 200)
        self.assertEqual(ready["snapshot"], self.snapshot)
        status, _ = self.request("GET", "/book/%2e%2e/schemas/x.json")
        self.assertIn(status, (400, 404))

    def test_search_modes_and_budget(self):
        status, payload = self.request(
            "GET",
            "/search?q=How+do+I+configure+a+specific+vendor+cache+policy"
            "&mode=exploratory&detail=ids",
        )
        self.assertEqual(status, 200)
        self.assertEqual(payload["mode"], "exploratory")
        self.assertEqual(payload["detail"], "ids")
        self.assertIn("weak_results", payload)
        self.assertIn("next_actions", payload)
        status, payload = self.request(
            "GET",
            "/search?q=vendor+cache+policy&mode=exploratory"
            "&detail=ids&max_chars=1200",
        )
        self.assertEqual(status, 200)
        self.assertLessEqual(payload["returned_chars"], 1200)
        status, _ = self.request("GET", "/search?q=zebra&mode=invalid")
        self.assertEqual(status, 400)

    def test_protocol_and_header_errors(self):
        status, payload = self.request("POST", "/mcp", None)
        self.assertEqual(status, 400)
        self.assertEqual(payload["error"]["code"], -32700)
        status, payload = self.request(
            "POST", "/mcp",
            {"jsonrpc": "2.0", "id": 4, "method": "tools/list",
             "params": {"_meta": META}},
            headers={"Mcp-Method": "tools/call"},
        )
        self.assertEqual(status, 400)
        self.assertEqual(payload["error"]["code"], -32020)
        status, payload = self.request(
            "POST", "/mcp",
            {"jsonrpc": "2.0", "id": 5, "method": "initialize",
             "params": {"protocolVersion": "2025-11-25"}},
        )
        self.assertEqual(status, 400)
        self.assertEqual(payload["error"]["code"], -32601)
        status, _ = self.request("GET", "/missing")
        self.assertEqual(status, 404)

    def test_contract_version_and_tool_list(self):
        status, health = self.request("GET", "/health", auth=False)
        self.assertEqual(status, 200)
        self.assertEqual(health["version"], mcp_http_server.SERVICE_VERSION)
        status, listed = self.mcp(
            20, "tools/list", {"_meta": META},
            {"Mcp-Method": "tools/list"})
        self.assertEqual(status, 200)
        names = [tool["name"] for tool in listed["result"]["tools"]]
        self.assertEqual(names, list(mcp_server.TOOL_ORDER))
        for tool in listed["result"]["tools"]:
            self.assertFalse(tool["inputSchema"]["additionalProperties"])
            self.assertTrue(tool["annotations"]["readOnlyHint"])

    def test_context_compare_outline_and_batch_over_http(self):
        status, context = self.mcp(21, "tools/call", {
            "_meta": META,
            "name": "tycho_context",
            "arguments": {"question": "retry budget", "max_chars": 4000},
        }, {"Mcp-Method": "tools/call", "Mcp-Name": "tycho_context"})
        self.assertEqual(status, 200)
        self.assertEqual(
            context["result"]["structuredContent"]["tool"], "tycho_context")

        status, compare = self.mcp(22, "tools/call", {
            "_meta": META,
            "name": "tycho_compare",
            "arguments": {"options": ["retry", "cache"]},
        }, {"Mcp-Method": "tools/call", "Mcp-Name": "tycho_compare"})
        self.assertEqual(status, 200)
        self.assertNotIn(
            "winner", compare["result"]["structuredContent"])

        status, outline = self.mcp(23, "tools/call", {
            "_meta": META,
            "name": "tycho_outline",
            "arguments": {"topic": "synthetic", "limit": 2},
        }, {"Mcp-Method": "tools/call", "Mcp-Name": "tycho_outline"})
        self.assertEqual(status, 200)
        self.assertIn(
            "entries", outline["result"]["structuredContent"])

        status, search = self.request("GET", "/search?q=zebra&abstain=false")
        key = search["results"][0]["section_key"]
        status, batch = self.mcp(24, "tools/call", {
            "_meta": META,
            "name": "tycho_batch",
            "arguments": {"section_keys": [key]},
        }, {"Mcp-Method": "tools/call", "Mcp-Name": "tycho_batch"})
        self.assertEqual(status, 200)
        self.assertEqual(
            batch["result"]["structuredContent"]["returned"], 1)

    def test_search_detail_ids_and_validation(self):
        status, payload = self.request(
            "GET", "/search?q=zebra&detail=ids&max_chars=2048")
        self.assertEqual(status, 200)
        self.assertLessEqual(payload["returned_chars"], 2048)
        if payload["results"]:
            self.assertNotIn("excerpt", payload["results"][0])
        status, _ = self.request("GET", "/search?q=zebra&detail=full")
        self.assertEqual(status, 400)
        status, _ = self.request("GET", "/search?q=zebra&max_chars=100")
        self.assertEqual(status, 400)


if __name__ == "__main__":
    unittest.main()
