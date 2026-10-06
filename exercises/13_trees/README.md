# 13 Trees & Binary Search Trees (NeetCode)

### The Mental Model: Recursion and Subproblems
A tree is a recursive structure: every node is the root of its own subtree.
- **DFS (Depth-First Search):** Solve the problem for `node.left` and `node.right`, then combine the answers at `node`.
- **BFS (Breadth-First Search):** Level-by-level traversal using a queue (`collections.deque`).
- **Binary Search Tree Property:** For every node: all values in the left subtree are strictly smaller, and all values in the right subtree are strictly greater. In-order traversal of a BST always yields sorted elements!
