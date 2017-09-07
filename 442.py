#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		result = []
		for i in range(len(nums)):
			a = nums[i] if nums[i] > 0 else -nums[i]
			if nums[a - 1] < 0:
				result.append(nums[i] if nums[i] > 0 else -nums[i])
			else:
				nums[a - 1] = -nums[a - 1]
		return result


print(Solution().findDuplicates([2,3,1]))
