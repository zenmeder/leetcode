#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class NumArray(object):
	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		# self.nums = nums
		# 新建树状数组
		tree = [0]
		for i in range(1, len(nums) + 1):
			tree.append(i & -i)
		# self.tree = tree
		self.nums = nums
		for i in range(1, len(nums) + 1):
			tree[i] = sum(nums[i - tree[i]:i])
		self.tree = tree

	def update(self, i, val):
		"""
		:type i: int
		:type val: int
		:rtype: void
		"""
		j = i + 1
		diff = val - self.nums[i]
		while j < len(self.nums):
			self.tree[j] += diff
			j += j & (-j)
		self.nums[i] = val


	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self.getSum(j+1)-self.getSum(i)
	def getSum(self, i):
		result = 0
		j = i
		while j > 0:
			result += self.tree[j]
			j -= j & (-j)
		return result


a = NumArray([1])
# print(a.update(0,2))
print(a.sumRange(0,0))

