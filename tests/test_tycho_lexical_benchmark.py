"""Synthetic FTS5 versus SQL-LIKE pilot, no external data."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import benchmark_lexical as b  # noqa: E402


class LexicalPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = json.loads((ROOT / "fixtures/lexical-engine-pilot.json").read_text())

    def test_relevance_labels_resolve(self):
        self.assertEqual(len(self.fixtures["documents"]), 12)
        b.validate_fixture(self.fixtures)

    def test_reject_bad_query_and_unknown_labels(self):
        for query in ("", " ", "word " * 20, "x" * 100):
            with self.assertRaises(ValueError):
                b.tokens(query)
        bad = json.loads(json.dumps(self.fixtures))
        bad["questions"][0]["relevant_ids"] = ["not-in-corpus"]
        with self.assertRaises(ValueError):
            b.validate_fixture(bad)

    def test_fts_query_does_not_inject_fts_operators(self):
        escaped = b.fts_query("Kafka OR partition")
        self.assertEqual(escaped, '"kafka" OR "or" OR "partition"')
        self.assertNotIn("NEAR(", b.fts_query("NEAR(kafka)"))

    def test_embedded_bm25_and_scan_both_operate(self):
        with tempfile.TemporaryDirectory() as d:
            db = b.build_sqlite(Path(d) / "index.sqlite", self.fixtures["documents"])
            self.assertIn("d02", b.search(db, "kafka partition ordering", "fts5"))
            self.assertIn("d02", b.search(db, "kafka partition ordering", "like"))
            with self.assertRaises(ValueError):
                b.search(db, "x", "unknown")
            db.close()

    def test_benchmark_metrics_and_size_have_units(self):
        result = b.bench(self.fixtures, repeats=2)
        self.assertEqual(result["queries"], 14)
        self.assertGreater(result["index_and_content_db_bytes"], 0)
        self.assertGreaterEqual(result["fts5_and_table_build_ms"], 0)
        for engine in ("fts5", "like"):
            item = result["engines"][engine]
            self.assertEqual(len(item["results"]), 14)
            self.assertGreaterEqual(item["median_ms"], 0)
            self.assertGreaterEqual(item["p95_ms"], 0)
            self.assertGreaterEqual(item["mrr_at_5"], 0)
            self.assertLessEqual(item["mean_recall_at_5"], 1)

    def test_reject_duplicate_docid(self):
        bad = json.loads(json.dumps(self.fixtures))
        bad["documents"].append(bad["documents"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            b.validate_fixture(bad)


    def test_ranked_results_deterministic_for_fixed_snapshot(self):
        with tempfile.TemporaryDirectory() as d:
            db = b.build_sqlite(Path(d) / "fixed.sqlite", self.fixtures["documents"])
            for engine in ("fts5", "like"):
                first = b.search(db, "database pool connection", engine)
                second = b.search(db, "database pool connection", engine)
                self.assertEqual(first, second)
                self.assertIn("d05", first)
            db.close()

    def test_alias_misses_are_exposed_not_reinterpreted_as_true_negative(self):
        cases = [q for q in self.fixtures["questions"]
                 if q["case"].endswith("-unindexed")]
        self.assertEqual(len(cases), 2)
        with tempfile.TemporaryDirectory() as d:
            db = b.build_sqlite(Path(d) / "aliases.sqlite", self.fixtures["documents"])
            for q in cases:
                hits = b.search(db, q["query"], "fts5")
                # A sparse lexical index is not proof that synonyms are resolved.
                self.assertNotIn(q["relevant_ids"][0], hits)
            db.close()

    def test_query_constraints_are_bounded(self):
        with tempfile.TemporaryDirectory() as d:
            db = b.build_sqlite(Path(d) / "limits.sqlite", self.fixtures["documents"])
            with self.assertRaises(ValueError):
                b.search(db, "kafka", "fts5", k=0)
            with self.assertRaises(ValueError):
                b.search(db, "kafka", "like", k=101)
            db.close()


if __name__ == "__main__":
    unittest.main()
