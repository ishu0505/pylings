"""
subsets — Solution
"""


def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    subset: list[int] = []

    def dfs(i: int) -> None:
        if i >= len(nums):
            res.append(list(subset))
            return
        # include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # exclude nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


# ---------------------------------------------------------------- tests


def test_subsets():
    res = subsets([1, 2, 3])
    sorted_res = sorted([sorted(s) for s in res])
    expected = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted_res == expected
    assert subsets([]) == [[]]
