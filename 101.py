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
	def isSymmetric(self, root):
		if not root:
			return True
		nodes = [root]
		while nodes:
			copy = []
			values = []
			for node in nodes:
				if node.left:
					values.append(node.left.val)
					copy.append(node.left)
				else:
					values.append(None)

				if node.right:
					values.append(node.right.val)
					copy.append(node.right)
				else:
					values.append(None)
			if values[:len(values)//2] != values[len(values)//2:][::-1]:
				return False
			nodes = copy[:]

		return True

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(Solution().isSymmetric(a))