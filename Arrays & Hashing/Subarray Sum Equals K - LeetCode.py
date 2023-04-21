class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        current_sum = 0
        total = 0
        for i in nums:
            current_sum += i
            prefix_to_remove = current_sum-k
            if(prefix_to_remove in prefix_sum):
                total += prefix_sum[prefix_to_remove]
            cur = prefix_sum.get(current_sum,0)
            prefix_sum[current_sum] = cur+1
        return total
