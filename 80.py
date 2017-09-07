#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from collections import Counter


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		result = 0
		for i in Counter(nums).values():
			result += min(i, 2)
		return result

print(Solution().removeDuplicates([1,1,1,2]))