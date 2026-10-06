# 02 Basics — Python Basics, Fast

Python is dynamically typed and memory-managed. When writing production code or AI backends, you need crystal clarity on how Python treats values, references, and control flow.

### Mental Model: Names vs Objects
In Python, variables are not boxes that hold values; they are **name tags** attached to objects in heap memory.
```python
a = [1, 2]
b = a        # b points to the EXACT SAME list object in memory
b.append(3)  # a is now [1, 2, 3]!
```

### Truthiness
Every Python object has an innate boolean value:
- Falsy: `None`, `False`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`
- Truthy: everything else!

Always check for `None` explicitly using identity (`if x is None:`) rather than equality (`if x == None:`), because custom classes can override `__eq__`.
