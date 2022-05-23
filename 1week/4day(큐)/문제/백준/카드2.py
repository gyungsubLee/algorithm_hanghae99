# 문제 링크)https://www.acmicpc.net/problem/2164
# 시간복잡도) https://wiki.python.org/moin/TimeComplexity

# 문제)카드2
# 큐 -> 파이썬에서 내장함수 deque를 사용

# Deque 객체의 내장 메소드
# append: 오른쪽 추가, appendleft:왼쪽 추가
# pop:오른쪽 제거, popleft: 왼쪽 제거
# 참조)https://docs.python.org/3/library/collections.html?

# 문제 포인트) 1) 맨밑 카드 제거, 2) 다음 맨 밑 카드를 위로 보냄
#            -> 한 사이클 -> 1장이 남을때까지 실행

from collections import deque

def test_problem_queue(num):
    deq = deque([i for i in range(1, num+1)])
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()

[4, 2, 3]
