"""CLI onboarding and prompt v3 contract."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class AgentSessionCliTests(unittest.TestCase):
    def test_describe_returns_layer_catalog(self):
        proc = subprocess.run(
            [sys.executable, "mcp/agent_session_cli.py", "describe"],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")
        self.assertIn("metadata", payload)
        names = [x["name"] for x in payload["metadata"]["layers"]]
        self.assertEqual(names[:3], ["book", "atlas", "modeling-and-simulation"])

    def test_search_can_target_atlas_volume(self):
        proc = subprocess.run(
            [sys.executable, "mcp/agent_session_cli.py", "search",
             "pattern", "--volume", "atlas", "--limit", "1"],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["layer"], "atlas")

    def test_book_volume_returns_book_layer(self):
        proc = subprocess.run(
            [sys.executable, "mcp/agent_session_cli.py", "search",
             "pattern", "--volume", "book", "--limit", "1"],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload["layer"], "book")

    def test_prompt_v3_requires_onboarding_and_evidence(self):
        text = (ROOT / "evaluation/agent-benchmark/AGENT-PROMPT-V3.md").read_text(
            encoding="utf-8")
        for phrase in ["describe", "Facet matrix", "Evidence ledger",
                       "detailed, justified, broader", "two consecutive searches"]:
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
