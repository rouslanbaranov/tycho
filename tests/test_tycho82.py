"""TYCHO-82 document structure and local navigation checks.

These tests do NOT prove Java framework semantics, JDK pinning, benchmark
performance, external URL availability or independent technical review.
"""
from pathlib import Path
import re
import unittest
from edition_paths import canonical_path, relative_link, read_original_manuscript

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "book/execution"
SOURCES = {
    "platform-threads-executors-and-virtual-threads.md": (
        "openjdk.org/jeps/444",
        "mail.openjdk.org/pipermail/core-libs-dev/2024-November/",
        "spring-boot/3.3/reference/",
    ),
    "reactor-webflux-r2dbc-and-backpressure.md": (
        "projectreactor.io/docs/core/3.7.0/",
        "spring-framework/reference/6.2/",
        "r2dbc.io/spec/1.0.0.RELEASE/",
    ),
    "vertx-netty-quarkus-mutiny-and-rxjava.md": (
        "vertx.io/docs/4.4.9/",
        "quarkus.io/version/3.27/",
        "smallrye.io/smallrye-mutiny/2.9.0/",
        "github.com/ReactiveX/RxJava/blob/v3.1.9/",
        "netty.io/wiki/user-guide-for-4.x.html",
    ),
}


class ExecutionCorpusTests(unittest.TestCase):
    def test_pages_have_substantial_original_explanation_and_evidence(self):
        for name, urls in SOURCES.items():
            with self.subTest(page=name):
                page = read_original_manuscript(canonical_path(BASE / name))
                self.assertGreater(len(page), 9000)
                self.assertGreaterEqual(page.count("```mermaid"), 2)
                self.assertGreaterEqual(page.count("Text alternative:"), 2)
                self.assertEqual(page.count("```") % 2, 0)
                self.assertIn("Evidence", page)
                self.assertIn("not", page.lower())
                for url in urls:
                    self.assertIn(url, page)

    def test_landing_and_book_index_link_to_real_files(self):
        landing = (BASE / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "book/README.md").read_text(encoding="utf-8")
        self.assertIn("execution/README.md", index)
        self.assertIn("```mermaid", landing)
        for name in SOURCES:
            self.assertIn("(" + relative_link(BASE / "README.md", BASE / name) + ")", landing)
            self.assertTrue(canonical_path(BASE / name).is_file())

    def test_relative_links_in_new_pages_resolve(self):
        for path in [BASE / "README.md", *(canonical_path(BASE / n) for n in SOURCES)]:
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                for target in re.findall(r"\]\(([^)]+)\)", text):
                    if target.startswith(("https://", "http://", "#", "mailto:")):
                        continue
                    local = target.split("#", 1)[0]
                    if local:
                        self.assertTrue((path.parent / local).is_file(), target)


if __name__ == "__main__":
    unittest.main()
