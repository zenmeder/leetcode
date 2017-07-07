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
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		maxLength = 0
		node = [root]
		flag = 0
		while len(node) != 0:
			if flag == 0:
				p = node[0].left
			elif flag == 1:
				p = node[0].right
