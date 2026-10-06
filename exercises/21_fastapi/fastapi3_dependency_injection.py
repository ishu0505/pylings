"""
fastapi3_dependency_injection — Dependency Injection   difficulty: medium

FastAPI's `Depends` system enables clean separation of concerns and effortless test mocking.
Build:
- A dependency `get_api_key(x_api_key: str = Header(...)) -> str`
- Route `GET /secure-data` which depends on `get_api_key` and returns `{"data": "secret"}`
- If api key is "valid-key", succeeds 200. Otherwise raises HTTPException(401, "Invalid key").
"""

# I AM NOT DONE

# Concept Tip: `Depends` executes a dependency function before running the route handler.
from fastapi import FastAPI, Depends, Header, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

# TODO: implement dependency and route


# ---------------------------------------------------------------- tests


def test_dependency_injection():
    client = TestClient(app)

    # Missing header -> 422
    assert client.get("/secure-data").status_code == 422

    # Wrong header -> 401
    r_bad = client.get("/secure-data", headers={"x-api-key": "wrong"})
    assert r_bad.status_code == 401

    # Valid header -> 200
    r_ok = client.get("/secure-data", headers={"x-api-key": "valid-key"})
    assert r_ok.status_code == 200
    assert r_ok.json() == {"data": "secret"}
