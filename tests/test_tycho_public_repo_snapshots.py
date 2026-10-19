"""Offline tests for Tycho E03-02 public pinned Git source snapshots.

Run: python3 -m unittest discover -s tests -p 'test_tycho_public_repo_snapshots.py' -v
These tests use only disposable local Git fixtures: they do not clone GitHub
sources, verify remote availability, or authorize repository reuse.
"""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import public_repo_snapshots as snap  # noqa: E402


def system_git(*args, cwd=None):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                          text=True, check=True).stdout.strip()


class PublicRepoSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)
        self.root = Path(self.dir.name)
        self.origin = self.root / "origin"
        system_git("init", "-q", str(self.origin))
        system_git("config", "user.email", "test@invalid.example", cwd=self.origin)
        system_git("config", "user.name", "Synthetic Fixture", cwd=self.origin)
        (self.origin / "README.md").write_text("first commit\n")
        system_git("add", "README.md", cwd=self.origin)
        system_git("commit", "-qm", "fixture", cwd=self.origin)
        self.sha = system_git("rev-parse", "HEAD", cwd=self.origin)
        self.entry = {
            "id": "src.fixture",
            "url": "https://github.com/example/synthetic.git",
            "revision": self.sha,
            "submodules": {},
        }

    def manifest(self, entries):
        return {"schema_version": 1, "generated_from": "unit fixture",
                "repositories": entries}

    def detached_fixture(self):
        dst = self.root / "checkout"
        system_git("clone", "-q", "--no-checkout", str(self.origin), str(dst))
        system_git("checkout", "-q", "--detach", self.sha, cwd=dst)
        system_git("remote", "remove", "origin", cwd=dst)
        return dst

    def test_manifest_and_catalogue(self):
        self.assertEqual(snap.validate(self.manifest([self.entry])), [self.entry])
        text = snap.render_catalogue([self.entry])
        self.assertIn(self.sha, text)
        self.assertIn("src.fixture", text)
        self.assertIn("not cloned", text)
        with self.assertRaises(ValueError):
            snap.validate(self.manifest([self.entry, self.entry]))

    def test_private_url_unsupported_or_unpinned_rejected(self):
        for badurl in ("file:///tmp/private", "http://github.com/x/y",
                       "https://evil.example/x/y", "https://github.com/a/b?token=x",
                       "https://github.com/a/../b", "https://github.com/../repo",
                       "https://github.com/org/.", "https://github.com//org/repo",
                       "https://github.com/org/repo/"):
            e = {**self.entry, "url": badurl}
            with self.assertRaises(ValueError, msg=badurl):
                snap.validate(self.manifest([e]))
        with self.assertRaises(ValueError):
            snap.validate(self.manifest([{**self.entry, "revision": "main"}]))

    def test_reject_submodule_path_traversal(self):
        for path in ("../private", "/absolute", "foo/../bar", "foo\\bar"):
            with self.assertRaises(ValueError):
                snap.validate(self.manifest([{**self.entry,
                    "submodules": {path: self.sha}}]))

    def test_detached_clean_checkout_matches_exact_sha(self):
        dst = self.detached_fixture()
        self.assertEqual(snap.inspect_checkout(dst, self.entry), self.sha)

    def test_mismatched_sha_is_rejected_without_reset(self):
        dst = self.detached_fixture()
        wrong = {**self.entry, "revision": "0" * 40}
        with self.assertRaisesRegex(ValueError, "mismatch"):
            snap.checkout_one(wrong, dst)
        self.assertEqual(system_git("rev-parse", "HEAD", cwd=dst), self.sha)

    def test_missing_checkout_and_dirty_tree(self):
        with self.assertRaisesRegex(ValueError, "Missing"):
            snap.inspect_checkout(self.root / "missing", self.entry)
        dst = self.detached_fixture()
        (dst / "README.md").write_text("dirty change\n")
        with self.assertRaisesRegex(ValueError, "Dirty"):
            snap.inspect_checkout(dst, self.entry)

    def test_submodule_gitlink_manifest_mismatch(self):
        dst = self.detached_fixture()
        with self.assertRaisesRegex(ValueError, "gitlinks"):
            snap.inspect_checkout(dst, {**self.entry, "submodules": {"vendor": self.sha}})

    def test_does_not_overwrite_failed_missing_clone(self):
        dst = self.root / "unavailable"
        with patch.object(snap, "git", side_effect=ValueError("synthetic unavailable origin")):
            with self.assertRaisesRegex(ValueError, "unavailable origin"):
                snap.checkout_one(self.entry, dst)
        self.assertFalse(dst.exists())
        self.assertEqual(list(self.root.glob(".tycho-clone-*")), [])


    def test_full_checkout_lifecycle_with_disposable_local_origin(self):
        """Only the clone transport is swapped for a local Git fixture.

        Production manifest admission remains HTTPS-only; all checkout,
        gitlink, detached, hook and reinspection logic is the real code.
        """
        dst = self.root / "new-checkout"
        original = snap.git
        calls = []

        def fixture_clone(args, cwd=None, timeout=300):
            if args[0] == "clone":
                calls.append(args[0])
                system_git("clone", "-q", "--no-checkout",
                           str(self.origin), args[-1])
                return ""
            return original(args, cwd=cwd, timeout=timeout)

        with patch.object(snap, "git", side_effect=fixture_clone):
            self.assertEqual(snap.checkout_one(self.entry, dst), self.sha)
            self.assertEqual(snap.checkout_one(self.entry, dst), self.sha)
        self.assertEqual(calls, ["clone"], "same revision must not re-clone")
        self.assertEqual(system_git("rev-parse", "--abbrev-ref", "HEAD", cwd=dst), "HEAD")
        self.assertEqual(system_git("remote", cwd=dst), "")
        self.assertTrue((dst / ".git" / "hooks" / "pre-push").is_file())
        self.assertTrue((dst / ".git" / "hooks" / "pre-commit").is_file())
        self.assertFalse((dst / "README.md").stat().st_mode & 0o222)
        self.assertEqual(snap.inspect_checkout(dst, self.entry), self.sha)


if __name__ == "__main__":
    unittest.main()
