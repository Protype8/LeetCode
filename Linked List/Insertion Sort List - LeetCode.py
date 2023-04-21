# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_head = head
        head = head.next
        cur_head.next = None
        while head:
            a = head
            head = head.next
            a.next = None
            b = cur_head
            if b.val > a.val:
                a.next = b
                cur_head = a
            else:
                while b and b.next:
                    if(b.next.val > a.val):
                        c = b.next
                        b.next = a
                        a.next = c
                        break
                    b = b.next
                else:
                    b.next = a
        return cur_head

