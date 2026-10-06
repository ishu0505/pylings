"""
sqs4_idempotent_consumer — Idempotent Worker           difficulty: medium

Because SQS guarantees at-least-once delivery, workers frequently receive duplicates.
Implement `IdempotentHandler`:
- `__init__(self, target_fn: Callable[[str], None])`
- `handle(message_id: str, body: str) -> bool`:
  executes target_fn(body) ONLY if message_id was never seen before.
  Returns True if newly processed, False if duplicate skipped.
"""

# I AM NOT DONE

# Concept Tip: Idempotency keys prevent double charging credit cards or duplicating database entries on SQS redeliveries.
from typing import Callable


class IdempotentHandler:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_idempotent_handler():
    calls = []

    def process(body: str) -> None:
        calls.append(body)

    handler = IdempotentHandler(process)

    # First delivery
    assert handler.handle("msg-001", "payment: $50") is True
    assert len(calls) == 1

    # Redelivery of same message id
    assert handler.handle("msg-001", "payment: $50") is False
    assert len(calls) == 1  # Not called again!

    # New message id
    assert handler.handle("msg-002", "payment: $20") is True
    assert len(calls) == 2
