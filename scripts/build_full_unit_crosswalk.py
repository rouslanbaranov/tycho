#!/usr/bin/env python3
"""Build a 155-unit crosswalk against the #225 audit readings."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "edition/patterns/source-plan.v1.json"
OUT = ROOT / "edition/patterns/full-unit-reading-plan.v1.json"
AUDIT = ROOT / "research/source-audit-225"


def norm(value):
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def tokens(value):
    return {t for t in re.findall(r"[a-z0-9]+", (value or "").lower()) if len(t) > 2}


def main():
    plan = json.loads(PLAN.read_text())
    units = [(entry["pattern_id"], entry["catalog_name"], unit)
             for entry in plan["entries"] for unit in entry["required_units"]]
    readings = json.loads((AUDIT / "readings.json").read_text())["readings"]
    source_units = json.loads((AUDIT / "source-units.json").read_text())["sources"]
    by_url = {}
    for reading in readings:
        by_url.setdefault(norm(reading.get("url")), []).append(reading)
    for source in source_units:
        for unit in source.get("units", []):
            if unit.get("url"):
                by_url.setdefault(norm(unit["url"]), []).append({
                    "id": unit.get("record") or unit.get("id"),
                    "source_ids": [source["source_id"]],
                    "url": unit["url"],
                    "unit": unit.get("unit", ""),
                    "status": "full-scoped-text-read" if unit.get("status") == "read" else unit.get("status"),
                    "coverage": unit.get("unit", ""),
                    "revision": "source-units record",
                })
    rows = []
    for pattern_id, catalog_name, unit in units:
        if unit.get("status") == "blocked":
            rows.append({"pattern_id": pattern_id, "catalog_name": catalog_name,
                         "source_id": unit["source_id"], "unit": unit["unit"],
                         "url": unit.get("url"), "sections": unit.get("sections", []),
                         "current_status": unit.get("status"), "match_225": None,
                         "disposition": "blocked-current"})
            continue
        url_matches = [r for r in readings if norm(unit.get("url")) == norm(r.get("url"))]
        source_matches = [r for r in readings if unit["source_id"] in r.get("source_ids", [])]
        candidates = list(url_matches)
        for item in by_url.get(norm(unit.get("url")), []):
            if item not in candidates:
                candidates.append(item)
        exact_url = bool(candidates)
        if not candidates:
            if source_matches:
                best = max(source_matches, key=lambda x: len((x.get("unit", "") + " " + x.get("coverage", "")).lower()))
                match = {"id": best.get("id"), "source_ids": best.get("source_ids", []),
                         "url": best.get("url"), "unit": best.get("unit"),
                         "status": best.get("status"), "revision": best.get("revision", "")}
                disposition = "reread-scope"
            else:
                disposition = "reread-no-225"
                match = None
        else:
            sections = [norm(s) for s in unit.get("sections", [])]
            def score(item):
                text = norm(item.get("unit", "") + " " + item.get("coverage", ""))
                return sum(1 for s in sections if s and s in text)
            best = max(candidates, key=score)
            match = {"id": best.get("id"), "source_ids": best.get("source_ids", []),
                     "url": best.get("url"), "unit": best.get("unit"),
                     "status": best.get("status"), "revision": best.get("revision", "")}
            if best.get("status") == "blocked-full-text":
                disposition = "blocked"
            elif best.get("status") == "excluded-from-scope":
                disposition = "reread-no-225"
            elif best.get("status") == "partial-scoped-text-read":
                disposition = "reread-partial"
            elif score(best) == len([s for s in sections if s]):
                disposition = "reuse-scope-check"
            else:
                disposition = "reread-scope"
        rows.append({
            "pattern_id": pattern_id, "catalog_name": catalog_name,
            "source_id": unit["source_id"], "unit": unit["unit"],
            "url": unit.get("url"), "sections": unit.get("sections", []),
            "current_status": unit.get("status"), "match_225": match,
            "disposition": disposition,
        })
    counts = {}
    for row in rows:
        counts[row["disposition"]] = counts.get(row["disposition"], 0) + 1
    data = {"schema_version": 1, "issue": 535, "date": "2026-10-26",
            "units": len(rows), "dispositions": counts, "entries": rows}
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(len(rows), counts)


if __name__ == "__main__":
    main()
