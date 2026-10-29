import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from source_content_hash import canonical_text, digest


class SourceContentHashTests(unittest.TestCase):
    def test_article_marker_and_digest(self):
        html = ('<html><body><nav>ignore</nav>'
                '<div class="devsite-article-body clearfix"><h1>Title</h1>'
                '<p>Useful text.</p></div><footer>ignore</footer></body></html>')
        text = canonical_text(html)
        self.assertIn("Useful text.", text)
        self.assertNotIn("ignore", text)
        self.assertEqual(len(digest(text)), 64)


if __name__ == "__main__":
    unittest.main()
