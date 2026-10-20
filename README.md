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

## First Markdown Edition — 2026.10.0

**[Read the ten-volume book](book/README.md).** The edition has **69 primary chapters**, their 69 bounded technical pages, and a linked applied layer of 29 historical cases and six synthetic playbooks. Original supporting essays remain available. The complete canonical corpus contains **215 documents**.

[Edition scope, migration and reproducible checks](edition/README.md) and the [frozen inventory](edition/inventory.json) record the publication boundary. All 136 original document identities are retained; 79 new volume/chapter entities have separately recorded IDs. The technical manuscripts retain their owner-confirmed #213 acceptance; new landing syntheses are editorially self-checked.

[Current state](authoring/STATE.md) and [roadmap](authoring/ROADMAP.md) distinguish this readable Markdown edition from later retrieval/MCP/deployment work. No hosted service or new technology benchmark is claimed. Curated concept-graph infrastructure remains excluded.

Run `python3 scripts/check_boundary.py` from the repository root. A successful scan detects none of the configured patterns; it does not certify independent origin or semantic correctness.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.
