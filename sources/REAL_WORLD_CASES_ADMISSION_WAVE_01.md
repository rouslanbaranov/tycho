# M9 / E16-01 — Netflix Source Admission Triage, Wave 01

**Prepared:** 2026-10-19  
**Scope:** Five of the 43 candidates in [the M9 source register](REAL_WORLD_ARCHITECTURE_CASES.md): N01, N02, N05, N06 and N07.  
**Status:** **first-pass verification of public primary-source identity, date and bounded claims**; NOT full completion of E16-01, copyright/license clearance, independent performance validation or publication of finished case-study chapters.

This small wave intentionally exercises the M9 GitHub research → issue-specific branch → source ledger → PR workflow without interrupting the separate original Tycho-book worker. No employer/private materials, code clones, transcripts or copied diagrams were incorporated. Claims below are paraphrased and bound to precise public sections.

## First-pass provenance and attribution

| ID | Original source and status | Publisher / practitioner | Historical date verified | Admission decision |
|---|---|---|---|---|
| **N01** | [Completing the Netflix Cloud Migration](https://about.netflix.com/en/news/completing-the-netflix-cloud-migration) — accessible original article | Netflix About; Yury Izrailevsky, Stevan Vlaovic, Ruslan Meshenberg | **2016-02-12** | **Reference accepted for original attributed analysis**; reproduction rights of figures/text NOT established |
| **N02** | [How Netflix Really Uses Java](https://www.infoq.com/presentations/netflix-java/) — accessible named-engineer talk and transcript, not a company-hosted blog | Paul Bakker, Netflix Java Platform; distributed by InfoQ; [original conference agenda](https://qconsf.com/presentation/oct2023/how-netflix-really-uses-java) | **Talk 2023-10-03**; [InfoQ video release listing: 2024-02-26](https://qconsf.com/videos/oct2023) | **Practitioner reference accepted**, conference transcript not licensed for republication; avoid mixing date of talk and publication |
| **N05** | [Bending pause times to your will with Generational ZGC](https://netflixtechblog.com/bending-pause-times-to-your-will-with-generational-zgc-256629c9386b) — accessible source | Netflix TechBlog; Danny Thomas, JVM Ecosystem Team | **2024-03-06** | **Reference accepted** for reported behavior, not an independently reproduced JVM benchmark |
| **N06** | [Java 21 Virtual Threads — Dude, Where's My Lock?](https://netflixtechblog.com/java-21-virtual-threads-dude-wheres-my-lock-3052540e231d) — accessible source | Netflix TechBlog; Vadim Filanovsky, Mike Huang, Danny Thomas, Martin Chalupa | **2024-07-29** | **Reference accepted** for one demonstrated Java 21 incident; not a fleet-wide prohibition on Loom |
| **N07** | [Zuul 2 — Journey to Asynchronous, Non-Blocking Systems](https://netflixtechblog.com/zuul-2-the-netflix-journey-to-asynchronous-non-blocking-systems-45947377fb5c) — accessible source | Netflix TechBlog; Cloud Gateway Team (named in conclusion) | **2016-09-21** | **Reference accepted** for a historical gateway migration, NOT a general benchmark of reactive Java |

The word **accepted** above means admissible as a linked, attributed public source for **new original Tycho prose**; it does not mean permission to mirror the original source or that all its performance claims have been independently validated. No textual republication rights were inferred from the ability to access the pages. Precise article section names and corroborating first-party conference schedule provide section-level location; any later numerical case-study assertion should carry a corresponding evidence row.

## Bounded claim evidence ledger

| Claim | Reported observation | Location in original source | Version / constraint / uncertainty |
|---|---|---|---|
| N01.1 | August 2008 major database corruption disrupted DVD shipments for **three days**, motivating moving away from vertically scaled single points of failure | N01, opening paragraph | Historical triggering event, **not** a blanket conclusion that relational databases fail |
| N01.2 | Majority of systems (including customer-facing services) migrated before 2015; streaming data-center shutdown completed **early January 2016** | N01, second and third paragraphs | The company describes a **seven-year** transition; do not call it an instantaneous lift-and-shift |
| N01.3 | Netflix rebuilt nearly all underlying technology, monolith to hundreds of microservices, and explicitly rejected simple unchanged-system forklift | N01, final two technical paragraphs | Company architectural account; service counts and present-day topology may differ |
| N02.1 | The 2023 presentation describes Groovy device-specific backends with RxJava/Hystrix fan-out, followed by a schema/federation-based GraphQL path | N02, transcript sections **The Groovy Era**, **Limitations**, **GraphQL Federation** | Old BFF/RxJava parts can coexist for older devices; no universal 'RxJava removed from Netflix' |
| N02.2 | Bakker identifies the GraphQL federated gateway as still using a reactive client, while common domain services do not require bespoke reactive fan-out logic | N02, transcript **What Does that Mean for Our Java Stack?** | **Boundary distinction:** reactive gateway remains; not all components changed execution model |
| N02.3 | At talk date, Netflix reports **~2,800 Java applications**, **~1,500 internal libraries**, mostly Java 17, JDK 21 being tested | N02, transcript **Java at Netflix** / **The Java 17 Upgrade** | Period **October 2023**, not a current fleet inventory or extrapolation to 2026 |
| N05.1 | Netflix reports JDK 21 Generational ZGC default and more than half of critical streaming services running it as of article date | N05, opening paragraphs | **2024-03** source-reported adoption; limited to described subset |
| N05.2 | For a specific worst-case comparison, **non-generational ZGC** cost **36% more CPU than G1**, while the **generational** variant performed nearly **10% better** | N05, **Operational simplicity** | Do not reuse figures as generic global gains; distinguish three distinct collectors |
| N05.3 | For some throughput-oriented bursty workloads G1 did better; a large precompute workload reportedly gained **6–8% throughput** with the *parallel* collector vs G1 | N05, **What workloads weren't a good fit?** | Strong counterexample to selecting ZGC for every JVM; exact workload/env not reproducibly specified |
| N06.1 | Netflix observed intermittent REST-service hangs on Java 21 + Spring Boot 3 + embedded Tomcat after enabling virtual threads; CLOSE_WAIT sockets accumulated | N06, **The problem** / **Collected diagnostics** | One production failure type, not all virtual-thread uses |
| N06.2 | On a **4-vCPU** instance, four pinned virtual threads monopolized four carrier OS threads while waiting in a Brave/Zipkin span-finish locking path, preventing Tomcat's other virtual requests from scheduling | N06, **Why is Tomcat stuck?**, **Who has the lock?** | Specific Java 21 monitor/lock interaction and observability limits; compare later JDK versions before making current claims |
| N07.1 | Netty-based Zuul 2 achieved **persistent-connection scaling**, but no significant *overall* CPU-efficiency win was reported | N07, **Results of Zuul 2 in Production** | The architectural benefit is connection lifetime/scale, not an automatic 10x CPU claim |
| N07.2 | Zuul API-facing CPU-intensive cluster had **no measured efficiency gain**; lower-work logging cluster reported approximately **25% throughput gain** with corresponding CPU-use reduction | N07, **Results of Zuul 2 in Production** | Important nuance missing from blanket 'no efficiency gain'; cluster/workload-specific |
| N07.3 | The migration brought nontrivial complexity in thread locals, blocking dependencies, troubleshooting and testing | N07, last part of **Results of Zuul 2 in Production** | Valid modernization cost, not a universal indictment of Netty |

## Requirements and cautions for authors

1. These are **source-reported statements**. The verification above confirms their presence, provenance, timestamps and appropriate qualification, **not** that Netflix's measurement pipelines have been independently audited.
2. **N02 historical date:** the public original conference agenda confirms **October 3, 2023**; InfoQ's own video-publication calendar lists **February 26, 2024**. Always date architecture claims to the 2023 talk.
3. **N07 corrective nuance:** an overly broad summary of Zuul 2 as 'no efficiency improvement' erases its specific logging-cluster result. The observed outcome **depends on CPU intensity and connection scale**.
4. **N06 version caveat:** a lock/pinning failure in Java 21 cannot be treated as proof that the same root cause persists unchanged in current JDKs. Do not infer rollout, code-level patch or systemwide rollback when the article does not establish it.
5. **N05 three-way comparison:** G1 vs pre-generational ZGC vs Generational ZGC are different choices. A distinct parallel-GC batch result is not a Generational ZGC benchmark.
6. **N01 legacy migration:** costs, regulatory constraints, team size and measured deployment cadence at other organizations may justify a different answer (e.g., modular monolith).
7. **Reuse:** retain original URL and author/title/section pointers. Do not import protected transcript passages, charts, diagrams, images or slide decks without explicit rights. New illustrations must be redrawn independently and factually cited.
8. **Remaining gate:** the other **38** initial candidates still require first-pass identity/date/claim validation. Any subsequently added claims to these first five need their own evidence ledger. Record source access date and publication context as part of any final chapter or structured admission. There is no independently appointed technical reviewer yet.

## Proposed mapping to future Tycho case chapters

- N01 → cloud migration and architecture-state transition; negative contrast with Shopify modular monolith.
- N02 → JVM/platform convergence and device API redesign; RxJava-to-GraphQL federation decision.
- N05 → workload-shaped JVM GC selection and tail amplification by retries; include throughput countercase.
- N06 → production failure from virtual-thread pinning, JVM observability, rollback/safety gates.
- N07 → blocking-to-event-loop migration with per-workload CPU and connection results.

This is **not** a new chapter series. Actual pages remain assigned to E16-02..04 after enough admitted evidence; avoid duplicating canonical technical material from E14.

## Wave 01 quality/status checkpoint

- Initial registered source candidates: **43**
- Accessed and reviewed for first-pass provenance, historical date and bounded claims: **5**
- Other candidates not yet reviewed in this wave: **38**
- First-pass acceptable public reference candidates: **5**, with no bulk reuse permissions asserted
- Rejected or dead URLs observed in this slice: **0**
- Finished Tycho case-study chapters from this wave: **0**
- Production benchmarks reproduced, copyrighted diagrams imported, or independent expert reviews performed: **0**
- Issue E16-01 **remains open** pending all-source admission and full supporting evidence, licensing and exact-claim gates.
