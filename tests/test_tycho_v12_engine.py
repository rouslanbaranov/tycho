"""V12 reference-engine verification cases.

These tests exercise the implemented reference cases only. They do not validate a
production system, a calibrated input or an external source claim.
"""
import json
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import v12_engine as engine

MODEL_PATH = ROOT / "edition/v12/models/checkout-des.json"
SCENARIO_PATH = ROOT / "edition/v12/scenarios/checkout-b-queue.json"


def scenario(model_id="tycho.model.checkout-des", kind="discrete-event", **overrides):
    base = {
        "id": "tycho.scenario.test-" + model_id.split(".")[-1],
        "model_id": model_id,
        "workload": {
            "duration": 300.0,
            "warmup": 60.0,
            "time_unit": "second",
            "arrival_process": {"kind": "poisson", "rate": 10.0, "unit": "request/second"},
        },
        "configuration": {
            "servers": 4,
            "service_time": {"kind": "lognormal", "mean": 0.3, "cv": 0.5},
            "queue_capacity": 50,
            "timeout": 2.0,
            "max_attempts": 2,
            "retry_backoff": {"kind": "exponential", "base": 0.1, "jitter": "full"},
            "bulkhead": 100,
            "cost_per_server_hour": 10.0,
        },
        "uncertainty": {"parameter_draws": [], "correlations": []},
        "replications": 4,
        "seed": {"base": 12345, "scheme": "test"},
        "metrics": [{"id": "success_rate", "unit": "ratio", "direction": "higher",
                     "business_comparable": True}],
        "constraints": [],
        "evidence_status": "assumed",
        "validity_limits": ["test only"],
    }
    base.update(overrides)
    return base


def model(kind):
    return {"id": "tycho.model.checkout-des" if kind == "discrete-event" else "tycho.model.order-intake",
            "dynamics": {"kind": kind}}


class StockFlowTests(unittest.TestCase):
    def test_conservation_below_capacity(self):
        s = scenario("tycho.model.order-intake", "stock-flow",
                     workload={"duration": 600.0, "warmup": 60.0, "time_unit": "second",
                               "arrival_process": {"kind": "deterministic", "rate": 10.0,
                                                   "unit": "request/second"}},
                     configuration={"servers": 8, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.5, "cv": 0.01},
                                    "queue_capacity": 100, "timeout": 2.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 1000, "cost_per_server_hour": 10.0})
        result = engine.run_stock_flow(s, engine.base_parameters(s), 7)
        self.assertTrue(result["conservation_ok"])
        self.assertEqual(result["rejection_rate"], 0.0)
        self.assertAlmostEqual(result["throughput"], 10.0, places=6)

    def test_saturation_rejects_and_conserves(self):
        s = scenario("tycho.model.order-intake", "stock-flow",
                     workload={"duration": 600.0, "warmup": 60.0, "time_unit": "second",
                               "arrival_process": {"kind": "deterministic", "rate": 30.0,
                                                   "unit": "request/second"}},
                     configuration={"servers": 8, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.5, "cv": 0.01},
                                    "queue_capacity": 20, "timeout": 2.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 1000, "cost_per_server_hour": 10.0})
        result = engine.run_stock_flow(s, engine.base_parameters(s), 7)
        self.assertTrue(result["conservation_ok"])
        self.assertGreater(result["rejection_rate"], 0.0)
        self.assertGreaterEqual(result["backlog_end"], 0.0)

    def test_zero_boundary(self):
        s = scenario("tycho.model.order-intake", "stock-flow",
                     workload={"duration": 120.0, "warmup": 30.0, "time_unit": "second",
                               "arrival_process": {"kind": "deterministic", "rate": 0.0,
                                                   "unit": "request/second"}},
                     configuration={"servers": 0, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.5, "cv": 0.01},
                                    "queue_capacity": 10, "timeout": 2.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 10, "cost_per_server_hour": 10.0})
        result = engine.run_stock_flow(s, engine.base_parameters(s), 7)
        self.assertEqual(result["offered"], 0.0)
        self.assertEqual(result["completed"], 0.0)
        self.assertEqual(result["backlog_end"], 0.0)


