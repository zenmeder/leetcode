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
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        p = self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        if s.val != t.val:
            return p
        return p or (self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right))

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (not t and s) or s.val != t.val:
            return False
        return self.isSameTree(s.left,t.left) and self.isSameTree(s.right, t.right)

a = TreeNode()