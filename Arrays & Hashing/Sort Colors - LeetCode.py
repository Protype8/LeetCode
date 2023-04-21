class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = 0
        nums_cop = nums.copy()
        for i in range(0,3):
            for _ in range(nums_cop.count(i)):
                nums[count] = i
                count += 1
