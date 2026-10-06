"""
min_stack — Solution
"""


class MinStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        current_min = min(val, self._min_stack[-1] if self._min_stack else val)
        self._min_stack.append(current_min)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]


# ---------------------------------------------------------------- tests


def test_min_stack():
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    assert st.get_min() == -3
    st.pop()
    assert st.top() == 0
    assert st.get_min() == -2
