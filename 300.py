#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		ranks = [nums[0]]
		for i in range(1, len(nums)):

