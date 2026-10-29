---
metadata_version: 1
id: "tycho.page.870e64da1f925c52109a602440048603"
kind: "page"
parent_id: "tycho.chapter.6006603befaacfc1baadc486a0f7007a"
canonical_path: "book/volumes/v12-modeling-simulation-and-decision-validation/c01-foundations/stock-and-flow-vs-stock-to-flow.md"
title: "Stock-and-flow modeling versus stock-to-flow shorthand"
topic_ids:
  - "system-dynamics"
  - "simulation"
perspectives:
  - "architecture"
  - "evaluation"
summary: "Stocks accumulate; flows are rates; units and conservation decide coherence."
route_hints:
  questions:
    - "What distinguishes a stock from a flow in an architecture model?"
    - "Which unit and conservation errors invalidate a backlog model?"
  prerequisites: []
  related_ids:
    - "tycho.page.d860bc57cdfe6c6163912819f7679d17"
    - "tycho.page.c264e48a38af3148eff0c87a3b98a8dd"
  excludes:
    - "No production measurement, independent review or owner acceptance is asserted."
  keywords:
    - "stock"
    - "flow"
    - "accumulation"
    - "conservation"
    - "system dynamics"
evidence_scope:
  source_ids:
    - "src.mit-esd-system-dynamics"
    - "src.sargent-vv"
  claim_ids: []
  status: "source-linked"
  notes: "Page-local source records and limits; not independent review."
content_review:
  status: "self-checked"
  reviewed_at: "2026-10-29"
  reviewer: "DeepSeek Harness authoring agent"
  proof_uri: null
authored_at: "2026-10-29"
updated_at: "2026-10-29"
source_inspection_date: "2026-10-29"
content_verified_at: null
---

# Stock-and-flow modeling versus stock-to-flow shorthand

**Question.** What is the difference between a stock and a flow, and why does conflating
them produce a model that cannot conserve its own quantities?

**Short answer.** A stock is an accumulation at a point in time. A flow is a rate over an
interval. A model is coherent only when every state variable has a stock unit, every rate
has a per-time unit, and the integration step preserves the accounting identity. The phrase
"stock-to-flow" is useful only as shorthand for a ratio of two different quantities; it is
not a license to divide a level by a rate and call the result a time.

## Why the distinction matters

A backlog is a stock measured in requests. An arrival rate is a flow measured in requests
per second. A service rate is another flow. The change in backlog over a small interval is
the difference between the two flows:

    backlog(t + dt) = backlog(t) + arrivals(dt) - completions(dt)

If a diagram labels both the backlog and the arrival rate as "requests", the model has lost
its units. A reviewer cannot tell whether a value of 20 means twenty waiting requests or
twenty requests arriving each second. The first is a state; the second is a rate.

The MIT system-dynamics lectures make the same point in hydraulic terms: stocks are
accumulations, flows are rates, and stocks integrate their flows. A stock provides memory
and inertia because it accumulates past inflows. That is why a queue can remain long after
the arrival rate has fallen, and why a service that looks fast in a single request can still
have a growing backlog.

## Units, conservation and the integration step

A stock-and-flow model has three unit rules:

1. Each state variable carries a stock unit, such as requests, records or messages.
2. Each flow carries that unit divided by time, such as requests per second.
3. Each parameter that multiplies a flow carries the reciprocal unit or a dimensionless
   factor.

The accounting identity must hold at every step, not only at the end:

    offered = completed + rejected + backlog

If the identity fails, the model is creating or destroying work. A tolerance is acceptable
for floating-point arithmetic; a persistent gap is a modelling defect. The V12 order-intake
model checks the identity at every step and refuses a negative backlog.

The integration step matters. A large step can admit a whole interval of arrivals at once,
serve more than the available backlog, and produce a negative stock. A small step costs
runtime but keeps the fluid approximation stable. The V12 model uses a fixed 0.1-second step
and asserts non-negativity after every update. The step is part of the model contract, not a
private implementation detail.

