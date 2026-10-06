"""
fastapi4_testclient_tdd — Solution
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()


def calculate_discount(total: float, promo_code: str | None) -> float:
    if promo_code == "VIP":
        return round(total * 0.20, 2)
    elif promo_code == "FIXED10":
        return min(10.0, total)
    return 0.0


class CheckoutRequest(BaseModel):
    total: float
    promo_code: str | None = None


@app.post("/checkout")
def checkout(payload: CheckoutRequest):
    discount = calculate_discount(payload.total, payload.promo_code)
    final_amount = max(0.0, round(payload.total - discount, 2))
    return {"final_amount": final_amount, "discount": discount}


# ---------------------------------------------------------------- tests


def test_vip_discount():
    client = TestClient(app)
    r = client.post("/checkout", json={"total": 100.0, "promo_code": "VIP"})
    assert r.status_code == 200
    assert r.json()["discount"] == 20.0
    assert r.json()["final_amount"] == 80.0


def test_fixed10_discount():
    client = TestClient(app)
    r = client.post("/checkout", json={"total": 50.0, "promo_code": "FIXED10"})
    assert r.status_code == 200
    assert r.json()["discount"] == 10.0
    assert r.json()["final_amount"] == 40.0


def test_no_promo_or_unknown():
    client = TestClient(app)
    r = client.post("/checkout", json={"total": 50.0, "promo_code": "UNKNOWN"})
    assert r.status_code == 200
    assert r.json()["discount"] == 0.0
    assert r.json()["final_amount"] == 50.0
