#!/usr/bin/env python3
"""Validate V12 structural, provenance, calibration and iron-rule gates.

This validator is read-only. It checks schemas, unique identifiers, referential
integrity, stored hashes, the derived reverse index and the protected baseline.
It does not fetch sources, execute simulations, review prose or claim independent
review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
V12 = Path("edition/v12")
SCHEMAS = Path("schemas/v12")
BOOK = Path("book/volumes/v12-modeling-simulation-and-decision-validation")
PATTERN_ID = re.compile(r"^tycho\.pattern\.[a-z0-9]+(?:-[a-z0-9]+)*$")
V12_REFERENCE = re.compile(r"(?:book/volumes/v12-|tycho\.(?:model|scenario|run)\.[a-z0-9-]+|tycho\.decision\.v12-)")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_json(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode()).hexdigest()


def schema_check(data, schema_path: Path, label: str) -> None:
    from jsonschema import Draft202012Validator
    schema = load(schema_path)
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(data),
                    key=lambda error: (list(map(str, error.path)), error.message))
    if errors:
        first = errors[0]
        path = "/".join(map(str, first.path)) or "(root)"
        raise ValueError(label + ": " + path + ": " + first.message)


def protected_check() -> dict:
    baseline = load(V12 / "protected-baseline.json")
    changed, missing = [], []
    for path, digest in baseline["book_pages"].items():
        target = ROOT / path
        if not target.is_file():
            missing.append(path)
        elif sha(target) != digest:
            changed.append(path)
    if missing:
        raise ValueError("protected baseline page missing: " + missing[0])
    if changed:
        raise ValueError("protected baseline page changed: " + changed[0])
    for path, digest in baseline["promotion_records"].items():
        require((ROOT / path).is_file(), "promotion record missing: " + path)
        require(sha(ROOT / path) == digest, "promotion record changed: " + path)
    leaked = []
    for path in baseline["book_pages"]:
        text = (ROOT / path).read_text(encoding="utf-8")
        if V12_REFERENCE.search(text):
            leaked.append(path)
    if leaked:
        raise ValueError("iron-rule violation: protected page references V12: " + leaked[0])
    return {"protected_pages": len(baseline["book_pages"]),
            "promotion_records": len(baseline["promotion_records"]),
            "changed": len(changed), "missing": len(missing), "leaked": len(leaked)}


def validate(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    manifest = load(root / V12 / "manifest.json")
    registry = load(root / V12 / "registry.json")
    ledger = load(root / V12 / "reading-ledger.v1.json")
    v12_index = load(root / "generated/v12-index.v1.json")
    reverse_file = load(root / V12 / "reverse-index.v1.json")
    plan = load(root / V12 / "source-plan.v1.json")
    route = load(root / "generated/route-index.v1.json")
    sources = {item["id"] for item in load(root / "sources/register.json")["sources"]}
    patterns = {item["id"]: item for item in load(root / "edition/patterns/registry.v1.json")["patterns"]}
    index = {item["id"]: item for item in route["documents"]}

    schema_check(manifest, root / SCHEMAS / "manifest.v1.schema.json", "manifest")
    schema_check(registry, root / SCHEMAS / "registry.v1.schema.json", "registry")
    schema_check(ledger, root / SCHEMAS / "reading-ledger.v1.schema.json", "ledger")
    schema_check(plan, root / SCHEMAS / "source-plan.v1.schema.json", "source-plan")

    # Manifest documents and hashes.
    documents = manifest["documents"]
    require(len({d["id"] for d in documents}) == len(documents), "manifest duplicate id")
    require(len({d["path"] for d in documents}) == len(documents), "manifest duplicate path")
    for document in documents:
        target = root / document["path"]
        require(target.is_file(), "manifest missing page: " + document["path"])
        require(sha(target) == document["sha256"], "manifest hash drift: " + document["path"])
        require(document["id"] in index, "manifest id missing from route index: " + document["id"])
        require(index[document["id"]]["path"] == document["path"], "manifest path mismatch")
    v12_route = {item["id"]: item for item in route["documents"]
                 if item["path"].startswith(str(BOOK) + "/")}
    require(set(v12_route) == {d["id"] for d in documents}, "route index V12 membership")
    require(len(manifest["chapters"]) == 7, "manifest chapter count")
    for chapter in manifest["chapters"]:
        require(chapter["id"] in index and index[chapter["id"]]["kind"] == "chapter",
                "manifest chapter kind")
        require(sha(root / chapter["path"]) == chapter["sha256"], "chapter hash drift")

    # Artifact schemas, hashes and references.
    artifacts = registry["artifacts"]
    models = {a["id"]: a for a in artifacts["models"]}
    scenarios = {a["id"]: a for a in artifacts["scenarios"]}
    runs = {a["id"]: a for a in artifacts["runs"]}
    decisions = {a["id"]: a for a in artifacts["decisions"]}
    for collection in ("models", "scenarios", "runs", "decisions"):
        require(len({a["id"] for a in artifacts[collection]}) == len(artifacts[collection]),
                "duplicate registry id in " + collection)
    for artifact in artifacts["models"]:
        data = load(root / artifact["path"])
        schema_check(data, root / SCHEMAS / "model-specification.v1.schema.json", "model " + artifact["id"])
        require(sha(root / artifact["path"]) == artifact["sha256"], "model hash drift")
        for parameter in data["parameters"]:
            if parameter["evidence_status"] == "measured":
                require(parameter["source_ids"], "measured parameter without source: " + parameter["name"])
                require(parameter.get("measurement"), "measured parameter without measurement: " + parameter["name"])
        for source_id in {s for p in data["parameters"] for s in p["source_ids"]}:
            require(source_id in sources, "model unknown source: " + source_id)
    for artifact in artifacts["scenarios"]:
        data = load(root / artifact["path"])
        schema_check(data, root / SCHEMAS / "scenario-specification.v1.schema.json", "scenario " + artifact["id"])
        require(sha(root / artifact["path"]) == artifact["sha256"], "scenario hash drift")
        require(data["model_id"] == artifact["model_id"] and data["model_id"] in models,
                "scenario model reference")
    for artifact in artifacts["runs"]:
        data = load(root / artifact["path"])
        schema_check(data, root / SCHEMAS / "run-result.v1.schema.json", "run " + artifact["id"])
        require(sha(root / artifact["path"]) == artifact["sha256"], "run hash drift")
        require(data["model_id"] in models and data["scenario_id"] in scenarios, "run reference")
        require(data["provenance"]["model_sha256"] == sha(root / models[data["model_id"]]["path"]),
                "run model hash mismatch: " + artifact["id"])
        require(data["provenance"]["scenario_sha256"] == sha(root / scenarios[data["scenario_id"]]["path"]),
                "run scenario hash mismatch: " + artifact["id"])
        body = {k: v for k, v in data.items() if k != "result_sha256"}
        require(data["result_sha256"] == sha_json(body), "run result hash mismatch: " + artifact["id"])
        require(data["invariants"]["conservation_ok"] is True,
                "run invariant failed: " + artifact["id"])
        require(all(check["status"] == "pass" for check in data["invariants"]["checks"]),
                "run invariant check failed: " + artifact["id"])
        require(data["provenance"]["engine_sha256"] == sha(root / "scripts/v12_engine.py"),
                "run engine hash mismatch: " + artifact["id"])
        for metric in data["metrics"].values():
            require(metric["ci_low"] <= metric["ci_high"], "run metric interval order")
    for artifact in artifacts["decisions"]:
        data = load(root / artifact["path"])
        schema_check(data, root / SCHEMAS / "decision-record.v1.schema.json", "decision " + artifact["id"])
        require(sha(root / artifact["path"]) == artifact["sha256"], "decision hash drift")
        for candidate in data["candidates"]:
            require(candidate["scenario_id"] in scenarios, "decision scenario reference")
            require(all(run_id in runs for run_id in candidate["run_ids"]), "decision run reference")
            for pattern_id in candidate["pattern_ids"]:
                require(pattern_id in patterns, "decision unknown pattern: " + pattern_id)
            for page in candidate["owner_pages"]:
                require((root / page).is_file(), "decision owner page missing: " + page)
        constraint_ids = {item["id"] for item in data["constraints"]}
        evaluation_ids = {item["constraint_id"] for item in data["constraint_evaluation"]}
        require(constraint_ids == evaluation_ids, "decision constraint evaluation mismatch")
        for link in data["pattern_links"]:
            require(link["pattern_id"] in patterns, "decision link unknown pattern")
            require(link["owner_document_id"] in index, "decision link unknown owner id")
            require((root / link["owner_page"]).is_file(), "decision link owner page missing")

    # Derived reverse index must match the artifacts exactly.
    expected = {}
    for artifact_type, collection in (("model", artifacts["models"]), ("scenario", artifacts["scenarios"]),
                                      ("run", artifacts["runs"]), ("decision", artifacts["decisions"])):
        for artifact in collection:
            for pattern_id in artifact["pattern_ids"]:
                expected.setdefault(pattern_id, []).append(
                    {"artifact_type": artifact_type, "id": artifact["id"], "path": artifact["path"]})
    for value in expected.values():
        value.sort(key=lambda item: (item["artifact_type"], item["id"]))
    actual = {key: sorted(value, key=lambda item: (item["artifact_type"], item["id"]))
              for key, value in registry["reverse_index"].items()}
    require(expected == actual, "reverse index is not derived from artifacts")

    # Source ledger and plan.
    records = {record["id"]: record for record in ledger["records"]}
    require(len(records) == len(ledger["records"]), "duplicate ledger record")
    for record in ledger["records"]:
        require(record["source_id"] in sources, "ledger unknown source: " + record["source_id"])
        require(record["representation_sha256"] == record["representation_sha256"].lower(),
                "ledger hash format")
    for entry in plan["entries"]:
        for unit in entry["required_units"]:
            require(unit["source_id"] in sources, "source plan unknown source")
            if unit["status"] == "read":
                require(unit["read_record_id"] in records, "source plan missing ledger record")
                require(records[unit["read_record_id"]]["source_id"] == unit["source_id"],
                        "source plan record source mismatch")
            for page in unit["used_by"]:
                require((root / page).is_file(), "source plan page missing: " + page)
                page_meta = index.get(next((d["id"] for d in route["documents"]
                                            if d["path"] == page), ""), None)
                require(page_meta is not None, "source plan page not in route index")
    require(plan["summary"]["topics"] == len(plan["entries"]), "source plan topic count")
    require(plan["summary"]["required_units"] == sum(len(e["required_units"]) for e in plan["entries"]),
            "source plan unit count")

    # Derived V12 search namespace and reverse lookup.
    require(v12_index["volume"] == "v12", "v12 index volume")
    require(reverse_file["patterns"] == registry["reverse_index"], "standalone reverse index drift")
    expected_docs = len(documents) + len(models) + len(scenarios) + len(runs) + len(decisions)
    require(len(v12_index["documents"]) == expected_docs, "v12 index document count")
    for document in v12_index["documents"]:
        require(document["volume"] == "v12", "v12 index facet volume")
        require(document["artifact_type"] in {"document", "model", "scenario", "run", "decision"},
                "v12 index artifact type")
        if document["artifact_type"] == "document":
            require(document["path"].startswith(str(BOOK) + "/"), "v12 index book scope")
        else:
            require(document["path"].startswith("edition/v12/"), "v12 index artifact scope")
    require(set(v12_index["pattern_catalog"]) <= set(patterns), "v12 index pattern catalog")
    long_lines = []
    for document in documents:
        for number, line in enumerate((root / document["path"]).read_text(encoding="utf-8").splitlines(), 1):
            if len(line) > 100 and not line.startswith("canonical_path:"):
                long_lines.append((document["path"], number, len(line)))
    if long_lines:
        raise ValueError("V12 markdown line over 100 characters: " + long_lines[0][0]
                         + ":" + str(long_lines[0][1]))

    protected = protected_check()
    return {
        "documents": len(documents),
        "chapters": len(manifest["chapters"]),
        "models": len(models),
        "scenarios": len(scenarios),
        "runs": len(runs),
        "decisions": len(decisions),
        "reverse_patterns": len(actual),
        "v12_index_documents": len(v12_index["documents"]),
        "source_records": len(records),
        "source_plan_units": plan["summary"]["required_units"],
        "long_body_lines": 0,
        "protected": protected,
        "scope": "structure, hashes, references, reverse index and iron rule; not independent review or production validity",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print("FAIL:", error, file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("PASS: V12 structure, hashes, reverse index and iron rule")
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
