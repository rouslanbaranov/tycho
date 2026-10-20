# Tycho

An independent, self-contained System Design book and planned MCP knowledge service for external AI agents.

Tycho explains engineering principles, architectural trade-offs, failure modes, and practical design reasoning through independently sourced public knowledge and original synthetic examples. It is not a description of any employer's systems.

## Non-negotiable boundary

References to employer-specific documents, sources, source code, internal technology usage, architectural decisions, or component names are strictly prohibited. This includes copied, paraphrased, translated, renamed, anonymized, reconstructed, or indirectly linked material. Employer names and abbreviations must not appear anywhere, including governance, examples, scanner rules, fixtures, or metadata.

Read [the independence policy](governance/INDEPENDENCE.md) before contributing. Every agent must follow [AGENTS.md](AGENTS.md).

## Start here

- [Book mission](book/README.md)
- [Authoring methodology](authoring/METHODOLOGY.md)
- [Current state and next action](authoring/STATE.md)
- [Roadmap](authoring/ROADMAP.md)
- [Knowledge platform and MCP delivery plan](authoring/knowledge-platform-and-mcp-plan.md)
- [Source catalogue](sources/CATALOG.md)
- [Coverage and research questions](sources/COVERAGE.md)
- [Implementation families](sources/IMPLEMENTATIONS.md)
- [Source register](sources/register.json)
- [Research contract template](templates/research-contract.md)

All repository content is written in English. Reading the book must not require access to private repositories, accounts, internal networks, another book, or an external agent service. External citations support verification; essential explanations belong in the book itself. Public source dependencies must be recorded explicitly.

## Current implementation — 2026-10-20

**Canonical current checkpoint:** [status](authoring/STATE.md), [roadmap](authoring/ROADMAP.md), [post-merge reconciliation](authoring/PROJECT_STATUS_RECONCILIATION_2026-10-20.md). The owner confirmed independent substantive/content acceptance of all **69 manuscripts** at `986b1ddbe985079b7c647182fcf1c2fc8911d96c`. PR #218 is merged into main (`f9834ef903fc5808f3a1edede208d82aac08f4e6`); #213 and E14 #15 are completed.

The accepted manuscript includes 29 historical cases and six synthetic playbooks. **[Issue #214](https://github.com/rouslanbaranov/tycho/issues/214) is open and ready** to assemble the real ten-volume/69-chapter/bounded-page edition, coherent navigation and a named release. The [selected outline](authoring/FINAL_TOC_AND_OWNER_BOUNDARIES_2026-10-20.md) remains the edition target.

Strict metadata/schema foundations, stable IDs, source controls, local validators and a complete 136-document offline routing index exist. Hosted ranked/semantic retrieval, MCP, the shared specialist runtime and deployment remain subsequent roadmap work. A curated concept graph is excluded.

The [accepted-head verification report](https://github.com/rouslanbaranov/tycho/pull/218#issuecomment-6294804915) records the owner's 13/13 groups and 215/215 tests PASS; it is pinned to the accepted SHA, not a fresh result for later status changes. No published physical edition or deployed service is claimed.

Run `python3 scripts/check_boundary.py` from the repository root. A successful scan detects none of the configured patterns; it does not certify independent origin or semantic correctness.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.
