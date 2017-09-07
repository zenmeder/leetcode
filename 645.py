#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findErrorNums(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		d = {i:0 for i in range(1, len(nums)+1)}
		result = []
		for num in nums:
			if d[num] == 0:
				d[num] = 1
			else:
				result.append(num)
		for i in d.keys():
			if d[i] == 0:
				result.append(i)
				return result
print(Solution().findErrorNums([]))
