"""Canonical M9 source identities without an alias compatibility layer."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from route_index import FENCE, engine
from validate_book_metadata import validate
from validate_sources import validate as validate_sources
from validate_m9_cases import parse_source_registry


class M9SourceIdentityTests(unittest.TestCase):
    def inventory(self):
        return parse_source_registry((ROOT / 'sources/REAL_WORLD_ARCHITECTURE_CASES.md').read_text())

    def test_no_legacy_source_or_evidence_labels_in_m9_content(self):
        aliases = [sid.removeprefix('src.m9-').upper() for sid in self.inventory()]
        legacy = re.compile(r'(?<![A-Za-z0-9_.-])(?:' + '|'.join(aliases) + r')(?:\.[0-9]+)?(?![A-Za-z0-9_-])')
        paths = [*(ROOT / 'book/cases').rglob('*.md'),
                 *(ROOT / 'sources').glob('REAL_WORLD*.md'),
                 *(ROOT / 'authoring/cases').rglob('*.md'),
                 *(ROOT / 'authoring').glob('M9*.md'),
                 *(ROOT / 'tests/fixtures').glob('m9-*.json'),
                 ROOT / 'sources/register.json',
                 ROOT / 'authoring/cases/examples/case-records.json']
        for path in paths:
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertIsNone(legacy.search(path.read_text()))

    def test_inventory_preserves_exact_global_urls(self):
        register = json.loads((ROOT / 'sources/register.json').read_text())
        validate_sources(register)
        sources = {s['id']: s['url'] for s in register['sources']}
        inventory = self.inventory()
        self.assertEqual(len(inventory), 43)
        for sid, url in inventory.items():
            with self.subTest(source=sid):
                self.assertEqual(sources[sid], url)

    def test_pages_retain_the_exact_source_link(self):
        inventory = self.inventory()
        used = set()
        yaml, _, _ = engine()
        for path in (ROOT / 'book/cases').glob('*.md'):
            text = path.read_text()
            header = FENCE.match(text)
            meta = yaml.safe_load(header[1])
            ids = set(meta['evidence_scope']['source_ids']) & inventory.keys()
            for sid in ids:
                with self.subTest(path=path.name, source=sid):
                    self.assertIn(inventory[sid], text[header.end():])
            used.update(ids)
        self.assertTrue(used)

    def test_actual_corpus_retains_strict_metadata_and_reference_integrity(self):
        self.assertEqual(validate(ROOT)['coverage'], 'complete')


if __name__ == '__main__':
    unittest.main()
