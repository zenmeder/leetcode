#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		plus = True
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				if plus:
					return nums[i]
				plus = False
			else:
				plus = True
		return nums[-1]
print(Solution().findPeakElement([1,2,3,4]))
