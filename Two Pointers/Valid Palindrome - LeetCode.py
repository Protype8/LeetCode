import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for w in s:
            if(w in string.ascii_lowercase or w in string.digits):
                new_s+=w
        if(new_s == new_s[::-1]):
            return True
        return False
