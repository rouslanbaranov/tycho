# Pattern owner-unit audit — 2026-10-21

Status: self-checked audit for issue #286. It is not independent review, not
sufficient coverage and not owner acceptance.

## Scope

The audit covers the 144 carded catalog entries on 65 registered technical
owner pages and classifies the 30 pages that own more than one carded pattern.
It follows the remediation in #284 without splitting a page, creating a
document ID or moving ownership to another document.

Artifacts:

- [owner-unit evidence](../edition/patterns/owner-units.v1.json);
- [JSON Schema](../schemas/pattern-owner-units.v1.schema.json);
- [validator](../scripts/validate_pattern_owner_units.py) and adversarial tests;
- premerge integration in [premerge_check.py](../scripts/premerge_check.py).

## Method

1. Read each registered owner page in full.
2. Select exactly one owner unit per entry: one heading section whose text
   owns the pattern's mechanism.
3. Copy mechanism, invariant, failure/recovery and alternative evidence
   verbatim from the unit; the validator rejects a quote that is not an exact
   page substring.
4. Read the decision evidence from the atlas card and the reading ledger:
   decision question, competing alternative, decision state, ten components and
   the exact read record.
5. Derive technical and decision coverage from that evidence.
6. Record a keep, deepen or split decision for every shared owner page.

Where a registered page only linked a carded pattern, a bounded owner note was
added under the section "Bounded pattern ownership notes". These notes are
synthetic design guidance, labelled as such, and do not create a source claim.
The card's reading record remains the source evidence.

## Coverage rules

- partial-bounded: one unit explains the mechanism and states an invariant.
- partial: one unit explains the mechanism only partially, or states no
  invariant.
- partial-reviewed: bounded plus a named independent technical review. None
  exists, so this state is not used.
- name-only: the pattern appears only in a link or list. No carded entry is
  in this state.
- sufficient: a dedicated deep explanation with independent review. Not
  claimed by section-level evidence.

Decision coverage is partial-bounded for all 144 cards because each has the
ten contract components, an exact owner link and a read source record. It is
not sufficient without an independent editorial review.

## Findings

| Measure | Value |
|---|---|
| Carded entries | 144 |
| Registered owner pages | 65 |
| Distinct owner units | 118 |
| Dedicated units | 64 |
| Embedded units | 54 |
| partial-bounded technical | 96 |
| partial technical | 48 |
| name-only technical | 0 |
| sufficient technical | 0 |
| partial-bounded decision | 144 |
| sufficient decision | 0 |
| Independent reviews | 0 |

Evidence dimensions: mechanism is supported for 100 entries and partial for
44; an invariant is supported for 116; failure/recovery for 88; a competing
alternative for 69.

Shared-page decisions: 14 keep, 13 deepen and 3 split. The split candidates are
the identity and authorization landing, the discovery and balancing page, and
the TLS and gateway page. No split is performed.

Thirty-eight bounded notes were added to 24 owner pages. Fourteen entries whose
mechanism was named but not explained were mapped to an existing adjacent
section as partial units instead of receiving a note.

## Edition changes

- Added bounded owner notes to 24 registered owner pages.
- Updated registry and atlas-card owner anchors to the selected section-level
  units; page paths and document IDs are unchanged.
- Recorded content revisions for the 36 changed canonical pages.
- Refreshed the route index, inventory, page census, coverage map, Phase 4
  artifact and delivery evidence.
- Fixed two hyphenated line breaks introduced by earlier bounded notes.

## Limits

- Every unit and quote is self-checked; no named independent reviewer examined
  the mapping or the notes.
- A bounded note is not a deep mechanism chapter and does not establish
  sufficient technical coverage.
- The 48 partial entries still lack either a full mechanism statement or a
  stated invariant and need deepening.
- The 30 shared-page decisions are editorial classifications; the three split
  candidates are not scheduled or performed.
- Page dispositions remain structural; the 419-page semantic review is still
  not performed.
- No release, deployment, hosted retrieval or CI result is claimed.

## Reproduction

    python3 scripts/validate_pattern_registry.py
    python3 scripts/validate_pattern_owner_units.py
    python3 scripts/validate_pattern_cards.py
    python3 scripts/phase4_audit.py --check
    python3 scripts/validate_pattern_phase4.py
    python3 scripts/validate_delivery_evidence.py
    python3 scripts/premerge_check.py \
      --branch feature/TYCHO-286-audit-owner-units-and-coverage-evidence-for-shared-pages \
      --issue-title '[E17-28] Audit owner units and coverage evidence for shared pages'
