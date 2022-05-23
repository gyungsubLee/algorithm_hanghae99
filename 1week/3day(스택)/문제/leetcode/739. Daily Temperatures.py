'''
    enumerate()
    리스트의 인덱스와 value를 tuple형태로 반환

    ex)
    t = [1, 5, 7]
    for p in enumerate(t):
     -> print(p) 
    (0, 1)
    (1, 5)
    (2, 7)
'''
# 참조)https://inma.tistory.com/101

#leetcode) https://leetcode.com/problems/daily-temperatures/submissions/

from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack=[]
    # day = index
    for today_day, today_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < today_temp:
            pass_day = stack.pop()
            answer[pass_day] = today_day - pass_day
        stack.append(today_day)
    return answer

T = [73, 74, 75, 71, 69, 72, 76, 73]
dailyTemperatures(T)
