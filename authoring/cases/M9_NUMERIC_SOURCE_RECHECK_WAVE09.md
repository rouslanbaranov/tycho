# M9 E16-08 — Numeric Claim Re-verification Wave 09 (Airbnb, Discord, Uber)

**Checked:** 2026-10-19, by authoring/research assistant against **three directly accessible original publisher articles** and their named sections. **Disposition:** editorial **source-alignment check** on the listed claims, **not independent human peer review**, measurement reproduction, license certification or present-day architecture inventory. Each item cites public-source prose and carries the publisher's observation window and comparability limits.

## Airbnb — A01 (2025-09-17)

**Original:** Jack Dai, Howard Ho, Loc Dinh, Stepan Goncharov, Ted Tenedorio and Thomas Bao, [*Migrating Airbnb’s JVM Monorepo to Bazel*](https://airbnb.tech/infrastructure/migrating-airbnbs-jvm-monorepo-to-bazel/), sections **Migration in numbers**, **How did we migrate? → Proof of concept**, **Migrating the deploys → Services**, **What did we learn?** and **Conclusion**.

| Claim | Direct article observation | Admissible reading | Reviewer caveat |
|---|---|---|---|
| A01.V09-01 | **4.5 years** total migration | Duration covers build and deploy migration and coexistence | Not implementation lead time for adding a Bazel dependency |
| A01.V09-02 | Local builds/tests **3–5×** faster; IntelliJ sync/development deploy **2–3×** faster | Publisher-reported results for its JVM monorepo | Different user workflows/CI workloads; not a controlled universal speedup |
| A01.V09-03 | Build satisfaction **38% → 68%** | Internal reported satisfaction movement | Not a directly comparable engineering productivity percentage |
| A01.V09-04 | **2–4×** faster initial Viaduct pilot but engineers **did not initially opt in** | Faster execution alone was insufficient: IDE integrations and bugs blocked adoption | Negative outcome must survive summarization |
| A01.V09-05 | Approx. **700** services and **100** startup/integration failures in deployment parity tests | Java reflection/runtime classpath checks uncovered a compile-vs-deploy gap | Not 100 production outages or a Bazel defect rate across all repositories |

**Correction guard:** Avoid saying Airbnb obtained its 3–5× speedup in four months or that service deploy parity automatically followed compilation. Its article explicitly warns against optimizing granularity during migration before compatibility is secured.

## Discord — DI01 (2023-03-06)

**Original:** Bo Ingram, [*How Discord Stores Trillions of Messages*](https://discord.com/blog/how-discord-stores-trillions-of-messages), sections **Our Cassandra Troubles**, **A Very Big Migration**, **Several Months Later…**.

| Claim | Direct article observation | Admissible reading | Reviewer caveat |
|---|---|---|---|
| DI01.V09-01 | **177 Cassandra nodes** at beginning of 2022 → **72 ScyllaDB nodes** | Change in number of message-store nodes for Discord's deployment | Original also specifies ≈**4 TB/node Cassandra** versus **9 TB/node ScyllaDB**: these nodes are not equivalent units |
| DI01.V09-02 | Historical-message read p99 **40–125 ms → ~15 ms** | Publisher's before/after comparison, not a reproducible estimate for a third party | Traffic, hardware, capacity and distribution may differ |
| DI01.V09-03 | Message insert p99 **5–70 ms → ~5 ms** | Different measured operation than historical reads | Do not combine read/insert ranges into one p99 |
| DI01.V09-04 | End-of-migration tombstones delayed last data ranges | Progress marker approaching completion was insufficient | Full equality requires authoritative reconciliation, not success percent alone |

**Correction guard:** Discord's separate 2025 **search indexing** latency improvements are DI02, **not** these DI01 2022 message-store measurements.

## Uber — U06 (2026-04-20)

**Original:** Dhyanam Vaidya, Prathamesh Deshpande, Mike Ma et al., [*How Uber Conquered Database Overload*](https://www.uber.com/us/en/blog/from-static-rate-limiting-to-intelligent-load-management/), sections **Quota-Based Rate Limiting in the Query Engine Layer**, **Cinnamon Replaces CoDel**, **Centralizing Overload Decisions**, **The Payoff: Unified Control, Simplified Load Management**.

| Claim | Direct article observation | Admissible reading | Reviewer caveat |
|---|---|---|---|
| U06.V09-01 | During overload **3,000 → 5,400 average QPS**, company calls this **80% increase** | Before token-bucket control vs Cinnamon/PID on publisher's workload | Not arbitrary-tenant/cluster sustained QPS; workload shape not independently reproduced |
| U06.V09-02 | Upsert **p99 3.1 s → 1.0 s**, company calls this **~70% reduction** | Upsert tail latency under publisher's overload test | Not all request classes or universally applicable SLO |
| U06.V09-03 | Peak goroutines **150,000 → 10,000**, publisher describes ~**93% reduction** | One overload resource-pressure comparison | Scheduler/runtime configuration not public enough to generalize |
| U06.V09-04 | Heap described as **1 GB maximum vs 5–6 GB spikes**, while article labels reduction **~60%** | **Keep the publisher's approximate percent separately from its displayed maxima** | The two raw maxima suggest a different naive arithmetic percentage; the exact aggregation/base used for the reported 60% is unspecified. **Do not reconcile silently or invent a denominator** |
| U06.V09-05 | The early Redis-based stateless query-tier quota did not work well; storage-local overload signals and priority-aware control were adopted | A **documented failed architectural alternative** | API-edge quotas can remain useful for independent contractual/policy goals |

## What was checked; what remains

**Performed:** opened all three first-party HTML publications; read exact sections matching metrics; compared with [Airbnb](../../book/cases/airbnb-jvm-monorepo-bazel.md), [Discord](../../book/cases/discord-cassandra-scylladb-messages.md) and [Uber](../../book/cases/uber-cinnamon-admission-and-fairness.md) case-page claims and the earlier [numeric ledger](../../sources/REAL_WORLD_CASES_NUMERIC_CLAIM_LEDGER.md). Company numbers were **not** recalculated as independently measured gains.

**Findings:** the existing case-page major numbers agree with the primary reports. Two editorial traps need to be retained as explicit caveats: Discord's 177-vs-72 node comparison has different **disk capacity per node**, and Uber's publisher-reported heap percentage is **not transparently derivable from the stated maxima**. These should be first-class source caveats rather than omitted or averaged away.

**Still not performed:** independent qualified peer review, current company topology verification, benchmark replication, source-rights legal signoff, full repository checkout Python suite, production search/MCP result evaluation. Source web content may be revised by its publisher; no content-hash archival of public article bytes was generated. Keep M9 acceptance #121 **open**.
