"""Offline regression tests for the per-issue feature branch convention and case math."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("feature_branch", ROOT / "scripts/check_feature_branch.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class BranchNamingTests(unittest.TestCase):
    def test_exact_issue_slug(self):
        self.assertEqual(
            mod.validate("feature/TYCHO-17-requirements-and-workload-profile",
                         "[E01-01] Requirements and workload profile"), 17)

    def test_punctuation_slug(self):
        self.assertEqual(mod.title_slug("[E14-09] Deployment topology, multi-region and disaster recovery"),
                         "deployment-topology-multi-region-and-disaster-recovery")

    def test_unrelated_branch(self):
        with self.assertRaises(ValueError):
            mod.validate("fix/TYCHO-17-requirements-and-workload-profile",
                         "[E01-01] Requirements and workload profile")

    def test_wrong_issue_title(self):
        with self.assertRaises(ValueError):
            mod.validate("feature/TYCHO-17-wrong-scope",
                         "[E01-01] Requirements and workload profile")

    def test_padding_and_empty_slug(self):
        for branch in ("feature/TYCHO-017-requirements-and-workload-profile",
                       "feature/TYCHO-0-requirements-and-workload-profile",
                       "feature/TYCHO-17-",
                       "feature/TYCHO-17-Requirements-and-workload-profile"):
            with self.subTest(branch=branch), self.assertRaises(ValueError):
                mod.validate(branch, "[E01-01] Requirements and workload profile")

    def test_activated_parent_issue_slug(self):
        self.assertEqual(
            mod.validate(
                "feature/TYCHO-587-v12-architecture-modeling-simulation-decision-validation-isolated-volume",
                "[FUTURE] V12 - Architecture Modeling, Simulation & Decision Validation (isolated volume)"),
            587)

    def test_simulation_child_issue_slug(self):
        self.assertEqual(
            mod.validate(
                "feature/TYCHO-598-integrate-simulation-artifacts-into-search-facets-and-qrels",
                "[SIM-G] Integrate simulation artifacts into search facets and qrels"),
            598)

    def test_epic_not_executable_subissue(self):
        with self.assertRaises(ValueError):
            mod.validate("feature/TYCHO-2-architecture-decision-models",
                         "[EPIC E01] Architecture decision models")


class WorkloadModelTests(unittest.TestCase):
    def test_nominal_arrival_derivation(self):
        simultaneous_active, calls_per_minute = 600, 3
        self.assertEqual(simultaneous_active * calls_per_minute / 60, 30)

    def test_peak_mix_and_bandwidth(self):
        peak = 120
        shares = (0.70, 0.29, 0.01)
        self.assertAlmostEqual(sum(shares), 1)
        op_rates = [peak * share for share in shares]
        self.assertEqual(op_rates, [84, 34.8, 1.2])
        self.assertAlmostEqual(sum(rate * kib for rate, kib in zip(op_rates, (4, 1, 2))), 373.2)

    def test_little_law_is_conditional_arithmetic_only(self):
        completed_throughput_per_second = 120
        hypothetical_mean_seconds = 0.2
        self.assertEqual(completed_throughput_per_second * hypothetical_mean_seconds, 24)

    def test_storage_increment(self):
        bytes_added = 25000 * 2 * 1024
        self.assertAlmostEqual(bytes_added / (1024 * 1024), 48.828125)
        self.assertAlmostEqual(bytes_added * 12 / (1024 * 1024), 585.9375)

    def test_artifact_cross_links(self):
        paths = [
            ROOT / "authoring/models/requirements-workload-profile.md",
            ROOT / "templates/requirements-workload-profile.md",
            ROOT / "examples/synthetic-workshop-registration.md",
            ROOT / "authoring/contracts/TYCHO-17-research-contract.md",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue(path.exists())
                self.assertIn("TYCHO", path.read_text() if "contract" in path.name else
                              (path.read_text() + " TYCHO"), msg=str(path))
        self.assertIn("Status: **entirely fictional",
                      (ROOT / "examples/synthetic-workshop-registration.md").read_text())


if __name__ == "__main__":
    unittest.main()
