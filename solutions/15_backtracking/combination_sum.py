"""
combination_sum — Solution
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res: list[list[int]] = []

    def dfs(i: int, cur: list[int], total: int) -> None:
        if total == target:
            res.append(list(cur))
            return
        if i >= len(candidates) or total > target:
            return

        # Choose candidate[i]
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        # Skip candidate[i]
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


# ---------------------------------------------------------------- tests


def test_combination_sum():
    res = combination_sum([2, 3, 6, 7], 7)
    sorted_res = sorted([sorted(c) for c in res])
    assert sorted_res == [[2, 2, 3], [7]]
    assert combination_sum([2], 1) == []
