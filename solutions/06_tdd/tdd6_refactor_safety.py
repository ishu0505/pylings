"""
tdd6_refactor_safety — Solution
"""


def compare_semver(v1: str, v2: str) -> int:
    t1 = tuple(int(x) for x in v1.split("."))
    t2 = tuple(int(x) for x in v2.split("."))
    if t1 > t2:
        return 1
    if t1 < t2:
        return -1
    return 0


# ---------------------------------------------------------------- tests


def test_compare_semver():
    assert compare_semver("1.2.3", "1.2.3") == 0
    assert compare_semver("1.2.4", "1.2.3") == 1
    assert compare_semver("1.2.3", "1.2.4") == -1
    assert compare_semver("2.0.0", "1.99.99") == 1
    assert compare_semver("0.10.0", "0.9.0") == 1
