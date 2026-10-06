"""
errors2_custom_hierarchy — Domain Exception Hierarchy  difficulty: easy

Design an exception hierarchy for an API:
- `AppError(Exception)`: base error with message and `status_code: int = 500`
- `NotFoundError(AppError)`: status_code = 404
- `UnauthorizedError(AppError)`: status_code = 401
- `ConflictError(AppError)`: status_code = 409

Write `dispatch_error(exc: Exception) -> dict`:
- returns `{"error": str(exc), "status_code": exc.status_code}` if exc is an AppError
- otherwise returns `{"error": "Internal Server Error", "status_code": 500}`
"""

# I AM NOT DONE

# Concept Tip: A structured exception hierarchy allows central error middleware to map errors to HTTP status codes cleanly.


# TODO: define exception hierarchy and dispatch_error


# ---------------------------------------------------------------- tests


def test_exception_hierarchy():
    nf = NotFoundError("Item not found")
    assert isinstance(nf, AppError)
    assert nf.status_code == 404
    assert str(nf) == "Item not found"

    auth = UnauthorizedError("Invalid token")
    assert auth.status_code == 401


def test_dispatch_error():
    assert dispatch_error(NotFoundError("User missing")) == {
        "error": "User missing",
        "status_code": 404,
    }
    assert dispatch_error(ValueError("random crash")) == {
        "error": "Internal Server Error",
        "status_code": 500,
    }
