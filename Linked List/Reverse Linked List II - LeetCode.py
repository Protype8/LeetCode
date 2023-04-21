# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self,node):
        a = node.next
        if(a == None):
            return node
        if(a.next == None):
            a.next = node
            node.next = None
            return a
        new_head = self.reverseNode(a)
        node.next = None
        a.next = node
        return new_head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional
[ListNode]:
        count = 0
        start = head
        reverse_start = reverse_end = None
        dummyNode = ListNode(val=-1)
        dummyNode.next = head
        head = dummyNode
        while head:
            if(count+1 == left):
                reverse_start = head
            if(count == right):
                reverse_end = head
                break
            count += 1
            head = head.next
