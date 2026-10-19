#!/usr/bin/env python3
"""Explicit metadata-only acquisition of admitted public web documents.

Does not store copied documents, refresh source registers, reindex chapters,
trigger enrichment, reset Git clones, or infer licensing rights. Network GET
requires an explicit --allow-network flag. Uses only Python standard library.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources" / "register.json"
LEDGER = ROOT / "sources" / "document-observations.json"
MAX_BYTES = 2 * 1024 * 1024
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CONTENT_TYPES = {"text/plain", "text/html", "application/json", "text/xml", "application/xml"}
FIELDS = {"source_id", "requested_url", "resolved_url", "fetched_at",
          "source_version", "http_status", "state", "content_type",
          "bytes_read", "content_sha256", "etag", "last_modified",
          "access_scope", "rights_status", "reason"}


def require(ok, why):
    if not ok:
        raise ValueError(why)


def public_https(value):
    try:
        u = urlsplit(value)
        if u.scheme != "https" or not u.hostname or u.username or u.password or u.fragment:
            return False
        ip = None
        try:
            ip = ipaddress.ip_address(u.hostname)
        except ValueError:
            pass
        host = u.hostname.lower().rstrip('.')
        return (ip is None and host not in {'localhost'}
                and not host.endswith(('.local', '.internal', '.test', '.example'))
                and u.port in (None, 443))
    except ValueError:
        return False


def check_observations(data, inventory):
    require(isinstance(data, dict) and set(data) == {"schema_version", "scope", "observations"},
            "unexpected observation ledger fields")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "unsupported observation ledger schema")
    require(isinstance(data["scope"], str) and bool(data["scope"].strip()), "missing scope")
    require(isinstance(data["observations"], list), "observation list required")
    ids = {x["id"] for x in inventory["sources"]}
    used = set()
    for rec in data["observations"]:
        require(isinstance(rec, dict) and set(rec) == FIELDS, "unexpected observation fields")
        require(rec["source_id"] in ids, "unregistered observation source")
        require(rec["state"] in {"available", "unavailable"}, "invalid observation state")
        require(rec["access_scope"] == "metadata-only", "external content not allowed in ledger")
        require(rec["rights_status"] == "not-assessed", "observation must not infer reuse rights")
        require(public_https(rec["requested_url"]) and public_https(rec["resolved_url"]),
                "invalid observed public URL")
        dt = datetime.fromisoformat(rec["fetched_at"])
        require(dt.tzinfo is not None, "observation must use an aware timestamp")
        require(isinstance(rec["source_version"], str) and bool(rec["source_version"].strip()),
                "source version/scope required")
        require(type(rec["http_status"]) is int and 100 <= rec["http_status"] <= 599,
                "invalid HTTP status")
        require(type(rec["bytes_read"]) is int and 0 <= rec["bytes_read"] <= MAX_BYTES,
                "invalid content size")
        if rec["state"] == "available":
            require(rec["http_status"] == 200 and rec["bytes_read"] > 0
                    and isinstance(rec["content_sha256"], str)
                    and SHA256.fullmatch(rec["content_sha256"]), "available record must have exact digest")
            require(rec["content_type"] in CONTENT_TYPES, "disallowed type")
            require(rec["reason"] is None, "available record cannot claim error")
        else:
            require(rec["bytes_read"] == 0 and rec["content_sha256"] is None
                    and isinstance(rec["reason"], str) and rec["reason"],
                    "unavailable cannot claim acquired content")
        for field in ("etag", "last_modified", "content_type"):
            require(rec[field] is None or isinstance(rec[field], str), "bad response header")
        identity = (rec["source_id"], rec["fetched_at"])
        require(identity not in used, "duplicate observation timestamp and source ID")
        used.add(identity)
    return len(used)


def read_ledger(path, registry):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    check_observations(data, registry)
    return data


def admitted_source(inventory, sid):
    entries = [x for x in inventory["sources"] if x["id"] == sid]
    require(len(entries) == 1, "unknown source ID")
    entry = entries[0]
    require(entry["admission"] == "admitted-for-research",
            "source not admitted for technical evidence")
    require(entry["access"] == "public-web-or-author-download",
            "source access needs separate authorization")
    require(public_https(entry["url"]) and public_https(entry["resolved_url"]),
            "canonical or resolved origin is not a public HTTPS hostname")
    return entry


class RestrictedRedirect(HTTPRedirectHandler):
    """Allow only HTTPS redirects to registered canonical/resolved hostnames."""

    def __init__(self, hosts):
        self.hosts = hosts
        super().__init__()

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        target = urlsplit(newurl)
        require(public_https(newurl) and target.hostname in self.hosts,
                "cross-origin or unsafe redirect rejected")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def acquire(entry, *, timeout=20, opener=None):
    start_url = entry["url"]
    hosts = {urlsplit(entry["url"]).hostname, urlsplit(entry["resolved_url"]).hostname}
    require(public_https(start_url), "source origin invalid")
    if opener is None:
        opener = build_opener(RestrictedRedirect(hosts))
    request = Request(start_url, headers={
        "User-Agent": "TychoPublicResearchSnapshot/1.0 (metadata-only)",
        "Accept": "text/html,text/plain,application/json,application/xml,text/xml",
    })
    stamp = datetime.now(timezone.utc).isoformat()
    try:
        response = opener.open(request, timeout=timeout)
    except HTTPError as exc:
        error_url = exc.geturl()
        require(public_https(error_url) and urlsplit(error_url).hostname in hosts,
                'HTTP error came from unexpected redirect origin')
        if exc.code not in (401, 403, 404, 410, 429):
            raise ValueError("Document fetch error; no record written: HTTP " + str(exc.code)) from exc
        return {
            "source_id": entry["id"], "requested_url": start_url, "resolved_url": error_url,
            "fetched_at": stamp, "source_version": entry["version"],
            "http_status": exc.code, "state": "unavailable", "content_type": None,
            "bytes_read": 0, "content_sha256": None, "etag": None, "last_modified": None,
            "access_scope": "metadata-only", "rights_status": "not-assessed",
            "reason": "HTTP " + str(exc.code) + "; no technical content inspected",
        }
    with response:
        final_url = response.geturl()
        require(public_https(final_url) and urlsplit(final_url).hostname in hosts,
                "unexpected final response origin")
        status = response.getcode()
        require(status == 200, "non-200 response not admitted")
        kind = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        require(kind in CONTENT_TYPES, "content type not explicitly supported")
        body = response.read(MAX_BYTES + 1)
        require(0 < len(body) <= MAX_BYTES, "empty or oversized document; no record written")
        return {
            "source_id": entry["id"], "requested_url": start_url, "resolved_url": final_url,
            "fetched_at": stamp, "source_version": entry["version"],
            "http_status": status, "state": "available", "content_type": kind,
            "bytes_read": len(body), "content_sha256": hashlib.sha256(body).hexdigest(),
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
            "access_scope": "metadata-only", "rights_status": "not-assessed", "reason": None,
        }


def delta(before, after):
    """Report re-review candidates, NOT semantic-change determinations."""
    def latest(records):
        result = {}
        for r in records:
            prev = result.get(r["source_id"])
            if prev is None or prev["fetched_at"] < r["fetched_at"]:
                result[r["source_id"]] = r
        return result
    old, new = latest(before["observations"]), latest(after["observations"])
    out = []
    for sid in sorted(set(old) | set(new)):
        a, b = old.get(sid), new.get(sid)
        if a is None:
            out.append({"source_id": sid, "change": "new-observation", "requires_review": True})
        elif b is None:
            out.append({"source_id": sid, "change": "missing-new-observation", "requires_review": False})
        else:
            changed = [k for k in ("state", "source_version", "content_sha256", "resolved_url", "http_status")
                       if a[k] != b[k]]
            if changed:
                out.append({"source_id": sid, "change": "candidate-re-review",
                            "changed_metadata": changed, "requires_review": True})
    return out


def append_record(path, registry, record):
    path = Path(path)
    original_bytes = path.read_bytes()
    data = json.loads(original_bytes)
    check_observations(data, registry)
    data["observations"].append(record)
    check_observations(data, registry)
    staged = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, encoding="utf-8",
                                         prefix=".observation-", delete=False) as out:
            staged = Path(out.name)
            json.dump(data, out, indent=2, sort_keys=True)
            out.write("\n")
        require(path.read_bytes() == original_bytes, "ledger changed concurrently; refuse overwrite")
        os.replace(staged, path)
        staged = None
    finally:
        if staged and staged.exists():
            staged.unlink()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("validate", "acquire", "compare"))
    p.add_argument("--source", help="Exact registered source ID for explicit acquisition")
    p.add_argument("--allow-network", action="store_true", help="Explicitly permit one admitted HTTPS GET")
    p.add_argument("--register", type=Path, default=REGISTRY)
    p.add_argument("--ledger", type=Path, default=LEDGER)
    p.add_argument("--before", type=Path)
    p.add_argument("--after", type=Path)
    args = p.parse_args()
    registry = json.loads(args.register.read_text(encoding="utf-8"))
    if args.action == "compare":
        require(args.before is not None and args.after is not None,
                "comparison requires before/after manifests")
        old = read_ledger(args.before, registry)
        new = read_ledger(args.after, registry)
        print(json.dumps(delta(old, new), indent=2))
    elif args.action == "validate":
        print("PASS observation records:", check_observations(
            json.loads(args.ledger.read_text(encoding="utf-8")), registry))
    else:
        require(args.allow_network and args.source, "acquire requires --source and --allow-network")
        entry = admitted_source(registry, args.source)
        obs = acquire(entry)
        append_record(args.ledger, registry, obs)
        print("Recorded only metadata:", obs["source_id"], obs["state"], obs["fetched_at"])


if __name__ == "__main__":
    main()
