"""Regression tests for hash-pinned reviewed binary media."""
import hashlib
import json
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_boundary as guard  # noqa: E402


class ReviewedMediaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "governance").mkdir()
        (self.root / "media").mkdir()
        self.binary = self.root / "media" / "example.jpg"
        self.binary.write_bytes(b"\xff\xd8\xff\x00not-text")
        self.digest = hashlib.sha256(self.binary.read_bytes()).hexdigest()
        self.manifest = self.root / "governance" / "reviewed-media.json"

    def tearDown(self):
        self.temp.cleanup()

    def entry(self, **overrides):
        item = {
            "path": "media/example.jpg",
            "sha256": self.digest,
            "reviewed_at": "2026-11-01",
            "reviewed_by": "project owner",
            "origin": "Project-supplied fixture.",
            "rights": "Synthetic test fixture; no third-party rights.",
        }
        item.update(overrides)
        return item

    def write_manifest(self, entries, version=1):
        self.manifest.write_text(
            json.dumps({"version": version, "media": entries}),
            encoding="utf-8",
        )

    def run_main(self):
        output = StringIO()
        with patch.object(guard, "ROOT", self.root), redirect_stdout(output):
            code = guard.main()
        return code, output.getvalue()

    def test_matching_binary_is_skipped(self):
        self.write_manifest([self.entry()])
        code, output = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn("hash-pinned reviewed media", output)

    def test_hash_mismatch_fails(self):
        self.write_manifest([self.entry(sha256="0" * 64)])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("reviewed media hash mismatch", output)

    def test_unlisted_binary_fails(self):
        self.write_manifest([])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("unscannable file requires explicit origin review", output)

    def test_text_file_cannot_bypass_scanning(self):
        self.binary.unlink()
        text = self.root / "media" / "notes.md"
        token = "ba" + "nk"
        text.write_text("This note mentions " + token + " terminology.", encoding="utf-8")
        digest = hashlib.sha256(text.read_bytes()).hexdigest()
        self.write_manifest([self.entry(path="media/notes.md", sha256=digest)])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("industry-specific terminology is prohibited", output)
        self.assertIn("stale reviewed-media entry", output)

    def test_stale_entry_fails(self):
        self.write_manifest([self.entry(path="media/missing.jpg")])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("stale reviewed-media entry", output)

    def test_malformed_manifest_fails(self):
        self.manifest.write_text("{not json", encoding="utf-8")
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("not readable JSON", output)

    def test_duplicate_paths_fail(self):
        self.write_manifest([self.entry(), self.entry()])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("duplicate path", output)

    def test_unknown_fields_fail(self):
        self.write_manifest([self.entry(extra="not allowed")])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("missing or unknown fields", output)

    def test_invalid_hash_fails(self):
        self.write_manifest([self.entry(sha256="not-a-digest")])
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("invalid SHA-256", output)

    def test_unsupported_manifest_version_fails(self):
        self.write_manifest([self.entry()], version=2)
        code, output = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("unsupported schema", output)


if __name__ == "__main__":
    unittest.main()
