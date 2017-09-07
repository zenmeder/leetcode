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
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		nodes = [root]
		res = []
		while nodes:
			q = nodes.pop()
			if not q:
				break
			res.append(q)
			if q.right:
				nodes.append(q.right)
			if q.left:
				nodes.append(q.left)
		for i in range(len(res)-1):
			res[i].right = res[i+1]
			res[i].left = None

a = TreeNode(1)
a1 = TreeNode(2)
a2 = TreeNode(3)
a3 = TreeNode(4)
a4 = TreeNode(5)
a5 = TreeNode(6)
a.left = a1
# a.right = a4
# a1.left = a2
# a1.right = a3
# a4.right = a5

Solution().flatten(a)

while a:
	print(a.val)
	a = a.right
	print(a.left.val)

