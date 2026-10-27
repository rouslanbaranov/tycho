import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_sufficient_pilot import check_manifest_units, validate


class SufficientPilotTests(unittest.TestCase):
    def test_six_pilot_inputs_are_current(self):
        self.assertEqual(validate(ROOT), {"entries": 6, "batches": 18})

    def test_stale_manifest_source_unit_is_rejected(self):
        manifest = json.loads(
            (ROOT / "research/sufficient-pilot-540/manifest.json").read_text())
        plan = json.loads(
            (ROOT / "edition/patterns/source-plan.v1.json").read_text())
        entry = manifest["entries"][0]
        units = {item["pattern_id"]: item for item in plan["entries"]}
        check_manifest_units(entry, units[entry["pattern_id"]]["required_units"])
        stale = copy.deepcopy(entry)
        stale["source_units"][0]["url"] = "https://example.invalid/stale"
        with self.assertRaisesRegex(ValueError, "pilot-source-unit-url"):
            check_manifest_units(stale, units[entry["pattern_id"]]["required_units"])


if __name__ == "__main__":
    unittest.main()
