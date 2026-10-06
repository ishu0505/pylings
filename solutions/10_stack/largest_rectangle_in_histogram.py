"""
largest_rectangle_in_histogram — Solution
"""


def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    stack: list[tuple[int, int]] = []  # (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area


# ---------------------------------------------------------------- tests


def test_largest_rectangle():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([1]) == 1
