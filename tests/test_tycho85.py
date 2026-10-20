"""TYCHO-85 only validates manuscript, original maths and navigation.

Not a search deployment, measured recall or a full answer-quality benchmark.
"""
from pathlib import Path
import re
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "book/search"
PAGES = {
    "lexical-indexing-bm25-and-sql-fts.md": [
        "www.postgresql.org/docs/17/textsearch-controls.html",
        "lucene.apache.org/core/10_3_0"],
    "vector-hnsw-faiss-pgvector.md": [
        "github.com/pgvector/pgvector",
        "github.com/facebookresearch/faiss/wiki/Faiss-indexes"],
    "hybrid-ranking-graph-and-evaluation.md": [
        "www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion",
        "neo4j.com/docs/getting-started/"],
}


class SearchResearchChecks(unittest.TestCase):
    def test_technical_pages_and_visuals(self):
        for name, links in PAGES.items():
            with self.subTest(name=name):
                s = canonical_path(BASE / name).read_text(encoding="utf-8")
                self.assertGreater(len(s), 9000)
                self.assertGreaterEqual(s.count("```mermaid"), 3)
                self.assertGreaterEqual(s.count("Text alternative:"), 3)
                self.assertEqual(s.count("```") % 2, 0)
                self.assertIn("Insufficient evidence", s)
                for link in links:
                    self.assertIn(link.lower(), s.lower())

    def test_relative_navigation(self):
        landing = BASE / "README.md"
        root = (ROOT / "book/README.md").read_text(encoding="utf-8")
        self.assertIn("(search/README.md)", root)
        for name in PAGES:
            self.assertIn("(" + relative_link(BASE / "README.md", BASE / name) + ")", landing.read_text(encoding="utf-8"))
        for path in [landing, *(canonical_path(BASE / n) for n in PAGES)]:
            for ref in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if ref.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = ref.split("#", 1)[0]
                if target:
                    self.assertTrue((path.parent / target).is_file(), (str(path), ref))

    def test_synthetic_rrf_example(self):
        a = 1 / 61 + 1 / 62
        b, c = 1 / 62, 1 / 61
        self.assertTrue(a > c > b)
        self.assertAlmostEqual(a, .0325224749, places=7)

    def test_vector_raw_size_example(self):
        self.assertEqual(4500 * 768 * 4, 13_824_000)


if __name__ == "__main__":
    unittest.main()
