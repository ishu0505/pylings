"""
ai1_retry_backoff — Solution
"""
import time
import random


class RateLimitError(Exception):
    pass


def retry_with_backoff(fn, max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 10.0, sleep_fn=None, random_fn=None):
    sleep = sleep_fn if sleep_fn is not None else time.sleep
    rand = random_fn if random_fn is not None else random.random

    for attempt in range(max_retries):
        try:
            return fn()
        except RateLimitError as err:
            if attempt == max_retries - 1:
                raise err
            delay = min(max_delay, base_delay * (2 ** attempt)) + rand()
            sleep(delay)


# ---------------------------------------------------------------- tests
import pytest


def test_retry_backoff_success_after_retries():
    calls = 0
    sleeps = []

    def flaky_llm():
        nonlocal calls
        calls += 1
        if calls < 3:
            raise RateLimitError("rate limit exceeded")
        return "response"

    result = retry_with_backoff(
        flaky_llm,
        max_retries=3,
        base_delay=1.0,
        max_delay=10.0,
        sleep_fn=sleeps.append,
        random_fn=lambda: 0.1,
    )

    assert result == "response"
    assert calls == 3
    assert sleeps == [1.1, 2.1]
