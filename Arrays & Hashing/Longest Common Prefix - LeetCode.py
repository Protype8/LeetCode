class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = ""
        count = 0
        while True:
            for w in strs:
                if(count == len(w)):
                    return strs[0][0:count]
                if(w[count] != strs[0][count]):
                    return strs[0][0:count]
            else:
                count += 1

