"""Deterministic sanity checks; not a deployment or load-test certificate."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from capacity_trace_lab import (  # noqa: E402
    closed_arrivals, example, open_arrivals, simulate_admission,
)


class CapacityTraceLabTests(unittest.TestCase):
    def test_open_vs_closed_same_nominal_count(self):
        self.assertEqual(open_arrivals(4, .1), [0.0, .1, .2, .3])
        self.assertEqual(closed_arrivals(4, .5, .1), [0.0, .6, 1.2, 1.8])
        self.assertGreater(closed_arrivals(4, .5, .1)[-1], open_arrivals(4, .1)[-1])

    def test_isolation_preserves_healthy_A_in_synthetic_trace(self):
        cases = example()
        shared = cases["shared_capacity_2"]
        isolated = cases["isolated_capacity_A1_B1"]
        self.assertEqual(shared["admitted"], {"B": 2})
        self.assertEqual(shared["rejected"], {"A": 2})
        self.assertEqual(isolated["admitted"], {"A": 2, "B": 1})
        self.assertEqual(isolated["rejected"], {"B": 1})
        self.assertEqual(shared["offered"], isolated["offered"])

    def test_releases_slots_and_never_exceeds_pool_capacity(self):
        out = simulate_admission([(0.0, "A", 0.1), (0.1, "A", 0.1)],
                                 {"A": 1}, shared=False)
        self.assertEqual(out["admitted"], {"A": 2})
        self.assertEqual(out["peak_inflight_by_pool"], {"A": 1})

    def test_invalid_traces_fail_closed(self):
        with self.assertRaises(ValueError):
            simulate_admission([(0.2, "A", .1), (0.1, "A", .1)], {"A": 1}, shared=False)
        with self.assertRaises(ValueError):
            simulate_admission([(0.0, "X", .1)], {"A": 1}, shared=False)
        with self.assertRaises(ValueError):
            simulate_admission([(0.0, "A", 0)], {"A": 1}, shared=False)
        with self.assertRaises(ValueError):
            open_arrivals(2, 0)


    def test_nonfinite_and_bool_parameters_are_rejected(self):
        for invalid in (float("nan"), float("inf"), float("-inf")):
            with self.assertRaises(ValueError):
                open_arrivals(2, invalid)
            with self.assertRaises(ValueError):
                closed_arrivals(2, invalid)
            with self.assertRaises(ValueError):
                simulate_admission([(invalid, "A", .1)], {"A": 1}, shared=False)
            with self.assertRaises(ValueError):
                simulate_admission([(0.0, "A", invalid)], {"A": 1}, shared=False)
        with self.assertRaises(ValueError):
            open_arrivals(True, 0.1)
        with self.assertRaises(ValueError):
            closed_arrivals(False, 0.1)
        with self.assertRaises(ValueError):
            simulate_admission([(0.0, "A", 0.1)], {"A": True}, shared=False)


if __name__ == "__main__":
    unittest.main()
