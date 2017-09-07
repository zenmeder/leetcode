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
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return False
		def height(root):
			if not root:
				return 0
			return 1+max(height(root.left), height(root.right))
		nodes = [root]
		while nodes:
			node = nodes.pop()
			if abs(height(node.left)-height(node.right)) > 1:
				return False
			if node.left:
				nodes.append(node.left)
			if node.right:
				nodes.append(node.right)
		return True

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
b.right = c
print(Solution().isBalanced(a))