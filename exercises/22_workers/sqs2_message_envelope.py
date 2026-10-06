"""
sqs2_message_envelope — Strongly Typed SQS Envelopes   difficulty: medium

AI task messages sent via SQS require strict schemas.
Define `TaskEnvelope`:
- `task_id: str`
- `action: str`
- `payload: dict`

Implement `safe_parse_message(raw_body: str) -> TaskEnvelope | None`:
- Parses raw_body string into TaskEnvelope.
- Returns None if JSON is malformed or schema validation fails (poison message).
"""

# I AM NOT DONE

# Concept Tip: In production, malformed messages that cannot be parsed must be routed to a Dead-Letter Queue (DLQ).
from pydantic import BaseModel, ValidationError


class TaskEnvelope(BaseModel):
    # TODO: implement
    pass


def safe_parse_message(raw_body: str) -> TaskEnvelope | None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_safe_parse_message():
    valid_json = '{"task_id": "t1", "action": "generate_summary", "payload": {"text": "hello"}}'
    envelope = safe_parse_message(valid_json)
    assert envelope is not None
    assert envelope.task_id == "t1"
    assert envelope.action == "generate_summary"
    assert envelope.payload == {"text": "hello"}

    # Malformed JSON
    assert safe_parse_message("not json") is None

    # Missing required field
    assert safe_parse_message('{"task_id": "t1"}') is None
