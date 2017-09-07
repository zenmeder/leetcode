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
	def inorderTraversal(self, root):
		res, stack = [], []
		while True:
			while root:
				stack.append(root)
				root = root.left
			if not stack:
				return res
			node = stack.pop()
			res.append(node.val)
			root = node.right

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
print(Solution().inorderTraversal(a))
