class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        j = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j] = nums[i]
                count = 1
                j+=1
            elif nums[i] == nums[i-1] and count < 2:
                nums[j] = nums[i]
                count += 1
                j+=1
        return j 
