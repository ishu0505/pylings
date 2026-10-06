# 04 Classes, Dunders & OOP

Object-Oriented Programming in Python is lightweight and expressive. Understanding it thoroughly prepares you for designing services in FastAPI and prepares you for Rust structs and Go types.

### Mental Model: Memory, Pointers, and Dunders
- **Instances are dictionaries under the hood:** An instance `user` holds attributes in a hidden `__dict__` mapped in heap memory.
- **Dunder methods (Magic methods):** Methods starting and ending with double underscores (`__repr__`, `__len__`, `__getitem__`) wire your class directly into Python's syntax (`len(x)`, `x[i]`, `x == y`).
- **Dynamic Array Memory Allocation:**
  In C, Rust, or Python's internal `PyListObject`, an array is a contiguous slab of memory pointers. When it runs out of space, the runtime allocates a new slab *twice as large*, copies pointers over, and frees the old block. This makes appending **amortized $O(1)$**.
