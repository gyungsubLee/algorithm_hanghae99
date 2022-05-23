# 문제)https://programmers.co.kr/learn/courses/30/lessons/42583

# def solution(bridge_length, weight, truck_weights):
#     bridge = [0]*bridge_length
#     complete = []
#     time = 0
#     long = len(truck_weights)
#     while len(complete) < long:
#         time += 1
#         out = bridge.pop(0)
#         if out != 0:
#             complete.append(out)
#         if len(truck_weights) > 0:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 bridge.append(truck_weights.pop(0))
#             else:
#                 bridge.append(0)
#     return time
import collections


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time

t = [7,4,5,6]
solution(2, 10, t)

# deque 형태 -> 프로그래머스 테스트5 실행시간 초과
#              why) pop(0)보다 deque가 더 빠른데 왜 그렇지?
from collections import deque
import collections

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    truck = collections.deque(truck_weights)
    time = 0
    while len(bridge) != 0:
        time += 1
        bridge.popleft()
        if truck:
            if sum(bridge) + truck[0] <= weight:
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
    return time