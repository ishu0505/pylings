# 03 Pythonic Python — Idiomatic & Clean

Writing Pythonic code isn't about clever one-liners; it's about leveraging Python's built-in protocols (iteration, generator pipelines, closures, unpacking) so the intent is immediately clear.

### Mental Model: Streams and Lazy Evaluation
Generators produce one value at a time via `yield` without allocating the whole collection in RAM.
- List comprehension `[x for x in data]`: evaluates eagerly into heap memory ($O(n)$ space).
- Generator expression `(x for x in data)`: evaluates lazily on demand ($O(1)$ memory buffer).
In backend systems processing gigabytes of JSON logs or AI embedding vectors, lazy generator pipelines prevent out-of-memory (OOM) crashes.
