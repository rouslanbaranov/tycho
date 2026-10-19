"""E04-03 deterministic frontmatter insertion tests, all standard library."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import frontmatter_generate as gen  # noqa: E402


class FrontmatterGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads((ROOT / "fixtures/metadata-valid-page.v1.json").read_text())

    def test_stable_rendering_and_noninvented_dates(self):
        a = gen.render(self.record)
        self.assertEqual(a, gen.render(deepcopy(self.record)))
        self.assertIn('id: "tycho.page.01h9abcdef"', a)
        self.assertIn("content_verified_at: null", a)
        self.assertIn("source_inspection_date: null", a)
        self.assertIn("status: \"draft\"", a)

    def test_deterministic_order_independent_of_json_field_order(self):
        reverse = dict(reversed(list(self.record.items())))
        self.assertEqual(gen.render(reverse), gen.render(self.record))

    def test_fresh_document_receives_header_without_body_edit(self):
        original = "# Real page\n\nKeep explanation unchanged.\n"
        header = gen.render(self.record)
        status, result = gen.proposed_change(original, header)
        self.assertEqual(status, "would-insert")
        self.assertTrue(result.endswith(original))

    def test_existing_exact_frontmatter_is_idempotent(self):
        original = gen.render(self.record) + "\n# Preserved body\n"
        status, result = gen.proposed_change(original, gen.render(self.record))
        self.assertEqual(status, "unchanged")
        self.assertEqual(result, original)

    def test_changed_metadata_preserves_existing_identifiers_and_review(self):
        original = gen.render(self.record) + "\n# Body\n"
        changed = deepcopy(self.record)
        changed["id"] = "tycho.page.02h9abcdef"
        status, result = gen.proposed_change(original, gen.render(changed))
        self.assertEqual(status, "conflict-existing-frontmatter")
        self.assertEqual(result, original)

    def test_malformed_existing_frontmatter_never_replaced(self):
        with self.assertRaisesRegex(ValueError, "Malformed"):
            gen.proposed_change("---\nid: existing\n# Missing closing fence", gen.render(self.record))

    def test_explicit_write_gate_and_idempotent_apply(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root / "book/performance/queueing-littles-law.md"
            path.parent.mkdir(parents=True)
            original = "# Existing technical prose\n\nOriginal claim wording.\n"
            path.write_text(original)
            header = gen.render(self.record)
            self.assertEqual(gen.apply_safe(path, header, allow_write=False), "would-insert")
            self.assertEqual(path.read_text(), original)
            self.assertEqual(gen.apply_safe(path, header, allow_write=True), "inserted")
            self.assertEqual(gen.apply_safe(path, header, allow_write=True), "unchanged")
            self.assertEqual(path.read_text(), header + "\n" + original)
            self.assertEqual(gen.target_path(root, self.record), path)

    def test_traversal_and_nonbook_targets_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            for invalid in ("../secrets.md", "authoring/STATE.md",
                            "book/../restricted.md", "/tmp/absolute.md"):
                doc = {**self.record, "canonical_path": invalid}
                with self.assertRaises(ValueError):
                    gen.target_path(d, doc)

    def test_extra_fields_and_bad_id_never_rendered(self):
        with self.assertRaisesRegex(ValueError, "exact v1 keys"):
            gen.render({**self.record, "verified_by_model": True})
        with self.assertRaisesRegex(ValueError, "identity"):
            gen.render({**self.record, "id": "tycho.page../secret"})

    def test_invalid_nested_yaml_array_is_rejected(self):
        bad = deepcopy(self.record)
        bad["route_hints"]["questions"] = [{"bad": "nested"}]
        with self.assertRaisesRegex(ValueError, "Nested YAML array"):
            gen.render(bad)


if __name__ == "__main__":
    unittest.main()
