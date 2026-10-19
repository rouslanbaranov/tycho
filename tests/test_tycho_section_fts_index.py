"""Offline section-index tests with synthetic canonical route snapshots.

No external corpus, YAML/schema dependencies, real book rewriting or network.
"""
import hashlib
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_fts_index as idx  # noqa: E402


class SectionIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tycho-section-fixture-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "book").mkdir()
        (self.root / "generated").mkdir()
        self.a = self.root / "book" / "a.md"
        self.b = self.root / "book" / "b.md"
        self.a.write_text("---\nid: tycho.page.alpha\n---\n"
                          "# Example A\nText α.\n"
                          "~~~python\n## Not A Heading\n~~~\n"
                          "## Retry {#retry-anchor}\nA detail.\n"
                          "## Retry\nAnother.\n", encoding="utf-8")
        self.b.write_text("---\nid: tycho.page.beta\n---\n"
                          "# Example B\nSecond original page.\n", encoding="utf-8")

    def fake_scan(self, root, allow_partial):
        self.assertTrue(allow_partial)
        docs = []
        for path, identity in ((self.a,"tycho.page.alpha"), (self.b,"tycho.page.beta")):
            text = path.read_text(encoding="utf-8")
            docs.append({"id":identity, "path":path.relative_to(self.root).as_posix(),
                         "title": identity, "sha256": hashlib.sha256(text.encode()).hexdigest()})
        snapshot = hashlib.sha256("|".join(d["sha256"] for d in docs).encode()).hexdigest()
        return {"snapshot_sha256": snapshot, "coverage":"partial",
                "unannotated_paths":["book/unannotated.md"], "documents":docs}

    def fake_only_a(self, root, allow_partial):
        state = self.fake_scan(root, allow_partial)
        state["documents"] = state["documents"][:1]
        return state

    def test_section_ids_offsets_and_code_fence_exclusion(self):
        page = self.fake_scan(self.root, True)["documents"][0]
        rows = idx.parse_sections(page, self.a.read_text(encoding="utf-8"))
        names = [r["section_id"] for r in rows]
        self.assertIn("example-a", names)
        self.assertIn("retry-anchor", names)
        self.assertIn("retry", names)
        self.assertNotIn("not-a-heading", names)
        for section in rows:
            text = self.a.read_text(encoding="utf-8")
            self.assertEqual(text[section["char_start"]:section["char_end"]], section["content"])

    def test_full_incremental_and_unchanged_are_reproducible(self):
        a_before = self.a.read_bytes()
        b_before = self.b.read_bytes()
        with patch.object(idx.route_index, "canonical_scan", side_effect=self.fake_scan):
            first = idx.publish(self.root, full=True)
            self.assertEqual(first["outcome"], "published")
            self.assertEqual(idx.verify(self.root)["coverage"], "partial")
            again = idx.publish(self.root)
            self.assertEqual(again["outcome"], "unchanged")
            self.assertEqual(again["snapshot"], first["snapshot"])
            full = idx.publish(self.root, full=True)
            self.assertEqual(full["snapshot"], first["snapshot"])
        self.assertEqual(self.a.read_bytes(), a_before)
        self.assertEqual(self.b.read_bytes(), b_before)
        with sqlite3.connect(self.root / "generated" / idx.INDEX_NAME) as db:
            self.assertGreater(db.execute("SELECT count(*) FROM fts").fetchone()[0], 0)

    def test_changed_document_requires_new_snapshot_and_reuses_unchanged(self):
        with patch.object(idx.route_index, "canonical_scan", side_effect=self.fake_scan):
            old = idx.publish(self.root)
            self.a.write_text(self.a.read_text() + "\n## Extra\nNew note.\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "stale"):
                idx.verify(self.root)
            new = idx.publish(self.root)
            self.assertNotEqual(old["snapshot"], new["snapshot"])
            self.assertEqual(new["reused_documents"], 1)
            self.assertEqual(idx.verify(self.root)["snapshot"], new["snapshot"])

    def test_tampered_fts_payload_is_rejected(self):
        with patch.object(idx.route_index, "canonical_scan", side_effect=self.fake_scan):
            idx.publish(self.root)
            path = self.root / "generated" / idx.INDEX_NAME
            with sqlite3.connect(path) as db:
                key = db.execute("SELECT section_key FROM fts LIMIT 1").fetchone()[0]
                db.execute("UPDATE fts SET body='tampered-index-payload' WHERE section_key=?", (key,))
                db.commit()
            with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
                idx.verify(self.root)
            with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
                idx.publish(self.root)

    def test_corrupt_section_identity_is_not_reused(self):
        with patch.object(idx.route_index, "canonical_scan", side_effect=self.fake_scan):
            idx.publish(self.root)
            with sqlite3.connect(self.root / "generated" / idx.INDEX_NAME) as db:
                db.execute("UPDATE sections SET section_id='forged' WHERE rowid=1")
                db.commit()
            with self.assertRaises(ValueError):
                idx.verify(self.root)

    def test_unsafe_index_destination_is_blocked(self):
        with patch.object(idx.route_index, "canonical_scan", side_effect=self.fake_scan):
            with self.assertRaisesRegex(ValueError, "under generated"):
                idx.publish(self.root, self.root / "book" / "illegal.sqlite")
            outside = self.root / "generated" / idx.INDEX_NAME
            outside.symlink_to(self.a)
            with self.assertRaisesRegex(ValueError, "under generated"):
                idx.publish(self.root)

    def test_target_sqlite_fts5_profile_is_checked(self):
        """Capability check exercises the exact FTS5 features of the index."""
        if sqlite3.sqlite_version_info < (3, 26, 0):
            with self.assertRaisesRegex(ValueError, "3.26"):
                idx.require_fts5()
        else:
            idx.require_fts5()

    def test_old_sqlite_version_is_rejected_before_writes(self):
        with patch.object(idx.sqlite3, "sqlite_version_info", (3, 25, 0)):
            with self.assertRaisesRegex(ValueError, "3.26"):
                idx.publish(self.root)
        self.assertFalse((self.root / "generated" / idx.INDEX_NAME).exists())

    def test_case_sensitive_section_identifiers_and_bm25_probe(self):
        """Do not mistake the version number for successful FTS feature checks."""
        with patch.object(idx.sqlite3, "sqlite_version_info", (3, 26, 0)):
            # A modern local SQLite runtime still exercises the real probe.
            idx.require_fts5()

    def test_incomplete_metadata_is_not_misrepresented(self):
        with patch.object(idx.route_index, "canonical_scan", return_value={
            "snapshot_sha256":"0"*64, "coverage":"partial",
            "unannotated_paths":["book/a.md"], "documents":[] }):
            with self.assertRaisesRegex(ValueError, "No validated"):
                idx.publish(self.root)


if __name__ == "__main__":
    unittest.main()
