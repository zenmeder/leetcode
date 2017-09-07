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
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		values = []
		def midOrder(root):
			if root:
				midOrder(root.left)
				# if values and root.val <= values[-1]:
				# 	return False
				values.append(root.val)
				midOrder(root.right)
		midOrder(root)
		for i in range(len(values)-1):
			if values[i] >= values[i+1]:
				return False
		return True
a = TreeNode(1)
b = TreeNode(1)
a.right = b
print(Solution().isValidBST(a))