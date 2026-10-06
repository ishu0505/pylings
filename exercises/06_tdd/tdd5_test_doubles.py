"""
tdd5_test_doubles — Test Doubles & Clock Injection     difficulty: medium

Build `SessionManager`:
- `__init__(self, ttl_seconds: float = 300, clock: Callable[[], float] | None = None)`
  clock defaults to `time.time` if None.
- `create_session(user_id: str) -> str`: generates a session token and stores (user_id, created_at).
- `get_user(token: str) -> str | None`: returns user_id if session exists and has NOT expired.
  If expired, returns None and deletes the session.
"""

# I AM NOT DONE

# Concept Tip: Never use `time.sleep()` in unit tests. Inject a clock and control time directly.
import time
from typing import Callable


class SessionManager:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_session_manager_with_fake_clock():
    current_time = 1000.0

    def fake_clock() -> float:
        return current_time

    mgr = SessionManager(ttl_seconds=60, clock=fake_clock)
    token = mgr.create_session("user-42")

    # Immediately valid
    assert mgr.get_user(token) == "user-42"

    # Advance time within TTL
    current_time += 30.0
    assert mgr.get_user(token) == "user-42"

    # Advance past TTL
    current_time += 35.0  # now 1065.0 > 1060.0
    assert mgr.get_user(token) is None
