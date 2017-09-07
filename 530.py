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
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		res = [root.val]
		nodes = [root]
		while nodes:
			copy = []
			for node in nodes:
				if node.left:
					copy.append(node.left)
					res.append(node.left.val)
				if node.right:
					copy.append(node.right)
					res.append(node.right.val)
			nodes = copy[:]
		res = sorted(res)

		return min([abs(res[i]-res[i+1]) for i in range(len(res)-1)])
