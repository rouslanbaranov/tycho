"""Offline unit tests for the explicitly pinned M1–M9 integration runner.

These tests validate branch/SHA checks and the planned command inventory.
They do not execute the whole repository suite or claim publication/MCP review.
"""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "scripts/premerge_integration_check.py"
spec = importlib.util.spec_from_file_location("integration_premerge", MODULE)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

PIN = "a" * 40


class IdentityTests(unittest.TestCase):
    def test_exact_approved_branch_and_sha(self):
        self.assertIsNone(runner.validate_identity(
            "integration/tycho-m1-m9-unified-manuscript-20261019", PIN, PIN
        ))

    def test_nonintegration_feature_cannot_sidestep_issue_naming_rules(self):
        for name in [
            "feature/TYCHO-213-book-audit-and-complete-all-69-planned-system-design-chapters",
            "integration/tycho-anything",
            "main",
            "integration/tycho-m1-m9-unified-manuscript-20261019/",
        ]:
            with self.subTest(branch=name), self.assertRaises(ValueError):
                runner.validate_identity(name, PIN, PIN)

    def test_unpinned_or_moved_head_rejected(self):
        branch = runner.INTEGRATION_BRANCH
        for value in ["", "main", "abcdef0", "A" * 40, "g" * 40, "0" * 41]:
            with self.subTest(expected=value), self.assertRaises(ValueError):
                runner.validate_identity(branch, value, value)
        with self.assertRaises(ValueError):
            runner.validate_identity(branch, PIN, "b" * 40)


class CommandInventoryTests(unittest.TestCase):
    def test_scoped_suite_reuses_existing_validators(self):
        commands = runner.commands("python-test-executable")
        self.assertEqual(len(commands), 10)
        self.assertTrue(all(command[0] == "python-test-executable"
                            for command in commands))
        paths = [" ".join(c) for c in commands]
        for needle in [
            "scripts/check_boundary.py",
            "scripts/validate_sources.py",
            "scripts/source_catalog.py --check",
            "scripts/validate_claim_references.py",
            "scripts/validate_metadata_schemas.py examples",
            "scripts/validate_book_navigation.py",
            "scripts/validate_m9_cases.py --self-test",
            "test_tycho*.py",
            "test_m9*.py",
        ]:
            with self.subTest(needle=needle):
                self.assertTrue(any(needle in c for c in paths))

    def test_does_not_claim_to_run_graph_or_hosted_mcp(self):
        commands = " ".join(" ".join(c) for c in runner.commands("python3"))
        self.assertNotIn("graph", commands.lower())
        self.assertNotIn("mcp", commands.lower())
        self.assertNotIn("github", commands.lower())


if __name__ == "__main__":
    unittest.main()
