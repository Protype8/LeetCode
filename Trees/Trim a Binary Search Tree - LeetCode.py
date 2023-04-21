# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            while node and not low <= node.val <= high:
                if(node.val < low):
                    node = node.right
                elif(node.val > high):
                    node = node.left
            if(node):
                if(node.left):
                    node.left = trim(node.left)
                if(node.right):
                    node.right = trim(node.right)
            return node
        return trim(root)

