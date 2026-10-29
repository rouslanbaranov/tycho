"""Offline tests for the read-only MCP stdio adapter.

The suite builds a synthetic three-page book with valid strict metadata, publishes
a real section index, and exercises the modern and legacy protocol paths. It does
not test a hosted endpoint, an external SDK, authentication or answer quality.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import mcp_server  # noqa: E402
import route_index  # noqa: E402
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
        '  keywords: ["synthetic", "mcp", "quasar"]\n'
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
        cls.external = tempfile.TemporaryDirectory(
            prefix="tycho-mcp-log-")
        cls.log_dir = Path(cls.external.name)
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
        route_payload = route_index.canonical_scan(cls.root)
        (cls.root / "generated" / "route-index.v1.json").write_text(
            json.dumps(route_payload, sort_keys=True),
            encoding="utf-8",
        )
        cls.write_patterns()

    @classmethod
    def write_patterns(cls):
        directory = cls.root / "edition" / "patterns"
        directory.mkdir(parents=True)
        registry = {
            "schema_version": 1,
            "registry_version": "test-0.1",
            "edition_version": "test",
            "status": "draft",
            "updated_at": "2026-10-23",
            "catalog": {"entry_count": 2},
            "atlas": {"volume_code": "V11"},
            "families": [
                {
                    "id": "family-a",
                    "number": 1,
                    "title": "Family A",
                    "chapter": "V11/C01",
                    "chapter_path": "book/volumes/v11-pattern-atlas",
                    "pattern_ids": ["tycho.pattern.alpha-pattern"],
                },
                {
                    "id": "family-b",
                    "number": 2,
                    "title": "Family B",
                    "chapter": "V11/C02",
                    "chapter_path": "book/volumes/v11-pattern-atlas",
                    "pattern_ids": ["tycho.pattern.beta-pattern"],
                },
            ],
            "patterns": [
                {
                    "id": "tycho.pattern.alpha-pattern",
                    "catalog_name": "Alpha pattern",
                    "catalog_order": 1,
                    "family": "family-a",
                    "kind": "architecture-style",
                    "priority": "core",
                    "catalog_problem": (
                        "Separate alpha concerns from beta concerns"),
                    "aliases": ["Alpha"],
                    "relations": [],
                    "atlas_section": "alpha-pattern",
                    "technical_owner": {
                        "document_id": "tycho.page.alphaa",
                        "path": "book/alpha.md",
                        "anchor": "retry-budget",
                        "state": "partial-bounded",
                    },
                    "atlas_owner": {
                        "chapter": "V11/C01",
                        "section": "alpha-pattern",
                        "state": "partial-bounded",
                    },
                    "coverage": {
                        "technical": "partial-bounded",
                        "decision": "partial-bounded",
                        "overall": "partial-bounded",
                    },
                    "confidence": "medium",
                    "source_units": [],
                    "review_status": "self-checked",
                    "notes": "Synthetic pattern fixture.",
                },
                {
                    "id": "tycho.pattern.beta-pattern",
                    "catalog_name": "Beta pattern",
                    "catalog_order": 2,
                    "family": "family-b",
                    "kind": "resilience",
                    "priority": "advanced",
                    "catalog_problem": "Handle beta failures",
                    "aliases": ["Beta"],
                    "relations": [],
                    "atlas_section": "beta-pattern",
                    "technical_owner": {
                        "document_id": "tycho.page.betaaa",
                        "path": "book/beta.md",
                        "anchor": "overview",
                        "state": "partial-bounded",
                    },
                    "atlas_owner": {
                        "chapter": "V11/C02",
                        "section": "beta-pattern",
                        "state": "partial-bounded",
                    },
                    "coverage": {
                        "technical": "partial-bounded",
                        "decision": "partial-bounded",
                        "overall": "partial-bounded",
                    },
                    "confidence": "low",
                    "source_units": [],
                    "review_status": "self-checked",
                    "notes": "Synthetic pattern fixture.",
                },
            ],
            "source_policy": {},
            "review": {},
        }
        cards = {
            "schema_version": 1,
            "batches": [
                {
                    "id": "test-batch",
                    "issue": 1,
                    "chapter": "V11/C01",
                    "status": "self-checked",
                    "entries": [
                        {
                            "pattern_id": "tycho.pattern.alpha-pattern",
                            "atlas_section": "alpha-pattern",
                            "owner_path": "book/alpha.md",
                            "owner_anchor": "retry-budget",
                            "ledger_record": "read.test",
                            "owner_state": "linked",
                        },
                    ],
                },
            ],
        }
        (directory / "registry.v1.json").write_text(
            json.dumps(registry, indent=1), encoding="utf-8")
        (directory / "card-batches.v1.json").write_text(
            json.dumps(cards, indent=1), encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.external.cleanup()
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
        if name == "tycho_search":
            arguments = {"abstain": False, **arguments}
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

    def test_best_retrieval_mode_is_opt_in(self):
        base = mcp_server.section_search.search(
            self.root, "zebra", limit=1, abstain=False)
        fake = {"status": "ok", "retrieval_mode": "best",
                "snapshot": base["snapshot"], "rerank": "reranked",
                "results": base["results"]}
        with patch.object(mcp_server.best_search, "best_search",
                          return_value=fake):
            payload = self.call(self.server(), "tycho_search", {
                "query": "zebra", "retrieval_mode": "best",
            })["structuredContent"]
        self.assertEqual(payload["retrieval_mode"], "best")
        self.assertEqual(payload["rerank"], "reranked")
        self.assertEqual(payload["results"][0]["section_id"],
                         "retry-budget")

    def test_best_mode_default_and_filter_guard(self):
        schema = mcp_server.search_schema()
        self.assertEqual(
            schema["properties"]["retrieval_mode"]["default"], "bm25")
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_search", {
                "query": "zebra", "retrieval_mode": "best",
                "kind": "page",
            })

    def test_h3_match_maps_to_parent_and_is_not_readable(self):
        payload = self.call(self.server(), "tycho_search", {
            "query": "nested text", "limit": 2,
        })["structuredContent"]
        top = payload["results"][0]
        self.assertEqual(top["section_id"], "retry-budget")
        self.assertEqual(top["matched_passage_heading"], "Nested detail")
        self.assertIn("~", top["matched_passage_key"])
        self.assertEqual(top["citation"], "book/alpha.md#retry-budget")
        read = self.call(self.server(), "tycho_read", {
            "section_key": top["matched_passage_key"],
        })
        self.assertTrue(read["isError"])

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

    def test_calibrated_abstention_is_not_a_tool_error(self):
        result = self.call(self.server(), "tycho_search", {
            "query": "How do I configure a specific vendor cache policy?",
            "abstain": True,
        })
        payload = result["structuredContent"]
        self.assertFalse(result["isError"])
        self.assertEqual(payload["status"], "no-confident-answer")
        self.assertEqual(payload["returned"], 0)
        self.assertTrue(payload["answerability"]["no_confident_answer"])
        self.assertEqual(payload["answerability"]["basis"],
                         "evidence-score-threshold")

    def test_exploratory_mode_returns_separate_weak_results(self):
        payload = self.call(self.server(), "tycho_search", {
            "query": "How do I configure a specific vendor cache policy?",
            "mode": "exploratory",
            "detail": "ids",
            "limit": 2,
            "abstain": True,
        })["structuredContent"]
        self.assertEqual(payload["status"], "no-confident-answer")
        self.assertEqual(payload["returned"], 0)
        self.assertGreater(payload["weak_returned"], 0)
        self.assertTrue(payload["answerability"]["no_confident_answer"])
        weak = payload["weak_results"][0]
        self.assertIn("citation", weak)
        self.assertIn("section_key", weak)
        self.assertNotIn("excerpt", weak)
        self.assertTrue(weak["next_actions"])
        self.assertEqual(payload["content_trust"],
                         mcp_server.CONTENT_TRUST)

    def test_metadata_expansion_returns_weak_candidates(self):
        payload = self.call(self.server(), "tycho_search", {
            "query": "quasar",
            "mode": "exploratory",
            "limit": 2,
        })["structuredContent"]
        self.assertEqual(payload["status"], "no-confident-answer")
        self.assertTrue(payload["metadata_expanded"])
        self.assertGreater(payload["weak_returned"], 0)
        self.assertEqual(
            payload["weak_results"][0]["match_source"], "route-metadata")

    def test_batch_read_and_evidence_isolate_failures(self):
        search = self.call(self.server(), "tycho_search", {
            "query": "zebra", "abstain": False})["structuredContent"]
        top = search["results"][0]
        payload = self.call(self.server(), "tycho_batch", {
            "section_keys": [top["section_key"], "missing-section"],
            "document_ids": [top["document_id"]],
            "max_chars": 8000,
        })["structuredContent"]
        self.assertEqual(payload["tool"], "tycho_batch")
        self.assertEqual(payload["returned"], 3)
        self.assertEqual(payload["status"], "partial")
        self.assertGreaterEqual(payload["errors"], 1)
        self.assertTrue(payload["notice"])

    def test_outline_returns_canonical_paths_without_full_text(self):
        payload = self.call(self.server(), "tycho_outline", {
            "topic": "synthetic",
            "limit": 3,
            "max_chars": 5000,
        })["structuredContent"]
        self.assertEqual(payload["tool"], "tycho_outline")
        self.assertGreater(payload["returned"], 0)
        self.assertLessEqual(payload["returned_chars"], 5000)
        self.assertTrue(payload["entries"])
        self.assertIn("citation", payload["entries"][0])
        self.assertNotIn("content", payload["entries"][0])
        self.assertIn("notice", payload)

    def test_compare_returns_cited_cells_without_winner(self):
        payload = self.call(self.server(), "tycho_compare", {
            "options": ["retry budget", "cache stampede"],
            "max_chars": 5000,
        })["structuredContent"]
        self.assertEqual(payload["tool"], "tycho_compare")
        self.assertGreater(payload["returned_cells"], 0)
        self.assertLessEqual(payload["returned_chars"], 5000)
        self.assertTrue(payload["cells"])
        self.assertIn("notice", payload)
        self.assertNotIn("winner", payload)
        self.assertIn("citation", payload["cells"][0])

    def test_context_bundle_is_extractive_and_bounded(self):
        payload = self.call(self.server(), "tycho_context", {
            "question": "retry budget",
            "max_chars": 5000,
        })["structuredContent"]
        self.assertEqual(payload["tool"], "tycho_context")
        self.assertGreater(payload["returned_sections"], 0)
        self.assertLessEqual(payload["returned_chars"], 5000)
        self.assertTrue(payload["sections"])
        section = payload["sections"][0]
        self.assertIn("citation", section)
        self.assertIn("role", section)
        self.assertIn("notice", payload)
        self.assertNotIn("answer", payload)
        self.assertNotIn("verdict", payload)

    def test_search_budget_returns_bounded_payload(self):
        payload = self.call(self.server(), "tycho_search", {
            "query": "zebra",
            "limit": 5,
            "max_chars": 1200,
        })["structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 1200)
        self.assertTrue(payload["truncated"])
        self.assertGreaterEqual(payload["returned"], 0)

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
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.call(self.server(), "tycho_page", {
                "path": "book/alpha.md", "offset": 10 ** 9,
            })
        self.assertEqual(caught.exception.code, -32602)

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

    def test_patterns_list_filter_and_pagination(self):
        server = self.server()
        payload = self.call(server, "tycho_patterns", {})[
            "structuredContent"]
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["total"], 2)
        self.assertEqual(payload["returned"], 2)
        self.assertEqual(payload["registry_entries"], 2)
        self.assertEqual(payload["coverage_summary"],
                         {"partial-bounded": 2})
        self.assertEqual(
            payload["sufficiency"]["sufficient_entries"], 0)
        self.assertEqual(
            payload["sufficiency"]["registry_status"], "draft")
        self.assertEqual(payload["citation_scheme"],
                         mcp_server.PATTERN_CITATION_SCHEME)
        self.assertEqual(
            [item["pattern_id"] for item in payload["patterns"]],
            ["tycho.pattern.alpha-pattern",
             "tycho.pattern.beta-pattern"],
        )
        self.assertEqual(payload["patterns"][0]["citation_scheme"],
                         mcp_server.PATTERN_CITATION_SCHEME)
        self.assertEqual(payload["patterns"][0]["source_units"], [])
        filtered = self.call(server, "tycho_patterns", {
            "family": "family-b",
        })["structuredContent"]
        self.assertEqual(filtered["total"], 1)
        self.assertEqual(filtered["patterns"][0]["pattern_id"],
                         "tycho.pattern.beta-pattern")
        searched = self.call(server, "tycho_patterns", {
            "query": "alpha",
        })["structuredContent"]
        self.assertEqual(searched["total"], 1)
        self.assertEqual(searched["patterns"][0]["pattern_id"],
                         "tycho.pattern.alpha-pattern")
        first = self.call(server, "tycho_patterns", {
            "limit": 1,
        })["structuredContent"]
        self.assertTrue(first["truncated"])
        self.assertEqual(first["next_offset"], 1)
        second = self.call(server, "tycho_patterns", {
            "limit": 1, "offset": 1,
        })["structuredContent"]
        self.assertFalse(second["truncated"])
        self.assertEqual(second["patterns"][0]["pattern_id"],
                         "tycho.pattern.beta-pattern")
        past = self.call(server, "tycho_patterns", {
            "offset": 99,
        })["structuredContent"]
        self.assertEqual(past["status"], "ok")
        self.assertEqual(past["returned"], 0)
        self.assertEqual(past["total"], 2)

    def test_pattern_get_returns_card_owner_and_coverage(self):
        payload = self.call(self.server(), "tycho_pattern", {
            "pattern_id": "tycho.pattern.alpha-pattern",
        })["structuredContent"]
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["pattern"]["id"],
                         "tycho.pattern.alpha-pattern")
        self.assertEqual(payload["family"]["title"], "Family A")
        self.assertEqual(payload["card"]["ledger_record"], "read.test")
        self.assertEqual(payload["cards_status"], "ok")
        self.assertEqual(payload["citation"],
                         "book/alpha.md#retry-budget")
        self.assertEqual(payload["citation_scheme"],
                         mcp_server.PATTERN_CITATION_SCHEME)
        self.assertEqual(payload["owner_read"],
                         {"tool": "tycho_page",
                          "arguments": {"path": "book/alpha.md"}})
        self.assertEqual(payload["sufficiency"]["coverage_state"],
                         "partial-bounded")
        self.assertFalse(payload["sufficiency"]["sufficient"])
        self.assertEqual(payload["pattern"]["source_units"], [])
        missing = self.call(self.server(), "tycho_pattern", {
            "pattern_id": "tycho.pattern.missing-pattern",
        })
        self.assertTrue(missing["isError"])
        self.assertEqual(missing["structuredContent"]["status"], "not-found")

    def test_pattern_registry_snapshot_mismatch(self):
        server = self.server()
        listed = self.call(server, "tycho_patterns", {})[
            "structuredContent"]
        snapshot = listed["registry_snapshot"]
        mismatch = self.call(server, "tycho_patterns", {
            "registry_snapshot_id": "0" * 64,
        })
        self.assertTrue(mismatch["isError"])
        payload = mismatch["structuredContent"]
        self.assertEqual(payload["status"], "snapshot-mismatch")
        self.assertEqual(payload["requested_registry_snapshot"], "0" * 64)
        self.assertEqual(payload["current_registry_snapshot"], snapshot)

    def test_query_log_is_opt_in_and_search_only(self):
        log_path = self.log_dir / "queries.jsonl"
        if log_path.exists():
            log_path.unlink()
        server = mcp_server.TychoMcpServer(
            self.root, query_log=log_path)
        first = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(first["structuredContent"]["query_log"], "recorded")
        second = self.call(server, "tycho_search", {
            "query": "nothingmatches",
        })
        self.assertEqual(second["structuredContent"]["query_log"], "recorded")
        self.call(server, "tycho_read", {
            "section_key": "tycho.page.alphaa#retry-budget",
        })
        lines = [
            json.loads(line) for line in log_path.read_text(
                encoding="utf-8").splitlines()
        ]
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0]["tool"], "tycho_search")
        self.assertEqual(lines[0]["query_sha256"],
                         hashlib.sha256(b"zebra").hexdigest())
        self.assertNotIn("query", lines[0])
        self.assertEqual(lines[1]["status"], "no-results")
        self.assertNotIn("clientInfo", lines[0])
        self.assertNotIn("ip", lines[0])
        self.assertNotIn("request_id", lines[0])
        plain = self.call(self.server(), "tycho_search", {
            "query": "zebra",
        })["structuredContent"]
        self.assertNotIn("query_log", plain)

    def test_query_log_raw_is_explicit_opt_in(self):
        log_path = self.log_dir / "raw.jsonl"
        if log_path.exists():
            log_path.unlink()
        server = mcp_server.TychoMcpServer(
            self.root, query_log=log_path, query_log_raw=True)
        self.call(server, "tycho_search", {"query": "zebra"})
        record = json.loads(log_path.read_text(encoding="utf-8"))
        self.assertEqual(record["query"], "zebra")
        self.assertNotIn("query_sha256", record)

    def test_query_log_failure_does_not_break_search(self):
        log_path = self.log_dir / "missing" / "queries.jsonl"
        server = mcp_server.TychoMcpServer(
            self.root, query_log=log_path)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertFalse(result["isError"])
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")

    def test_query_log_rejects_root_protected_hardlink_and_special(self):
        protected = self.root / "book" / "queries.jsonl"
        server = mcp_server.TychoMcpServer(
            self.root, query_log=protected)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")
        self.assertFalse(protected.exists())

        readme = self.root / "book" / "README.md"
        original = readme.read_text(encoding="utf-8")
        server = mcp_server.TychoMcpServer(
            self.root, query_log=readme)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")
        self.assertEqual(readme.read_text(encoding="utf-8"), original)

        git_dir = self.root / ".git"
        git_dir.mkdir()
        config = git_dir / "config"
        config.write_text("x", encoding="utf-8")
        server = mcp_server.TychoMcpServer(
            self.root, query_log=config)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")
        self.assertEqual(config.read_text(encoding="utf-8"), "x")

        root_log = self.root / "queries.jsonl"
        server = mcp_server.TychoMcpServer(
            self.root, query_log=root_log)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")
        self.assertFalse(root_log.exists())

        directory = self.log_dir / "log-dir"
        directory.mkdir()
        server = mcp_server.TychoMcpServer(
            self.root, query_log=directory)
        result = self.call(server, "tycho_search", {"query": "zebra"})
        self.assertEqual(
            result["structuredContent"]["query_log"], "not-available")

        target = self.log_dir / "target.jsonl"
        target.write_text("", encoding="utf-8")
        link = self.log_dir / "log-link.jsonl"
        try:
            link.symlink_to(target)
        except OSError:
            link = None
        if link is not None:
            server = mcp_server.TychoMcpServer(
                self.root, query_log=link)
            result = self.call(server, "tycho_search", {"query": "zebra"})
            self.assertEqual(
                result["structuredContent"]["query_log"], "not-available")
            self.assertEqual(target.read_text(encoding="utf-8"), "")

        alpha = self.root / "book" / "alpha.md"
        before = alpha.read_text(encoding="utf-8")
        hardlink = self.log_dir / "hardlink.jsonl"
        try:
            os.link(alpha, hardlink)
        except OSError:
            hardlink = None
        if hardlink is not None:
            server = mcp_server.TychoMcpServer(
                self.root, query_log=hardlink)
            result = self.call(server, "tycho_search", {"query": "zebra"})
            self.assertEqual(
                result["structuredContent"]["query_log"], "not-available")
            self.assertEqual(alpha.read_text(encoding="utf-8"), before)

        fifo = self.log_dir / "fifo.jsonl"
        try:
            os.mkfifo(fifo)
        except OSError:
            fifo = None
        if fifo is not None:
            server = mcp_server.TychoMcpServer(
                self.root, query_log=fifo)
            result = self.call(server, "tycho_search", {"query": "zebra"})
            self.assertEqual(
                result["structuredContent"]["query_log"], "not-available")

    def test_stdio_protocol_error_responses(self):
        stdin = io.StringIO("{bad\n[]\n" + "x" * 1000001 + "\n")
        stdout = io.StringIO()
        mcp_server.serve(self.server(), stdin=stdin, stdout=stdout)
        responses = [
            json.loads(line) for line in stdout.getvalue().splitlines()
        ]
        self.assertEqual(
            [response["error"]["code"] for response in responses],
            [-32700, -32600, -32700],
        )

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

    def test_legacy_progress_meta_is_not_modern(self):
        server = self.initialize(self.server())
        response = self.request(server, 2, "tools/call", {
            "name": "tycho_search",
            "arguments": {"query": "zebra", "abstain": False},
            "_meta": {"progressToken": "p-1"},
        })
        result = response["result"]
        self.assertFalse(result["isError"])
        self.assertEqual(
            result["structuredContent"]["status"], "ok")

        fresh = self.server()
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(fresh, 1, "tools/call", {
                "name": "tycho_search",
                "arguments": {"query": "zebra"},
                "_meta": {"progressToken": "p-1"},
            })
        self.assertEqual(caught.exception.code, -32602)

    def test_modern_tools_call_envelope(self):
        response = self.request(self.server(), 1, "tools/call", {
            "_meta": self.meta(),
            "name": "tycho_search",
            "arguments": {"query": "zebra"},
        })
        result = response["result"]
        self.assertEqual(result["resultType"], "complete")
        self.assertEqual(
            result["_meta"][mcp_server.META_SERVER]["name"],
            mcp_server.SERVER_NAME)
        self.assertIn("content", result)
        self.assertIn("structuredContent", result)
        self.assertFalse(result["isError"])

    def test_notifications_produce_no_response(self):
        stdin = io.StringIO(
            '{"jsonrpc":"2.0","method":"notifications/initialized"}\n'
            '{"jsonrpc":"2.0","method":"notifications/cancelled",'
            '"params":[]}\n')
        stdout = io.StringIO()
        mcp_server.serve(self.server(), stdin=stdin, stdout=stdout)
        self.assertEqual(stdout.getvalue(), "")

    def test_page_hash_reconstruction_and_symlink_refusals(self):
        server = self.server()
        db, manifest = server.open_snapshot()
        try:
            rows = db.execute(
                "SELECT section_key,document_id,section_id,path,heading,"
                "heading_level,title,kind,evidence_status,content,char_start,"
                "char_end,document_sha256 FROM sections WHERE path = ? "
                "ORDER BY char_start",
                ("book/alpha.md",),
            ).fetchall()
        finally:
            db.close()
        self.assertGreaterEqual(len(rows), 2)
        source = self.root / "book" / "alpha.md"
        original = source.read_text(encoding="utf-8")
        try:
            source.write_text(
                original + "\n<!-- changed -->\n", encoding="utf-8")
            changed = server.page_payload(
                rows, manifest, "book/alpha.md", 0, 10, False)
            self.assertEqual(changed["status"], "snapshot-mismatch")
        finally:
            source.write_text(original, encoding="utf-8")
        broken = [dict(row) for row in rows]
        broken[1]["char_start"] += 1
        no_reconstruction = server.page_payload(
            broken, manifest, "book/alpha.md", 0, 10, False)
        self.assertEqual(no_reconstruction["status"], "not-available")
        link = self.root / "book" / "link.md"
        link.symlink_to(source)
        try:
            link_rows = [dict(row) for row in rows]
            for row in link_rows:
                row["path"] = "book/link.md"
            symlinked = server.page_payload(
                link_rows, manifest, "book/link.md", 0, 10, False)
            self.assertEqual(symlinked["status"], "not-available")
        finally:
            link.unlink()

    def test_registry_failure_is_path_free(self):
        server = mcp_server.TychoMcpServer(
            self.root,
            pattern_registry=self.root / "missing-registry.json",
        )
        result = self.call(server, "tycho_patterns", {})
        payload = result["structuredContent"]
        self.assertEqual(payload["status"], "not-available")
        self.assertNotIn(str(self.root), payload["error"])

    def test_legacy_version_and_cursor_rejections(self):
        fresh = self.server()
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(fresh, 1, "initialize", {
                "protocolVersion": "1900-01-01",
                "capabilities": {},
            })
        self.assertEqual(caught.exception.code, -32602)
        self.assertEqual(
            caught.exception.data["supported"], [mcp_server.LEGACY_VERSION])
        self.assertEqual(caught.exception.data["requested"], "1900-01-01")
        legacy = self.initialize(self.server())
        with self.assertRaises(mcp_server.ProtocolFailure) as caught:
            self.request(legacy, 2, "tools/list", {"cursor": "next"})
        self.assertEqual(caught.exception.code, -32602)

    def test_evidence_wrapper_binds_snapshot_and_trust(self):
        fake = {"status": "ok", "search_snapshot": self.snapshot}
        with patch.object(
                mcp_server.section_search, "evidence", return_value=fake):
            result = self.call(self.server(), "tycho_evidence", {
                "document_id": "tycho.page.alphaa",
            })
        payload = result["structuredContent"]
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["content_trust"],
                         mcp_server.CONTENT_TRUST)
        self.assertEqual(payload["tool"], "tycho_evidence")
        with patch.object(
                mcp_server.section_search, "evidence", return_value=fake):
            mismatch = self.call(self.server(), "tycho_evidence", {
                "document_id": "tycho.page.alphaa",
                "snapshot_id": "0" * 64,
            })
        self.assertTrue(mismatch["isError"])
        self.assertEqual(
            mismatch["structuredContent"]["status"], "snapshot-mismatch")

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
        self.assertEqual(payload["limits"]["patterns_limit"], [1, 50])
        self.assertIn("tycho_page", payload["tools"])
        self.assertIn("tycho_patterns", payload["tools"])
        self.assertEqual(payload["pattern_registry"]["status"], "ok")
        self.assertEqual(payload["pattern_registry"]["entries"], 2)
        self.assertEqual(payload["query_logging"], "disabled")
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
            self.assertEqual(len(listed["result"]["tools"]), 11)
            called = send({
                "jsonrpc": "2.0", "id": 3, "method": "tools/call",
                "params": {
                    "name": "tycho_search",
                    "arguments": {"query": "zebra", "abstain": False},
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
