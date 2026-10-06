"""
permutations — Solution
"""


def permute(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return [[]]
    perms = permute(nums[1:])
    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = list(p)
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res


# ---------------------------------------------------------------- tests


def test_permutations():
    res = permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res
    assert [3, 2, 1] in res
    assert permute([1]) == [[1]]
