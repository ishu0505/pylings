# 08 Two Pointers (NeetCode)

### The Mental Model: Shrinking the Search Space
Instead of testing all $O(n^2)$ pairs, maintain two index pointers `l` and `r` at opposite ends of a sorted array or sequence.
Because the array is ordered, the sum `nums[l] + nums[r]` tells you exactly which pointer must move:
- If sum < target: `l += 1` to increase the sum.
- If sum > target: `r -= 1` to decrease the sum.
This eliminates an entire row/column of candidates on every iteration, achieving **$O(n)$ time and $O(1)$ space**.
