#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		length = len(nums)
		d = dict()
		for i in range(length):
			if nums[i] in d:
				del d[nums[i]]
			else:
				d[nums[i]] = 1
		return list(d.keys())
solution = Solution()
print(solution.singleNumber([1, 2, 1, 3, 2, 5]))