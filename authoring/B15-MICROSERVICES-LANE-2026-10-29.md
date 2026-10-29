# B15 — Microservices Architecture failure/recovery lane

Status: lane-local book edit, self-checked on 2026-10-29. No shared edition
metadata, promotion, generated artifact or owner acceptance is included. The
entry stays `partial-bounded`; the preflight pass below depends on the
integrator applying the metadata patch and later splitting the inline card.

## Lane coordinates

- Parent HEAD: `50fecc2b464d8f8e11b07d460d8545dfbaa98716`.
- Branch: `b15-microservices`; worktree:
  `/Users/rbaranov/Projects/tycho-worktrees/b15-microservices`.
- Scope: the inline V11/C01 `README.md` Microservices Architecture card and
  the V02/C04 owner section
  `service-orientation-microservices-and-distribution.md#microservices-architecture`
  only.
- The card remains inline in the V11/C01 README. It is not split into a
  dedicated card file in this lane; the integrator owns that split.
- This is a single-entry lane; no other entry, shared owner page, promotion or
  generated file is changed.

## Source binding

- Source: `src.microservices`, Lewis and Fowler, *Microservices*,
  `https://martinfowler.com/articles/microservices.html`.
- Ledger record: `read.microservices-article.2026-10-21`; section
  `Design for failure`. The record already lists that section in
  `sections_read`.
- Exact primary quote, verbatim in the canonical visible text of the served
  page:

      Since services can fail at any time, it's important to be able to detect the
      failures quickly and, if possible, automatically restore service.

- Exact supporting quote, same section and representation:

      Any service call could fail due to unavailability of the supplier, the client
      has to respond to this as gracefully as possible.

- Revision: `a29812554151c3ca90c22a81aef80ea271ae1ee80bf6ca90fb8d9d78281338f8`.
  The public URL was fetched on 2026-10-29 and the 86,071 served HTML bytes hash
  to this value, matching the ledger `content_sha256`. The canonical
  visible-text hash computed by `scripts/source_content_hash.py` is
  `1e5eb8ca1c2120855ac41b072396d216c6ab04bd66ee3b96497a1d514595b1fd`.
  The 2026-10-21 record pins the raw served-HTML digest; this lane reuses that
  recorded revision rather than minting a second record for the same page.
- The primary quote supports failure detection and automatic restoration. The
  supporting quote supports graceful client response. The section does not
  specify timeout values, an idempotency or retry mechanism, observability
  signals or a recovery-time bound. Those remain Tycho guidance and are
  labelled as such in both book files.
- No new source, ledger record, source-plan unit or registry unit is needed:
  `src.microservices` is already admitted, read and declared for this pattern.

## Book edits

- V02/C04 owner section `### Microservices Architecture`:
  - The failure paragraph now opens with the bound owner claim: because
    services can fail at any time, applications must tolerate the failure and
    respond gracefully, while detecting failures quickly and, if possible,
    restoring service automatically.
  - The paragraph keeps the remote-surface budget and dependency-degradation
    guidance as Tycho synthesis, and states the source limits explicitly:
    timeout values, idempotency/retry mechanics, observability signals and a
    recovery-time bound are not specified by the article.
  - `updated_at` and `source_inspection_date` advance to 2026-10-29. The
    section heading remains at line 92. The next shared-page heading,
    `### Service-Oriented Architecture (SOA)`, moves from 111 to 114, so the
    metadata patch must update both owner-unit `line` fields.
- V11/C01 inline card, `### Microservices Architecture`:
  - **Failure and recovery** now states the source-bound claim, names the
    `Design for failure` section, and labels timeouts, retry identity,
    observability signals and recovery-time bounds as Tycho guidance.
  - **Sources** records the section and the pinned revision in addition to the
    existing read-record citation.
  - `content_review.reviewed_at`, `updated_at` and
    `source_inspection_date` advance to 2026-10-29. `evidence_scope.source_ids`
    already lists `src.microservices`, so no frontmatter source list changes.
  - The card stays inline; no section is moved or split.
- Lane file hashes:
  - Card:
    `21e735e089fe12be4863430d2dcf7e983ec31dedc945c562a9225b3294c33de2`
  - Owner:
    `827cecd2c4dda19c78d43660f163888cc42b160690a3e32ea48f5ce181d115b3`
