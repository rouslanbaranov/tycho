"""Judge v2.1 claim-level consistency tests."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_judge_verdicts", ROOT / "scripts/validate_judge_verdicts.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def task():
    return {"task_id": "Q300", "claims": [{"claim_id": "C1", "text": "claim"}]}


def judge(verdict="supported", coverage=2, support=2, passed=True):
    return {"status": "ai-judge-not-human", "items": [{
        "task_id": "Q300", "citation_resolution": True,
        "required_anchor_coverage": 1.0,
        "claim_verdicts": [{
            "claim_id": "C1", "core": True, "verdict": verdict,
            "quote_id": "C1-E1", "reason": "quote entails claim"}],
        "semantic_support": support, "core_coverage": coverage,
        "pass": passed, "notes": "ok"}]}


class JudgeVerdictTests(unittest.TestCase):
    def test_supported_passes(self):
        result = MODULE.validate(judge(), [task()])
        self.assertTrue(result["ok"], result["errors"])

    def test_partial_cannot_pass(self):
        result = MODULE.validate(judge("partial", 2, 1, True), [task()])
        self.assertFalse(result["ok"])
        self.assertTrue(any("pass inconsistent" in e for e in result["errors"]))

    def test_missing_core_claim_blocks_coverage(self):
        data = judge()
        data["items"][0]["claim_verdicts"] = []
        result = MODULE.validate(data, [task()])
        self.assertFalse(result["ok"])

    def test_unsupported_forces_zero_support(self):
        result = MODULE.validate(judge("unsupported", 2, 2, True), [task()])
        self.assertFalse(result["ok"])
        self.assertTrue(any("semantic_support" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
