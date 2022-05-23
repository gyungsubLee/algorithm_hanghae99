from typing import List

def largestNumber(nums: List[int]) -> str:
    i = 0
    while i < len(nums):
        j = i
        while j > 0 and str(nums[j-1]) + str(nums[j]) < str(nums[j]) + str(nums[j-1]):
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        i += 1

    return str(int(''.join(map(str, nums))))

l1 = ['10', '2']

t = largestNumber(l1)
print(t)
