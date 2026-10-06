"""
house_robber — House Robber (NeetCode)                 difficulty: medium

You are planning to rob houses along a street. Each house has money.
Adjacent houses have connected security systems; robbing two adjacent houses alerts police.
Return the maximum amount of money you can rob tonight without alerting police.
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: `current = max(rob_this_house + two_houses_back, previous_house)`.


def rob(nums: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
