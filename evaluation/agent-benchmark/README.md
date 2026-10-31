# External-agent benchmark

This directory holds a 100-question corpus and the telemetry contract for
independent external-agent runs.

## Files

- `corpus.json` — 100 questions, expected evidence, criteria weights.
- `telemetry-schema.json` — per-session telemetry and token accounting.
- `logs/` — one JSONL file per agent session (created by the harness).
- `results.json` — harness output after a run.

## Run

```bash
.venv/bin/python scripts/agent_benchmark.py \
  --corpus evaluation/agent-benchmark/corpus.json \
  --agent-command '<external-agent-command>' \
  --judge-command '.venv/bin/python scripts/agent_judge.py' \
  --jobs 4
```

The agent command receives `TYCHO_TASK_JSON`, `TYCHO_QUESTION`,
`TYCHO_TASK_ID` and `TYCHO_SESSION_LOG` in its environment. It must print one
JSON answer to stdout. The judge receives the task on `TYCHO_TASK_JSON` and
the answer on stdin.

Use `--limit N` for a pilot, and `--validate-only` to check the corpus.

## Limits

- The harness does not create independent agents; the caller supplies them.
- The bundled judge is deterministic and rule-based, not semantic.
- Token counts are self-reported unless the agent emits provider usage.
- No human review or acceptance is implied.
