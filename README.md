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

## Current enrichment candidate — 2026.10.1-rc.2

**[Read the ten-volume manuscript](book/README.md).** This candidate contains 71 chapters and 398 canonical documents. Two new chapters explain network request paths and object storage; twelve existing mechanism pages gain worked failure/recovery reasoning. All prior identities and original source blocks remain.

[Scope and acceptance questions](authoring/ENRICHMENT_SCOPE_2026-10-20.md) describe the additions and source boundaries. **Integration checks are pending:** this candidate has not had a Python or Mermaid run because the execution environment is unavailable. The previous candidate's passing results belong to that earlier tree.

#214 remains open for integration verification and substantive page acceptance. The historical 2026.10.0 snapshot is unchanged; no final release or deployment is claimed.

## Industry-neutral delivery

Describe deployment and compatibility requirements without naming a specific sector or institution. Use neutral descriptions such as `restricted enterprise environments`, `regulated environments`, and `security-constrained deployments`. This applies to docs, prompts, examples, code, filenames, issues and releases; see [governance/INDEPENDENCE.md](governance/INDEPENDENCE.md) and [AGENTS.md](AGENTS.md) for mandatory contributor rules.
