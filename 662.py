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
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        root.val, res = 0, 0
        nodes = [root]
        while nodes:
            res = max(res, nodes[-1].val - nodes[0].val + 1)
            nodes_copy = []
            for node in nodes:
                if node.left:
                    node.left.val = 2*node.val -1
                    nodes_copy.append(node.left)
                if node.right:
                    node.right.val = 2*node.val
                    nodes_copy.append(node.right)
            nodes = nodes_copy[:]
        return res


a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(3)
f = TreeNode(9)
g = TreeNode(10)
a.left = b
a.right = c
b.left = d
d.left = e
c.right = f
f.right = g
print(Solution().widthOfBinaryTree(a))
