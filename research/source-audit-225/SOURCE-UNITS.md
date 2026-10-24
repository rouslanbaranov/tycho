# Source-unit plan for remaining documentation sets

**Date:** 2026-10-24. **Baseline:** 6754bac6e26faa57d65a301a60be10b3da93f65b.
**Machine-readable plan:** [source-units.json](source-units.json).

## Rule

A source leaves landing-only only when every unit in its declared audit scope is
read and accepted. A page-level record does not by itself complete a multi-unit
source. Scopes are bounded to the units relevant to the book; they are not a
claim that the entire documentation site was read.

## Status

- **src.otel** - Signals index plus four signal pages; read 5/5; complete-scoped.
  R116 and R118-R121 accepted.
- **src.citus** - Concepts, sharding, query execution; read 1/3; in progress.
  Next: resolve sharding/query URLs and read them.
- **src.temporal** - Workflow execution, patching, activities, versioning;
  read 2/4; in progress. Next: activities and versioning.
- **src.kafka** - Consumer config, design, producer config; read 1/3;
  in progress. Next: design and producer config.
- **src.lucene** - Overview, indexing, search; read 0/3; planned.
  Next: resolve indexing/search URLs.
- **src.nats** - JetStream concepts, streams, consumers; read 0/3; planned.
  Next: resolve stream/consumer URLs.
- **src.owasp-asvs** - not bounded; scope decision required.
- **src.continuous-delivery-book** - not bounded; scope decision required.

## Batch 13

The OpenTelemetry scope is the first execution of this plan: R116 read the
Signals index; R118-R121 read Traces, Metrics, Logs and Baggage. All four
records passed parent validation; src.otel is **complete-scoped**; the
landing count dropped by one. It does not become a complete read of every
OpenTelemetry page.

## Counts are not moved by partial units

Current canonical ledger: 121 records (98 full, 3 partial, 18 blocked, 2
excluded); 134 landing-only sources. R116/R117 are partial and do not reduce
that count. Only a completed scope does.

## Scope decisions needed

- **OWASP ASVS:** chapters V1-V14 are too large to claim from the project page.
  Choose a bounded chapter set or leave the source landing-only.
- **Continuous Delivery:** the online book needs an explicit chapter list; the
  landing page is not evidence.
