class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        res = 1 if current_sum/k >= threshold else 0
        for i in range(k,len(arr)):
            current_sum -= arr[i-k]
            current_sum += arr[i]
            if current_sum/k >= threshold:res += 1
        return res
