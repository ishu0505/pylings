# 15 Backtracking & Recursion (NeetCode)

### The Mental Model: Choose → Explore → Un-choose
Backtracking systematically explores a decision tree.
```python
def backtrack(candidate_path, state):
    if is_solution(candidate_path):
        results.append(list(candidate_path))
        return
    for choice in available_choices:
        candidate_path.append(choice)  # Choose
        backtrack(candidate_path, ...) # Explore
        candidate_path.pop()           # Un-choose (backtrack)
```
Pruning dead branches before exploring them keeps search spaces practical.
