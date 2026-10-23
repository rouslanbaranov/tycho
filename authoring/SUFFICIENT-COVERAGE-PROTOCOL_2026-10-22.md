# Sufficient-coverage protocol — 2026-10-22

## Status

This is a protocol and candidate triage, not a sufficiency claim. All 145 pattern
entries remain `partial-bounded`; 0 are `sufficient`. All 145 have a non-human
independent-agent section review record, but no human per-page review and no owner
acceptance is recorded. Review findings remain unremediated unless a re-review record says
otherwise.

> **Phase B acceptance — 2026-10-23:** Phase A is 52 pass / 0 PWF / 0 reject. The
> independent Phase B re-audit accepted 34 pass / 59 PWF / 0 reject, so the overall
> record is 86 pass / 59 PWF / 0 reject. Phase B is accepted with findings; sufficient
> remains 0; human and owner gates remain open. See
> [the Phase B acceptance](PHASE-B-ACCEPTANCE_2026-10-23.md),
> [the gap acceptance](PHASE-A-GAP-ACCEPTANCE_2026-10-23.md) and
> [integration](SUFFICIENT-REVIEW-INTEGRATION_2026-10-22.md).

## Contract criteria

The pattern-atlas contract defines `sufficient` as a dedicated deep explanation plus
independent review. A section-level bounded unit is not enough.

A candidate must satisfy all of:

1. **Dedicated owner unit.** The heading names the pattern or an alias.
2. **Deep explanation.** At least 120 words in the anchored section, covering mechanism,
   invariant, failure/recovery, alternative and limits.
3. **Source read.** The card's reading-ledger record status is `read`.
4. **Independent review.** A named reviewer who did not author the change records the
   page hash, verdict and findings.
5. **Decision layer.** The card keeps its decision question, competing alternative,
   applicability state and ten components.

## Current triage

Generated from `edition/patterns/sufficient-candidates.v1.json`:

| Status | Entries |
|---|---:|
| Candidate for independent review | 145 |
| Needs a deeper dedicated section | 0 |
| Needs a dedicated section | 0 |
| **Total** | **145** |

The 145 candidates are the only entries whose current owner unit is dedicated and at
least 120 words. They still need a named independent review before any promotion.


## Review status

Non-human independent-agent reviews are recorded for all 145 candidates:

| Verdict | Entries |
|---|---:|
| Pass | 11 |
| Pass with findings | 134 |
| Reject | 0 |
| Unreviewed | 0 |

All eight originally rejected sections were rewritten. The 2026-10-22 independent agent
re-review found five no longer reject-level: SOA, Priority Queue, Index Table, Shuffle
Sharding and Static Content Hosting. Three remain reject-level: Cell-Based Architecture,
Change Data Capture and Materialized View. A pass-with-findings or reject section is not
promoted until its findings are remediated and re-reviewed. No record here is human
review, owner acceptance, or a sufficient claim.

## Promotion sequence

1. Create dedicated sections for all embedded/shared entries; this is complete
   (145/145 dedicated units).
2. Obtain an independent section review and record reviewer, verdict and findings.
   All 145 now have a non-human independent-agent record.
3. Remediate findings and obtain re-review; rejected sections cannot be promoted.
4. Only then change the validators that currently enforce zero `sufficient` entries,
   and update owner units, registry, delivery evidence and the semantic audit in one
   reviewed change.
5. Human per-page review and owner acceptance remain separate, external gates.

## Current policy blocker

The current validators deliberately reject any `sufficient` claim:

- `scripts/validate_pattern_owner_units.py` requires zero technical/decision sufficient.
- `scripts/validate_delivery_evidence.py` requires zero sufficient summaries.
- `scripts/validate_pattern_semantic_audit.py` requires `owner_acceptance` to remain
  `not-recorded`.

Those checks are an evidence-integrity guard. Removing them without a real review record
would manufacture the claim this protocol is meant to prevent.

## Review record template

```
reviewer:
relationship: did not author the reviewed change
reviewed_at:
entries: [pattern ids]
page_hashes: [exact SHA-256 per page]
checks: [mechanism, invariant, failure, alternative, limits, sources]
verdict: pass | pass-with-findings | reject
findings: [entry, severity, remediation]
```

## Nonclaims

- No entry is promoted to `sufficient` by this document.
- The 14 candidates are not reviewed yet.
- Owner acceptance remains unrecorded.
