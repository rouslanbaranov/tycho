"""Migration guardrails seeded before evidence labels are replaced."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import m9_evidence_identity as evidence


class EvidenceMigrationTests(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / 'tests/fixtures/m9-evidence-migration-baseline.json').read_text())['rows']
        self.actual = [{k: v for k, v in r.items() if k != 'primary_url'} for r in self.rows]
        self.sources = {r['source_id']: r['primary_url'] for r in self.rows}

    def test_current_corpus_preserves_all_pre_migration_evidence(self):
        self.assertEqual(evidence.validate(ROOT), {'rows': 123, 'identities': 116})

    def test_valid_lossless_identity_normalization(self):
        self.assertEqual(evidence.validate_rows(self.rows, self.actual, self.sources)['rows'], 123)

    def test_lost_row_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'definitions lost'):
            evidence.validate_rows(self.rows, self.actual[:-1], self.sources)

    def test_duplicate_definition_in_one_document_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate evidence identity'):
            evidence.validate_rows(self.rows, self.actual + [self.actual[0]], self.sources)

    def test_statement_or_qualifier_change_is_rejected(self):
        self.actual[0]['payload_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'payload changed'):
            evidence.validate_rows(self.rows, self.actual, self.sources)

    def test_wrong_source_is_rejected(self):
        self.actual[0]['source_id'] = 'src.m9-n02'
        with self.assertRaisesRegex(ValueError, 'source binding changed'):
            evidence.validate_rows(self.rows, self.actual, self.sources)

    def test_primary_url_drift_is_rejected(self):
        self.sources[self.actual[0]['source_id']] += '-wrong-article'
        with self.assertRaisesRegex(ValueError, 'primary URL changed'):
            evidence.validate_rows(self.rows, self.actual, self.sources)

    def test_numeric_suffix_is_not_padded_or_merged(self):
        short = next(r for r in self.actual if r['id'].endswith('.1'))
        short['id'] = short['id'][:-1] + '001'
        with self.assertRaisesRegex(ValueError, 'definitions lost'):
            evidence.validate_rows(self.rows, self.actual, self.sources)

    def test_retired_compatibility_table_is_absent(self):
        self.assertFalse((ROOT / 'sources/m9-source-aliases.json').exists())


if __name__ == '__main__':
    unittest.main()
