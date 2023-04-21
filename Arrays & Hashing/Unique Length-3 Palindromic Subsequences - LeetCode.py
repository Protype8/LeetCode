class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        output = 0
        reverse_s = s[::-1]
        for unique_char in set(s):
            first_index = s.index(unique_char)
            last_index  = len(s) - reverse_s.index(unique_char) - 1
            if(last_index > first_index):
                characters = len(set(s[first_index+1:last_index]))
                output+=characters
        return output

