# Manual RBAC review hand-off

Use this when the local Codex and DeepSeek reviewers stall. Give the prompt below
to a fresh external AI reviewer from a different vendor. The reviewer must use
read-only access and must not see this authoring conversation.

## Bounded inputs

- Repository: `/Users/rbaranov/Projects/tycho`
- HEAD: `79439b351958ebade9413fa759d5ad062252d551`
- Scope: `tycho.pattern.rbac-abac`
- Owner units SHA-256: `c79a697c8ef3e7f7e08630136a792c2fcabccdfbd8bf4a8fe414592c09092a21`
- Source plan SHA-256: `064fbc67def76b67187af13e1dab0aa306be5fca64328b07694e2f0c769b5f2a`
- Owner page: `book/volumes/v09-observability-security-and-operations/c05-identity-authorization-and-threat-modeling/authorization-policy-and-least-privilege.md`
- Card: `book/volumes/v11-pattern-atlas/c11-security-operations/rbac-abac.md`
- Ledger record: `read.nist-sp-800-162.2026-10-26`

## Exact prompt

```text
You are an independent external AI reviewer from a different vendor than the
authoring agent. Work read-only. Review exactly tycho.pattern.rbac-abac at HEAD
79439b351958ebade9413fa759d5ad062252d551 in /Users/rbaranov/Projects/tycho.
Owner units SHA-256: c79a697c8ef3e7f7e08630136a792c2fcabccdfbd8bf4a8fe414592c09092a21
Source plan SHA-256: 064fbc67def76b67187af13e1dab0aa306be5fca64328b07694e2f0c769b5f2a

Verify all four dimensions and the narrowed decision conditions: owner claim,
binding source/section/quote/revision, source-plan unit and ledger record, and
whether each quote supports the full claim and reason. Check the card, the owner
section, the RBAC-only mechanism, the ABAC invariant, the ACL-context failure,
the identity-ACL alternative and the narrowed good-fit/contraindications. Check
the four dimensions jointly justify the decision without circularity. Check the
current state: partial-bounded coverage, no promotion or owner acceptance.
Review current artifacts only at this exact HEAD.

Return only JSON matching this shape:
{"verdict":"pass|fail","technical":"pass|fail","decision":"pass|fail",
 "entries_reviewed":1,
 "findings":[{"severity":"blocking|major|minor","pattern_id":"...",
   "dimension":"...","path":"...","evidence":"...",
   "required_remediation":"..."}],
 "limits":"..."}

A pass requires no blocking or major finding. Report exact paths and concrete
remediation for any finding. State limits. Do not write, commit or change files.
```

## After the review

1. Save the raw JSON verbatim under `authoring/ai-reviews/`.
2. Add its SHA-256 to `authoring/ai-reviews/README.md`.
3. If pass, restore promotion only through the normal promotion path.
4. Do not treat a pass as owner acceptance or CI.
