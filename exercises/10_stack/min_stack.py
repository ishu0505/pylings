"""
min_stack — Min Stack (NeetCode)                       difficulty: medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time O(1).
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int get_min() retrieves the minimum element in the stack.
"""

# I AM NOT DONE

# Concept Tip: Storing the minimum alongside each element makes `get_min()` trivial O(1).


class MinStack:
    # TODO: implement
    pass


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
