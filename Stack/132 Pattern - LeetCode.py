class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if(stack and stack[-1][1] < n):
                return True
            stack.append((n,curMin))
            print(stack)
            curMin = min(curMin,n)
                    
