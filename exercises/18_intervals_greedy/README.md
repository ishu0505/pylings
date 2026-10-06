# 18 Intervals & Greedy (NeetCode)

### The Mental Model: Sorting and Greedy Choices
Greedy algorithms make the locally optimal choice at each step without backtracking.
- **Intervals:** Almost all interval problems require **sorting by start time** (or sometimes end time) first!
- **Kadane's Algorithm:** If the current running sum drops below zero, reset it: a negative prefix can never help a future subarray.
