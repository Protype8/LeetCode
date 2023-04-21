class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        w = 0
        ans = -1
        for i in set(nums):
            if(nums.count(i) > w):
                w = nums.count(i)
                ans = i
        return ans
