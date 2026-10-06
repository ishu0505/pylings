TARGET = "clamp"


def _no_error_on_invalid_bounds(val, low, high):
    if val < low:
        return low
    if val > high:
        return high
    return val


def _off_by_one_low(val, low, high):
    if low > high:
        raise ValueError()
    if val <= low:
        return low + 1
    if val > high:
        return high
    return val


def _ignores_high(val, low, high):
    if low > high:
        raise ValueError()
    if val < low:
        return low
    return val


MUTANTS = {
    "does not raise ValueError when low > high": _no_error_on_invalid_bounds,
    "off-by-one or corrupts boundary when val <= low": _off_by_one_low,
    "does not clamp values greater than high": _ignores_high,
}
