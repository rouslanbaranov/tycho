"""Offline E03-05 research checkpoint tests: append-only history and source scope."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import research_checkpoints as r  # noqa: E402


class ResearchCheckpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.events = json.loads((ROOT / "sources/research-events.json").read_text())
        cls.sources = json.loads((ROOT / "sources/register.json").read_text())
        cls.claims = json.loads((ROOT / "sources/claim-references.json").read_text())

    def validate(self, events=None):
        return r.validate(events if events is not None else self.events,
                          self.sources, self.claims)

    def test_example_contains_distinct_entry_section_and_blocked(self):
        self.assertEqual(self.validate(), {"events": 4, "slices": 3})
        self.assertEqual(r.current(self.events["events"])["slice.idempotency-claim"]["kind"],
                         "section-inspected")

    def test_report_is_deterministic_and_matches_checked_in_generated_file(self):
        generated = r.render(self.events)
        self.assertEqual(generated,
                         (ROOT / "sources/RESEARCH-CHECKPOINTS.md").read_text())
        self.assertIn("no verified section", generated)
        self.assertNotIn("fully reviewed", generated)

    def test_unadmitted_jep_cannot_claim_section_read(self):
        data = deepcopy(self.events)
        e = data["events"][-1]
        e["kind"] = "section-inspected"
        e["section"] = "Imaginary subsection"
        e["status"] = "ready-for-review"
        with self.assertRaisesRegex(ValueError, "unadmitted"):
            self.validate(data)

    def test_landing_only_cannot_be_marked_readiness(self):
        data = deepcopy(self.events)
        data["events"][0]["status"] = "ready-for-review"
        with self.assertRaises(ValueError):
            self.validate(data)

    def test_section_read_requires_exact_section(self):
        data = deepcopy(self.events)
        data["events"][1]["section"] = None
        with self.assertRaisesRegex(ValueError, "exact inspected section"):
            self.validate(data)

    def test_duplicate_event_ids_refused(self):
        data = deepcopy(self.events)
        data["events"].append(deepcopy(data["events"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate immutable"):
            self.validate(data)

    def test_invalid_claim_reference_refused(self):
        data = deepcopy(self.events)
        data["events"][1]["claim_ids"] = ["claim.fake"]
        with self.assertRaisesRegex(ValueError, "unknown claim"):
            self.validate(data)

    def test_wrong_publisher_host_rejected(self):
        data = deepcopy(self.events)
        data["events"][0]["reference_url"] = "https://unrelated.example/article"
        with self.assertRaisesRegex(ValueError, "canonical"):
            self.validate(data)

    def test_historical_order_violation_rejected(self):
        data = deepcopy(self.events)
        data["events"][1]["observed_on"] = "2026-10-01"
        with self.assertRaisesRegex(ValueError, "observation-date order"):
            self.validate(data)

    def test_appending_new_event_does_not_erase_prior_history(self):
        with tempfile.TemporaryDirectory() as root:
            p = Path(root) / "research.json"
            p.write_text(json.dumps(self.events))
            event = deepcopy(self.events["events"][1])
            event["id"] = "evt.aws-idempotency.next-review"
            event["kind"] = "checkpoint"
            event["section"] = None
            event["status"] = "blocked"
            event["finding"] = "Independent review not completed"
            event["next_action"] = "Request named human or domain review"
            event["observed_on"] = "2026-10-20"
            r.append_event(p, self.sources, self.claims, event)
            state = json.loads(p.read_text())
            self.assertEqual(len(state["events"]), 5)
            self.assertEqual(state["events"][:4], self.events["events"])
            self.assertEqual(r.current(state["events"])["slice.idempotency-claim"]["status"],
                             "blocked")


if __name__ == "__main__":
    unittest.main()
