class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        left = 0
        right = len(nums)-1
        while right >= left:
            if(abs(nums[left]) >= abs(nums[right])):
                sorted_nums.append(nums[left]**2)
                left += 1
            else:
                sorted_nums.append(nums[right]**2)
                right -= 1
        return sorted_nums[::-1]
