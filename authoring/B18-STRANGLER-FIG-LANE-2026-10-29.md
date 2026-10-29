# B18 — Strangler Fig failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; preflight still fails on the inline card path
until the integrator applies the metadata patch and splits the card.

## Lane coordinates

- Parent HEAD: `79d7eb1299f017ac7111a07d640d1d57f76fe14a` (`79d7eb12`).
- Branch: `b18-strangler`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b18-strangler`.
- Scope: the inline V11/C10 `README.md` Strangler Fig card and the V10/C05
  owner section
  `target-and-transition-architecture-states.md#strangler-fig` only.
- The card remains inline in the V11/C10 README. It is not split in this lane;
  the integrator owns that split.
- This is a single-entry lane; no other entry, shared owner page, promotion or
  generated file is changed.

## Source binding

- Source: `src.aws-strangler`, AWS Prescriptive Guidance, *Strangler fig
  pattern*. The page was not previously registered; the metadata patch adds the
  source, one ledger record, one source-plan unit and one registry unit.
- Unit: Strangler fig pattern — AWS Prescriptive Guidance; the exact public URL
  is in the metadata patch's `URL` value and in the ledger record.
- New ledger record: `read.aws-strangler.2026-10-29`; sections read:
  `Strangler fig pattern`, `Transform`, `Coexist`, `Eliminate`,
  `Advantages and disadvantages`.
- Exact public quote, verbatim in the served page's extracted article text:

      Cannot be used in systems where requests to the backend system cannot be
      intercepted and routed. The proxy or facade layer can become a single
      point of failure or a performance bottleneck if it isn't designed
      properly. Requires a rollback plan for each refactored service to revert
      to the old way of doing things quickly and safely if things go wrong.

- Revision:
  `787962ad56fbc52feb9e3198749ceb7e3b9cea44bca6f9c2bb50530e30c66044`.
  The page was fetched twice on 2026-10-29; both responses were 17,551 bytes with
  raw-HTML SHA-256
  `23643ba61a0797a8d0c3b02205f85aa2e23bbe714effef2a35845b04d1b64919`, and
  both canonical article-text hashes were the revision above, computed with
  `scripts/source_content_hash.py`. The canonical text is 4,174 characters /
  664 words; the digest covers title and navigation chrome because AWS markup
  has no recognized article-body marker.
- The quote is from the page's advantages/disadvantages table. It states the
  interception prerequisite, the proxy/facade single-point-of-failure risk and
  the need for a per-service rollback plan. It does not define bypass detection,
  routing inventory, data reconciliation, a no-return record or a rollback
  procedure; those remain Tycho guidance.
- The existing Fowler record `read.fowler-strangler.2026-10-21` at revision
  `ac274ebe2a36e7553e9f1923e7fbfbc3ff52504c542eec5353127ffba335989e` covers
  mechanism, invariant and alternative; its article has no interception/bypass
  failure or recovery path. The B11 binding audit recorded that gap. The new page
  supplies the missing failure/recovery binding without rewriting the Fowler
  record.
- Adding the public unit is authorized by AGENTS rule 28; the lane does not edit
  the shared register, ledger, source plan or registry. The metadata patch below
  supplies those declarations.

## Book edits

- V10/C05 owner section `### Strangler Fig`:
  - Adds the exact quote as a blockquote after the existing failure/recovery
    owner claim and states the source's support: interception as a prerequisite,
    the façade as a possible failure domain and a per-service rollback plan.
  - Keeps the existing owner claim and its Tycho checks verbatim: bypass
    detection, routing inventory, data reconciliation, named owners and the
    recorded no-return point are not source claims.
  - `updated_at` and `source_inspection_date` advance to 2026-10-29. The
    `### Strangler Fig` heading remains at line 141. The page-level
    `evidence_scope` stays empty because it holds normalized page claims, not
    the pattern-source binding; the binding is recorded in the owner unit, the
    card and the ledger.
