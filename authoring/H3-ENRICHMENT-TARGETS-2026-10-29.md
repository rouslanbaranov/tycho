# H3 enrichment targets — 2026-10-29

Status: read-only enrichment targeting. Not a quality, sufficiency, review or
content-change decision.

## Snapshot

- H2 sections: 2328
- H2 with H3: 228
- H2 without H3: 2100
- Pages without H3: 239
- Orphan H3: 0

## Highest-count pages without H3

| Page | Missing H2 |
|---|---:|
| book/cases/shopify-packwerk-boundary-evolution.md | 13 |
| book/cases/uber-mezzanine-pg-to-schemaless.md | 13 |
| book/cases/netflix-casspactor-shadow-migration.md | 12 |
| book/cases/stripe-online-subscriptions-migration.md | 12 |
| book/cases/uber-cinnamon-admission-and-fairness.md | 12 |
| book/cases/airbnb-jvm-monorepo-bazel.md | 11 |
| book/cases/decisions/build-delivery-migration.md | 11 |
| book/cases/decisions/data-migration-correctness.md | 11 |
| book/cases/discord-cassandra-scylladb-messages.md | 11 |
| book/cases/discord-search-index-cells.md | 11 |
| book/cases/netflix-cassandra-dynamic-time-series-splits.md | 11 |
| book/cases/netflix-java-platform-convergence.md | 11 |
| book/cases/shopify-helix-checkpoint-gated-native-migration.md | 11 |
| book/cases/uber-mysql-to-myrocks.md | 11 |
| book/cases/decisions/agentic-migration-safety.md | 10 |

The complete top-50 target grouping is reproducible with:

```sh
python3 scripts/h3_coverage.py --targets
```

## Use

Use this list to prioritize nested-heading enrichment where H3 parent-aware
retrieval can actually apply. Do not treat H2 count as a quality or coverage
judgment; most sections are intentionally flat.
