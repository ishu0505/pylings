# 22 Queue Workers: SQS & SNS

In modern AI backend architectures, heavy tasks (LLM generation, embedding indexing, video transcoding) are never run directly inside HTTP request handlers. Instead, the API enqueues a message to **AWS SQS**, returns HTTP 202 Accepted, and dedicated background workers process messages asynchronously.

### The Mental Model: The Restaurant Ticket Rail
- **Producer (Waiter):** Takes an order and clips a ticket onto the rail (`sqs.send_message`).
- **Consumer (Chef):** Grabs a ticket off the rail (`sqs.receive_message`).
- **Visibility Timeout:** While the chef cooks, the ticket is invisible to other chefs.
- **At-Least-Once Delivery:** If the chef crashes before completing the meal, the ticket becomes visible again for another chef!
- **Mandatory Deletion:** You MUST explicitly call `sqs.delete_message` using the `ReceiptHandle` once finished, or the message will re-appear.
- **Idempotency:** Because messages can be redelivered during network hiccups, your worker must be idempotent (safe to process twice).
