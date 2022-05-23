# 문제링크)https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque
"""
deque: 연결리스트로 구성
-> popleft 시 O(1)의 시간 복잡도를 가진다.
"""

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0