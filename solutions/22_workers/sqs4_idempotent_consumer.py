"""
sqs4_idempotent_consumer — Solution
"""
from typing import Callable


class IdempotentHandler:
    def __init__(self, target_fn: Callable[[str], None]) -> None:
        self.target_fn = target_fn
        self._seen_ids: set[str] = set()

    def handle(self, message_id: str, body: str) -> bool:
        if message_id in self._seen_ids:
            return False
        self._seen_ids.add(message_id)
        self.target_fn(body)
        return True


# ---------------------------------------------------------------- tests


def test_idempotent_handler():
    calls = []

    def process(body: str) -> None:
        calls.append(body)

    handler = IdempotentHandler(process)

    assert handler.handle("msg-001", "payment: $50") is True
    assert len(calls) == 1

    assert handler.handle("msg-001", "payment: $50") is False
    assert len(calls) == 1

    assert handler.handle("msg-002", "payment: $20") is True
    assert len(calls) == 2
