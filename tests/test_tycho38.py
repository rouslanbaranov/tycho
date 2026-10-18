"""Deterministic checks for the original TYCHO-38 queueing examples.

These are arithmetic/consistency tests, NOT measured software capacity,
mathematical proof of real performance, or review of external publications.
"""
from pathlib import Path
import statistics
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "book/performance/queueing-littles-law.md"
LANDING = ROOT / "book/performance/README.md"


class QueueingArithmeticTests(unittest.TestCase):
    def test_little_law_steady_hypothesis_only(self):
        completed_per_second = 120
        mean_seconds = 0.2
        self.assertEqual(completed_per_second * mean_seconds, 24)

    def test_tail_not_mean(self):
        # Invented exact 100-request population: 95 fast, five slow.
        durations = [0.1] * 95 + [2.1] * 5
        self.assertAlmostEqual(statistics.mean(durations), 0.2)
        self.assertEqual(sorted(durations)[98], 2.1)
        # Deliberately wrong p99 substitution is not the mean occupancy.
        self.assertEqual(120 * sorted(durations)[98], 252)
        self.assertNotEqual(252, 120 * statistics.mean(durations))

    def test_boundary_work_is_conserved(self):
        # Starts empty, accepts 200/s, exits 150/s, nothing rejects.
        self.assertEqual((200 - 150) * 30, 1500)
        # Reject before boundary at 50/s: remaining admits == exits.
        self.assertEqual((200 - 50 - 150) * 30, 0)

    def test_closed_model_feedback(self):
        self.assertEqual(100 / 2, 50)
        self.assertEqual(100 / 4, 25)

    def test_finite_window_edge_counterexample(self):
        # One admitted request t=0..10; observe t=[0,5).
        arrivals = 1
        seconds = 5
        actual_inflight_area_seconds = 5
        full_eventual_residence_seconds = 10
        observed_occupancy = actual_inflight_area_seconds / seconds
        wrong_finite_estimate = (arrivals / seconds) * full_eventual_residence_seconds
        self.assertEqual(observed_occupancy, 1)
        self.assertEqual(wrong_finite_estimate, 2)
        self.assertNotEqual(observed_occupancy, wrong_finite_estimate)

    def test_source_and_navigation_presence(self):
        text = CHAPTER.read_text(encoding="utf-8")
        landing = LANDING.read_text(encoding="utf-8")
        self.assertIn("## Evidence-based counterexample", text)
        self.assertIn("## Independent public sources", text)
        self.assertIn("insufficient evidence", text.lower())
        for source in ("columbia.edu/~ww2040/LL_OR.pdf", "grafana.com/docs/k6/",
                       "sre.google/sre-book/handling-overload/"):
            self.assertIn(source, text)
        self.assertIn("(queueing-littles-law.md)", landing)


if __name__ == "__main__":
    unittest.main()
