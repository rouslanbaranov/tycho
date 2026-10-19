"""E04-02 Draft 2020-12 metadata/source schema test fixtures.

If the explicit optional dependency is unavailable, unittest reports SKIP
rather than pretending schema checks ran. The dedicated CLI MUST fail closed.
"""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    Draft202012Validator = None
    FormatChecker = None


@unittest.skipUnless(Draft202012Validator, "install requirements-validation.txt")
class MetadataSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document_schema = json.loads((ROOT / "schemas/document-metadata.v1.schema.json").read_text())
        cls.source_schema = json.loads((ROOT / "schemas/source-reference.v1.schema.json").read_text())
        Draft202012Validator.check_schema(cls.document_schema)
        Draft202012Validator.check_schema(cls.source_schema)
        cls.doc_check = Draft202012Validator(cls.document_schema, format_checker=FormatChecker())
        cls.source_check = Draft202012Validator(cls.source_schema, format_checker=FormatChecker())
        cls.page = json.loads((ROOT / "fixtures/metadata-valid-page.v1.json").read_text())
        cls.book = json.loads((ROOT / "fixtures/metadata-valid-book.v1.json").read_text())
        cls.section = json.loads((ROOT / "fixtures/source-valid-section.v1.json").read_text())
        cls.code = json.loads((ROOT / "fixtures/source-valid-git-reference.v1.json").read_text())

    def assertRejected(self, validator, sample):
        self.assertGreater(len(list(validator.iter_errors(sample))), 0)

    def test_valid_document_and_landing_instances(self):
        self.doc_check.validate(self.page)
        self.doc_check.validate(self.book)

    def test_valid_source_section_and_git_reference(self):
        self.source_check.validate(self.section)
        self.source_check.validate(self.code)

    def test_no_unexpected_properties(self):
        bad = {**self.page, "verified_by_ai": True}
        self.assertRejected(self.doc_check, bad)
        bad = {**self.section, "commercial_reprint_allowed": True}
        self.assertRejected(self.source_check, bad)

    def test_dates_are_real_calendar_days(self):
        bad = {**self.page, "updated_at": "2026-02-30"}
        self.assertRejected(self.doc_check, bad)
        bad = {**self.section, "access_checked": "2026-13-01"}
        self.assertRejected(self.source_check, bad)

    def test_hierarchy_requires_book_null_parent_and_children_parent(self):
        bad = {**self.book, "parent_id": "tycho.volume.01h9abcdef"}
        self.assertRejected(self.doc_check, bad)
        bad = {**self.page, "parent_id": None}
        self.assertRejected(self.doc_check, bad)

    def test_evidence_date_cannot_be_fabricated_from_build(self):
        bad = deepcopy(self.page)
        bad["evidence_scope"]["status"] = "independently-verified"
        bad["evidence_scope"]["claim_ids"] = []
        bad["content_verified_at"] = None
        self.assertRejected(self.doc_check, bad)

    def test_verified_content_needs_review_identity(self):
        bad = deepcopy(self.page)
        bad["content_review"]["status"] = "accepted"
        self.assertRejected(self.doc_check, bad)
        bad["content_review"].update(reviewed_at="2026-10-19",
                                     reviewer="Reviewer", proof_uri="https://example.org/review")
        self.doc_check.validate(bad)

    def test_identity_and_path_traversal_refused(self):
        bad = {**self.page, "id": "tycho.page./../bad"}
        self.assertRejected(self.doc_check, bad)
        bad = {**self.page, "canonical_path": "../restricted/file.md"}
        self.assertRejected(self.doc_check, bad)

    def test_source_unadmitted_cannot_claim_inspected_content(self):
        bad = {**self.section, "admission": "pending-content-access"}
        self.assertRejected(self.source_check, bad)

    def test_wrong_source_location_kind_or_revision_rejected(self):
        bad = {**self.code, "verification": "code-inspected",
               "content_verified_at": "2026-10-19"}
        self.source_check.validate(bad)
        bad["location"]["revision"] = "main"
        self.assertRejected(self.source_check, bad)

    def test_lists_reject_wrong_type_and_duplicate_terms(self):
        bad = deepcopy(self.page)
        bad["perspectives"] = ["architecture", "architecture"]
        self.assertRejected(self.doc_check, bad)
        bad = deepcopy(self.page)
        bad["topic_ids"] = ["queueing", 5]
        self.assertRejected(self.doc_check, bad)


if __name__ == "__main__":
    unittest.main()
