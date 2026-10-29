# B16 — Vertical Scaling alternative lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; the preflight pass below depends on the
integrator applying the metadata patch and later splitting the inline card.

## Lane coordinates

- Parent HEAD: `036310e73ff4d6174e3f7e724d7d1b073aab5786`.
- Branch: `b16-vertical-scaling`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b16-vertical-scaling`.
- Scope: the inline V11/C09 `README.md` Vertical Scaling card and the V07/C06
  owner section
  `autoscaling-lag-and-capacity-limits.md#vertical-scaling` only.
- The card remains inline in the V11/C09 README. It is not split into a
  dedicated card file in this lane; the integrator owns that split.
- This is a single-entry lane; no other entry, shared owner page, promotion or
  generated file is changed.

## Source binding

- Source: `src.kubernetes`, Kubernetes documentation. The source is already in
  `sources/register.json` (`Kubernetes Concepts`, admitted-for-research).
- New public unit: Autoscaling Workloads —
  `https://kubernetes.io/docs/concepts/workloads/autoscaling/`.
- Ledger record: `read.autoscaling-workloads-vertical.2026-10-29`; sections
  read: `Autoscaling Workloads`, `Scaling workloads manually`,
  `Scaling workloads automatically`.
- Exact public quote, verbatim in the served page's rendered article text:

      When you scale a workload, you can either increase or decrease the number
      of replicas managed by the workload, or adjust the resources available to
      the replicas in-place. The first approach is referred to as horizontal
      scaling, while the second is referred to as vertical scaling.

- Revision:
  `f653ca7cce9cb752cd41e1fc2d10b335acd8033a186aa324eb499897bb7219ab`.
  The page was fetched twice on 2026-10-29; both 509,120-byte served HTML
  representations produced this canonical-text hash with
  `scripts/source_content_hash.py`. The extractor inserts spaces before
  punctuation that follows inline links; the block quote above is the rendered
  article wording.
- The quote frames horizontal scaling (changing the replica count) and vertical
  scaling (adjusting resources in place) as the two approaches. It does not say
  when either is preferable, does not compare cost or availability, and is not
  a benchmark. The availability, partition and restart conditions in the two
  book files are Tycho synthesis.
- No new source-register entry is needed. The lane does not edit the shared
  ledger, source plan or registry; the metadata patch below supplies the new
  record and the unit declarations.

## Book edits

- V07/C06 owner section `### Vertical Scaling`:
  - The final paragraph now states horizontal scaling as the competing
    alternative, carries the exact quote, and labels the page's limit: it
    defines the two approaches but does not state when horizontal scaling is
    preferable.
  - It drops the unbound "or sharding" alternative; sharding is not asserted
    by this source.
  - `evidence_scope.source_ids` adds `src.kubernetes`; `updated_at` and
    `source_inspection_date` advance to 2026-10-29.
  - The heading moves from line 120 to 121 because of the added frontmatter
    source id. The `### Autoscaling` heading moves from 137 to 147 because the
    section grows; the metadata patch recomputes every owner `line` on the page.
- V11/C09 inline card `### Vertical Scaling`:
  - **Competing alternative** now names horizontal scaling by adding replicas,
    states the page's either/or framing, and labels the availability/cost
    reversal as Tycho synthesis.
  - **Sources** adds the new record, section, revision and exact quote, and
    repeats the page's limit.
  - `content_review.reviewed_at`, `updated_at` and `source_inspection_date`
    advance to 2026-10-29. `evidence_scope.source_ids` already lists
    `src.kubernetes`, so no card source-list change is needed.
  - The card stays inline; no section is moved or split.
- Lane file hashes:
  - Card:
    `2b09de52ae167bc5f6978113eb511ea5fa1fb2e6880970fa89a6e94475a620c8`
  - Owner:
    `2374524889d8d7bf27862776bf6a0e9791b6124c2597a6d1b24b42747c338707`
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Promotion check

`edition/patterns/sufficient-promotions.v1.json` contains 28 promotions. No
promotion names `tycho.pattern.vertical-scaling`, and neither lane file hash
matches any `card_sha256` or `owner_page_sha256`. The entry remains
unpromoted and this lane adds no promotion.

## Preflight

At parent HEAD the baseline fails on the pre-existing mechanism quote
capitalization, the unbound alternative and the inline card path:

    FAIL: tycho.pattern.vertical-scaling
      - mechanism: owner quote not verbatim in owner section
      - alternative: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

The lane worktree before the integrator patch reports the same three errors.
A detached scratch worktree at parent HEAD with the two book files copied and
the metadata patch below applied runs:

    FAIL: tycho.pattern.vertical-scaling
      - card_path missing or absent
    0/1 entries preflight clean

This is the expected card-path failure: the card is inline in the V11/C09
README and `edition/patterns/card-batches.v1.json` has no `card_path` for this
entry. The preflight stops before card frontmatter checks. The integrator
should split the card after the lane and then record its path.

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145
  entries; 169 read; 140 ledger records.
- `python3 scripts/validate_pattern_registry.py` — PASS: pattern registry 145
  entries, 11 families.
