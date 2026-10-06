"""
diag4_longest_consecutive — Solution
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start a streak if this number is the beginning of one
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)

    return longest


# ---------------------------------------------------------------- tests


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
