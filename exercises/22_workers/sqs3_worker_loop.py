"""
sqs3_worker_loop — The Worker Processing Loop          difficulty: medium

Implement `SQSWorker`:
- `__init__(self, sqs, queue_url: str, handler: Callable[[str], None])`
- `process_one_batch() -> tuple[int, int]`:
  receives up to 5 messages.
  Calls handler(body) for each message.
  - If handler succeeds: delete message.
  - If handler raises an exception: do NOT delete (allow retry).
  Returns `(succeeded_count, failed_count)`.
"""

# I AM NOT DONE

# Concept Tip: Leaving failed messages in the queue allows the visibility timeout to expire so another worker can retry.
from typing import Callable


class SQSWorker:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests
import boto3
from moto import mock_aws


@mock_aws
def test_worker_success_and_failure():
    sqs = boto3.client("sqs", region_name="us-east-1")
    q_url = sqs.create_queue(QueueName="work-queue")["QueueUrl"]

    sqs.send_message(QueueUrl=q_url, MessageBody="good_task")
    sqs.send_message(QueueUrl=q_url, MessageBody="bad_task")

    processed = []

    def handler(body: str) -> None:
        if body == "bad_task":
            raise RuntimeError("processing crashed")
        processed.append(body)

    worker = SQSWorker(sqs, q_url, handler)
    succ, fail = worker.process_one_batch()

    assert succ == 1
    assert fail == 1
    assert processed == ["good_task"]
