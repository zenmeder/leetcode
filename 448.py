#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		for i in range(len(nums)):
			a = nums[i] if nums[i] > 0 else -nums[i]
			if nums[a - 1] > 0:
				nums[a - 1] = -nums[a - 1]
		for i in range(len(nums)):
			if nums[i] > 0:
				result.append(i+1)

		return result

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))