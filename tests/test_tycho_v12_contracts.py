"""V12 contract, provenance and structural regressions."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_v12

SCHEMAS = ROOT / "schemas/v12"


def load(path):
    return json.loads(Path(path).read_text())


class ContractTests(unittest.TestCase):
    def test_all_artifact_schemas(self):
        from jsonschema import Draft202012Validator
        pairs = [
            ("models", "model-specification.v1.schema.json"),
            ("scenarios", "scenario-specification.v1.schema.json"),
            ("runs", "run-result.v1.schema.json"),
            ("decisions", "decision-record.v1.schema.json"),
        ]
        registry = load(ROOT / "edition/v12/registry.json")
        for collection, schema_name in pairs:
            schema = load(SCHEMAS / schema_name)
            validator = Draft202012Validator(schema)
            for artifact in registry["artifacts"][collection]:
                errors = list(validator.iter_errors(load(ROOT / artifact["path"])))
                self.assertEqual(errors, [], artifact["path"])

    def test_manifest_and_source_contracts(self):
        from jsonschema import Draft202012Validator
        manifest = load(ROOT / "edition/v12/manifest.json")
        Draft202012Validator(load(SCHEMAS / "manifest.v1.schema.json")).validate(manifest)
        ledger = load(ROOT / "edition/v12/reading-ledger.v1.json")
        Draft202012Validator(load(SCHEMAS / "reading-ledger.v1.schema.json")).validate(ledger)
        plan = load(ROOT / "edition/v12/source-plan.v1.json")
        Draft202012Validator(load(SCHEMAS / "source-plan.v1.schema.json")).validate(plan)
        self.assertEqual(len(manifest["documents"]), 31)
        self.assertEqual(len(manifest["chapters"]), 7)
        self.assertGreaterEqual(len(ledger["records"]), 10)

    def test_canonical_pattern_link_rejects_wrong_owner(self):
        registry = load(ROOT / "edition/patterns/registry.v1.json")
        patterns = {item["id"]: item for item in registry["patterns"]}
        route = load(ROOT / "generated/route-index.v1.json")
        index = {doc["id"]: doc for doc in route["documents"]}
        first, second = list(patterns.values())[:2]
        link = {
            "pattern_id": first["id"],
            "owner_document_id": second["technical_owner"]["document_id"],
            "owner_page": second["technical_owner"]["path"],
        }
        with self.assertRaisesRegex(ValueError, "owner id mismatch"):
            validate_v12.canonical_link(link, patterns, index, ROOT)

    def test_manifest_page_hashes(self):
        manifest = load(ROOT / "edition/v12/manifest.json")
        for document in manifest["documents"]:
            self.assertEqual(
                validate_v12.sha(ROOT / document["path"]), document["sha256"], document["path"]
            )

    def test_run_provenance_hashes(self):
        registry = load(ROOT / "edition/v12/registry.json")
        models = {a["id"]: a for a in registry["artifacts"]["models"]}
        scenarios = {a["id"]: a for a in registry["artifacts"]["scenarios"]}
        for run in registry["artifacts"]["runs"]:
            data = load(ROOT / run["path"])
            self.assertEqual(data["provenance"]["model_sha256"],
                             validate_v12.sha(ROOT / models[data["model_id"]]["path"]))
            self.assertEqual(data["provenance"]["scenario_sha256"],
                             validate_v12.sha(ROOT / scenarios[data["scenario_id"]]["path"]))
            body = {k: v for k, v in data.items() if k != "result_sha256"}
            self.assertEqual(data["result_sha256"], validate_v12.sha_json(body))
            self.assertTrue(data["invariants"]["conservation_ok"])
            self.assertTrue(all(check["status"] == "pass" for check in data["invariants"]["checks"]))

    def test_decision_references(self):
        registry = load(ROOT / "edition/v12/registry.json")
        runs = {a["id"] for a in registry["artifacts"]["runs"]}
        scenarios = {a["id"] for a in registry["artifacts"]["scenarios"]}
        patterns = {p["id"] for p in load(ROOT / "edition/patterns/registry.v1.json")["patterns"]}
        for decision in registry["artifacts"]["decisions"]:
            data = load(ROOT / decision["path"])
            for candidate in data["candidates"]:
                self.assertIn(candidate["scenario_id"], scenarios)
                self.assertTrue(set(candidate["run_ids"]) <= runs)
                self.assertTrue(set(candidate["pattern_ids"]) <= patterns)
            for link in data["pattern_links"]:
                self.assertIn(link["pattern_id"], patterns)
                self.assertTrue((ROOT / link["owner_page"]).is_file())

    def test_repository_validator(self):
        result = validate_v12.validate(ROOT)
        self.assertEqual(result["documents"], 31)
        self.assertEqual(result["chapters"], 7)
        self.assertEqual(result["models"], 3)
        self.assertEqual(result["scenarios"], 10)
        self.assertEqual(result["runs"], 10)
        self.assertEqual(result["decisions"], 2)
        self.assertEqual(result["protected"]["changed"], 0)
        self.assertEqual(result["protected"]["leaked"], 0)

    def test_iron_rule_detector_ignores_historical_decisions(self):
        self.assertTrue(validate_v12.V12_REFERENCE.search("see tycho.model.order-intake"))
        self.assertTrue(validate_v12.V12_REFERENCE.search("book/volumes/v12-modeling"))
        self.assertFalse(validate_v12.V12_REFERENCE.search(
            "tycho.decision.c089ea2f22f54b0ebbe9ebc3804a7e14"))


if __name__ == "__main__":
    unittest.main()
