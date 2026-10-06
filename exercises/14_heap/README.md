# 14 Heaps & Priority Queues (NeetCode)

### The Mental Model: Tournament Brackets
A binary heap is a complete binary tree where every parent is smaller (min-heap) or larger (max-heap) than its children.
- Python's `heapq` module implements a **min-heap** in an array.
- Insertion (`heappush`) and extraction (`heappop`) run in **$O(\log n)$** time.
- `heapq.heapify(list)` turns an arbitrary list into a heap in **$O(n)$** linear time!
- To make a max-heap in Python, negate the values: `-x`.
