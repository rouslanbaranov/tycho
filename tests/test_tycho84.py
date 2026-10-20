"""Bounded document checks for TYCHO-84; no actual sharding or pool validation."""
from pathlib import Path
import re
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "book/scaling"
PAGES = {
  "shard-keys-hotspots-and-resharding.md": (
    "vitess.io/docs/24.0/user-guides/configuration-advanced/resharding/",
    "www.postgresql.org/docs/17/ddl-partitioning.html"),
  "connection-pools-hikaricp-pgbouncer.md": (
    "github.com/brettwooldridge/HikariCP",
    "www.pgbouncer.org/config"),
  "local-distributed-caching-and-invalidation.md": (
    "github.com/ben-manes/caffeine/wiki/Refresh",
    "redis.io/docs/latest/develop/use-cases/cache-aside/"),
}


class ScalingEvidenceTests(unittest.TestCase):
    def test_substantive_mermaid_sources(self):
        for name, sources in PAGES.items():
            with self.subTest(name=name):
                text = canonical_path(BASE / name).read_text(encoding="utf-8")
                self.assertGreater(len(text), 9000)
                self.assertGreaterEqual(text.count("```mermaid"), 3)
                self.assertGreaterEqual(text.count("Text alternative:"), 3)
                self.assertEqual(text.count("```") % 2, 0)
                self.assertIn("Insufficient evidence", text)
                for url in sources:
                    self.assertIn(url.lower(), text.lower())

    def test_live_relative_navigation(self):
        landing = BASE / "README.md"
        root = (ROOT / "book/README.md").read_text(encoding="utf-8")
        self.assertIn("(scaling/README.md)", root)
        for name in PAGES:
            self.assertIn("(" + relative_link(BASE / "README.md", BASE / name) + ")", landing.read_text(encoding="utf-8"))
        for doc in [landing, *(canonical_path(BASE / name) for name in PAGES)]:
            for raw in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if raw.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                path = raw.split("#", 1)[0]
                if path:
                    self.assertTrue((doc.parent / path).is_file(), (str(doc), raw))

    def test_original_synthetic_numbers(self):
        self.assertEqual(4 * 25, 100)
        self.assertEqual(20 / .1, 200)
        self.assertEqual(20 / .25, 80)
        self.assertEqual(2000 - 1500, 500)


if __name__ == "__main__":
    unittest.main()
