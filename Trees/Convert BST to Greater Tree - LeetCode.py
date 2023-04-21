# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return
        stack = [root]
        visited = set([])
        s = 0
        l = []
        while stack:
            cur = stack[-1]
            if(cur.right and not cur.right in visited):
                stack.append(cur.right)
                visited.add(cur.right)
            elif(cur.left and not cur.left in visited):
                stack.pop()
                cur.val += s 
                s = cur.val
                stack.append(cur.left)
                visited.add(cur.left)
            else:
                stack.pop()
                cur.val += s 
                s = cur.val
        return root
