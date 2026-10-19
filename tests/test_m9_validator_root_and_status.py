#!/usr/bin/env python3
"""M9 validator unit regression tests using standard-library unittest.

Execute from a pinned Tycho checkout:
    python3 -m unittest discover -s tests -p 'test_m9_validator*.py' -v

These tests do NOT execute MCP or independently verify corporate case studies.
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_m9_cases import (  # noqa: E402
    check,
    iso_date,
    json_read,
    self_test,
    validate_record,
)


class PinnedRootAndFormatTest(unittest.TestCase):
    def test_date_requires_full_calendar_syntax(self) -> None:
        for value in ("2026-10-19", "2024-02-29"):
            with self.subTest(valid=value):
                iso_date(value, "test")
        for value in ("20261019", "2026-W43-1", "2026-02-30",
                      "2026-1-09", "2026-10-19T00:00:00"):
            with self.subTest(invalid=value):
                with self.assertRaises(ValueError):
                    iso_date(value, "test")
        iso_date(None, "optional date", nullable=True)
        with self.assertRaises(ValueError):
            iso_date(None, "required date", nullable=False)

    def test_check_does_not_fall_back_to_script_checkout(self) -> None:
        # This catches the old bug where check(root) ignored root for almost all reads.
        with tempfile.TemporaryDirectory() as directory:
            selected_root = Path(directory)
            with self.assertRaises(FileNotFoundError):
                check(selected_root)
            with self.assertRaises(FileNotFoundError):
                self_test(selected_root)

    def test_independent_review_needs_nonempty_reviewer_and_date(self) -> None:
        schema = json_read(ROOT / "authoring/cases/case-record.schema.json")
        baseline = json_read(ROOT / "authoring/cases/examples/case-records.json")[0]
        refs = set(baseline["source_refs"])
        validate_record(baseline, schema, refs)

        for reviewer, date in (
            (None, "2026-10-19"),
            ("Independent Reviewer", None),
            ("   ", "2026-10-19"),
        ):
            with self.subTest(reviewer=reviewer, date=date):
                item = copy.deepcopy(baseline)
                item["status"] = "independent_reviewed"
                item["review"]["reviewer"] = reviewer
                item["review"]["reviewed_on"] = date
                with self.assertRaises(ValueError):
                    validate_record(item, schema, refs)

        metadata_only = copy.deepcopy(baseline)
        metadata_only["status"] = "independent_reviewed"
        metadata_only["review"]["reviewer"] = "Independent Reviewer"
        metadata_only["review"]["reviewed_on"] = "2026-10-19"
        validate_record(metadata_only, schema, refs)
        # Passing this structural test is never proof of real reviewer identity.

    def test_full_schema_rejects_empty_review_metadata_when_installed(self) -> None:
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema optional; Draft2020-12 engine NOT RUN")
        schema = json_read(ROOT / "authoring/cases/case-record.schema.json")
        record = json_read(ROOT / "authoring/cases/examples/case-records.json")[0]
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker())
        self.assertEqual([], list(validator.iter_errors(record)))
        record["status"] = "independent_reviewed"
        self.assertTrue(list(validator.iter_errors(record)))
        record["review"]["reviewer"] = "Independent Reviewer"
        record["review"]["reviewed_on"] = "2026-10-19"
        self.assertEqual([], list(validator.iter_errors(record)))


if __name__ == "__main__":
    unittest.main()
