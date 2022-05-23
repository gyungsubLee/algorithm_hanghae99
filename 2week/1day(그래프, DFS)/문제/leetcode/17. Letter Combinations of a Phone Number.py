# 문제)https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List
#
# 풀이1)
# def letterCombinations(digits: str) -> List[str]:
#     letter = {
#         '2': ["a", "b", "c"],
#         '3': ["d", "e", "f"],
#         '4': ["g", "h", "i"],
#         '5': ["j", "k", "l"],
#         '6': ["m", "n", "o"],
#         '7': ["p", "q", "r", "s"],
#         '8': ["t", "u", "v"],
#         '9': ["w", "x", "y", "z"]}
#     result = []
#     for digit in digits:
#         if not result:
#             result = letter[digit]
#         else:
#             tmp = []
#             for r in result:
#                 for l in letter[digit]:
#                     tmp.append(r+l)
#             # 해당 변수에 다른 메모리 주소를 할당시킴.
#             result = tmp
#     return result
#
# letterCombinations("23")

# 풀이2)

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                # digits = "23"인데 왜 "2"와 "3"을 차례로 가르키지?
                # print(digits[i]) -> 디버그로 찍어보니 digits[0] = 2, digits[1] = 3 이 차례로 나옴.
                # 정신 나갔나... 당연한 걸...
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result

Solution().letterCombinations("23")