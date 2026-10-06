# 17 Dynamic Programming (NeetCode)

### The Mental Model: Remembering the Past
Dynamic Programming solves complex problems by breaking them into overlapping subproblems:
1. **Identify the State:** What parameters uniquely describe a subproblem? (e.g. `dp[i]` = max amount from houses 0..i).
2. **Find the Recurrence Relation:** How does state `i` relate to previous states? (e.g. `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`).
3. **Base Cases:** Smallest trivial inputs (`dp[0]`, `dp[1]`).
4. **Space Optimization:** Can we keep only the last 2 variables instead of an entire array?
