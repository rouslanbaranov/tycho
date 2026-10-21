"""Adversarial checks for the source plan and reading ledger, not source truth."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_sources import load, validate_data

PLAN = ROOT / "edition/patterns/source-plan.v1.json"
LEDGER = ROOT / "edition/patterns/reading-ledger.v1.json"
REGISTRY = ROOT / "edition/patterns/registry.v1.json"
ROUTE = ROOT / "generated/route-index.v1.json"
REGISTER = ROOT / "sources/register.json"


class PatternSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = load(PLAN)
        cls.ledger = load(LEDGER)
        cls.registry = load(REGISTRY)
        cls.route = load(ROUTE)
        cls.sources = load(REGISTER)

    def copy(self):
        return (copy.deepcopy(self.plan), copy.deepcopy(self.ledger),
                copy.deepcopy(self.registry), copy.deepcopy(self.route),
                copy.deepcopy(self.sources))

    def check_error(self, plan, ledger, registry, route, sources, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_data(plan, ledger, registry, route, sources, ROOT)

    def test_complete_foundation_plan(self):
        result = validate_data(self.plan, self.ledger, self.registry,
                               self.route, self.sources, ROOT)
        self.assertEqual(result["entries"], 145)
        self.assertEqual(result["read_units"], 5)
        self.assertEqual(result["planned_units"], 139)
        self.assertEqual(result["blocked_units"], 1)
        self.assertEqual(result["ledger_records"], 6)

    def test_missing_plan_entry_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        plan["entries"].pop()
        self.check_error(plan, ledger, registry, route, sources, "source-schema")

    def test_unknown_pattern_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        plan["entries"][0]["pattern_id"] = "tycho.pattern.not-real"
        self.check_error(plan, ledger, registry, route, sources, "source-plan-pattern")

    def test_unknown_source_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        plan["entries"][0]["required_units"][0]["source_id"] = "src.not-real"
        self.check_error(plan, ledger, registry, route, sources, "source-plan-unknown-source")

    def test_missing_read_record_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        unit = next(unit for entry in plan["entries"] for unit in entry["required_units"]
                    if unit["status"] == "read")
        unit["read_record_id"] = "read.not-real.2026-10-21"
        self.check_error(plan, ledger, registry, route, sources, "ledger-unreferenced-record")

    def test_unreferenced_ledger_record_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        record = copy.deepcopy(ledger["records"][0])
        record["id"] = "read.unreferenced.2026-10-21"
        ledger["records"].append(record)
        self.check_error(plan, ledger, registry, route, sources, "ledger-unreferenced-record")

    def test_unknown_ledger_source_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        ledger["records"][0]["source_id"] = "src.not-real"
        self.check_error(plan, ledger, registry, route, sources, "ledger-unknown-source")

    def test_registry_binding_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        registry["patterns"][0]["source_units"][0]["status"] = "read"
        self.check_error(plan, ledger, registry, route, sources, "source-registry-mismatch")

    def test_summary_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        plan["summary"]["read_units"] = 4
        self.check_error(plan, ledger, registry, route, sources, "source-summary-read")

    def test_registry_hash_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        plan["registry_sha256"] = "0" * 64
        self.check_error(plan, ledger, registry, route, sources, "source-registry-hash")

    def test_duplicate_ledger_id_is_rejected(self):
        plan, ledger, registry, route, sources = self.copy()
        ledger["records"][1]["id"] = ledger["records"][0]["id"]
        self.check_error(plan, ledger, registry, route, sources, "ledger-duplicate-id")


if __name__ == "__main__":
    unittest.main()
