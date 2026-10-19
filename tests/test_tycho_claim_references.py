"""Offline contract tests for claim/source reference validation (E03-03)."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_claim_references as v  # noqa: E402


class ClaimReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads((ROOT / "sources" / "claim-references.json").read_text())
        cls.sources = json.loads((ROOT / "sources" / "register.json").read_text())
        cls.lock = json.loads((ROOT / "sources" / "public-repositories.lock.json").read_text())

    def check(self, example=None, sources=None, lock=None):
        return v.validate(example or self.example, sources or self.sources, lock or self.lock)

    def test_reference_examples_validate(self):
        result = self.check()
        self.assertEqual(result["claims"], 3)
        self.assertGreaterEqual(result["sources"], 3)

    def test_unknown_source_not_accepted(self):
        data = deepcopy(self.example)
        data["claims"][0]["evidence"][0]["source_id"] = "src.nonexistent"
        with self.assertRaisesRegex(ValueError, "unknown source"):
            self.check(data)

    def test_unavailable_cannot_be_fake_inspected(self):
        data = deepcopy(self.example)
        data["claims"][2]["evidence"][0]["verification"] = "section-inspected"
        with self.assertRaisesRegex(ValueError, "unavailable"):
            self.check(data)

    def test_pending_source_cannot_support_material_claim(self):
        data = deepcopy(self.example)
        data["claims"][0]["evidence"][0]["source_id"] = "src.jep491"
        with self.assertRaisesRegex(ValueError, "bibliography-only/pending"):
            self.check(data)

    def test_document_location_must_match_canonical_host(self):
        data = deepcopy(self.example)
        data["claims"][0]["evidence"][0]["location"]["url"] = "https://hostile.example/ref"
        with self.assertRaisesRegex(ValueError, "canonical"):
            self.check(data)

    def test_conflict_forces_contested_state(self):
        data = deepcopy(self.example)
        data["claims"][1]["status"] = "evidence-linked"
        with self.assertRaisesRegex(ValueError, "requires support|contested"):
            self.check(data)

    def test_no_evidence_linked_without_support(self):
        data = deepcopy(self.example)
        data["claims"][0]["evidence"][0]["relation"] = "qualifies"
        with self.assertRaisesRegex(ValueError, "requires support"):
            self.check(data)

    def test_code_revision_and_symbol_resolve_to_lock(self):
        data = deepcopy(self.example)
        row = self.lock["repositories"][0]
        ev = data["claims"][0]["evidence"][0]
        ev["source_id"] = row["id"]
        ev["verification"] = "code-inspected"  # synthetic fixture only; no real code was read
        ev["location"] = {
            "kind": "source-code", "url": None, "section": None,
            "revision": row["revision"], "path": "README.md", "symbol": "syntheticSymbol",
        }
        self.assertEqual(self.check(data)["claims"], 3)

    def test_code_revision_mismatch_rejected(self):
        data = deepcopy(self.example)
        row = self.lock["repositories"][0]
        ev = data["claims"][0]["evidence"][0]
        ev["source_id"] = row["id"]
        ev["verification"] = "code-inspected"  # synthetic fixture only; no real code was read
        ev["location"] = {"kind": "source-code", "url": None, "section": None,
                          "revision": "0" * 40, "path": "README.md", "symbol": None}
        with self.assertRaisesRegex(ValueError, "differs from pinned"):
            self.check(data)

    def test_code_path_traversal_rejected(self):
        data = deepcopy(self.example)
        row = self.lock["repositories"][0]
        ev = data["claims"][0]["evidence"][0]
        ev["source_id"] = row["id"]
        ev["verification"] = "code-inspected"  # synthetic fixture only; no real code was read
        ev["location"] = {"kind": "source-code", "url": None, "section": None,
                          "revision": row["revision"], "path": "../private", "symbol": None}
        with self.assertRaisesRegex(ValueError, "invalid code path"):
            self.check(data)

    def test_owner_page_path_must_be_relative(self):
        data = deepcopy(self.example)
        data["claims"][0]["owner_page"] = "../../secret.md"
        with self.assertRaisesRegex(ValueError, "unsafe"):
            self.check(data)


if __name__ == "__main__":
    unittest.main()
