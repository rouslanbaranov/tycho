#!/usr/bin/env python3
"""Preflight a pattern before external review.

Checks quote verbatimness, bindings, source declarations, card/owner agreement and
review dates. It does not replace review, tests or owner acceptance.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMS = ("mechanism", "invariant", "failure_recovery", "alternative")


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def owner_section(entry):
    lines = (ROOT / entry["owner"]["path"]).read_text(encoding="utf-8").splitlines()
    heading = entry["owner"]["heading"]
    start = None
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") and line.lstrip().lstrip("#").strip() == heading:
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^#{1,3} ", lines[i]):
            end = i
            break
    return "\n".join(lines[start:end])


def card_path(entry, cards):
    for batch in cards.get("batches", []):
        for item in batch.get("entries", []):
            if item.get("pattern_id") == entry["pattern_id"]:
                return item.get("card_path")
    return None


def frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    import yaml
    return yaml.safe_load(text[4:end]) or {}


def check(entry, cards, registry, ledger, sources):
    errors = []
    pid = entry["pattern_id"]
    tech = entry.get("technical_evidence", {})
    section = owner_section(entry)
    if section is None:
        return ["owner section not found"]
    section_n = norm(section)
    ledger_map = {}
    for item in ledger.get("records", ledger.get("entries", [])):
        rid = item.get("id") or item.get("record_id")
        if rid:
            ledger_map[rid] = item
    ledger_ids = set(ledger_map)
    source_ids = set()
    for item in sources.get("sources", sources.get("entries", [])):
        sid = item.get("id") or item.get("source_id")
        if sid:
            source_ids.add(sid)
    registry_sources = set()
    for item in registry.get("patterns", registry.get("entries", [])):
        if item.get("id") == pid:
            for unit in item.get("source_units", []):
                registry_sources.add(unit.get("source_id"))
    binding_sources = set()
    support = entry.get("source_support") or {}
    support_sources = {support.get("source_id")} if isinstance(support, dict) else set()
    if isinstance(support, dict):
        for aux in support.get("auxiliary", []) or []:
            support_sources.add(aux.get("source_id"))
    elif isinstance(support, list):
        support_sources = {x.get("source_id") for x in support if isinstance(x, dict)}
    for dim in DIMS:
        row = tech.get(dim, {})
        if row.get("state") != "supported":
            errors.append(f"{dim}: state {row.get('state')!r}, not supported")
            continue
        quote = row.get("quote", "")
        if not quote or norm(quote) not in section_n:
            errors.append(f"{dim}: owner quote not verbatim in owner section")
        binding = row.get("binding", {})
        for key in ("source_id", "ledger_record", "section", "quote", "revision"):
            if not binding.get(key):
                errors.append(f"{dim}: binding missing {key}")
        record = ledger_map.get(binding.get("ledger_record"))
        if binding.get("ledger_record") and record is None:
            errors.append(f"{dim}: ledger record {binding['ledger_record']} absent")
        if record:
            if record.get("source_id") != binding.get("source_id"):
                errors.append(f"{dim}: ledger source_id mismatch")
            if binding.get("section") and binding["section"] not in (record.get("sections_read") or []):
                errors.append(f"{dim}: section not in ledger sections_read")
            if binding.get("revision") and binding["revision"] != record.get("content_sha256"):
                errors.append(f"{dim}: revision differs from ledger content_sha256")
        if binding.get("source_id"):
            binding_sources.add(binding["source_id"])
            if binding["source_id"] not in support_sources:
                errors.append(f"{dim}: source {binding['source_id']} absent from source_support")
            if binding["source_id"] not in source_ids:
                errors.append(f"{dim}: source {binding['source_id']} absent from register")
            if binding["source_id"] not in registry_sources:
                errors.append(f"{dim}: source {binding['source_id']} absent from registry units")
        if binding.get("revision") and not re.fullmatch(r"[0-9a-f]{64}", binding["revision"]):
            errors.append(f"{dim}: revision is not sha256")
    cp = card_path(entry, cards)
    if not cp or not (ROOT / cp).is_file():
        errors.append("card_path missing or absent")
        return errors
    text = (ROOT / cp).read_text(encoding="utf-8")
    meta = frontmatter(text)
    declared = set((meta.get("evidence_scope") or {}).get("source_ids") or [])
    for sid in sorted(binding_sources - declared):
        errors.append(f"card evidence_scope.source_ids missing {sid}")
    review = meta.get("content_review") or {}
    reviewed = str(review.get("reviewed_at") or "")
    updated = str(meta.get("updated_at") or "")
    inspected = str(meta.get("source_inspection_date") or "")
    if inspected and reviewed and reviewed < inspected:
        errors.append("content_review.reviewed_at predates source_inspection_date")
    if inspected and updated and updated < inspected:
        errors.append("updated_at predates source_inspection_date")
    questions = (meta.get("route_hints") or {}).get("questions") or []
    if not questions or not all(str(q).strip().endswith("?") for q in questions):
        errors.append("route_hints.questions missing or not a full question")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pattern", action="append", default=[])
    ap.add_argument("--all-supported", action="store_true")
    args = ap.parse_args()
    units = load("edition/patterns/owner-units.v1.json")
    cards = load("edition/patterns/card-batches.v1.json")
    registry = load("edition/patterns/registry.v1.json")
    ledger = load("edition/patterns/reading-ledger.v1.json")
    sources = load("sources/register.json")
    selected = [e for e in units["entries"] if e["pattern_id"] in args.pattern]
    if args.all_supported:
        selected = [
            e for e in units["entries"]
            if e.get("technical_coverage") != "sufficient"
            and all(e.get("technical_evidence", {}).get(d, {}).get("state") == "supported"
                   for d in DIMS)
        ]
    if not selected:
        print("FAIL: no matching entries", file=sys.stderr)
        return 1
    failed = 0
    for entry in selected:
        errors = check(entry, cards, registry, ledger, sources)
        if errors:
            failed += 1
            print("FAIL:", entry["pattern_id"])
            for err in errors:
                print("  -", err)
        else:
            print("PASS:", entry["pattern_id"])
    print(f"{len(selected) - failed}/{len(selected)} entries preflight clean")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
