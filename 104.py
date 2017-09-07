#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		lst = [root]
		res = 0
		while lst:
			lstc = []
			res += 1
			for node in lst:
				if node.left:
					lstc.append(node.left)
				if node.right:
					lstc.append(node.right)
			lst = lstc[:]
		return res