#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]
		dps = []
		dps.append([nums[0], None] if nums[0] > 0 else [None, nums[0]])
		res = 0 if nums[0] < 0 else nums[0]
		for i in range(1, len(nums)):
			if nums[i] > 0:
				a = nums[i] if not dps[-1][0] else nums[i] * dps[-1][0]
				b = None if not dps[-1][1] else nums[i] * dps[-1][1]
			elif nums[i] < 0:
				a = None if not dps[-1][1] else nums[i] * dps[-1][1]
				b = nums[i] if not dps[-1][0] else nums[i] * dps[-1][0]
			elif nums[i] == 0:
				a = 0
				b = 0
			dps.append([a,b])
			if a:
				res = max(res, a)
		return res

print(Solution().maxProduct([-3,0,-2,4]))

