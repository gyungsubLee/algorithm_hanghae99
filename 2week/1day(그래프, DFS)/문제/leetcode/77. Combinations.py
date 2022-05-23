# 문제) https://leetcode.com/problems/combinations/
from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return
            # return 시 재귀함수가 호출된 바로 밑의 코드로 진행된다.
            # why) 기본적으로 스택으로 재귀함수가 호출될 때, 주소 값을 기억하고 return시 그 밑으로 들어간다.
            # 따라서 return 시 재귀함수가 호출된 주소값으로 돌아가기 떄문에 그 바로 밑에 있는 코드가 실행된다.

        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()
    backtrack(1, [])
    return res

combine(4, 2)