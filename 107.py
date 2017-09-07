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
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		lst = [root]
		res = []
		while lst:
			res.append([n.val for n in lst])
			lstc = []
			for node in lst:
				if node.left:
					lstc.append(node.left)
				if node.right:
					lstc.append(node.right)
			lst = lstc[:]
		return res[::-1]

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().levelOrderBottom(a))