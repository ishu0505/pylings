"""
oop5_dataclasses — Solution
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class JobSpec:
    id: str
    task_name: str
    priority: int = 1


@dataclass
class ExecutionContext:
    trace_id: str
    tags: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- tests
import pytest
from dataclasses import FrozenInstanceError


def test_job_spec():
    job = JobSpec("j-1", "embed_text")
    assert job.id == "j-1"
    assert job.priority == 1
    with pytest.raises(FrozenInstanceError):
        job.priority = 2


def test_execution_context():
    ctx1 = ExecutionContext("t-1")
    ctx2 = ExecutionContext("t-2")
    ctx1.tags.append("gpu")
    assert ctx1.tags == ["gpu"]
    assert ctx2.tags == []
