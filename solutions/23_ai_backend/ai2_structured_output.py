"""
ai2_structured_output — Solution
"""
import json
from pydantic import BaseModel, ValidationError


def extract_structured_data(llm_fn, initial_prompt: str, schema_cls):
    response = llm_fn(initial_prompt)
    try:
        return schema_cls.model_validate_json(response)
    except (ValidationError, ValueError) as err:
        correction_prompt = f"{initial_prompt} -- Error: {err}. Please correct."
        second_response = llm_fn(correction_prompt)
        return schema_cls.model_validate_json(second_response)


# ---------------------------------------------------------------- tests


class SentimentAnalysis(BaseModel):
    sentiment: str
    confidence: float


def test_extract_structured_data_heals():
    prompts_called = []
    responses = [
        '{"sentiment": "positive"}',
        '{"sentiment": "positive", "confidence": 0.95}',
    ]

    def fake_llm(prompt: str) -> str:
        prompts_called.append(prompt)
        return responses.pop(0)

    result = extract_structured_data(fake_llm, "Analyze: Great product", SentimentAnalysis)
    assert result.sentiment == "positive"
    assert result.confidence == 0.95
    assert len(prompts_called) == 2
