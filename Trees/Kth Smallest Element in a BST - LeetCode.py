# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    a = []
    def build(self,node):
        if(not node):
            return []
        return self.build(node.left)+[node]+self.build(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.build(root)[k-1].val
