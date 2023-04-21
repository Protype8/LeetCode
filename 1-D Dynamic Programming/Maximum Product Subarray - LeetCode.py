import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_highest = nums[0]
        current_lowest = nums[0]
        max_num = nums[0]
        for i in range(1,len(nums)):
            temp_highest = current_highest
            current_highest = max(current_highest*nums[i],current_lowest*nums[i],nums[i])
            current_lowest = min(temp_highest*nums[i],current_lowest*nums[i],nums[i])
            print(current_highest,current_lowest)
            max_num = max(max_num,current_highest)
        return max_num
