"""
fastapi2_pydantic_routes — Solution
"""
import uuid
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient

app = FastAPI()
db: dict[str, dict] = {}


class ItemCreate(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)


class ItemResponse(BaseModel):
    id: str
    name: str
    price: float


@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    item_id = str(uuid.uuid4())
    record = {"id": item_id, "name": payload.name, "price": payload.price}
    db[item_id] = record
    return record


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]


# ---------------------------------------------------------------- tests


def test_items_crud():
    client = TestClient(app)

    r = client.post("/items", json={"name": "Widget", "price": 19.99})
    assert r.status_code == 201
    item_id = r.json()["id"]
    assert r.json()["name"] == "Widget"

    r_get = client.get(f"/items/{item_id}")
    assert r_get.status_code == 200
    assert r_get.json()["id"] == item_id

    r_missing = client.get("/items/nonexistent")
    assert r_missing.status_code == 404

    r_bad = client.post("/items", json={"name": "Bad", "price": -5.0})
    assert r_bad.status_code == 422
