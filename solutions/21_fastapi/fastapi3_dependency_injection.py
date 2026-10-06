"""
fastapi3_dependency_injection — Solution
"""
from fastapi import FastAPI, Depends, Header, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()


def get_api_key(x_api_key: str = Header(...)) -> str:
    if x_api_key != "valid-key":
        raise HTTPException(status_code=401, detail="Invalid key")
    return x_api_key


@app.get("/secure-data")
def secure_data(api_key: str = Depends(get_api_key)):
    return {"data": "secret"}


# ---------------------------------------------------------------- tests


def test_dependency_injection():
    client = TestClient(app)

    assert client.get("/secure-data").status_code == 422

    r_bad = client.get("/secure-data", headers={"x-api-key": "wrong"})
    assert r_bad.status_code == 401

    r_ok = client.get("/secure-data", headers={"x-api-key": "valid-key"})
    assert r_ok.status_code == 200
    assert r_ok.json() == {"data": "secret"}
