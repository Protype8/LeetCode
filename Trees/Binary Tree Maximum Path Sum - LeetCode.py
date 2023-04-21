# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if(not node):
                return [None,None]
            res_left = dfs(node.left)
            res_right = dfs(node.right)
            l,r = res_left[0] if res_left[0] else 0,res_right[0] if res_right[0] else 0
            continuable = max(l+node.val,r+node.val,node.val)
            not_continuable = max(res_left[0] if res_left[0] else float(-inf),res_right[0] if 
res_right[0] else float(-inf),l+r+node.val,res_left[1] if res_left[1] else float(-inf),res_right
[1] if res_right[1] else float(-inf))
            return [continuable,not_continuable]
        ans = dfs(root)
        print(ans)
        return max(ans)
