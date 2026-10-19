# M9 E16-08 — Primary-Sourced Authority-Cutover Contrast: Stripe vs Meta

**Checked 2026-10-19**, publicly accessible original first-party engineering reports. This is an **author-led source-specific quality pass**, NOT an external independent reviewer verdict, source-code audit or production benchmark.

## Two real organizations, different state machines

| | Stripe ST01 | Meta ME03 |
|---|---|---|
| Original | Jacqueline Xu Atlas, [*Online migrations at scale*](https://stripe.com/blog/online-migrations), **2017-02-02** | Zihao Tao et al., [*Migrating Data Ingestion Systems at Meta Scale*](https://engineering.fb.com/2026/05/12/data-infrastructure/migrating-data-ingestion-systems-at-meta-scale/), **2026-05-12** |
| Legacy responsibility | Subscription representation embedded on Customer records | Customer-owned CDC ingestion jobs loading MySQL-backed warehouse data |
| Phase 1 | Dual-write Customer + new Subscription table, lazy and offline backfill | Run replacement ingestion as shadow to isolated table; compare counts/checksums, landing time, resource usage |
| First authority shift | **Read** traffic to new table after GitHub Scientist comparison | **Reverse shadow:** new job writes *production* table, old job writes shadow table |
| Subsequent state | Migrate **write** paths to new table, while keeping old representation consistent during transition | Continue comparisons and backfill **after** new job becomes production, old job ready for fast rollback |
| Removal | Remove old writes and stale Customer subscriptions field | Remove old shadow job **only after** stable reverse-shadow criteria |
| Failure oracle | Semantically equivalent subscription reads and mutation-path behavior | Ingestion counts/checksum per partition + no landing latency/resource regression and extra critical-table checks |
| Containment | Scientist discrepancy alerts and incremental code-path rollout | Flag unsafe CDC delta/target partitions, stop delta landing, repair/backfill and rollback |
| Source observation | No universally transferable p99 result in article | Publisher reports 100% migrated workload at publication; not independent mathematical proof of no data loss |

## Exact source anchors and a substantive gap fixed

- **Stripe, 'A pattern for online migrations'** and **'Part 1: Dual writing' → 'Part 4: Removing old data'** state dual-write → migrate all reads → migrate writes → remove old data. Scientist checks the behavioral read path with the old path continuing to serve until confidence is reached.
- **Meta, 'The Migration Lifecycle' / 'Phase 1: The Shadow Phase'**: old writes consumer production table while new writes shadow; row-count/checksum, landing latency and resource gates must pass.
- **Meta, 'Phase 2: The Reverse Shadow Phase'**: after promotion the *new* job writes production while the *old* job writes shadow. Both remain running, allowing ongoing comparison and quick rollback without reconstructing old job configuration.
- **Meta, 'Phase 3: Migration Cleanup'**: remove legacy job after stable observation.
- **Meta, 'Stopping the Bad Data Propagation Quickly During Rollback'**: CDC deltas and target partitions can recursively carry bad prior data; partition metadata allows stopping unsafe deltas and reverting to a previous target plus later valid deltas. The source also describes full-dump backfills for repair.
- **Meta, 'Planning With Limited Capacity'**: resource-constrained migration batches and known-defect exclusion were deliberate design features, not merely an implementation detail.

**Detected source-to-book gap:** the earlier Tycho Meta case stopped its diagram at a generic 'controlled active-job cutover', omitting the **reverse-shadow authority swap**, CDC partition quarantine and limited-capacity batching explicitly described in the first-party publication. These details materially affect reversibility, safety and applicability. This source-review wave updated that case and the cross-company migration playbook.

## Prohibited conclusions / remaining review

Stripe did not use Meta's reverse-shadow CDC job swap, and Meta's ingestion migration does not demonstrate Stripe's subscription-specific Scientist protocol. Neither report establishes a universal migration recipe; equality of row counts or even checksums is not a proof of arbitrary semantic integrity. Source-publisher metrics and migration-completion statements are company-reported, not replicated. No original diagrams, internal code, or long excerpts were copied. Independent review of the revised pages and real-case behavior tests remain outstanding under [#121](https://github.com/rouslanbaranov/tycho/issues/121).

**Related documents:** [Stripe case](../../book/cases/stripe-online-subscriptions-migration.md), [Meta case](../../book/cases/meta-ingestion-shadow-migration-lifecycle.md), [migration decision guide](../../book/cases/decisions/data-migration-correctness.md).
