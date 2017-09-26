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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes, res= [root], 0
        def tilt(root):
            if not root.left and not root.right:
                return 0
            elif not root.left and root.right:
                return abs(root.right.val)
            elif not root.right and root.left:
                return abs(root.left.val)
            else:
                return abs(root.left.val-root.right.val)
        while nodes:
            tmp = []
            for node in nodes:
                res += tilt(node)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            nodes = tmp[:]
        return res