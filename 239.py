#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		p = 0
		if len(nums) == 0:
			return []
		if k >= len(nums):
			return [max(nums)]
		result = []
		while p + k <= len(nums):
			result.append(max(nums[p:p+k]))
			p+=1
		return result
	def maxSlidingWindow2(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		#todo 双向队列，方法1的效率不够高
		if len(nums) == 0:
			return []
		if k >= len(nums):
			return [max(nums)]
		result = []
		maxValue = max(nums[0:k])
		result.append(maxValue)
		p = 1
		while p + k <= len(nums):
			# result.append(max(nums[p:p+k]))
			p+=1
		return result
solution = Solution()
print(solution.maxSlidingWindow([1],10))
