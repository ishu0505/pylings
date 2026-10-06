"""
ai3_rag_chunking — Solution
"""


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= 0 or overlap >= chunk_size:
        raise ValueError("invalid chunk_size or overlap")
    words = text.split()
    if not words:
        return []

    step = chunk_size - overlap
    chunks: list[str] = []
    i = 0

    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
        i += step

    return chunks


# ---------------------------------------------------------------- tests
import pytest


def test_chunk_text():
    words = [f"word{i}" for i in range(10)]
    text = " ".join(words)

    chunks = chunk_text(text, chunk_size=4, overlap=1)
    assert len(chunks) == 4
    assert chunks[0] == "word0 word1 word2 word3"
    assert chunks[1] == "word3 word4 word5 word6"


def test_chunk_text_invalid_params():
    with pytest.raises(ValueError):
        chunk_text("hello world", chunk_size=2, overlap=2)
