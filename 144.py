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
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		nodes = [root]
		res = []
		while nodes:
			node = nodes.pop()
			res.append(node.val)
			if node.right:
				nodes.append(node.right)
			if node.left:
				nodes.append(node.left)

		return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d

i = Solution().preorderTraversal(None)
