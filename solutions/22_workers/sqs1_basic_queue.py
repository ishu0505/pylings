"""
sqs1_basic_queue — Solution
"""
import boto3
from moto import mock_aws


def create_queue(sqs, name: str) -> str:
    resp = sqs.create_queue(QueueName=name)
    return resp["QueueUrl"]


def send_task(sqs, queue_url: str, body: str) -> str:
    resp = sqs.send_message(QueueUrl=queue_url, MessageBody=body)
    return resp["MessageId"]


def receive_and_delete(sqs, queue_url: str) -> str | None:
    resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=0)
    messages = resp.get("Messages", [])
    if not messages:
        return None
    msg = messages[0]
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
    return msg["Body"]


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

    assert receive_and_delete(sqs, q_url) is None
