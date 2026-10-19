#!/usr/bin/env python3
"""Append-only, public-source research reading and checkpoint CLI (E03-05).

Derived current state avoids overwriting historical observations. Separate from
source acquisition, content verification, book enrichment and indexing.
"""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "sources" / "research-events.json"
REGISTER = ROOT / "sources" / "register.json"
CLAIMS = ROOT / "sources" / "claim-references.json"
REPORT = ROOT / "sources" / "RESEARCH-CHECKPOINTS.md"
SCOPE = "Append-only research event examples for public-source slices; current status is derived from latest event per slice. No private sources or implied human approval."
FIELDS = {"id", "slice_id", "source_id", "observed_on", "kind",
          "section", "reference_url", "source_version", "claim_ids",
          "finding", "next_action", "status"}
KINDS = {"entry-inspected", "section-inspected", "dispute-recorded", "blocked", "checkpoint"}
STATES = {"researching", "ready-for-review", "blocked"}
TOKEN = re.compile(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*$")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data, registered, claims):
    require(isinstance(data, dict) and set(data) == {"schema_version", "scope", "events"},
            "unexpected research ledger fields")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "unsupported research ledger schema")
    require(isinstance(data["scope"], str) and bool(data["scope"].strip()),
            "missing provenance scope")
    require(isinstance(data["events"], list), "events must be an array")
    index = {s["id"]: s for s in registered["sources"]}
    claim_ids = {c["id"] for c in claims["claims"]}
    seen, last_dates = set(), {}
    for e in data["events"]:
        require(isinstance(e, dict) and set(e) == FIELDS, "invalid event fields")
        for name in ("id", "slice_id", "source_id", "source_version",
                     "finding", "next_action", "reference_url"):
            require(isinstance(e[name], str) and bool(e[name].strip()),
                    "missing event field: " + name)
        require(TOKEN.fullmatch(e["id"]) and e["id"].startswith("evt."), "invalid event ID")
        require(TOKEN.fullmatch(e["slice_id"]) and e["slice_id"].startswith("slice."),
                "invalid research slice ID")
        require(e["id"] not in seen, "duplicate immutable event ID")
        seen.add(e["id"])
        require(e["source_id"] in index, "unknown source ID in research event")
        source = index[e["source_id"]]
        require(e["kind"] in KINDS and e["status"] in STATES, "invalid research kind/status")
        when = date.fromisoformat(e["observed_on"])
        require(e["slice_id"] not in last_dates or when >= last_dates[e["slice_id"]],
                "research history out of observation-date order")
        last_dates[e["slice_id"]] = when
        require(isinstance(e["claim_ids"], list) and all(c in claim_ids for c in e["claim_ids"]),
                "unknown claim reference in research event")
        require(len(e["claim_ids"]) == len(set(e["claim_ids"])), "duplicate claim references")
        target = urlsplit(e["reference_url"])
        origin = urlsplit(source["url"])
        require(target.scheme == "https" and target.hostname == origin.hostname
                and not target.username and not target.password and not target.fragment,
                "research URL must use registered canonical public host")
        if e["kind"] in {"section-inspected", "dispute-recorded"}:
            require(source["admission"] == "admitted-for-research",
                    "unadmitted source cannot be claimed section-inspected")
            require(isinstance(e["section"], str) and e["section"].strip(),
                    "exact inspected section is required")
        else:
            require(e["section"] is None or isinstance(e["section"], str),
                    "section must be a string or null")
        if e["kind"] == "entry-inspected":
            require(e["section"] is None and e["status"] == "researching",
                    "entry inspection is not verified section research")
        if e["kind"] == "blocked":
            require(e["status"] == "blocked", "blocked event must remain blocked")
        if e["status"] == "ready-for-review":
            require(e["kind"] == "section-inspected",
                    "review readiness requires an inspected section")
        if e["kind"] == "checkpoint":
            require(e["status"] in {"researching", "blocked"},
                    "checkpoint alone cannot promote reading or independent review readiness")
        if source["admission"] != "admitted-for-research":
            require(e["kind"] in {"blocked", "checkpoint"},
                    "unadmitted source may not be marked inspected")
    return {"events": len(seen), "slices": len(last_dates)}


def current(events):
    # Historical events are never rewritten. The latest event in list order
    # owns the derived status, evidence limit and next action for its slice.
    out = {}
    for event in events:
        out[event["slice_id"]] = event
    return out


def render(data):
    lines = [
        "# Current bounded public research checkpoints", "",
        "Generated from [research-events.json](research-events.json); do not edit this file independently.",
        "These rows show the **latest event by append order**, not a historical overwrite or an approved technical claim.",
        "Source admission is verified separately; entry-page inspection is not full-section reading.",
        "", "| Slice | Latest kind/status | Source + scoped reference | Next finite action |",
        "|---|---|---|---|",
    ]
    for sid, e in sorted(current(data["events"]).items()):
        def esc(value):
            return value.replace("|", "\\|").replace("\n", " ")
        lines.append("| " + esc(sid) + " | " + esc(e["kind"] + " / " + e["status"]) +
                     " | " + esc(e["source_id"] + " — " + (e["section"] or "no verified section")) +
                     " | " + esc(e["next_action"]) + " |")
    lines.extend(["", "Do not upgrade this output to accepted evidence without actual source verification,",
                  "an independent review where required, and a separately recorded claim relationship.", ""])
    return "\n".join(lines)


def append_event(path, registry, claims, new_event):
    path = Path(path)
    old = path.read_bytes()
    data = json.loads(old)
    validate(data, registry, claims)
    data["events"].append(new_event)
    validate(data, registry, claims)
    staged = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                         prefix=".research-event-", delete=False) as out:
            staged = Path(out.name)
            json.dump(data, out, indent=2, ensure_ascii=False)
            out.write("\n")
        require(path.read_bytes() == old, "concurrent update: do not overwrite existing research history")
        os.replace(staged, path)
        staged = None
    finally:
        if staged and staged.exists():
            staged.unlink()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("validate", "status", "regenerate", "check", "append"))
    p.add_argument("--events", type=Path, default=EVENTS)
    p.add_argument("--register", type=Path, default=REGISTER)
    p.add_argument("--claims", type=Path, default=CLAIMS)
    p.add_argument("--report", type=Path, default=REPORT)
    p.add_argument("--event-json", type=Path, help="One explicit new event object to append")
    args = p.parse_args()
    registry = json.loads(args.register.read_text(encoding="utf-8"))
    claims = json.loads(args.claims.read_text(encoding="utf-8"))
    data = json.loads(args.events.read_text(encoding="utf-8"))
    result = validate(data, registry, claims)
    if args.action == "append":
        require(args.event_json is not None, "--event-json required")
        event = json.loads(args.event_json.read_text(encoding="utf-8"))
        append_event(args.events, registry, claims, event)
        print("Appended research event without rewriting historical entries", event["id"])
    elif args.action == "regenerate":
        args.report.write_text(render(data), encoding="utf-8")
        print("Generated current research checkpoint report")
    elif args.action == "check":
        require(args.report.is_file() and args.report.read_text(encoding="utf-8") == render(data),
                "research checkpoint report stale")
        print("PASS: current research checkpoint report")
    elif args.action == "status":
        print(render(data))
    else:
        print("PASS: append-only research records", result)


if __name__ == "__main__":
    main()
