# Evidence layer and entry promotion

The evidence layer is Tycho's mechanism for turning public sources and original
synthesis into an auditable pattern entry. It is deliberately stricter than a
bibliography: a link alone is not evidence, and a card is not sufficient merely
because it exists.

This document describes the current promotion program, its records, its
measurements and its limits. The authoritative machine-readable artifacts are
[sufficient-promotions.v1.json](../edition/patterns/sufficient-promotions.v1.json),
[owner-units.v1.json](../edition/patterns/owner-units.v1.json),
[sufficient-owner-acceptance.v1.json](../edition/patterns/sufficient-owner-acceptance.v1.json)
and the [promotion rules](../governance/ENTRY-PROMOTION.md).

## Why the layer exists

A system-design claim can be:

- a direct statement in a public source;
- a synthesis across sources;
- a conditional recommendation;
- a contraindication or failure mode;
- an inference that must remain labelled as inference.

Tycho keeps those categories separate. The promotion program records which
dimensions are supported, by which source and section, with which exact owner
page and card. It also records what remains unknown.

## Current status

| Measure | Value |
|---|---:|
| Pattern entries | 145 |
| Sufficient technical and decision | 104 |
| Owner-accepted | 94 |
| Acceptance-pending | 10 |
| Remaining entries | 41 |
| Owner units | 145 |
| Shared owner pages | 30 |
| Promotion records with review reports | 80 |
| Saved AI-review reports | 199 |
| Promotion timing cycles | 84 |

All 145 entries are self-checked and have an owner unit. The current coverage
states are:

| Technical coverage | Entries |
|---|---:|
| Sufficient | 104 |
| Partial | 37 |
| Partial-bounded | 4 |

| Decision coverage | Entries |
|---|---:|
| Sufficient | 104 |
| Partial-bounded | 41 |

The difference between technical and decision coverage matters: an entry can
have source support for a mechanism and still lack a decision-grade card,
contraindications or a reviewable alternative.

## The vocabulary

### Source register

A source record contains public origin, publisher, version or access date,
scope, licensing notes and reading status. The canonical file is
[register.json](../sources/register.json). The register is not proof that the
source was fully read.

### Reading ledger

The reading ledger records bounded source units, sections, hashes and reading
outcomes. It is the evidence trail behind a source claim. Unit reads do not
silently promote a source-level status.

### Source plan

The source plan connects an entry or owner unit to the exact source unit and
section that can support it. It is part of the review packet.

### Owner unit

An owner unit is the section-level home of a pattern entry. It carries:

- stable pattern and owner IDs;
- the canonical page and heading anchor;
- technical and decision coverage states;
- source support and decision evidence;
- the review state.

The current owner-unit file has 145 entries, 30 shared pages and no
`name-only` entries.

### Promotion record

A promotion record is the durable claim that a specific owner page and card were
reviewed at a specific commit. It contains:

| Field | Meaning |
|---|---|
| `pattern_id` | Stable pattern identifier |
| `technical` | Technical review result |
| `decision` | Decision review result |
| `reviewed_at` | Review date |
| `reviewed_head` | Commit reviewed |
| `owner_page_sha256` | Hash of the owner page |
| `card_sha256` | Hash of the decision card |
| `reviewer` | Reviewer harness/vendor |
| `report_path` | Saved review report |
| `report_sha256` | Hash of the report |

A promotion is not valid if the owner or card bytes have changed without a
rebind or re-review.

### Owner acceptance

Owner acceptance is a separate decision from technical promotion. It is recorded
in
[sufficient-owner-acceptance.v1.json](../edition/patterns/sufficient-owner-acceptance.v1.json)
and does not replace a review report.

## The promotion pipeline

The current workflow is defined in
[governance/ENTRY-PROMOTION.md](../governance/ENTRY-PROMOTION.md). The short
version is:

1. **Select one entry.** Do not start a second entry while the first is in
   review, rebind or merge.
2. **Prepare the lane.** Edit the owner section, the inline card and a lane note.
   Preserve promoted sibling sections byte-for-byte.
