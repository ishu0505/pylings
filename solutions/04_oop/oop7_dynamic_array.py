"""
oop7_dynamic_array — Solution
"""


class DynamicArray:
    def __init__(self, capacity: int = 2) -> None:
        self._capacity = max(1, capacity)
        self._size = 0
        self._data: list[object] = [None] * self._capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    def __len__(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        new_data: list[object] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, val: int) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = val
        self._size += 1

    def __getitem__(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]  # type: ignore

    def pop(self) -> int:
        if self._size == 0:
            raise IndexError("pop from empty dynamic array")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val  # type: ignore

    def insert(self, index: int, val: int) -> None:
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = val
        self._size += 1


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
    arr.insert(1, 2)
    assert len(arr) == 3
    assert [arr[i] for i in range(len(arr))] == [1, 2, 3]
