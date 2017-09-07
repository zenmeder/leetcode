#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		rank = []
		snums = sorted(nums, reverse=True)
		for num in nums:
			id = snums.index(num)
			if  id == 0:
				rank.append('Gold Medal')
			elif id == 1:
				rank.append('Silver Medal')
			elif id == 2:
				rank.append('Bronze Medal')
			else:
				rank.append(str(id+1))
		return rank

print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))