- `python3 scripts/validate_pattern_cards.py` — PASS: pattern cards 11
  batch(es), 145 entries.
- `python3 scripts/check_boundary.py` — PASS: configured lexical boundary
  checks; independent-origin review still required.
- `python3 scripts/check_markdown_line_length.py` — PASS: V11 prose <=100; 145
  exact owner-link exceptions.
- `python3 scripts/validate_claim_references.py` — PASS: traceable claims,
  inventory IDs, evidence status and pinned references.
- `python3 scripts/validate_enrichment.py` — PASS: explicit membership and
  byte conservation.

`python3 scripts/validate_pattern_atlas.py` fails at `atlas-document-sha` in
the lane worktree and at `atlas-registry-hash` in the scratch tree with the
metadata patch. This is a derived-artifact refresh, not a content failure. The
lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only shared metadata; the two book
files are already in the lane commit. It reuses the admitted
`src.kubernetes` source and adds one new ledger record, one source-plan unit
and one registry unit for the vertical-scaling entry.

```python
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(".").resolve()
PATTERN = "tycho.pattern.vertical-scaling"
RECORD_ID = "read.autoscaling-workloads-vertical.2026-10-29"
SOURCE_ID = "src.kubernetes"
REVISION = "f653ca7cce9cb752cd41e1fc2d10b335acd8033a186aa324eb499897bb7219ab"
UNIT = "Autoscaling Workloads — Kubernetes documentation"
URL = "https://kubernetes.io/docs/concepts/workloads/autoscaling/"
SECTIONS = [
    "Autoscaling Workloads",
    "Scaling workloads manually",
    "Scaling workloads automatically",
]
CARD = "book/volumes/v11-pattern-atlas/c09-scalability/README.md"
OWNER = ("book/volumes/v07-performance-scale-and-resilience/"
         "c06-horizontal-vertical-scaling-and-autoscaling-delay/"
         "autoscaling-lag-and-capacity-limits.md")


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path, data):
    (ROOT / path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def squash(value):
    return " ".join(value.split())


card_text = (ROOT / CARD).read_text(encoding="utf-8")
card_lines = card_text.splitlines()
card_start = next(
    index for index, line in enumerate(card_lines)
    if line == "### Vertical Scaling"
)
card_end = next(
    index for index in range(card_start + 1, len(card_lines))
    if card_lines[index].startswith("### ")
)
card_section = "\n".join(card_lines[card_start:card_end])
match = re.search(r"\*\*Competing alternative\.\*\*\s*(.+?)(?:\n\n|\Z)",
                  card_section, re.S)
assert match, "card alternative field missing"
alternative = squash(match.group(1))

owner_text = (ROOT / OWNER).read_text(encoding="utf-8")
owner_quote = (
    "The Kubernetes autoscaling page frames the same choice as either changing "
    "the replica count (horizontal scaling) or adjusting resources in place "
    "(vertical scaling)."
)
assert squash(owner_quote) in squash(owner_text), "owner quote not verbatim"

source_quote = (
    "When you scale a workload, you can either increase or decrease the number "
    "of replicas managed by the workload, or adjust the resources available to "
    "the replicas in-place. The first approach is referred to as horizontal "
    "scaling, while the second is referred to as vertical scaling."
)

# Owner units
path = "edition/patterns/owner-units.v1.json"
units = load(path)
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
entry["technical_evidence"]["mechanism"]["quote"] = (
    "Vertical scaling changes resources available to existing replicas."
)
alt = entry["technical_evidence"]["alternative"]
alt["state"] = "supported"
alt["quote"] = owner_quote
alt["reason"] = (
    "Binds the Kubernetes Autoscaling Workloads page, which frames horizontal "
    "scaling (changing the replica count) and vertical scaling (adjusting "
    "resources in place) as the two scaling approaches. The page does not state "
    "when either is preferable; availability, partition and restart conditions "
    "remain Tycho synthesis."
)
alt["binding"] = {
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "section": "Autoscaling Workloads",
    "quote": source_quote,
    "revision": REVISION,
}
entry["decision_evidence"]["competing_alternative"] = alternative
entry["source_support"]["auxiliary"] = [{
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "revision": REVISION,
}]
entry["notes"] = (
    "Alternative bound 2026-10-29 to the Kubernetes Autoscaling Workloads "
    "page, which frames replica-count scaling and in-place resource scaling as "
    "the two approaches; all four dimensions supported, coverage "
    "partial-bounded, no promotion; availability, partition and restart "
    "conditions remain Tycho synthesis."
)

lines = owner_text.splitlines()
for item in units["entries"]:
    if item["owner"]["path"] == OWNER:
        heading = "### " + item["owner"]["heading"]
        item["owner"]["line"] = next(
            number for number, line in enumerate(lines, 1) if line == heading
        )
units["summary"]["alternative_supported"] += 1
save(path, units)

# Reading ledger
path = "edition/patterns/reading-ledger.v1.json"
ledger = load(path)
assert not any(r["id"] == RECORD_ID for r in ledger["records"])
ledger["records"].append({
    "id": RECORD_ID,
    "source_id": SOURCE_ID,
    "unit_url": URL,
    "unit_label": UNIT,
    "unit_type": "documentation-page",
    "access_date": "2026-10-29",
    "access_method": "public HTTP fetch; served text/html inspected",
    "sections_read": SECTIONS,
    "sections_not_read": [
        "linked child pages",
        "navigation and unrelated chrome",
        "examples not reproduced",
    ],
    "tables_figures": [
        "no tables or figures in the inspected sections",
    ],
    "license_notes": (
        "Public page; cite short excerpts and paraphrase; do not mirror."
    ),
    "claims_supported": [
        "Horizontal scaling changes the number of replicas, while vertical "
        "scaling adjusts resources available to replicas in place; the page "
        "presents them as the two scaling approaches."
    ],
    "claims_not_supported": [
        "selection conditions",
        "cost or availability comparison",
        "implementation behavior",
        "independent reproduction or benchmark",
    ],
    "limitations": (
        "One rolling Kubernetes documentation page; no cluster, autoscaler or "
        "benchmark was run; linked child pages were not read."
    ),
    "content_sha256": REVISION,
    "read_scope": (
        "publicly served page as returned by fetch; introduction and manual/"
        "automatic scaling sections inspected"
    ),
    "reviewer": "Automated authoring agent",
    "status": "read",
})
save(path, ledger)

# Registry
path = "edition/patterns/registry.v1.json"
registry = load(path)
pattern = next(p for p in registry["patterns"] if p["id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID and u["unit"] == UNIT
               for u in pattern["source_units"])
pattern["source_units"].append({
    "source_id": SOURCE_ID,
    "unit": UNIT,
    "status": "read",
})
save(path, registry)

# Source plan
path = "edition/patterns/source-plan.v1.json"
plan = load(path)
entry = next(e for e in plan["entries"] if e["pattern_id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID and u["unit"] == UNIT
               for u in entry["required_units"])
entry["required_units"].append({
    "source_id": SOURCE_ID,
    "unit": UNIT,
    "unit_type": "documentation-page",
    "url": URL,
    "sections": SECTIONS,
    "status": "read",
    "read_record_id": RECORD_ID,
    "blocked_reason": None,
})
plan["summary"]["required_units"] += 1
plan["summary"]["read_units"] += 1
plan["summary"]["ledger_records"] += 1
plan["registry_sha256"] = hashlib.sha256(
    (ROOT / "edition/patterns/registry.v1.json").read_bytes()
).hexdigest()
save(path, plan)
print("metadata patch applied")
```

