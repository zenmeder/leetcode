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
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		orientation = 1 #left-to-right
		nodes = [root]
		res = []
		if not root:
			return res
		while nodes:
			res.append([n.val for n in nodes])
			copy = []
			if not orientation:
				for node in nodes[::-1]:
					if node.left:
						copy.append(node.left)
					if node.right:
						copy.append(node.right)
			else:
				for node in nodes[::-1]:
					if node.right:
						copy.append(node.right)
					if node.left:
						copy.append(node.left)
			orientation = 1 - orientation
			nodes = copy[:]

		return res

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

print(Solution().zigzagLevelOrder(a))





