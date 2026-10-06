"""
pythonic6_sorting_bisect — Sorting & Bisect             difficulty: medium

1. `insert_sorted(arr: list[int], val: int) -> None`:
   inserts val into already-sorted list arr using `bisect.insort` in O(log n) search time.
2. `sort_students(students: list[dict]) -> list[dict]`:
   given list of {"name": str, "gpa": float, "age": int}, sort by:
   - gpa descending (highest first)
   - age ascending (youngest first)
   - name alphabetically
"""

# I AM NOT DONE

# Concept Tip: In Python, `sorted` is stable (preserves existing order for equal keys).
import bisect


def insert_sorted(arr: list[int], val: int) -> None:
    # TODO: implement
    raise NotImplementedError


def sort_students(students: list[dict]) -> list[dict]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_insert_sorted():
    nums = [10, 20, 30]
    insert_sorted(nums, 25)
    assert nums == [10, 20, 25, 30]
    insert_sorted(nums, 5)
    assert nums == [5, 10, 20, 25, 30]


def test_sort_students():
    data = [
        {"name": "Bob", "gpa": 3.8, "age": 21},
        {"name": "Alice", "gpa": 3.8, "age": 20},
        {"name": "Charlie", "gpa": 3.9, "age": 22},
        {"name": "David", "gpa": 3.8, "age": 20},
    ]
    sorted_data = sort_students(data)
    assert [s["name"] for s in sorted_data] == ["Charlie", "Alice", "David", "Bob"]
