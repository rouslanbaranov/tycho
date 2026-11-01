"""Adversarial checks for the pattern registry, not technical acceptance."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pattern_registry import load_json, validate_data


class PatternRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_json(ROOT / "edition/patterns/registry.v1.json")

    def copy(self):
        return copy.deepcopy(self.data)

    def check_error(self, data, message):
        with self.assertRaisesRegex(ValueError, message):
            validate_data(data, ROOT)

    def test_complete_catalog_partition(self):
        result = validate_data(self.data, ROOT)
        self.assertEqual(result["patterns"], 145)
        self.assertEqual(result["families"], 11)
        self.assertEqual((result["core"], result["advanced"]), (123, 22))
        self.assertEqual(result["technical_owners"], 145)
        self.assertEqual(result["atlas_sections"], 145)
        self.assertEqual(result["source_units"], 388)

    def test_missing_pattern_is_rejected(self):
        data = self.copy()
        data["patterns"].pop()
        self.check_error(data, "registry-schema")

    def test_duplicate_pattern_id_is_rejected(self):
        data = self.copy()
        data["patterns"][1]["id"] = data["patterns"][0]["id"]
        self.check_error(data, "registry-duplicate-pattern-id")

    def test_family_partition_is_rejected(self):
        data = self.copy()
        data["families"][0]["pattern_ids"].pop()
        self.check_error(data, "registry-family-partition")

    def test_catalog_order_gap_is_rejected(self):
        data = self.copy()
        data["patterns"][-1]["catalog_order"] = 144
        self.check_error(data, "registry-catalog-order")

    def test_priority_count_is_rejected(self):
        data = self.copy()
        data["patterns"][0]["priority"] = "advanced"
        self.check_error(data, "registry-priority-count")

    def test_alias_collision_is_rejected(self):
        data = self.copy()
        data["patterns"][0]["aliases"].append("CQRS")
        self.check_error(data, "registry-alias-collision")

    def test_atlas_chapter_mismatch_is_rejected(self):
        data = self.copy()
        data["patterns"][0]["atlas_owner"]["chapter"] = "V11/C02"
        self.check_error(data, "registry-atlas-chapter-mismatch")

    def test_duplicate_atlas_section_is_rejected(self):
        data = self.copy()
        data["patterns"][1]["atlas_section"] = data["patterns"][0]["atlas_section"]
        self.check_error(data, "registry-duplicate-atlas-section")

    def test_sufficient_without_owner_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": None,
            "path": None,
            "anchor": None,
            "state": "sufficient",
        }
        pattern["coverage"]["technical"] = "sufficient"
        pattern["coverage"]["decision"] = "sufficient"
        pattern["coverage"]["overall"] = "sufficient"
        self.check_error(data, "registry-sufficient-without-owner")

    def test_sufficient_without_read_source_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.book.37c50125355948f1b52ec66229ef59bd",
            "path": "book/README.md",
            "anchor": None,
            "state": "sufficient",
        }
        pattern["atlas_owner"]["state"] = "sufficient"
        pattern["source_units"] = []
        pattern["coverage"]["technical"] = "sufficient"
        pattern["coverage"]["decision"] = "sufficient"
        pattern["coverage"]["overall"] = "sufficient"
        self.check_error(data, "registry-sufficient-without-read-source")

    def test_unknown_source_is_rejected(self):
        data = self.copy()
        data["patterns"][0]["source_units"].append(
            {"source_id": "src.not-real", "unit": "test", "status": "read"}
        )
        self.check_error(data, "registry-unknown-source")

    def test_unknown_owner_id_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.page.000000",
            "path": "book/README.md",
            "anchor": None,
            "state": "partial",
        }
        pattern["coverage"]["technical"] = "partial"
        pattern["coverage"]["decision"] = "partial"
        pattern["coverage"]["overall"] = "partial"
        self.check_error(data, "registry-unknown-owner-id")

    def test_owner_path_mismatch_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.book.37c50125355948f1b52ec66229ef59bd",
            "path": "book/application/README.md",
            "anchor": None,
            "state": "partial",
        }
        pattern["coverage"]["technical"] = "partial"
        pattern["coverage"]["decision"] = "partial"
        pattern["coverage"]["overall"] = "partial"
        self.check_error(data, "registry-owner-path-mismatch")

    def test_owner_anchor_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.book.37c50125355948f1b52ec66229ef59bd",
            "path": "book/README.md",
            "anchor": "definitely-missing",
            "state": "partial",
        }
        pattern["coverage"]["technical"] = "partial"
        pattern["coverage"]["decision"] = "partial"
        pattern["coverage"]["overall"] = "partial"
        self.check_error(data, "registry-owner-anchor")

    def test_technical_state_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.book.37c50125355948f1b52ec66229ef59bd",
            "path": "book/README.md",
            "anchor": None,
            "state": "partial",
        }
        pattern["atlas_owner"]["state"] = "sufficient"
        pattern["coverage"]["technical"] = "sufficient"
        pattern["coverage"]["decision"] = "sufficient"
        pattern["coverage"]["overall"] = "sufficient"
        pattern["source_units"] = [
            {"source_id": "src.ddia", "unit": "test", "status": "read"}
        ]
        self.check_error(data, "registry-technical-state")

    def test_atlas_state_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["technical_owner"] = {
            "document_id": "tycho.book.37c50125355948f1b52ec66229ef59bd",
            "path": "book/README.md",
            "anchor": None,
            "state": "sufficient",
        }
        pattern["coverage"]["technical"] = "sufficient"
        pattern["coverage"]["decision"] = "sufficient"
        pattern["coverage"]["overall"] = "sufficient"
        pattern["source_units"] = [
            {"source_id": "src.ddia", "unit": "test", "status": "read"}
        ]
        self.check_error(data, "registry-atlas-state")

    def test_coverage_overall_is_rejected(self):
        data = self.copy()
        pattern = data["patterns"][0]
        pattern["coverage"]["technical"] = "partial"
        pattern["coverage"]["decision"] = "sufficient"
        pattern["coverage"]["overall"] = "sufficient"
        self.check_error(data, "registry-coverage-overall")

    def test_schema_rejects_extra_property(self):
        data = self.copy()
        data["patterns"][0]["unexpected"] = True
        self.check_error(data, "registry-schema")

    def test_independent_review_claim_is_rejected(self):
        data = self.copy()
        data["patterns"][0]["review_status"] = "independent-reviewed"
        self.check_error(data, "registry-independent-review-claim")


if __name__ == "__main__":
    unittest.main()
