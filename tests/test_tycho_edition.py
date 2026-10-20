"""Migration regression checks: evidence, identity, content and hierarchy loss."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_edition import check_migration, inventory_members
from assemble_edition import split, MARKER, rewrite_links
from frontmatter_generate import render


class EditionMigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.outline=json.loads((ROOT/'edition/outline.json').read_text())
        self.migration=json.loads((ROOT/'edition/migration.json').read_text())
        paths=['book/README.md']
        paths += [v['path'] for v in self.outline['volumes']]
        paths += [c['path'] for c in self.outline['chapters']]
        paths += [r['new_path'] for r in self.migration['documents']]
        for path in paths:
            target=self.root/path;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/path,target)
        self.row=self.migration['documents'][0]
        self.path=self.root/self.row['new_path']

    def check(self):
        return check_migration(self.root,self.outline,self.migration)

    def test_preserved_complete_migration(self):
        self.assertEqual(self.check()['migrated_pages'],69)

    def test_payload_loss_rejected(self):
        self.path.write_text(self.path.read_text().replace('## Purpose and mission','## Removed original section',1))
        with self.assertRaisesRegex(ValueError,'lost-or-altered-payload'):
            self.check()

    def test_new_page_identity_rejected(self):
        meta,body=split(self.path.read_text());meta['id']='tycho.page.123456'
        self.path.write_text(render(meta)+body)
        with self.assertRaisesRegex(ValueError,'changed-page-id'):
            self.check()

    def test_wrong_parent_rejected(self):
        meta,body=split(self.path.read_text());meta['parent_id']=self.row['old_parent_id']
        self.path.write_text(render(meta)+body)
        with self.assertRaisesRegex(ValueError,'changed-page-parent'):
            self.check()

    def test_fabricated_verification_rejected(self):
        meta,body=split(self.path.read_text());meta['source_inspection_date']='2026-10-20'
        self.path.write_text(render(meta)+body)
        with self.assertRaisesRegex(ValueError,'changed-evidence-metadata'):
            self.check()

    def test_missing_page_rejected(self):
        self.path.unlink()
        with self.assertRaisesRegex(ValueError,'missing-primary-page'):
            self.check()

    def test_duplicate_canonical_copy_rejected(self):
        old=self.root/self.row['old_path'];old.parent.mkdir(parents=True,exist_ok=True);old.write_text('# Duplicate\n')
        with self.assertRaisesRegex(ValueError,'duplicate-canonical-old-path'):
            self.check()

    def test_duplicate_outline_owner_rejected(self):
        self.outline['chapters'][1]['code']=self.outline['chapters'][0]['code']
        with self.assertRaisesRegex(ValueError,'duplicate-chapter-code'):
            self.check()

    def test_missing_volume_synthesis_rejected(self):
        v=self.outline['volumes'][0];p=self.root/v['path']
        p.write_text(p.read_text().replace(v['counterexample'],'Removed'))
        with self.assertRaisesRegex(ValueError,'volume-synthesis-content'):
            self.check()

    def test_fragment_external_and_moved_link_semantics(self):
        moves={'book/a.md':'book/volumes/v01/c01/a.md'}
        old='[self](#scope) [web](https://example.org/x#y) [page](a.md#details)'
        result=rewrite_links(old,'book/b.md','book/b.md',moves)
        self.assertEqual(result,'[self](#scope) [web](https://example.org/x#y) [page](volumes/v01/c01/a.md#details)')

    def test_evidence_url_tampering_rejected_even_with_new_payload_hash(self):
        from assemble_edition import sha
        meta,body=split(self.path.read_text())
        original=self.row['external_urls'][0]
        body=body.replace(original,'https://example.invalid/replaced')
        self.path.write_text(render(meta)+body)
        self.row['migrated_payload_sha256']=sha(body.split(MARKER)[0])
        with self.assertRaisesRegex(ValueError,'changed-external-citations'):
            self.check()


if __name__=='__main__':
    unittest.main()
