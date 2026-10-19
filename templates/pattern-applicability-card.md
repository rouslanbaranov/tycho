# Pattern applicability card template

Reference: [decision model](../authoring/models/pattern-applicability-card.md), issue #19. Status: draft, not a machine-validated schema.

## Identity
- Stable pattern ID and revision:
- Human name and provisional classification (style, pattern, resilience, data, deployment):
- Existing canonical technical owner and version:
- Source observation date, evidence quality, reviewer status:

## Decision problem and conditions
- Measurable user or operational objective:
- Required workload: offered/admitted/completed traffic, mix, duration, skew and failure case:
- Baseline/modernization boundary and compatibility:
- Nonnegotiable correctness, security, latency, availability and cost gates:
- Unknowns, evidence owners and decision deadline:

## Applicability
| Good-fit condition | Evidence and version | Reason | Validation |
|---|---|---|---|
| Scenario-specific condition | Actual observation or unknown | Causal hypothesis | Discriminating test |

## Contraindications and failure costs
| Hard disqualifier or risk | Observed versus hypothetical | Failure/impact | Alternative |
|---|---|---|---|
| Scenario-specific constraint | Evidence or unknown | Named consequence | Retain, simplify or substitute |

## Trade-off comparison
| Candidate | Workload benefit hypothesis | New failure or operational burden | Migration / rollback gate |
|---|---|---|---|
| Retain or improve existing mechanism | | | |
| Candidate pattern | | | |
| Distinct alternative | | | |

## Falsifiable experiment and rejection
- Hypothesis and control case:
- Controlled offered workload, invariant and version:
- p50/p95/p99, rejected/admitted/completed, resources, cost and failure observations:
- What observation rejects adoption, even if throughput improves:
- Decision: candidate / applicable-under-conditions / contraindicated / insufficient-evidence / not-required
- Required owner, validation and next review trigger:

## Source-to-claim ledger
| Claim | Exact inspected public URL, section, revision, date | Fact / inference / synthetic | Limits |
|---|---|---|---|
| E-01 | | | |

## Verification
- Relative links actually checked:
- Experimental outputs actually reproduced:
- Reviewer identified and actual status:
- No approved review, benchmark, or deployment may be inferred from filling this template.

Pilot example: [synthetic admission-control card](../examples/synthetic-admission-control-card.md).
