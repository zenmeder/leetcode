class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        root = t1
        t1.val += t2.val
        if t2.left:
            if not t1.left:
                t1.left = t2.left
            else:
                self.mergeTrees(t1.left, t2.left)
        if t2.right:
            if not t1.right:
                t1.right = t2.right
            else:
                self.mergeTrees(t1.right, t2.right)
        return root

