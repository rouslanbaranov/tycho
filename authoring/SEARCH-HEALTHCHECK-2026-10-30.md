# Search healthcheck — 2026-10-30

Status: local operational check; not CI, production monitoring, human review or
sufficient coverage.

## Check

`scripts/search_healthcheck.py` verifies:

- published index snapshot;
- qrels v4 page/section status, count and snapshot;
- artifact qrels status, count and snapshot;
- BM25 weights;
- MCP default section_rerank and margin.

## Result

```json
{
  "index_snapshot": "e7496a664281afd4a1fff483f68780107a9541e3771a44741322751322dfe8fa",
  "qrels": {"page": 150, "section": 150, "snapshot_match": true},
  "artifact_qrels": {"count": 30, "snapshot_match": true},
  "weights": [10.0, 5.0, 1.0],
  "mcp_defaults": {"section_rerank": false, "margin": 0.05},
  "status": "ok"
}
```

## Decision

Use this as a deployment/readiness check. It is not a quality metric and does
not replace external validation.

## Limits

- Local checkout only; no production monitoring.
- AI qrels; no human review, CI, owner acceptance or sufficient coverage.
