class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []
        def merge():
            i = j = 0
            while i < len(nums1) and j < len(nums2):
                if(nums1[i] < nums2[j]):
                    new_arr.append(nums1[i])
                    i+=1
                else:
                    new_arr.append(nums2[j])
                    j+=1
            for k in range(i,len(nums1)):
                new_arr.append(nums1[k])
            for l in range(j,len(nums2)):
                new_arr.append(nums2[l])
        merge()
        if len(new_arr)%2 == 1:
            return new_arr[len(new_arr)//2]
        else:
            return (new_arr[len(new_arr)//2]+new_arr[len(new_arr)//2-1])/2
