"""Verify the repository cannot start paid GitHub Actions on commit/PR events."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"


class MilestoneOnlyPipelineTests(unittest.TestCase):
    def test_one_consolidated_workflow(self):
        paths = sorted(list(WORKFLOWS.glob("*.yml")) + list(WORKFLOWS.glob("*.yaml")))
        self.assertEqual([path.name for path in paths], ["boundary.yml"])

    def test_milestone_closed_without_open_issues(self):
        content = (WORKFLOWS / "boundary.yml").read_text()
        header = content.split("\npermissions:", 1)[0]
        self.assertIn("\non:\n  milestone:\n    types: [closed]", header)
        self.assertNotIn("\n  push:", header)
        self.assertNotIn("\n  pull_request:", header)
        self.assertNotIn("\n  workflow_dispatch:", header)
        self.assertNotIn("\n  schedule:", header)
        self.assertIn("github.event.milestone.open_issues == 0", content)

    def test_required_batched_checks(self):
        text = (WORKFLOWS / "boundary.yml").read_text()
        for command in (
            "scripts/check_boundary.py",
            "scripts/validate_sources.py",
            "scripts/source_catalog.py --check",
            "unittest discover -s tests -p 'test_tycho*.py'",
        ):
            with self.subTest(command=command):
                self.assertIn(command, text)
        self.assertTrue((ROOT / "scripts/premerge_check.py").is_file())


if __name__ == "__main__":
    unittest.main()
