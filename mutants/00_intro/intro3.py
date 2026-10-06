TARGET = "is_even"


def _always_true(n):
    return True


def _odd_check(n):
    return n % 2 == 1


def _breaks_on_zero(n):
    return n != 0 and n % 2 == 0


def _breaks_on_negatives(n):
    return n > 0 and n % 2 == 0 or n == 0


MUTANTS = {
    "always returns True": _always_true,
    "returns the opposite answer": _odd_check,
    "thinks 0 is not even": _breaks_on_zero,
    "wrong for negative even numbers": _breaks_on_negatives,
}
