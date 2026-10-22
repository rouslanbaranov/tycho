# Sufficient-review packet — 2026-10-22

Status: **not reviewed**. This packet prepares an independent review; it is not a review
record, a sufficiency claim or owner acceptance.

## Reviewer instructions

Read each section and its atlas card. Check mechanism, invariant, failure/recovery,
alternative and limits. Confirm the section is dedicated to the named pattern and that
the reading-ledger record is `read`. Reject the candidate if the section is shared,
thin, generic or missing an exact source/limit. Record verdict, page hash and findings.

Do not edit the repository. Do not treat this packet as approval.

## Candidates

1. **Clean / Onion Architecture** — `tycho.pattern.clean-onion-architecture`
   - File: `layered-hexagonal-ports-and-adapters.md`
   - Heading: `Clean / Onion Architecture`; 211 words
   - SHA-256: `76a5dc742c37f26888c6697f8e26f5b2a99c5c4fd4706a6bd5215c1d1c158d57`

2. **API Gateway** — `tycho.pattern.api-gateway`
   - File: `gateway-boundaries-and-offloading.md`
   - Heading: `API Gateway`; 260 words
   - SHA-256: `589dfb82c569eb0d7238c72a33a6bb741229b09fa5f85fc3d42aba446cbd9535`

3. **Event Sourcing** — `tycho.pattern.event-sourcing`
   - File: `cqrs-event-sourcing-and-projections.md`
   - Heading: `2. Event sourcing: what becomes authoritative?`; 427 words
   - SHA-256: `2cf8dc6cdb3f8abaf4f334e81c7ff12149f84c1249a67476be850319acf35a59`

4. **Transactional Inbox** — `tycho.pattern.transactional-inbox`
   - File: `inbox-atomicity.md`
   - Heading: `3. Inbox and consumer-local atomicity`; 249 words
   - SHA-256: `2a3f563de1388cc8005664126c90253133003af2b1861738625bd91c7d7a719f`

5. **Command-Side Replica** — `tycho.pattern.command-side-replica`
   - File: `cqrs-event-sourcing-and-projections.md`
   - Heading: `Command-Side Replica`; 227 words
   - SHA-256: `2cf8dc6cdb3f8abaf4f334e81c7ff12149f84c1249a67476be850319acf35a59`

6. **Cache-Aside / Lazy Loading** — `tycho.pattern.cache-aside-lazy-loading`
   - File: `refresh-semantics.md`
   - Heading: `4. Cache-aside is a sequence, not a consistency theorem`; 398 words
   - SHA-256: `eb4c8c6a4438899077ba74dd319fa2c7c56ced4e91c74fae6dff941d8675304e`

7. **Negative Caching** — `tycho.pattern.negative-caching`
   - File: `negative-cache.md`
   - Heading: `4. Negative caching and evicted authorization`; 230 words
   - SHA-256: `a62e595ed394e19b710023f52bf7cb91be0a34ea30d7c31ddac837a749d68471`

8. **Hedged Requests** — `tycho.pattern.hedged-requests`
   - File: `deadline-hedging.md`
   - Heading: `4. Hedging, replication and selective degradation`; 396 words
   - SHA-256: `28e9253299bbeeaa4e753b68edb2be9341b59eeadffc557db72f28c782ec9b22`

9. **Health Endpoint Monitoring** — `tycho.pattern.health-endpoint-monitoring`
   - File: `routing-and-health.md`
   - Heading: `Health endpoint monitoring`; 236 words
   - SHA-256: `421498d62ce164a2c617ccb9ef8724f38b2da01b97f986a68426d544fd69c451`

10. **Leader Election** — `tycho.pattern.leader-election`
   - File: `leader-recovery.md`
    - Heading: `4. Leader elections, logs and client observations`; 295 words
    - SHA-256: `1993ed0bca91913562b6103c6de77c4fbeff1ea4456afc945c249dabd83d76e9`

## Required output

A reviewer record with: reviewer identity and independence, reviewed date, per-entry
verdict, page hash, findings and severity. A pass does not by itself change coverage;
the validators still require a separate policy change.

11. **Sidecar** — `tycho.pattern.sidecar`
    - File: `static-stability.md`
    - Heading: `Sidecar`; 122 words
    - SHA-256: `da0ec4a38b5b605c61261fecb745f4cad886a16ea992d5f5d896f0c6810bcc1c`

12. **Ambassador** — `tycho.pattern.ambassador`
    - File: `static-stability.md`
    - Heading: `Ambassador`; 140 words
    - SHA-256: `da0ec4a38b5b605c61261fecb745f4cad886a16ea992d5f5d896f0c6810bcc1c`

