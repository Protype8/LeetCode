class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = [0 for num in range(len(nums))]
        for i in range(0,len(profit)):
            if(i < 2):
                profit[i] = nums[i]
            if(i+2 < len(profit)):
                if(profit[i]+nums[i+2] > profit[i+2]):
                    profit[i+2] = profit[i]+nums[i+2]
            if(i+3 < len(profit)):
                if(profit[i]+nums[i+3] > profit[i+3]):
                    profit[i+3] = profit[i]+nums[i+3]
        print(profit)
        if(len(profit) == 1):
            return profit[0]
        return max(profit[-1],profit[-2])
