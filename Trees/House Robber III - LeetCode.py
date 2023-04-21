# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if(not node):
                return [0,0]
            res_left = dfs(node.left)
            res_right = dfs(node.right)
            with_root = node.val+res_left[1]+res_right[1]
            without_root = max(res_left[0],res_left[1])+max(res_right[0],res_right[1])
            return [with_root,without_root]
        return max(dfs(root))
