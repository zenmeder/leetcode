#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findUnsortedSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sorted_nums = sorted(nums)
		i, j = 0, len(nums)-1
		while i < len(nums)  and nums[i] == sorted_nums[i]:
			i += 1
		while j > 0 and nums[j] == sorted_nums[j]:
			j -= 1
		return j-i+1 if j>i else 0

print(Solution().findUnsortedSubarray([1,2,3,4]))