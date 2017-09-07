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
	def constructMaximumBinaryTree(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		maxValue = nums[0]
		maxPosition = 0
		for i in range(len(nums)):
			if nums[i] > maxValue:
				maxPosition = i
				maxValue = nums[i]

		root = TreeNode(nums[maxPosition])
		root.left = self.constructMaximumBinaryTree(nums[:maxPosition])
		root.right = self.constructMaximumBinaryTree(nums[maxPosition+1:])

		return root