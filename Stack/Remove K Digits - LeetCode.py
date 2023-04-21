class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k == len(num)):
            return "0"
        stack = [num[0]]
        i = 1
        while i < len(num):
            while(stack and stack[-1] > num[i] and k > 0):
                stack.pop()
                k-=1
            if(stack or num[i] != "0"):
                stack.append(num[i])
            i += 1
        stack = "".join(stack[:len(stack)-k])
        return stack or "0"
