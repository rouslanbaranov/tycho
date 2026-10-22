# Sufficient-candidate review reconciliation — 2026-10-22

> Issue [#302](https://github.com/rouslanbaranov/tycho/issues/302), child of #228. This is a
> read-only reconciliation of existing records against their cited reports. It is **not** a
> new review, a sufficiency claim, a promotion, human review or owner acceptance.

## Inputs and method

The reconciliation reads:

- [sufficient-candidates.v1.json](../edition/patterns/sufficient-candidates.v1.json);
- [sufficient-review-records.v1.json](../edition/patterns/sufficient-review-records.v1.json);
- [the batch review](INDEPENDENT-AGENT-REVIEW-BATCH-2026-10-22.md);
- [the sufficient-candidate review](INDEPENDENT-AGENT-REVIEW-SUFFICIENT-CANDIDATES_2026-10-22.md);
- [the sufficient-coverage protocol](SUFFICIENT-COVERAGE-PROTOCOL_2026-10-22.md).

[reconcile_sufficient_reviews.py](../scripts/reconcile_sufficient_reviews.py) parses report
headings and verdicts, matches catalog names exactly or by a unique prefix alias, derives a
remediation state and writes the per-record ledger to
[sufficient-review-reconciliation.v1.json](../edition/patterns/sufficient-review-reconciliation.v1.json).
Input SHA-256 values are stored in the ledger. No record is edited.

## Headline counts

| Measure | Value |
|---|---:|
| Review records | 145 |
| Current verdict `pass` | 51 |
| Current verdict `pass-with-findings` | 94 |
| Current verdicts matching the cited report | 98 |
| Current verdicts mismatching the cited report | **47** |
| Report names matched exactly | 144 |
| Report names matched by unique alias | 1 |
| Records claiming a re-review | 52 |
| Re-reviews with a separate report path | **0** |
| Records with no remediation and no re-review | 83 |
| Records remediated but not re-reviewed | 6 |
| Re-reviewed records with residual findings | 5 |
| Initial pass with zero findings | 4 |
| Promoted after remediation | 47 |

The protocol records **11 pass / 134 pass-with-findings**. The records show
**51 / 94**: +40 pass and -40 findings. That direction is consistent with a later promotion
wave, but the arithmetic is not fully documented: 41 current passes still cite a
`pass-with-findings` report and one current pass cites a `reject`. Only **9 of 51**
current passes are supported by a cited `pass`.

## Report support

| Current verdict | Cited report `pass` | Cited report `pass-with-findings` | Cited report `reject` |
|---|---:|---:|---:|
| `pass` | 9 | 41 | 1 |
| `pass-with-findings` | 0 | 89 | 5 |

The report trail does not support 47 current verdicts. The mismatch is not a schema problem:
the cited report is the evidence attached to the record, and its verdict differs.

## Re-review traceability

All 52 records with `re_reviewed: true` point to their **original** report. The re-review
verdict and findings exist only in the record's `re_review` object; there is no separate
re-review report path, reviewer attestation or page hash in a report document. Of those 52,
47 claim a pass and 5 still carry two findings.

This means the 47 promoted entries cannot be described as independently re-reviewed based on
the cited files alone. The record says so; the report trail does not.

## Reject conflicts

Six records cite a report verdict of `reject`:

| Entry | Current verdict | State |
|---|---|---|
| Service-Oriented Architecture (SOA) | `pass` | promoted after remediation |
| Change Data Capture (CDC) | `pass-with-findings` | residual findings |
| Materialized View | `pass-with-findings` | residual findings |
| Cell-Based Architecture | `pass-with-findings` | residual findings |
| Shuffle Sharding | `pass-with-findings` | residual findings |
| Static Content Hosting | `pass-with-findings` | residual findings |

The protocol says the originally rejected sections were rewritten and re-reviewed. The record
state is consistent with that claim; the cited reports still show `reject`. The provision is
therefore unverified until a re-review report exists.

## Remediation backlog

| Derived state | Records | Meaning |
|---|---:|---|
| initial pass, zero findings | 4 | No remediation needed; still needs human review/acceptance. |
| promoted after remediation | 47 | Record claims pass; re-review report missing. |
| needs remediation and re-review | 83 | No remediation and no re-review recorded. |
| remediated, needs re-review | 6 | Code/prose changed; re-review absent. |
| residual findings after re-review | 5 | Re-reviewed; two findings remain. |

## What cannot be claimed

- That 51 entries are independently reviewed. Only 9 current passes cite a pass report, and
  the 47 promotions lack a re-review report.
- That SOA or the five residual entries passed their cited review.
- That the protocol counts are current.
- That any entry is `sufficient`. The validators that require zero `sufficient` entries
  must stay until a review report and human/owner gate exist.
- That human per-page review or owner acceptance happened. Neither is recorded.

## Next actions

1. Attach a re-review report for each of the 52 re-reviewed records: reviewer, page hash,
   verdict, findings and date, or redo the review.
2. Reconcile the 47 verdict mismatches by correcting the report or the record; do not silently
   edit one side.
3. Remediate the 83 untouched and 6 remediated-but-unreviewed records, then re-review.
4. Resolve the 5 residual-findings entries and the 6 reject conflicts.
5. Obtain human per-page review and owner acceptance.
6. Only then update the protocol, promotion validators and registry in one reviewed change.

## Nonclaims

This document does not promote, reject, rewrite or approve any pattern entry. It records what
the existing files say and where they disagree. A passing script run is not a review event.
