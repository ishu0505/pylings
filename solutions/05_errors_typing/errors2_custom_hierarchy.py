"""
errors2_custom_hierarchy — Solution
"""


class AppError(Exception):
    status_code: int = 500

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotFoundError(AppError):
    status_code = 404


class UnauthorizedError(AppError):
    status_code = 401


class ConflictError(AppError):
    status_code = 409


def dispatch_error(exc: Exception) -> dict:
    if isinstance(exc, AppError):
        return {"error": str(exc), "status_code": exc.status_code}
    return {"error": "Internal Server Error", "status_code": 500}


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