- V11/C10 inline card `### Strangler Fig`:
  - **Failure and recovery** carries the exact quote, the source's support and
    the unsupported checks/limits.
  - **Sources** adds `src.aws-strangler`, the record, sections and revision.
  - `evidence_scope.source_ids` adds `src.aws-strangler`;
    `content_review.reviewed_at`, `updated_at` and `source_inspection_date`
    advance to 2026-10-29.
  - The card stays inline; no section is moved or split.
- Lane file hashes:
  - Card (canonical):
    `16f862fa9f2ec4bab78a4bf22bdec67c43458d47e1da38290489fc6ac61572b9`
  - Owner (canonical):
    `b4dbac57ff22b94080610ffd8fe5f1eb09b068392251d1d9e4b5b7f43a315020`
  - Historical views used by content revisions: card
    `20cc89f77091698a397e952de22ac1380a262392c3ddde969b90462af3df89f4`,
    owner
    `5502eeeff9d5407439fae6e425fdccad362156d391592aa1ba7d253787ff48cf`.
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Promotion check

`edition/patterns/sufficient-promotions.v1.json` contains 29 promotions. No
promotion names `tycho.pattern.strangler-fig`, and neither lane file hash matches
any `card_sha256` or `owner_page_sha256`. The entry remains unpromoted and this
lane adds no promotion.

## Preflight

At parent HEAD the baseline fails on the partial dimension and the inline card
path:

    FAIL: tycho.pattern.strangler-fig
      - failure_recovery: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

The lane worktree before the integrator patch reports the same two errors.
A detached scratch worktree at parent HEAD with the two book files copied and
the metadata patch below applied runs:

    FAIL: tycho.pattern.strangler-fig
      - card_path missing or absent
    0/1 entries preflight clean

This is the expected card-path failure: the card is inline in the V11/C10
README and `edition/patterns/card-batches.v1.json` has no `card_path` for this
entry. The preflight stops before card frontmatter checks. The integrator should
split the card after the lane and then record its path.

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145
  entries; 172 read; 142 ledger records.
- `python3 scripts/validate_pattern_registry.py` — PASS: pattern registry 145
  entries, 11 families.
- `python3 scripts/validate_pattern_cards.py` — PASS: pattern cards 11
  batch(es), 145 entries.
- `python3 scripts/check_boundary.py` — PASS: configured lexical boundary
  checks; independent-origin review still required.
- `python3 scripts/check_markdown_line_length.py` — PASS: V11 prose <=100;
  145 exact owner-link exceptions.
- `python3 scripts/validate_claim_references.py` — PASS: traceable claims,
  inventory IDs, evidence status and pinned references.
- `python3 scripts/validate_enrichment.py` — PASS: explicit membership and
  byte conservation.
- `python3 scripts/validate_directory_migration.py` — PASS: reversible
  path-only edits and retained identities.

`python3 scripts/validate_pattern_atlas.py` fails at `atlas-registry-hash` in
the scratch tree because the registry changes and the atlas manifest is a
derived artifact. In the lane worktree before the metadata patch it fails at
`atlas-document-sha`. The lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only shared metadata; the two book
files are already in the lane commit. It adds the new `src.aws-strangler` source,
one ledger record, one source-plan unit and one registry unit, the owner-unit
failure/recovery binding and auxiliary declaration, owner line/count updates,
and authorized content revisions for the two edited files.

