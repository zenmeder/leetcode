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
	def __init__(self):
		self.lst = []
		self.result = []

	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""

	def tarverse(self, root, p):
		lst = self.lst
		if root.left != None:
			lst.append(root.left)
		if root.right != None:
			lst.append(root.right)
		if p > (len(lst) - 2):
			return
		else:
			self.tarverse(lst[p + 1], p + 1)
