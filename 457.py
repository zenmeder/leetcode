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
		for i in range(length):
			if nums[i] % length == 0:
				continue
			start = i


print(Solution().circularArrayLoop([1,2,3,4,5]))
3 1 2