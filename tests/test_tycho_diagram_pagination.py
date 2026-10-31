"""Diagram-safe pagination contract."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_server  # noqa: E402
import section_search  # noqa: E402

FENCE = chr(96) * 3


def sample():
    return ("before\n" + FENCE + "mermaid\nsequenceDiagram\n"
            "  A->>B: " + "x" * 80 + "\n" + FENCE + "\nafter\n")


class DiagramPaginationTests(unittest.TestCase):
    def test_ranges_and_budget_overrun(self):
        text = sample()
        ranges = section_search.diagram_ranges(text)
        self.assertEqual(len(ranges), 1)
        start, end = ranges[0]
        first = section_search.paginate_text(text, 0, 10)
        self.assertEqual(first["end"], end)
        self.assertGreater(first["overrun"], 0)
        self.assertTrue(first["diagram_completed"])
        self.assertTrue(text[:first["end"]].endswith(FENCE + "\n"))

    def test_manual_offset_inside_diagram_is_error(self):
        text = sample()
        start, end = section_search.diagram_ranges(text)[0]
        with self.assertRaises(section_search.SearchError) as caught:
            section_search.paginate_text(text, start + 1, 10)
        self.assertEqual(caught.exception.status, "offset-inside-diagram")
        message = str(caught.exception)
        self.assertIn("diagram_start=", message)
        self.assertIn("diagram_end=", message)
        self.assertIn("suggested_offset=", message)

    def test_sequential_slices_have_no_gap(self):
        text = sample()
        offset = 0
        chunks = []
        while offset < len(text):
            info = section_search.paginate_text(text, offset, 5)
            chunks.append(text[offset:info["end"]])
            self.assertGreater(info["end"], offset)
            offset = info["end"]
        self.assertEqual("".join(chunks), text)

    def test_page_includes_complete_diagram(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        path = "book/distributed/transactional-outbox-and-idempotency.md"
        full = server._tool_page({"path": path, "budget_chars": 5000})
        full = full.get("structuredContent", full)
        ranges = section_search.diagram_ranges(full["content"])
        if not ranges:
            self.skipTest("fixture has no mermaid in first page slice")
        start, end = ranges[0]
        payload = server._tool_page({
            "path": path, "offset": start, "budget_chars": 20})
        payload = payload.get("structuredContent", payload)
        self.assertEqual(payload["status"], "ok")
        self.assertIn(FENCE + "mermaid", payload["content"])
        self.assertIn(FENCE + "\n", payload["content"])
        self.assertEqual(payload["next_offset"], end)
        self.assertGreater(payload["budget_overrun_chars"], 0)

    def test_read_offset_inside_diagram_is_text_error(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        path = "book/distributed/transactional-outbox-and-idempotency.md"
        page = server._tool_page({"path": path, "budget_chars": 5000})
        page = page.get("structuredContent", page)
        start, _ = section_search.diagram_ranges(page["content"])[0]
        section = next(s for s in page["sections"]
                       if s["body_offset_start"] <= start < s["body_offset_end"])
        offset = start - section["body_offset_start"] + 1
        payload = server._tool_read({
            "section_key": section["section_key"],
            "offset": offset, "budget_chars": 20})
        payload = payload.get("structuredContent", payload)
        self.assertEqual(payload["status"], "offset-inside-diagram")
        result = server.tool_result(payload)
        self.assertTrue(result["isError"])
        self.assertNotIn("structuredContent", result)

    def test_text_only_error_has_no_structured_content(self):
        server = mcp_server.TychoMcpServer(root=ROOT)
        result = server.tool_result({
            "status": "offset-inside-diagram",
            "error": "offset-inside-diagram: requested_offset=1",
        })
        self.assertTrue(result["isError"])
        self.assertNotIn("structuredContent", result)
        self.assertIn("offset-inside-diagram",
                      result["content"][0]["text"])


if __name__ == "__main__":
    unittest.main()
