# External AI review reports

This directory preserves verbatim reports from independent external AI reviewers.
Every completed review must be saved here; a review without a saved report is not a
completed review.

## Naming

`YYYY-MM-DD-<scope-slug>-<reviewer-slug>.md`

Examples:

- `2026-10-26-full-unit-reading-chatgpt.md`
- `2026-10-26-pattern-atlas-claude-code.md`

The reviewer runs read-only and does not write this file. The author saves the reviewer
output verbatim. Do not edit the report; add corrections as a separate addendum.

## Index

| Date | Reviewer harness / vendor | Scope | Verdict | Report | SHA-256 |
|---|---|---|---|---|---|
| 2026-10-26 | Codex / OpenAI | #535 full-unit reading and 23 removed claims | reject | `2026-10-26-full-unit-reading-codex.md` | `4e9ed912281f84346dfa11caec0a05b50ef613de461443afb662481f37b0eb90` |
| 2026-10-26 | Codex / OpenAI | #535 remediation R-01–R-08 | reject | `2026-10-26-remediation-rereview-codex.md` | `430d30bbb689e5ad15127f7790eb2a0e0cc4b39fd663602ccde854cc7bfbb2f7` |
| 2026-10-26 | Codex / OpenAI | #535 round-3 focused re-review | pass | `2026-10-26-round3-rereview-codex.md` | `b4ecbb26a1eaf395df439d82a98a21c819ea3d4c428818a6338076955c34dbe1` |
| 2026-10-26 | Codex / OpenAI | #540 six-entry sufficient pilot | reject | `2026-10-26-sufficient-pilot-codex.md` | `b755e412cf6de44e58d111448dd2595a228dbd4a133d20087f65ffccd13faaa9` |
| 2026-10-27 | Codex / OpenAI | #540 sufficient pilot remediation R2 | pass-with-findings | `2026-10-27-sufficient-r2-codex.md` | `3997c55722125ca28477b4a0e07feb57437710ed334708595187effb1ded5278` |
| 2026-10-27 | Codex / OpenAI | #540 sufficient R2 residual re-review | pass-with-findings | `2026-10-27-sufficient-r3-codex.md` | `0b1ca9965cc40f8522a8f6994a3bb27ea76c5eb99af1dc56d0957c975d4a718d` |
| 2026-10-27 | Codex / OpenAI | #540 sufficient R3-01 remediation | pass | `2026-10-27-sufficient-r4-codex.md` | `38bf30011abb8b68288b30940411a2f0378741fcc641253002a4358b27bf738a` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 review-ready batch (25 entries) | reject | `2026-10-27-sufficient-batch-review-codex.md` | `3a32b2a96b476c64d12540e33c839669c8b7752addfe50f26c0335488215e71d` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 focused survivors (2 entries) | reject | `2026-10-27-sufficient-survivors-review-codex.md` | `23896ff428ea860da5a556dede13dbed55caf09fcd631ab8ead45d200eddcf13` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 static content hosting round 2 | reject | `2026-10-27-static-content-hosting-review2-codex.md` | `aa5a1550da7dafe2ada45a26093ba8e6b571bffd81c45c79971de18ff4fb1a4f` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 static content hosting round 3 | reject | `2026-10-27-static-content-hosting-review3-codex.md` | `520600735f49e8e434aeb0048a00b5679a795b4c877103c014f4386124ce96f5` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 static content hosting round 4 | reject | `2026-10-27-static-content-hosting-review4-codex.md` | `b531ce8b0146d06973ea677221091782eb45397aeabdc1ff7960c7fe60212e40` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 static content hosting round 6 | pass | `2026-10-27-static-content-hosting-review6-codex.md` | `e4b818e42ba61bc09040b4e9290a7935b32b0dbe47ceaa3a46b93962ee80a814` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 transactional outbox | reject | `2026-10-27-transactional-outbox-review-codex.md` | `35354132fe729ea1eb3c904fa8d164cb48d1b6ab4e99db488b6d223d860fd3c4` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 transactional outbox round 2 | reject | `2026-10-27-transactional-outbox-review2-codex.md` | `d2860eab85d84b5bd7348e31be7e961554854ffaf84225d6a1e3e98f89c70609` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 transactional outbox round 3 | reject | `2026-10-27-transactional-outbox-review3-codex.md` | `ea48fc1c6b0b8ef1e0ddf029be06a5242d0f80c8c4da2fba128d317e1f3eac28` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 transactional outbox round 4 | pass | `2026-10-27-transactional-outbox-review4-codex.md` | `e7d894774c096dcb54a5d1dbdd4817f8d88671c91e6e1f42e88032765b8408db` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 valet key round 3 | reject | `2026-10-27-valet-key-review3-codex.md` | `733227f644caf5e4ae8f846f84b3082b12e50d41204a4135a814263ea72afa92` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 valet key round 4 | pass | `2026-10-27-valet-key-review4-codex.md` | `2aab633fc5a566532cc3973814f5803143cc979368a5ffd5855e22d4cdbe77ff` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 cache | pass | `2026-10-27-cache-invalidation-review-codex.md` | `26323bcdf779dbca8db2f9e4abe439affd94bb24143896d02df314d12b139a0b` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 ttl | reject | `2026-10-27-ttl-expiration-review-codex.md` | `06e0574b1134e12c6549f3725a8022e4cb947ec2029aa64bf92b6c56fc18404b` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar | reject | `2026-10-27-sidecar-review-codex.md` | `cc7208f6df8b790cb73bff93b4fe8e0381cafa9e4b06c3e3c5fae92b092e5bc7` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer | reject | `2026-10-27-anti-corruption-layer-review-codex.md` | `4b29a05eee669687ded6ab84d2ffb2248ec2cc74e188dbbc1569227f9d2419a1` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 dark launching | reject | `2026-10-27-dark-launching-review-codex.md` | `1d757b4448f2711e5cdcb67d987308413f89b3d9fd3d15abc3ca66f4b168a3d9` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 2 | reject | `2026-10-27-anti-corruption-layer-review2-codex.md` | `a437bb9ad9c9073b372540526ccc1c6620539d13133a3dfe4cec57e369feb9fb` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 3 | reject | `2026-10-27-anti-corruption-layer-review3-codex.md` | `368ef64070e82cb0455215fc0baab508d360441ed0e24e3677d750495a871d58` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 4 | pass | `2026-10-27-anti-corruption-layer-review4-codex.md` | `e4c87513e47e5b75442837931e52761c6b1f8ae7825bf78de972b731c14d1338` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 service discovery | reject | `2026-10-27-service-discovery-review-codex.md` | `ff80611cb796877c1a04f57f32c2250436c5a54de1ae20206997d615159da716` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 parallel run | reject | `2026-10-27-parallel-run-review-codex.md` | `d298b3529aa2136b1ad73360cd367bcc6dcf1c86c027bf789d867917e607bf13` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 parallel run round 3 | pass | `2026-10-27-parallel-run-review3-codex.md` | `84904118869e13d928eb699301eb53f4b2360e7b3fde5ef29ff144e0644e67ca` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 async request-reply | reject | `2026-10-27-async-request-reply-review-codex.md` | `05cb7aca247305bab1e5fcb8fefc0c95f347416c0990ea5f99d04b53e58a616c` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 valet key split | reject | `2026-10-27-valet-key-split-review-codex.md` | `382038377705bb9e78168280a292e90ad7bd2358eb22db8b00df518080f78891` |
