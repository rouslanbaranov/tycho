# B17 — Server-Side Discovery invariant lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry remains `partial-bounded`; the preflight pass below depends on the
integrator applying the metadata patch and later splitting the inline card.

## Lane coordinates

- Parent HEAD: `c1ba6a9db37711cdedac956a481ee0a0ab4edda1` (`c1ba6a9d`).
- Branch: `b17-server-side-discovery`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b17-server-side-discovery`.
- Scope: the inline V11/C02 `README.md` Server-Side Discovery card and the
  V08/C08 owner section `discovery-balancing.md#server-side-discovery` only.
- The card remains inline in the V11/C02 README. It is not split into a
  dedicated card file in this lane; the integrator owns that split.
- This is a single-entry lane; no other entry, shared owner page, promotion or
  generated file is changed.

## Source binding

- Source: `src.envoy`, Envoy documentation. Already admitted in
  `sources/register.json`; no register change is needed.
- Unit: Service discovery — Envoy documentation,
  `https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/service_discovery`.
- New ledger record: `read.envoy-service-discovery-consistency.2026-10-29`;
  section read: `On eventually consistent service discovery`.
- Exact public quote, verbatim in the served article text:

      If a host continues to pass health check even after becoming absent from
      the discovery data, Envoy will still route.

- Revision:
  `f07699d00554ee3b3cf13d6644b115645ba5efe4258cbb5331471bbdd0a59e6e`.
  The page was fetched twice on 2026-10-29; both responses were 30,248 bytes
  with raw-HTML SHA-256
  `d3698391dd7042a86eaf6e564af6d6bc47b7927dae6a777eda27106ad3cc0679`, and
  both canonical article-text hashes were the revision above, computed with
  `scripts/source_content_hash.py`. The record pins the 2026-10-29
  representation.
- The existing record `read.envoy-service-discovery.2026-10-21` covers the
  same page at revision
  `f8e4f3e08d81df8cb182ef8e7b443162d2180d8b2b6b653785722a6e282571af`
  and lists the same section, but its revision does not match the 2026-10-29
  representation. This lane does not rewrite the historical record; the
  metadata patch adds a second record for the re-fetched section. The same
  sentence is present in a 2026-10-02 Wayback snapshot of the page, but the
  binding revision is the 2026-10-29 canonical hash.
- The quote states that a host absent from discovery data can still receive
  traffic while its health check passes. It does not define a propagation
  bound, a drain procedure or a health-check interval; those remain Tycho
  guidance.
- No new source-register entry is needed. The lane does not edit the shared
  ledger, source plan or registry; the metadata patch below supplies the
  record and the unit declarations.

## Book edits

- V08/C08 owner section `### Server-Side Discovery`:
  - Adds the exact quote as a blockquote and states the consequence: a healthy
    proxy can route to a backend that discovery has already removed; active
    health checking is the documented way to determine cluster health.
  - Keeps the existing mechanism, invariant, failure/recovery and alternative
    sentences verbatim so the existing bindings still preflight.
  - Labels the unsupported limits: no propagation bound, drain procedure or
    health-check interval.
  - `updated_at` advances to 2026-10-29. `source_inspection_date` remains
    2026-10-20 because the page's `evidence_scope` records the 2026-10-20
    enrichment sources (`src.sre-frontend-enrichment`,
    `src.sre-balancing-enrichment`), not the new pattern-source binding.
    Adding `src.envoy` there would require an enrichment inspection record.
    The new binding is recorded in the owner-unit, card and ledger record.
  - The `### Server-Side Discovery` heading remains at line 231. The
    `### Load Balancing` heading moves from 246 to 255; the metadata patch
    recomputes every owner `line` on the page.
- V11/C02 inline card `### Server-Side Discovery`:
  - **Good-fit conditions** now names eventual consistency and active health
    checks as conditions.
  - **Failure and recovery** carries the exact quote, the source section, the
    active-health-check mitigation, and the unsupported propagation/interval
    limits.
  - **Sources** adds the new record, section, revision and the same limit.
  - `content_review.reviewed_at`, `updated_at` and
    `source_inspection_date` advance to 2026-10-29.
    `evidence_scope.source_ids` already lists `src.envoy`, so no card
    source-list change is needed.
  - The card stays inline; no section is moved or split.
