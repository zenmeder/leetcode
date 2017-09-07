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
	def pathSum(self, root, sum):
		if not root:
			return []
		if not root.left and not root.right and sum == root.val:
			return [[root.val]]
		tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
		return [[root.val]+i for i in tmp]

a,b,c,d,e,f,g,h,i,j = map(lambda x: TreeNode(x), [5,4,8,11,13,4,7,2,5,1])
# print(Solution().pathSum())
a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
d.left = g
d.right = h
f.left = i
f.right = j
print(Solution().pathSum(a, 22))

