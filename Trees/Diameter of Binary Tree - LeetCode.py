# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    biggest = 0
    def depth(self,root):
        if(root == None):
            return -1
        left_depth = self.depth(root.left)+1
        right_depth = self.depth(root.right)+1
        self.biggest = max(self.biggest,left_depth+right_depth)
        m = max(left_depth,right_depth)
        return m
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.depth(root)
        return self.biggest
