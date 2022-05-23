# 백준 링크)https://www.acmicpc.net/problem/1966
# 프로그래머스 링크)https://programmers.co.kr/learn/courses/30/lessons/42587

# 프린터 youtube 영상 참조)https://www.youtube.com/watch?v=ZMfuDnUfdAc&list=PLlV7zJmoG4XJfK8vVL2E2NX8ej73vjNlh&index=6
from collections import deque

# 문제: 프린터(큐)
def solution(priorities, location):
    #1. Queue를 만든다.
    printer = [(i, p) for i,p in enumerate(priorities)]
    turn = 0
    while printer:
        job = printer.pop(0)
    #2. 나보다 중요한 job이 있으면 뒤에 넣는다.
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            turn+=1
    #3. 내가 제일 중요하다면 수행하고 location과 비교한다.
            if job[0] == location:
                break
    return turn

print(solution([2, 1, 3, 2], 0))



# 백준- 풀이)
from collections import deque

x = int(input())

for _ in range(x):
    n, m = map(int, input().split()) # 문서 개수, 궁금한 문서 idx (6, 0)
    # 리스트 선언 안 추가해도 됨.
    prior = deque((map(int, input().split()))) # 중요도 [1, 1, 9, 1, 1, 1]
    array = deque(list[ _ for i in range(1, n + 1)])         # [1, 2, 3, 4, 5, 6]
    array[m] = 0
    ans = 0

    while True:
        if prior[0] != max(prior):
            prior.append(prior.popleft())
            array.append(array.popleft())
        elif prior[0] == max(prior) and array[0] != 0:
            prior.popleft()
            array.popleft()
            ans += 1
        elif prior[0] == max(prior) and array[0] == 0:
            ans += 1
            print(ans)
            break

