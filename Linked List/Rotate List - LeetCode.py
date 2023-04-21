# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ans = None
    def editLink(self,head,node,k):
        if(not node):
            return 0
        pos_from_last = self.editLink(head,node.next,k)+1
        if(pos_from_last == 1):
            node.next = head
        if(pos_from_last == k):
            self.ans = node
        if(pos_from_last == k+1):
            node.next = None
        return pos_from_last
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.ans = head
        if(not head):
            return
        len_of_linked_list = 0
        c = head
        while c:
            len_of_linked_list += 1
            c = c.next
        k %= len_of_linked_list
        if(k != 0):
            self.editLink(head,head,k)
        return self.ans
