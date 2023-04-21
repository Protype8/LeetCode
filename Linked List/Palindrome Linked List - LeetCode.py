class ListNode:
    def __init__(self, val=0, next=None,previous = None):
        self.val = val
        self.next = next
        self.previous = previous
class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]
