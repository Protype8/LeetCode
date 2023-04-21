class Solution:
    def binary_search(self,arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            if(low >= len(arr)):
                return high
            return low if abs(arr[low]-x) < abs(arr[high]-x) else high
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if(len(arr) == 1):
            return arr
        closest_index = self.binary_search(arr, 0, len(arr)-1, x)
        print(closest_index)
        l = r = closest_index
        while r-l+1 < k:
            if(l-1 >= 0 and r+1 < len(arr)):
                if(abs(arr[l-1]-x) <= abs(arr[r+1]-x)):
                    l-=1
                else:
                    r += 1
            elif(l-1 < 0):
                r += 1
            elif(r+1 >= len(arr)):
                l -= 1
        print(l,r)
        return arr[l:r+1]

