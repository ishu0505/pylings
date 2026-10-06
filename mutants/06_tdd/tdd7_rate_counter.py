TARGET = "RateCounter"


class _StrictlyGreaterThreshold:
    def __init__(self):
        self.events = []

    def record(self, timestamp):
        self.events.append(timestamp)

    def count(self, now, window_seconds):
        threshold = now - window_seconds
        # Bug: strictly greater drops events on exact boundary
        return sum(1 for ts in self.events if threshold < ts <= now)


class _IncludesFutureEvents:
    def __init__(self):
        self.events = []

    def record(self, timestamp):
        self.events.append(timestamp)

    def count(self, now, window_seconds):
        threshold = now - window_seconds
        # Bug: ignores now upper bound
        return sum(1 for ts in self.events if threshold <= ts)


MUTANTS = {
    "off-by-one: drops events on the exact window boundary": _StrictlyGreaterThreshold,
    "does not cap events at now (counts future timestamps)": _IncludesFutureEvents,
}
