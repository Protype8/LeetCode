class Solution:
    def jump(self, nums: List[int]) -> int:
        current_index = 0
        jumps = 0
        while current_index < len(nums)-1:
            #Jump as much as possible
            next_index = current_index+nums[current_index]
            max_num = -1000000000
            for i in range(1,nums[current_index]+1):
                if(current_index+i >= len(nums)):
                    break
                over_1_distance = nums[current_index]-nums[current_index+i] < i
                if(nums[current_index+i] >= max_num and over_1_distance):
                    next_index = current_index+i
                    max_num = nums[current_index+i]
                max_num -= 1
            if(current_index+nums[current_index] >= len(nums)-1):
                jumps+=1
                break
            else:
                current_index = next_index
                jumps+=1
        return jumps
