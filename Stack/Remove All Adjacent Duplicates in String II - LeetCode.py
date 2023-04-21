class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0],1]]
        for i in range(1,len(s)):
            if(s[i] == stack[-1][0]):
                stack[-1][1] += 1
            else:
                while stack and stack[-1][1] >= k:
                    a,b = stack.pop()
                    if(b-k != 0):
                        stack.append([a,b-k])
                if(not stack or stack[-1][0] != s[i]):
                    stack.append([s[i],1])
                else:
                    stack[-1][1] += 1
        while stack and stack[-1][1] >= k:
            a,b = stack.pop()
            if(b-k != 0):
                stack.append([a,b-k])
        result = ""
        for i in stack:
            result += i[0]*i[1]
        return result
