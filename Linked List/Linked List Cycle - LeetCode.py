# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortise = head
        hare = head
        while tortise and tortise.next:
            hare = hare.next
            tortise = tortise.next.next
            if(hare == tortise):
                return True
