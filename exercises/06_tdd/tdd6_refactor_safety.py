"""
tdd6_refactor_safety — SemVer comparison               difficulty: medium

Implement `compare_semver(v1: str, v2: str) -> int`:
- parses strings like "1.2.3" or "2.0.0"
- returns:
  - 1 if v1 > v2
  - -1 if v1 < v2
  - 0 if v1 == v2
"""

# I AM NOT DONE

# Concept Tip: Tuples compare left-to-right: (1, 2, 0) < (1, 10, 0) compares correctly without custom loops.


def compare_semver(v1: str, v2: str) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_compare_semver():
    assert compare_semver("1.2.3", "1.2.3") == 0
    assert compare_semver("1.2.4", "1.2.3") == 1
    assert compare_semver("1.2.3", "1.2.4") == -1
    assert compare_semver("2.0.0", "1.99.99") == 1
    assert compare_semver("0.10.0", "0.9.0") == 1
