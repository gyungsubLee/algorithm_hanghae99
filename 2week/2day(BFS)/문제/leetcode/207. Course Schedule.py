# 문제)https://leetcode.com/problems/course-schedule/

# https://www.youtube.com/watch?v=EgI5nU9etnU

# 이해 실패

# 그래프, 사이클 감지 (recursive, visited node)
import collections
from typing import List


# 풀이1)
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjList = collections.defaultdict(list)

    for course, pre in prerequisites:
        adjList[pre].append(course)

    def cycle(node, tracker):
        tracker[node] = True
        for n in adjList[node]:
            if n in tracker or cycle(n, tracker):
                return True
        tracker.pop(node)
        return False

    for n in range(numCourses):
        tracker = {}
        if cycle(n, tracker):
            return False

    return True
c = 4
t = [[0,1], [1,2], [2,3]]

canFinish(c, t)


# 풀이1) 코드 수정
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjList = collections.defaultdict(list)

    for course, pre in prerequisites:
        adjList[pre].append(course)

    def cycle(node, tracker, visited):
        tracker[node] = True
        visited[node] = True

        for n in adjList[node]:
            if n not in visited and cycle(n, tracker, visited):
                return True
            elif n in tracker:
                return True
        tracker.pop(node)
        return False
    visited = {}
    for n in range(numCourses):
        tracker = {}
        if n not in visited and cycle(n, tracker, visited):
            return False

    return True

# 풀이2)
class SolutionL:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

