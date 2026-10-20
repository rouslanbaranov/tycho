"""Adversarial split-migration checks, never independent editorial acceptance."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_decomposition import validate
from assemble_edition import split
from frontmatter_generate import render
from decompose_chapters import extract_blocks,rebase


class EditionMigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        shutil.copytree(ROOT/'book',self.root/'book')
        (self.root/'edition').mkdir()
        for name in ('decomposition-plan.json','decomposition-manifest.json','migration.json'):
            shutil.copyfile(ROOT/'edition'/name,self.root/'edition'/name)
        self.plan=json.loads((self.root/'edition/decomposition-plan.json').read_text())
        self.chapter=self.plan['chapters'][0]
        self.page=self.root/self.chapter['pages'][0]['path']

    def check(self):
        return validate(self.root)

    def test_complete_payload_and_ownership(self):
        result=self.check()
        self.assertEqual(result['preserved_original_manuscripts'],69)
        self.assertEqual(result['new_question_pages'],sum(len(c['pages']) for c in self.plan['chapters']))

    def test_lost_prose_is_rejected(self):
        self.page.write_text(self.page.read_text().replace('## 1.','## Removed.',1))
        with self.assertRaisesRegex(ValueError,'altered-source-payload'):self.check()

    def test_new_page_identity_is_rejected(self):
        m,b=split(self.page.read_text());m['id']='tycho.page.123456';self.page.write_text(render(m)+b)
        with self.assertRaisesRegex(ValueError,'question-identity-parent'):self.check()

    def test_wrong_parent_is_rejected(self):
        m,b=split(self.page.read_text());m['parent_id']='tycho.chapter.123456';self.page.write_text(render(m)+b)
        with self.assertRaisesRegex(ValueError,'question-identity-parent'):self.check()

    def test_fabricated_source_inspection_is_rejected(self):
        m,b=split(self.page.read_text());m['source_inspection_date']='2026-10-20';self.page.write_text(render(m)+b)
        with self.assertRaisesRegex(ValueError,'fabricated-question-verification'):self.check()

    def test_missing_page_is_rejected(self):
        self.page.unlink()
        with self.assertRaisesRegex(ValueError,'missing-source-payload'):self.check()

    def test_duplicate_original_payload_is_rejected(self):
        m,b=split(self.page.read_text());m['id']='tycho.page.123456';m['canonical_path']='book/duplicate.md'
        (self.root/'book/duplicate.md').write_text(render(m)+b)
        with self.assertRaisesRegex(ValueError,'duplicate-source-payload'):self.check()

    def test_duplicate_owner_is_rejected(self):
        self.plan['chapters'][1]['code']=self.plan['chapters'][0]['code']
        (self.root/'edition/decomposition-plan.json').write_text(json.dumps(self.plan))
        with self.assertRaisesRegex(ValueError,'duplicate-chapter-code'):self.check()

    def test_removed_new_walkthrough_is_rejected(self):
        c=next(c for c in self.plan['chapters'] if c['code']=='V04/C05')
        p=next(p for p in c['pages'] if p['editorial_addition'])
        f=self.root/p['path'];f.write_text(f.read_text().replace(p['editorial_addition'],'Removed'))
        with self.assertRaisesRegex(ValueError,'missing-editorial-deepening'):self.check()

    def test_external_citation_change_is_rejected(self):
        manifest=json.loads((self.root/'edition/decomposition-manifest.json').read_text())
        record=manifest['source_bodies'][0]
        target=next(s['target'] for s in record['sections'] if any('https://' in b for b in extract_blocks((self.root/s['target']).read_text()).values()))
        p=self.root/target;p.write_text(p.read_text().replace('https://','http://'))
        with self.assertRaisesRegex(ValueError,'altered-source-payload'):self.check()

    def test_original_provenance_is_protected(self):
        p=self.root/self.chapter['source_page'];m,b=split(p.read_text())
        m['evidence_scope']['status']='independently-verified';p.write_text(render(m)+b)
        with self.assertRaisesRegex(ValueError,'altered-original-provenance'):self.check()

    def test_missing_chapter_source_ledger_is_rejected(self):
        p=self.root/self.chapter['chapter_path']
        p.write_text(p.read_text().replace('## Chapter source ledger','## Removed ledger route'))
        with self.assertRaisesRegex(ValueError,'missing-chapter-ledger'):self.check()

    def test_fragment_routing_keeps_external_urls(self):
        routes={('book/a.md','old'):('book/b.md','new')}
        result=rebase('[local](a.md#old) [external](https://example.org/x#y)','book/a.md','book/a.md',routes)
        self.assertEqual(result,'[local](b.md#new) [external](https://example.org/x#y)')


if __name__=='__main__':
    unittest.main()
