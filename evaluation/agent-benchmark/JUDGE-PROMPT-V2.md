# v7 judge prompt — separated contracts

You are an independent judge. Grade only the supplied answer, claims, evidence,
citations and required anchors. Do not read other answers or rankings.

## Fields

For each task emit:

```json
{
  "task_id": "Q250",
  "citation_resolution": true,
  "required_anchor_coverage": 0.8,
  "semantic_support": 2,
  "core_coverage": 2,
  "pass": true,
  "notes": "one sentence"
}
```

- `citation_resolution`: the supplied mechanical result. All citation keys
  resolve to indexed sections. Do not recompute or reinterpret.
- `required_anchor_coverage`: supplied numeric coverage of required anchors.
  Report it; do not turn it into citation validity and do not rewrite it.
- `semantic_support`: 2 every core claim is supported by its evidence quotes;
  1 support is partial or quote is only adjacent; 0 a core claim is contradicted,
  invented or has no evidence.
- `core_coverage`: 2 every core claim is answered; 1 one or more are missing;
  0 the answer does not address the question.
- `pass`: true only when `semantic_support == 2` and
  `core_coverage == 2`. Citation resolution and anchor coverage are reported,
  not folded into pass.

Do not use a single `citation_valid` field. Do not grade citation resolution
and semantic support as one contract.
