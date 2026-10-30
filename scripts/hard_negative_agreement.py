#!/usr/bin/env python3
"""Measure hard-negative label agreement and Cohen's kappa."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def flatten(label):
    rows = []
    for item in label["items"]:
        for level, values in (("page", item.get("page_grades", {})),
                              ("section", item.get("section_grades", {}))):
            for key, value in values.items():
                rows.append((item["id"], level, key, int(value)))
    return rows


def kappa(pairs, weighted=False):
    if not pairs:
        return 0.0
    categories = (0, 1, 2)
    n = len(pairs)
    observed = sum(1 for a, b in pairs if a == b) / n
    counts_a = {c: sum(1 for a, _ in pairs if a == c) for c in categories}
    counts_b = {c: sum(1 for _, b in pairs if b == c) for c in categories}
    expected = sum((counts_a[c] / n) * (counts_b[c] / n)
                   for c in categories)
    if weighted:
        total = 0.0
        actual = 0.0
        for a, b in pairs:
            actual += ((a - b) ** 2) / 4.0
            for ca in categories:
                for cb in categories:
                    total += (((ca - cb) ** 2) / 4.0 *
                              (counts_a[ca] / n) * (counts_b[cb] / n))
        return 1 - (actual / n) / total if total else 0.0
    return (observed - expected) / (1 - expected) if expected != 1 else 0.0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--batch", action="append", default=[])
    args = ap.parse_args(argv)
    batches = args.batch or ["HN01", "HN02", "HN03", "HN04", "HN05", "HN06"]
    output = {}
    all_pairs = []
    for batch in batches:
        path_a = (args.root / "evaluation/hard-negatives-v5/labels" /
                  (batch + "-A.json"))
        path_b = (args.root / "evaluation/hard-negatives-v5/labels" /
                  (batch + "-B.json"))
        if not path_a.is_file() or not path_b.is_file():
            output[batch] = {"status": "missing"}
            continue
        a = {row[0:3]: row[3] for row in flatten(
            json.loads(path_a.read_text(encoding="utf-8")))}
        b = {row[0:3]: row[3] for row in flatten(
            json.loads(path_b.read_text(encoding="utf-8")))}
        keys = sorted(set(a) & set(b))
        pairs = [(a[key], b[key]) for key in keys]
        all_pairs.extend(pairs)
        output[batch] = {
            "keys": len(keys),
            "exact_agreement": round(
                sum(1 for x, y in pairs if x == y) / len(pairs), 4),
            "kappa": round(kappa(pairs), 4),
            "weighted_kappa": round(kappa(pairs, weighted=True), 4),
            "both_hard_negative": sum(1 for x, y in pairs if x == 0 and y == 0),
            "disagreements": sum(1 for x, y in pairs if x != y),
        }
    if all_pairs:
        output["all"] = {
            "keys": len(all_pairs),
            "exact_agreement": round(
                sum(1 for x, y in all_pairs if x == y) / len(all_pairs), 4),
            "kappa": round(kappa(all_pairs), 4),
            "weighted_kappa": round(kappa(all_pairs, weighted=True), 4),
            "both_hard_negative": sum(1 for x, y in all_pairs
                                     if x == 0 and y == 0),
            "disagreements": sum(1 for x, y in all_pairs if x != y),
        }
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
