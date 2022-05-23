"""
INPUT
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""

def hide(graph):
    N = len(graph)
    dist = [INF for _ in range(N + 1)]  # 1번 ~ N번까지

    q = []
    dist[0] = dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue

        for adj in graph[cur]:
            cost = acc + 1
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    max_dist = max(dist[1:])
    cnt = sum([1 for idx in range(1, N + 1) if dist[idx] == max_dist])

    return dist.index(max_dist), max_dist, cnt



import sys
from collections import defaultdict

from min_cost.dijkstra import hide

with open('testcase_hide.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(hide(graph))  # (4, 2, 3)