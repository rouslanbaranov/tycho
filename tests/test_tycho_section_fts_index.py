"""Offline section-index tests with synthetic canonical route snapshots.

No external corpus, YAML/schema dependencies, real book rewriting or network.
"""
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import section_fts_index as idx  # noqa: E402

PAGE_A = (
    "---\nid: tycho.page.alpha\nkind: page\ntitle: Alpha page\n---\n"
    "# Alpha page\n\nOverview text about bounded retrieval.\n\n"
    "## Retry policy {#retry-anchor}\nRetry detail with token zebra.\n\n"
    "### Nested detail {#nested-anchor}\nNested text stays in its parent section.\n\n"
    "### Nested detail\nSecond nested note.\n\n"
    "## Retry\nSecond retry section.\n\n"
    "~~~python\n## Not A Heading\n### Not A Passage\n~~~\n"
)
PAGE_B = (
    "---\nid: tycho.page.beta\nkind: landing\ntitle: Beta landing\n---\n"
    "# Beta landing\n\nOnly overview content, no level-two heading.\n"
)


class SectionIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="tycho-section-fixture-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "book").mkdir()
        (self.root / "generated").mkdir()
        self.a = self.root / "book" / "a.md"
        self.b = self.root / "book" / "b.md"
        self.a.write_text(PAGE_A, encoding="utf-8")
        self.b.write_text(PAGE_B, encoding="utf-8")

    def docs(self):
        docs = []
        for path, identity, kind, title, topics, evidence in (
                (self.a, "tycho.page.alpha", "page", "Alpha page",
                 ["search-architecture", "caching"], "source-linked"),
                (self.b, "tycho.page.beta", "landing", "Beta landing",
                 ["deployment"], "unknown")):
            text = path.read_text(encoding="utf-8")
            docs.append({
                "id": identity, "path": path.relative_to(self.root).as_posix(),
                "title": title, "kind": kind, "topics": topics,
                "evidence_status": evidence,
                "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            })
        return docs

    def fake_scan(self, root, allow_partial):
        docs = self.docs()
        snapshot = hashlib.sha256(
            "|".join(d["id"] + d["sha256"] for d in docs).encode()).hexdigest()
        return {"snapshot_sha256": snapshot, "coverage": "complete",
                "unannotated_paths": [], "documents": docs}

    def partial_scan(self, root, allow_partial):
        if not allow_partial:
            raise ValueError("1 unannotated Markdown page")
        state = self.fake_scan(root, allow_partial)
        state["coverage"] = "partial"
        state["unannotated_paths"] = ["book/unannotated.md"]
        return state

    def publish(self, **kwargs):
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return idx.publish(self.root, **kwargs)

    def verify(self):
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            return idx.verify(self.root)

    def test_overview_and_h2_sections_only(self):
        page = self.docs()[0]
        rows = idx.parse_sections(page, self.a.read_text(encoding="utf-8"))
        self.assertEqual([r["section_id"] for r in rows],
                         ["overview", "retry-anchor", "retry"])
        self.assertEqual([r["heading_level"] for r in rows], [0, 2, 2])
        self.assertEqual(rows[0]["heading"], "Alpha page")
        self.assertIn("### Nested detail", rows[1]["content"])
        self.assertNotIn("Not A Heading", [r["heading"] for r in rows])
        for section in rows:
            text = self.a.read_text(encoding="utf-8")
            self.assertEqual(
                text[section["char_start"]:section["char_end"]],
                section["content"])
        self.assertFalse(idx.body_of(rows[1]).startswith("## Retry policy"))
        self.assertIn("token zebra", idx.body_of(rows[1]))

    def test_h3_passages_need_parent_h2_and_stable_keys(self):
        page = self.docs()[0]
        text = self.a.read_text(encoding="utf-8")
        rows = idx.parse_sections(page, text)
        passages = idx.parse_passages(rows[1])
        self.assertEqual([p["passage_id"] for p in passages],
                         ["nested-anchor", "nested-detail"])
        self.assertEqual(
            [p["passage_key"] for p in passages],
            ["tycho.page.alpha#retry-anchor~nested-anchor",
             "tycho.page.alpha#retry-anchor~nested-detail"])
        self.assertEqual(
            [p["heading"] for p in passages],
            ["Nested detail", "Nested detail"])
        self.assertEqual([p["heading_level"] for p in passages], [3, 3])
        for passage in passages:
            self.assertEqual(passage["parent_section_key"],
                             rows[1]["section_key"])
            self.assertEqual(passage["parent_section_id"], "retry-anchor")
            self.assertEqual(passage["document_id"], page["id"])
            self.assertEqual(passage["path"], page["path"])
            self.assertEqual(passage["char_start"],
                             text.index(passage["content"]))
            self.assertEqual(
                text[passage["char_start"]:passage["char_end"]],
                passage["content"])
            self.assertFalse(passage["body"].startswith("### "))
            self.assertEqual(passage["body"],
                             passage["content"].partition("\n")[2])
        self.assertIn("Second nested note", passages[1]["content"])
        self.assertEqual(idx.parse_passages(rows[2]), [])
        with self.assertRaisesRegex(ValueError, "level-2 parent"):
            idx.parse_passages(rows[0])

    def test_published_index_contains_internal_passages_and_parent_mapping(self):
        self.publish(full=True)
        path = self.root / "generated" / idx.INDEX_NAME
        with sqlite3.connect(path) as db:
            manifest = json.loads(db.execute(
                "SELECT value FROM meta WHERE key='manifest'").fetchone()[0])
            self.assertEqual(manifest["format_version"], 5)
            self.assertEqual(manifest["passage_count"], 2)
            self.assertEqual(manifest["section_count"], 4)
            self.assertEqual(db.execute(
                "SELECT count(*) FROM sections").fetchone()[0], 4)
            self.assertEqual(db.execute(
                "SELECT count(*) FROM passages").fetchone()[0], 2)
            rows = db.execute(
                "SELECT passage_key,passage_id,parent_section_key,"
                "parent_section_id,heading,heading_level,content,body,"
                "char_start,char_end FROM passages ORDER BY passage_key"
            ).fetchall()
            self.assertEqual([row[1] for row in rows],
                             ["nested-anchor", "nested-detail"])
            for key, passage_id, parent_key, parent_id, heading, level, \
                    content, body, start, end in rows:
                self.assertEqual(key, parent_key + "~" + passage_id)
                self.assertEqual(parent_key,
                                 "tycho.page.alpha#retry-anchor")
                self.assertEqual(parent_id, "retry-anchor")
                self.assertEqual(heading, "Nested detail")
                self.assertEqual(level, 3)
                self.assertTrue(content.startswith("### "))
                self.assertEqual(body, content.partition("\n")[2])
                self.assertLess(start, end)
            self.assertEqual(db.execute(
                "SELECT count(*) FROM passage_fts").fetchone()[0], 2)
            self.assertEqual(
                db.execute("SELECT count(*) FROM fts").fetchone()[0], 4)
            topics = db.execute(
                "SELECT section_key FROM section_topics"
                " WHERE topic='search-architecture' ORDER BY section_key"
            ).fetchall()
            self.assertEqual([row[0] for row in topics],
                             ["tycho.page.alpha#overview",
                              "tycho.page.alpha#retry",
                              "tycho.page.alpha#retry-anchor"])

    def test_tampered_passage_payload_is_rejected(self):
        self.publish()
        path = self.root / "generated" / idx.INDEX_NAME
        with sqlite3.connect(path) as db:
            key = db.execute(
                "SELECT passage_key FROM passage_fts LIMIT 1").fetchone()[0]
            db.execute("UPDATE passage_fts SET body='tampered-passage'"
                       " WHERE passage_key=?", (key,))
            db.commit()
        with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
            self.verify()
        with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
            self.publish()

    def test_incompatible_index_format_is_not_reused(self):
        self.assertEqual(idx.VERSION, 5)
        self.assertTrue(idx.INDEX_NAME.endswith("v5.sqlite"))
        self.publish()
        path = self.root / "generated" / idx.INDEX_NAME
        with sqlite3.connect(path) as db:
            raw = db.execute(
                "SELECT value FROM meta WHERE key='manifest'").fetchone()[0]
            manifest = json.loads(raw)
            manifest["format_version"] = 3
            db.execute("UPDATE meta SET value=? WHERE key='manifest'",
                       (idx.canonical_json(manifest),))
            db.commit()
        with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
            self.publish()
        fresh = self.publish(full=True)
        self.assertEqual(fresh["outcome"], "published")
        self.assertEqual(self.verify()["snapshot"], fresh["snapshot"])

    def test_full_incremental_and_unchanged_are_reproducible(self):
        a_before = self.a.read_bytes()
        b_before = self.b.read_bytes()
        first = self.publish(full=True)
        self.assertEqual(first["outcome"], "published")
        self.assertEqual(first["documents"], 2)
        self.assertEqual(first["sections"], 4)
        self.assertEqual(self.verify()["coverage"], "complete")
        again = self.publish()
        self.assertEqual(again["outcome"], "unchanged")
        self.assertEqual(again["snapshot"], first["snapshot"])
        self.assertEqual(again["reused_documents"], 2)
        full = self.publish(full=True)
        self.assertEqual(full["snapshot"], first["snapshot"])
        self.assertEqual(self.a.read_bytes(), a_before)
        self.assertEqual(self.b.read_bytes(), b_before)
        with sqlite3.connect(self.root / "generated" / idx.INDEX_NAME) as db:
            keys = [r[0] for r in db.execute(
                "SELECT section_key FROM sections ORDER BY section_key")]
            self.assertEqual(len(keys), 4)
            self.assertEqual(len(set(keys)), 4)
            self.assertEqual(db.execute(
                "SELECT count(*) FROM fts").fetchone()[0], 4)
            topics = db.execute(
                "SELECT topic FROM section_topics"
                " WHERE section_key='tycho.page.alpha#overview'"
                " ORDER BY topic").fetchall()
            self.assertEqual([t[0] for t in topics],
                             ["caching", "search-architecture"])

    def test_changed_document_requires_new_snapshot_and_reuses_unchanged(self):
        old = self.publish()
        self.a.write_text(
            self.a.read_text() + "\n## Extra\nNew note.\n\n"
            "### Extra passage\nNew H3 note.\n",
            encoding="utf-8")
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            with self.assertRaisesRegex(ValueError, "stale"):
                idx.verify(self.root)
        new = self.publish()
        self.assertNotEqual(old["snapshot"], new["snapshot"])
        self.assertEqual(new["reused_documents"], 1)
        self.assertEqual(new["passages"], 3)
        with sqlite3.connect(self.root / "generated" / idx.INDEX_NAME) as db:
            keys = [row[0] for row in db.execute(
                "SELECT passage_key FROM passages ORDER BY passage_key")]
        self.assertIn("tycho.page.alpha#extra~extra-passage", keys)
        self.assertEqual(self.verify()["snapshot"], new["snapshot"])

    def test_tampered_fts_payload_is_rejected(self):
        self.publish()
        path = self.root / "generated" / idx.INDEX_NAME
        with sqlite3.connect(path) as db:
            key = db.execute("SELECT section_key FROM fts LIMIT 1").fetchone()[0]
            db.execute("UPDATE fts SET body='tampered-index-payload'"
                       " WHERE section_key=?", (key,))
            db.commit()
        with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
            self.verify()
        with self.assertRaisesRegex(ValueError, "corrupt/incompatible"):
            self.publish()

    def test_corrupt_section_identity_is_not_reused(self):
        self.publish()
        with sqlite3.connect(self.root / "generated" / idx.INDEX_NAME) as db:
            db.execute("UPDATE sections SET section_id='forged' WHERE rowid=1")
            db.commit()
        with self.assertRaises(ValueError):
            self.verify()

    def test_unsafe_index_destination_is_blocked(self):
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.fake_scan):
            with self.assertRaisesRegex(ValueError, "under generated"):
                idx.publish(self.root, self.root / "book" / "illegal.sqlite")
            outside = self.root / "generated" / idx.INDEX_NAME
            outside.symlink_to(self.a)
            with self.assertRaisesRegex(ValueError, "under generated"):
                idx.publish(self.root)

    def test_target_sqlite_fts5_profile_is_checked(self):
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

    def test_partial_coverage_requires_explicit_flag(self):
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.partial_scan):
            with self.assertRaisesRegex(ValueError, "unannotated"):
                idx.publish(self.root)
            result = idx.publish(self.root, allow_partial=True)
        self.assertEqual(result["outcome"], "published")
        with patch.object(idx.route_index, "canonical_scan",
                          side_effect=self.partial_scan):
            verified = idx.verify(self.root)
        self.assertEqual(verified["coverage"], "partial")
        self.assertEqual(verified["unannotated_count"], 1)

    def test_incomplete_metadata_is_not_misrepresented(self):
        with patch.object(idx.route_index, "canonical_scan", return_value={
                "snapshot_sha256": "0" * 64, "coverage": "partial",
                "unannotated_paths": ["book/a.md"], "documents": []}):
            with self.assertRaisesRegex(ValueError, "No validated"):
                idx.publish(self.root)


if __name__ == "__main__":
    unittest.main()
