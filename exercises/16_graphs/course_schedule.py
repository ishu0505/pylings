"""
course_schedule — Course Schedule (NeetCode)           difficulty: medium

There are numCourses labeled from 0 to numCourses - 1. You are given prerequisites [a, b]
meaning you must take b before a.
Return true if you can finish all courses, or false if there is a cycle.
Goal: O(V + E) time.
"""

# I AM NOT DONE

# Concept Tip: A directed acyclic graph (DAG) has at least one topological ordering. A cycle prevents resolution.
from collections import defaultdict, deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_course_schedule():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False  # cycle
    assert can_finish(1, []) is True
