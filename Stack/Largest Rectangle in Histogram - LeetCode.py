class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_h = 0
        for i in range(len(heights)):
            current_index = i
            while stack and stack[-1][0] >= heights[i]:
                a = stack.pop()
                h = a[0]*(i-a[1])
                max_h = max(max_h,h)
                current_index = a[1]
            stack.append((heights[i],current_index))
        print(stack)
        while stack:   
            a = stack.pop()
            h = a[0]*(len(heights)-a[1])
            max_h = max(max_h,h)
        return max_h
