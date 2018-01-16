#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left:
            if not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
