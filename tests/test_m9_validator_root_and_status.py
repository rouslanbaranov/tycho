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
    parse_source_registry,
    read_case_catalog,
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

    @staticmethod
    def _synthetic_cases(root: Path) -> Path:
        case_dir = root / "book/cases"
        case_dir.mkdir(parents=True)
        lines = []
        for i in range(20):
            filename = "case-%02d.md" % i
            lines.append("- [Case %02d](%s)" % (i, filename))
            (case_dir / filename).write_text(
                "# Case %02d\n\nCase ID: `case.synthetic.example-%02d`\n\n"
                "```mermaid\nflowchart TD\n  A --> B\n```\n\n"
                "https://example.org/engineering\n" % (i, i), encoding="utf-8")
        (case_dir / "README.md").write_text("\n".join(lines) + "\n",
                                            encoding="utf-8")
        return case_dir

    def test_valid_case_links_inside_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            source = root / "sources" / "public.md"
            source.parent.mkdir(parents=True)
            source.write_text("Synthetic source", encoding="utf-8")
            first = case_dir / "case-00.md"
            first.write_text(first.read_text(encoding="utf-8") +
                             "\n[Public source](../../sources/public.md)\n",
                             encoding="utf-8")
            ids, links = read_case_catalog(root)
            self.assertEqual(20, len(ids))
            self.assertEqual(20, len(links))

    def test_existing_file_outside_snapshot_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            outside = Path(workspace) / "private.md"
            outside.write_text("Must never be accepted as Tycho source",
                               encoding="utf-8")
            first = case_dir / "case-00.md"
            first.write_text(first.read_text(encoding="utf-8") +
                             "\n[Outside](../../../private.md)\n",
                             encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "escapes selected root"):
                read_case_catalog(root)

    def test_case_index_symlink_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            outside = Path(workspace) / "outside.md"
            outside.write_text("case.synthetic.outside\n", encoding="utf-8")
            alias = case_dir / "alias.md"
            try:
                alias.symlink_to(outside)
            except (NotImplementedError, OSError):
                self.skipTest("filesystem does not support test symlinks")
            index = case_dir / "README.md"
            index.write_text(index.read_text(encoding="utf-8") +
                             "- [Alias](alias.md)\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "escapes the selected case collection"):
                read_case_catalog(root)

    def test_symlinked_readme_is_rejected_before_read(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            readme = case_dir / "README.md"
            outside = Path(workspace) / "external-index.md"
            outside.write_text(readme.read_text(encoding="utf-8"),
                               encoding="utf-8")
            readme.unlink()
            try:
                readme.symlink_to(outside)
            except (NotImplementedError, OSError):
                self.skipTest("filesystem does not support test symlinks")
            with self.assertRaisesRegex(ValueError, "README index escapes its collection"):
                read_case_catalog(root)

    def test_symlinked_case_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            base = Path(workspace)
            outside = self._synthetic_cases(base / "external")
            root = base / "pinned"
            (root / "book").mkdir(parents=True)
            try:
                (root / "book/cases").symlink_to(outside, target_is_directory=True)
            except (NotImplementedError, OSError):
                self.skipTest("filesystem does not support test symlinks")
            with self.assertRaisesRegex(ValueError, "case collection escapes the selected root"):
                read_case_catalog(root)

    def test_contextual_index_link_stays_in_selected_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            good = root / "sources" / "REAL_WORLD_ARCHITECTURE_CASES.md"
            good.parent.mkdir(parents=True)
            good.write_text("Synthetic public source register", encoding="utf-8")
            index = case_dir / "README.md"
            index.write_text(index.read_text(encoding="utf-8") +
                             "\n- [Public source](../../sources/REAL_WORLD_ARCHITECTURE_CASES.md)\n",
                             encoding="utf-8")
            ids, pages = read_case_catalog(root)
            self.assertEqual(20, len(ids))
            self.assertEqual(20, len(pages))

    def test_contextual_index_link_cannot_escape_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            outside = Path(workspace) / "private.md"
            outside.write_text("Not in snapshot", encoding="utf-8")
            index = case_dir / "README.md"
            index.write_text(index.read_text(encoding="utf-8") +
                             "\n- [Outside](../../../private.md)\n",
                             encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "contextual link escapes"):
                read_case_catalog(root)

    def test_contextual_index_link_must_exist(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            index = case_dir / "README.md"
            index.write_text(index.read_text(encoding="utf-8") +
                             "\n- [Missing](../../sources/not-present.md)\n",
                             encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "broken contextual link"):
                read_case_catalog(root)

    def test_independent_review_needs_nonempty_reviewer_and_date(self) -> None:
        schema = json_read(ROOT / "authoring/cases/case-record.schema.json")
        baseline = json_read(ROOT / "authoring/cases/examples/case-records.json")[0]
        refs = parse_source_registry(
            (ROOT / "sources/REAL_WORLD_ARCHITECTURE_CASES.md").read_text(encoding="utf-8"))
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

    def test_curated_source_id_url_binding(self) -> None:
        schema = json_read(ROOT / "authoring/cases/case-record.schema.json")
        records = json_read(ROOT / "authoring/cases/examples/case-records.json")
        refs = parse_source_registry(
            (ROOT / "sources/REAL_WORLD_ARCHITECTURE_CASES.md").read_text(encoding="utf-8"))
        self.assertEqual(43, len(refs))
        for record in records:
            with self.subTest(valid=record["case_id"]):
                validate_record(record, schema, refs)

        case = next(record for record in records if record["source_refs"] == ["N11"])
        for url in (refs["ST01"], refs["N11"] + "-different-article",
                    "https://evil.example.org/" + refs["N11"].rsplit("/", 1)[-1]):
            with self.subTest(invalid_url=url):
                wrong = copy.deepcopy(case)
                wrong["claims"][0]["primary_url"] = url
                with self.assertRaisesRegex(ValueError, "URL disagrees"):
                    validate_record(wrong, schema, refs)

    def test_case_page_requires_a_curated_primary_url(self) -> None:
        with tempfile.TemporaryDirectory() as workspace:
            root = Path(workspace) / "pinned"
            case_dir = self._synthetic_cases(root)
            registered = {"N11": "https://example.org/engineering/primary"}
            for case_path in case_dir.glob("case-*.md"):
                case_path.write_text(
                    case_path.read_text(encoding="utf-8") +
                    "\nEvidence N11: https://example.org/engineering/primary\n",
                    encoding="utf-8")
            ids, pages = read_case_catalog(root, registered)
            self.assertEqual(20, len(ids))
            self.assertEqual(20, len(pages))
            first = case_dir / "case-00.md"
            first.write_text(first.read_text(encoding="utf-8").replace(
                registered["N11"], "https://example.org/engineering/different"),
                encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "no matching curated source"):
                read_case_catalog(root, registered)

    def test_curated_source_registry_rejects_duplicate_and_unparseable_urls(self) -> None:
        raw = (ROOT / "sources/REAL_WORLD_ARCHITECTURE_CASES.md").read_text(encoding="utf-8")
        refs = parse_source_registry(raw)
        self.assertEqual(43, len(refs))
        first = next(line for line in raw.splitlines() if line.startswith("| N11 |"))
        with self.assertRaisesRegex(ValueError, "duplicate primary source ID"):
            parse_source_registry(raw + "\n" + first + "\n")
        with self.assertRaisesRegex(ValueError, "missing HTTPS primary link"):
            parse_source_registry(raw.replace(first, first.replace(
                refs["N11"], "http://untrusted.example/blog"), 1))

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
