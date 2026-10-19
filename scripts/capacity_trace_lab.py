#!/usr/bin/env python3
"""Deterministic, zero-I/O admission-control thought experiment for Tycho E14-08.

This is NOT a load generator or benchmark of a real deployment. Durations and
arrivals are synthetic; the model has no waiting queue, retries, network,
CPU contention, warm-up, clocks, or latency correction. Use a real test
harness to validate any production architecture conclusion.
"""

from collections import defaultdict
import heapq
import json
import math
from typing import Iterable


def open_arrivals(count: int, interval_s: float) -> list[float]:
    """Offered arrivals independent of previous service completions."""
    if type(count) is not int or count < 0 or not math.isfinite(interval_s) or interval_s <= 0:
        raise ValueError("count must be nonnegative and interval_s positive")
    return [round(i * interval_s, 9) for i in range(count)]


def closed_arrivals(count: int, service_s: float, think_s: float = 0) -> list[float]:
    """A single synchronous virtual user; next start depends on completion."""
    if type(count) is not int or count < 0 or not math.isfinite(service_s) or not math.isfinite(think_s) or service_s <= 0 or think_s < 0:
        raise ValueError("invalid closed-model parameters")
    return [round(i * (service_s + think_s), 9) for i in range(count)]


def simulate_admission(
    arrivals: Iterable[tuple[float, str, float]],
    limits: dict[str, int],
    *,
    shared: bool,
) -> dict:
    """Admit or reject immediately; releases occur at arrival + service time.

    In shared mode a single 'shared' capacity is consumed by all classes.
    In isolated mode each class uses its own capacity. No waiting occurs.
    """
    if not limits or any(type(n) is not int or n <= 0 for n in limits.values()):
        raise ValueError("capacity limits must be positive integers")
    if shared and set(limits) != {"shared"}:
        raise ValueError("shared mode requires exactly {'shared': capacity}")
    pools: dict[str, list[float]] = defaultdict(list)
    admitted: dict[str, int] = defaultdict(int)
    rejected: dict[str, int] = defaultdict(int)
    max_inflight: dict[str, int] = defaultdict(int)
    total_offered = 0
    last_t = float("-inf")
    for t, cls, service_s in arrivals:
        if (not isinstance(cls, str) or not cls or not math.isfinite(t)
                or not math.isfinite(service_s) or t < 0 or service_s <= 0 or t < last_t):
            raise ValueError("arrivals must be sorted, nonnegative, with positive durations and class")
        last_t = t
        total_offered += 1
        pool = "shared" if shared else cls
        if pool not in limits:
            raise ValueError(f"missing capacity for {pool}")
        active = pools[pool]
        while active and active[0] <= t:
            heapq.heappop(active)
        if len(active) >= limits[pool]:
            rejected[cls] += 1
        else:
            heapq.heappush(active, t + service_s)
            admitted[cls] += 1
            max_inflight[pool] = max(max_inflight[pool], len(active))
    return {
        "model": "immediate-admission-no-waiting-queue",
        "offered": total_offered,
        "admitted": dict(sorted((c, n) for c, n in admitted.items() if n)),
        "rejected": dict(sorted((c, n) for c, n in rejected.items() if n)),
        "peak_inflight_by_pool": dict(sorted(max_inflight.items())),
    }


def example() -> dict:
    """Class B stalls; compare equal aggregate two-slot capacity."""
    trace = [(0.0, "B", 5.0), (0.01, "B", 5.0),
             (0.02, "A", 0.05), (0.12, "A", 0.05)]
    return {
        "trace": [{"arrival_s": t, "class": cls, "service_s": d} for t, cls, d in trace],
        "shared_capacity_2": simulate_admission(trace, {"shared": 2}, shared=True),
        "isolated_capacity_A1_B1": simulate_admission(trace, {"A": 1, "B": 1}, shared=False),
        "open_offered_starts": open_arrivals(5, 0.1),
        "closed_user_starts": closed_arrivals(5, 0.5, 0.1),
    }


if __name__ == "__main__":
    print(json.dumps(example(), indent=2, sort_keys=True))
