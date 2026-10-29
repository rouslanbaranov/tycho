"""V12 comparative and modernization experiment regressions."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text())


class ComparativeExperimentTests(unittest.TestCase):
    def setUp(self):
        self.scenarios = {
            name: load("edition/v12/scenarios/" + name + ".json")
            for name in ("checkout-a-synchronous", "checkout-b-queue", "checkout-c-partitioned")
        }
        self.runs = {
            name: load("edition/v12/runs/" + name + ".json")
            for name in ("checkout-a-synchronous", "checkout-b-queue", "checkout-c-partitioned")
        }

    def test_identical_workload_seed_and_metrics(self):
        workloads = {json.dumps(s["workload"], sort_keys=True) for s in self.scenarios.values()}
        seeds = {json.dumps(s["seed"], sort_keys=True) for s in self.scenarios.values()}
        metrics = {json.dumps(s["metrics"], sort_keys=True) for s in self.scenarios.values()}
        self.assertEqual(len(workloads), 1)
        self.assertEqual(len(seeds), 1)
        self.assertEqual(len(metrics), 1)
        self.assertEqual({s["replications"] for s in self.scenarios.values()}, {30})

    def test_candidate_configurations_differ(self):
        configs = {name: json.dumps(s["configuration"], sort_keys=True)
                   for name, s in self.scenarios.items()}
        self.assertEqual(len(set(configs.values())), 3)

    def test_business_metric_ordering(self):
        a = self.runs["checkout-a-synchronous"]["metrics"]
        b = self.runs["checkout-b-queue"]["metrics"]
        c = self.runs["checkout-c-partitioned"]["metrics"]
        self.assertLess(a["success_rate"]["value"], b["success_rate"]["value"])
        self.assertLess(b["cost_per_1k_success"]["value"], a["cost_per_1k_success"]["value"])
        self.assertLess(a["cost_per_1k_success"]["value"], c["cost_per_1k_success"]["value"])
        self.assertGreater(c["cost_per_1k_success"]["value"], 3.0)
        self.assertLessEqual(c["latency_p95"]["value"], 1.5)
        self.assertLessEqual(b["latency_p95"]["value"], 1.5)

    def test_all_runs_are_converged(self):
        for run in self.runs.values():
            self.assertEqual(run["convergence"]["status"], "converged")
            self.assertEqual(run["result_sha256"], run["result_sha256"].lower())

    def test_decision_is_conditional_and_supported(self):
        decision = load("edition/v12/decisions/checkout-candidate.json")
        self.assertEqual(decision["status"], "decision-supported")
        self.assertEqual(decision["outcome"]["recommendation"], "B")
        self.assertEqual(decision["evidence"]["calibration"], "uncalibrated")
        self.assertEqual(decision["evidence"]["simulation"], "decision-supported")
        self.assertTrue(any(c["kind"] == "hard" for c in decision["constraints"]))
        self.assertTrue(any(c["kind"] == "non-quantitative" for c in decision["constraints"]))
        self.assertGreaterEqual(len(decision["reversal_triggers"]), 3)
        self.assertEqual({item["constraint_id"] for item in decision["constraint_evaluation"]},
                         {"C1", "C2", "C3", "C4", "C5"})


class ModernizationExperimentTests(unittest.TestCase):
    def test_staged_and_baseline_differ(self):
        staged = load("edition/v12/runs/modernization-staged.json")["metrics"]
        baseline = load("edition/v12/runs/modernization-no-cutover.json")["metrics"]
        self.assertGreater(staged["max_divergence"]["value"], 0.0)
        self.assertEqual(baseline["max_divergence"]["value"], 0.0)
        self.assertEqual(staged["rollback_completed"]["value"], 0.1)
        self.assertEqual(baseline["rollback_completed"]["value"], 1.0)

    def test_decision_is_insufficient_evidence(self):
        decision = load("edition/v12/decisions/modernization-cutover.json")
        self.assertEqual(decision["status"], "insufficient-evidence")
        self.assertEqual(decision["outcome"]["recommendation"], "none")
        self.assertEqual(decision["evidence"]["simulation"], "insufficient-evidence")
        self.assertEqual(decision["evidence"]["calibration"], "uncalibrated")
        self.assertTrue(any("rollback" in t.lower() for t in decision["reversal_triggers"]))


class SensitivityExperimentTests(unittest.TestCase):
    def test_sensitivity_screen_is_explicit(self):
        run = load("edition/v12/runs/checkout-sensitivity.json")
        self.assertEqual(run["convergence"]["status"], "converged")
        stress = load("edition/v12/runs/checkout-convergence-stress.json")
        self.assertEqual(stress["convergence"]["status"], "insufficient-sample")
        self.assertEqual(len(run["sensitivity"]), 2)
        for row in run["sensitivity"]:
            self.assertEqual(row["method"], "quadratic-response-surface")
            self.assertGreaterEqual(row["total_order_index"], row["first_order_index"])
            self.assertLessEqual(row["total_order_index"], 1.0)


if __name__ == "__main__":
    unittest.main()
