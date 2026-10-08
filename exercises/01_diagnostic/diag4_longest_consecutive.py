"""
diag4_longest_consecutive — Longest Consecutive Sequence   difficulty: medium

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


# Concept Tip: Store numbers in a set. Only begin counting a streak if (num - 1)
# is NOT in the set — that guarantees each number is visited at most twice.


def longest_consecutive(nums: list[int]) -> int:
    # TODO: implement in O(n)
    num_set = set(nums)

    longest = 0


    for num in num_set:
        if num - 1 in num_set:
            continue

        current_num = num
        current_longest = 0

        while current_num in num_set:
            current_longest +=1
            current_num +=1

        if current_longest > longest:
            longest = current_longest

    return longest





# ---------------------------------------------------------------- tests


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
