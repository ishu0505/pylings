"""
fastapi1_hello_world — Solution
"""
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/echo")
def echo(message: str):
    return {"message": message}


# ---------------------------------------------------------------- tests


def test_fastapi_endpoints():
    client = TestClient(app)
    r1 = client.get("/health")
    assert r1.status_code == 200
    assert r1.json() == {"status": "healthy"}

    r2 = client.get("/echo?message=pylings")
    assert r2.status_code == 200
    assert r2.json() == {"message": "pylings"}
