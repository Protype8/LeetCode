class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        current_max = 0
        nums2 = nums.copy()
        for i in range(1,len(nums)):
            if(nums[i-1] > nums[i]):
                nums.pop(i-1)
                nums2.pop(i)
                break
        a = sorted(nums)
        b = sorted(nums2)
        if(a == nums or b == nums2):
            return True
        else:
            return False

