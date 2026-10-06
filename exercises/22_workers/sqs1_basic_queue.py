"""
sqs1_basic_queue — SQS Message Lifecycle                difficulty: easy

Implement:
1. `create_queue(sqs, name: str) -> str`: creates SQS queue and returns QueueUrl.
2. `send_task(sqs, queue_url: str, body: str) -> str`: sends message, returns MessageId.
3. `receive_and_delete(sqs, queue_url: str) -> str | None`:
   receives up to 1 message. If found, deletes it from queue and returns its Body string.
   If queue is empty, returns None.
"""

# I AM NOT DONE

# Concept Tip: Deleting with `ReceiptHandle` signals to SQS that processing succeeded.
import boto3
from moto import mock_aws


def create_queue(sqs, name: str) -> str:
    # TODO: implement
    raise NotImplementedError


def send_task(sqs, queue_url: str, body: str) -> str:
    # TODO: implement
    raise NotImplementedError


def receive_and_delete(sqs, queue_url: str) -> str | None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


@mock_aws
def test_sqs_lifecycle():
    sqs = boto3.client("sqs", region_name="us-east-1")
    q_url = create_queue(sqs, "test-tasks")
    assert "test-tasks" in q_url

    msg_id = send_task(sqs, q_url, "process_order_123")
    assert msg_id is not None

    body = receive_and_delete(sqs, q_url)
    assert body == "process_order_123"

    # Queue should now be empty
    assert receive_and_delete(sqs, q_url) is None
