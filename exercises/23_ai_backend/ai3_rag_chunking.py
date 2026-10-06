"""
ai3_rag_chunking — RAG Text Chunking                   difficulty: medium

Embedding models have strict context limits (e.g. 512 tokens).
Implement `chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]`:
- Splits text by whitespace into words.
- Generates chunks where each chunk has up to chunk_size words.
- Each successive chunk starts `(chunk_size - overlap)` words after the previous chunk start.
- Re-joins words with single spaces.
- Raises ValueError if overlap >= chunk_size or chunk_size <= 0.
"""

# I AM NOT DONE

# Concept Tip: Overlap prevents cutting sentences or semantic thoughts directly across chunk boundaries.


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


def test_chunk_text():
    words = [f"word{i}" for i in range(10)]
    text = " ".join(words)

    chunks = chunk_text(text, chunk_size=4, overlap=1)
    # step = 4 - 1 = 3
    # chunk 0: words 0..4
    # chunk 1: words 3..7
    # chunk 2: words 6..10
    # chunk 3: words 9..10
    assert len(chunks) == 4
    assert chunks[0] == "word0 word1 word2 word3"
    assert chunks[1] == "word3 word4 word5 word6"


def test_chunk_text_invalid_params():
    with pytest.raises(ValueError):
        chunk_text("hello world", chunk_size=2, overlap=2)
