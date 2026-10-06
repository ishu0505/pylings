"""
pythonic4_collections — Solution
"""
from collections import defaultdict, deque


def invert_multi_dict(d: dict[str, list[int]]) -> dict[int, list[str]]:
    out = defaultdict(list)
    for k, values in d.items():
        for v in values:
            out[v].append(k)
    return dict(out)


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    if not nums or k == 0:
        return []
    q: deque[int] = deque()  # stores indices
    res: list[int] = []

    for i, x in enumerate(nums):
        # Remove elements outside window
        while q and q[0] <= i - k:
            q.popleft()
        # Maintain decreasing monotonic order
        while q and nums[q[-1]] < x:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])

    return res


# ---------------------------------------------------------------- tests


def test_invert_multi_dict():
    d = {"a": [1, 2], "b": [2, 3]}
    res = invert_multi_dict(d)
    assert res[1] == ["a"]
    assert sorted(res[2]) == ["a", "b"]
    assert res[3] == ["b"]


def test_sliding_window_max():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert sliding_window_max(nums, 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([1], 1) == [1]
