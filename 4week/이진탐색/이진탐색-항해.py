# 항해99 - 알고리즘 강의
# 구현
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)


assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

import bisect

#좋은 엔지니어의 자세: '이게 있네?' '저것도 있어야 하지 않나?' -> 좋은 가설과 직감(논리구조상 반대거나 비슷한 부분을 생각 할 수 있어야함.)
                  # bisect_left -> bisect_right, bisect 에 대한 의문(좋은 엔지니어의 태도)

#내장모듈 - bisect
def binary_search_builtin(nums, target):
    """
    1) Array 안에 target이 있는 경우
    [-1, 1, 2, 2, 2, 3]  target=2
    bisect_left = 2
     -> list 안에 target이 중복으로 있는 경우, 제일 왼쪽에 있는 index를 return함.

    2)Array 안에 target이 없는 경우
        2-1)
        [-1, 1, 3, 3, 5]  target=2
        bisect_left = 2
         -> target을 기준으로 작은 값, 크거나 같은 값으로 나누고 해당 index를 return함.

        2-2)
        [-5, -4, -3, -2, -1] target=2
        bisect_left = 5
         -> target보다 모든 값이 작기때문에 list 길이를 return함.

        2-3)
        [3, 4, 5, 6, 7]  target=2
        bisect+left = 0
         -> target 보다 모든 값이 크기 때문에 최소 index return.

    결론) 작으면: index+1, 크거나 같으면: index
    """
    idx = bisect.bisect_left(nums, target)
        # idx == len(nums) 가능하기 떄문.
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1
