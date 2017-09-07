#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def circularArrayLoop(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if not nums:
			return False
		length = len(nums)
		if nums[0] == length:
			return False
		i = nums[0]
		while i != 0 and nums[i] != length:
			i += nums[i]
			if i >= length:
				i %= length
		if not i:
			return True
		return False


print(Solution().circularArrayLoop([-2,1,-1,-2,-2]))
