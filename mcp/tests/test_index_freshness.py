"""Automatic freshness for the derived section index."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "mcp"))
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_http_server
import mcp_server
import section_fts_index


class IndexFreshnessTests(unittest.TestCase):
    def test_ensure_fresh_noop_when_verified(self):
        result = section_fts_index.ensure_fresh(ROOT)
        self.assertEqual(result["status"], "fresh", result)
        self.assertTrue(result.get("cached"), result)

    def test_ensure_fresh_rebuilds_stale_index(self):
        with patch.object(section_fts_index, "_marker_matches",
                          return_value=None):
            with patch.object(section_fts_index, "verify",
                              side_effect=[ValueError("stale"),
                                           {"snapshot": "x"}]):
                with patch.object(section_fts_index, "publish") as publish:
                    result = section_fts_index.ensure_fresh(ROOT)
        self.assertEqual(result["status"], "rebuilt")
        publish.assert_called_once()

    def test_server_refreshes_on_init(self):
        with patch.object(mcp_server.section_fts_index, "ensure_fresh",
                          return_value={"status": "fresh"}) as ensure:
            server = mcp_server.TychoMcpServer(root=ROOT)
        self.assertEqual(server.index_refresh["status"], "fresh")
        ensure.assert_called_once()

    def test_http_application_refreshes_on_startup(self):
        with patch.object(mcp_server.section_fts_index, "ensure_fresh",
                          return_value={"status": "fresh"}) as ensure:
            app = mcp_http_server.TychoHttpApplication(
                root=ROOT, token="test-token")
        self.assertEqual(app.server.index_refresh["status"], "fresh")
        ensure.assert_called_once()


if __name__ == "__main__":
    unittest.main()
