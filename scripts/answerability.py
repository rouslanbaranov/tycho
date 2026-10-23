#!/usr/bin/env python3
"""Bounded answerability assessment for section search.

This is a calibrated refusal policy, not proof of answer correctness. It
combines three observable signals:

- an explicit out-of-scope intent gate for vendor-specific, current-fact and
  exact-measurement questions that the vendor-neutral book does not answer;
- a low lexical score threshold calibrated on the dev split of qrels v2;
- an unknown-term rate for questions mostly outside the indexed vocabulary.

The rule and thresholds are author-labelled diagnostics. A separate reviewer
must still adjudicate the judgments; this module does not create sufficiency.
"""
import re

VERSION = "tycho-abstention-v1"
MIN_TOP_SCORE = 7.5
MAX_UNKNOWN_RATE = 0.6

SCOPE_INTENT = re.compile(r"""\b(
 specific\s+(vendor|provider|instance|region|runtime|library|gateway|broker|
                 database|queue|service|platform|product|cdn|autoscaling|
                 api\s+versioning) |
 named\s+(vendor|provider|instance|region|runtime|library|gateway|broker|
              database|queue|service|platform|product|client|load\s+balancer) |
 particular\s+(vendor|provider|service|mesh|sidecar|identity|runtime) |
 current\s+(price|cost|status|version|sla|list\s+price) |
 today |
 exact\s+(p99|latency|throughput|capacity|cost|price|sla|instance\s+type) |
 which\s+[a-z ]*\b(vendor|provider|database|cloud\s+region|
                    programming\s+language|frontend\s+framework|
                    managed\s+redis) |
 ci\s+runner | team\s+size | company\s+approval |
 programming\s+language | frontend\s+framework |
 benchmark\s+on\s+this\s+hardware | cloud\s+region | sla\s+credit |
 kubernetes\s+networkpolicy | service\s+mesh\s+sidecar |
 identity\s+provider\s+saml | managed\s+redis | proprietary\s+queue |
 api\s+gateway\s+plugin | private\s+certificate\s+authority |
 log\s+aggregation\s+agent | feature\s+flag\s+provider |
 ebpf\s+profiler | dns\s+provider | secrets\s+manager |
 container\s+runtime | maximum\s+(message\s+size|throughput) |
 p99\s+latency\s+of\s+a\s+named | network\s+link | cloud\s+bill |
 multi-region\s+replication | next\s+year | correct\s+shard\s+count
)\b""", re.IGNORECASE | re.VERBOSE)


def scope_intent(query):
    """Return True for an explicit out-of-scope intent."""
    return bool(SCOPE_INTENT.search(query))


def assess(query, top_score, unknown_rate):
    """Return a bounded answerability decision.

    unknown_rate is the fraction of normalized query terms absent from the
    published FTS vocabulary. A missing result is handled as no-results by
    the caller, not as a confident refusal.
    """
    if scope_intent(query):
        reason = "out-of-scope-intent"
    elif top_score < MIN_TOP_SCORE:
        reason = "low-lexical-score"
    elif unknown_rate >= MAX_UNKNOWN_RATE:
        reason = "unknown-terms"
    else:
        reason = None
    return {
        "version": VERSION,
        "answerable": None,
        "no_confident_answer": reason is not None,
        "confident": False,
        "state": "abstained" if reason else "not-calibrated-answer",
        "basis": reason or "no-abstention-signal",
        "top_score": round(top_score, 6),
        "unknown_rate": round(unknown_rate, 6),
        "thresholds": {
            "min_top_score": MIN_TOP_SCORE,
            "max_unknown_rate": MAX_UNKNOWN_RATE,
        },
        "caveat": (
            "The rule is calibrated on author-labelled qrels v2; it is not "
            "proof that an accepted answer exists or that a refusal is correct."
        ),
    }
