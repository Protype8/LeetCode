# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return
        stack = [root]
        visited = set([])
        l = []
        while stack:
            cur = stack[-1]
            if(cur.left and not cur.left in visited):
                stack.append(cur.left)
                visited.add(cur.left)
            elif(cur.right and not cur.right in visited):
                stack.pop()
                l.append(cur.val)
                stack.append(cur.right)
                visited.add(cur.right)
            else:
                stack.pop()
                l.append(cur.val)
        return l
