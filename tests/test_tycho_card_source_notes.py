import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C11 = ROOT / "book/volumes/v11-pattern-atlas/c11-security-operations/README.md"


class CardSourceNoteTests(unittest.TestCase):
    def test_no_stale_asvs_overview_note(self):
        text = C11.read_text().lower()
        self.assertNotIn("fourteen headings", text)
        self.assertNotIn("it has no levels or verification requirements headings", text)

    def test_mtls_note_names_the_supported_headings(self):
        text = C11.read_text()
        for heading in ("Istio identity", "Identity and certificate management",
                        "Authentication", "Mutual TLS authentication",
                        "Secure naming", "Peer authentication",
                        "Authorization", "Authorization policies"):
            self.assertIn(heading, text)


if __name__ == "__main__":
    unittest.main()
