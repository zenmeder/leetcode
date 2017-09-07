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
		nodes = [root]
		maxWidth = 1
		while True:
			c = []
			for node in nodes:
				if not node:
					c += [None, None]
				else:
					c.append(node.left)
					c.append(node.right)
			i, j = 0, len(c)-1
			while i < len(c) and not c[i]:
				i += 1
			while j >= 0 and not c[j]:
				j -= 1
			if j < i:
				break
			maxWidth = max(maxWidth, j - i + 1)
			nodes = c[:]
		return maxWidth


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