- No other book file, edition JSON, promotion or generated file is changed by
  this lane.

## Promotion check

`edition/patterns/sufficient-promotions.v1.json` contains 27 promotions. No
promotion names `tycho.pattern.microservices-architecture`, and neither lane
file hash matches any `card_sha256` or `owner_page_sha256`. The entry remains
unpromoted and this lane adds no promotion.

## Preflight

At the parent HEAD the baseline fails on the unbound dimension and on the inline
card path:

    FAIL: tycho.pattern.microservices-architecture
      - failure_recovery: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

After the two book edits, the lane worktree still fails because the
integrator-owned `edition/patterns/owner-units.v1.json` says
`failure_recovery: partial`:

    FAIL: tycho.pattern.microservices-architecture
      - failure_recovery: state 'partial', not supported
      - card_path missing or absent
    0/1 entries preflight clean

A detached scratch worktree at the parent HEAD with the two book files copied
and the metadata patch below applied runs:

    FAIL: tycho.pattern.microservices-architecture
      - card_path missing or absent
    0/1 entries preflight clean

This is the expected card-path failure: the card is inline in the V11/C01
README and `edition/patterns/card-batches.v1.json` has no `card_path` for this
entry. The preflight stops before card frontmatter checks. The integrator
should split the card after the lane and then record its path.

The same scratch tree also passes:

- `python3 scripts/validate_pattern_owner_units.py` — PASS: owner units 145
  entries, 145 units, 30 shared pages.
- `python3 scripts/validate_pattern_sources.py` — PASS: source plan 145 entries;
  168 read; 139 ledger records.
- `python3 scripts/validate_pattern_registry.py` — PASS: pattern registry 145
  entries, 11 families.
- `python3 scripts/validate_pattern_cards.py` — PASS: pattern cards 11
  batch(es), 145 entries.
- `python3 scripts/check_boundary.py` — PASS: configured lexical boundary
  checks; independent-origin review still required.
- `python3 scripts/validate_claim_references.py` — PASS: traceable claims,
  inventory IDs, evidence status and pinned references.
- `python3 scripts/validate_enrichment.py` — PASS: explicit membership and
  byte conservation.

`python3 scripts/check_markdown_line_length.py` fails in the scratch and at the
parent HEAD on a pre-existing, unrelated line:
`book/volumes/v11-pattern-atlas/c03-messaging-integration/request-reply-messaging.md:59: 165`.
This lane did not edit that file. Its two edited files have no line over 100
characters, including the new prose.

`python3 scripts/validate_pattern_atlas.py` still fails at
`atlas-document-sha` until the integrator refreshes the atlas manifest and the
other derived artifacts. This is a derived-artifact refresh, not a content
failure. The lane intentionally does not touch generated files.

## Metadata patch (integrator)

Run this from the repository root. It edits only the shared owner-units file;
the two book files are already in the lane commit. It reuses the admitted
`read.microservices-article.2026-10-21` ledger record. No ledger, source-plan,
registry, source-register or promotion change is required.

