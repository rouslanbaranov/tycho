"""Corpus metadata regressions: reject invalid identity and provenance references."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_book_metadata as validator
import frontmatter_generate as front


class CorpusMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'sources').mkdir()
        (self.root / 'schemas').mkdir()
        shutil.copy(ROOT / 'schemas/document-metadata.v1.schema.json', self.root / 'schemas')
        self.meta = json.loads((ROOT / 'fixtures/metadata-valid-book.v1.json').read_text())
        self.meta['route_hints']['related_ids'] = []
        self.write_page()
        self.registry = {'schema_version': 1, 'documents': [{
            'id': self.meta['id'], 'kind': 'book', 'canonical_path': 'book/README.md',
            'authored_at': self.meta['authored_at']}]}
        self.write_json('document-identities.json', self.registry)
        self.write_json('document-topics.json', {'schema_version': 1, 'topics': [{'id': 'system-design'}]})
        self.write_json('register.json', {'sources': []})
        self.write_json('claim-references.json', {'claims': []})

    def write_json(self, name, value):
        (self.root / 'sources' / name).write_text(json.dumps(value))

    def write_page(self):
        p = self.root / 'book/README.md'
        p.parent.mkdir(exist_ok=True)
        p.write_text(front.render(self.meta) + '\n# Synthetic book\n')

    def test_valid_complete_corpus(self):
        self.assertEqual(validator.validate(self.root)['coverage'], 'complete')

    def test_identity_cannot_be_silently_reminted(self):
        self.meta['id'] = 'tycho.book.different1'
        self.write_page()
        with self.assertRaisesRegex(ValueError, 'identity registry mismatch'):
            validator.validate(self.root)

    def test_unannotated_page_is_not_complete(self):
        (self.root / 'book/extra.md').write_text('# Extra page\n')
        with self.assertRaisesRegex(ValueError, 'unannotated'):
            validator.validate(self.root)

    def test_unknown_topic_is_rejected(self):
        self.meta['topic_ids'] = ['unregistered-topic']
        self.write_page()
        with self.assertRaisesRegex(ValueError, 'unknown taxonomy topic'):
            validator.validate(self.root)

    def test_unknown_source_or_claim_is_rejected(self):
        for key, value in [('source_ids', 'src.missing'), ('claim_ids', 'claim.missing')]:
            with self.subTest(field=key):
                self.meta['evidence_scope']['source_ids'] = []
                self.meta['evidence_scope']['claim_ids'] = []
                self.meta['evidence_scope'][key] = [value]
                self.write_page()
                with self.assertRaisesRegex(ValueError, 'unknown (source|claim) ID'):
                    validator.validate(self.root)

    def test_registered_origin_date_is_preserved(self):
        self.meta['authored_at'] = '2026-10-18'
        self.write_page()
        with self.assertRaisesRegex(ValueError, 'authored date differs'):
            validator.validate(self.root)

    def test_local_m9_alias_is_not_a_global_source_id(self):
        self.meta['evidence_scope']['source_ids'] = ['A01']
        self.write_page()
        with self.assertRaisesRegex(ValueError, 'invalid strict metadata'):
            validator.validate(self.root)

    def test_registered_m9_identity_is_valid_without_claiming_review(self):
        self.meta['evidence_scope']['source_ids'] = ['src.m9-a01']
        self.write_json('register.json', {'sources': [{'id': 'src.m9-a01'}]})
        self.write_page()
        self.assertEqual(validator.validate(self.root)['coverage'], 'complete')

    def test_prefix_alone_does_not_register_a_source(self):
        self.meta['evidence_scope']['source_ids'] = ['src.m9-a01']
        self.write_page()
        with self.assertRaisesRegex(ValueError, 'unknown source ID'):
            validator.validate(self.root)


if __name__ == '__main__':
    unittest.main()
