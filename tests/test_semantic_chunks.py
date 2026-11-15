"""Unit tests for semantic chunking and section fusion."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import hybrid_rerank
import semantic_chunks

WORDS = re.compile(r"\S+")


def synthetic(count=1000):
    return " ".join(("word%d." % i) if i % 12 == 0 else ("word%d" % i)
                    for i in range(count))


class SemanticChunkTests(unittest.TestCase):
    def test_chunk_sizes_and_overlap(self):
        text = synthetic()
        spans = semantic_chunks.word_spans(text)
        ranges = semantic_chunks.split_section(text)
        self.assertGreater(len(ranges), 1)
        for index, (start, end, words) in enumerate(ranges):
            self.assertGreater(words, 0)
            if index < len(ranges) - 1:
                self.assertGreaterEqual(words, 180)
                self.assertLessEqual(words, 250)
        for (_, end, _), (start, _, _) in zip(ranges, ranges[1:]):
            prev_end = max(i for i, span in enumerate(spans) if span.end() <= end)
            next_start = min(i for i, span in enumerate(spans)
                             if span.start() >= start)
            self.assertEqual(prev_end - next_start + 1, 40)

    def test_short_section_stays_single_chunk(self):
        text = synthetic(80)
        self.assertEqual(semantic_chunks.split_section(text), [
            (0, len(text), 80)])

    def test_build_chunks_keeps_parent(self):
        chunks = semantic_chunks.build_chunks(ROOT)
        self.assertTrue(chunks)
        for chunk in chunks[:20]:
            self.assertIn("#chunk-", chunk["chunk_id"])
            self.assertEqual(chunk["parent_section_key"],
                             chunk["chunk_id"].split("#chunk-")[0])
            self.assertLessEqual(chunk["word_count"], 250)


class FusionTests(unittest.TestCase):
    def test_semantic_candidate_is_added(self):
        bm = [{"section_key": "a", "section_id": "x", "path": "p",
               "heading": "h"}]
        sem = [{"section_key": "b", "section_id": "y", "path": "q",
                "heading": "i", "chunk_id": "b#chunk-0",
                "score": 0.9}]
        fused = hybrid_rerank.fuse(bm, sem, 0.5, 5)
        self.assertEqual({row["section_key"] for row in fused}, {"a", "b"})
        self.assertTrue(all("hybrid_score" in row for row in fused))


if __name__ == "__main__":
    unittest.main()
