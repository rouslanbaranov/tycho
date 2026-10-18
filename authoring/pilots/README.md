# Tycho — first bounded technical research wave

Status: **three research contracts specified, not researched or written**. Portfolio owner: [Issue #26](https://github.com/rouslanbaranov/tycho/issues/26). Complete the three scopes separately under their own feature branches and GitHub Issues.

| Pilot | Type | Canonical proposed book owner | Task | Question and key evidence |
|---|---|---|---|---|
| [P01 — Queueing and demand](P01-queueing-and-workload.md) | Mechanism | V07/C01 | [#38](https://github.com/rouslanbaranov/tycho/issues/38) | Little's Law 2013 paper, Grafana k6 open/closed arrivals, SRE overload; conditional mean-workload reasoning |
| [P02 — Outbox and idempotency](P02-outbox-and-idempotency.md) | Cross-component | V04/C04–C05 | [#39](https://github.com/rouslanbaranov/tycho/issues/39) | Transaction, publication, duplicate side effects and ambiguous acknowledgements |
| [P03 — Rollout and recovery](P03-rollout-and-recovery.md) | Failure/recovery | V08/C04–C07 | [#40](https://github.com/rouslanbaranov/tycho/issues/40) | Compatibility stages, recovery checks, RPO/RTO and a deliberately unanswerable scenario |

## Independence, coverage and stop rules

- Use **only** admitted public primary specifications or source code and original synthetic examples. Initial `sources/register.json` records discovery, not completed page/section reading. Pin versions and exact sections as the work is actually performed.
- Execute one pilot at a time using its issue-specific `feature/TYCHO-<issue-number>-<slug>` branch. Pages must explain mechanisms, assumptions, failure modes and evidence, not merely list resources.
- The selected pilots cover *new-system workload analysis*, *cross-boundary correctness* and a *modernization/transition scenario* without reusing any private system description.
- Across the wave, include both answerable questions with bounded evidence and a **real insufficient-evidence** outcome. In particular, lack of recovery/reconciliation evidence must preclude RPO/RTO guarantees.
- Run current source/independence CI and manually inspect citations, links and technical claims; do not claim JSON Schema or graph validators that are not built. Stage post-merge checks according to each issue's actual artifact.
- Stopping one pilot does not automatically regenerate book/volumes, index, search or knowledge graph. Keep research, validation, deepening and serving independent.

After the pilot wave, refine the generalized applicability and legacy decision templates (#19, #18) from actual technical findings. Planned book routes remain proposals until target files exist.
