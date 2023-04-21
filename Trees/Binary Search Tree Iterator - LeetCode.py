# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.order = self.inorderTraversal(root)
        self.count = -1
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return
        stack = [root]
        l = []
        while stack:
            cur = stack[-1]
            if(cur.left):
                stack.append(cur.left)
                cur.left = None
            elif(cur.right):
                stack.pop()
                l.append(cur.val)
                stack.append(cur.right)
                cur.right = None
            else:
                stack.pop()
                l.append(cur.val)
        return l
    def next(self) -> int:
        self.count+=1
        return self.order[self.count]
    def hasNext(self) -> bool:
        return self.count < len(self.order)-1
