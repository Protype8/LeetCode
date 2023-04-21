import math
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        if(k == 1):
            return 0
        s=math.inf
        k -=1
        for i in range(k,len(nums)):
            print(nums[i],nums[i-k])
            s=min(s,nums[i]-nums[i-k])
        return s
