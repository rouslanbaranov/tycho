"""Checks for the read-only bounded-book-change plan."""
import hashlib
import io
import json
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
import book_change
from book_change import (build_plan, delivery_state, diff_maps,
                         directory_revision_gaps, fts_state, owner_units_state,
                         semantic_audit_state, semantic_changes, state)
import section_fts_index


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fresh(label):
    return state(label, "fresh", "ok")


class BookChangePlanTests(unittest.TestCase):
    def test_repository_plan_shape(self):
        plan = build_plan(ROOT)
        for key in ("clean", "blocking", "changed_pages", "missing_revisions",
                    "artifacts", "steps", "limits"):
            self.assertIn(key, plan)
        artifacts = {row["artifact"] for row in plan["artifacts"]}
        self.assertIn("edition/patterns/semantic-audit.v1.json", artifacts)
        self.assertIn("edition/patterns/owner-units.v1.json", artifacts)
        self.assertIn("generated/" + section_fts_index.INDEX_NAME, artifacts)

    def test_diff_maps_classifies_added_removed_changed(self):
        rows = diff_maps({"a": "1", "b": "2"}, {"a": "1", "b": "3", "c": "4"})
        self.assertEqual([row["path"] for row in rows], ["b", "c"])
        self.assertEqual([row["state"] for row in rows], ["changed", "added"])
        removed = diff_maps({"a": "1"}, {})
        self.assertEqual(removed[0]["state"], "removed")

    def test_directory_revision_gap_and_authorization(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "book/volumes/v01/c01/a.md"
            page.parent.mkdir(parents=True)
            page.write_text("new\n", encoding="utf-8")
            (root / "edition").mkdir()
            migration = {
                "schema_version": 1,
                "directories": [{"old": "book/v01", "new": "book/volumes/v01"}],
                "documents": [{
                    "old_path": "book/v01/c01/a.md",
                    "new_path": "book/volumes/v01/c01/a.md",
                    "baseline_sha256": sha("old\n"),
                }],
            }
            (root / "edition/directory-migration.json").write_text(
                json.dumps(migration), encoding="utf-8")
            revisions = {"schema_version": 1, "revisions": []}
            (root / "edition/content-revisions.json").write_text(
                json.dumps(revisions), encoding="utf-8")

            gaps = directory_revision_gaps(root)
            self.assertEqual(len(gaps), 1)
            self.assertEqual(gaps[0]["kind"], "directory_documents")
            self.assertEqual(gaps[0]["previous_sha256"], sha("old\n"))
            self.assertEqual(gaps[0]["current_sha256"], sha("new\n"))

            revisions["revisions"].append({
                "issue": 384,
                "authorized_at": "2026-10-24",
                "directory_documents": [{
                    "path": "book/volumes/v01/c01/a.md",
                    "previous_sha256": sha("old\n"),
                    "current_sha256": sha("new\n"),
                }],
            })
            (root / "edition/content-revisions.json").write_text(
                json.dumps(revisions), encoding="utf-8")
            self.assertEqual(directory_revision_gaps(root), [])

    def test_semantic_changes_detect_hash_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "book").mkdir()
            (root / "book/a.md").write_text("new\n", encoding="utf-8")
            (root / "edition/patterns").mkdir(parents=True)
            audit = {"pages": [{"path": "book/a.md", "sha256": sha("old\n")}]}
            (root / "edition/patterns/semantic-audit.v1.json").write_text(
                json.dumps(audit), encoding="utf-8")
            rows = semantic_changes(root)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["current_sha256"], sha("new\n"))

            audit["pages"][0]["sha256"] = sha("new\n")
            (root / "edition/patterns/semantic-audit.v1.json").write_text(
                json.dumps(audit), encoding="utf-8")
            self.assertEqual(semantic_changes(root), [])

    def test_missing_semantic_audit_is_blocking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "edition/patterns").mkdir(parents=True)
            item = semantic_audit_state(root, {"documents": []})
            self.assertEqual(item["state"], "missing")
            self.assertTrue(item["blocking"])

    def test_fts_uses_current_index_name(self):
        item = fts_state(Path("/tmp"), {"snapshot_sha256": "x"})
        self.assertEqual(item["artifact"], "generated/" + section_fts_index.INDEX_NAME)
        self.assertNotIn("v3", item["artifact"])

    def test_owner_units_validator_error_is_blocking(self):
        with mock.patch.object(book_change.validate_pattern_owner_units, "validate",
                               side_effect=ValueError("owner-units-summary-mismatch")):
            item = owner_units_state(ROOT)
        self.assertEqual(item["state"], "stale")
        self.assertTrue(item["blocking"])

    def test_semantic_audit_validator_error_is_blocking(self):
        route = book_change.canonical_scan(ROOT)
        with mock.patch.object(book_change.validate_pattern_semantic_audit, "validate",
                               side_effect=ValueError("semantic-audit-summary-mismatch")):
            item = semantic_audit_state(ROOT, route)
        self.assertEqual(item["state"], "stale")
        self.assertTrue(item["blocking"])

    def test_delivery_validator_error_is_blocking(self):
        route = book_change.canonical_scan(ROOT)
        with mock.patch.object(book_change.validate_delivery_evidence, "validate",
                               side_effect=ValueError("delivery-owner-acceptance-claim")):
            item = delivery_state(ROOT, route)
        self.assertEqual(item["state"], "stale")
        self.assertTrue(item["blocking"])

    def test_strict_blocks_on_stale_artifact(self):
        route = {"documents": [], "snapshot_sha256": "x"}
        stale = state("probe", "stale", "test", "fix", True)
        with mock.patch.multiple(
                book_change,
                canonical_scan=mock.Mock(return_value=route),
                changed_book_pages=mock.Mock(return_value=[]),
                directory_revision_gaps=mock.Mock(return_value=[]),
                enrichment_revision_gaps=mock.Mock(return_value=[]),
                atlas_changes=mock.Mock(return_value=[]),
                semantic_changes=mock.Mock(return_value=[]),
                route_state=mock.Mock(return_value=fresh("route")),
                fts_state=mock.Mock(return_value=state("fts", "not-built", "absent")),
                census_state=mock.Mock(return_value=fresh("census")),
                coverage_state=mock.Mock(return_value=fresh("coverage")),
                phase4_state=mock.Mock(return_value=fresh("phase4")),
                source_plan_state=mock.Mock(return_value=fresh("plan")),
                delivery_state=mock.Mock(return_value=stale),
                owner_units_state=mock.Mock(return_value=fresh("owner")),
                semantic_audit_state=mock.Mock(return_value=fresh("semantic")),
                inventory_state=mock.Mock(return_value=fresh("inventory"))):
            plan = book_change.build_plan("/tmp")
            self.assertTrue(plan["blocking"])
            with redirect_stdout(io.StringIO()) as out:
                code = book_change.main(["--root", "/tmp", "--json", "--strict"])
            self.assertEqual(code, 1)
            self.assertTrue(json.loads(out.getvalue())["blocking"])

    def test_scan_failure_returns_blocking_json(self):
        with mock.patch.object(book_change, "canonical_scan",
                               side_effect=ValueError("bad metadata")):
            plan = book_change.build_plan("/tmp")
            self.assertTrue(plan["blocking"])
            self.assertIn("bad metadata", plan["error"])
            with redirect_stdout(io.StringIO()) as out:
                code = book_change.main(["--root", "/tmp", "--json", "--strict"])
            self.assertEqual(code, 1)
            self.assertIn("bad metadata", json.loads(out.getvalue())["error"])

    def test_phase4_builder_error_is_reported(self):
        route = {"documents": [], "snapshot_sha256": "x"}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "edition/patterns").mkdir(parents=True)
            (root / "edition/patterns/phase4.v1.json").write_text("{}")
            with mock.patch.multiple(
                book_change,
                canonical_scan=mock.Mock(return_value=route),
                changed_book_pages=mock.Mock(return_value=[]),
                directory_revision_gaps=mock.Mock(return_value=[]),
                enrichment_revision_gaps=mock.Mock(return_value=[]),
                atlas_changes=mock.Mock(return_value=[]),
                semantic_changes=mock.Mock(return_value=[]),
                route_state=mock.Mock(return_value=fresh("route")),
                fts_state=mock.Mock(return_value=state("fts", "not-built", "absent")),
                census_state=mock.Mock(return_value=fresh("census")),
                coverage_state=mock.Mock(return_value=fresh("coverage")),
                source_plan_state=mock.Mock(return_value=fresh("plan")),
                delivery_state=mock.Mock(return_value=fresh("delivery")),
                owner_units_state=mock.Mock(return_value=fresh("owner")),
                semantic_audit_state=mock.Mock(return_value=fresh("semantic")),
                inventory_state=mock.Mock(return_value=fresh("inventory")),
                phase4_audit=mock.Mock(build=mock.Mock(
                    side_effect=ValueError("phase4-page-count")))):
                plan = build_plan(root)
        rows = [row for row in plan["artifacts"]
                if row["artifact"] == "edition/patterns/phase4.v1.json"]
        self.assertEqual(rows[0]["state"], "unavailable")
        self.assertTrue(plan["blocking"])


if __name__ == "__main__":
    unittest.main()
