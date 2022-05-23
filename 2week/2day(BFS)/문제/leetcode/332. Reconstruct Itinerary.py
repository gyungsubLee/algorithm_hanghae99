# 문제)https://leetcode.com/problems/reconstruct-itinerary/
from typing import List
import collections

# reverse -> pop() = pop(0) 같지만 O(1)의 시간을 갖는다.

# 풀이1) DFS (stack 보다 빠름)
def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    # reversed -> 그래프 역순 구성 pop() 시, pop(0)와 같은
    #  why) pop(0)는 O(n)의 시간복잡도를 가진다. 따라서 그래프 구조를 역순으로 구성해
    #        O(1)의 시간복잡도를 가진 pop()으로 pop(0)와 같은 역활을 한다.
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]

t = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

findItinerary(t)

# 풀이2) stack
def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        route.append(stack.pop())

    return route

t = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

findItinerary(t)





