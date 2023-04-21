class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        all_list = []
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,len(nums)):
                if(j > i+1 and nums[j] == nums[j-1]):
                    continue
                left_pointer = j+1
                right_pointer = len(nums)-1
                right_inputs = []
                while left_pointer < right_pointer:
                    if(nums[i]+nums[j]+nums[left_pointer]+nums[right_pointer] < target):
                        left_pointer +=1
                    elif(nums[i]+nums[j]+nums[left_pointer]+nums[right_pointer] > target):
                        right_pointer -=1
                    else:
                        all_list.append([nums[i],nums[j],nums[left_pointer],nums[right_pointer]])
                        left_pointer += 1
                        while nums[left_pointer] == nums[left_pointer-1] and left_pointer < 
right_pointer:
                            left_pointer+=1
        return all_list