13. **Immutable Infrastructure** — `tycho.pattern.immutable-infrastructure`
    - File: `static-stability.md`
    - Heading: `Immutable Infrastructure`; 131 words
    - SHA-256: `da0ec4a38b5b605c61261fecb745f4cad886a16ea992d5f5d896f0c6810bcc1c`

14. **Read-Through Cache** — `tycho.pattern.read-through-cache`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Read-Through Cache`; 129 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

15. **Write-Through Cache** — `tycho.pattern.write-through-cache`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Write-Through Cache`; 122 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

16. **Write-Around** — `tycho.pattern.write-around`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Write-Around`; 127 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

17. **Multi-Level Caching** — `tycho.pattern.multi-level-caching`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Multi-Level Caching`; 123 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

18. **Competing Consumers** — `tycho.pattern.competing-consumers`
    - File: `message-selection.md`
    - Heading: `Competing Consumers`; 124 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

19. **Content-Based Router** — `tycho.pattern.content-based-router`
    - File: `message-selection.md`
    - Heading: `Content-Based Router`; 122 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

20. **Message Filter** — `tycho.pattern.message-filter`
    - File: `message-selection.md`
    - Heading: `Message Filter`; 120 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

21. **Pipes and Filters** — `tycho.pattern.pipes-and-filters`
    - File: `message-selection.md`
    - Heading: `Pipes and Filters`; 122 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

22. **Resequencer** — `tycho.pattern.resequencer`
    - File: `message-selection.md`
    - Heading: `Resequencer`; 123 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

23. **Canonical Data Model** — `tycho.pattern.canonical-data-model`
    - File: `message-selection.md`
    - Heading: `Canonical Data Model`; 125 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

24. **Multi-Leader Replication** — `tycho.pattern.multi-leader-replication`
    - File: `replication-consensus-and-leader-change.md`
    - Heading: `Multi-Leader Replication`; 130 words
    - SHA-256: `1b68e603c024182de4316235360a70ef4456cf720ac17c201b04a926c151c9a3`

25. **Read Replicas** — `tycho.pattern.read-replicas`
    - File: `replication-consensus-and-leader-change.md`
    - Heading: `Read Replicas`; 125 words
    - SHA-256: `1b68e603c024182de4316235360a70ef4456cf720ac17c201b04a926c151c9a3`

26. **Partitioning** — `tycho.pattern.partitioning`
    - File: `shard-keys-hotspots-and-resharding.md`
    - Heading: `Partitioning`; 126 words
    - SHA-256: `0ec1c84e22e1374dec45bd765ce3606519e82f7f6875d028432f6a5cdc21a933`

27. **Consistent Hashing** — `tycho.pattern.consistent-hashing`
    - File: `resharding-transition.md`
    - Heading: `Consistent Hashing`; 122 words
    - SHA-256: `093cc20efcbb43ba501273959614291f9b787b1e58df096025aeb6e906b89581`

28. **Backup, PITR and Restore** — `tycho.pattern.backup-pitr-and-restore`
    - File: `backup-restore-pitr-and-recovery-drills.md`
    - Heading: `Backup, PITR and Restore`; 127 words
    - SHA-256: `d6e6ffece4259cbc5472dc3c5c92eed7a5ed14abf518cb58bc2760cd48b9eaee`

29. **Cache Invalidation** — `tycho.pattern.cache-invalidation`
    - File: `cache-invalidation-stampede-and-hot-keys.md`
    - Heading: `Cache Invalidation`; 166 words
    - SHA-256: `820c9cffa217a8c22637ff83c4d973b6001bcd1d12655ed0a859f7ce227caa67`

30. **Stale-While-Revalidate** — `tycho.pattern.stale-while-revalidate`
    - File: `stale-fill.md`
    - Heading: `Stale-While-Revalidate`; 123 words
    - SHA-256: `fc8ec7d736a980edf25d9cedaca087e1cc5fea9f9a8bdab1b24cefb477d1dfe8`

31. **Rolling Deployment** — `tycho.pattern.rolling-deployment`
    - File: `gitops-canary-and-progressive-rollout.md`
    - Heading: `Rolling Deployment`; 124 words
    - SHA-256: `52a62dbd6570cb269e4f98088f5581b8ee1982f03a9d1b797241d28ed949285a`

32. **Blue/Green Deployment** — `tycho.pattern.blue-green-deployment`
    - File: `gitops-canary-and-progressive-rollout.md`
    - Heading: `Blue/Green Deployment`; 126 words
    - SHA-256: `52a62dbd6570cb269e4f98088f5581b8ee1982f03a9d1b797241d28ed949285a`

33. **Dark Launching / Shadow Traffic** — `tycho.pattern.dark-launching-shadow-traffic`
    - File: `gitops-canary-and-progressive-rollout.md`
    - Heading: `Dark Launching / Shadow Traffic`; 124 words
    - SHA-256: `52a62dbd6570cb269e4f98088f5581b8ee1982f03a9d1b797241d28ed949285a`

