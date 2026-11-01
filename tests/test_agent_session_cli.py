"""CLI onboarding and prompt v3 contract."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AgentSessionCliTests(unittest.TestCase):
    def test_describe_returns_layer_catalog(self):
        proc = subprocess.run(
            [sys.executable, "scripts/agent_session_cli.py", "describe"],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")
        self.assertIn("metadata", payload)
        names = [x["name"] for x in payload["metadata"]["layers"]]
        self.assertEqual(names[:3], ["book", "atlas", "modeling-and-simulation"])

    def test_prompt_v3_requires_onboarding_and_evidence(self):
        text = (ROOT / "evaluation/agent-benchmark/AGENT-PROMPT-V3.md").read_text(
            encoding="utf-8")
        for phrase in ["describe", "Facet matrix", "Evidence ledger",
                       "detailed, justified, broader", "two consecutive searches"]:
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
