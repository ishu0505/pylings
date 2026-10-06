"""
car_fleet — Solution
"""


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = sorted(zip(position, speed), reverse=True)
    stack: list[float] = []

    for pos, spd in pair:
        time = (target - pos) / spd
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


# ---------------------------------------------------------------- tests


def test_car_fleet():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