3. **Integrate.** Add sources, ledger records, source-plan units, registry and
   owner-unit metadata. Split a shared card when required.
4. **Review.** A separate read-only reviewer receives the exact owner section,
   card, metadata, hashes and required checks. It must not write to the
   repository.
5. **Promote.** Add or update the promotion record only after the reviewer
   passes. Set `sufficient` only after the record validates.
6. **Merge.** Open a PR from the integration branch and merge only after the
   promotion records validate.
7. **Bookkeep.** Update timing, forecast, charts, STATE, HANDOFF and the README
   counts, then merge the bookkeeping PR.

The evidence gate is not satisfied by a card, a count or a `sufficient-ready`
label. It requires all four technical dimensions and decision evidence to be
supported, plus the independent review.

## The technical dimensions

An entry must cover:

1. **Mechanism** — how it works and what invariant it preserves.
2. **Failure and recovery** — how it fails, what is detected, what recovers.
3. **Alternatives** — a competing option and the conditions that reverse the
   choice.
4. **Limits** — workload, version, operational and evidence boundaries.

Each supported dimension needs a source binding with a source ID, ledger record,
section, exact quote and revision hash. The quote must be verbatim; Tycho
synthesis must be labelled separately.

## The decision dimensions

A decision-sufficient card needs:

- a concrete decision question;
- fit conditions and contraindications;
- a competing alternative;
- failure and recovery consequences;
- related entries and source notes;
- a decision state compatible with the evidence.

A card that says only "use this pattern" is not decision-sufficient.

## Review and acceptance

The review report is saved verbatim under `authoring/ai-reviews/` and indexed by
SHA-256. The current promotions use three reviewer labels:

| Reviewer label | Promotions |
|---|---:|
| DeepSeek Reviewer | 97 |
| Codex / OpenAI gpt-5.6-sol | 6 |
| Codex / OpenAI (gpt-5.6-sol) | 1 |

A reviewer pass is evidence for the gate. It is not owner acceptance, CI or a
claim that the whole book has been reviewed. The owner acceptance record is
batched and currently covers 94 of the 104 promotions.

## Timing and measurements

The timing record measures intervals between consecutive promotion commits in
Europe/Zurich. The values include review, remediation and parallel lane work.

| Measure | Value |
|---|---:|
| Promotion cycles | 84 |
| Mean interval | 57.0 min |
| Median interval | 34.5 min |
| Minimum | 6 min |
| Maximum | 406 min |

The distribution is heavy-tailed. A mean alone would hide the long review and
integration waits. The timing record explicitly says that early entries without
commits are session estimates, not stopwatch measurements.

## What a promotion proves

A promotion proves that:

- the entry's owner page and card were hashed at a reviewed commit;
- a reviewer saw the bounded packet and passed it;
- the technical and decision gates were recorded;
- the promotion record validates against the current artifacts.

It does not prove that:

- every source claim in the book is covered;
- the pattern is correct for every environment;
- the owner accepted the entry;
- the review was human;
- CI ran.

## Failure modes

- **Stale hashes.** A page or card edit without a rebind invalidates the record.
- **Unsupported dimensions.** A missing source binding keeps the entry partial.
- **Review theatre.** A pass without a saved report and hash is not a pass.
- **Count inflation.** A `sufficient-ready` matrix is not a promotion.
- **Acceptance conflation.** Technical sufficiency and owner acceptance are
  separate decisions.
- **Timing distortion.** Intervals include waiting and parallel work; they are
  not pure authoring time.

## How to inspect the layer

1. Read the promotion rules.
2. Open the promotion records and choose one entry.
3. Read its owner unit and card.
4. Compare the recorded hashes with the current files.
5. Open the saved review report and verify its SHA-256.
6. Check the source plan and reading ledger.
7. Check whether owner acceptance is recorded separately.

The layer is intentionally inspectable. A claim that cannot be traced back to a
record is not sufficient, even if the prose sounds convincing.
