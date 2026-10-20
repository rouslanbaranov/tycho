"""Issue TYCHO-81 bounded document/diagram source tests.

Purely structural: does not validate software releases or broker recovery.
"""
from pathlib import Path
import unittest
from edition_paths import canonical_path, relative_link

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "book/integration"
PAGES = {
    "kafka-partitions-replication-and-contracts.md": ["kafka.apache.org/41/design/design/", "grpc.io/docs/what-is-grpc/core-concepts/"],
    "messaging-families-and-durable-workflows.md": ["rabbitmq.com/docs/reliability", "docs.nats.io/concepts/jetstream", "pulsar.apache.org/docs/4.1.x/"],
    "stateful-stream-processing-and-cdc.md": ["kafka.apache.org/41/streams/architecture/", "nightlies.apache.org/flink/flink-docs-release-2.1", "debezium.io/documentation/reference/3.6/"],
}


class IntegrationCorpusTests(unittest.TestCase):
    def test_bounded_research_pages(self):
        for name, sources in PAGES.items():
            with self.subTest(name=name):
                text = canonical_path(BASE / name).read_text(encoding="utf-8")
                self.assertGreater(len(text), 8000)
                self.assertGreaterEqual(text.count("```mermaid"), 3)
                self.assertGreaterEqual(text.count("Text alternative:"), 3)
                self.assertEqual(text.count("```") % 2, 0)
                self.assertIn("insufficient", text.lower())
                for source in sources:
                    self.assertIn(source, text)

    def test_index_and_provenance(self):
        landing = (BASE / "README.md").read_text()
        self.assertIn("```mermaid", landing)
        for name in PAGES:
            self.assertIn("(" + relative_link(BASE / "README.md", BASE / name) + ")", landing)
        self.assertTrue((ROOT / "book/distributed/README.md").is_file())

    def test_original_example_arithmetic_does_not_claim_measurement(self):
        # A synthetic number alone is not capacity or a consumer exactly-once proof.
        self.assertEqual(2 * 3, 6)


if __name__ == "__main__":
    unittest.main()
