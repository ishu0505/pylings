"""
ai4_vector_similarity — Solution
"""
import math


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def search_top_k(query_vec: list[float], doc_vectors: list[dict], k: int = 2) -> list[dict]:
    scored = []
    for doc in doc_vectors:
        sim = cosine_similarity(query_vec, doc["vector"])
        scored.append((sim, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:k]]


# ---------------------------------------------------------------- tests


def test_vector_similarity():
    assert math.isclose(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
    assert math.isclose(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)

    docs = [
        {"id": "doc1", "vector": [1.0, 0.0]},
        {"id": "doc2", "vector": [0.8, 0.6]},
        {"id": "doc3", "vector": [0.0, 1.0]},
    ]
    query = [1.0, 0.0]
    top = search_top_k(query, docs, k=2)
    assert [d["id"] for d in top] == ["doc1", "doc2"]
