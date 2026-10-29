"""Adversarial checks for the V11 atlas manifest, not technical acceptance."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_atlas import load, validate_data

MANIFEST = ROOT / "edition/atlas-manifest.json"
BOOK_ID = "tycho.book.37c50125355948f1b52ec66229ef59bd"


class PatternAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(MANIFEST)

    def copy(self):
        return copy.deepcopy(self.data)

    def check_error(self, data, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_data(data, ROOT)

    def test_complete_scaffold(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["volume"], "V11")
        self.assertEqual(result["chapters"], 11)
        self.assertEqual(result["documents"], 49)
        self.assertEqual(result["patterns"], 145)

    def test_registry_hash_is_rejected(self):
        data = self.copy()
        data["registry_sha256"] = "0" * 64
        self.check_error(data, "atlas-registry-hash")

    def test_edition_version_is_rejected(self):
        data = self.copy()
        data["version"] = "2026.10.1-rc.3"
        self.check_error(data, "atlas-edition-version")

    def test_chapter_parent_is_rejected(self):
        data = self.copy()
        chapter_id = data["chapters"][0]["id"]
        doc = next(item for item in data["documents"] if item["id"] == chapter_id)
        doc["parent_id"] = BOOK_ID
        self.check_error(data, "atlas-chapter-parent")

    def test_document_sha_is_rejected(self):
        data = self.copy()
        data["documents"][1]["sha256"] = "0" * 64
        self.check_error(data, "atlas-document-sha")

    def test_pattern_partition_is_rejected(self):
        data = self.copy()
        data["chapters"][0]["pattern_ids"].pop()
        self.check_error(data, "atlas-pattern-partition")

    def test_duplicate_document_path_is_rejected(self):
        data = self.copy()
        data["documents"][1]["path"] = data["documents"][0]["path"]
        self.check_error(data, "atlas-schema|atlas-duplicate-document-path")

    def test_volume_section_missing_is_rejected(self):
        data = self.copy()
        data["documents"][0]["sha256"] = "0" * 64
        data["volume"]["path"] = data["documents"][0]["path"]
        self.check_error(data, "atlas-document-sha")


if __name__ == "__main__":
    unittest.main()
