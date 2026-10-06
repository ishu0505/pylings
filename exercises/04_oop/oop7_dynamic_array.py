"""
oop7_dynamic_array — Dynamic Array from Scratch        difficulty: hard

Implement `DynamicArray`:
- `__init__(self, capacity: int = 2)`: allocates fixed-size internal storage `[None] * capacity`
- `capacity`: property returning current capacity
- `__len__(self)`: returns current number of elements (size)
- `append(self, val: int)`: adds val. If size == capacity, resize by doubling capacity!
- `__getitem__(self, index: int)`: returns element at index; raises IndexError if out of bounds.
- `pop(self) -> int`: removes and returns last element; raises IndexError if empty.
- `insert(self, index: int, val: int)`: inserts at index shifting subsequent elements. Resizes if needed.
"""

# I AM NOT DONE

# Concept Tip: Doubling capacity makes N appends take O(N) total time -> Amortized O(1).


class DynamicArray:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests
import pytest


def test_dynamic_array_append_doubling():
    arr = DynamicArray(capacity=2)
    assert arr.capacity == 2
    assert len(arr) == 0

    arr.append(10)
    arr.append(20)
    assert arr.capacity == 2
    assert len(arr) == 2

    # Triggers resize
    arr.append(30)
    assert arr.capacity == 4
    assert len(arr) == 3
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30


def test_dynamic_array_pop_and_errors():
    arr = DynamicArray(capacity=2)
    with pytest.raises(IndexError):
        arr.pop()

    arr.append(100)
    assert arr.pop() == 100
    assert len(arr) == 0

    with pytest.raises(IndexError):
        _ = arr[0]


def test_dynamic_array_insert():
    arr = DynamicArray(capacity=2)
    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)  # [1, 2, 3]
    assert len(arr) == 3
    assert [arr[i] for i in range(len(arr))] == [1, 2, 3]
