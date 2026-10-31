# External-agent MCP drill-down — 2026-10-31

Status: AI sessions and AI judge. Not human review, CI or owner acceptance.

## Product model

The target is not one-shot recall. The target is: a search provides good entry
points; the external agent chooses relevance, follows pages/sections, refines
queries and assembles a picture across MCP calls.

## Sessions

Four complex questions, each answered through the read-only CLI:

| Task | Search | Page | Read | Outline | Failed | Steps |
|---|---:|---:|---:|---:|---:|---:|
| S1 outbox/idempotency/replay | 12 | 2 | 13 | 1 | 4 | 28 ok |
| S2 invalidation/stampede/stale | 15 | 2 | 13 | 1 | 4 | 31 ok |
| S3 queueing/admission/shedding | 6 | 8 | 11 | 1 | 6 | 26 ok |
| S4 schema/snapshot/migration | 5 | 9 | 20 | 0 | 0 | 34 ok |

Judge result: **4/4 answer_support 2**, **4/4 coverage 2**, **4/4
citation_valid**, **4/4 drill_down_appropriate**.

- 35 cited sections, all valid and read;
- 23 distinct pages;
- 127 session steps reported by the sessions;
- S4 had zero failed CLI calls after the fixes.

## What the sessions demonstrate

- agents found entry points with 3-15 refined searches;
- they followed page and section maps into multiple volumes;
- they used outline and section reads, not one large response;
- all answers required synthesis across pages;
- no answer depended on enumerating every relevant section in one search.

## Dead ends fixed

The CLI initially used stale MCP argument names:

- read/page: max_chars to budget_chars;
- outline: query to topic;
- default --max-chars exceeded the 5000 cap;
- outline --limit exceeded the route cap.

Fixed defaults: 4500 chars, limit 5, optional --offset.

## Limits

- Four tasks only; AI answerers and AI judge.
- Search often returned at most three results, so more calls were needed.
- Long sections cannot be paged; CLI has offset but sessions used a single
  read budget.
- Book evidence is synthetic/proposed where the book says so.
- No human review, production benchmark or owner acceptance.
