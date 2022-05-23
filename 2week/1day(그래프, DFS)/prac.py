# DFS 구현

# 재귀

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def dfs_recursive(node, visited):
    # 방문 처리
    visited.append(node)

    # 인접 노드 방문
    for a in graph[node]:
        if a not in visited:
            dfs_recursive(a, visited)

    return visited

dfs_recursive(1, [])
