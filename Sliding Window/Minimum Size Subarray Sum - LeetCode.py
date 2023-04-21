class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        window_size = float(inf)
        left = 0
        right = 0
        while right < len(nums):
            current_sum += nums[right]
            while(current_sum >= target):
                window_size = min(window_size,right-left+1)
                current_sum -= nums[left]
                left += 1
            right += 1
        return window_size if window_size != float(inf) else 0
