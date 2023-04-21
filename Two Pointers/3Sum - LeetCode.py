class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        all_list = []
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            left_pointer = i+1
            right_pointer = len(nums)-1
            right_inputs = []
            while left_pointer < right_pointer:
                if(nums[i]+nums[left_pointer]+nums[right_pointer] < 0):
                    left_pointer +=1
                elif(nums[i]+nums[left_pointer]+nums[right_pointer] > 0):
                    right_pointer -=1
                else:
                    all_list.append([nums[i],nums[left_pointer],nums[right_pointer]])
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer-1] and left_pointer < 
right_pointer:
                        left_pointer+=1
        return all_list
