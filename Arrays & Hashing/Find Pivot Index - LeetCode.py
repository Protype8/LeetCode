class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        current_left = 0
        current_right = sum(nums[1:])
        result = -1
        if(current_left == current_right):
            return 0
        for i in range(1,len(nums)):
            current_left += nums[i-1]
            current_right -= nums[i]
            if(current_left == current_right):
                result = i
                break
        return result
