# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root,current):
            if(root == None):
                return current
            m = max(depth(root.left,current+1),depth(root.right,current+1))
            return m
        return depth(root,0)
        
        
        
