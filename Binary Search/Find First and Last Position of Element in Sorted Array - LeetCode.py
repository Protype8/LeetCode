class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start , end = 0 ,len(nums) - 1 
        while start  <=  end:
            mid = (start + end ) // 2
            if(nums[mid] == target):
                print(mid)
                a = [mid,mid]
                c = 1
                while mid-c >= 0 and nums[mid-c] == target:
                    a[0] -= 1
                    c+=1
                c = 1
                while mid+c < len(nums) and nums[mid+c] == target:
                    a[1] += 1
                    c+=1
                return a
            elif nums[mid] > target:
                end = mid - 1 
            else:
                start = mid + 1
        return [-1,-1]
