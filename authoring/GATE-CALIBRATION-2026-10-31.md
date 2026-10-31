# Agent evidence-gate calibration — 2026-10-31

Status: AI-adjudicated only. No ranking default change. Not human review, CI or
owner acceptance.

## Problem

The existing model gate on 100 answerable tasks:

- 21/100 false abstention;
- 0/20 off-topic rejection.

It suppressed evidence on normal queries without rejecting unrelated probes.

## Calibration

A simple top-score floor separates the 100-task sample perfectly:

| Feature | AUC | Best threshold | Accept answerable | Reject off-topic |
|---|---:|---:|---:|---:|
| retrieval score | 1.000 | 15.618 | 100/100 | 20/20 |
| coverage | 0.664 | 0.529 | 89/100 | 10/20 |
| margin | 0.785 | 1.827 | 65/100 | 17/20 |

Holdout check on 50 answerable + 20 new off-topic items:

- score floor accepts 47/50 answerable (6% false abstention);
- rejects 20/20 off-topic.

## Implementation

- strict decision: score below 15.618061 abstains;
- model probability remains metadata (model_abstain);
- basis is evidence-score-floor or below-threshold;
- MCP default remains abstain=false; strict mode is now the score floor.

## Effect

| Mode | answerable zero | off-topic abstain |
|---|---:|---:|
| old strict | 21/100 | 0/20 |
| calibrated strict | **0/100** | **20/20** |

Holdout strict: 3/50 false abstention, 20/20 off-topic rejection.

## Limits

- The floor was selected on an AI-labelled sample and checked on a small holdout.
- 3/50 false abstention remains.
- No human review, answer correctness, CI or owner acceptance.
