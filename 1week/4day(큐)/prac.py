# 문제 포인트) 1) 맨밑 카드 제거, 2) 다음 맨 밑 카드를 위로 보냄
#            -> 한 사이클 -> 1장이 남을때까지 실행
from collections import deque

def test_problem_queue(num):
     deq = deque(i for i in range(i, num+1))
     while len(deq) > 1:
         deq.popleft()
         deq.append(deq.popleft())
     return deq.popleft()


