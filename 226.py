#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if not root.left and not root.right:
            root.left, root.right = root.right, root.left
            return root
        root.right, root.left = self.invertTree(root.left),  self.invertTree(root.right)
        return root

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
b.left = c
res = Solution().invertTree(a)
print(res.val)
print(res.right.val)
print(res.right.right.val)