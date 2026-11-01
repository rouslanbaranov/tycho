#!/usr/bin/env python3
"""Derived guards for atlas card, owner-path and promotion state."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check(root=ROOT):
    root = Path(root)
    registry = load("edition/patterns/registry.v1.json")["patterns"]
    owner = {e["pattern_id"]: e for e in load("edition/patterns/owner-units.v1.json")["entries"]}
    batches = load("edition/patterns/card-batches.v1.json")
    cards = {e["pattern_id"]: e.get("card_path") for b in batches["batches"] for e in b["entries"]}
    promotions = {p["pattern_id"] for p in load("edition/patterns/sufficient-promotions.v1.json")["promotions"]}
    manifest = load("edition/atlas-manifest.json")["documents"]
    errors = []
    ids = {p["id"] for p in registry}
    if set(owner) != ids:
        errors.append("owner-units pattern ids differ from registry")
    if set(cards) != ids:
        errors.append("card-batches pattern ids differ from registry")
    for pid, e in owner.items():
        path = e["owner"]["path"]
        if not path.startswith("book/volumes/"):
            errors.append(f"owner path outside volumes: {pid}: {path}")
        if not (root / path).is_file():
            errors.append(f"owner page missing: {pid}: {path}")
    manifest_paths = {d["path"] for d in manifest}
    for pid, card in cards.items():
        if not card:
            continue
        if not (root / card).is_file():
            errors.append(f"card missing: {pid}: {card}")
        if card not in manifest_paths:
            errors.append(f"card not in atlas manifest: {pid}: {card}")
    promoted_without_card = [p for p in promotions if not cards.get(p)]
    if promoted_without_card:
        errors.append("promoted without card: " + ", ".join(sorted(promoted_without_card)))
    card_paths = [c for c in cards.values() if c]
    if len(card_paths) != len(set(card_paths)):
        errors.append("duplicate card_path values")
    return {
        "registry": len(registry),
        "cards": len(card_paths),
        "cardless": len(registry) - len(card_paths),
        "promotions": len(promotions),
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    result = check(args.root)
    print(json.dumps(result, indent=2))
    if result["errors"]:
        for error in result["errors"]:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print(f"PASS: atlas integrity: {result['cards']}/{result['registry']} cards, "
          f"{result['cardless']} cardless, {result['promotions']} promotions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
