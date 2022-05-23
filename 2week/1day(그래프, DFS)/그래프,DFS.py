# 목적: 그래프, 그래프 코드 구현, DFS 구현
# 연습문제: 섬의 개수

"""
그래프: 연결되어 있는 정점과 정점간의 관계를 표현할 수 있는 자료구조.

자료구조: 선형구조, 비선형 구조
   선형구조: 자료를 저장하고 꺼내는 것에 초점이 맞춰져 있다. ex) 스택, 큐, ...
   비선형구조: 표현에 초점이 맞춰져 있다. ex) DFS, BFS ...

#용어정리
노드(Node): 연결 관계를 가진 각 데이터를 의미함. 정점(Vertex)라고도 함.
간선(Edge): 노드 간의 관계를 표시한 선.
인접 노드(Adjacent Node):간선으로 직접 연결된 노드(또는 정점)

유방향 그래프 vs 무방향 그래프
    유방향 그래프(Directed Graph): 간선(연결선) 방향 존재, 각 간선은 한 방향으로 진행 가능
    무방향 그래프(Undirected Graph): 간선(연결선) 방향 x
"""

'''
# 그래프 표현 방법
1) 인접 행렬(Adjacency Matrix): 2차원 배열(행렬)로 그래프의 연결 관계(간선 표시, 연결:1, 미연결:0)를 표현
2) 인접 리스트(Adjacnecy List): linked list로 그래프의 연결관게 표현

 - 인접 행렬 vs 인접 리스트 -> 시간(인접 행렬) vs 공간(연결 리스트)
  인접 행렬로 표현하면 즉각적으로 0과 1이 연결되었는지 여부를 바로 알 수 있다. 
  그러나, 모든 조합이 연결 여부를 저장해야 되기 때문에 O(노드^2)만큼의 공간 사용
  
  인접 리스트로 표현하면 즉각적으로 연결되었는지 알 수 없고, 각 리스트를 돌아봐야한다.
  따라서 연결 여부를 알기 위해선 최대 O(간선)만큼의 시간을 사용함.
  대신 모든 조합의 연결 여부를 저장할 필요가 없으니 O(노드 + 간선)만큼의 공간 사용     
'''

# DFS(Depth First Seatch)
# 갈 수 있을 만큼 계속해서 탐색하다가 갈 수 없게 되면 다른 방향으로 다시 탐색한다.
# 노드 방문 -> 깊이 우선으로 인접한 노드 방문 ->

# 백트래킹!

# 이미지/테스트코드.png 참조

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
# 구현1 (재귀)
#   재귀함수: 반복적으로 발생하는 일이 무엇인지 아는 것, 종료 조건을 아는 것
def dfs_recursive(node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited

assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]



# 구현2 (스택)
def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    # while문이 true인 동안 아래 로직이 계속 실행(return은 while문이 false일때 넘어감)
    # visited 와 stack은 위에 선언해서 for문에서 참조하는 것이다. 따라서 return을 시키지 않아도 된다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited

assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]






