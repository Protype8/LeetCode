# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        val = 0
        prev_level = 0
        def dfs(node,level):
            nonlocal prev_level,val
            if(not node):
                return
            if(not node.left and not node.right):
                if(level > prev_level):
                    prev_level = level
                    val = node.val
            if(node.left):
                dfs(node.left,level+1)
            if(node.right):
                dfs(node.right,level+1)
        dfs(root,1)
        return val
            

