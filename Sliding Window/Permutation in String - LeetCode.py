import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        sliding_window_size = len(s1)
        word_dict_list = {}
        if sliding_window_size == 1:
            return s1 in s2
        s1_word_dict = {i:0 for i in string.ascii_lowercase}
        for i in range(len(s1)):
            s1_word_dict[s1[i]] = s1_word_dict.get(s1[i],0)+1
        s2_word_dict = {i:0 for i in string.ascii_lowercase}
        for i in range(len(s2)):
            s2_word_dict[s2[i]] = s2_word_dict.get(s2[i],0)+1
            word_dict_list[i] = s2_word_dict.copy()
        if(word_dict_list[sliding_window_size-1] == s1_word_dict):
            return True
        for i in range(0,len(s2)-sliding_window_size):
            for alphabet in string.ascii_lowercase:
                if(word_dict_list[i+sliding_window_size][alphabet] - word_dict_list[i][alphabet] 
!= s1_word_dict[alphabet]):
                    break
            else:
                return True
        return False
