"""
maximum_subarray — Solution
"""


def max_sub_array(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for x in nums:
        curr_sum = max(x, curr_sum + x)
        max_sum = max(max_sum, curr_sum)
    return max_sum


# ---------------------------------------------------------------- tests


def test_max_sub_array():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1, -2]) == -1