34. **Federated Identity** — `tycho.pattern.federated-identity`
    - File: `identity-authorization-and-isolation.md`
    - Heading: `Federated Identity`; 121 words
    - SHA-256: `8a7c087d993960c00c97ec2a9df4d4d1cfaff88ff0f69726f7b538e6a142b0d8`

35. **Workload Identity / mTLS** — `tycho.pattern.workload-identity-mtls`
    - File: `identity-authorization-and-isolation.md`
    - Heading: `Workload Identity / mTLS`; 127 words
    - SHA-256: `8a7c087d993960c00c97ec2a9df4d4d1cfaff88ff0f69726f7b538e6a142b0d8`

36. **Least Privilege** — `tycho.pattern.least-privilege`
    - File: `authorization-policy-and-least-privilege.md`
    - Heading: `Least Privilege`; 121 words
    - SHA-256: `e8c480106a885bb691f9ae7d4289fbf5c0683e3bc46dd4b9f3899da63fa15e6b`

37. **RBAC / ABAC** — `tycho.pattern.rbac-abac`
    - File: `authorization-policy-and-least-privilege.md`
    - Heading: `RBAC / ABAC`; 122 words
    - SHA-256: `e8c480106a885bb691f9ae7d4289fbf5c0683e3bc46dd4b9f3899da63fa15e6b`

38. **Tenant-Based Resource Isolation** — `tycho.pattern.tenant-based-resource-isolation`
    - File: `multitenant-isolation.md`
    - Heading: `Tenant-Based Resource Isolation`; 121 words
    - SHA-256: `5409f130f7bf8b35f046487848bb6089bce31ca2d3bd58b60fcca2431f989295`

39. **Multitenant Isolation** — `tycho.pattern.multitenant-isolation`
    - File: `multitenant-isolation.md`
    - Heading: `Multitenant Isolation`; 120 words
    - SHA-256: `5409f130f7bf8b35f046487848bb6089bce31ca2d3bd58b60fcca2431f989295`

40. **Gateway Aggregation** — `tycho.pattern.gateway-aggregation`
    - File: `gateway-boundaries-and-offloading.md`
    - Heading: `Gateway Aggregation`; 126 words
    - SHA-256: `1ccfdf1234e62e76bbeae7fa039634e953a48e31c455e1c4fe722984c3c365e7`

41. **Gateway Offloading** — `tycho.pattern.gateway-offloading`
    - File: `gateway-boundaries-and-offloading.md`
    - Heading: `Gateway Offloading`; 125 words
    - SHA-256: `1ccfdf1234e62e76bbeae7fa039634e953a48e31c455e1c4fe722984c3c365e7`

42. **Reverse Proxy** — `tycho.pattern.reverse-proxy`
    - File: `gateway-boundaries-and-offloading.md`
    - Heading: `Reverse Proxy`; 124 words
    - SHA-256: `1ccfdf1234e62e76bbeae7fa039634e953a48e31c455e1c4fe722984c3c365e7`

43. **Aggregator** — `tycho.pattern.aggregator`
    - File: `messaging-families-and-durable-workflows.md`
    - Heading: `Aggregator`; 129 words
    - SHA-256: `e726b57f97234a532aedb59a88eec1a63400cf64d3c1d16e2784b50842e7a8b2`

44. **Splitter** — `tycho.pattern.splitter`
    - File: `messaging-families-and-durable-workflows.md`
    - Heading: `Splitter`; 123 words
    - SHA-256: `e726b57f97234a532aedb59a88eec1a63400cf64d3c1d16e2784b50842e7a8b2`

45. **Scatter-Gather** — `tycho.pattern.scatter-gather`
    - File: `messaging-families-and-durable-workflows.md`
    - Heading: `Scatter-Gather`; 127 words
    - SHA-256: `e726b57f97234a532aedb59a88eec1a63400cf64d3c1d16e2784b50842e7a8b2`

46. **Claim Check** — `tycho.pattern.claim-check`
    - File: `workflow-failure.md`
    - Heading: `Claim Check`; 125 words
    - SHA-256: `57d173f1846271dd9a8f84287158cb43ee36d6684e6e7988faf3202f93b30c3f`

47. **Correlation Identifier** — `tycho.pattern.correlation-identifier`
    - File: `workflow-failure.md`
    - Heading: `Correlation Identifier`; 120 words
    - SHA-256: `57d173f1846271dd9a8f84287158cb43ee36d6684e6e7988faf3202f93b30c3f`

48. **Request-Reply Messaging** — `tycho.pattern.request-reply-messaging`
    - File: `workflow-failure.md`
    - Heading: `Request-Reply Messaging`; 124 words
    - SHA-256: `57d173f1846271dd9a8f84287158cb43ee36d6684e6e7988faf3202f93b30c3f`

