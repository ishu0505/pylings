"""
intro1 — Welcome to pylings!                              difficulty: easy

How it works (just like rustlings):
  1. `uv run pylings` starts WATCH mode. It runs the current exercise every
     time you save the file and shows you the test output.
  2. Each exercise is one .py file: code at the top, tests at the bottom.
  3. Make the tests pass (Red -> Green), clean up (Refactor), then delete the
     `# I AM NOT DONE` line. Only then does pylings move to the next exercise.

Stuck?  `uv run pylings hint`  reveals hints one at a time.
Mentor: open Claude Code / Codex in this folder and say "check and correct".

This one already passes. Delete the marker below and save.
"""

# I AM NOT DONE

# Concept Tip: tests are just functions starting with `test_` that use `assert`.


def add(a: int, b: int) -> int:
    return a + b


# ---------------------------------------------------------------- tests


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
