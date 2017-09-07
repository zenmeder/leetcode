#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for a binary tree node.
from functools import reduce
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumNumbers(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		visit = {} #1 mean left child visited 2 mean right
		stack = []
		p = root
		result = []
		while p:
			if p.left and p not in visit:
				stack.append(p)
				visit[p] = 1
				p = p.left
				continue
			elif p.right and (p not in visit or visit[p] == 1):
				stack.append(p)
				visit[p] = 2
				p = p.right
				continue
			elif not p.left and not p.right:
				stack.append(p)
				result.append(''.join([str(node.val) for node in stack]))
				stack.pop()
			if not stack:
				break
			p = stack.pop()
			while stack and p in visit and visit[p] == 2:
				p = stack.pop()
		result = reduce(self.add, result)
		return result
	def add(self, str1, str2):
		return int(str1)+int(str2)
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
# a.right = c
# b.left = e
# b.right = f
print(Solution().sumNumbers(a))

