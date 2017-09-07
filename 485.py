#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maxOne = count = 0
		for num in nums:
			if num == 1:
				count += 1
			elif num == 0:
				count = 0
			maxOne = max(maxOne, count)
		return maxOne

print(Solution().findMaxConsecutiveOnes([]))
