# Sufficient-coverage protocol — 2026-10-22

## Status

This is a protocol and candidate triage, not a sufficiency claim. All 145 pattern
entries remain `partial-bounded`; 0 are `sufficient`. No independent per-page review
is recorded for this protocol.

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
| Candidate for independent review | 45 |
| Needs a deeper dedicated section | 21 |
| Needs a dedicated section | 79 |
| **Total** | **145** |

The 45 candidates are the only entries whose current owner unit is dedicated and at
least 120 words. They still need a named independent review before any promotion.

## Promotion sequence

1. Deepen the 56 dedicated-but-short sections and create dedicated sections for the 75
   embedded entries.
2. Recompute the candidate matrix after each family.
3. Send candidates to a reviewer independent of the authoring pass.
4. Record the reviewer, reviewed page hash, verdict and findings.
5. Only then change the validators that currently enforce zero `sufficient` entries,
   and update owner units, registry, delivery evidence and the semantic audit in one
   reviewed change.

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
