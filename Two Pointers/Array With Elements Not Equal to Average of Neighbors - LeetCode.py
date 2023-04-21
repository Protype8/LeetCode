import collections
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        deque = collections.deque(nums)
        count = 0
        while count < len(nums):
            if(count%2 == 0):
                nums[count] = deque.popleft()
            else:
                nums[count] = deque.pop()
            count += 1
        return nums
