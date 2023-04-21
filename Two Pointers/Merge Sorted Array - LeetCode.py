class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if(nums1[pointer1] > nums2[pointer2]): 
                nums1.insert(pointer1,nums2[pointer2])
                pointer2+=1
                nums1.pop()
                print(nums1)
            else:
                pointer1+=1
        for i in range(pointer2,len(nums2)):
            nums1[i+(len(nums1)-len(nums2))] = nums2[i]
        print(nums1)
