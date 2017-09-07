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
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		stack = []
		res = []
		stack.append(root)
		res.append(root.val)
		while stack:
			tmp = stack[:]
			node = stack.pop()
			while node:
				if node.right != None:
					res.append(node.right.val)
					break
				elif node.left != None:
					res.append(node.left.val)
					break
				if stack:
					node = stack.pop()
				else:
					break
			stack = []
			for node in tmp:
				if node.left:
					stack.append(node.left)
				if node.right:
					stack.append(node.right)

		return res
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.right = c
# a.left = b
# b.right = e
# c.right = d
result = Solution().rightSideView(None)
print(result)