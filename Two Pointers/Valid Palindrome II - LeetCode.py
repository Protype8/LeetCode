class Solution:
    def validPalindrome(self, s: str) -> bool:
        right_pointer = len(s)-1
        left_pointer = 0
        while right_pointer >= left_pointer:
            if(s[right_pointer] != s[left_pointer]):
                ll_p,rr_p = left_pointer+1,right_pointer
                while rr_p >= ll_p:
                    if(s[rr_p] != s[ll_p]):
                        break
                    ll_p +=1
                    rr_p -=1
                else:
                    return True
                ll_p,rr_p = left_pointer,right_pointer-1
                while rr_p >= ll_p:
                    if(s[rr_p] != s[ll_p]):
                        break
                    ll_p +=1
                    rr_p -=1
                else:
                    return True
                return False
            left_pointer += 1
            right_pointer -= 1  
        return True
