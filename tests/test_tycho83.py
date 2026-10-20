"""TYCHO-83 document mechanics, no real database execution or benchmark."""
from pathlib import Path
import re
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "book/data"
PAGES = {
  "postgresql-mvcc-indexes-and-query-plans.md": (
      "www.postgresql.org/docs/17/mvcc-intro.html",
      "www.postgresql.org/docs/17/using-explain.html"),
  "postgresql-wal-replication-and-recovery.md": (
      "www.postgresql.org/docs/17/wal-intro.html",
      "www.postgresql.org/docs/17/warm-standby.html"),
  "storage-model-alternatives-and-workload-fit.md": (
      "www.sqlite.org/arch.html",
      "cassandra.apache.org/doc/stable/",
      "apple.github.io/foundationdb/architecture.html",
      "clickhouse.com/docs/reference/engines",
      "neo4j.com/docs/getting-started/"),
}


class DataArchitectureTests(unittest.TestCase):
    def test_substantial_research_sources_and_mermaid(self):
        for name, sources in PAGES.items():
            with self.subTest(page=name):
                content = canonical_path(DATA / name).read_text(encoding="utf-8")
                self.assertGreater(len(content), 11000)
                self.assertGreaterEqual(content.count("```mermaid"), 3)
                self.assertGreaterEqual(content.count("Text alternative:"), 3)
                self.assertEqual(content.count("```") % 2, 0)
                self.assertIn("Insufficient evidence", content)
                for source in sources:
                    self.assertIn(source, content)

    def test_navigation_and_local_links(self):
        texts = [DATA / "README.md", *(canonical_path(DATA / x) for x in PAGES)]
        index = (ROOT / "book/README.md").read_text(encoding="utf-8")
        self.assertIn("(data/README.md)", index)
        for name in PAGES:
            self.assertIn("(" + relative_link(DATA / "README.md", DATA / name) + ")", texts[0].read_text(encoding="utf-8"))
        for path in texts:
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                local = target.split("#", 1)[0]
                if local:
                    self.assertTrue((path.parent / local).is_file(), (str(path), target))


if __name__ == "__main__":
    unittest.main()
