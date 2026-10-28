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
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer | reject | `2026-10-27-anti-corruption-layer-review-codex.md` | `4b29a05eee669687ded6ab84d2ffb2248ec2cc74e188dbbc1569227f9d2419a1` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 2 | reject | `2026-10-27-anti-corruption-layer-review2-codex.md` | `a437bb9ad9c9073b372540526ccc1c6620539d13133a3dfe4cec57e369feb9fb` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 3 | reject | `2026-10-27-anti-corruption-layer-review3-codex.md` | `368ef64070e82cb0455215fc0baab508d360441ed0e24e3677d750495a871d58` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 anti-corruption layer round 4 | pass | `2026-10-27-anti-corruption-layer-review4-codex.md` | `e4c87513e47e5b75442837931e52761c6b1f8ae7825bf78de972b731c14d1338` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 service discovery | reject | `2026-10-27-service-discovery-review-codex.md` | `ff80611cb796877c1a04f57f32c2250436c5a54de1ae20206997d615159da716` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 parallel run | reject | `2026-10-27-parallel-run-review-codex.md` | `d298b3529aa2136b1ad73360cd367bcc6dcf1c86c027bf789d867917e607bf13` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 parallel run round 3 | pass | `2026-10-27-parallel-run-review3-codex.md` | `84904118869e13d928eb699301eb53f4b2360e7b3fde5ef29ff144e0644e67ca` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 async request-reply | reject | `2026-10-27-async-request-reply-review-codex.md` | `05cb7aca247305bab1e5fcb8fefc0c95f347416c0990ea5f99d04b53e58a616c` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 valet key split | reject | `2026-10-27-valet-key-split-review-codex.md` | `382038377705bb9e78168280a292e90ad7bd2358eb22db8b00df518080f78891` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 valet key after split | pass | `2026-10-27-valet-key-split-review6-codex.md` | `9ae5b68f13ffd8fe47d410bb2010ad4e561aa2848390d3cef59692a2f38dff04` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 ACL after split | reject | `2026-10-27-anti-corruption-layer-split-review-codex.md` | `10d0e227d55b04c9daa5b281d19e0da58bb73758eadcc3fcc552850f3d73321c` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 ACL after split round 4 | pass | `2026-10-27-anti-corruption-layer-split-review4-codex.md` | `2c7c0220f0ca61cf4a75f86fda6edfbfc22e0de5265cd987a503f2d4420e4b90` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 parallel run after split round 2 | pass | `2026-10-27-parallel-run-split-review2-codex.md` | `f4db0f3d67061885e2dc47a743d2dc5a5c6f5d66df3511f8a86e361a1e829dfa` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar | reject |  |  |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar | reject | `2026-10-27-sidecar-review-codex.md` | `bf3cf2331ee6a342a3e3810f803d77ba57f9c963091e84502f05e41e0371980d` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar round 2 | reject |  |  |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar round 2 | reject | `2026-10-27-sidecar-review2-codex.md` | `1cfaefc5bb8b430d7646b4690488d0778a3874a643a7b373f97b75dcf589885c` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 workload identity | reject | `2026-10-27-workload-identity-review-codex.md` | `aaea18396c072a32896cc3f24815f0802b57d534c01a53bb734934b060678ba3` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 workload identity round 2 | reject | `2026-10-27-workload-identity-review2-codex.md` | `020838225bccbf9f3e1ccb027b80d8c50446e0575f2d3b3a82163f48e0b24070` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 workload identity round 5 | pass | `2026-10-27-workload-identity-review5-codex.md` | `e17f5382b3f36b7acda6280a6de38ea6ead21f030de7a3ab2652129c8e0d6d62` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar round 5 | pass | `2026-10-27-sidecar-review5-codex.md` | `dd0ee130dbd4e1d717e833725eb0a71b46fa79634e85c067f5c98c28abd11bc2` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 dark launching | reject | `2026-10-27-dark-launching-review-codex.md` | `750b4f9ad590ce64c5994e79bc0beb77c2ac4c70901bf075487c9bfc2a949fa0` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 dark launching round 2 | pass | `2026-10-27-dark-launching-review2-codex.md` | `12b7e87d9f75bdd85aa84b11e3f6d39074e6b98baed8f8fcdc37ae8c4af5ba64` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 RBAC/ABAC round 2 | reject | `2026-10-27-rbac-abac-review2-codex.md` | `3ee849573c2b9166c84012646c68ae21b6aa7f866afd4cbe001ec26a237e9779` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 RBAC/ABAC round 3 | reject | `2026-10-27-rbac-abac-review3-codex.md` | `5a5e30f7e63a51927012a2a80b3ee99fedd75585b146c0365f69beef3e76a134` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 service discovery round 2 | reject | `2026-10-27-service-discovery-review2-codex.md` | `b9dd6228423a3c728f5127f1ae6d3d6147c8368dfc95562bfde1f5ac2a0297ac` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 async request-reply round 2 | reject | `2026-10-27-async-request-reply-review2-codex.md` | `ccad0f776364db002b9a51e5918c40752fcd286b39ac6dc9630648d63d256098` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 async request-reply round 3 | pass | `2026-10-27-async-request-reply-review3-codex.md` | `8918f85776490abd2ca5015d3c35baebc9d559e185b5026846b11b132aa6562a` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 TTL expiration | reject | `2026-10-27-ttl-expiration-review-codex.md` | `411dab8517b5c729a4fa522e3a3583d0f4f12655bd8a04bde8d06e9f732a72db` |
| 2026-10-27 | Codex / OpenAI (gpt-5.6-sol) | #540 throttling | reject | `2026-10-27-throttling-review-codex.md` | `bf8a49578e37e5634d27a897f8f3519e8dc0b42242976895b6d918bb61e33a8d` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 RBAC/ABAC | pass | `2026-10-28-rbac-abac-review-codex.md` | `e729d03b2f1f81ead2e9d4d9011477ef6392c259f5b8698da37fe37868414371` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 async split | pass | `2026-10-28-async-request-reply-split-review-codex.md` | `59b9b64d0aeed47c31263fe33cab103fa787558d85feb9326aee987d610f8fe9` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 dark split | pass | `2026-10-28-dark-launching-split-review-codex.md` | `a7471e45c8632ed81def3f0a87e38dc049d99236bc2e1cb8fd74cf9b7f671ccd` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 service discovery | pass | `2026-10-28-service-discovery-review-codex.md` | `b0f08b230e052109eef51c2f4b0876234d2b7046417906675d3dbb4b1771447f` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 controlled cutover | pass | `2026-10-28-controlled-cutover-review-codex.md` | `68573a3f0373de47d0e84674fc8c70ffb8ffb3140801f3c154cf8b5c8cd8af30` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 federated identity | reject | `2026-10-28-federated-identity-review-codex.md` | `cbec07e52ae5916242e9f875c20317fe963bb73af1132cd5845ef63e8ddcc5d0` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 request-reply messaging | pass | `2026-10-28-request-reply-messaging-review-codex.md` | `0b87ff932e6ae8287ac6ac710eddad46e743031d064215c4d870dad525bc8dfe` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 workload identity after page change | pass | `2026-10-28-workload-identity-review6-codex.md` | `c7c476c3df3d76f61d2300112454956f370b8ca5f8cde26d96cc2ec8bddf6d66` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 federated identity | pass | `2026-10-28-federated-identity-review2-codex.md` | `ebef99dcc833f149723cb463f09ce638d2691e65dbcc215b8ef140920325e1fd` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar split | pass | `2026-10-28-sidecar-split-review-codex.md` | `1457a2a769edca01e59fff6424fe2ae614454d24e8afcc55924a895423064d9d` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 ambassador | pass | `2026-10-28-ambassador-review-codex.md` | `ec385313b887742ca865a576eddfb0d70856fe6f5ec64a5627b2b7ecac70d4e8` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar after page change | pass | `2026-10-28-sidecar-review-codex.md` | `3a5ab63edb52224287ff15b3e7d4fe349a5854c15da2d516e9d1e447ee3fa361` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar after Ambassador page | pass | `2026-10-28-sidecar-review9-codex.md` | `78ada626bd8ca6fa274e5e24bc1050cb070fa06842427ec65ee8f43ff3839e47` |
| 2026-10-28 | DeepSeek Reviewer | #540 self-contained service | pass | `2026-10-28-self-contained-service-review-deepseek.md` | `d6ebe907bf78974c6d2331d6314ea9a2aef024e3536f62062b0f85f5aa44597a` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 ambassador retry binding | pass | `2026-10-28-ambassador-review3-codex.md` | `7b77ae47d2130fec8e44000533c53397d3c64717e8dbf5df7a4e4be88ec58860` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 sidecar after Ambassador fix | pass | `2026-10-28-sidecar-review10-codex.md` | `445018565323f0b68e19bc14a9da744e55db3055ceac4a160d87cd8a56c8fed6` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 message filter | pass | `2026-10-28-message-filter-review-codex.md` | `9cd31daccc99bfd1056ac46027cb264c6e2b00104f3af9edb24ac2b97bf999e6` |
| 2026-10-28 | Codex / OpenAI (gpt-5.6-sol) | #540 request-reply after page change | pass | `2026-10-28-request-reply-review4-codex.md` | `9f88fb7e8a2a54453c2c7835a2a1897a23c299bdfd94ee27e18dc8fb4134b2d1` |
| 2026-10-28 | Codex / OpenAI | #540 tycho.pattern.request-reply-messaging | pass | `2026-10-28-request-reply-split-review2-codex.json` | `103a6d41d0bdcb20a36ef502e6813bd58dd7b1dcca998d40565342286d5ceba3` |
| 2026-10-28 | Codex / OpenAI | #540 tycho.pattern.message-filter | pass | `2026-10-28-message-filter-split-review2-codex.json` | `69b8e804d8b687af50b41ea4c30cb452d4344d96b8f073020fc126d619befb0c` |
| 2026-10-28 | DeepSeek Reviewer | #540 aggregator/scatter-gather | pass | `2026-10-28-aggregator-scatter-deepseek.md` | `20a17a26bf0c7b1bd2bbf21c43ed9105d04bf01c696de78cef2d15bd3613d234` |
