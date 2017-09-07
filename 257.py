#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def binaryTreePaths(self, root):
		self.ans = []
		if not root:
			return self.ans
		def dfs(root, path):
			print(root.val)
			if not root.left and not root.right:
				self.ans.append(path)
			if root.left:
				dfs(root.left, path+"->"+str(root.left.val))
			if root.right:
				dfs(root.right, path+"->"+str(root.right.val))
		dfs(root,str(root.val))
		return self.ans

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
# c.left = e
# c.right = f
print(Solution().binaryTreePaths(a))


