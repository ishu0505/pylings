"""
oop5_dataclasses — Python Dataclasses                   difficulty: easy

1. `JobSpec`:
   - `@dataclass(frozen=True)`
   - fields: `id: str`, `task_name: str`, `priority: int = 1`
   - Trying to mutate fields after creation raises FrozenInstanceError.

2. `ExecutionContext`:
   - `@dataclass`
   - fields: `trace_id: str`, `tags: list[str] = field(default_factory=list)`
"""

# I AM NOT DONE

# Concept Tip: `dataclass` generates `__init__`, `__repr__`, `__eq__` automatically.
from dataclasses import dataclass, field


# TODO: implement JobSpec and ExecutionContext


# ---------------------------------------------------------------- tests
import pytest
from dataclasses import FrozenInstanceError


def test_job_spec():
    job = JobSpec("j-1", "embed_text")
    assert job.id == "j-1"
    assert job.priority == 1
    with pytest.raises(FrozenInstanceError):
        job.priority = 2  # frozen!


def test_execution_context():
    ctx1 = ExecutionContext("t-1")
    ctx2 = ExecutionContext("t-2")
    ctx1.tags.append("gpu")
    assert ctx1.tags == ["gpu"]
    assert ctx2.tags == []  # default factory prevents shared state
