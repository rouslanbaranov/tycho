"""Integration tests for automatic section-index refresh."""
import shutil
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))

import mcp_http_server
import mcp_server
import section_fts_index
from mcp.tests.test_tycho_mcp_server import McpServerTests


class AutoRefreshIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        McpServerTests.setUpClass()
        cls.base = Path(McpServerTests.root)

    @classmethod
    def tearDownClass(cls):
        McpServerTests.tearDownClass()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tycho-refresh-")
        self.root = Path(self.tmp.name)
        shutil.copytree(self.base, self.root, dirs_exist_ok=True)
        self.page = self.root / "book/alpha.md"

    def tearDown(self):
        self.tmp.cleanup()

    def test_real_stale_rebuild_after_book_change(self):
        first = section_fts_index.ensure_fresh(self.root)
        self.assertEqual(first["status"], "fresh", first)
        before = first["snapshot"]
        self.page.write_text(
            self.page.read_text(encoding="utf-8") + "\nSecond body.\n",
            encoding="utf-8")
        rebuilt = section_fts_index.ensure_fresh(self.root)
        self.assertEqual(rebuilt["status"], "rebuilt", rebuilt)
        self.assertNotEqual(before, rebuilt["snapshot"])

    def test_marker_invalidated_by_source_change(self):
        section_fts_index.ensure_fresh(self.root)
        index = self.root / "generated" / section_fts_index.INDEX_NAME
        self.assertIsNotNone(section_fts_index._marker_matches(self.root, index))
        self.page.write_text(
            self.page.read_text(encoding="utf-8") + "\nChanged.\n",
            encoding="utf-8")
        self.assertIsNone(section_fts_index._marker_matches(self.root, index))

    def test_http_ready_refreshes_after_change(self):
        app = mcp_http_server.TychoHttpApplication(self.root, token="t")
        app.ready()
        app.server._last_refresh = 0
        self.page.write_text(
            self.page.read_text(encoding="utf-8") + "\nHTTP change.\n",
            encoding="utf-8")
        result = app.ready()
        self.assertEqual(result["status"], "ok")
        self.assertIn(app.server.index_refresh["status"], ("rebuilt", "fresh"))

    def test_handle_refreshes_after_init(self):
        with mock.patch.object(
                mcp_server.section_fts_index, "ensure_fresh",
                return_value={"status": "fresh"}) as ensure:
            server = mcp_server.TychoMcpServer(root=self.root)
            server._last_refresh = 0
            with self.assertRaises(Exception):
                server.handle({"jsonrpc": "2.0", "method": "noop", "id": 1})
        self.assertGreaterEqual(ensure.call_count, 2)

    def test_build_lock_serializes_threads(self):
        index = self.root / "generated/lock-test.sqlite"
        order = []
        first_entered = threading.Event()

        def first():
            with section_fts_index.build_lock(index):
                order.append(1)
                first_entered.set()
                time.sleep(0.05)

        def second():
            with section_fts_index.build_lock(index):
                order.append(2)

        one = threading.Thread(target=first)
        two = threading.Thread(target=second)
        one.start()
        first_entered.wait(timeout=1)
        two.start()
        one.join()
        two.join()
        self.assertEqual(order, [1, 2])


if __name__ == "__main__":
    unittest.main()
