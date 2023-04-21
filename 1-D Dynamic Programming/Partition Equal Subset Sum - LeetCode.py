class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2):
            return False
        dp = set()
        dp.add(0)
        dp.add(nums[0])
        for i in nums[1:]:
            nextDp = set()
            for t in dp:
                nextDp.add(t+i)
                nextDp.add(t)
            dp = nextDp
        print(dp)
        if(sum(nums)//2 in dp):
            return True
        else:
            return False
                
                
