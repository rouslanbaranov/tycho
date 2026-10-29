#!/usr/bin/env python3
"""Deterministic V12 reference engine.

The engine implements three bounded model families used by the V12 volume:

* a stock-and-flow backlog model with exact request conservation;
* a discrete-event checkout model with capacity, queueing, timeouts, retries and
  backpressure;
* a staged modernization model with dual-write lag, reconciliation and rollback.

It also provides seeded Monte Carlo aggregation, pick-freeze first-order and
total-order sensitivity estimates, canonical provenance hashes and a replay
check. It is intentionally small, dependency-free and separate from the book
pages. Passing engine tests proves only the exercised reference cases.
"""
from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass, field
from datetime import date
import hashlib
import heapq
import json
import math
from pathlib import Path
import platform
import random
import statistics
import sys
import time
from typing import Any, Callable

ENGINE_VERSION = "1.0.0"
ENGINE_NAME = "tycho-v12-reference-engine"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ALPHA = 0.05
Z_975 = 1.959963984540054


class EngineError(ValueError):
    """A deterministic input or invariant failure."""


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_bytes(canonical_json(value).encode("utf-8"))


def fnv1a(text: str) -> int:
    value = 0xCBF29CE484222325
    for byte in text.encode("utf-8"):
        value ^= byte
        value = (value * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return value & 0x7FFFFFFF


def display_path(path: str | Path) -> str:
    candidate = Path(path)
    try:
        return candidate.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def file_sha256(path: str | Path) -> str:
    return sha256_bytes(Path(path).read_bytes())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise EngineError(message)


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = (len(ordered) - 1) * fraction
    low = math.floor(index)
    high = math.ceil(index)
    if low == high:
        return ordered[int(index)]
    weight = index - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


# ---------------------------------------------------------------------------
# Deterministic event queue
# ---------------------------------------------------------------------------


@dataclass(order=True)
class Event:
    time: float
    priority: int
    sequence: int
    kind: str = field(compare=False)
    payload: dict = field(default_factory=dict, compare=False)


class EventQueue:
    """Heap queue with a stable (time, priority, insertion) order."""

    def __init__(self) -> None:
        self._heap: list[Event] = []
        self._sequence = 0

    def schedule(self, time_value: float, priority: int, kind: str,
                 payload: dict | None = None) -> None:
        require(time_value >= 0.0, "event time must be non-negative")
        self._sequence += 1
        heapq.heappush(self._heap, Event(round(time_value, 12), priority,
                                         self._sequence, kind, payload or {}))

    def pop(self) -> Event | None:
        if not self._heap:
            return None
        return heapq.heappop(self._heap)

    def __len__(self) -> int:
        return len(self._heap)


# ---------------------------------------------------------------------------
# Sampling helpers
# ---------------------------------------------------------------------------


def sample_lognormal(rng: random.Random, mean: float, cv: float) -> float:
    """Lognormal with requested arithmetic mean and coefficient of variation."""
    require(mean > 0.0 and cv > 0.0, "lognormal mean and cv must be positive")
    sigma2 = math.log(1.0 + cv * cv)
    mu = math.log(mean) - sigma2 / 2.0
    return math.exp(rng.gauss(mu, math.sqrt(sigma2)))


def sample_service(rng: random.Random, spec: dict) -> float:
    kind = spec["kind"]
    mean = float(spec["mean"])
    cv = float(spec["cv"])
    if kind == "deterministic":
        return mean
    if kind == "exponential":
        return rng.expovariate(1.0 / mean)
    if kind == "lognormal":
        return sample_lognormal(rng, mean, cv)
    raise EngineError("unsupported service-time distribution: " + str(kind))


def backoff_delay(rng: random.Random, spec: dict, attempt: int) -> float:
    kind = spec["kind"]
    base = float(spec["base"])
    if kind == "none" or base == 0.0:
        return 0.0
    if kind == "exponential":
        delay = base * (2 ** (attempt - 1))
    elif kind == "linear":
        delay = base * attempt
    else:
        raise EngineError("unsupported retry backoff: " + str(kind))
    jitter = spec["jitter"]
    if jitter == "full":
        return rng.uniform(0.0, delay)
    if jitter == "equal":
        return delay / 2.0 + rng.uniform(0.0, delay / 2.0)
    return delay


# ---------------------------------------------------------------------------
# Discrete-event checkout model
# ---------------------------------------------------------------------------


class CheckoutSimulation:
    """Single-class queue with capacity, timeouts, retries and a bulkhead."""

    def __init__(self, scenario: dict, parameters: dict, seed: int) -> None:
        self.scenario = scenario
        self.parameters = parameters
        self.rng = random.Random(seed)
        self.queue: deque[dict] = deque()
        self.events = EventQueue()
        self.now = 0.0
        self.free_servers = int(parameters["servers"])
        self.in_service: dict[int, dict] = {}
        self.requests: list[dict] = []
        self.by_id: dict[int, dict] = {}
        self.attempts_total = 0
        self.completed: list[float] = []
        self.rejected = 0
        self.timed_out = 0
        self.failed = 0
        self.offered = 0
        self.max_queue = 0
        self.queue_area = 0.0
        self.busy_area = 0.0
        self.last_area_time = 0.0
        self.measurement_start = float(scenario["workload"]["warmup"])
        self.duration = float(scenario["workload"]["duration"])
        self.queue_capacity = int(parameters["queue_capacity"])
        self.bulkhead = int(parameters["bulkhead"])
        self.timeout = float(parameters["timeout"])
        self.max_attempts = int(parameters["max_attempts"])
        self.arrival_rate = float(parameters["arrival_rate"])
        self._next_request_id = 0

    # -- accounting -----------------------------------------------------
    def _accumulate(self, until: float) -> None:
        start = max(self.last_area_time, self.measurement_start)
        if until > start:
            effective = until - start
            self.queue_area += len(self.queue) * effective
            busy = self.parameters["servers"] - self.free_servers
            self.busy_area += busy * effective
        self.last_area_time = max(self.last_area_time, until)

    def _record_offer(self) -> None:
        if self.now >= self.measurement_start:
            self.offered += 1

    def _in_window(self, request: dict) -> bool:
        return float(request["first_arrival"]) >= self.measurement_start

    # -- lifecycle ------------------------------------------------------
    def _schedule_arrivals(self) -> None:
        if self.arrival_rate <= 0.0:
            return
        first = self.rng.expovariate(self.arrival_rate)
        self.events.schedule(first, 1, "arrival")

    def _enqueue(self, request: dict) -> None:
        if request["done"]:
            return
        total = len(self.queue) + len(self.in_service)
        if len(self.queue) >= self.queue_capacity or total >= self.bulkhead:
            if self._in_window(request):
                self.rejected += 1
            request["done"] = True
            request["outcome"] = "rejected"
            return
        self.queue.append(request)
        self.max_queue = max(self.max_queue, len(self.queue))
        self._dispatch()

    def _dispatch(self) -> None:
        while self.free_servers > 0 and self.queue:
            request = self.queue.popleft()
            if request["done"]:
                continue
            self.free_servers -= 1
            if self._in_window(request):
                self.attempts_total += 1
            request["attempts"] += 1
            request["attempt"] += 1
            request["state"] = "service"
            service_time = sample_service(self.rng, self.parameters["service_time"])
            request["service_end"] = self.now + service_time
            self.in_service[request["id"]] = request
            self.events.schedule(self.now + self.timeout, 0, "timeout",
                                 {"request_id": request["id"], "attempt": request["attempt"]})
            self.events.schedule(request["service_end"], 0, "service_done",
                                 {"request_id": request["id"], "attempt": request["attempt"]})

    def _timeout(self, request: dict, attempt: int) -> None:
        if request["done"] or request["attempt"] != attempt:
            return
        request["done"] = True
        request["outcome"] = "timeout"
        if request["id"] in self.in_service:
            del self.in_service[request["id"]]
            self.free_servers += 1
        else:
            try:
                self.queue.remove(request)
            except ValueError:
                pass
        if self._in_window(request):
            self.timed_out += 1
        if request["attempts"] < self.max_attempts:
            request["done"] = False
            request["outcome"] = "retry"
            delay = backoff_delay(self.rng, self.parameters["retry_backoff"],
                                  request["attempts"])
            self.events.schedule(self.now + delay, 2, "retry",
                                 {"request_id": request["id"]})
        else:
            if self._in_window(request):
                self.failed += 1
            request["outcome"] = "failed"

    def _complete(self, request: dict, attempt: int) -> None:
        if request["done"] or request["attempt"] != attempt or request["state"] != "service":
            return
        request["done"] = True
        request["outcome"] = "completed"
        if request["id"] in self.in_service:
            del self.in_service[request["id"]]
            self.free_servers += 1
        latency = self.now - request["first_arrival"]
        if self._in_window(request):
            self.completed.append(latency)
        self._dispatch()

    def run(self) -> dict:
        self._schedule_arrivals()
        while True:
            event = self.events.pop()
            if event is None or event.time > self.duration:
                break
            self.now = event.time
            self._accumulate(self.now)
            if event.kind == "arrival":
                self._record_offer()
                self._next_request_id += 1
                request = {
                    "id": self._next_request_id,
                    "first_arrival": self.now,
                    "attempts": 0,
                    "attempt": 0,
                    "done": False,
                    "state": "queued",
                    "outcome": None,
                }
                self.requests.append(request)
                self.by_id[request["id"]] = request
                self.events.schedule(self.now + self.timeout, 0, "timeout",
                                     {"request_id": request["id"], "attempt": 0})
                self._enqueue(request)
                if self.arrival_rate > 0.0:
                    self.events.schedule(self.now + self.rng.expovariate(self.arrival_rate),
                                         1, "arrival")
            elif event.kind == "service_done":
                request = self.in_service.get(event.payload["request_id"])
                if request is not None:
                    self._complete(request, event.payload["attempt"])
            elif event.kind == "timeout":
                request = self._request(event.payload["request_id"])
                if request is not None:
                    self._timeout(request, event.payload["attempt"])
                    self._dispatch()
            elif event.kind == "retry":
                request = self._request(event.payload["request_id"])
                if request is not None and not request["done"]:
                    request["state"] = "queued"
                    self.events.schedule(self.now + self.timeout, 0, "timeout",
                                         {"request_id": request["id"],
                                          "attempt": request["attempt"]})
                    self._enqueue(request)
        self.now = self.duration
        self._accumulate(self.duration)
        return self._metrics()

    def _request(self, request_id: int) -> dict | None:
        return self.by_id.get(request_id)

    def _metrics(self) -> dict:
        measurement = max(self.duration - self.measurement_start, 1e-9)
        completed = len(self.completed)
        latency_mean = statistics.fmean(self.completed) if self.completed else 0.0
        latency_p95 = percentile(self.completed, 0.95)
        latency_p99 = percentile(self.completed, 0.99)
        in_system_window = sum(1 for request in self.requests
                               if self._in_window(request) and not request["done"])
        conservation = self.offered == (completed + self.rejected + self.failed
                                        + in_system_window)
        return {
            "offered": self.offered,
            "completed": completed,
            "rejected": self.rejected,
            "timed_out": self.timed_out,
            "failed": self.failed,
            "in_system_at_end": in_system_window,
            "success_rate": completed / self.offered if self.offered else 0.0,
            "rejection_rate": self.rejected / self.offered if self.offered else 0.0,
            "timeout_rate": self.timed_out / self.offered if self.offered else 0.0,
            "throughput": completed / measurement,
            "latency_mean": latency_mean,
            "latency_p95": latency_p95,
            "latency_p99": latency_p99,
            "mean_queue_length": self.queue_area / measurement,
            "max_queue_length": self.max_queue,
            "server_utilization": min(1.0, self.busy_area / (self.parameters["servers"] * measurement))
            if self.parameters["servers"] else 0.0,
            "retry_amplification": self.attempts_total / self.offered if self.offered else 0.0,
            "cost_per_1k_success": (self.parameters["servers"] * self.parameters["cost_per_server_hour"]
                                   * (measurement / 3600.0) / completed * 1000.0) if completed else 0.0,
            "served": completed + in_system_window,
            "conservation_ok": conservation,
        }


# ---------------------------------------------------------------------------
# Stock-and-flow model
# ---------------------------------------------------------------------------


def run_stock_flow(scenario: dict, parameters: dict, seed: int) -> dict:
    """Fluid backlog model with exact request conservation.

    Each step admits as many offered requests as queue capacity allows, then
    serves up to the configured service capacity. The accounting identity
    offered = completed + rejected + backlog holds exactly at every step.
    """
    rng = random.Random(seed)
    duration = float(scenario["workload"]["duration"])
    warmup = float(scenario["workload"]["warmup"])
    step = float(parameters.get("time_step", 0.1))
    require(step > 0.0, "stock-flow time step must be positive")
    arrival_rate = float(parameters["arrival_rate"])
    servers = int(parameters["servers"])
    service_mean = float(parameters["service_time"]["mean"])
    capacity = int(parameters["queue_capacity"])
    service_rate = servers / service_mean if service_mean > 0.0 else 0.0
    backlog = 0.0
    completed = 0.0
    rejected = 0.0
    offered = 0.0
    completed_window = 0.0
    rejected_window = 0.0
    offered_window = 0.0
    samples: list[float] = []
    steps = int(math.ceil(duration / step))
    for index in range(steps):
        now = index * step
        arrivals = arrival_rate * step
        # A fluid model uses the declared rate directly; stochastic arrivals are
        # represented by the discrete-event model, not by per-step sampling here.
        arrivals = arrival_rate * step
        offered += arrivals
        room = max(0.0, capacity - backlog)
        admitted = min(arrivals, room)
        rejected += arrivals - admitted
        service = min(backlog + admitted, service_rate * step)
        backlog = backlog + admitted - service
        completed += service
        if now >= warmup:
            samples.append(backlog)
            offered_window += arrivals
            rejected_window += arrivals - admitted
            completed_window += service
        require(backlog >= -1e-9, "negative backlog")
    measurement = max(duration - warmup, 1e-9)
    conservation = abs(offered - (completed + rejected + backlog)) < 1e-6
    throughput = completed_window / measurement
    mean_backlog = statistics.fmean(samples) if samples else 0.0
    little_time = mean_backlog / throughput if throughput > 0.0 else 0.0
    return {
        "offered": offered,
        "completed": completed,
        "rejected": rejected,
        "backlog_end": backlog,
        "success_rate": completed_window / offered_window if offered_window else 0.0,
        "rejection_rate": rejected_window / offered_window if offered_window else 0.0,
        "timeout_rate": 0.0,
        "throughput": throughput,
        "latency_mean": little_time,
        "latency_p95": percentile(samples, 0.95) / throughput if throughput else 0.0,
        "latency_p99": percentile(samples, 0.99) / throughput if throughput else 0.0,
        "mean_queue_length": mean_backlog,
        "max_queue_length": max(samples) if samples else 0.0,
        "server_utilization": min(1.0, throughput * service_mean / servers) if servers else 0.0,
        "retry_amplification": 1.0,
        "cost_per_1k_success": (servers * float(parameters["cost_per_server_hour"])
                               * (measurement / 3600.0) / completed_window * 1000.0) if completed_window else 0.0,
        "served": completed,
        "conservation_ok": conservation,
    }


# ---------------------------------------------------------------------------
# Staged modernization model
# ---------------------------------------------------------------------------


def run_modernization(scenario: dict, parameters: dict, seed: int) -> dict:
    """Staged traffic shift with dual-write lag, reconciliation and rollback.

    The model is deliberately synthetic. It computes a divergence backlog from
    target throughput and dual-write lag, drains it at the reconciliation
    capacity, and records the time needed to drain after a rollback trigger. It
    does not claim measured migration behavior.
    """
    rng = random.Random(seed)
    duration = float(scenario["workload"]["duration"])
    warmup = float(scenario["workload"]["warmup"])
    step = float(parameters.get("time_step", 1.0))
    arrival_rate = float(parameters["arrival_rate"])
    target_capacity = float(parameters["target_capacity"])
    legacy_capacity = float(parameters.get("legacy_capacity", 1e12))
    reconciliation_capacity = float(parameters["reconciliation_capacity"])
    dual_write_lag = float(parameters["dual_write_lag"])
    rollback_at = float(parameters["rollback_at"])
    rollback_drain = float(parameters["rollback_drain"])
    stages = parameters["stages"]
    backlog = 0.0
    divergence = 0.0
    max_divergence = 0.0
    cutover_done = False
    rollback_started = False
    rollback_end = None
    completed = 0.0
    rejected = 0.0
    offered = 0.0
    completed_window = 0.0
    rejected_window = 0.0
    offered_window = 0.0
    target_served_total = 0.0
    samples: list[float] = []
    steps = int(math.ceil(duration / step))
    for index in range(steps):
        now = index * step
        share = 0.0
        for stage in stages:
            if now >= float(stage["at"]):
                share = float(stage["target_share"])
        if rollback_started:
            share = 0.0
        offered += arrival_rate * step
        target_traffic = arrival_rate * share
        target_served = min(target_traffic * step, target_capacity * step)
        legacy_served = min((arrival_rate - target_traffic) * step, legacy_capacity * step)
        completed += target_served + legacy_served
        target_served_total += target_served
        rejected += max(0.0, arrival_rate * step - target_served - legacy_served)
        backlog += target_served * dual_write_lag
        drained = min(backlog, reconciliation_capacity * step)
        backlog -= drained
        divergence = max(0.0, divergence + (backlog - reconciliation_capacity * step) * step * 0.001)
        max_divergence = max(max_divergence, divergence)
        if not cutover_done and share >= 1.0:
            cutover_done = True
        if not rollback_started and now >= rollback_at:
            rollback_started = True
        if rollback_started and rollback_end is None and backlog <= 1e-9 and divergence <= 1e-9:
            rollback_end = now
        if now >= warmup:
            samples.append(backlog)
            offered_window += arrival_rate * step
            completed_window += target_served + legacy_served
            rejected_window += max(0.0, arrival_rate * step - target_served - legacy_served)
    measurement = max(duration - warmup, 1e-9)
    latency = dual_write_lag if target_served_total > 0.0 else 0.0
    rollback_applicable = rollback_at <= duration
    return {
        "offered": offered,
        "completed": completed,
        "rejected": rejected,
        "success_rate": completed_window / offered_window if offered_window else 0.0,
        "rejection_rate": rejected_window / offered_window if offered_window else 0.0,
        "timeout_rate": 0.0,
        "throughput": completed_window / measurement,
        "latency_mean": latency,
        "latency_p95": latency,
        "latency_p99": latency,
        "mean_queue_length": statistics.fmean(samples) if samples else 0.0,
        "max_queue_length": max(samples) if samples else 0.0,
        "server_utilization": 0.0,
        "retry_amplification": 1.0,
        "cost_per_1k_success": 0.0,
        "max_divergence": max_divergence,
        "rollback_seconds": ((rollback_end - rollback_at) if rollback_end is not None
                             else (0.0 if not rollback_applicable else None)),
        "rollback_completed": 1.0 if (rollback_end is not None or not rollback_applicable) else 0.0,
        "cutover_completed": cutover_done,
        "served": completed,
        "conservation_ok": abs(offered - completed - rejected) < 1e-6,
    }


# ---------------------------------------------------------------------------
# Scenario execution
# ---------------------------------------------------------------------------


def base_parameters(scenario: dict) -> dict:
    config = dict(scenario["configuration"])
    workload = scenario["workload"]
    config["arrival_rate"] = float(workload["arrival_process"]["rate"])
    config["arrival_process"] = workload["arrival_process"]["kind"]
    config.setdefault("time_step", 0.1)
    config.setdefault("target_share", 1.0)
    config.setdefault("target_capacity", float(config["servers"]) / float(config["service_time"]["mean"]) if config["servers"] else 0.0)
    config.setdefault("reconciliation_capacity", 10.0)
    config.setdefault("dual_write_lag", 0.5)
    config.setdefault("rollback_at", 1e9)
    config.setdefault("rollback_drain", 5.0)
    config.setdefault("legacy_capacity", 1e12)
    config.setdefault("stages", [])
    for draw in scenario["uncertainty"].get("parameter_draws", []):
        name = draw["parameter"]
        if name in config:
            if isinstance(config[name], dict) and draw["distribution"] == "normal":
                config[name]["mean"] = float(draw.get("mean") or config[name]["mean"])
        elif name not in config:
            config[name] = float(draw.get("mean") or 0.0)
    return config


def apply_parameter(parameters: dict, name: str, value: float) -> dict:
    updated = json.loads(json.dumps(parameters))
    if name == "arrival_rate":
        updated["arrival_rate"] = max(0.0, value)
    elif name == "service_mean":
        updated["service_time"]["mean"] = max(1e-6, value)
    elif name == "timeout":
        updated["timeout"] = max(1e-6, value)
    elif name == "servers":
        updated["servers"] = max(0, int(round(value)))
    elif name == "queue_capacity":
        updated["queue_capacity"] = max(0, int(round(value)))
    elif name == "target_share":
        updated["target_share"] = min(1.0, max(0.0, value))
    elif name == "dual_write_lag":
        updated["dual_write_lag"] = max(0.0, value)
    elif name == "reconciliation_capacity":
        updated["reconciliation_capacity"] = max(1e-6, value)
    elif name == "legacy_capacity":
        updated["legacy_capacity"] = max(1e-6, value)
    else:
        updated[name] = value
    return updated


def sample_draw(rng: random.Random, draw: dict) -> float:
    kind = draw["distribution"]
    mean = draw.get("mean")
    sd = draw.get("sd")
    low = draw.get("low")
    high = draw.get("high")
    if kind == "fixed":
        require(mean is not None, "fixed draw requires mean")
        return float(mean)
    if kind == "normal":
        require(mean is not None and sd is not None, "normal draw requires mean and sd")
        return rng.gauss(float(mean), float(sd))
    if kind == "uniform":
        require(low is not None and high is not None, "uniform draw requires low and high")
        return rng.uniform(float(low), float(high))
    if kind == "lognormal":
        require(mean is not None and sd is not None, "lognormal draw requires mean and sd")
        require(float(mean) > 0.0 and float(sd) > 0.0, "lognormal parameters must be positive")
        return sample_lognormal(rng, float(mean), float(sd) / float(mean))
    raise EngineError("unsupported uncertainty distribution: " + str(kind))


def get_parameter(parameters: dict, name: str) -> float:
    if name == "service_mean":
        return float(parameters["service_time"]["mean"])
    return float(parameters[name])


def _correlation_matrix(scenario: dict, names: list[str]) -> list[list[float]]:
    size = len(names)
    index = {name: position for position, name in enumerate(names)}
    matrix = [[1.0 if row == column else 0.0 for column in range(size)] for row in range(size)]
    for pair in scenario["uncertainty"].get("correlations", []):
        left, right = pair["left"], pair["right"]
        require(left in index and right in index,
                "correlation names a parameter without a draw: " + left + "/" + right)
        coefficient = float(pair["coefficient"])
        require(-1.0 <= coefficient <= 1.0, "correlation coefficient out of range")
        matrix[index[left]][index[right]] = coefficient
        matrix[index[right]][index[left]] = coefficient
    return matrix


def _cholesky(matrix: list[list[float]]) -> list[list[float]]:
    size = len(matrix)
    lower = [[0.0] * size for _ in range(size)]
    for row in range(size):
        for column in range(row + 1):
            total = matrix[row][column] - sum(lower[row][k] * lower[column][k]
                                              for k in range(column))
            if row == column:
                require(total > 1e-12, "correlation matrix is not positive definite")
                lower[row][column] = math.sqrt(total)
            else:
                lower[row][column] = total / lower[column][column]
    return lower


def _inverse_draw(draw: dict, uniform: float) -> float:
    kind = draw["distribution"]
    mean = draw.get("mean")
    sd = draw.get("sd")
    low = draw.get("low")
    high = draw.get("high")
    require(0.0 < uniform < 1.0, "uniform draw must be strictly between zero and one")
    if kind == "fixed":
        require(mean is not None, "fixed draw requires mean")
        return float(mean)
    if kind == "uniform":
        require(low is not None and high is not None, "uniform draw requires low and high")
        return float(low) + (float(high) - float(low)) * uniform
    z = statistics.NormalDist().inv_cdf(uniform)
    if kind == "normal":
        require(mean is not None and sd is not None, "normal draw requires mean and sd")
        return float(mean) + float(sd) * z
    if kind == "lognormal":
        require(mean is not None and sd is not None, "lognormal draw requires mean and sd")
        require(float(mean) > 0.0 and float(sd) > 0.0, "lognormal parameters must be positive")
        cv = float(sd) / float(mean)
        sigma2 = math.log(1.0 + cv * cv)
        mu = math.log(float(mean)) - sigma2 / 2.0
        return math.exp(mu + math.sqrt(sigma2) * z)
    raise EngineError("unsupported uncertainty distribution: " + str(kind))


def sample_row(scenario: dict, rng: random.Random) -> dict:
    parameters = base_parameters(scenario)
    draws = scenario["uncertainty"].get("parameter_draws", [])
    if not draws:
        return parameters
    names = [draw["parameter"] for draw in draws]
    lower = _cholesky(_correlation_matrix(scenario, names))
    independent = [rng.gauss(0.0, 1.0) for _ in draws]
    correlated = [sum(lower[row][column] * independent[column]
                      for column in range(len(draws))) for row in range(len(draws))]
    for draw, z in zip(draws, correlated):
        uniform = statistics.NormalDist().cdf(z)
        value = _inverse_draw(draw, uniform)
        parameters = apply_parameter(parameters, draw["parameter"], value)
    return parameters

def run_replication(model: dict, scenario: dict, parameters: dict, seed: int) -> dict:
    kind = model["dynamics"]["kind"]
    model_id = model["id"]
    if "modernization" in model_id or kind == "hybrid":
        return run_modernization(scenario, parameters, seed)
    if kind == "discrete-event" or "checkout" in model_id:
        return CheckoutSimulation(scenario, parameters, seed).run()
    return run_stock_flow(scenario, parameters, seed)


def aggregate(values: list[float]) -> tuple[float, float, float, float]:
    if not values:
        return 0.0, 0.0, 0.0, 0.0
    mean = statistics.fmean(values)
    if len(values) < 2:
        return mean, 0.0, mean, mean
    sd = statistics.stdev(values)
    se = sd / math.sqrt(len(values))
    return mean, se, mean - Z_975 * se, mean + Z_975 * se


METRIC_UNITS = {
    "success_rate": "ratio",
    "rejection_rate": "ratio",
    "timeout_rate": "ratio",
    "throughput": "request/second",
    "latency_mean": "second",
    "latency_p95": "second",
    "latency_p99": "second",
    "mean_queue_length": "request",
    "max_queue_length": "request",
    "server_utilization": "ratio",
    "retry_amplification": "ratio",
    "cost_per_1k_success": "cost-unit/1000 successes",
    "rollback_completed": "ratio",
    "max_divergence": "record",
    "rollback_seconds": "second",
}


def run_scenario(model: dict, scenario: dict, model_path: str, scenario_path: str,
                 seed_override: int | None = None) -> dict:
    require(model["id"] == scenario["model_id"], "scenario model_id mismatch")
    replications = int(scenario["replications"])
    base_seed = int(seed_override if seed_override is not None else scenario["seed"]["base"])
    per_replication: list[dict] = []
    for rep in range(replications):
        seed = base_seed + rep
        rng = random.Random(base_seed + 100000 + rep)
        parameters = sample_row(scenario, rng)
        result = run_replication(model, scenario, parameters, seed)
        for key in ("conservation_ok",):
            require(result[key] is True, "invariant failed in replication " + str(rep))
        per_replication.append(result)

    metric_names = [
        "success_rate", "rejection_rate", "timeout_rate", "throughput",
        "latency_mean", "latency_p95", "latency_p99", "mean_queue_length",
        "max_queue_length", "server_utilization", "retry_amplification",
        "cost_per_1k_success",
    ]
    if any("max_divergence" in r for r in per_replication):
        metric_names.extend(["max_divergence", "rollback_seconds", "rollback_completed"])
    metrics: dict[str, dict] = {}
    for name in metric_names:
        values = [float(r[name]) for r in per_replication if r.get(name) is not None]
        if not values and name == "rollback_seconds":
            values = [float(scenario["workload"]["duration"]) for _ in per_replication]
        mean, se, low, high = aggregate(values)
        if name in {"success_rate", "rejection_rate", "timeout_rate",
                    "server_utilization", "rollback_completed"}:
            low, high = max(0.0, low), min(1.0, high)
        elif name in {"latency_mean", "latency_p95", "latency_p99",
                      "mean_queue_length", "max_queue_length", "retry_amplification",
                      "cost_per_1k_success", "max_divergence", "rollback_seconds"}:
            low, high = max(0.0, low), max(0.0, high)
        metrics[name] = {
            "value": mean,
            "unit": METRIC_UNITS.get(name, "unit"),
            "replications": len(values),
            "standard_error": se,
            "ci_low": low,
            "ci_high": high,
        }
    totals = {
        key: sum(float(result.get(key, 0.0)) for result in per_replication)
        for key in ("offered", "completed", "rejected", "failed", "in_system_at_end", "backlog_end")
    }
    invariants = {
        "conservation_ok": all(result.get("conservation_ok") is True for result in per_replication),
        "checks": [{
            "name": "request-conservation",
            "status": "pass" if all(result.get("conservation_ok") is True for result in per_replication) else "fail",
            "detail": ("offered=" + str(round(totals["offered"], 6))
                       + "; completed=" + str(round(totals["completed"], 6))
                       + "; rejected=" + str(round(totals["rejected"], 6))
                       + "; failed=" + str(round(totals["failed"], 6))
                       + "; in_system=" + str(round(totals["in_system_at_end"], 6))
                       + "; backlog_end=" + str(round(totals["backlog_end"], 6))),
        }],
    }
    primary = metrics["success_rate"]
    relative_error = primary["standard_error"] / abs(primary["value"]) if primary["value"] else 0.0
    convergence = {
        "status": "converged" if relative_error <= 0.02 else "insufficient-sample",
        "metric": "success_rate",
        "relative_error": relative_error,
        "threshold": 0.02,
        "replications": replications,
    }
    engine_sha = file_sha256(Path(__file__).resolve())
    provenance = {
        "model_sha256": file_sha256(model_path),
        "scenario_sha256": file_sha256(scenario_path),
        "engine_sha256": engine_sha,
        "seed_base": base_seed,
        "replications": replications,
        "input_sha256": sha256_json({"model": model, "scenario": scenario,
                                     "engine_version": ENGINE_VERSION,
                                     "engine_sha256": engine_sha}),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "invocation": ("python3 scripts/v12_engine.py run --model "
                       + display_path(model_path) + " --scenario " + display_path(scenario_path)),
    }
    uncertainty = {
        "method": "gaussian-copula" if scenario["uncertainty"].get("correlations") else "replication",
        "draws": replications,
        "correlated_inputs": bool(scenario["uncertainty"].get("correlations")),
        "notes": "Independent replications with seeded parameter draws. Correlations are declared in the scenario and are not inferred from data.",
    }
    return {
        "schema_version": 1,
        "id": scenario.get("run_id", "tycho.run." + scenario["id"].split(".")[-1]),
        "version": "1.0.0",
        "model_id": model["id"],
        "scenario_id": scenario["id"],
        "engine": {"name": ENGINE_NAME, "version": ENGINE_VERSION, "deterministic": True},
        "provenance": provenance,
        "metrics": metrics,
        "convergence": convergence,
        "invariants": invariants,
        "uncertainty": uncertainty,
        "sensitivity": [],
        "limitations": [
            "Synthetic workload; no production measurement is claimed.",
            "Metrics are conditional on the declared model and scenario assumptions.",
            "Confidence intervals use a normal approximation across replications.",
        ],
        "result_sha256": None,
    }


def finalize_run(run: dict) -> dict:
    body = {k: v for k, v in run.items() if k != "result_sha256"}
    run["result_sha256"] = sha256_json(body)
    return run


def replay(run_path: str | Path, model_path: str | Path, scenario_path: str | Path) -> dict:
    run = load_json(run_path)
    model = load_json(model_path)
    scenario = load_json(scenario_path)
    require(run["model_id"] == model["id"], "replay model mismatch")
    require(run["scenario_id"] == scenario["id"], "replay scenario mismatch")
    require(run["provenance"]["model_sha256"] == file_sha256(model_path), "model hash changed")
    require(run["provenance"]["scenario_sha256"] == file_sha256(scenario_path), "scenario hash changed")
    require(run["provenance"].get("engine_sha256") == file_sha256(Path(__file__).resolve()),
            "engine source changed since the run")
    regenerated = run_scenario(model, scenario, str(model_path), str(scenario_path))
    if run.get("sensitivity"):
        draws = run["sensitivity"][0]["replications"]
        regenerated["sensitivity"] = sensitivity(model, scenario, str(model_path),
                                                 str(scenario_path), draws=draws)
    finalize_run(regenerated)
    require(regenerated["result_sha256"] == run["result_sha256"], "replay result hash mismatch")
    return {"status": "replayed", "result_sha256": run["result_sha256"]}


# ---------------------------------------------------------------------------
# Sensitivity analysis
# ---------------------------------------------------------------------------


def _solve_linear(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting for a small dense system."""
    size = len(vector)
    a = [row[:] + [vector[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(a[row][column]))
        if abs(a[pivot][column]) < 1e-12:
            raise EngineError("singular sensitivity system")
        a[column], a[pivot] = a[pivot], a[column]
        scale = a[column][column]
        a[column] = [value / scale for value in a[column]]
        for row in range(size):
            if row == column:
                continue
            factor = a[row][column]
            if factor == 0.0:
                continue
            a[row] = [value - factor * other for value, other in zip(a[row], a[column])]
    return [a[index][size] for index in range(size)]


def sensitivity(model: dict, scenario: dict, model_path: str, scenario_path: str,
                draws: int = 48) -> list[dict]:
    """Quadratic response-surface variance decomposition for 1-2 inputs.

    The screen fits a quadratic response surface to sampled model outputs and
    decomposes the fitted variance into main and interaction terms. It is a
    screening approximation, not an exact pick-freeze Sobol estimate. The
    returned total-order indices are always at least the first-order indices
    because they include the fitted interaction variance.
    """
    uncertain = scenario["uncertainty"].get("parameter_draws", [])
    require(1 <= len(uncertain) <= 2,
            "response-surface sensitivity supports 1-2 uncertain parameters")
    names = [item["parameter"] for item in uncertain]
    rng = random.Random(int(scenario["seed"]["base"]) + 700001)

    def run_row(row: dict, seed: int) -> float:
        if "modernization" in model["id"]:
            result = run_modernization(scenario, row, seed)
        elif model["dynamics"]["kind"] == "discrete-event":
            result = CheckoutSimulation(scenario, row, seed).run()
        else:
            result = run_stock_flow(scenario, row, seed)
        return float(result["success_rate"])

    rows: list[dict] = []
    outputs: list[float] = []
    for index in range(draws * 2):
        row = sample_row(scenario, rng)
        rows.append(row)
        outputs.append(run_row(row, int(scenario["seed"]["base"]) + 800000 + index))

    columns = [[get_parameter(row, name) for row in rows] for name in names]
    standardized: list[list[float]] = []
    for values in columns:
        mean = statistics.fmean(values)
        sd = statistics.pstdev(values)
        standardized.append([0.0 if sd == 0.0 else (value - mean) / sd for value in values])

    if len(names) == 1:
        x1 = standardized[0]
        terms = [[1.0, value, value * value] for value in x1]
        coefficients = _solve_linear(
            [[sum(row[i] * row[j] for row in terms) for j in range(3)] for i in range(3)],
            [sum(row[i] * value for row, value in zip(terms, outputs)) for i in range(3)],
        )
        b1, b11 = coefficients[1], coefficients[2]
        variance = b1 * b1 + 2.0 * b11 * b11
        if variance <= 1e-15:
            return [{"parameter": names[0], "first_order_index": 0.0,
                     "total_order_index": 0.0, "method": "quadratic-response-surface",
                     "replications": draws}]
        return [{"parameter": names[0], "first_order_index": 1.0,
                 "total_order_index": 1.0, "method": "quadratic-response-surface",
                 "replications": draws}]

    x1, x2 = standardized
    terms = [[1.0, a, b, a * b, a * a, b * b] for a, b in zip(x1, x2)]
    matrix = [[sum(row[i] * row[j] for row in terms) for j in range(6)] for i in range(6)]
    vector = [sum(row[i] * value for row, value in zip(terms, outputs)) for i in range(6)]
    coefficients = _solve_linear(matrix, vector)
    _, b1, b2, b12, b11, b22 = coefficients
    var_main_1 = b1 * b1 + 2.0 * b11 * b11
    var_main_2 = b2 * b2 + 2.0 * b22 * b22
    var_interaction = b12 * b12
    var_total = var_main_1 + var_main_2 + var_interaction
    if var_total <= 1e-15:
        return [{"parameter": name, "first_order_index": 0.0,
                 "total_order_index": 0.0, "method": "quadratic-response-surface",
                 "replications": draws} for name in names]
    first_1 = max(0.0, min(1.0, var_main_1 / var_total))
    first_2 = max(0.0, min(1.0, var_main_2 / var_total))
    total_1 = max(first_1, min(1.0, (var_main_1 + var_interaction) / var_total))
    total_2 = max(first_2, min(1.0, (var_main_2 + var_interaction) / var_total))
    return [
        {"parameter": names[0], "first_order_index": first_1,
         "total_order_index": total_1, "method": "quadratic-response-surface",
         "replications": draws},
        {"parameter": names[1], "first_order_index": first_2,
         "total_order_index": total_2, "method": "quadratic-response-surface",
         "replications": draws},
    ]


# ---------------------------------------------------------------------------
# Reference checks and CLI
# ---------------------------------------------------------------------------


def reference_checks() -> dict:
    """Small analytic and invariant checks used by tests and CI-free validation."""
    ok = True
    details = []

    # Conservation and non-negativity in the fluid model.
    scenario = {
        "id": "tycho.scenario.reference-stock-flow",
        "model_id": "tycho.model.order-intake",
        "workload": {"duration": 600.0, "warmup": 60.0, "time_unit": "second",
                     "arrival_process": {"kind": "deterministic", "rate": 10.0, "unit": "request/second"}},
        "configuration": {"servers": 8, "service_time": {"kind": "deterministic", "mean": 0.5, "cv": 0.01},
                          "queue_capacity": 100, "timeout": 2.0, "max_attempts": 1,
                          "retry_backoff": {"kind": "none", "base": 0.0, "jitter": "none"},
                          "bulkhead": 1000, "cost_per_server_hour": 0.1},
        "uncertainty": {"parameter_draws": [], "correlations": []},
        "replications": 2,
        "seed": {"base": 7, "scheme": "reference"},
        "metrics": [{"id": "success_rate", "unit": "ratio", "direction": "higher", "business_comparable": True}],
        "constraints": [], "evidence_status": "assumed", "validity_limits": ["reference only"],
    }
    params = base_parameters(scenario)
    flow = run_stock_flow(scenario, params, 7)
    details.append(("stock-flow-conservation", flow["conservation_ok"]))
    details.append(("stock-flow-non-negative", flow["backlog_end"] >= 0.0))
    ok = ok and flow["conservation_ok"] and flow["backlog_end"] >= 0.0

    # Exponential decay reference: S(t) = S0 * exp(-d t) under Euler integration.
    decay = run_stock_flow(
        scenario,
        {**params, "arrival_rate": 0.0, "servers": 0, "queue_capacity": 1000000},
        7,
    )
    details.append(("zero-arrival-zero-service", decay["offered"] == 0.0 and decay["completed"] == 0.0))
    ok = ok and decay["offered"] == 0.0 and decay["completed"] == 0.0

    # Event ordering: same-time events retain insertion order.
    queue = EventQueue()
    queue.schedule(1.0, 2, "second")
    queue.schedule(1.0, 0, "first")
    queue.schedule(1.0, 1, "middle")
    order = [queue.pop().kind for _ in range(3)]
    details.append(("event-ordering", order == ["first", "middle", "second"]))
    ok = ok and order == ["first", "middle", "second"]

    return {"status": "pass" if ok else "fail", "checks": details}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="Run one model/scenario pair and write a run record")
    run.add_argument("--model", required=True)
    run.add_argument("--scenario", required=True)
    run.add_argument("--out", required=True)
    run.add_argument("--seed", type=int, default=None)
    run.add_argument("--run-id", default=None)
    run.add_argument("--sensitivity", action="store_true")
    replay_cmd = sub.add_parser("replay", help="Recompute a stored run and compare its hash")
    replay_cmd.add_argument("--run", required=True)
    replay_cmd.add_argument("--model", required=True)
    replay_cmd.add_argument("--scenario", required=True)
    sub.add_parser("verify", help="Run internal reference checks")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "verify":
        result = reference_checks()
        print(json.dumps(result, indent=2))
        return 0 if result["status"] == "pass" else 1
    if args.command == "replay":
        print(json.dumps(replay(args.run, args.model, args.scenario), indent=2))
        return 0
    model = load_json(args.model)
    scenario = load_json(args.scenario)
    if args.run_id:
        scenario["run_id"] = args.run_id
    run = run_scenario(model, scenario, args.model, args.scenario, args.seed)
    if args.sensitivity:
        run["sensitivity"] = sensitivity(model, scenario, args.model, args.scenario)
    finalize_run(run)
    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(run, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(target), "result_sha256": run["result_sha256"],
                      "convergence": run["convergence"]}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (EngineError, OSError, KeyError, ValueError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