- Lane file hashes:
  - Card:
    `a8a2b57a10082f1066068b71e8f4c743dd3487a48aef7644a9b5ad0a6d647b02`
  - Owner:
    `a9f1ea00ae683adc78062c1ba15a9376c6fd64908a3028777b159958a5cef2ab`
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Promotion check

`edition/patterns/sufficient-promotions.v1.json` contains 29 promotions. No
promotion names `tycho.pattern.server-side-discovery`, and neither lane file
hash matches any `card_sha256` or `owner_page_sha256`. The entry remains
unpromoted and this lane adds no promotion.

## Preflight

At parent HEAD the baseline fails on the partial invariant and the inline card
path:

    FAIL: tycho.pattern.server-side-discovery
      - invariant: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

The lane worktree before the integrator patch reports the same two errors.
`python3 scripts/validate_pattern_owner_units.py` also reports
`owner-units-unit-ambiguous: Load Balancing` because the moved heading still
has its old line field; the metadata patch fixes that.

A detached scratch worktree at parent HEAD with the two book files copied and
the metadata patch below applied runs:

    FAIL: tycho.pattern.server-side-discovery
      - card_path missing or absent
    0/1 entries preflight clean

This is the expected card-path failure: the card is inline in the V11/C02
README and `edition/patterns/card-batches.v1.json` has no `card_path` for
this entry. The preflight stops before card frontmatter checks. The integrator
should split the card after the lane and then record its path.

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145
  entries; 171 read; 141 ledger records.
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

`python3 scripts/validate_pattern_atlas.py` fails at `atlas-registry-hash`
in the scratch tree because the registry changes and the atlas manifest is a
derived artifact. In the lane worktree before the metadata patch it fails at
`atlas-document-sha`. The lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only shared metadata; the two book
files are already in the lane commit. It reuses the admitted `src.envoy` and
adds one ledger record, one source-plan unit, one registry unit, the owner-unit
invariant binding and auxiliary declaration, owner line/count updates, and
authorized content revisions for the two edited files.