class EventOrderTests(unittest.TestCase):
    def test_ties_use_priority_then_insertion(self):
        queue = engine.EventQueue()
        queue.schedule(1.0, 2, "second")
        queue.schedule(1.0, 0, "first")
        queue.schedule(1.0, 1, "middle")
        queue.schedule(0.5, 9, "earlier")
        self.assertEqual([queue.pop().kind for _ in range(4)],
                         ["earlier", "first", "middle", "second"])

    def test_timeout_before_completion(self):
        s = scenario(configuration={"servers": 1, "service_time": {"kind": "deterministic",
                                                                  "mean": 2.0, "cv": 0.01},
                                    "queue_capacity": 10, "timeout": 0.5, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 20, "cost_per_server_hour": 10.0},
                     workload={"duration": 120.0, "warmup": 20.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 2.0,
                                                   "unit": "request/second"}})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertEqual(result["metrics"]["success_rate"]["value"], 0.0)
        self.assertGreater(result["metrics"]["timeout_rate"]["value"], 0.0)

    def test_completion_before_timeout(self):
        s = scenario(configuration={"servers": 2, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.05, "cv": 0.01},
                                    "queue_capacity": 20, "timeout": 2.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 40, "cost_per_server_hour": 10.0},
                     workload={"duration": 120.0, "warmup": 20.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 2.0,
                                                   "unit": "request/second"}})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertGreater(result["metrics"]["success_rate"]["value"], 0.9)


class DiscreteEventTests(unittest.TestCase):
    def test_conservation_under_retries(self):
        result = engine.run_scenario(model("discrete-event"), scenario(), str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertGreater(result["metrics"]["success_rate"]["value"], 0.5)

    def test_zero_capacity_boundary(self):
        s = scenario(configuration={"servers": 1, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.1, "cv": 0.01},
                                    "queue_capacity": 0, "timeout": 5.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 10, "cost_per_server_hour": 10.0})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertEqual(result["metrics"]["success_rate"]["value"], 0.0)

    def test_zero_arrivals(self):
        s = scenario(workload={"duration": 120.0, "warmup": 20.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 0.0,
                                                   "unit": "request/second"}})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertEqual(result["metrics"]["success_rate"]["value"], 0.0)

    def test_stale_completion_does_not_complete_retry(self):
        s = scenario(configuration={"servers": 1, "service_time": {"kind": "deterministic",
                                                                  "mean": 1.0, "cv": 0.01},
                                    "queue_capacity": 10, "timeout": 0.6, "max_attempts": 2,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 20, "cost_per_server_hour": 10.0},
                     workload={"duration": 60.0, "warmup": 10.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 0.5,
                                                   "unit": "request/second"}})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        self.assertEqual(result["metrics"]["success_rate"]["value"], 0.0)
        self.assertTrue(result["invariants"]["conservation_ok"])

    def test_cost_uses_measurement_window(self):
        s = scenario(configuration={"servers": 12, "service_time": {"kind": "deterministic",
                                                                  "mean": 0.5, "cv": 0.01},
                                    "queue_capacity": 200, "timeout": 2.0, "max_attempts": 1,
                                    "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                                    "bulkhead": 240, "cost_per_server_hour": 10.0},
                     workload={"duration": 900.0, "warmup": 300.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 10.0,
                                                   "unit": "request/second"}})
        result = engine.run_scenario(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH))
        completed = result["metrics"]["success_rate"]["value"] * 10.0 * 600.0
        expected = 12 * 10.0 * (600.0 / 3600.0) / completed * 1000.0
        self.assertAlmostEqual(result["metrics"]["cost_per_1k_success"]["value"], expected,
                               delta=expected * 0.02)

    def test_committed_runs_replay(self):
        import glob
        for path in glob.glob(str(ROOT / "edition/v12/runs/*.json")):
            run = json.loads(Path(path).read_text())
            model_path = ROOT / "edition/v12/models" / (run["model_id"].split(".")[-1] + ".json")
            scenario_path = ROOT / "edition/v12/scenarios" / (run["scenario_id"].split(".")[-1] + ".json")
            with self.subTest(run=run["id"]):
                self.assertEqual(engine.replay(path, model_path, scenario_path)["status"], "replayed")

    def test_deterministic_replay(self):
        first = engine.finalize_run(engine.run_scenario(model("discrete-event"), scenario(),
                                                        str(MODEL_PATH), str(SCENARIO_PATH)))
        second = engine.finalize_run(engine.run_scenario(model("discrete-event"), scenario(),
                                                         str(MODEL_PATH), str(SCENARIO_PATH)))
        self.assertEqual(first["result_sha256"], second["result_sha256"])


