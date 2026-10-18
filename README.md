# Tycho

An independent, self-contained System Design book for humans and AI agents.

Tycho explains engineering principles, architectural trade-offs, failure modes, and practical design reasoning through independently sourced public knowledge and original synthetic examples. It is not a description of any employer's systems.

## Non-negotiable boundary

References to employer-specific documents, sources, source code, internal technology usage, architectural decisions, or component names are strictly prohibited. This includes copied, paraphrased, translated, renamed, anonymized, reconstructed, or indirectly linked material. Employer names and abbreviations must not appear anywhere, including governance, examples, scanner rules, fixtures, or metadata.

Read [the independence policy](governance/INDEPENDENCE.md) before contributing. Every agent must follow [AGENTS.md](AGENTS.md).

## Start here

- [Book mission](book/README.md)
- [Authoring methodology](authoring/METHODOLOGY.md)
- [Current state and next action](authoring/STATE.md)
- [Initial roadmap](authoring/ROADMAP.md)
- [Source register](sources/register.json)
- [Research contract template](templates/research-contract.md)

All repository content is written in English. Reading the book must not require access to private repositories, accounts, internal networks, another book, or an external agent service. External citations support verification; essential explanations belong in the book itself. Public source dependencies must be recorded explicitly.

## Current implementation

This initial scaffold establishes governance, authoring rules, a source-register format, and a limited boundary scan. No technical chapters have been researched or validated. Metadata schemas, generated indexes, graph validators, and retrieval evaluation are planned, not implemented.

Run `python3 scripts/check_boundary.py` from the repository root. A successful scan detects none of the configured patterns; it does not certify independent origin or semantic correctness.
