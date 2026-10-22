# Sufficient-candidate review integration — 2026-10-22

> Issue [#306](https://github.com/rouslanbaranov/tycho/issues/306), child of #228. This
> records the integration of the independent agent re-review into the machine-readable
> records. It is not a promotion, human review or owner acceptance.

## What changed

- Added the [independent agent re-review](INDEPENDENT-AGENT-REREVIEW-2026-10-22.md) and its
  [machine-readable audit](../edition/patterns/independent-agent-rereview-2026-10-22.v1.json).
- Updated all 52 re-reviewed records with `re_review.report_path`, `page_sha256`,
  reviewer, reviewed_at, verdict, finding IDs and baseline.
- Corrected `findings` from the cited report sections, resolving F-002.
- Reran `reconcile_sufficient_reviews.py` and `build_rereview_packets.py`.
- Recorded F-001 and F-002 as resolved; F-003–F-022 remain open.

## Post-audit counts

| Measure | Value |
|---|---:|
| Records | 145 |
| Current `pass` | 37 |
| Current `pass-with-findings` | 105 |
| Current `reject` | 3 |
| Re-reviewed records with a separate report | 52 |
| Re-reviewed records without a report | 0 |
| Verdict mismatches against original reports | 34 |
| Original report reject conflicts | 6 |
| Initial pass, zero findings | 4 |
| Audited pass | 33 |
| Audited pass-with-findings | 16 |
| Audited reject | 3 |
| Needs remediation and re-review | 83 |
| Remediated but not re-reviewed | 6 |

The three reject-level entries are Cell-Based Architecture, Change Data Capture and
Materialized View. SOA moved to pass; Shuffle Sharding and Static Content Hosting moved to
pass-with-findings.

## Phase A v2 audit — 2026-10-22

The independent auditor reviewed all 52 Phase A entries at HEAD `86395ec`. Report verdict:
**REVISE**. Recommendation: 38 pass / 14 pass-with-findings / 0 reject; 7 findings
(G-001–G-007). Records are unchanged; no entry is promoted.

G-001 (four duplicated owner sections), G-002 (two long lines), G-003 (original vs
re-review findings counts), G-004 (F-020/F-021 attribution), G-005 (scope-manifest
anchors), G-006 (delivery evidence) and G-007 (unregistered NATS/Fowler claims) are
addressed here. G-007 uses narrowed claims, not new source admission. A delta re-review
of the seven findings is pending; Phase B remains un-reviewed.

## What is resolved and what remains

Resolved metadata findings:

- **F-001:** every one of the 52 records now has a separate re-review report path, page hash,
  reviewer and findings.
- **F-002:** original findings counts are derived from the cited report section.
- **F-007:** delivery evidence rebuilt from the current HEAD; counts 145 cards / 145 units /
  69 owner pages / 33 shared pages; one blocked DDIA unit; owner-confirmed review separated
  from independent editorial review. The validator now rejects a claimed independent review
  and requires the owner-confirmed record.
- **F-003 (source remediation):** a dedicated `src.cell-boundaries` read record, source-plan
  unit and card citation now replace the Deployment Stamps source. The Cell verdict remains
  `reject` pending independent re-review.
- **F-004 (source remediation):** a PostgreSQL logical-replication read record and binding
  now support general log-based CDC; the Debezium outbox unit is retained as a comparison.
  The CDC verdict remains `reject` pending independent re-review.
- **F-005 (source remediation):** a PostgreSQL 18 `REFRESH MATERIALIZED VIEW` read record
  now supports the card; failure/recovery describes refresh locks, the CONCURRENTLY unique
  index and rebuild from base tables. The Materialized View verdict remains `reject`
  pending independent re-review.
- **F-006:** the protocol now records three reject-level entries instead of claiming zero.
- **F-008/F-017/F-019 (card hygiene):** the Read Replicas limit and the Correlation,
  Request-Reply and Deadline labels are corrected in the V11 cards; owner pages are unchanged.
- **F-016/F-018 (owner-page hygiene):** five slash-heading backlinks use the correct
  double-hyphen anchors and the three cited workflow-failure lines are wrapped; four owner
  pages changed and 21 owner-linked records carry a remediation note.
- **F-014/F-020/F-021/F-022 (content hygiene):** Circuit Breaker fallback, Static Content
  Hosting cost/version authority, Shuffle Sharding containment/recovery and the 11 empty
  evidence-scope blocks are now recorded; 14 owner pages changed.
- **F-009/F-010/F-011 (PWF card alignment):** Expand-and-Contract, Event Sourcing and
  Cache-Aside cards now use only owner-supported contraindications, alternatives and failure
  conditions; verdicts stay `pass-with-findings` pending re-review.
- **F-012/F-013 (PWF card alignment):** Negative Caching uses the owner-supported bypass/
  per-principal-key/short-TTL alternative; Process Manager states the routing-slip source
  boundary. Verdicts stay `pass-with-findings` pending re-review.
- **F-015 (duplication):** removed the identified earlier-page repeats from DLQ, Durable
  Subscriber, Feature Flags, Graceful Degradation and Idempotent Receiver; owner-unit quotes
  and terms now match the rewritten text.

Open findings:

- **Blocking:** none open. F-003–F-005 are remediated but still require re-review before
  any verdict change.
- **Major:** none open; all F-001–F-022 findings are resolved or remediated, pending re-review.
- **Minor:** none open; F-008, F-014 and F-016–F-022 are resolved or remediated.

No page, card or `sufficient` state was changed by this integration. The delivery-evidence
artifact and validator were updated for F-007; owner page bytes remain at the audit head.

## Next actions

1. Remediate or explicitly retain the three reject-level entries.
2. Remediate the 16 audited pass-with-findings entries and re-review them.
3. Work through the 83 untouched and 6 remediated-but-unreviewed records.
4. Resolve the F-008–F-022 hygiene findings; F-007 is resolved.
5. Obtain human per-page review and owner acceptance; keep `sufficient` at zero until then.

## Nonclaims

This document does not promote any entry, replace the reviewer, or establish independent
human review or owner acceptance. The audit is an agent review; its limitations remain.
