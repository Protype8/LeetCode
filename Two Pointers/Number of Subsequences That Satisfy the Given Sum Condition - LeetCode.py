n = 100_000
pow2 = [1]*(n+1) 
for i in range(1, n+1):
    pow2[i] = pow2[i-1]*2 % 1_000_000_007
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0
        left = 0
        right = len(nums)-1
        while right >= left:
            if(nums[left]+nums[right] <= target):
                print(left,right)
                output += pow2[right-left]
                left+= 1
            else:
                right -= 1
        return output%1_000_000_007
