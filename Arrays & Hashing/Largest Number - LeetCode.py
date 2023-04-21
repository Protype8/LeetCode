from math import floor,log10 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ""
        nums = [str(i) for i in nums]
        while nums != []:
            current_num = nums[0]
            for i in range(1,len(nums)):
                if(int(current_num+nums[i]) < int(nums[i]+current_num)):
                    current_num = nums[i]
            result+= current_num
            nums.remove(current_num)
        return str(int(result))
        
