"""
tdd2_slugify — You write the tests (TDD mode)          difficulty: medium

`slugify(text: str, sep: str = "-") -> str`:
- converts text to lowercase
- replaces spaces and non-alphanumeric chars with sep
- collapses consecutive separators
- strips leading and trailing separators

Write tests to kill all planted mutants!
"""

# I AM NOT DONE

# Concept Tip: Good tests cover: case-folding, consecutive spaces, punctuation, edge strips.
import re


def slugify(text: str, sep: str = "-") -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", sep, text)
    return text.strip(sep)


# ---------------------------------------------------------------- tests
# TODO: write your tests below.
