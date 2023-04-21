import math
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        current = 1
        for num in nums:
            if(not current in nums):
                return current
            current+=1
        return max(nums)+1
