"""Checks for the read-only bounded-book-change plan."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from book_change import build_plan, diff_maps, directory_revision_gaps, semantic_changes


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class BookChangePlanTests(unittest.TestCase):
    def test_clean_repository_plan(self):
        plan = build_plan(ROOT)
        self.assertTrue(plan["clean"], plan["artifacts"])
        self.assertFalse(plan["blocking"])
        self.assertEqual(plan["changed_pages"], [])
        self.assertEqual(plan["missing_revisions"], [])
        self.assertEqual(plan["semantic_changes"], [])

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

    def test_cli_json_and_strict_exit(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts/book_change.py"),
             "--plan", "--json", "--strict"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        data = json.loads(completed.stdout)
        for key in ("clean", "blocking", "changed_pages", "missing_revisions",
                    "artifacts", "steps", "limits"):
            self.assertIn(key, data)


if __name__ == "__main__":
    unittest.main()
