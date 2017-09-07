#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if not nums:
			return [[]]
		result = set()
		nums.sort()
		for num in nums:
			if not result:
				result.add(tuple([]))
				result.add(tuple([num]))
			else:
				for s in result.copy():
					s = list(s)
					s.append(num)
					result.add(tuple(s))
		return [list(a) for a in result]
print(Solution().subsetsWithDup([1,4,4,4,1]))
