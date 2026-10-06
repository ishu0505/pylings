# 11 Binary Search (NeetCode)

### The Mental Model: Halving the Hypothesis Space
Binary search is not just for finding a number in a sorted list; it is a general technique to search **any monotonic condition** in $O(\log n)$ time.

### Invariant Template:
```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1
```
