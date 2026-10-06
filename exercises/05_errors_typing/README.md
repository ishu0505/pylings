# 05 Errors, Context Managers & Types

Reliable backend systems never crash with untracked 500s. They handle exceptions deliberately, validate untrusted inputs with Pydantic, and manage resources safely with context managers.

### Mental Model: Context Managers and Resource Safety
`with open(...) as f:` or `with db_transaction():` ensures resources are closed or rolled back even if an exception strikes in the middle.
In Go, this is `defer`. In Rust, it is RAII (`Drop`). In Python, it is `__enter__` and `__exit__`.

### Modern Types in Python 3.12+
Python now supports native union syntax: `int | None` replaces `Optional[int]`. Pydantic v2 compiles type models using Rust underneath (`pydantic-core`), providing blazing fast schema parsing for FastAPI.
