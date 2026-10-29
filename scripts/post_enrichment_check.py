#!/usr/bin/env python3
"""Run the read-only post-enrichment validation sequence.

This is a diagnostic gate, not owner acceptance, CI or a quality threshold.
"""
import argparse
import json
from pathlib import Path
import sys

import search_reindex

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "edition/patterns/search-pre-enrichment.v1.json"


def run(root, manifest=MANIFEST, regression=False):
    report = {"quality_claims": "suspended-until-revalidation"}
    try:
        report["check"] = search_reindex.check(root, manifest)
    except (OSError, ValueError, RuntimeError) as exc:
        report["check"] = {"status": "error", "error": str(exc)}
    try:
        report["diff"] = search_reindex.diff_current(root, manifest)
    except (OSError, ValueError, RuntimeError) as exc:
        report["diff"] = {"status": "error", "error": str(exc)}
    try:
        report["verify"] = search_reindex.verify(root, manifest)
    except (OSError, ValueError, RuntimeError) as exc:
        report["verify"] = {"status": "error", "error": str(exc)}
    if regression:
        try:
            import search_regression
            report["regression"] = search_regression.run(root)
        except (OSError, ValueError, RuntimeError) as exc:
            report["regression"] = {"status": "error", "error": str(exc)}
    report["status"] = ("verified" if report.get("verify", {}).get("status")
                        == "verified" else "failed")
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--manifest", type=Path, default=MANIFEST)
    ap.add_argument("--regression", action="store_true")
    args = ap.parse_args(argv)
    report = run(args.root, args.manifest, args.regression)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "verified" else 1


if __name__ == "__main__":
    sys.exit(main())
