class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = nums[len(nums)-(k%len(nums)):]+nums[:len(nums)-(k%len(nums))]
        nums[:] = n

