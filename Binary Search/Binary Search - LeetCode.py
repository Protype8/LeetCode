class Solution:
    def binary_search(self,nums,high,low,target):
        mid = (high+low)//2
        if(nums[mid] == target):
            print("found",target,"at index",mid)
            return mid
        if(high > low):
            if(nums[mid] > target):
                return self.binary_search(nums,mid-1,low,target)
            elif(nums[mid] < target):
                return self.binary_search(nums,high,mid+1,target)
        else:
            return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,len(nums)-1,0,target)