```python
import hashlib
import json
from pathlib import Path

ROOT = Path(".").resolve()
PATTERN = "tycho.pattern.server-side-discovery"
SOURCE_ID = "src.envoy"
RECORD_ID = "read.envoy-service-discovery-consistency.2026-10-29"
UNIT = "Service discovery \u2014 Envoy documentation"
URL = "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/service_discovery"
SECTION = "On eventually consistent service discovery"
REVISION = "f07699d00554ee3b3cf13d6644b115645ba5efe4258cbb5331471bbdd0a59e6e"
OWNER = ("book/volumes/v08-delivery-deployment-and-recovery/"
         "c08-network-request-paths-routing-and-edge-delivery/"
         "discovery-balancing.md")
OWNER_OLD = "book/volumes/v08/c08/discovery-balancing.md"
CARD = "book/volumes/v11-pattern-atlas/c02-api-communication/README.md"
ENRICHMENT_PREVIOUS = "d7f5b7990f9fef61888321259f45733b71f9b8e6757483a2c5ffbcd2c9bedc9e"
DIRECTORY_PREVIOUS = "1ade6168a2bf516ea916bbcdfd0fa16605587e129598946a6d3f5ac4d1c0299a"
CARD_PREVIOUS = "aae986266f0a3b93e2711c8a33f9026c6e68413cd6fab37e03fefa5cceb27e3f"


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
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    from directory_paths import HistoricalView, sha as text_sha
    return text_sha(HistoricalView(ROOT).read_text(path))


# Owner units
path = "edition/patterns/owner-units.v1.json"
units = load(path)
entry = next(e for e in units["entries"] if e["pattern_id"] == PATTERN)
inv = entry["technical_evidence"]["invariant"]
inv["state"] = "supported"
inv["reason"] = (
    "Envoy documents that a host absent from discovery data can still receive "
    "traffic while its health check passes, so a healthy proxy can hold a stale "
    "selection set; active health checking is the documented mitigation."
)
inv["binding"] = {
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "section": SECTION,
    "quote": ("If a host continues to pass health check even after becoming "
              "absent from the discovery data, Envoy will still route."),
    "revision": REVISION,
}
entry["source_support"]["auxiliary"] = [{
    "source_id": SOURCE_ID,
    "ledger_record": RECORD_ID,
    "revision": REVISION,
}]
entry["technical_coverage"] = "partial-bounded"
entry["notes"] = (
    "Invariant bound 2026-10-29 to Envoy's 'On eventually consistent service "
    "discovery' section: a host absent from discovery data can still receive "
    "traffic while its health check passes. Coverage partial-bounded; no "
    "promotion. Propagation bounds, drain procedures and health-check intervals "
    "remain Tycho guidance."
)

owner_text = (ROOT / OWNER).read_text(encoding="utf-8")
owner_lines = owner_text.splitlines()
for item in units["entries"]:
    if item["owner"]["path"] == OWNER:
        heading = "### " + item["owner"]["heading"]
        item["owner"]["line"] = next(
            number for number, line in enumerate(owner_lines, 1)
            if line == heading
        )

entries = units["entries"]
by_page = {}
for item in entries:
    by_page.setdefault(item["owner"]["path"], []).append(item)
units_seen = {}
for item in entries:
    key = (item["owner"]["path"], item["owner"]["heading"])
    units_seen.setdefault(key, {"kinds": set(), "count": 0})
    units_seen[key]["kinds"].add(item["owner"]["unit_kind"])
    units_seen[key]["count"] += 1
shared = [path for path, items in by_page.items() if len(items) > 1]
for page in units["shared_pages"]:
    if page["path"] in by_page:
        page["bounded_entries"] = sum(
            1 for item in by_page[page["path"]]
            if item["technical_coverage"] == "partial-bounded"
        )
units["summary"].update({
    "entries": len(entries),
    "owner_pages": len(by_page),
    "shared_pages": len(shared),
    "owner_units": len(units_seen),
    "dedicated_units": sum(1 for value in units_seen.values()
                           if "dedicated" in value["kinds"]),
    "embedded_units": sum(1 for value in units_seen.values()
                          if "dedicated" not in value["kinds"]),
    "mechanism_supported": sum(1 for item in entries
                               if item["technical_evidence"]["mechanism"]["state"] == "supported"),
    "invariant_supported": sum(1 for item in entries
                               if item["technical_evidence"]["invariant"]["state"] == "supported"),
    "failure_recovery_supported": sum(
        1 for item in entries
        if item["technical_evidence"]["failure_recovery"]["state"] == "supported"
    ),
    "alternative_supported": sum(
        1 for item in entries
        if item["technical_evidence"]["alternative"]["state"] == "supported"
    ),
    "technical_partial_bounded": sum(1 for item in entries
                                     if item["technical_coverage"] == "partial-bounded"),
    "technical_partial": sum(1 for item in entries
                             if item["technical_coverage"] == "partial"),
    "technical_name_only": sum(1 for item in entries
                               if item["technical_coverage"] == "name-only"),
    "technical_sufficient": sum(1 for item in entries
                                if item["technical_coverage"] == "sufficient"),
    "decision_partial_bounded": sum(1 for item in entries
                                    if item["decision_coverage"] == "partial-bounded"),
    "decision_partial": sum(1 for item in entries
                            if item["decision_coverage"] == "partial"),
    "decision_name_only": sum(1 for item in entries
                              if item["decision_coverage"] == "name-only"),
    "decision_sufficient": sum(1 for item in entries
                               if item["decision_coverage"] == "sufficient"),
    "partial_reviewed": sum(1 for item in entries
                            if "partial-reviewed" in (item["technical_coverage"],
                                                      item["decision_coverage"])),
    "independent_reviews": sum(1 for item in entries
                               if item["review_state"] == "independent-reviewed"),
})
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
    "sections_read": [SECTION],
    "sections_not_read": [
        "other sections of the service discovery page",
        "linked child pages",
        "navigation and unrelated chrome",
    ],
    "tables_figures": [
        "the routing matrix in the inspected section was read in text form; not reproduced",
    ],
    "license_notes": "Public page; cite short excerpts and paraphrase; do not mirror.",
    "claims_supported": [
        "Envoy treats service discovery as eventually consistent; a host absent ",
        "from discovery data can still receive traffic while its health check ",
        "passes, and active health checking determines cluster health.",
    ],
    "claims_not_supported": [
        "a propagation bound",
        "a drain procedure",
        "a health-check interval",
        "implementation behavior",
        "independent reproduction or benchmark",
    ],
    "limitations": (
        "One documentation page section read on 2026-10-29; the rest of the page "
        "was not re-read in this record and no cluster, proxy or failure test was run."
    ),
    "content_sha256": REVISION,
    "read_scope": (
        "served page section 'On eventually consistent service discovery' from the "
        "2026-10-29 fetch; other sections not re-read"
    ),
    "reviewer": "Automated authoring agent",
    "status": "read",
})
save(path, ledger)

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
pattern["coverage"]["technical"] = "partial-bounded"
pattern["coverage"]["overall"] = "partial-bounded"
pattern["technical_owner"]["state"] = "partial-bounded"
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
    "sections": [SECTION],
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
assert owner_current != ENRICHMENT_PREVIOUS
for revision in revisions["revisions"]:
    for kind in ("directory_documents", "enrichment_documents"):
        for item in revision.get(kind, []):
            if item.get("current_sha256") == owner_current:
                raise SystemExit("owner revision already recorded")
revisions["revisions"].append({
    "issue": 540,
    "authorized_at": "2026-10-29",
    "authorization": (
        "B17 lane: bind the Server-Side Discovery invariant to the Envoy service "
        "discovery page and update the owner section and inline card; no promotion "
        "or owner acceptance."
    ),
    "directory_documents": [
        {
            "path": OWNER,
            "previous_sha256": DIRECTORY_PREVIOUS,
            "current_sha256": owner_current,
        },
        {
            "path": CARD,
            "previous_sha256": CARD_PREVIOUS,
            "current_sha256": card_current,
        },
    ],
    "source_blocks": [],
    "enrichment_documents": [{
        "path": OWNER_OLD,
        "previous_sha256": ENRICHMENT_PREVIOUS,
        "current_sha256": owner_current,
    }],
    "enrichment_additions": [],
    "enrichment_baselines": [],
})
save(path, revisions)
print("metadata patch applied; owner", owner_current, "card", card_current)
```

