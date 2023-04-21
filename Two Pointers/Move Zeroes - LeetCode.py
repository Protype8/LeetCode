class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        e =[num for num in nums if num != 0]+[0]*nums.count(0)
        for i in range(len(nums)):
            nums[i] = e[i]
        print(nums)
