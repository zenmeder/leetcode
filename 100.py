#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if not p and not q:
			return True
		if not p or not q:
			return False
		nodes1 , nodes2 = [p],[q]
		while nodes1 and nodes2:
			n1 = nodes1.pop()
			n2 = nodes2.pop()
			if (n1.val and not n2.val) or (not n1.val and n2.val) or n1.val != n2.val:
				return False
			if (n1.right and not n2.right) or (n1.left and not n2.left) or (not n1.right and n2.right) or (not n1.left and n2.left):
				return False
			if n1.right:
				nodes1.append(n1.right)
				nodes2.append(n2.right)
			if n1.left:
				nodes1.append(n1.left)
				nodes2.append(n2.left)
		return True
a = TreeNode(2)
b = TreeNode(4)
c = TreeNode(3)
a.left = c
a.right = b
d = TreeNode(2)
e = TreeNode(4)
d.right = e
print(Solution().isSameTree(d,a))