class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            index = i
            current_length = 0
            current_words = []
            while(s[index] not in current_words):
                current_length+=1
                current_words.append(s[index])
                if(index+1 == len(s)):
                    break
                index+=1
            print(current_length)
            max_length = max(max_length,current_length)
            
        return max_length
