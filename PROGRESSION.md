# Coding Mastery Tracker

## Current Status
- **Active Track:** 01_diagnostic
- **Current Module:** Phase 0: Intro & Diagnostic Phase
- **Overall Level:** Determining baseline

---

## Python Progression Roadmap

### Phase 0: Intro & Diagnostic Baseline
- [ ] Intro (`exercises/00_intro/`) — CLI mechanics, `# I AM NOT DONE`, test-driven mutant checking
- [~] Diagnostic Assessment (`exercises/01_diagnostic/`) — find baseline & skip mastered tracks
  - [x] `diag1_first_unique` — 2026-10-06: CLI confirms completion; 17 attempts and 1 hint. Review loop completion and empty-input fallback after a gap.
  - [x] `diag2_top_k_words` — 2026-10-06: Completed; 14 attempts and 0 hints. Practice converting selected `(word, count)` pairs into a list of words.
  - [x] `diag3_stack_class` — 2026-10-07: CLI confirms completion; 15 attempts and 1 hint. Review `__bool__` truthiness after a gap.
  - [x] `diag4_longest_consecutive` — 2026-10-07: CLI confirms all tests pass; 9 attempts and 0 hints. Re-solve from scratch after a gap because the solution was shown step by step.
  - [x] `diag5_clamp_tdd` — 2026-10-07: CLI confirms completion; 15 attempts and 1 hint. Review pytest.raises syntax after a gap.
  - [~] `diag6_validate_user` — 2026-10-07: Username/age checks are in place and valid payload test passes. Email type check incorrectly asks for int instead of str; function returns errors instead of raising `ValidationError` when errors exist. 10 attempts, 2 hints.

### Phase 1: Foundations, Pythonic Idioms & OOP
- [ ] Python Basics, Fast (`exercises/02_basics/`) — types, control flow, functions, collections
- [ ] Pythonic Python (`exercises/03_pythonic/`) — comprehensions, generators, itertools, decorators
- [ ] Classes, Dunders & OOP (`exercises/04_oop/`) — self, dunders, properties, dataclasses, DynamicArray from scratch
- [ ] Errors, Context Managers & Types (`exercises/05_errors_typing/`) — exceptions, context managers, typing, Pydantic v2
- [ ] Test-Driven Development (`exercises/06_tdd/`) — Red-Green-Refactor, pytest fixtures & parametrization, mutation testing

### Phase 2: NeetCode Core & Transferable DSA (Built with TDD)
- [ ] Arrays & Hashing (`exercises/07_arrays_hashing/`) — NeetCode core + HashMap from scratch
- [ ] Two Pointers (`exercises/08_two_pointers/`) — Palindromes, Two Sum II, 3Sum, Trapping Rain Water
- [ ] Sliding Window (`exercises/09_sliding_window/`) — Stock, Longest Substring, Min Window Substring
- [ ] Stack (`exercises/10_stack/`) — Min Stack, RPN, Monotonic stack, Histogram
- [ ] Binary Search (`exercises/11_binary_search/`) — Search 2D, Rotated arrays, TimeMap
- [ ] Linked Lists (`exercises/12_linked_list/`) — Linked list from scratch, Reverse, Cycle, LRU Cache
- [ ] Trees & BST (`exercises/13_trees/`) — DFS, BFS, BST validation, Serialize/Deserialize
- [ ] Heaps & Priority Queues (`exercises/14_heap/`) — Top-K, Median from Data Stream
- [ ] Backtracking & Recursion (`exercises/15_backtracking/`) — Subsets, Permutations, N-Queens
- [ ] Graphs (`exercises/16_graphs/`) — Grid BFS/DFS, Topo sort, Union-Find, Dijkstra
- [ ] Dynamic Programming (`exercises/17_dp/`) — 1D/2D DP, Memoization vs Tabulation, Knapsack patterns
- [ ] Intervals & Greedy (`exercises/18_intervals_greedy/`) — Merge Intervals, Meeting Rooms II, Kadane
- [ ] Tries (`exercises/19_tries/`) — Trie prefix tree, Wildcard search, Word Search II

