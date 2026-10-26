import hashlib
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_sufficient_promotions import validate


class SufficientPromotionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "schemas").mkdir()
        (self.root / "edition/patterns").mkdir(parents=True)
        shutil.copy(ROOT / "schemas/sufficient-promotions.v1.schema.json",
                    self.root / "schemas/sufficient-promotions.v1.schema.json")
        (self.root / "edition/patterns/registry.v1.json").write_text(
            json.dumps({"patterns": [{"id": "tycho.pattern.test"}]}))
        (self.root / "authoring/ai-reviews").mkdir(parents=True)
        self.report = self.root / "authoring/ai-reviews/report.md"
        self.report.write_text("# Report\n\nTest only.\n")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"],
                       cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "test"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "test"], cwd=self.root, check=True)
        self.head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()
        self.record = {
            "pattern_id": "tycho.pattern.test",
            "technical": "pass",
            "decision": "pass",
            "reviewed_at": "2026-10-26",
            "reviewed_head": self.head,
            "owner_page_sha256": "a" * 64,
            "card_sha256": "b" * 64,
            "reviewer": "test/other",
            "report_path": "authoring/ai-reviews/report.md",
            "report_sha256": hashlib.sha256(self.report.read_bytes()).hexdigest(),
        }

    def tearDown(self):
        self.temp.cleanup()

    def write(self, promotions):
        data = {"schema_version": 1, "issue": 540,
                "policy": "governance/SUFFICIENT-COVERAGE.md",
                "promotions": promotions}
        (self.root / "edition/patterns/sufficient-promotions.v1.json").write_text(
            json.dumps(data))

    def test_valid_promotion_passes(self):
        self.write([self.record])
        self.assertEqual(validate(self.root), {"promotions": 1})

    def test_report_hash_mismatch_is_rejected(self):
        self.record["report_sha256"] = "c" * 64
        self.write([self.record])
        with self.assertRaisesRegex(ValueError, "promotions-report-hash"):
            validate(self.root)

    def test_unknown_pattern_is_rejected(self):
        self.record["pattern_id"] = "tycho.pattern.unknown"
        self.write([self.record])
        with self.assertRaisesRegex(ValueError, "promotions-unknown-pattern"):
            validate(self.root)

    def test_missing_report_is_rejected(self):
        self.record["report_path"] = "authoring/ai-reviews/missing.md"
        self.write([self.record])
        with self.assertRaisesRegex(ValueError, "promotions-report-missing"):
            validate(self.root)

    def test_report_outside_reviews_is_rejected(self):
        outside = self.root / "outside.md"
        outside.write_text("# Outside\n")
        self.record["report_path"] = "outside.md"
        self.record["report_sha256"] = hashlib.sha256(outside.read_bytes()).hexdigest()
        self.write([self.record])
        with self.assertRaisesRegex(ValueError, "promotions-report-location"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
