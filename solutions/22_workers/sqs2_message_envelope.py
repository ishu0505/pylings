"""
sqs2_message_envelope — Solution
"""
import json
from pydantic import BaseModel, ValidationError


class TaskEnvelope(BaseModel):
    task_id: str
    action: str
    payload: dict


def safe_parse_message(raw_body: str) -> TaskEnvelope | None:
    try:
        return TaskEnvelope.model_validate_json(raw_body)
    except (ValidationError, ValueError):
        return None


# ---------------------------------------------------------------- tests


def test_safe_parse_message():
    valid_json = '{"task_id": "t1", "action": "generate_summary", "payload": {"text": "hello"}}'
    envelope = safe_parse_message(valid_json)
    assert envelope is not None
    assert envelope.task_id == "t1"
    assert envelope.action == "generate_summary"
    assert envelope.payload == {"text": "hello"}

    assert safe_parse_message("not json") is None
    assert safe_parse_message('{"task_id": "t1"}') is None
