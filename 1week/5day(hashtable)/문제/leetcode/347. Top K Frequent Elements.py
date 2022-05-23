#heapq 참조) https://www.daleseo.com/python-heapq/

import collections
import heapq

# 내장함수: counter
# t1 = [2, 2, 3, 1, 1, 1]
# f1 = collections.Counter(t1)
# print(f1)
# # -> Counter({1: 3, 2: 2, 3: 1})
# t2 = [2, 2, 3, 3, 3, 3, 1, 1, 1]
# f2 = collections.Counter(t1)
# print(f2)
# # -> Counter({3: 4, 1: 3, 2: 2})
#   => value 값 큰 것부터 내림차순 정렬

# 문제) 상위 k의 빈도수
# inupt: list, k
#   -> list의 상위 빈도수 순으로 k의 요소를 추출

import collections
import heapq

#point) counter, heapq(list -> heap) -> heapqpush, heapqpop

# 1. counter라는 내장 함수를 통해 "리스트의 요소(key): 빈도수(value)로 도출(빈도수 높은 우선순위로 내림차순)
# 2. heapq모듈(최소힙만 적용)을 통해 heapqpop을 통해 우선순위가 가장 작은 데이터를 우선적으로 가져올 수 있다.
#      heapq: heap 자료구조를 파이썬 내장 모듈로 구현


def topKFrequent(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 읍수로 삽입 -> heappop시 가장 작은 값을 return한다.
    #               -> 부호가 반대 -> 가장 큰 값을 return한다.
    for f in freqs:
        # heappush() -> 첫번째 인자: 원소를 추가할 대상 리스트
        #               두번째 인자: 추가할 원소
        # why?) key:value가 바뀐 이유? key값을 기준으로 오름차순으로 정렬
        # 빈도수를 기준으로 가장 작은(실제: 가장 큰)을 기준으로 내림차순
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        # heappop(): heap 구조의 가장 작은 key의 값을 꺼내온다.
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

ag1 = [1, 1, 1, 2, 2, 3]
ag2 = 2

topKFrequent(ag1, ag2)




































# from typing import List
#
#
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
#
#         res = []
#         for i in range(len(freq) -1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res



