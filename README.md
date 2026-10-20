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

## Current editorial candidate — 2026.10.1-rc.1

**[Read the ten-volume manuscript](book/README.md).** All 69 chapters now have individual question-based page routes, rather than uniform one-article wrappers. There are 174 new mechanism/question owners alongside the 69 integrated walkthroughs; retained supporting and case material brings the canonical corpus to 389 documents.

The owner reopened #214 after rejecting the first structural checkpoint as final editorial completion. Version 2026.10.0 and its named snapshot remain historical evidence. The current candidate preserves that content, its identities and source history through [explicit section/fragment mappings](edition/decomposition-manifest.json). It includes seven additional worked explanations and a newly sourced MVCC/snapshot/vacuum page.

[Decomposition decisions and acceptance limits](authoring/CHAPTER_DECOMPOSITION_REVIEW_2026-10-20.md), [current state](authoring/STATE.md) and [edition checks](edition/README.md) distinguish implemented page structure, mechanical validation and remaining substantive acceptance. #214 stays open; page counts and passing tests do not close it. Hosted retrieval/MCP/deployment work remains postponed.

Run `python3 scripts/check_boundary.py` from the repository root. A successful scan detects none of the configured patterns; it does not certify independent origin or semantic correctness.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.
