# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeNode(self,node1,node2):
        if(not node1 and not node2):
            return None
        new_node = TreeNode()
        new_node.val = (node1.val if node1 else 0)+(node2.val if node2 else 0)
        print(new_node)
        new_node.left = self.mergeNode(node1.left if node1 else None,node2.left if node2 else 
None)
        new_node.right = self.mergeNode(node1.right if node1 else None,node2.right if node2 else 
None)
        return new_node
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional
[TreeNode]:
        root = self.mergeNode(root1,root2)
        return root
