class Solution:
    def reverseString(self, s: List[str]) -> None:
        left_pointer = 0
        right_pointer = len(s)-1
        while right_pointer >= left_pointer:
            s[left_pointer],s[right_pointer] = s[right_pointer],s[left_pointer]
            left_pointer += 1
            right_pointer -= 1
