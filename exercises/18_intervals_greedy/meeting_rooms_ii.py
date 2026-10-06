"""
meeting_rooms_ii — Meeting Rooms II (NeetCode)         difficulty: medium

Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required.
Goal: O(n log n) time.
"""

# I AM NOT DONE

# Concept Tip: Two pointers comparing sorted starts vs sorted ends tracks peak overlapping meetings.


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_meeting_rooms():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
