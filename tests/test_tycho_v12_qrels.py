"""Validate the V12 simulation qrels against the canonical route."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_corpus_qrels  # noqa: E402


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class V12QrelsTests(unittest.TestCase):
    def test_v12_qrels_validate_and_stay_in_v12(self):
        result = validate_corpus_qrels.validate(
            load("evaluation/v12-simulation-qrels.v1.json"),
            load("generated/route-index.v1.json"),
            load("schemas/corpus-qrels.v1.schema.json"),
            scope="v12",
        )
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["items"], 15)
        self.assertEqual(result["accepted_answers"], 28)
        qrels = load("evaluation/v12-simulation-qrels.v1.json")
        for item in qrels["items"]:
            for answer in item["accepted"]:
                self.assertTrue(answer["path"].startswith(
                    "book/volumes/v12-modeling-simulation-and-decision-validation/"))

    def test_v12_qrels_snapshot_is_full_route(self):
        qrels = load("evaluation/v12-simulation-qrels.v1.json")
        route = load("generated/route-index.v1.json")
        self.assertEqual(qrels["snapshot"]["route_index_snapshot"],
                         route["snapshot_sha256"])
        self.assertEqual(qrels["snapshot"]["document_count"],
                         len(route["documents"]))


if __name__ == "__main__":
    unittest.main()
