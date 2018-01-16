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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        visited = {}
        def dfs(root):
            self.h += 1
            visited[root] = True
            if not root.left:
                if self.h == self.height:
                    self.count += 1
                else:
                    self.flag = 1
            if root.left and root.left not in visited and not self.flag:
                dfs(root.left)
                self.h -= 1
            if root.right and root.right not in visited and not self.flag:
                dfs(root.right)
                self.h -= 1
        self.count, self.h, self.height, self.flag, p= 0, 0, 1, 0,root
        while root.left:
            self.height += 1
            root = root.left
        dfs(p)
        return 2**(self.height-1)+self.count-1

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
print(Solution().countNodes(a))