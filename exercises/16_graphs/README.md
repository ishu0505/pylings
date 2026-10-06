# 16 Graphs (NeetCode)

### The Mental Model: Nodes, Edges, and Traversal
Graphs model interconnected systems (dependency trees, network routes, state machines).
- **Adjacency List:** Represent graph as `dict[node, list[neighbor]]`.
- **DFS:** Explore deep into paths; great for cycle detection and topological sorting.
- **BFS:** Explore uniformly outward step by step; guaranteed to find the **shortest path in unweighted graphs**.
- **Dijkstra's Algorithm:** BFS with a min-heap priority queue for **shortest path in weighted graphs**.
