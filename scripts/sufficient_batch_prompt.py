#!/usr/bin/env python3
"""Render an exact external-review prompt for one sufficient batch."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PLAN = Path("research/sufficient-pilot-540/batch-plan.json")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build_prompt(root=ROOT, batch_id="B01"):
    root = Path(root).resolve()
    plan = load(root / PLAN)
    batch = next((item for item in plan["batches"]
                  if item["id"] == batch_id), None)
    if batch is None:
        raise ValueError("unknown batch: " + batch_id)
    entries = "\n".join(
        "%d. %s (`%s`)" % (index, item["catalog_name"], item["pattern_id"])
        for index, item in enumerate(batch["entries"], 1))
    return f"""You are an independent AI reviewer from a different vendor and harness than the
DeepSeek Harness authoring agent. Review one bounded Tycho pattern batch for promotion
from sufficient-ready to sufficient. Work read-only; do not edit, commit, open a PR or
change configuration.

Repository: {root}
Checkout: current branch HEAD; record `git rev-parse HEAD`.
Batch: {batch_id} ({batch['family']})
Policy: governance/SUFFICIENT-COVERAGE.md
Plan: research/sufficient-pilot-540/batch-plan.json
Manifest: research/sufficient-pilot-540/manifest.json
Owner units: edition/patterns/owner-units.v1.json
Registry: edition/patterns/registry.v1.json
Source plan: edition/patterns/source-plan.v1.json
Ledger: edition/patterns/reading-ledger.v1.json

Entries in this batch:
{entries}

Do not accept sufficient-ready as evidence. For each entry, apply the policy and decide
technical sufficiency and decision sufficiency independently. Read the owner heading and
card section, verify the source-plan unit and ledger record, and check that synthetic
limits are not presented as source support. Use public sources only.

Return one Markdown report with: reviewer harness/vendor, model/version, session id,
timestamp, repository path, review HEAD, batch id, per-entry table (technical
pass/PWF/reject, decision pass/PWF/reject), findings by severity with exact paths and
evidence, synthetic-only claims, limits, and `ai_review: performed` only if the checks
ran. State `sufficient: 0` until a separate promotion commit exists. Do not claim owner
acceptance, CI or merge permission.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", default="B01")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(build_prompt(args.root, args.batch))
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
