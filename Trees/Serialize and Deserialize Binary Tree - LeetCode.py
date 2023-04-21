# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        s = ""
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if(not node):
                s+="N,"
            else:
                s+=str(node.val)+","
                stack.append(node.left)
                stack.append(node.right)
        return s[0:-1]
    def deserialize(self, data):
        data = data.split(",")
        if(data == ["N"]):
            return None
        root = TreeNode(data[0])
        i = 1
        stack = deque([root])
        a = True
        while stack:
            if(a):
                left = TreeNode(data[i]) if data[i] != "N" else None
                stack[0].left = left
                if(left):
                    stack.append(left)
