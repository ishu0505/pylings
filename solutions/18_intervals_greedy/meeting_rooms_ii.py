"""
meeting_rooms_ii — Solution
"""


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    s = e = 0
    count = max_rooms = 0

    while s < len(intervals):
        if starts[s] < ends[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        max_rooms = max(max_rooms, count)

    return max_rooms


# ---------------------------------------------------------------- tests


def test_meeting_rooms():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