```python
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(".").resolve()
sys.path.insert(0, str(ROOT / "scripts"))
from directory_paths import HistoricalView, sha as text_sha

PATTERN = "tycho.pattern.strangler-fig"
SOURCE_ID = "src.aws-strangler"
RECORD_ID = "read.aws-strangler.2026-10-29"
UNIT = "Strangler fig pattern \u2014 AWS Prescriptive Guidance"
URL = (
    "https://docs.aws.amazon.com/prescriptive-guidance/latest/"
    "modernization-decomposing-monoliths/strangler-fig.html"
)
SECTION = "Strangler fig pattern"
SECTIONS = [
    "Strangler fig pattern",
    "Transform",
    "Coexist",
    "Eliminate",
    "Advantages and disadvantages",
]
REVISION = "787962ad56fbc52feb9e3198749ceb7e3b9cea44bca6f9c2bb50530e30c66044"
SOURCE_QUOTE = (
    "Cannot be used in systems where requests to the backend system cannot be "
    "intercepted and routed. The proxy or facade layer can become a single point "
    "of failure or a performance bottleneck if it isn't designed properly. "
    "Requires a rollback plan for each refactored service to revert to the old "
    "way of doing things quickly and safely if things go wrong."
)
OWNER_QUOTE = (
    "Interception may be impossible, internal callers may bypass the fa\u00e7ade, "
    "and old/new state can diverge. Add a bypass detector, a routing inventory "
    "and a data reconciliation check before retiring the old path. Fund "
    "coexistence and name owners for both paths. Rollback remains possible until "
    "a recorded no-return point, where routing inventory and reconciliation "
    "evidence authorize retirement."
)
OWNER = (
    "book/volumes/v10-decision-support-and-modernization/"
    "c05-target-architecture-versus-transition-states/"
    "target-and-transition-architecture-states.md"
)
OWNER_OLD = "book/volumes/v10/c05/target-and-transition-architecture-states.md"
CARD = "book/volumes/v11-pattern-atlas/c10-deployment-modernization/README.md"
OWNER_BASELINE = "be96c16a239a0102b3f96560a4ad1b984f27a90b6147d583a156cd581c82e152"
OWNER_HISTORICAL_PREVIOUS = (
    "6b26a82cb438c8207e8f607c439258a7d9210f37e589043d7effd734dcf44f27"
)
CARD_BASELINE = "dffed0a0c31023b87696c64cd838fe8defe739cc06825aff369bd558003c2976"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(path, data):
    (ROOT / path).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def historical_sha(path):
    return text_sha(HistoricalView(ROOT).read_text(path))


# Source register
path = "sources/register.json"
register = load(path)
assert not any(s["id"] == SOURCE_ID for s in register["sources"])
register["sources"].append({
    "id": SOURCE_ID,
    "title": "Strangler fig pattern",
    "category": "architecture",
    "publisher": "AWS Prescriptive Guidance",
    "kind": "official-docs",
    "url": URL,
    "resolved_url": URL,
    "topics": ["deployment", "migration"],
    "priority": "core",
    "planned_use": (
        "Bounded public page for incremental replacement, coexistence, rollback "
        "planning, interception prerequisites and facade failure conditions."
    ),
    "admission": "admitted-for-research",
    "access": "public-web-or-author-download",
    "reading_status": "full-public-page-inspected",
    "version": (
        "Living documentation, accessed 2026-10-29; canonical text hash "
        f"{REVISION} via scripts/source_content_hash.py"
    ),
    "access_checked": "2026-10-29",
    "content_verified": "2026-10-29",
    "license_notes": (
        "Public AWS documentation; cite short excerpts and paraphrase; do not mirror."
    ),
    "verification_scope": (
        "Complete public page read 2026-10-29: transform/coexist/eliminate "
        "process, advantages and disadvantages table, illustration prose; linked "
        "pages and image interiors not read."
    ),
    "observed_title": "Strangler fig pattern - AWS Prescriptive Guidance",
})
save(path, register)

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
    "access_method": (
        "public HTTPS GET; canonical page text extracted with "
        "scripts/source_content_hash.py"
    ),
    "sections_read": SECTIONS,
    "sections_not_read": [
        "linked child pages",
        "navigation and unrelated chrome (not read as content)",
        "images and their interiors",
    ],
    "tables_figures": [
        "the advantages and disadvantages table was read in text form; not reproduced",
        "one illustration was present but not read; surrounding prose was read",
    ],
    "license_notes": (
        "Public AWS documentation; cite short excerpts and paraphrase; do not mirror."
    ),
    "claims_supported": [
        "Requests to the backend system must be interceptable and routable "
        "for the pattern to apply.",
        "The proxy or facade layer can become a single point of failure or a "
        "performance bottleneck if it is not designed properly.",
        "Each refactored service needs a rollback plan that can revert to the "
        "old way quickly and safely if things go wrong.",
        "Coexistence keeps the monolith available for rollback while traffic is "
        "redirected incrementally.",
    ],
    "claims_not_supported": [
        "automatic bypass detection, routing inventory, data reconciliation or "
        "ownership assignment",
        "a specific rollback procedure, test result or recovery-time bound",
        "implementation behavior, measured migration cost or production outcomes",
        "linked pages, code examples or images",
        "independent reproduction or benchmark",
    ],
    "limitations": (
        "One AWS documentation page; no implementation, migration or production "
        "observation. The canonical digest covers the full extracted page text "
        "because AWS markup has no recognized article-body marker; it includes "
        "title and navigation chrome."
    ),
    "content_sha256": REVISION,
    "read_scope": (
        "complete public page text: transform/coexist/eliminate process, "
        "advantages and disadvantages table and illustration prose; linked pages "
        "and image interiors excluded; digest covers full extracted page text "
        "including navigation chrome"
    ),
    "reviewer": "Automated authoring agent",
    "status": "read",
})
save(path, ledger)

# Owner units
path = "edition/patterns/owner-units.v1.json"
units = load(path)
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
fr = entry["technical_evidence"]["failure_recovery"]
fr["state"] = "supported"
fr["quote"] = OWNER_QUOTE
fr["reason"] = (
    "Binds the AWS Prescriptive Guidance 'Strangler fig pattern' page: "
    "interception and routing are prerequisites, the proxy or facade can become "
    "a single point of failure or performance bottleneck, and each refactored "
    "service needs a rollback plan. Bypass detection, routing inventory, data "
    "reconciliation and the recorded no-return point remain Tycho guidance."
)
fr["binding"] = {
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "section": SECTION,
    "quote": SOURCE_QUOTE,
    "revision": REVISION,
}
entry["source_support"].setdefault("auxiliary", [])
assert not any(
    a["source_id"] == SOURCE_ID for a in entry["source_support"]["auxiliary"]
)
entry["source_support"]["auxiliary"].append({
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "revision": REVISION,
})
entry["notes"] = (
    "Failure/recovery bound 2026-10-29 to the AWS Prescriptive Guidance "
    "'Strangler fig pattern' page: interception and routing are prerequisites, "
    "the proxy or facade can become a single point of failure, and each "
    "refactored service needs a rollback plan. Coverage remains partial-bounded; "
    "no promotion."
)
owner_text = (ROOT / OWNER).read_text(encoding="utf-8")
owner_lines = owner_text.splitlines()
for item in units["entries"]:
    if item["owner"]["path"] == OWNER:
        heading = "### " + item["owner"]["heading"]
        item["owner"]["line"] = next(
            number for number, line in enumerate(owner_lines, 1) if line == heading
        )
units["summary"]["failure_recovery_supported"] += 1
save(path, units)

# Registry
path = "edition/patterns/registry.v1.json"
registry = load(path)
pattern = next(p for p in registry["patterns"] if p["id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID for u in pattern["source_units"])
pattern["source_units"].append({
    "source_id": SOURCE_ID,
    "unit": UNIT,
    "status": "read",
})
pattern["notes"] = (
    "Phase 3 C10 card; bounded owner section and backlink are self-checked. "
    "Failure/recovery bound 2026-10-29 to AWS Prescriptive Guidance; no "
    "promotion, sufficient coverage or independent review is claimed."
)
save(path, registry)

# Source plan
path = "edition/patterns/source-plan.v1.json"
plan = load(path)
entry = next(e for e in plan["entries"] if e["pattern_id"] == PATTERN)
assert not any(u["source_id"] == SOURCE_ID for u in entry["required_units"])
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
plan["registry_sha256"] = sha("edition/patterns/registry.v1.json")
save(path, plan)

# Authorized content revisions for the two edited book files.
path = "edition/content-revisions.json"
revisions = load(path)
owner_current = historical_sha(OWNER_OLD)
card_current = historical_sha(CARD)
assert owner_current != OWNER_HISTORICAL_PREVIOUS
assert card_current != CARD_BASELINE
for revision in revisions["revisions"]:
    for kind in ("directory_documents", "enrichment_documents"):
        for item in revision.get(kind, []):
            if item.get("current_sha256") in (owner_current, card_current):
                raise SystemExit("revision already recorded")
revisions["revisions"].append({
    "issue": 540,
    "authorized_at": "2026-10-29",
    "authorization": (
        "B18 lane: bind the Strangler Fig failure/recovery dimension to the AWS "
        "Prescriptive Guidance page, update the owner section and inline card; "
        "no promotion or owner acceptance."
    ),
    "directory_documents": [
        {
            "path": OWNER,
            "previous_sha256": OWNER_BASELINE,
            "current_sha256": owner_current,
        },
        {
            "path": CARD,
            "previous_sha256": CARD_BASELINE,
            "current_sha256": card_current,
        },
    ],
    "source_blocks": [],
    "enrichment_documents": [{
        "path": OWNER_OLD,
        "previous_sha256": OWNER_HISTORICAL_PREVIOUS,
        "current_sha256": owner_current,
    }],
    "enrichment_additions": [],
    "enrichment_baselines": [],
})
save(path, revisions)
print("metadata patch applied")
print("owner", owner_current)
print("card", card_current)
print("registry_sha", plan["registry_sha256"])
```

