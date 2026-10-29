import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "edition/patterns/reading-ledger.v1.json"


class LedgerScopeTests(unittest.TestCase):
    def test_read_and_not_read_do_not_overlap(self):
        records = json.loads(LEDGER.read_text())["records"]
        for record in records:
            read = {item.strip().lower()
                    for item in record.get("sections_read", [])}
            not_read = {item.strip().lower()
                        for item in record.get("sections_not_read", [])}
            self.assertEqual(read & not_read, set(), record["id"])


if __name__ == "__main__":
    unittest.main()
