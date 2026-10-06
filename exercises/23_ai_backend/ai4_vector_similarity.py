"""
ai4_vector_similarity — Cosine Similarity Top-K Search   difficulty: medium

Vector databases (Pinecone, Qdrant, Chroma) match queries to text via embedding similarity.
Implement:
1. `cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float`
2. `search_top_k(query_vec: list[float], doc_vectors: list[dict], k: int = 2) -> list[dict]`:
   each doc is `{"id": str, "vector": list[float]}`.
   Returns top k docs sorted from highest similarity to lowest.
"""

# I AM NOT DONE

# Concept Tip: Cosine similarity measures the angle between vectors, independent of magnitude.
import math


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    # TODO: implement
    raise NotImplementedError


def search_top_k(query_vec: list[float], doc_vectors: list[dict], k: int = 2) -> list[dict]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_vector_similarity():
    # Identical vectors -> similarity 1.0
    assert math.isclose(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
    # Orthogonal vectors -> similarity 0.0
    assert math.isclose(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)

    docs = [
        {"id": "doc1", "vector": [1.0, 0.0]},
        {"id": "doc2", "vector": [0.8, 0.6]},
        {"id": "doc3", "vector": [0.0, 1.0]},
    ]
    query = [1.0, 0.0]
    top = search_top_k(query, docs, k=2)
    assert [d["id"] for d in top] == ["doc1", "doc2"]
