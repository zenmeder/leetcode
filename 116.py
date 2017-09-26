#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if not root:
			return root
		nodes = [root]
		while nodes:
			nxt = []
			for i, node in enumerate(nodes):
				node.next = nodes[i + 1] if i != len(nodes)-1 else None
				if node.left:
					nxt.append(node.left)
				if node.right:
					nxt.append(node.right)
			nodes = nxt[:]
		return root