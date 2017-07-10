#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# todo
		if len(nums) == 1:
			return 1
		if nums[-1]-1 in nums:
			return max(self.longestConsecutive(nums[:-1]))