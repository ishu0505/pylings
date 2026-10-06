"""
sqs3_worker_loop — Solution
"""
from typing import Callable


class SQSWorker:
    def __init__(self, sqs, queue_url: str, handler: Callable[[str], None]) -> None:
        self.sqs = sqs
        self.queue_url = queue_url
        self.handler = handler

    def process_one_batch(self) -> tuple[int, int]:
        resp = self.sqs.receive_message(QueueUrl=self.queue_url, MaxNumberOfMessages=5, WaitTimeSeconds=0)
        messages = resp.get("Messages", [])
        succ = fail = 0

        for msg in messages:
            try:
                self.handler(msg["Body"])
                self.sqs.delete_message(QueueUrl=self.queue_url, ReceiptHandle=msg["ReceiptHandle"])
                succ += 1
            except Exception:
                fail += 1

        return succ, fail


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
