#!/usr/bin/env python3
"""Generate a bounded top-1 miss packet for owner adjudication.

This script does not adjudicate or claim human review.
"""
import argparse
import json
from pathlib import Path
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "authoring/TOP1-ADJUDICATION-PACKET-2026-10-29.md"
SOURCES = (
    ("v2", "evaluation/corpus-qrels.v2.json", 12),
    ("p3", "evaluation/agent-qrels.phase3.json", 4),
    ("v12", "evaluation/v12-simulation-qrels.v1.json", 4),
)


def wrap(value, width=84):
    return textwrap.fill(str(value), width=width,
                         break_long_words=True,
                         break_on_hyphens=True)


def accepted_rank(results, accepted):
    for rank, result in enumerate(results, 1):
        if ((result["path"], result["section_id"]) in accepted
                or (result["path"], None) in accepted):
            return rank
    return None


def collect(root):
    import section_search
    packet = []
    for split, relative, wanted in SOURCES:
        data = json.loads((Path(root) / relative).read_text(encoding="utf-8"))
        rows = []
        for item in data.get("items", []):
            if split == "p3" and item.get("final_label") != "answerable":
                continue
            if item.get("category") == "unanswerable":
                continue
            results = section_search.search(
                root, item["question"], limit=5, abstain=False).get(
                    "results", [])
            accepted = {(a["path"], a.get("section_id"))
                        for a in item.get("accepted", [])}
            rank = accepted_rank(results, accepted)
            if rank == 1:
                continue
            rows.append((item, results, accepted, rank))
        packet.extend((split, row) for row in rows[:wanted])
    return packet


def render(packet):
    lines = [
        "# Top-1 adjudication packet — 2026-10-29",
        "",
        "Status: **review pending**. No adjudication has been performed.",
        "",
        "For each item, mark whether the BM25 top-1 is a defensible answer",
        "even if it is absent from the original accepted set.",
        "",
        "- valid: top-1 is a correct and useful answer;",
        "- invalid: top-1 is wrong;",
        "- uncertain: needs source reading.",
        "",
    ]
    for split, (item, results, accepted, rank) in packet:
        top = results[0]
        lines += [
            "## " + split + " " + item["id"],
            "",
            "Query:",
            "",
            wrap(item["question"]),
            "",
            "- Top-1: " + wrap("%s#%s" % (top["path"],
                                         top["section_id"])),
            "- Heading: " + wrap(top.get("heading", "")),
            "- BM25 score: " + str(top.get("score")),
            "- Accepted rank: " + (str(rank) if rank else "not in top-5"),
            "- Accepted pages:",
        ]
        for path, section in sorted(accepted):
            lines.append("  - " + wrap("%s#%s" % (path, section or "")))
        lines += [
            "- Verdict: [ ] valid  [ ] invalid  [ ] uncertain",
            "- Notes:",
            "",
        ]
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args(argv)
    packet = collect(args.root)
    args.output.write_text(render(packet), encoding="utf-8")
    print("wrote", len(packet), "items to", args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
