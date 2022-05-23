from collections import deque

# graph = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }
#
#
# def bfs_queue(start):
#     visited = [start]
#     q = deque([start])
#
#     while q:
#         node = q.popleft()
#         for adj in graph[node]:
#             if adj not in visited:
#                 q.append(adj)
#                 visited.append(adj)
#
#     return visited
#
#
# assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for a in graph[node]:
            if not a in visited:
                visited.append(a)
                q.append(a)

    return visited

bfs_queue(1)


