### Phase 3: Software Engineering & AI Backend Systems
- [ ] Async Python & Event Loops (`exercises/20_async/`) — Coroutines, Gather, Semaphore, Worker Pool, Raw ASGI
- [ ] FastAPI for Production (`exercises/21_fastapi/`) — Endpoints, Pydantic schemas, Dependency Injection, SQLite Repo, Auth, Middleware
- [ ] Queue Workers: SQS & SNS (`exercises/22_workers/`) — Boto3, Moto, DLQ, Fan-out, Idempotency, Graceful shutdown
- [ ] AI Backend Systems (`exercises/23_ai_backend/`) — Retries with jitter, Rate limiting, Structured LLM outputs, RAG chunking, Vector cosine search, SSE token streaming, Async LLM gateway

---

## Review Queue (Spaced Repetition)
| Exercise | Last Attempted | Notes / Triggers | Next Review Due |
|---|---|---|---|
| `diag1_first_unique` | 2026-10-06 | Loop completion vs early return; empty-input fallback; 14+ attempts | 2026-10-09 |
| `diag2_top_k_words` | 2026-10-06 | Revisit pair-to-word extraction after a gap; 14 attempts | 2026-10-10 |
| `diag3_stack_class` | 2026-10-07 | Re-solve `__bool__` from scratch after a gap; 15 attempts, 1 hint | 2026-10-10 |
| `diag4_longest_consecutive` | 2026-10-07 | Re-solve after seeing the solution; trace start detection and forward counting; 9 attempts | 2026-10-10 |
| `diag5_clamp_tdd` | 2026-10-07 | Recreate the three tests from scratch after a gap; focus on `pytest.raises` context syntax | 2026-10-10 |
| `diag6_validate_user` | 2026-10-07 | Check email is text; raise `ValidationError(errors)` when dict is nonempty; valid case should return None | 2026-10-10 |

---

## Future Tracks (Queued)
- [ ] Go Track (Goroutines, Channels, Pointers, Structs, Porting NeetCode solutions)
- [ ] Rust Track (Ownership, Borrowing, Lifetimes, Tokio async, Porting NeetCode solutions)

<!-- pylings:auto:start -->
_Auto-generated by `pylings` (run `uv run pylings sync`). Do not edit inside this block._

- **Updated:** 2026-10-07T16:13:20
- **Exercises done:** 9/116 (skipped: 0)
- **Current exercise:** `basics1_truthiness` — Truthiness, None checks, and identity vs equality (02_basics)
- **Focus track:** none (linear order)

| Track | Done | Progress |
|---|---|---|
| 00_intro | 3/3 | 100% |
| 01_diagnostic | 6/6 | 100% |
| 02_basics | 0/6 | 0% |
| 03_pythonic | 0/7 | 0% |
| 04_oop | 0/7 | 0% |
| 05_errors_typing | 0/6 | 0% |
| 06_tdd | 0/7 | 0% |
| 07_arrays_hashing | 0/7 | 0% |
| 08_two_pointers | 0/5 | 0% |
| 09_sliding_window | 0/5 | 0% |
| 10_stack | 0/5 | 0% |
| 11_binary_search | 0/5 | 0% |
| 12_linked_list | 0/5 | 0% |
| 13_trees | 0/5 | 0% |
| 14_heap | 0/3 | 0% |
| 15_backtracking | 0/3 | 0% |
| 16_graphs | 0/4 | 0% |
| 17_dp | 0/4 | 0% |
| 18_intervals_greedy | 0/3 | 0% |
| 19_tries | 0/2 | 0% |
| 20_async | 0/5 | 0% |
| 21_fastapi | 0/4 | 0% |
| 22_workers | 0/4 | 0% |
| 23_ai_backend | 0/5 | 0% |

**Recently completed** (attempts = test runs before passing, hints = hints revealed):

| Exercise | Completed | Attempts | Hints |
|---|---|---|---|
| diag6_validate_user | 2026-10-07T16:13:20 | 13 | 2 |
| diag5_clamp_tdd | 2026-10-07T15:55:19 | 15 | 1 |
| diag4_longest_consecutive | 2026-10-07T15:44:02 | 9 | 0 |
| diag3_stack_class | 2026-10-07T10:04:26 | 15 | 1 |
| diag2_top_k_words | 2026-10-06T23:48:25 | 14 | 0 |
| diag1_first_unique | 2026-10-06T23:26:39 | 17 | 1 |
| intro3 | 2026-10-06T23:03:12 | 8 | 0 |
| intro2 | 2026-10-06T23:01:05 | 8 | 1 |
<!-- pylings:auto:end -->
