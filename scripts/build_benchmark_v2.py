#!/usr/bin/env python3
"""Build benchmark v2: core/optional claims, rubric and dev/holdout split."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERIC = {
    "purpose and mission", "entry inventory", "overview",
    "decision and worked result", "integrated decision and reading route",
    "bounded pattern ownership notes", "engineering walkthrough",
    "purpose", "scope", "summary",
}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args(argv)
    root = args.root
    old = json.loads((root / "evaluation/agent-benchmark/corpus.json").read_text())
    items = []
    for q in old["questions"]:
        points = [p for p in q.get("expected_answer_points", []) if p]
        specific = [p for p in points if p.strip().casefold() not in GENERIC]
        core = specific[:4] or points[:2]
        optional = [p for p in points if p not in core]
        split = "dev" if int(q["id"][1:]) % 2 == 0 else "holdout"
        item = dict(q)
        item["core_claims"] = core
        item["optional_claims"] = optional
        item["split"] = split
        item["rubric"] = {
            "core_support": 0.45,
            "core_coverage": 0.35,
            "citation_validity": 0.20,
            "optional_coverage": "reported-not-gating",
        }
        item["required_evidence"] = list(q.get("required_evidence", []))
        items.append(item)
    out = {
        "status": "ai-benchmark-corpus-v2-not-human",
        "version": "v2",
        "source": "corpus.json",
        "questions": items,
        "limits": ("Core claims are a heuristic de-genericized subset of the "
                   "existing heading-derived points; holdout is deterministic. "
                   "This is not a semantic gold answer key."),
    }
    (root / "evaluation/agent-benchmark/corpus-v2.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n")
    counts = {}
    for item in items:
        counts[(item["split"], item["layer_expected"])] = (
            counts.get((item["split"], item["layer_expected"]), 0) + 1)
    print(json.dumps({str(k): v for k, v in sorted(counts.items())}, indent=2))
    print("dev", sum(x["split"] == "dev" for x in items),
          "holdout", sum(x["split"] == "holdout" for x in items))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
