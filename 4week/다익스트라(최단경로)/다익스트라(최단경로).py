"""
최단경로 (A -> B로 가는 최소 경로)
- 그래프 표현 -> 각 지점: 노드, 도로: 간선
-다익스트라, 플로이드-워셜

-지도 앱에서 사용
"""

"""
1. 출발지를 s로 정하고, 다음과 같이 표시한다.
      (s,    t,     x,     y,     z  순)
거리 = [0,    inf,   inf,   inf,   inf]
방문 = [True, False, False, False, False]

2. 갈 수 있는 노드들의 최소거리를 측정한다.
s->t: 10
s->y: 5
      (s,    t,     x,     y,     z  순)
거리 = [0,    10,    inf,   5,     inf]
방문 = [True, False, False, False, False]

3. 방문 안한 녀석들 중 가장 가까운 녀석인 y를 방문하고, 최소거리를 측정한다.
y->t: 3
y->x: 9
y->z: 2
      (s,    t,     x,     y,    z  순)
거리 = [0,    8,     14,    5,    7]
방문 = [True, False, False, True, False]

4. 방문 안한 녀석들 중 가장 가까운 녀석인 z를 방문하고, 최소거리를 측정한다.
z->x: 6
      (s,    t,     x,     y,    z  순)
거리 = [0,    8,     13,    5,    7]
방문 = [True, False, False, True, True]

5. 방문 안한 녀석들 중 가장 가까운 녀석인 t를 방문하고, 최소거리를 측정한다.
t->x: 1
t->y: 2
      (s,    t,     x,    y,    z  순)
거리 = [0,    8,     9,    5,    7]
방문 = [True, True, False, True, True]

6. 방문 안한 녀석들 중 가장 가까운 녀석인 x를 방문하고, 최소거리를 측정한다.
x->z: 4
      (s,    t,     x,    y,    z  순)
거리 = [0,    8,     9,    5,    7]
방문 = [True, True, True, True, True]

7. 방문 안한 노드가 없으므로 끝낸다.
      (s,    t,     x,    y,    z  순)
거리 = [0,    8,     9,    5,    7]
방문 = [True, True, True, True, True]
"""

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
#구현1)  Naive: 이중 for 문이므로 O(V^2)
import sys

from min_cost.dijkstra import dijkstra_naive, dijkstra_pq

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]

INF = int(1e9)


def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node()
        visited[cur] = True
        # 최단거리를 비교, 수정한다.
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist

#구현2)  PriorityQueue: O(ElogV)
import heapq


def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

import sys

from min_cost.dijkstra import dijkstra_naive, dijkstra_pq

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
assert dijkstra_pq(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]