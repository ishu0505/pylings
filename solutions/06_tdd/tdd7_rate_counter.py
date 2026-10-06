"""
tdd7_rate_counter — Solution
"""


class RateCounter:
    def __init__(self) -> None:
        self.events: list[float] = []

    def record(self, timestamp: float) -> None:
        self.events.append(timestamp)

    def count(self, now: float, window_seconds: float) -> int:
        threshold = now - window_seconds
        return sum(1 for ts in self.events if threshold <= ts <= now)


# ---------------------------------------------------------------- tests


def test_rate_counter_window():
    rc = RateCounter()
    rc.record(10.0)
    rc.record(15.0)
    rc.record(20.0)

    # Window from 10.0 to 20.0 inclusive
    assert rc.count(now=20.0, window_seconds=10.0) == 3
    # Window from 11.0 to 20.0 (excludes 10.0)
    assert rc.count(now=20.0, window_seconds=9.0) == 2


def test_rate_counter_future_events():
    rc = RateCounter()
    rc.record(10.0)
    rc.record(25.0)  # future event relative to now=20.0
    assert rc.count(now=20.0, window_seconds=15.0) == 1


def test_rate_counter_empty():
    rc = RateCounter()
    assert rc.count(now=100.0, window_seconds=60.0) == 0
