"""
fastapi4_testclient_tdd — You write the tests (TDD mode) difficulty: medium

An e-commerce checkout endpoint applies promotional discounts.
`calculate_discount(total: float, promo_code: str | None) -> float`:
- If promo_code == "VIP", discount is 20% (0.20 * total).
- If promo_code == "FIXED10", discount is min(10.0, total).
- Otherwise discount is 0.0.

Write at least 3 tests calling the endpoint via TestClient to kill all mutants!
"""

# I AM NOT DONE

# Concept Tip: Test endpoints from the client's perspective to verify HTTP status, payload parsing, and business logic.
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
# TODO: write your tests below using client = TestClient(app).
