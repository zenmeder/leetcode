#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		return sum(nums[::2])

print(Solution().arrayPairSum([4,3,1,2]))