# 10 Stacks (NeetCode)

### The Mental Model: LIFO and Monotonic Sequences
Stacks follow Last-In First-Out (LIFO).
**Monotonic Stack:**
When elements arrive, pop elements that are smaller (or larger) than the current element.
This answers queries like *"What is the next greater element to the right?"* in **$O(n)$ total time**, because every element is pushed once and popped at most once!
