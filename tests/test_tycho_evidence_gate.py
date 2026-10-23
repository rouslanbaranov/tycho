"""Pure checks for the evidence-aware refusal model."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import evidence_gate  # noqa: E402


class EvidenceGateTests(unittest.TestCase):
    def test_model_artifact_is_present_and_bounded(self):
        model = evidence_gate.load_model()
        self.assertIsNotNone(model)
        self.assertEqual(model["version"], evidence_gate.VERSION)
        self.assertGreater(model["threshold"], 0)
        self.assertLess(model["threshold"], 1)
        self.assertEqual(len(model["numeric_features"]),
                         len(model["means"]))
        self.assertEqual(len(model["numeric_features"]),
                         len(model["stds"]))

    def test_features_are_finite_and_complete(self):
        results = [{
            "score": 12.5,
            "title": "Cache design",
            "heading": "Cache invalidation",
            "excerpt": "A cache miss reads the origin and fills a TTL value.",
            "matched_terms": ["cache", "miss"],
        }]
        features = evidence_gate.extract_features(
            "How does a cache miss work?", results, 0.1)
        for name in evidence_gate.FEATURES:
            self.assertIn(name, features)
            self.assertIsInstance(features[name], (int, float))

    def test_probability_is_in_range(self):
        model = evidence_gate.load_model()
        results = [{
            "score": 10.0,
            "title": "Queue design",
            "heading": "Backpressure",
            "excerpt": "Queue depth and residence time.",
            "matched_terms": ["queue"],
        }]
        features = evidence_gate.extract_features(
            "How does queue backpressure work?", results, 0.2)
        probability = evidence_gate.probability(
            model, "How does queue backpressure work?", features)
        self.assertGreaterEqual(probability, 0.0)
        self.assertLessEqual(probability, 1.0)


if __name__ == "__main__":
    unittest.main()
