# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return
        start = head.next if head.next else head
        prev = ListNode(val=100)
        while head and head.next:
            n = head.next
            print(prev.val,head.val,n.val)
            head.next = n.next
            n.next = head
            prev.next = n
            prev = head
            head = head.next
        return start
