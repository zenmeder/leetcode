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
	def __init__(self):
		self.lst = []
		self.result = []

	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if not root:
			return 0
		lst = [root]
		res = []
		while lst:
			res.append(sum([n.val for n in lst])/len(lst))
			lstc = []
			for node in lst:
				if node.left:
					lstc.append(node.left)
				if node.right:
					lstc.append(node.right)
			lst = lstc[:]
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
print(Solution().averageOfLevels(a))

