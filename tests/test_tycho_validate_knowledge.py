"""Offline tests for E04-06 knowledge validation composition.

These exercises use isolated fixtures or mock subprocesses; they do NOT
claim that the entire live repository or graph integration passed.
"""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_knowledge as k  # noqa: E402


class KnowledgeValidationTests(unittest.TestCase):
    def test_current_contract_versions(self):
        versions = k.contract_versions(ROOT)
        self.assertEqual(versions["sources/register.json"], 2)
        self.assertEqual(versions["sources/claim-references.json"], 1)

    def test_bad_version_fails_closed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, (_, version) in k.EXPECTED.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps({"schema_version":version}))
            for name in k.SCHEMAS:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps({"$schema":"https://json-schema.org/draft/2020-12/schema"}))
            file = root / "sources" / "claim-references.json"
            file.write_text(json.dumps({"schema_version":99}))
            with self.assertRaisesRegex(ValueError,"incompatible"):
                k.contract_versions(root)

    def test_missing_index_and_graph_not_reported_as_pass(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            checks, missing = k.ordered_checks(root, "available")
            self.assertTrue(any(x.startswith("routing-index") for x in missing))
            self.assertIn("graph-validator-not-implemented", missing)
            self.assertTrue(any(name == "source-register" for name,_ in checks))
            with self.assertRaisesRegex(ValueError,"strict knowledge validation unavailable"):
                k.ordered_checks(root, "strict")

    def test_optional_hooks_explicit_and_ordered(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("generated/route-index.v1.json", "scripts/validate_graph.py"):
                path = root / name
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text("{}")
            checks, missing = k.ordered_checks(root, "strict")
            self.assertFalse(missing)
            self.assertEqual([x[0] for x in checks][-2:], ["routing-index","graph-hook"])

    def test_structural_green_with_missing_hooks_still_incomplete(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for _name,argv in k.CORE:
                f = root / argv[0]
                f.parent.mkdir(parents=True,exist_ok=True)
                f.write_text("# pretend checker\n")
            with patch.object(k,"contract_versions",return_value={"sources/register.json":2}):
                with patch.object(k.subprocess,"run",return_value=SimpleNamespace(returncode=0)) as stub:
                    result = k.run(root,"available")
            self.assertEqual(result["outcome"],"incomplete")
            self.assertEqual(len(result["checks"]),len(k.CORE))
            self.assertTrue(all(x["status"]=="passed" for x in result["checks"]))
            self.assertEqual(stub.call_count,len(k.CORE))

    def test_checker_failure_stops_chain(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for _name,argv in k.CORE:
                f = root / argv[0]
                f.parent.mkdir(parents=True,exist_ok=True)
                f.write_text("# checker\n")
            with patch.object(k,"contract_versions",return_value={}):
                with patch.object(k.subprocess,"run",side_effect=[
                    SimpleNamespace(returncode=0), SimpleNamespace(returncode=9)
                ]) as stub:
                    result = k.run(root,"available")
            self.assertEqual(result["outcome"],"failed")
            self.assertEqual(len(result["checks"]),2)
            self.assertEqual(stub.call_count,2)

    def test_mode_rejection(self):
        with self.assertRaises(ValueError):
            k.ordered_checks(ROOT,"invented")


if __name__=="__main__":
    unittest.main()
