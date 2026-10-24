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
- **src.citus** - Concepts (including query execution) plus distribution
  column; read 2/2; complete-scoped.
  R117 and R122 accepted.
- **src.temporal** - Workflow execution, patching, activities, versioning;
  read 4/4; complete-scoped. R102, R106, R125, R126 accepted.
- **src.kafka** - Consumer config, design, producer config; read 3/3;
  complete-scoped. R094, R123, R124 accepted.
- **src.lucene** - Documentation overview, demo API, core API and
  queryparser API; read 4/4; complete-scoped. R127 accepted.
- **src.nats** - JetStream concepts including Streams and Consumers;
  read 1/1; complete-scoped. R128 accepted.
- **src.owasp-asvs** - ASVS 5.0 chapters V1-V5; read 5/5;
  complete-scoped. R129 accepted; V6-V17 outside scope.
- **src.continuous-delivery-book** - blocked-full-text; no lawful
  full text; landing/preview is not evidence.

## Batch 13

The OpenTelemetry scope is the first execution of this plan: R116 read the
Signals index; R118-R121 read Traces, Metrics, Logs and Baggage. All four
records passed parent validation; src.otel is **complete-scoped**; the
landing count dropped by one. It does not become a complete read of every
OpenTelemetry page.

## Counts are not moved by partial units

Current canonical ledger: 130 records (106 full, 3 partial, 19 blocked, 2
excluded); 130 landing-only sources. R116/R117 are partial and do not reduce
that count. Only a completed scope does.

## Scope decisions

No open scope decisions remain for the eight planned sources. ASVS is bounded
to V1-V5; Continuous Delivery is blocked because no lawful full text was
available. Further sources outside this plan still require their own units.
