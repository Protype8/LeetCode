class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        res = 0
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        for i in range(len(nums)):
            n = nums[i]
            newStart = i
            while stack and stack[-1][1] > n:
                start,num = stack.pop()
                res = max(res,(prefix[i]-prefix[start])*num)
                newStart = start
            stack.append((newStart,n))
        for start,num in stack:
            total = (prefix[len(nums)]-prefix[start])
            res = max(res,total*num)
        return res%(10**9 + 7)