The patch:

- sets `invariant.state` to `supported`, adds the binding to the
  `On eventually consistent service discovery` section and the auxiliary
  source declaration, changes `technical_coverage` from `partial` to
  `partial-bounded`, and recomputes the owner-unit summary
  (`invariant_supported` 61→62, `technical_partial` 89→88,
  `technical_partial_bounded` 27→28) and the shared page's
  `bounded_entries` 0→1;
- recomputes every owner `line` field on the shared page (Server-Side 231,
  Client-Side 216, Load Balancing 255) and the shared-page and summary counts;
- adds the new ledger record, the registry source unit and the source-plan
  unit, updates the registry coverage and technical-owner state, increments
  `required_units` 171→172, `read_units` 170→171 and `ledger_records`
  140→141, and recomputes `registry_sha256`;
- adds authorized `directory_documents` revisions for the owner page and the
  V11/C02 README, and an `enrichment_documents` revision for the owner page,
  so the directory-migration and enrichment validators pass;
- leaves `review_state` at `self-checked`, technical/decision coverage at
  `partial-bounded`, and promotion and owner acceptance unchanged.

## Remaining metadata and review needs

- Refresh derived artifacts after applying the patch: atlas manifest,
  inventory, page census, route index, coverage and reverse maps, semantic
  audit, candidate and review packets, delivery evidence and search indexes.
  The lane intentionally does not touch them.
- After rebuilding the route index, rebind the source-plan
  `route_index_snapshot` and the delivery-evidence ledger counts; the patch
  updates the registry hash and unit counts only.
- Split the inline card as planned and add its `card_path` to
  `edition/patterns/card-batches.v1.json`; until then preflight reports the
  expected `card_path missing or absent` failure. The new card should keep
  `src.envoy` in `evidence_scope.source_ids`.
- The owner page `content_review` remains the pre-existing self-checked record
  with its 2026-10-20 reviewer field; this lane updates only `updated_at`.
  No content acceptance is asserted. The page-level `source_inspection_date`
  remains the 2026-10-20 enrichment date for the reason explained above.
- Request a fresh external review under the book/atlas gate. Historical
  phase-B findings B4-036 and B4-037 are prior observations, not reviews of
  this text; this lane is self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No proxy, cluster, resize or failure test was executed.

## Limits

The binding covers one Envoy documentation page section at the 2026-10-29
canonical revision. It states eventual consistency and stale routing; it does
not quantify propagation delay, define a drain protocol or specify a
health-check interval. Those remain Tycho synthesis. Coverage remains
`partial-bounded`.
