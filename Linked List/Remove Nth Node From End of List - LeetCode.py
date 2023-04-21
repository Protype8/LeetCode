# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trevase(self,prev_node,node,n):
        if(node == None):
            return 0
        from_last = self.trevase(node,node.next,n)+1
        print(from_last,node.val)
        if(from_last == n):
            prev_node.next = node.next
        return from_last
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        self.trevase(dummyNode,head,n)
        return dummyNode.next
