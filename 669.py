#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root
        while root.val > R or root.val < L:
            root = root.left if root.val > R else root.right
        self.trim(root, 0, L, R)
        self.trim(root, 1, L, R)
        return root

    def trim(self, p, ori, L, R):
        q = p.left if not ori else p.right
        if q:
            if L <= q.val <= R:
                self.trim(q, 0, L, R)
                self.trim(q, 1, L, R)
            elif q.val < L:
                if not ori:
                    p.left = q.right
                else:
                    p.right = q.right
                self.trim(p, ori, L, R)
            elif q.val > R:
                if not ori:
                    p.left = q.left
                else:
                    p.right = q.left
                self.trim(p, ori, L, R)
a = TreeNode(3)
b = TreeNode(0)
c = TreeNode(4)
d = TreeNode(2)
e = TreeNode(1)
a.left = b
a.right = c
b.right = d
d.left = e

Solution().trimBST(a, 0, 3)
print(a.left.val)
print(a.left.right.val)