The patch:

- adds the source register entry and the `read.aws-strangler.2026-10-29`
  ledger record, and declares the page in the source plan and registry;
- sets `failure_recovery.state` to `supported`, adds the binding to the
  `Strangler fig pattern` section and the auxiliary source declaration, and
  increments the summary `failure_recovery_supported` 50→51;
- recomputes the owner-unit line (unchanged at 141), and increments source-plan
  `required_units` 172→173, `read_units` 171→172 and `ledger_records`
  141→142; the patched registry hash is
  `41c4f2d2aece727aba5d45f9470894ab7a20ca58e66af2387c00d0612b822d65`;
- adds authorized `directory_documents` revisions for the owner page and the
  V11/C10 README, and an `enrichment_documents` revision for the owner page, so
  the directory-migration and enrichment validators pass;
- keeps `technical_coverage`/`decision_coverage` at `partial-bounded`,
  `review_state` at `self-checked`, and promotion and owner acceptance
  unchanged.

## Remaining metadata and review needs

- Split the inline card as planned and add its `card_path` to
  `edition/patterns/card-batches.v1.json`; until then preflight reports the
  expected `card_path missing or absent` failure. The new card must keep
  `src.aws-strangler` in `evidence_scope.source_ids`.
- Refresh derived artifacts after applying the patch: atlas manifest, inventory,
  page census, route index, coverage and reverse maps, semantic audit, candidate
  and review packets, delivery evidence and search indexes. The lane
  intentionally does not touch them.
- After rebuilding the route index, rebind the source-plan
  `route_index_snapshot` and the delivery-evidence ledger counts; the patch
  updates the registry hash and unit counts only.
- Request a fresh external review under the book/atlas gate. Historical B11
  audit findings are prior observations, not reviews of this text; this lane is
  self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No migration, rollback, bypass, reconciliation or failure test was executed.

## Limits

The binding covers one AWS Prescriptive Guidance page at the 2026-10-29
canonical revision. It states the interception prerequisite, façade failure
risk and rollback-plan requirement; it does not define a bypass detector,
routing inventory, reconciliation procedure, no-return record, recovery-time
bound or proof that a migration is safe. Those remain Tycho synthesis. Coverage
remains `partial-bounded`.
