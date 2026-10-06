"""
network_delay_time — Network Delay Time (NeetCode)     difficulty: medium

You are given a network of n nodes labeled 1 to n, and times list of [u, v, w] (source, target, time).
We send a signal from node k. Return minimum time for all n nodes to receive signal, or -1 if impossible.
Goal: O(E log V) time using Dijkstra's algorithm.
"""

# I AM NOT DONE

# Concept Tip: Dijkstra always finalizes the shortest distance to the next closest unexplored node.
import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    # TODO: implement Dijkstra
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_network_delay():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert network_delay_time(times, 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
