class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        pre = 1
        post = 1
        length = len(nums)
        for i in range(length):
            pre *= nums[i]
            post *= nums[length-i-1]
            postfix.append(post)
            prefix.append(pre)
        postfix = postfix[::-1]
        output = []
        print(prefix)
        print(postfix)
        for i in range(length):
            ans = 1
            if(i-1 >= 0):
                ans *= prefix[i-1]
            if(i+1 < length):
                ans *= postfix[i+1]
            output.append(ans)
        return output
