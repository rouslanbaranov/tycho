"""Integration regressions for the M9 exact-URL source identity bridge."""
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


class M9SourceIdentityTests(unittest.TestCase):
    def test_bridge_preserves_exact_inventory_urls(self):
        bridge = json.loads((ROOT / 'sources/m9-source-aliases.json').read_text())
        self.assertEqual(bridge['schema_version'], 1)
        self.assertEqual(bridge['inventory'], 'sources/REAL_WORLD_ARCHITECTURE_CASES.md')
        inventory = {}
        for line in (ROOT / bridge['inventory']).read_text().splitlines():
            match = re.match(r'\| ([A-Z]+[0-9]+) \| [^|]+ \| \[[^]]+\]\((https://[^)]+)\) \|', line)
            if match:
                self.assertNotIn(match[1], inventory)
                inventory[match[1]] = match[2]
        register = json.loads((ROOT / 'sources/register.json').read_text())
        validate_sources(register)
        sources = {s['id']: s for s in register['sources']}
        self.assertTrue(bridge['aliases'])
        self.assertEqual(len(set(bridge['aliases'].values())), len(bridge['aliases']))
        for alias, sid in bridge['aliases'].items():
            with self.subTest(alias=alias):
                self.assertIn(alias, inventory)
                self.assertIn(sid, sources)
                self.assertEqual(sources[sid]['url'], inventory[alias])

    def test_mapped_pages_retain_the_exact_source_link(self):
        bridge = json.loads((ROOT / 'sources/m9-source-aliases.json').read_text())
        sources = {s['id']: s for s in json.loads((ROOT / 'sources/register.json').read_text())['sources']}
        mapped = set(bridge['aliases'].values())
        used = set()
        yaml, _, _ = engine()
        for path in (ROOT / 'book/cases').glob('*.md'):
            text = path.read_text()
            header = FENCE.match(text)
            meta = yaml.safe_load(header[1])
            ids = set(meta['evidence_scope']['source_ids']) & mapped
            for sid in ids:
                with self.subTest(path=path.name, source=sid):
                    self.assertIn(sources[sid]['url'], text[header.end():])
            used.update(ids)
        self.assertEqual(used, mapped)

    def test_actual_corpus_retains_strict_metadata_and_reference_integrity(self):
        self.assertEqual(validate(ROOT)['coverage'], 'complete')


if __name__ == '__main__':
    unittest.main()
