"""Negative integrity tests for the real directory migration, not page quotas."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from directory_paths import HistoricalView, rewrite
from validate_directory_migration import validate
from validate_knowledge import ordered_checks


class DirectoryMigrationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for name in ('book', 'edition', 'sources', 'schemas'):
            shutil.copytree(ROOT / name, self.root / name)
        self.file = self.root / 'edition/directory-migration.json'
        self.manifest = json.loads(self.file.read_text())
        self.record = next(r for r in self.manifest['documents'] if r['old_path'] != r['new_path'])

    def save(self):
        self.file.write_text(json.dumps(self.manifest))

    def test_complete_reversible_membership(self):
        result = validate(self.root)
        self.assertGreaterEqual(result['canonical_documents'], 423)
        self.assertEqual((result['volumes'], result['chapters']), (12, 89))
        self.assertEqual(result['protected_historical_manifests'], 4)

    def test_prose_change_is_not_a_path_migration(self):
        path = self.root / self.record['new_path']
        path.write_text(path.read_text() + '\nUnexpected narrative change.\n')
        with self.assertRaisesRegex(ValueError, 'directory-baseline-payload-drift'):
            validate(self.root)

    def test_missing_document_map_record_is_rejected(self):
        self.manifest['documents'].pop()
        self.save()
        with self.assertRaisesRegex(ValueError, 'directory-document-map-uniqueness'):
            validate(self.root)

    def test_colliding_destinations_are_rejected(self):
        rows = self.manifest['documents']
        rows[1]['new_path'] = rows[0]['new_path']
        self.save()
        with self.assertRaisesRegex(ValueError, 'directory-document-map-uniqueness'):
            validate(self.root)

    def test_legacy_canonical_copy_is_rejected(self):
        old = self.root / self.record['old_path']
        old.parent.mkdir(parents=True)
        shutil.copyfile(self.root / self.record['new_path'], old)
        with self.assertRaisesRegex(ValueError, 'directory-old-directory-retained'):
            validate(self.root)

    def test_historical_manifest_cannot_be_rebased_silently(self):
        path = self.root / 'edition/enrichment-manifest.json'
        path.write_text(path.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'directory-historical-manifest-drift'):
            validate(self.root)

    def test_bare_number_is_not_a_readable_directory(self):
        row = self.manifest['directories'][0]
        row['new'] = row['old']
        self.save()
        with self.assertRaisesRegex(ValueError, 'directory-readable-name'):
            validate(self.root)

    def test_external_urls_queries_and_fragments_survive(self):
        view = HistoricalView(self.root)
        source = 'book/volumes/v01/c01/README.md'
        text = '[source](https://example.org/p?path=book/volumes/v01/c01) [next](../c02/workload-contract.md?q=x#section)'
        changed = rewrite(text, source, view.directories)
        self.assertIn('https://example.org/p?path=book/volumes/v01/c01', changed)
        self.assertIn('?q=x#section', changed)
        self.assertEqual(rewrite(changed, view.current(source), view.inverse), text)

    def test_strict_runner_includes_directory_boundary(self):
        checks, _ = ordered_checks(ROOT, 'strict')
        self.assertIn(('directory-layout', ['scripts/validate_directory_migration.py']), checks)


if __name__ == '__main__':
    unittest.main()