class ModernizationTests(unittest.TestCase):
    def modernization(self, lag=0.0, reconciliation=20.0):
        return scenario("tycho.model.modernization-path", "hybrid",
                        workload={"duration": 600.0, "warmup": 60.0, "time_unit": "second",
                                  "arrival_process": {"kind": "deterministic", "rate": 10.0,
                                                      "unit": "request/second"}},
                        configuration={"servers": 1, "service_time": {"kind": "deterministic",
                                                                      "mean": 0.1, "cv": 0.01},
                                       "queue_capacity": 10, "timeout": 2.0, "max_attempts": 1,
                                       "retry_backoff": {"kind": "none", "base": 0.0,
                                                         "jitter": "none"},
                                       "bulkhead": 10, "cost_per_server_hour": 10.0,
                                       "target_share": 1.0, "target_capacity": 20.0,
                                       "legacy_capacity": 20.0, "dual_write_lag": lag,
                                       "reconciliation_capacity": reconciliation,
                                       "rollback_at": 400.0, "rollback_drain": 60.0,
                                       "stages": [{"at": 0.0, "target_share": 1.0}]})

    def test_zero_lag_has_no_divergence(self):
        s = self.modernization()
        result = engine.run_modernization(s, engine.base_parameters(s), 7)
        self.assertEqual(result["max_divergence"], 0.0)
        self.assertTrue(result["conservation_ok"])

    def test_modernization_capacity(self):
        s = self.modernization(lag=0.1, reconciliation=100.0)
        s["configuration"]["target_capacity"] = 1.0
        result = engine.run_modernization(s, engine.base_parameters(s), 7)
        self.assertGreater(result["rejection_rate"], 0.0)

    def test_rollback_completes_with_high_reconciliation(self):
        s = self.modernization(lag=0.1, reconciliation=100.0)
        result = engine.run_modernization(s, engine.base_parameters(s), 7)
        self.assertEqual(result["rollback_completed"], 1.0)
        self.assertEqual(result["rollback_seconds"], 0.0)


class CorrelationTests(unittest.TestCase):
    def test_declared_correlation_is_applied(self):
        s = scenario(uncertainty={"parameter_draws": [
            {"parameter": "arrival_rate", "distribution": "normal", "mean": 10.0,
             "sd": 2.0, "unit": "request/second"},
            {"parameter": "service_mean", "distribution": "normal", "mean": 0.3,
             "sd": 0.05, "unit": "second/request"}],
            "correlations": [{"left": "arrival_rate", "right": "service_mean",
                              "coefficient": -0.8}]})
        rows = [engine.sample_row(s, engine.random.Random(i)) for i in range(300)]
        arrival = [row["arrival_rate"] for row in rows]
        service = [row["service_time"]["mean"] for row in rows]
        import statistics
        mean_a = statistics.fmean(arrival)
        mean_s = statistics.fmean(service)
        covariance = sum((a - mean_a) * (b - mean_s) for a, b in zip(arrival, service)) / len(rows)
        correlation = covariance / (statistics.pstdev(arrival) * statistics.pstdev(service))
        self.assertLess(correlation, -0.5)


class SensitivityTests(unittest.TestCase):
    def test_indices_are_coherent(self):
        s = scenario(workload={"duration": 120.0, "warmup": 20.0, "time_unit": "second",
                               "arrival_process": {"kind": "poisson", "rate": 8.0,
                                                   "unit": "request/second"}},
                     uncertainty={"parameter_draws": [
                         {"parameter": "arrival_rate", "distribution": "normal",
                          "mean": 8.0, "sd": 1.0, "unit": "request/second"},
                         {"parameter": "service_mean", "distribution": "normal",
                          "mean": 0.3, "sd": 0.05, "unit": "second/request"}],
                         "correlations": []},
                     replications=2)
        rows = engine.sensitivity(model("discrete-event"), s, str(MODEL_PATH), str(SCENARIO_PATH), draws=8)
        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertGreaterEqual(row["first_order_index"], 0.0)
            self.assertLessEqual(row["total_order_index"], 1.0)
            self.assertGreaterEqual(row["total_order_index"], row["first_order_index"])


if __name__ == "__main__":
    unittest.main()
