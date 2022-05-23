# 문제)https://leetcode.com/problems/subsets/
from typing import List


# def subsets(nums: List[int]) -> List[List[int]]:
#     # 트리 구조의 dfs로 해결하기
#     result = []
#     def dfs(idx, path):
#         result.append(path)
#         # idx 순서대로 경로를 만들면서 dfs 연산
#         for next_idx in range(idx, len(nums)):
#             dfs(next_idx + 1, path + nums[next_idx])
#             #의문점) [] + []는 합쳐지나?
#
#     dfs(0, [])
#     return result

# t = [1, 2, 3]
# subsets(t)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
                # return 시, 재귀함수가 호출된
                # 재귀함수 호출 시 해당 함수의 메모리 주소
                # 코드 전개, 메모리 할당? 따라서 return 시 함수가 호출될 때를 메모리에 저장해서 불러오는 건가?


            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            # 의문점1) return 전 i = 3 이었는데, return 후 i = 2가 되었다. return을 하면 이전 변수 값도 가져오는 건가?
            #         i = 2 에서 44번 줄 다시 재귀호출로 인해 i=3이 된다. 근데 다시 return 시 i = 1이 된다. 왜 그렇지?
            # 의문점2) i라 명시하지 않는데, 왜 i로 들어가지?
            dfs(i + 1)
        dfs(0)
        return res

t = [1, 5, 2]
Solution().subsets(t)