class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1]
        greatest = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            result.append(greatest)
            if(arr[i] > greatest):
                greatest = arr[i]
        return result[::-1]
