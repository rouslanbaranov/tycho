"""Contract tests for the v2 answer/evidence validator."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_agent_answer", ROOT / "scripts/validate_agent_answer.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def answer(citations, missing, evidence_key="sec.a"):
    return {
        "task_id": "Q250",
        "answer": "full answer",
        "claims": [{
            "claim_id": "C1",
            "text": "claim",
            "evidence": [{
                "section_key": evidence_key,
                "quote": "quote",
                "supports": "C1",
                "status": "observed",
            }],
        }],
        "citations": citations,
        "missing_required_anchors": missing,
        "abstain": False,
    }


class AnswerContractTests(unittest.TestCase):
    def test_valid_answer_passes(self):
        result = MODULE.validate_answer(answer(["sec.a"], []), {
            "required_evidence": ["sec.a"]}, {"sec.a"})
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["required_anchor_coverage"], 1.0)

    def test_orphan_citation_fails(self):
        result = MODULE.validate_answer(answer(["sec.a", "sec.b"], []), {
            "required_evidence": ["sec.a"]}, {"sec.a", "sec.b"})
        self.assertFalse(result["ok"])
        self.assertIn("citations must equal unique evidence section keys",
                      result["errors"])

    def test_missing_anchor_must_be_declared(self):
        result = MODULE.validate_answer(answer(["sec.a"], []), {
            "required_evidence": ["sec.a", "sec.b"]}, {"sec.a"})
        self.assertFalse(result["ok"])
        self.assertEqual(result["missing_required_anchors"], ["sec.b"])

    def test_unresolved_key_fails(self):
        result = MODULE.validate_answer(answer(["sec.a"], []), {
            "required_evidence": ["sec.a"]}, set())
        self.assertFalse(result["ok"])
        self.assertTrue(any("unresolved" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
