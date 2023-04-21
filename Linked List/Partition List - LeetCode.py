# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greaterThan = gStart = ListNode()
        lessThan  = lStart= ListNode()
        while head:
            if(head.val < x):
                lessThan.next = head
                lessThan = lessThan.next
            else:
                greaterThan.next = head
                greaterThan = greaterThan.next
            a = head
            head = head.next
            a.next = None
        lessThan.next = gStart.next
        return lStart.next

