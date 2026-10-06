# 23 AI Backend Patterns

Building production AI backends requires resilience against model latency, rate limits, non-deterministic text outputs, and token costs.

### Key Architectural Patterns:
1. **Exponential Backoff with Jitter:** When an LLM API returns HTTP 429, retry after $base 	imes 2^{attempt} + jitter$ seconds.
2. **Token Bucket Rate Limiting:** Enforce requests-per-minute (RPM) and tokens-per-minute (TPM) locally before hitting third-party providers.
3. **Structured Outputs with Self-Correction:** Validate LLM outputs against Pydantic models. On validation error, feed the error back to the model once to self-correct.
4. **RAG Vector Search:** Efficiently chunk documents and compute cosine similarity across vector embeddings.
5. **Streaming (SSE):** Stream tokens incrementally using Server-Sent Events to minimize perceived user latency (TTFT: Time to First Token).
