"""
INPUT
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""

import sys

from collections import heapq

def mars(graph):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    N = len(graph)
    dist = [[INF] * N for _ in range(N)]

    q = []
    dist[0][0] = graph[0][0]
    heapq.heappush(q, (graph[0][0], 0, 0))  # 누적비용, row, col
    while q:
        acc, r, c = heapq.heappop(q)

        if dist[r][c] < acc:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                cost = dist[r][c] + graph[nr][nc]
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))

    return dist[N - 1][N - 1]

from min_cost.dijkstra import mars

with open('testcase_mars.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        graph = []
        for __ in range(N):
            graph.append(list(map(int, input().split())))

        print(mars(graph))