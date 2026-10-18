# Pilot P01 — Workload boundaries and Little's Law

**Status:** research contract ready; evidence reading and chapter writing **not performed**. **Execution owner:** issue [#38](https://github.com/rouslanbaranov/tycho/issues/38). **Draft book owner:** V07/C01, initial bounded pages defined in [the book proposal](../../book/PROPOSED-STRUCTURE.md). **Pilot class:** mechanism.

## Decision question and reader

How can a software engineer infer only what is justified about mean in-flight work, response time and completed throughput from a specified arrival/load experiment, and which unknowns prevent a capacity or scaling recommendation?

The reader must distinguish registered users, active users, independent offered arrival processes, completed throughput, in-flight requests, waiting queues, p99 latency and service demand. A request count alone must never select microservices or sharding.

## Bounded reading and provenance to acquire

These are admitted **source pointers**, not claims of completed reading:

- `src.little-law`, Kim and Whitt, *Statistical Analysis with Little's Law*, *Operations Research* 61(4), 2013, DOI 10.1287/opre.2013.1193, public PDF: https://www.columbia.edu/~ww2040/LL_OR.pdf. Examine theorem assumptions, definitions, estimation and transient/finite-window caveats. Pin exact page/section after actual reading.
- `src.k6`, official [Open and closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/), especially closed model, drawbacks, open model, coordinated omission and executor semantics. Record displayed documentation version and access time when researched; do not silently treat rolling `latest` as frozen.
- `src.sre-overload`, official [Handling Overload](https://sre.google/sre-book/handling-overload/). Examine overload/admission and user-visible rejection limits, with explicit chapter section references when reading.

No paid textbook is necessary for the pilot. Independent source statements and Tycho's own conclusions must be attributed separately.

## Research questions / artifact boundaries

1. Define one ingress-to-completion boundary; show offered arrivals, admitted work, completed transactions, queueing and timeout behavior.
2. Give conditional derivation `L = λ × W` using compatible **long-run averages** and units; explain why it is not a formula for peak concurrency or thread/connection pool sizes. Discuss statistical estimation limitations with actual reference support.
3. Model one hypothetical stable 30 completed requests/s case with assumed mean W=0.1s (L=3 average); contrast a burst where offered traffic exceeds sustainable completion and any stable identity assumptions may no longer be appropriate. All numbers **invented**, no benchmark claim.
4. Contrast closed and open arrival-generation modes; name which measured quantities and queues are needed to diagnose overload.
5. Evaluate normal, high-tail, queue growth, rejected traffic and recovery scenarios and identify whether the example is answerable given its evidence.

**Exclusions:** choosing a server framework, asserting service capacities, deriving universal RPS thresholds, benchmark execution, treating p99 as W, implementing retrieval/MCP.

## Delivery

- One to three **real researched pages** under V07/C01 only after source reading; no empty files.
- Direct public citations to exact paper pages/sections and versioned website passages supporting material claims, plus original explicitly synthetic arithmetic.
- A failure/measurement matrix and at least one **insufficient evidence** result for resource sizing.
- Explicit next experiment: controlled open-arrival scenario with well-defined measurement boundaries; hypothetical only until executed.

**Acceptance:** source support verified, calculations checked, conditional theorem boundaries correct, normal/failure/recovery and alternatives explicit, source availability/licensing confirmed, existing CI and manual provenance/link review recorded. **Human review:** not assumed.
