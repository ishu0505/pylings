"""
fastapi1_hello_world — Your first FastAPI app          difficulty: easy

Build a FastAPI app with:
- `GET /health`: returns `{"status": "healthy"}`
- `GET /echo?message=...`: query param, returns `{"message": message}`
"""

# I AM NOT DONE

# Concept Tip: FastAPI endpoints returning dicts are automatically serialized to JSON.
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

# TODO: implement endpoints


# ---------------------------------------------------------------- tests


def test_fastapi_endpoints():
    client = TestClient(app)
    r1 = client.get("/health")
    assert r1.status_code == 200
    assert r1.json() == {"status": "healthy"}

    r2 = client.get("/echo?message=pylings")
    assert r2.status_code == 200
    assert r2.json() == {"message": "pylings"}