```python
import json
from pathlib import Path

root = Path(".").resolve()
path = root / "edition/patterns/owner-units.v1.json"
data = json.loads(path.read_text(encoding="utf-8"))
entry = next(
    e for e in data["entries"]
    if e["pattern_id"] == "tycho.pattern.microservices-architecture"
)
owner_text = (root / entry["owner"]["path"]).read_text(encoding="utf-8")
squash = lambda value: " ".join(value.split())

owner_quote = (
    "Because services can fail at any time, applications must be designed to "
    "tolerate the failure of a service and respond as gracefully as possible; "
    "recovery depends on detecting failures quickly and, if possible, restoring "
    "service automatically."
)
assert squash(owner_quote) in squash(owner_text), "owner quote not verbatim"

fr = entry["technical_evidence"]["failure_recovery"]
fr["state"] = "supported"
fr["quote"] = owner_quote
fr["reason"] = (
    "Binds the article's Design for failure section: any service call can fail, "
    "applications must tolerate the failure and respond gracefully, and recovery "
    "depends on detecting failures quickly and restoring service automatically. "
    "The article does not specify timeout values, an idempotency or retry "
    "mechanism, observability signals or a recovery-time bound; those remain "
    "Tycho guidance."
)
fr["binding"] = {
    "source_id": "src.microservices",
    "ledger_record": "read.microservices-article.2026-10-21",
    "section": "Design for failure",
    "quote": (
        "Since services can fail at any time, it's important to be able to "
        "detect the failures quickly and, if possible, automatically restore "
        "service."
    ),
    "revision": (
        "a29812554151c3ca90c22a81aef80ea271ae1ee80bf6ca90fb8d9d78281338f8"
    ),
}
fr["supporting_bindings"] = [{
    "source_id": "src.microservices",
    "ledger_record": "read.microservices-article.2026-10-21",
    "section": "Design for failure",
    "quote": (
        "Any service call could fail due to unavailability of the supplier, the "
        "client has to respond to this as gracefully as possible."
    ),
    "revision": (
        "a29812554151c3ca90c22a81aef80ea271ae1ee80bf6ca90fb8d9d78281338f8"
    ),
}]
entry["notes"] = (
    "Failure/recovery bound 2026-10-29 to the Design for failure section of the "
    "admitted microservices article; all four dimensions supported, coverage "
    "partial-bounded, no promotion; timeout, retry-identity, observability and "
    "recovery-time specifics remain Tycho guidance."
)

lines = owner_text.splitlines()
entry["owner"]["line"] = next(
    number for number, line in enumerate(lines, 1)
    if line == "### " + entry["owner"]["heading"]
)
soa = next(
    e for e in data["entries"]
    if e["pattern_id"] == "tycho.pattern.service-oriented-architecture-soa"
)
soa["owner"]["line"] = next(
    number for number, line in enumerate(lines, 1)
    if line == "### " + soa["owner"]["heading"]
)
data["summary"]["failure_recovery_supported"] += 1
path.write_text(
    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
print("owner-units patch applied")
```

The patch:

- sets `failure_recovery.state` to `supported`, adds the bound owner claim,
  the primary binding to the `Design for failure` section and the supporting
  binding to the graceful-response sentence;
- rewrites the entry note and increments
  `summary.failure_recovery_supported` from 48 to 49;
- updates the owner-unit `line` fields for Microservices Architecture (92) and
  Service-Oriented Architecture SOA (114);
- leaves `technical_coverage` at `partial-bounded` (all four dimensions are
  supported but the entry has no promotion), `decision_coverage` at
  `partial-bounded`, and `review_state` at `self-checked`;
- does not change the registry, source plan, ledger, source register or any
  promotion.

## Remaining metadata and review needs

- Refresh derived artifacts after the patch: atlas manifest, inventory, content
  revisions, page census, route index, coverage/reverse maps, semantic audit,
  candidate and review packets, delivery evidence, search pre-enrichment
  snapshot and search indexes. The lane intentionally does not touch them.
- Split the inline card as planned and add its `card_path` to
  `edition/patterns/card-batches.v1.json`; until then preflight reports the
  expected `card_path missing or absent` failure. The new card should keep
  `src.microservices` in `evidence_scope.source_ids`.
- The owner page frontmatter `evidence_scope.source_ids` lists only
  `src.soa-model`, although the page already cites `src.microservices` and now
  carries an explicit failure/recovery binding. The lane leaves that
  pre-existing metadata for the integrator; the card and owner-unit source
  declarations carry `src.microservices`.
- Request a fresh external review under the book/atlas gate. The historical
  phase-B finding B3-009 is the finding this lane addresses, not a review of
  this text; this lane is self-checked only.
- Owner acceptance, promotion, CI and merge permission are not claimed.
- No runtime failure, degradation, retry or recovery test was executed.

## Limits

The binding covers one rolling public article at the recorded 2026-10-29
served-HTML revision. It supports failure tolerance, graceful client response,
failure detection and automatic restoration. It does not establish that a
particular topology recovers within a bound, that an idempotency mechanism is
correct, or that observability signals are sufficient. Those steps are Tycho
guidance, not source claims. Coverage remains `partial-bounded`.
