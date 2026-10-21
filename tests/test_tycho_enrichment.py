"""Adversarial preservation and membership checks for authorized enrichment."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from validate_enrichment import validate
from directory_paths import HistoricalView


class EnrichmentTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in ('book', 'edition', 'schemas', 'sources'):
            shutil.copytree(ROOT/name, self.root/name)
        self.manifest = json.loads((self.root/'edition/enrichment-manifest.json').read_text())
        self.view = HistoricalView(self.root)

    def test_explicit_extension_preserves_baseline(self):
        result = validate(self.root)
        self.assertEqual(result['retained_document_ids'], 389)
        self.assertEqual(result['new_documents'], len(self.manifest['new_documents']))
        self.assertEqual(result['new_chapters'], 2)

    def test_removing_a_new_mechanism_is_rejected(self):
        page = next(x for x in self.manifest['new_documents'] if x['kind'] == 'page')
        self.view.path(page['path']).unlink()
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_changing_original_prose_outside_added_section_is_rejected(self):
        edit = self.manifest['modified_documents'][0]
        path = self.view.path(edit['path'])
        text = path.read_text()
        text = text.replace('## 4.', '## Changed.', 1)
        self.assertNotEqual(text, path.read_text())
        path.write_text(text)
        with self.assertRaisesRegex(ValueError, 'enrichment-baseline-altered'):
            validate(self.root)

    def test_replacing_added_failure_reasoning_is_rejected(self):
        edit = self.manifest['modified_documents'][0]
        path = self.view.path(edit['path'])
        path.write_text(path.read_text().replace('epoch 41', 'epoch 99', 1))
        with self.assertRaisesRegex(ValueError, 'enrichment-addition-drift'):
            validate(self.root)

    def test_lost_inspection_binding_is_rejected(self):
        path = self.root/self.manifest['inspection_record']
        record = json.loads(path.read_text())
        record['inspections'] = []
        path.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, 'enrichment-uninspected-source'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
