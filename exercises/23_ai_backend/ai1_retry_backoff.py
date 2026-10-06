"""
ai1_retry_backoff — Exponential Backoff with Jitter     difficulty: medium

When calling OpenAI/Anthropic APIs, network blips and 429 rate limits are common.
Implement `retry_with_backoff(fn, max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 10.0, sleep_fn=None, random_fn=None)`:
- Calls `fn()`.
- If `RateLimitError` is raised, waits `min(max_delay, base_delay * (2 ** attempt)) + jitter` where jitter = random_fn().
- Retries up to max_retries times. If still failing, raises RateLimitError.
"""

# I AM NOT DONE

# Concept Tip: Jitter avoids the 'thundering herd' problem where thousands of clients retry at the exact same millisecond.


class RateLimitError(Exception):
    pass


def retry_with_backoff(fn, max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 10.0, sleep_fn=None, random_fn=None):
    # TODO: implement
    raise NotImplementedError


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
    # Attempt 0 backoff: 1.0 * (2^0) + 0.1 = 1.1
    # Attempt 1 backoff: 1.0 * (2^1) + 0.1 = 2.1
    assert sleeps == [1.1, 2.1]
