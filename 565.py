#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def arrayNesting(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maxlength = 0
		record = {}
		for num in nums:
			length = 0
			while num not in record and num < len(nums):
				record[num] = 1
				num = nums[num]
				length += 1
			maxlength = max(length,maxlength)
		return maxlength

print(Solution().arrayNesting([5,4,0,3,1,6,2]))