49. **Backend for Frontend (BFF)** — `tycho.pattern.backend-for-frontend-bff`
    - File: `http-rpc-contracts-and-compatibility.md`
    - Heading: `Backend for Frontend (BFF)`; 143 words
    - SHA-256: `dcc8eb423e5d9c4d8485a95f9895c3a19b972dd18eb8ee57f9d074a77219ccfe`

50. **API Composition** — `tycho.pattern.api-composition`
    - File: `http-rpc-contracts-and-compatibility.md`
    - Heading: `API Composition`; 198 words
    - SHA-256: `dcc8eb423e5d9c4d8485a95f9895c3a19b972dd18eb8ee57f9d074a77219ccfe`

51. **Zero Trust Architecture** — `tycho.pattern.zero-trust-architecture`
    - File: `authorization-policy-and-least-privilege.md`
    - Heading: `Zero Trust Architecture`; 134 words
    - SHA-256: `e8c480106a885bb691f9ae7d4289fbf5c0683e3bc46dd4b9f3899da63fa15e6b`

52. **Valet Key** — `tycho.pattern.valet-key`
    - File: `object-credentials.md`
    - Heading: `Valet Key`; 129 words
    - SHA-256: `538595c885d153b4bf16c14db24ea0fc7b3b7c220e3bbcc431543fe6f0a6fa9b`

53. **Retry with Jitter** — `tycho.pattern.retry-with-jitter`
    - File: `deadlines-retries.md`
    - Heading: `Retry with Jitter`; 184 words
    - SHA-256: `e9c135e7bcc767a609cb2502dad6bb0b82e18d9b345a1fb2253e39a1318dcb8a`

54. **Structured Logging** — `tycho.pattern.structured-logging`
    - File: `logs-audit-and-data-lineage.md`
    - Heading: `Structured Logging`; 203 words
    - SHA-256: `48a2bfd702316c1d1587e9883ca87ffcd1e427f1e29bee86861f036e7a84a331`

55. **Database per Service** — `tycho.pattern.database-per-service`
    - File: `ownership-isolation.md`
    - Heading: `Database per Service`; 132 words
    - SHA-256: `c278ed331b3f3acf4d35adaea22dc016fc40301063a9511bb238281872073886`

56. **Self-Contained Service** — `tycho.pattern.self-contained-service`
    - File: `service-independence.md`
    - Heading: `Self-Contained Service`; 127 words
    - SHA-256: `8616633953b0422d01608d9305fdbf2d957fce90cf8bfedaf2c47fec02975ea8`

57. **Asynchronous Request-Reply** — `tycho.pattern.asynchronous-request-reply`
    - File: `asynchronous-apis-streaming-and-cancellation.md`
    - Heading: `Asynchronous Request-Reply`; 123 words
    - SHA-256: `fd79ee55e9a8888d1562ccd5050adabc1c704470066b75e7dc83d53ec0888a8f`

58. **Gatekeeper** — `tycho.pattern.gatekeeper`
    - File: `authorization-boundaries-and-multitenancy.md`
    - Heading: `Gatekeeper`; 125 words
    - SHA-256: `a3ead39a7b313e4a44eb79d61b32ee3ea2029b1a5914e587d50cd678f3ed486b`

59. **Process Manager / Routing Slip** — `tycho.pattern.process-manager-routing-slip`
    - File: `saga-workflows.md`
    - Heading: `Process Manager / Routing Slip`; 121 words
    - SHA-256: `76c6c37fb8d5f7d6ba42d44c5c2f7fca8b22e1bbc819125da09e349df3797d66`

60. **Two-Phase Commit (2PC)** — `tycho.pattern.two-phase-commit-2pc`
    - File: `invariants-isolation.md`
    - Heading: `Two-Phase Commit (2PC)`; 126 words
    - SHA-256: `04bcf79cb71c11d28648b152be72d82a95fbbf34085c9c7237be9bf19558572f`

61. **Deployment Stamps** — `tycho.pattern.deployment-stamps`
    - File: `cells-shuffle-sharding.md`
    - Heading: `Deployment Stamps`; 134 words
    - SHA-256: `35346976f4b654f24e5beb6881cb26495339b3d3a131939a45f5538782d3c209`

62. **Parallel Run** — `tycho.pattern.parallel-run`
    - File: `authority-states.md`
    - Heading: `Parallel Run`; 129 words
    - SHA-256: `74eb15e131607021bcfddebbbe0893934c10eb42363f0227f79cf6c25737cf5a`

