#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def find(root, sum):
            res = 0
            if not root:
                return res
            if root.val == sum:
                res += 1
            res += find(root.left, sum - root.val)
            res += find(root.right, sum - root.val)
            return res

        return find(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)