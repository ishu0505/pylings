# 09 Sliding Window (NeetCode)

### The Mental Model: Caterpillars and Dynamic Windows
A sliding window maintains two pointers `l` and `r` representing a continuous subarray or substring `[l, r]`.
1. Expand `r` to include the next element and update window statistics.
2. If the window condition is violated (e.g. duplicate character or budget exceeded), advance `l` until valid again.
3. Record the maximum or minimum valid window length.
Both `l` and `r` only advance from left to right: **total runtime is $O(n)$**.
