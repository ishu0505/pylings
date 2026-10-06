"""
trapping_rain_water — Solution
"""


def trap(height: list[int]) -> int:
    if not height:
        return 0
    l, r = 0, len(height) - 1
    max_l, max_r = height[l], height[r]
    res = 0

    while l < r:
        if max_l < max_r:
            l += 1
            max_l = max(max_l, height[l])
            res += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            res += max_r - height[r]
    return res


# ---------------------------------------------------------------- tests


def test_trap_water():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    assert trap([1, 2]) == 0
