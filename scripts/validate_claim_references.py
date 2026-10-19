#!/usr/bin/env python3
"""Validate traceable technical claims against Tycho's admitted public inventory.

This checks structure, references and admission status. It CANNOT prove that a
cited source supports a claim, that a human read a section, or that its licence
permits republication. It makes no network requests or source changes.
"""
import argparse
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "sources" / "claim-references.json"
REGISTER = ROOT / "sources" / "register.json"
LOCK = ROOT / "sources" / "public-repositories.lock.json"
CLAIM_ID = re.compile(r"^claim\.[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_ID = re.compile(r"^src\.[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
VALID_REL = {"supports", "qualifies", "contradicts", "unavailable"}
VALID_STATUS = {"proposed", "evidence-linked", "contested", "insufficient-evidence"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def strict_fields(obj, keys, label):
    require(isinstance(obj, dict) and set(obj) == set(keys),
            label + ": invalid fields")


def plain_text(value, label):
    require(isinstance(value, str) and bool(value.strip())
            and len(value) < 5000, label + ": expected bounded nonempty string")


def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return False
    p = PurePosixPath(value)
    return all(chunk not in {"", ".", "..", ".git"} for chunk in value.split("/")) and len(p.parts) > 0


def validate_location(loc, source, locked, prefix):
    strict_fields(loc, {"kind", "url", "section", "revision", "path", "symbol"}, prefix)
    kind = loc["kind"]
    require(kind in {"document-section", "source-code"}, prefix + ": invalid kind")
    if kind == "document-section":
        require(loc["revision"] is None and loc["path"] is None and loc["symbol"] is None,
                prefix + ": document cannot claim a code revision/path")
        plain_text(loc["url"], prefix + ".url")
        plain_text(loc["section"], prefix + ".section")
        origin = urlsplit(source["url"])
        target = urlsplit(loc["url"])
        require(target.scheme == "https" and target.hostname == origin.hostname
                and not target.username and not target.password
                and not target.fragment and not target.query,
                prefix + ": document URL must be on canonical source origin")
    else:
        require(loc["url"] is None and loc["section"] is None,
                prefix + ": code must use lock commit, path and optional symbol")
        require(source["id"] in locked, prefix + ": code source must be pinned in lock")
        require(isinstance(loc["revision"], str) and SHA.fullmatch(loc["revision"]),
                prefix + ": bad Git revision")
        require(loc["revision"] == locked[source["id"]], prefix + ": revision differs from pinned source")
        require(safe_path(loc["path"]), prefix + ": invalid code path")
        if loc["symbol"] is not None:
            plain_text(loc["symbol"], prefix + ".symbol")


def validate(data, source_register, repository_lock):
    strict_fields(data, {"schema_version", "claims"}, "claims")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "unsupported claim-reference schema")
    require(isinstance(data["claims"], list) and bool(data["claims"]), "no claims")
    sources = {s["id"]: s for s in source_register["sources"]}
    locked = {r["id"]: r["revision"] for r in repository_lock["repositories"]}
    used = set()
    for claim in data["claims"]:
        strict_fields(claim, {"id", "statement", "owner_page", "status",
                              "applicability", "evidence"}, "claim")
        cid = claim["id"]
        require(isinstance(cid, str) and CLAIM_ID.fullmatch(cid), "invalid claim ID")
        require(cid not in used, "duplicate claim ID " + cid)
        used.add(cid)
        plain_text(claim["statement"], cid + ".statement")
        require(safe_path(claim["owner_page"]) and claim["owner_page"].endswith(".md"),
                cid + ": unsafe owning Markdown page")
        require(claim["status"] in VALID_STATUS, cid + ": invalid status")
        strict_fields(claim["applicability"], {"conditions", "exclusions"}, cid + ".applicability")
        for dimension in ("conditions", "exclusions"):
            values = claim["applicability"][dimension]
            require(isinstance(values, list), cid + ": applicability must be lists")
            for value in values:
                plain_text(value, cid + ".applicability." + dimension)
        require(isinstance(claim["evidence"], list) and bool(claim["evidence"]), cid + ": no evidence")
        relations = set()
        for ev in claim["evidence"]:
            strict_fields(ev, {"source_id", "relation", "reasoning", "observed_at",
                               "location", "verification"}, cid + ".evidence")
            sid = ev["source_id"]
            require(isinstance(sid, str) and SOURCE_ID.fullmatch(sid) and sid in sources,
                    cid + ": unknown source ID")
            require(ev["relation"] in VALID_REL, cid + ": invalid evidence relation")
            relations.add(ev["relation"])
            plain_text(ev["reasoning"], cid + ".reasoning")
            require(ev["verification"] in {"section-inspected", "identifier-only", "not-accessible"},
                    cid + ": invalid verification")
            require(isinstance(ev["observed_at"], str), cid + ": observation date missing")
            date.fromisoformat(ev["observed_at"])
            if ev["relation"] == "unavailable":
                require(ev["verification"] == "not-accessible" and ev["location"] is None,
                        cid + ": unavailable source cannot masquerade as inspected")
            else:
                require(sources[sid]["admission"] == "admitted-for-research",
                        cid + ": bibliography-only/pending source cannot support claims")
                require(ev["verification"] == "section-inspected",
                        cid + ": evidence relation must cite inspected location")
                validate_location(ev["location"], sources[sid], locked, cid + "." + sid)
        if claim["status"] == "evidence-linked":
            require("supports" in relations and "contradicts" not in relations,
                    cid + ": evidence-linked requires support without unresolved contradiction")
        if "contradicts" in relations:
            require(claim["status"] == "contested",
                    cid + ": contradictory evidence must remain contested")
    return {"claims": len(used), "sources": len(sources), "pinned_repositories": len(locked)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--claims", type=Path, default=CLAIMS)
    p.add_argument("--register", type=Path, default=REGISTER)
    p.add_argument("--lock", type=Path, default=LOCK)
    args = p.parse_args()
    data = json.loads(args.claims.read_text(encoding="utf-8"))
    src = json.loads(args.register.read_text(encoding="utf-8"))
    lock = json.loads(args.lock.read_text(encoding="utf-8"))
    outcome = validate(data, src, lock)
    for c in data["claims"]:
        local = ROOT / c["owner_page"]
        if not local.is_file():
            raise ValueError("Owner page missing in current checkout: " + c["owner_page"])
    print("PASS: traceable claims, inventory IDs, evidence status and pinned references", outcome)


if __name__ == "__main__":
    main()
