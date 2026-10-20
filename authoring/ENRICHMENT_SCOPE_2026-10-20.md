# Owner-authorized content enrichment and critical coverage gaps

Date: 2026-10-20. Refs #214. Baseline: `558ccf87f0648af6888057665fc64cd5617eab87`. Candidate: **2026.10.1-rc.2**.

## Authorization and purpose

The owner explicitly authorized all proposed critical-topic additions and enrichment, with continuous execution rather than intermediate approval stops. This is a controlled pass over identified gaps, not an automatic rewrite or a word-count target. All explanations use independently public primary evidence and original fictional scenarios.

Audience: architects, implementers, reviewers and agents making bounded design decisions. Completion means a question has assumptions, a mechanism, a worked normal/failure/recovery argument, alternatives, scoped evidence and an explicit acceptance case. It does not mean every product variant has been researched.

## Gap-to-owner contracts

| Gap | Priority | Canonical owner | Implemented writing delta | Acceptance question |
|---|---|---|---|---|
| Network request path | critical | [c08/README.md](../book/volumes/v08/c08/README.md) | New chapter with four mechanisms | Explain endpoint churn, uneven request costs, GOAWAY, hop trust and private edge caching without inferring rollback or authorization from transport. |
| Object storage and large payloads | high | [c08/README.md](../book/volumes/v05/c08/README.md) | New chapter with three mechanisms | Resolve interrupted transfer, verified publication and cleanup races using exact object and operation identities. |
| Leases and distributed authority | critical | [c02/leader-recovery.md](../book/volumes/v04/c02/leader-recovery.md) | Deepened existing owner | Reject an old owner's delayed write at the destination after takeover; explain token/restore and external-effect limits. |
| Clock domains and deadlines | critical | [c01/causal-order.md](../book/volumes/v04/c01/causal-order.md) | Deepened existing owner | Preserve one deadline budget across hops and explain why local monotonic readings do not establish global order. |
| Deletion and recovery lifecycle | high | [c06/migration-retirement.md](../book/volumes/v05/c06/migration-retirement.md) | Deepened existing owner | Prevent a retired entity from reappearing through delayed replay, a projection or a restored older backup. |
| Jobs, timers and workflow upgrades | high | [c06/workflow-failure.md](../book/volumes/v04/c06/workflow-failure.md) | Deepened existing owner | Distinguish missing/duplicate launches, durable intent, quarantined work and replay-compatible upgrades. |
| Keys, permission and revocation | high | [c05/object-credentials.md](../book/volumes/v09/c05/object-credentials.md) | Deepened existing owner | Distinguish planned rollover from compromise and show what cached credentials can do while authority is unavailable. |
| Rate and fairness budgets | high | [c05/admission-resource.md](../book/volumes/v07/c05/admission-resource.md) | Deepened existing owner | Compute scoped work-unit budgets and explain global overshoot and fairness during scale/outage. |
| API concurrency and traversal | high | [c05/version-compatibility.md](../book/volumes/v02/c05/version-compatibility.md) | Deepened existing owner | Resolve conditional-write races, changing list membership, cursor access and repeated callbacks. |
| PostgreSQL operational mechanisms | high | [c02/storage-workload.md](../book/volumes/v05/c02/storage-workload.md) | Deepened owner plus replica-recovery.md | Explain deadlock retry, old snapshots, concurrent index failure, lag/backlog and retained WAL under PostgreSQL 17. |
| Kafka external effects and replay | high | [c07/offsets-effects.md](../book/volumes/v04/c07/offsets-effects.md) | Deepened existing owner | Trace crash/rebalance/retention expiry without treating Kafka transactions as external SQL atomicity. |
| Migration reconciliation and repair | high | [c05/rollback-data.md](../book/volumes/v10/c05/rollback-data.md) | Deepened existing owner | Detect equal-count loss/duplication, match comparison boundaries and authorize guarded repair before cutover. |
| Time, numeric and text representation | high | [c01/relational-invariants.md](../book/volumes/v05/c01/relational-invariants.md) | Deepened existing owner | Preserve civil time, unit/rounding and equality/order meaning across APIs, storage and migration. |

PostgreSQL replica-specific enrichment is also in [replica recovery](../book/volumes/v05/c02/replica-recovery.md). The new chapter landings own the reading routes; existing introductions link to the newly deepened questions. No other page is certified as sufficient simply because this pass leaves it unchanged.

## Evidence and source boundaries

[Selected inspection records](../sources/enrichment-inspections-2026-10-20.json) identify 25 public documents, exact version/reading scope and non-execution limits. Twenty-two new public source records are admitted; three existing IDs are reused. The legacy register's entry-inspection enum is retained; the dated inspection record and page-local ledgers state the actual selected text read. No full documentation tree or paid book was read.

Reference behavior is pinned to PostgreSQL 17, Kafka 4.1, etcd 3.6 and the named RFCs where applicable. Living documentation is dated and scoped, not silently treated as immutable. An attempted Envoy documentation retrieval failed and supports no new claim.

All numeric workloads, epoch sequences, state machines, protocols and failure matrices are original synthetic reasoning. Product statements are published evidence, not local reproduction. Existing waiver/cancellation dispositions remain unchanged.

## Preservation and structural extension

The original 69 accepted manuscripts and their 739 split source blocks remain unchanged. All 389 existing document IDs remain. Add two chapters (V05/C08 and V08/C08), seven technical pages and nine opaque document identities. The candidate therefore has **10 volumes, 71 chapters and 398 canonical documents**. Twelve existing mechanism pages are deepened outside conserved source blocks; eleven existing introductions gain explicit routes.

The [enrichment manifest](../edition/enrichment-manifest.json) records the nine additions and byte-level insertion boundaries for the twelve deepened pages. Removing only each registered insertion reproduces its exact baseline page. The earlier migration and split manifests remain historical contracts; no baseline identity is reassigned or source payload rewritten.

## Review and validation state

Writing and selected-source review: **author self-review**, not independent acceptance. Available in-process checks and their actual results are recorded in [the validation report](ENRICHMENT_VALIDATION_2026-10-20.md).

The execution environment is unavailable. Python premerge, strict schema/edition/conservation tests, the new adversarial tests and Mermaid parsing **have not been run on this candidate**. Previous candidate test totals do not transfer. Keep the PR draft and #214 open until the required integration checks and substantive review are completed. No hosted service, benchmark or runtime experiment is claimed.

## Remaining questions

A particular DNS/proxy/CDN, object-store versioning/capability implementation, key service, workflow SDK or production rollout requires exact further product evidence. The pages explain how to make those decisions and when evidence is insufficient; they do not claim all implementation recipes are complete. Existing retrieval/MCP/deployment work remains behind final book acceptance.
