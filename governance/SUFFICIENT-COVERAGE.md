# Sufficient coverage

Status: mandatory for the #540 promotion program. Effective: 2026-10-26.

`sufficient-ready` is not `sufficient`. A sufficient entry needs evidence, an independent
external AI review and an explicit promotion record. A count, a batch label or a
`sufficient-ready` matrix does not promote an entry.

## Technical sufficiency

For a pattern entry, all of the following must hold:

1. One dedicated owner unit exists with a named heading and anchor.
2. Mechanism, invariant, failure/recovery and alternative are `supported` by an admitted
   source at the exact revision and section scope recorded in the ledger.
3. The source read record is `read`, has a content hash and records limitations.
4. Synthetic-only or operational limits are labelled and do not masquerade as source
   support.
5. No unresolved high-risk gap remains in the four dimensions.

## Decision sufficiency

All of the following must hold:

1. The atlas card has a decision question, identity, fit conditions, contraindications,
   competing alternative, failure/recovery, related entries and source note.
2. The decision state is compatible with the evidence; `applicable-under-conditions` is
   not a sufficient label by itself.
3. The card and owner unit do not claim `sufficient` before promotion.
4. The card, owner unit and source plan agree on the same pattern and source binding.

## Per-dimension source binding

A supported dimension may carry a `binding` with:

- `source_id`;
- `ledger_record`;
- `section` from the ledger's read scope;
- an exact `quote` from the source representation;
- the ledger `revision` hash.

A `sufficient` entry, or any entry with a promotion record, must bind every supported
dimension. A binding whose section was not read or whose revision does not match the
ledger is a validator failure.

## Independent review

A sufficient promotion requires an independent external AI review under
[AI-INDEPENDENT-REVIEW.md](AI-INDEPENDENT-REVIEW.md):

- reviewer from a different vendor and harness than the authoring agent;
- a fresh read-only DeepSeek Reviewer agent is an accepted external reviewer with the
  same authority when no different-vendor harness is available or it is unavailable;
- read-only, pinned HEAD and exact artifact hashes;
- per-entry or bounded-batch report;
- verdict `pass` for both technical and decision sufficiency;
- no blocking finding;
- report saved in `authoring/ai-reviews/` and indexed by SHA-256.

A pass on a reading package or a sufficient-ready matrix does not replace this review.

## Promotion record

Every promotion is recorded in `edition/patterns/sufficient-promotions.v1.json` with:

- `pattern_id`;
- the reviewed HEAD and artifact hashes;
- `technical: pass` and `decision: pass`;
- reviewer harness/vendor, session and timestamp;
- report path and SHA-256;
- owner acceptance reference, when recorded.

The registry, owner-units and delivery-evidence artifacts may record `sufficient` only
when this record exists and matches the current hashes. A stale record does not promote a
changed page, card or source binding.

## Remediation fan-out

A review finding is not closed when the primary record changes. Update every derived
copy in the same change: source plan, ledger, pilot manifest, owner units, registry,
cards, semantic audit, atlas manifest and content revisions. Then regenerate indexes and
run the validators.

The pilot validator compares the manifest source units and current coverage with the
source plan and owner units. A stale manifest field is a validator failure, not a note.

Do not use a mutable raw-HTML hash as a revision. Use the committed
`scripts/source_content_hash.py` canonical text hash, or record an explicit,
independently checkable representation and extraction procedure.

## Regression guards

Every review finding must add a mechanical regression guard, or record the exact
manual check and why automation is not yet possible. Track guards in
`authoring/ai-reviews/REGRESSIONS.md`; a finding without a guard is not closed.

## Scope and non-goals

- This rule applies to the pattern atlas entries, not to unrelated book pages.
- A sufficient entry is not a claim that every source claim is complete or that CI ran.
- Human review is not required for this gate; the external AI review is the review gate.
- Owner acceptance remains a separate decision, recorded in
  `edition/patterns/sufficient-owner-acceptance.v1.json`; pending is not acceptance.
