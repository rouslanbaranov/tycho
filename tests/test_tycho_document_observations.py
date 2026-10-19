"""E03-04 offline tests; no public web calls or source mirroring."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import document_observations as d  # noqa: E402


class FakeResponse:
    def __init__(self, url, body=b"<html>synthetic</html>", kind="text/html", status=200):
        self.url, self.body, self.status = url, body, status
        self.headers = {"Content-Type": kind, "ETag": "fixture-etag"}
    def geturl(self):
        return self.url
    def getcode(self):
        return self.status
    def read(self, size):
        return self.body[:size]
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False


class FakeOpener:
    def __init__(self, result):
        self.result = result
        self.calls = 0
    def open(self, request, timeout):
        self.calls += 1
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class ObservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "sources/register.json").read_text())
        cls.entry = next(x for x in cls.registry["sources"] if x["id"] == "src.http-semantics")

    def empty(self):
        return {"schema_version": 1, "scope": "synthetic, metadata-only", "observations": []}

    def fixture(self, content=b"<html>synthetic</html>"):
        opener = FakeOpener(FakeResponse(self.entry["url"], content))
        return d.acquire(self.entry, opener=opener)

    def test_empty_canonical_ledger_validates(self):
        original = json.loads((ROOT / "sources/document-observations.json").read_text())
        self.assertEqual(d.check_observations(original, self.registry), 0)

    def test_public_admission_and_pending_source_blocked(self):
        self.assertEqual(d.admitted_source(self.registry, self.entry["id"])["id"], self.entry["id"])
        with self.assertRaises(ValueError):
            d.admitted_source(self.registry, "src.jep491")
        with self.assertRaises(ValueError):
            d.admitted_source(self.registry, "src.unknown")

    def test_synthetic_fetch_hash_and_no_content_mirroring(self):
        body = b"<html>this is a fictional fixture</html>"
        out = self.fixture(body)
        self.assertEqual(out["content_sha256"], hashlib.sha256(body).hexdigest())
        self.assertEqual(out["bytes_read"], len(body))
        self.assertEqual(out["access_scope"], "metadata-only")
        self.assertNotIn("body", out)
        self.assertNotIn(body.decode(), json.dumps(out))
        self.assertEqual(d.check_observations({**self.empty(), "observations": [out]}, self.registry), 1)

    def test_http_403_preserves_unavailable_not_fake_content(self):
        error = HTTPError(self.entry["url"], 403, "Forbidden", {}, None)
        out = d.acquire(self.entry, opener=FakeOpener(error))
        self.assertEqual(out["state"], "unavailable")
        self.assertIsNone(out["content_sha256"])
        self.assertEqual(out["bytes_read"], 0)
        self.assertEqual(d.check_observations({**self.empty(), "observations": [out]}, self.registry), 1)

    def test_reject_unsafe_origin_and_document_type(self):
        for url in ("http://example.com/a", "https://" + "127.0.0.1/a",
                    "https://user:pass@example.com/a", "https://example.com/a#secret"):
            self.assertFalse(d.public_https(url))
        with self.assertRaisesRegex(ValueError, "type"):
            d.acquire(self.entry, opener=FakeOpener(
                FakeResponse(self.entry["url"], b"binary", "application/pdf")))

    def test_reject_excessive_or_empty_content(self):
        with self.assertRaisesRegex(ValueError, "oversized"):
            d.acquire(self.entry, opener=FakeOpener(
                FakeResponse(self.entry["url"], b"x" * (d.MAX_BYTES + 1))))
        with self.assertRaisesRegex(ValueError, "empty"):
            d.acquire(self.entry, opener=FakeOpener(
                FakeResponse(self.entry["url"], b"")))

    def test_reject_cross_origin_response_without_persisting(self):
        with self.assertRaisesRegex(ValueError, "origin"):
            d.acquire(self.entry, opener=FakeOpener(
                FakeResponse("https://not-the-publisher.example/redirect")))

    def test_detect_meaningful_metadata_change_candidates(self):
        old = self.fixture(b"version-one")
        changed = deepcopy(old)
        changed["content_sha256"] = hashlib.sha256(b"version-two").hexdigest()
        changed["fetched_at"] = "2026-10-20T12:00:00+00:00"
        a = {**self.empty(), "observations": [old]}
        b = {**self.empty(), "observations": [changed]}
        delta = d.delta(a, b)
        self.assertEqual(len(delta), 1)
        self.assertEqual(delta[0]["change"], "candidate-re-review")
        self.assertIn("content_sha256", delta[0]["changed_metadata"])

    def test_unchanged_metadata_does_not_trigger_false_change(self):
        old = self.fixture(b"same bytes")
        newer = deepcopy(old)
        newer["fetched_at"] = "2026-10-20T12:00:00+00:00"
        self.assertEqual(d.delta({**self.empty(), "observations": [old]},
                                 {**self.empty(), "observations": [newer]}), [])

    def test_append_history_preserves_prior_records(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "ledger.json"
            path.write_text(json.dumps(self.empty()))
            a = self.fixture(b"first")
            d.append_record(path, self.registry, a)
            b = self.fixture(b"second")
            b["fetched_at"] = "2026-10-20T12:00:00+00:00"
            d.append_record(path, self.registry, b)
            readback = json.loads(path.read_text())
            self.assertEqual(len(readback["observations"]), 2)
            self.assertEqual(readback["observations"][0]["content_sha256"], a["content_sha256"])
            self.assertEqual(readback["observations"][1]["content_sha256"], b["content_sha256"])

    def test_duplicate_timestamp_and_fabricated_licence_rejected(self):
        rec = self.fixture()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            d.check_observations({**self.empty(), "observations": [rec, rec]}, self.registry)
        changed = deepcopy(rec)
        changed["rights_status"] = "approved"
        with self.assertRaisesRegex(ValueError, "reuse rights"):
            d.check_observations({**self.empty(), "observations": [changed]}, self.registry)


if __name__ == "__main__":
    unittest.main()
