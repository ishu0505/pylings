"""
network_delay_time — Solution
"""
import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    min_heap = [(0, k)]
    dist: dict[int, int] = {}

    while min_heap:
        d, node = heapq.heappop(min_heap)
        if node in dist:
            continue
        dist[node] = d
        for neighbor, weight in adj[node]:
            if neighbor not in dist:
                heapq.heappush(min_heap, (d + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1


# ---------------------------------------------------------------- tests


def test_network_delay():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert network_delay_time(times, 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
