"""
find_median_from_data_stream — Find Median from Data Stream (NeetCode) difficulty: hard

The median is the middle value in an ordered integer list.
Implement MedianFinder:
- `add_num(num: int) -> None`: O(log n) time
- `find_median() -> float`: O(1) time
"""

# I AM NOT DONE

# Concept Tip: Two heaps meeting in the middle partition the numbers at the exact median in O(1) retrieval time.
import heapq


class MedianFinder:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_median_finder():
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
