class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        nums = sorted(set(nums))
        best_sequence = 1
        current_sequence = 1
        for i in range(len(nums)-1):
            if(nums[i]+1 == nums[i+1]):
                current_sequence+=1
            else:
                current_sequence = 1
            best_sequence = max(current_sequence,best_sequence)
        return best_sequence
                
