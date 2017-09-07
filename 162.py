#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		for i in range(1,len(nums)):
			if nums[i] < nums[i-1]:
				return i-1
		return len(nums)-1
