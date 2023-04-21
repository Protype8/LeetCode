# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    correct = True
    def depth(self,root):
        if(self.correct):
            if(root == None):
                return -1
            left_depth = self.depth(root.left)+1
            right_depth = self.depth(root.right)+1
            if(abs(left_depth-right_depth) > 1):
                self.correct = False
            m = max(left_depth,right_depth)
            return m
        return 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth(root)
        return self.correct
