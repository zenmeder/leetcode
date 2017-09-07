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
	def largestValues(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		stack = [root]
		res = [root.val]
		while stack:
			stack_copy = []
			for node in stack:
				if node.left:
					stack_copy.append(node.left)
				if node.right:
					stack_copy.append(node.right)
			if not stack_copy:
				break
			res.append(max([n.val for n in stack_copy]))
			stack = stack_copy[:]
		return res

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.right = d
c.left = e
print(Solution().largestValues(a))

