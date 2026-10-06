"""
pythonic6_sorting_bisect — Solution
"""
import bisect


def insert_sorted(arr: list[int], val: int) -> None:
    bisect.insort(arr, val)


def sort_students(students: list[dict]) -> list[dict]:
    return sorted(students, key=lambda s: (-s["gpa"], s["age"], s["name"]))


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
