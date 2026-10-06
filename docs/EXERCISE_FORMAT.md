# Exercise Format (for humans and AI mentors)

Every exercise is **one self-contained Python file** with the code to fix/write
*and* its tests. `pylings` runs it with pytest.

```
exercises/<NN_track>/info.toml        # track title + ordered exercise list + hints
exercises/<NN_track>/README.md        # companion notes (concept, mental model, brute vs optimal)
exercises/<NN_track>/<name>.py        # the exercise (ships failing, contains the marker)
solutions/<NN_track>/<name>.py        # reference solution (passes, no marker)
mutants/<NN_track>/<name>.py          # TDD mode only: planted bugs your tests must catch
```

Exercise names are globally unique, lowercase, and end in a number when part of a
series: `basics1`, `hashing3`, `fastapi5`. NeetCode problems may use the slug:
`two_sum`, `valid_anagram`.

## info.toml

```toml
title = "Arrays & Hashing (NeetCode)"

[[exercises]]
name = "two_sum"
title = "Two Sum — hash map lookup"
difficulty = "easy"          # easy | medium | hard   (order exercises easy → hard)
tags = ["neetcode", "hashmap"]
hints = [
  "Approach: for each number, what *other* number would complete the target?",
  "Optimization: store value -> index in a dict as you go; check before inserting. O(n) time, O(n) space.",
  "Almost there: `need = target - x; if need in seen: return [seen[need], i]`.",
]

[[exercises]]
name = "tdd2"
title = "Write tests that catch bugs in slugify"
difficulty = "medium"
mode = "tdd"                 # you write the tests; mutants must all be caught
target = "slugify"           # name of the function/class the mutants replace
min_tests = 4
hints = ["...", "..."]
```

Hints are revealed progressively by `pylings hint` — **never put answers in the file.**
Hint 1 = approach, Hint 2 = optimization / edge cases, Hint 3 (optional) = near-solution nudge.

## Exercise file template (`mode = "test"`)

```python
"""
two_sum — Two Sum (NeetCode: Arrays & Hashing)       difficulty: easy

Given a list of ints and a target, return indices [i, j] (i < j) of the two
numbers that add up to target. Exactly one answer exists.

Goal: O(n) time.  Brute force is O(n^2) — get it working, then optimise.
Run:  uv run pylings run two_sum      Hint: uv run pylings hint two_sum
"""

# I AM NOT DONE

# Concept Tip: A dict answers "have I seen X before?" in O(1).


def two_sum(nums: list[int], target: int) -> list[int]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
# Don't edit the tests (unless the docstring tells you to).


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_negative_and_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4], -7) == [2, 3]
```

Rules:
- The line `# I AM NOT DONE` must be present in the shipped exercise. The learner
  deletes it when happy; only then does the exercise count as done.
- The shipped file must **fail** its tests (stub with `raise NotImplementedError`,
  a deliberate bug, or a missing piece). The solution file must pass.
- Include a `# Concept Tip:` comment and `# TODO:` markers. Keep docstrings short —
  the learner wants speed. Deeper theory goes in the track `README.md`.
- Tests are visible and cover edge cases (empty, single item, duplicates, negatives, large input).
- Only stdlib + project deps (pytest, fastapi, httpx, pydantic, boto3, moto). No network.
- Async code: test with `asyncio.run(...)` inside a normal test function (no plugins).
- AWS code: use `moto`'s `mock_aws` (env vars for fake creds/region are set by pylings).
- Must finish in well under 60 seconds.

## TDD template (`mode = "tdd"`)

The learner gets a **correct** implementation and writes the tests. pylings checks:
1. their tests pass on the real implementation, 2. there are at least `min_tests`
zero-argument `test_*` functions, 3. every mutant in `mutants/.../<name>.py` makes
at least one test fail.

```python
# mutants/06_tdd/tdd2.py
TARGET = "slugify"

def _strips_nothing(text):            # each mutant = a realistic bug
    return text.lower().replace(" ", "-")

MUTANTS = {
    "does not strip surrounding whitespace": _strips_nothing,
    # ...
}
```

Mutant descriptions are shown when a bug slips through, so word them as a nudge.

## Validating

```bash
uv run pylings check-solutions                 # everything
uv run pylings check-solutions --track fastapi # one track
```
