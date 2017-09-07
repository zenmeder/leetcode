#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		for i in range(1, len(nums))[::-1]:
			if nums[i] < nums[i-1]:
				return nums[i]
		return nums[0]

print(Solution().findMin([0,1,2,4,5,6,7,0]))