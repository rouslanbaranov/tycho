# External-agent benchmark

This directory holds a 100-question corpus and the telemetry contract for
independent external-agent runs.

## Files

- `corpus.json` — v1 questions and expected evidence.
- `corpus-v2.json` — heuristic core/optional claims and 50/50 split.
- `corpus-v3.json` — AI-curated dev claims; v2 holdout is consumed.
- `AGENT-PROMPT.md` — v2 checklist prompt.
- `AGENT-PROMPT-V3.md` — full v3 prompt for the next holdout.
- `AGENT-PROMPT-V3-CONCISE.md` — concise v3 used by v5.
- `corpus-v6.json` — frozen new holdout; full v3; not executed.
- `telemetry-schema.json` — per-session telemetry and token accounting.
- `logs/` — one JSONL file per agent session (created by the harness).
- `results.json` — harness output after a run.

## Run

```bash
.venv/bin/python scripts/agent_benchmark.py \
  --corpus evaluation/agent-benchmark/corpus.json \
  --agent-command '<external-agent-command>' \
  --judge-command '.venv/bin/python scripts/agent_judge.py' \
  --judge-command-2 '<second-judge-command>' \
  --split holdout --jobs 4
```

Agents must run `agent_session_cli.py describe` before searching (prompt v3).
The agent command receives `TYCHO_TASK_JSON`, `TYCHO_QUESTION`,
`TYCHO_TASK_ID` and `TYCHO_SESSION_LOG` in its environment. It must print one
JSON answer to stdout. The judge receives the task on `TYCHO_TASK_JSON` and
the answer on stdin.

Use `--limit N` for a pilot, `--split dev|holdout` for isolation, and
`--validate-only` to check the corpus. A dual-judge run reports agreement and
uses strict consensus for the pass rate.

## Limits

- The harness does not create independent agents; the caller supplies them.
- The bundled judge is deterministic and rule-based, not semantic.
- Token counts are self-reported unless the agent emits provider usage.
- No human review or acceptance is implied.
