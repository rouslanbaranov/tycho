"""Offline deterministic syntactic imports; no public remote clone or code execution."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import extract_pinned_imports as ext  # noqa: E402


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True, check=True).stdout.strip()


class StaticImportsTests(unittest.TestCase):
    def test_python_ast_import_locations(self):
        source = "import os, sys\nfrom collections import deque\nif True:\n    import json\n"
        found = ext.syntactic_imports("example.py", source)
        self.assertIn(("python", "os", 1, "ast.Import"), found)
        self.assertIn(("python", "collections.deque", 2, "ast.ImportFrom"), found)
        self.assertIn(("python", "json", 4, "ast.Import"), found)

    def test_java_imports_avoid_commented_statements(self):
        source = "// import fake.One;\n/* import fake.Two; */\nimport java.util.List;\nimport static java.util.Collections.emptyList;\n"
        found = ext.syntactic_imports("Example.java", source)
        self.assertEqual([x[1] for x in found],
                         ["java.util.List", "java.util.Collections.emptyList"])
        self.assertEqual([x[2] for x in found], [3, 4])

    def test_unsupported_files_fail(self):
        with self.assertRaisesRegex(ValueError, "unsupported language"):
            ext.syntactic_imports("package.go", "import x")

    def test_invalid_python_is_explicit_failure(self):
        with self.assertRaisesRegex(ValueError, "Invalid Python syntax"):
            ext.syntactic_imports("broken.py", "from !!!")

    def test_real_git_tracking_and_repeatability_without_network(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            git(repo, "config", "user.name", "Fixture")
            git(repo, "config", "user.email", "fixture@invalid.example")
            (repo / "A.java").write_text("package example;\nimport java.util.List;\n")
            (repo / "b.py").write_text("from pathlib import Path\n")
            (repo / "ignored.go").write_text("package ignored\n")
            git(repo, "add", "A.java", "b.py", "ignored.go")
            git(repo, "commit", "-qm", "fixture")
            revision = git(repo, "rev-parse", "HEAD")
            manifest = [{"id": "src.fixture", "revision": revision, "url": "https://github.com/example/test.git", "submodules": {}}]
            with patch("public_repo_snapshots.load_manifest", return_value=manifest), patch(
                "public_repo_snapshots.inspect_checkout", return_value=revision
            ):
                one = ext.extract(repo, "src.fixture")
                two = ext.extract(repo, "src.fixture")
            self.assertEqual(json.dumps(one, sort_keys=True), json.dumps(two, sort_keys=True))
            self.assertEqual(len(one["observations"]), 2)
            self.assertEqual(one["locked_revision"], revision)
            self.assertTrue(all(x["kind"] == "imports" and x["plane"] == "code"
                                for x in one["observations"]))
            self.assertFalse(one["checked_out_code_executed"])

    def test_no_files_or_unlocked_source_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            with patch("public_repo_snapshots.load_manifest", return_value=[]):
                with self.assertRaisesRegex(ValueError, "Unknown or unlocked"):
                    ext.extract(repo, "src.missing")
            with patch("public_repo_snapshots.load_manifest", return_value=[
                {"id": "src.test", "revision": "0" * 40, "submodules": {}}],
            ), patch("public_repo_snapshots.inspect_checkout", return_value="0" * 40):
                with self.assertRaisesRegex(ValueError, "No supported"):
                    ext.extract(repo, "src.test")


if __name__ == "__main__":
    unittest.main()