The patch:

- sets `alternative.state` to `supported`, adds the owner quote, the binding
  to the `Autoscaling Workloads` section and the auxiliary source declaration;
- updates `decision_evidence.competing_alternative` from the Vertical Scaling
  card section, not from another card on the shared V11/C09 page;
- rewrites the entry note and increments `summary.alternative_supported` from
  62 to 63;
- corrects the existing mechanism quote's first letter to `Vertical`, making
  it verbatim in the owner section; the sentence and its binding are unchanged;
- updates the `owner.line` fields for all three entries on the shared owner
  page (Horizontal Scaling 104, Vertical Scaling 121, Autoscaling 147);
- adds the new ledger record, registry source unit and source-plan unit, and
  increments `required_units` 169→170, `read_units` 168→169 and
  `ledger_records` 139→140;
- recomputes `registry_sha256`;
- leaves `technical_coverage` and `decision_coverage` at
  `partial-bounded`, `review_state` at `self-checked`, and promotion and
  owner acceptance unchanged.

## Remaining metadata and review needs

- Refresh derived artifacts after applying the patch: atlas manifest,
  inventory, content revisions, page census, route index, coverage/reverse maps,
  semantic audit, candidate and review packets, delivery evidence and search
  indexes. The lane intentionally does not touch them.
- Split the inline card as planned and add its `card_path` to
  `edition/patterns/card-batches.v1.json`; until then preflight reports the
  expected `card_path missing or absent` failure. The new card should keep
  `src.kubernetes` in `evidence_scope.source_ids`.
- The owner page `content_review` remains the pre-existing decomposition-era
  `draft` with null reviewer fields; this lane updates only `updated_at` and
  `source_inspection_date`. No content acceptance is asserted.
- Request a fresh external review under the book/atlas gate. The historical
  phase-B findings B4-023 and B4-024 are prior observations, not reviews of this
  text; this lane is self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime cluster, autoscaler, resize or failure test was executed.

## Limits

The binding covers one rolling Kubernetes documentation page at the
2026-10-29 revision. The page defines horizontal and vertical scaling as the two
approaches, but it does not state when horizontal scaling is preferable, does
not compare cost or availability, and supplies no benchmark. The partition,
failure-domain, restart and cost reversal conditions remain Tycho synthesis;
sharding is no longer asserted by the alternative. The rendered quote and the
canonical-text hash differ only by extractor spaces at inline-link boundaries.
Coverage remains `partial-bounded`.
