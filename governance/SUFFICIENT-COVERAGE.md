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

## Independent review

A sufficient promotion requires an independent external AI review under
[AI-INDEPENDENT-REVIEW.md](AI-INDEPENDENT-REVIEW.md):

- reviewer from a different vendor and harness than the authoring agent;
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

## Scope and non-goals

- This rule applies to the pattern atlas entries, not to unrelated book pages.
- A sufficient entry is not a claim that every source claim is complete or that CI ran.
- Human review is not required for this gate; the external AI review is the review gate.
- Owner acceptance remains a separate decision, recorded in
  `edition/patterns/sufficient-owner-acceptance.v1.json`; pending is not acceptance.
