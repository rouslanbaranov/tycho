"""Pure RRF checks for the optional semantic experiment."""
import sys
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import semantic_search

class SemanticTests(unittest.TestCase):
    def test_rrf_merges_and_deduplicates_documents(self):
        a=[{"section_key":"a#1","path":"a","section_id":"1"},
           {"section_key":"b#1","path":"b","section_id":"1"}]
        b=[{"section_key":"b#1","path":"b","section_id":"1"},
           {"section_key":"c#1","path":"c","section_id":"1"}]
        out=semantic_search.rrf(a,b,3)
        self.assertEqual([x["path"] for x in out],["b","a","c"])

if __name__=="__main__":
    unittest.main()
