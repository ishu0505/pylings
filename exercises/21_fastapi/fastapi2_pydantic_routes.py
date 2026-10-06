"""
fastapi2_pydantic_routes — Request/Response models & Status Codes   difficulty: medium

Build an Item API:
- `ItemCreate` schema: `name: str` (min_length 2), `price: float` (gt 0)
- `ItemResponse` schema: `id: str`, `name: str`, `price: float`
- `POST /items` (status_code 201): saves item in memory, returns ItemResponse
- `GET /items/{item_id}`: returns ItemResponse; if missing, raises HTTPException(404, "Item not found")
"""

# I AM NOT DONE

# Concept Tip: Pydantic request models validate input automatically; bad input returns HTTP 422.
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient

app = FastAPI()

# TODO: implement schemas and routes


# ---------------------------------------------------------------- tests


def test_items_crud():
    client = TestClient(app)

    # Valid create
    r = client.post("/items", json={"name": "Widget", "price": 19.99})
    assert r.status_code == 201
    item_id = r.json()["id"]
    assert r.json()["name"] == "Widget"

    # Get created
    r_get = client.get(f"/items/{item_id}")
    assert r_get.status_code == 200
    assert r_get.json()["id"] == item_id

    # 404 on missing
    r_missing = client.get("/items/nonexistent")
    assert r_missing.status_code == 404

    # 422 on invalid price (<= 0)
    r_bad = client.post("/items", json={"name": "Bad", "price": -5.0})
    assert r_bad.status_code == 422
