# V12 artifact query ranking — 2026-10-30

Status: opt-in artifact lookup fix. AI/self-retrieval diagnostic; not independent
qrels, human review, CI, owner acceptance or sufficient coverage.

## Defect

`include_artifacts=True` returned all 25 V12 artifacts for every query,
regardless of the question. It was a filter-only lookup, not retrieval.

## Change

When no explicit pattern/type filter is supplied, artifacts are filtered and
ranked by query terms over title, summary, questions, keywords, topics and
pattern IDs. Stopwords are removed; at least two meaningful hits are required.
Explicit pattern/type filters keep their previous behavior.

Examples:

| Query | Artifacts returned |
|---|---:|
| matching V12 replay | 0 |
| stock-flow offered work | 5 (was 25) |

## Self-retrieval

Using the 50 artifact questions as queries for their own artifact:

| Metric | Value |
|---|---:|
| top-1 | .32 |
| top-3 | .68 |
| top-5 | .92 |

The low top-1 is expected in part because decision/run/scenario records share
the same questions; this is a diagnostic, not a qrels quality claim.

## Volume-only leak

A volume filter alone also populated all artifacts; that trigger was removed.
Only `include_artifacts`, `pattern_ids` or `artifact_type` populate the payload.

## Decision

- Keep artifact lookup opt-in.
- Do not claim artifact recall from self-retrieval.
- A true artifact qrels is still needed before production acceptance.

## Limits

- Not independent queries; shared questions; no human review or sufficient
  coverage.
- No artifact-level qrels.
