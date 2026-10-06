"""
tdd5_test_doubles — Solution
"""
import time
from typing import Callable


class SessionManager:
    def __init__(self, ttl_seconds: float = 300, clock: Callable[[], float] | None = None) -> None:
        self.ttl = ttl_seconds
        self.clock = clock if clock is not None else time.time
        self._sessions: dict[str, tuple[str, float]] = {}
        self._counter = 0

    def create_session(self, user_id: str) -> str:
        self._counter += 1
        token = f"sess_{self._counter}"
        self._sessions[token] = (user_id, self.clock())
        return token

    def get_user(self, token: str) -> str | None:
        if token not in self._sessions:
            return None
        user_id, created_at = self._sessions[token]
        if self.clock() - created_at > self.ttl:
            del self._sessions[token]
            return None
        return user_id


# ---------------------------------------------------------------- tests


def test_session_manager_with_fake_clock():
    current_time = 1000.0

    def fake_clock() -> float:
        return current_time

    mgr = SessionManager(ttl_seconds=60, clock=fake_clock)
    token = mgr.create_session("user-42")

    assert mgr.get_user(token) == "user-42"

    current_time += 30.0
    assert mgr.get_user(token) == "user-42"

    current_time += 35.0
    assert mgr.get_user(token) is None
