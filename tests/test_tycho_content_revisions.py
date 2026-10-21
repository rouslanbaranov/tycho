"""Adversarial checks for authorized post-migration content revisions."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from content_revisions import authorized, load


class ContentRevisionTests(unittest.TestCase):
    def test_real_revision_is_loaded(self):
        revisions = load(ROOT)
        self.assertTrue(any(r['issue'] == 227 for r in revisions))

    def test_authorized_entry_matches_both_hashes(self):
        revision = next(r for r in load(ROOT) if r['issue'] == 227)
        entry = revision['directory_documents'][0]
        self.assertTrue(authorized(
            ROOT, 'directory_documents', entry['path'],
            entry['previous_sha256'], entry['current_sha256']))

    def test_wrong_current_hash_is_not_authorized(self):
        revision = next(r for r in load(ROOT) if r['issue'] == 227)
        entry = revision['directory_documents'][0]
        self.assertFalse(authorized(
            ROOT, 'directory_documents', entry['path'],
            entry['previous_sha256'], '0' * 64))

    def test_unknown_key_is_not_authorized(self):
        self.assertFalse(authorized(
            ROOT, 'directory_documents', 'book/not-a-document.md',
            '0' * 64, '1' * 64))


if __name__ == '__main__':
    unittest.main()
