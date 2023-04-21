# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = None
        process = head
        while process:
            if(not current_node):
                current_node = process
            elif(process.val != current_node.val):
                current_node.next = process
                current_node = current_node.next
            process = process.next
        if(current_node):
            current_node.next = None
        return head
