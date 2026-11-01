"""Broad regression coverage for the E18 agent-facing MCP surface.

The fixture is reused from the existing stdio adapter suite so these tests do
not need a remote service, Docker, credentials or a developer-only index.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

import mcp_server  # noqa: E402
import test_tycho_mcp_server as fixture  # noqa: E402


class E18SurfaceTests(unittest.TestCase):
    setUpClass = classmethod(fixture.McpServerTests.setUpClass.__func__)
    tearDownClass = classmethod(fixture.McpServerTests.tearDownClass.__func__)
    write_page = classmethod(fixture.McpServerTests.write_page.__func__)
    write_patterns = classmethod(
        fixture.McpServerTests.write_patterns.__func__)
    server = fixture.McpServerTests.server
    meta = fixture.McpServerTests.meta
    request = fixture.McpServerTests.request
    initialize = fixture.McpServerTests.initialize
    call = fixture.McpServerTests.call

    def search(self, **arguments):
        return self.call(self.server(), "tycho_search", arguments)

    def test_search_strict_is_default_and_has_no_weak_candidates(self):
        payload = self.search(
            query="How do I configure a specific vendor cache policy?",
            abstain=True)["structuredContent"]
        self.assertEqual(payload["mode"], "strict")
        self.assertEqual(payload["returned"], 0)
        self.assertEqual(payload["weak_returned"], 0)

    def test_search_exploratory_keeps_weak_results_separate(self):
        payload = self.search(
            query="How do I configure a specific vendor cache policy?",
            mode="exploratory", abstain=True)["structuredContent"]
        self.assertEqual(payload["status"], "no-confident-answer")
        self.assertEqual(payload["returned"], 0)
        self.assertGreater(payload["weak_returned"], 0)
        self.assertTrue(all("citation" in item
                            for item in payload["weak_results"]))

    def test_search_can_return_weak_results_in_ids_detail(self):
        payload = self.search(
            query="How do I configure a specific vendor cache policy?",
            mode="exploratory", detail="ids", abstain=True)[
                "structuredContent"]
        item = payload["weak_results"][0]
        self.assertIn("citation", item)
        self.assertIn("next_actions", item)
        self.assertNotIn("excerpt", item)
        self.assertNotIn("snippet", item)

    def test_search_default_snippets_include_excerpt_and_anchor(self):
        payload = self.search(query="zebra")["structuredContent"]
        item = payload["results"][0]
        self.assertIn("excerpt", item)
        self.assertEqual(item["snippet"], item["excerpt"])
        self.assertEqual(item["anchor"], item["section_id"])

    def test_search_has_facets_and_next_actions(self):
        payload = self.search(query="zebra")["structuredContent"]
        self.assertIn("kind", payload["facets"])
        self.assertIn("evidence_status", payload["facets"])
        self.assertTrue(payload["next_actions"])

    def test_search_budget_is_a_hard_cap(self):
        payload = self.search(query="zebra", max_chars=2048)[
            "structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 2048)
        self.assertIn("truncated", payload)

    def test_search_rejects_out_of_range_budget(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", max_chars=100)
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", max_chars=60000)

    def test_search_rejects_invalid_mode_and_detail(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", mode="loose")
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", detail="full")

    def test_search_rejects_invalid_limit(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", limit=0)
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", limit=21)

    def test_search_filters_are_reflected(self):
        payload = self.search(
            query="zebra", kind="page", topic="system-design",
            path_prefix="book/alpha")["structuredContent"]
        self.assertEqual(payload["filters"]["kind"], "page")
        self.assertEqual(payload["filters"]["topic"], "system-design")
        self.assertEqual(payload["filters"]["path_prefix"], "book/alpha")

    def test_search_all_sections_changes_scope_label(self):
        payload = self.search(query="zebra", all_sections=True)[
            "structuredContent"]
        self.assertEqual(payload["result_scope"], "all-sections")

    def test_search_snapshot_mismatch_is_explicit(self):
        payload = self.search(
            query="zebra", snapshot_id="0" * 64)["structuredContent"]
        self.assertEqual(payload["status"], "snapshot-mismatch")
        self.assertEqual(payload["requested_snapshot"], "0" * 64)
        self.assertNotEqual(payload["current_snapshot"], "0" * 64)

    def test_search_unknown_argument_is_rejected(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.search(query="zebra", unknown_field=True)

    def test_context_has_grouped_cited_sections(self):
        payload = self.call(self.server(), "tycho_context", {
            "question": "retry budget", "max_chars": 5000,
        })["structuredContent"]
        self.assertIn(payload["status"], ("ok", "no-confident-answer"))
        self.assertGreater(payload["returned_sections"], 0)
        self.assertTrue(payload["sections"])
        section = payload["sections"][0]
        for key in ("role", "citation", "section_key", "excerpt"):
            self.assertIn(key, section)
        self.assertIn("notice", payload)

    def test_context_has_explicit_gaps_for_abstention(self):
        payload = self.call(self.server(), "tycho_context", {
            "question": "nothingmatches",
            "max_chars": 5000,
        })["structuredContent"]
        self.assertEqual(payload["status"], "no-results")
        self.assertTrue(payload["gaps"])
        self.assertEqual(payload["sections"], [])

    def test_context_budget_is_enforced(self):
        payload = self.call(self.server(), "tycho_context", {
            "question": "retry budget", "max_chars": 2048,
        })["structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 2048)
        self.assertIn("truncated", payload)

    def test_context_rejects_missing_question(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_context", {})

    def test_context_rejects_invalid_budget(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_context", {
                "question": "retry", "max_chars": 100})

    def test_compare_returns_cells_and_no_winner(self):
        payload = self.call(self.server(), "tycho_compare", {
            "options": ["retry budget", "cache stampede"],
            "max_chars": 5000,
        })["structuredContent"]
        self.assertGreater(payload["returned_cells"], 0)
        self.assertNotIn("winner", payload)
        self.assertIn("notice", payload)
        self.assertTrue(payload["cells"][0]["citation"])

    def test_compare_supports_five_options(self):
        payload = self.call(self.server(), "tycho_compare", {
            "options": ["retry", "cache", "snapshot", "landing", "rollback"],
            "limit": 1, "max_chars": 8000,
        })["structuredContent"]
        self.assertEqual(payload["options"][0], "retry")
        self.assertEqual(len(payload["options"]), 5)

    def test_compare_rejects_invalid_option_sets(self):
        for options in (["one"], ["a", "a"], ["a"] * 6):
            with self.assertRaises(mcp_server.ProtocolFailure):
                self.call(self.server(), "tycho_compare", {"options": options})
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_compare", {"options": "a b"})

    def test_compare_budget_is_enforced(self):
        payload = self.call(self.server(), "tycho_compare", {
            "options": ["retry", "cache"], "max_chars": 2048,
        })["structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 2048)

    def test_outline_topic_returns_canonical_citations(self):
        payload = self.call(self.server(), "tycho_outline", {
            "topic": "synthetic", "limit": 3,
        })["structuredContent"]
        self.assertGreater(payload["returned"], 0)
        self.assertTrue(payload["entries"])
        self.assertTrue(payload["entries"][0]["citation"].startswith("book/"))
        self.assertNotIn("content", payload["entries"][0])

    def test_outline_path_prefix_and_budget(self):
        payload = self.call(self.server(), "tycho_outline", {
            "path_prefix": "book/", "limit": 2, "max_chars": 2048,
        })["structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 2048)
        self.assertLessEqual(payload["returned"], 2)

    def test_outline_requires_topic_or_prefix(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_outline", {})

    def test_outline_unknown_topic_has_gap(self):
        payload = self.call(self.server(), "tycho_outline", {
            "topic": "not-a-real-topic", "limit": 2,
        })["structuredContent"]
        self.assertEqual(payload["status"], "no-results")
        self.assertTrue(payload["gaps"])

    def test_batch_combines_reads_and_evidence(self):
        top = self.search(query="zebra", abstain=False)[
            "structuredContent"]["results"][0]
        payload = self.call(self.server(), "tycho_batch", {
            "section_keys": [top["section_key"]],
            "max_chars": 8000,
        })["structuredContent"]
        self.assertEqual(payload["returned"], 1)
        self.assertEqual(payload["errors"], 0)
        self.assertEqual(payload["status"], "ok")

    def test_batch_isolates_a_missing_section(self):
        top = self.search(query="zebra", abstain=False)[
            "structuredContent"]["results"][0]
        payload = self.call(self.server(), "tycho_batch", {
            "section_keys": [top["section_key"], "missing-section"],
            "max_chars": 8000,
        })["structuredContent"]
        self.assertEqual(payload["status"], "partial")
        self.assertEqual(payload["errors"], 1)
        self.assertEqual(payload["returned"], 2)

    def test_batch_rejects_empty_and_oversized_batches(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_batch", {})
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_batch", {
                "section_keys": ["a"] * 9})

    def test_batch_budget_is_enforced(self):
        top = self.search(query="zebra", abstain=False)[
            "structuredContent"]["results"][0]
        payload = self.call(self.server(), "tycho_batch", {
            "section_keys": [top["section_key"]], "max_chars": 2048,
        })["structuredContent"]
        self.assertLessEqual(payload["returned_chars"], 2048)

    def test_tool_surface_has_expected_members_and_annotations(self):
        self.assertEqual(len(mcp_server.TOOL_ORDER), 11)
        for name in mcp_server.TOOL_ORDER:
            spec = mcp_server.TOOL_SPECS[name]
            self.assertTrue(spec["description"])
            self.assertFalse(spec["inputSchema"]["additionalProperties"])
            self.assertTrue(spec["annotations"]["readOnlyHint"])
            self.assertFalse(spec["annotations"]["destructiveHint"])
            self.assertFalse(spec["annotations"]["openWorldHint"])

    def test_unknown_tool_is_an_error(self):
        with self.assertRaises(mcp_server.ProtocolFailure):
            self.call(self.server(), "tycho_magic", {})

    def test_server_version_is_declared(self):
        self.assertRegex(mcp_server.SERVER_VERSION, r"^\d+\.\d+\.\d+$")


if __name__ == "__main__":
    unittest.main()
