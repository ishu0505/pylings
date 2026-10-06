"""
ai2_structured_output — Self-Correcting LLM Structured Output   difficulty: medium

When requesting JSON from an LLM, responses occasionally have schema errors.
Implement `extract_structured_data(llm_fn, initial_prompt: str, schema_cls)`:
- Calls `llm_fn(initial_prompt)`
- Parses response using `schema_cls.model_validate_json(response)`
- If ValidationError or JSONDecodeError occurs:
  calls `llm_fn(f"{initial_prompt}\n\nError: {error}. Please correct.")` once.
- Parses the second response and returns the schema instance, or raises if still invalid.
"""

# I AM NOT DONE

# Concept Tip: Reflection/correction loops allow AI backends to heal malformed JSON before returning to callers.
from pydantic import BaseModel, ValidationError


def extract_structured_data(llm_fn, initial_prompt: str, schema_cls):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


class SentimentAnalysis(BaseModel):
    sentiment: str
    confidence: float


def test_extract_structured_data_heals():
    prompts_called = []
    responses = [
        '{"sentiment": "positive"}',  # missing confidence!
        '{"sentiment": "positive", "confidence": 0.95}',  # valid
    ]

    def fake_llm(prompt: str) -> str:
        prompts_called.append(prompt)
        return responses.pop(0)

    result = extract_structured_data(fake_llm, "Analyze: Great product", SentimentAnalysis)
    assert result.sentiment == "positive"
    assert result.confidence == 0.95
    assert len(prompts_called) == 2
