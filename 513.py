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
	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		nodes = [root]
		while nodes:
			copy = []
			left = nodes[0]
			print([a.val for a in nodes])
			while nodes:
				node = nodes[0]
				if node.left:
					copy.append(node.left)
				if node.right:
					copy.append(node.right)
				del nodes[0]
			nodes = copy[:]

		return left.val

a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(5)
d = TreeNode(0)
e = TreeNode(2)
f = TreeNode(4)
g = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(Solution().findBottomLeftValue(a))