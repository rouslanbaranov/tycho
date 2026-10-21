import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_markdown_line_length import check_text


class MarkdownLineLengthTests(unittest.TestCase):
    def test_short_line_passes(self):
        self.assertEqual(check_text("short")[0], [])

    def test_long_prose_is_rejected(self):
        violations, exceptions = check_text("word " * 30)
        self.assertEqual(exceptions, 0)
        self.assertEqual(len(violations), 1)

    def test_exact_owner_link_is_an_exception(self):
        line = "**Technical owner.** [Owner](" + "a" * 120 + ")"
        violations, exceptions = check_text(line)
        self.assertEqual(violations, [])
        self.assertEqual(exceptions, 1)

    def test_owner_link_with_note_is_exempt(self):
        line = "**Technical owner.** [Owner](" + "a" * 120 + ") and more"
        violations, exceptions = check_text(line)
        self.assertEqual(exceptions, 1)
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
