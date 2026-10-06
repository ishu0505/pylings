"""
house_robber — Solution
"""


def rob(nums: list[int]) -> int:
    prev1 = prev2 = 0
    for x in nums:
        prev1, prev2 = max(prev2 + x, prev1), prev1
    return prev1


# ---------------------------------------------------------------- tests


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
