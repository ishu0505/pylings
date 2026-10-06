"""
tdd7_rate_counter — You write the tests (TDD mode)     difficulty: hard

`RateCounter`:
- `record(timestamp: float) -> None`: records an event at timestamp
- `count(now: float, window_seconds: float) -> int`:
  counts events where (now - window_seconds) <= timestamp <= now.
  Events older than now - window_seconds are ignored.

Write tests to kill all planted mutants!
"""

# I AM NOT DONE

# Concept Tip: Boundary bugs (`<` vs `<=`) are the #1 source of rate-limiter bugs in production.


class RateCounter:
    def __init__(self) -> None:
        self.events: list[float] = []

    def record(self, timestamp: float) -> None:
        self.events.append(timestamp)

    def count(self, now: float, window_seconds: float) -> int:
        threshold = now - window_seconds
        return sum(1 for ts in self.events if threshold <= ts <= now)


# ---------------------------------------------------------------- tests
# TODO: write your tests below.
