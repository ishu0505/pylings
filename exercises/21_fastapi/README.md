# 21 FastAPI for Production

FastAPI is the modern standard for Python API backends and AI model serving.

### The Request Lifecycle:
```
Client HTTP Request
      │
      ▼
Uvicorn ASGI Server
      │
      ▼
Middleware (Timing, Request-ID, CORS)
      │
      ▼
FastAPI Router & Path/Query Parsing
      │
      ▼
Dependency Injection (`Depends`) -> e.g. Auth, DB sessions
      │
      ▼
Pydantic Request Validation (returns 422 if invalid)
      │
      ▼
Route Handler (`@app.get(...)` / `@app.post(...)`)
      │
      ▼
Pydantic Response Serialization (`response_model`)
      │
      ▼
Client HTTP Response
```

### Dependency Injection
Dependencies in FastAPI allow swapping real database connections for in-memory test doubles using `app.dependency_overrides`.