63. **Write-Behind / Write-Back** — `tycho.pattern.write-behind-write-back`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Write-Behind / Write-Back`; 123 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

64. **Geode** — `tycho.pattern.geode`
    - File: `disaster-recovery-and-recovery-objectives.md`
    - Heading: `Geode`; 132 words
    - SHA-256: `535ad5af4c37a316ef26023360018081682de8ab014a96f8d182d476edeb9583`

65. **Synthetic Monitoring** — `tycho.pattern.synthetic-monitoring`
    - File: `budget-actions.md`
    - Heading: `Synthetic Monitoring`; 121 words
    - SHA-256: `928c499937ffba9f15e5ea0e4cce4c743a0e0d8a2e6001fbe8aeca3d987a70f0`

66. **Health, Readiness and Liveness Checks** — `tycho.pattern.health-readiness-and-liveness-checks`
    - File: `incident-practice.md`
    - Heading: `Health, Readiness and Liveness Checks`; 132 words
    - SHA-256: `8eed0c2ebac5f448d2b245d73a3c60c959806c067ceb9181eef05fb857a2a336`

67. **Retry with Exponential Backoff** — `tycho.pattern.retry-with-exponential-backoff`
    - File: `deadlines-retries.md`
    - Heading: `Retry with Exponential Backoff`; 140 words
    - SHA-256: `e9c135e7bcc767a609cb2502dad6bb0b82e18d9b345a1fb2253e39a1318dcb8a`

68. **Timeout** — `tycho.pattern.timeout`
    - File: `deadlines-retries.md`
    - Heading: `Timeout`; 120 words
    - SHA-256: `e9c135e7bcc767a609cb2502dad6bb0b82e18d9b345a1fb2253e39a1318dcb8a`

69. **Deadline Propagation** — `tycho.pattern.deadline-propagation`
    - File: `deadlines-retries.md`
    - Heading: `Deadline Propagation`; 120 words
    - SHA-256: `e9c135e7bcc767a609cb2502dad6bb0b82e18d9b345a1fb2253e39a1318dcb8a`

70. **Distributed Lock** — `tycho.pattern.distributed-lock`
    - File: `leader-recovery.md`
    - Heading: `Distributed Lock`; 126 words
    - SHA-256: `1993ed0bca91913562b6103c6de77c4fbeff1ea4456afc945c249dabd83d76e9`

71. **Lease-Based Ownership** — `tycho.pattern.lease-based-ownership`
    - File: `leader-recovery.md`
    - Heading: `Lease-Based Ownership`; 120 words
    - SHA-256: `1993ed0bca91913562b6103c6de77c4fbeff1ea4456afc945c249dabd83d76e9`

72. **Fencing Tokens** — `tycho.pattern.fencing-tokens`
    - File: `leader-recovery.md`
    - Heading: `Fencing Tokens`; 122 words
    - SHA-256: `1993ed0bca91913562b6103c6de77c4fbeff1ea4456afc945c249dabd83d76e9`

73. **Saga** — `tycho.pattern.saga`
    - File: `saga-workflows.md`
    - Heading: `Saga`; 123 words
    - SHA-256: `76c6c37fb8d5f7d6ba42d44c5c2f7fca8b22e1bbc819125da09e349df3797d66`

74. **Saga Choreography** — `tycho.pattern.saga-choreography`
    - File: `saga-workflows.md`
    - Heading: `Saga Choreography`; 123 words
    - SHA-256: `76c6c37fb8d5f7d6ba42d44c5c2f7fca8b22e1bbc819125da09e349df3797d66`

75. **Saga Orchestration** — `tycho.pattern.saga-orchestration`
    - File: `saga-workflows.md`
    - Heading: `Saga Orchestration`; 122 words
    - SHA-256: `76c6c37fb8d5f7d6ba42d44c5c2f7fca8b22e1bbc819125da09e349df3797d66`

76. **Compensating Transaction** — `tycho.pattern.compensating-transaction`
    - File: `saga-workflows.md`
    - Heading: `Compensating Transaction`; 124 words
    - SHA-256: `76c6c37fb8d5f7d6ba42d44c5c2f7fca8b22e1bbc819125da09e349df3797d66`

77. **Publish/Subscribe** — `tycho.pattern.publish-subscribe`
    - File: `message-selection.md`
    - Heading: `Publish / Subscribe`; 149 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

78. **Point-to-Point Queue** — `tycho.pattern.point-to-point-queue`
    - File: `message-selection.md`
    - Heading: `Point-to-Point Queue`; 126 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

79. **Event-Driven Consumer** — `tycho.pattern.event-driven-consumer`
    - File: `message-selection.md`
    - Heading: `Event-Driven Consumer`; 120 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

80. **Durable Subscriber** — `tycho.pattern.durable-subscriber`
    - File: `message-selection.md`
    - Heading: `Durable Subscriber`; 134 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

81. **Message Broker / Messaging Bridge** — `tycho.pattern.message-broker-messaging-bridge`
    - File: `message-selection.md`
    - Heading: `Message Broker / Messaging Bridge`; 124 words
    - SHA-256: `3664e20f93d6b6ee6d6f994b43c0d158de391f67aa023ed1b8a8e5e57378e4e3`

82. **Fallback** — `tycho.pattern.fallback`
    - File: `overload-admission-control-and-graceful-degradation.md`
    - Heading: `Fallback`; 125 words
    - SHA-256: `a80a884f7e2cc021ccd3acd1306a6ba369e97d59d7110b56afe7369d56976daf`

83. **Graceful Degradation** — `tycho.pattern.graceful-degradation`
    - File: `overload-admission-control-and-graceful-degradation.md`
    - Heading: `Graceful Degradation`; 120 words
    - SHA-256: `a80a884f7e2cc021ccd3acd1306a6ba369e97d59d7110b56afe7369d56976daf`

84. **Load Shedding** — `tycho.pattern.load-shedding`
    - File: `overload-admission-control-and-graceful-degradation.md`
    - Heading: `Load Shedding`; 120 words
    - SHA-256: `a80a884f7e2cc021ccd3acd1306a6ba369e97d59d7110b56afe7369d56976daf`

85. **Throttling** — `tycho.pattern.throttling`
    - File: `overload-admission-control-and-graceful-degradation.md`
    - Heading: `Throttling`; 120 words
    - SHA-256: `a80a884f7e2cc021ccd3acd1306a6ba369e97d59d7110b56afe7369d56976daf`

86. **Rate Limiting** — `tycho.pattern.rate-limiting`
    - File: `overload-admission-control-and-graceful-degradation.md`
    - Heading: `Rate Limiting`; 120 words
    - SHA-256: `a80a884f7e2cc021ccd3acd1306a6ba369e97d59d7110b56afe7369d56976daf`

87. **Service Discovery** — `tycho.pattern.service-discovery`
    - File: `discovery-balancing.md`
    - Heading: `Service Discovery`; 126 words
    - SHA-256: `c3f98b92903fa89a593c849e5a93f9092d490a46ea3e52f0641043bcd72e269f`

88. **Client-Side Discovery** — `tycho.pattern.client-side-discovery`
    - File: `discovery-balancing.md`
    - Heading: `Client-Side Discovery`; 126 words
    - SHA-256: `c3f98b92903fa89a593c849e5a93f9092d490a46ea3e52f0641043bcd72e269f`

89. **Server-Side Discovery** — `tycho.pattern.server-side-discovery`
    - File: `discovery-balancing.md`
    - Heading: `Server-Side Discovery`; 127 words
    - SHA-256: `c3f98b92903fa89a593c849e5a93f9092d490a46ea3e52f0641043bcd72e269f`

90. **Load Balancing** — `tycho.pattern.load-balancing`
    - File: `discovery-balancing.md`
    - Heading: `Load Balancing`; 132 words
    - SHA-256: `c3f98b92903fa89a593c849e5a93f9092d490a46ea3e52f0641043bcd72e269f`

91. **Layered Architecture** — `tycho.pattern.layered-architecture`
    - File: `layered-hexagonal-ports-and-adapters.md`
    - Heading: `Layered Architecture`; 123 words
    - SHA-256: `76a5dc742c37f26888c6697f8e26f5b2a99c5c4fd4706a6bd5215c1d1c158d57`

92. **Hexagonal Architecture / Ports and Adapters** — `tycho.pattern.hexagonal-architecture-ports-and-adapters`
    - File: `layered-hexagonal-ports-and-adapters.md`
    - Heading: `Hexagonal Architecture / Ports and Adapters`; 125 words
    - SHA-256: `76a5dc742c37f26888c6697f8e26f5b2a99c5c4fd4706a6bd5215c1d1c158d57`

93. **Horizontal Scaling** — `tycho.pattern.horizontal-scaling`
    - File: `autoscaling-lag-and-capacity-limits.md`
    - Heading: `Horizontal Scaling`; 136 words
    - SHA-256: `578fd03227719a52272b97089cbec74a1ee7d6135d2e9fe5a0549f48b58e52ce`

94. **Vertical Scaling** — `tycho.pattern.vertical-scaling`
    - File: `autoscaling-lag-and-capacity-limits.md`
    - Heading: `Vertical Scaling`; 130 words
    - SHA-256: `578fd03227719a52272b97089cbec74a1ee7d6135d2e9fe5a0549f48b58e52ce`

95. **Autoscaling** — `tycho.pattern.autoscaling`
    - File: `autoscaling-lag-and-capacity-limits.md`
    - Heading: `Autoscaling`; 120 words
    - SHA-256: `578fd03227719a52272b97089cbec74a1ee7d6135d2e9fe5a0549f48b58e52ce`

96. **Microservices Architecture** — `tycho.pattern.microservices-architecture`
    - File: `service-orientation-microservices-and-distribution.md`
    - Heading: `Microservices Architecture`; 125 words
    - SHA-256: `ebb099cba82b979816a5321d263646321b92e4996da170488812fa86d9a4c419`

97. **Service-Oriented Architecture (SOA)** — `tycho.pattern.service-oriented-architecture-soa`
    - File: `service-orientation-microservices-and-distribution.md`
    - Heading: `Service-Oriented Architecture (SOA)`; 126 words
    - SHA-256: `ebb099cba82b979816a5321d263646321b92e4996da170488812fa86d9a4c419`

98. **Distributed Tracing** — `tycho.pattern.distributed-tracing`
    - File: `distributed-tracing-context-and-sampling.md`
    - Heading: `Distributed Tracing`; 131 words
    - SHA-256: `cbb5676f377228fbb1a3bc0a1e8ef6fb74c4ca4495ba34f39280cf76c09794e1`

99. **Audit Trail** — `tycho.pattern.audit-trail`
    - File: `logs-audit-and-data-lineage.md`
    - Heading: `Audit Trail`; 146 words
    - SHA-256: `48a2bfd702316c1d1587e9883ca87ffcd1e427f1e29bee86861f036e7a84a331`

100. **SLI/SLO and Error Budgets** — `tycho.pattern.sli-slo-and-error-budgets`
    - File: `service-level-indicators-objectives-and-alerts.md`
    - Heading: `SLI / SLO and Error Budgets`; 187 words
    - SHA-256: `277e08fee127ea19bf70757a77b773a2fc46818b7baae0cbaaf24088774efcce`

101. **Polyglot Persistence** — `tycho.pattern.polyglot-persistence`
    - File: `multi-store-selection.md`
    - Heading: `Polyglot Persistence`; 139 words
    - SHA-256: `f60030288c218bf6175c16a1238f54574ce6f1f40e0f9c51aae9dea2a7152c6e`

102. **Modular Monolith** — `tycho.pattern.modular-monolith`
    - File: `modular-monolith-and-internal-events.md`
    - Heading: `Modular Monolith`; 120 words
    - SHA-256: `a54eacbfd845ca4dc142ef5e002cf7939bbecd6dca958210473291f9c46136dc`

103. **Domain-Driven Design / Bounded Context** — `tycho.pattern.domain-driven-design-bounded-context`
    - File: `domain-authority.md`
    - Heading: `Domain-Driven Design / Bounded Context`; 135 words
    - SHA-256: `82d8aab2c7a84c41aa11a0495fc2efb3ef49dfdc2a2e5d6fc6b439b23b5972a8`

104. **Anti-Corruption Layer** — `tycho.pattern.anti-corruption-layer`
    - File: `anti-corruption-adapters-and-coexistence.md`
    - Heading: `Anti-Corruption Layer`; 148 words
    - SHA-256: `e47be7ccd0b5950542264e20cee2e814c461d1ac672ea40fd4c6f3fb544dd420`

105. **Gateway Routing** — `tycho.pattern.gateway-routing`
    - File: `routing-and-health.md`
    - Heading: `Gateway Routing`; 132 words
    - SHA-256: `6f798e7796c556cfd1458b8ec2200ad113a0d74d033708740d3d61f7a2376f1a`

106. **Dead Letter Channel / DLQ** — `tycho.pattern.dead-letter-channel-dlq`
    - File: `workflow-failure.md`
    - Heading: `Dead Letter Channel / DLQ`; 139 words
    - SHA-256: `57d173f1846271dd9a8f84287158cb43ee36d6684e6e7988faf3202f93b30c3f`

107. **Idempotent Receiver** — `tycho.pattern.idempotent-receiver`
    - File: `dedup-authority.md`
    - Heading: `Idempotent Receiver`; 136 words
    - SHA-256: `06b4811f582595cc77d67d7179532676910c3e1bc697df6d945be3b4baa35111`

108. **Idempotency Key** — `tycho.pattern.idempotency-key`
    - File: `retries-idempotency-and-ambiguous-effects.md`
    - Heading: `Idempotency Key`; 154 words
    - SHA-256: `8b2dfc20407671fbc557e503f73d73b9337fa8a4b82e5a81886feccbd6dbbff8`

109. **Change Data Capture (CDC)** — `tycho.pattern.change-data-capture-cdc`
    - File: `cdc-state.md`
    - Heading: `Change Data Capture (CDC)`; 144 words
    - SHA-256: `147f4fd3c473ce49f03288915ea0de0ed58ca472f706fd7070b3e8ac5fabd213`

110. **Distributed Cache** — `tycho.pattern.distributed-cache`
    - File: `local-and-distributed-cache-design.md`
    - Heading: `Distributed Cache`; 134 words
    - SHA-256: `0a092ab1c69b079deff16172cf3a846d068155605ff6f080510c5580100b9a82`

111. **TTL-Based Expiration** — `tycho.pattern.ttl-based-expiration`
    - File: `refresh-semantics.md`
    - Heading: `TTL-Based Expiration`; 137 words
    - SHA-256: `eb4c8c6a4438899077ba74dd319fa2c7c56ced4e91c74fae6dff941d8675304e`

112. **Cache Stampede Protection** — `tycho.pattern.cache-stampede-protection`
    - File: `stampede-protection.md`
    - Heading: `Cache Stampede Protection`; 139 words
    - SHA-256: `fb59dca0cad703df369987fef4240393fe2254f5652ebc0c6922da8731bdfedb`

113. **Single Flight / Request Coalescing** — `tycho.pattern.single-flight-request-coalescing`
    - File: `stampede-protection.md`
    - Heading: `Single Flight / Request Coalescing`; 135 words
    - SHA-256: `fb59dca0cad703df369987fef4240393fe2254f5652ebc0c6922da8731bdfedb`

114. **Transactional Outbox** — `tycho.pattern.transactional-outbox`
    - File: `outbox-inbox-sagas-and-durable-workflows.md`
    - Heading: `Transactional Outbox`; 133 words
    - SHA-256: `70b13dee3bad23d6b63da787cf8af5f523c47e061f134fc16583f1bde551f86c`

115. **Distributed Workflow Orchestration** — `tycho.pattern.distributed-workflow-orchestration`
    - File: `outbox-inbox-sagas-and-durable-workflows.md`
    - Heading: `Distributed Workflow Orchestration`; 120 words
    - SHA-256: `70b13dee3bad23d6b63da787cf8af5f523c47e061f134fc16583f1bde551f86c`

116. **Leader-Follower Replication** — `tycho.pattern.leader-follower-replication`
    - File: `replication-consensus-and-leader-change.md`
    - Heading: `Leader-Follower Replication`; 136 words
    - SHA-256: `55ff8e5a0e47f1136f5f7d32a76f34d941e6991407643a58f752dba5d374db98`

117. **Consensus** — `tycho.pattern.consensus`
    - File: `replication-consensus-and-leader-change.md`
    - Heading: `Consensus`; 150 words
    - SHA-256: `55ff8e5a0e47f1136f5f7d32a76f34d941e6991407643a58f752dba5d374db98`

118. **Expand-and-Contract Schema** — `tycho.pattern.expand-and-contract-schema`
    - File: `migration-retirement.md`
    - Heading: `Expand-and-Contract Schema`; 122 words
    - SHA-256: `93e6128408bd4a0e2e53b5a79956fe8803e6e7b90f33328a381896fb6980de9b`

119. **Online Data Migration** — `tycho.pattern.online-data-migration`
    - File: `migration-retirement.md`
    - Heading: `Online Data Migration`; 126 words
    - SHA-256: `93e6128408bd4a0e2e53b5a79956fe8803e6e7b90f33328a381896fb6980de9b`

120. **Cell-Based Architecture** — `tycho.pattern.cell-based-architecture`
    - File: `cells-shuffle-sharding.md`
    - Heading: `Cell-Based Architecture`; 126 words
    - SHA-256: `35346976f4b654f24e5beb6881cb26495339b3d3a131939a45f5538782d3c209`

121. **Shuffle Sharding** — `tycho.pattern.shuffle-sharding`
    - File: `cells-shuffle-sharding.md`
    - Heading: `Shuffle Sharding`; 120 words
    - SHA-256: `35346976f4b654f24e5beb6881cb26495339b3d3a131939a45f5538782d3c209`

122. **Branch by Abstraction** — `tycho.pattern.branch-by-abstraction`
    - File: `cutover-gates.md`
    - Heading: `Branch by Abstraction`; 131 words
    - SHA-256: `fd2d8c0c617098a56c8125cb2e650b79fbc1caa0623fc527509799e8b655179c`

123. **Controlled Cutover** — `tycho.pattern.controlled-cutover`
    - File: `cutover-gates.md`
    - Heading: `Controlled Cutover`; 135 words
    - SHA-256: `fd2d8c0c617098a56c8125cb2e650b79fbc1caa0623fc527509799e8b655179c`

124. **Domain Events** — `tycho.pattern.domain-events`
    - File: `cqrs-event-sourcing-and-projections.md`
    - Heading: `Domain Events`; 134 words
    - SHA-256: `2cf8dc6cdb3f8abaf4f334e81c7ff12149f84c1249a67476be850319acf35a59`

125. **Materialized View** — `tycho.pattern.materialized-view`
    - File: `cqrs-event-sourcing-and-projections.md`
    - Heading: `Materialized View`; 123 words
    - SHA-256: `2cf8dc6cdb3f8abaf4f334e81c7ff12149f84c1249a67476be850319acf35a59`