## Feedback, delay and nonlinearity

A stock-and-flow model becomes interesting when flows depend on stocks. A service that
scales capacity with backlog creates a balancing loop. A queue that attracts more work
because it advertises low latency creates a reinforcing loop. A delay between a capacity
decision and available capacity can produce oscillation even when every individual decision
is locally reasonable.

The MIT lectures describe dynamic complexity as feedback, nonlinearity, history dependence,
adaptation and counterintuitive behavior. Those are reasons to simulate, not reasons to
trust a simulation. The model still needs a boundary, a purpose and a validity limit.

## The "stock-to-flow" shorthand error

Consider a statement such as "the system has 20 requests per second of backlog". It mixes a
rate with a level. A correct statement is either "the backlog is 20 requests" or "the arrival
rate is 20 requests per second". A ratio can be meaningful, for example backlog divided by
throughput gives an approximate time in system under Little's law. But the ratio has a time
unit only when the numerator is a stock and the denominator is a flow in the same unit.

The shorthand becomes dangerous when it is used to compare candidates. Candidate A may have
a smaller backlog but a larger arrival rate; candidate B may have a larger backlog but a
smaller arrival rate. Comparing the raw numbers without units can reverse the conclusion.
The V12 decision record keeps the metric identifiers and units in the scenario contract and
computes ratios only after the units are explicit.

## A worked order-intake example

The V12 order-intake model has three stocks and three flows:

- backlog (requests): admitted work not yet served;
- completed (requests): cumulative served work;
- rejected (requests): cumulative refused work;
- arrivals (requests/second): offered work;
- service (requests/second): capacity-limited completion;
- rejection (requests/second): offered work that cannot be admitted.

The baseline scenario offers 20 requests per second for 3,600 seconds with a 300-second
warmup. Twelve servers each handle 0.5 seconds of work, so the service capacity is 24
requests per second. The model reports a throughput of 20 requests per second, zero
rejection, zero backlog and a server utilization of 0.833. The saturation scenario offers
30 requests per second with an admission capacity of 80 requests. It reports 0.8 success,
0.2 rejection, a 77.6-request average backlog and a 24-request-per-second throughput. The
conservation identity holds in both runs.

These numbers are synthetic. They demonstrate that the model respects its declared capacity
and admission rules; they do not describe a real intake system.

## Where the model fails

- **Unit collapse.** A stock and a flow share a label. The model becomes dimensionally
  meaningless.
- **Hidden stock.** Work waiting in a database, a client retry buffer or an operator queue
  is omitted. The visible backlog looks stable while total work grows elsewhere.
- **Unbounded flow.** A service rate is treated as infinite because the server is "fast".
  The backlog then drains at an impossible rate.
- **Double counting.** A retry creates a second request in the model but the same business
  request in reality, so success and cost are inflated.
- **Step-size artifact.** A coarse step produces overshoot or negative stock, and the
  analyst reports the artifact as behavior.

Sargent's validation vocabulary helps separate these failures. A unit or conservation
failure is a model-verification problem. A hidden stock or an omitted boundary is a
conceptual-model validity problem. A mismatch between the model's arrival rate and a
measured rate is a data-validity problem. They require different evidence.

## Evidence ledger

- MIT ESD.00 lectures 2-4 (source src.mit-esd-system-dynamics; see the reading ledger)
  supports stocks as accumulations, flows as rates, integration, feedback and delay.
  It does not establish any V12 parameter, run or real-system behavior.
- [Sargent, WSC 2011](https://informs-sim.org/wsc11papers/016.pdf)
  supports verification versus validation, data and conceptual-model validity.
  It does not establish a V12 model's validity.

Both sources were read for method vocabulary. The V12 reading ledger records the exact
units, hashes and omissions.

## Navigation

- Parent: [V12/C01 - Foundations](../README.md)
- Next: [Model scope, boundary and abstraction](model-scope-and-abstraction.md)
- Related: [Queue and resource models](../c03-deterministic-and-des/queue-and-resource-models.md)
