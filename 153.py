#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		low, high = 0, len(nums) - 1
		while low < high:
			if nums[low] < nums[low + 1]:
				low += 1
			else:
				return nums[low+1]
			if nums[high] > nums[high - 1]:
				high -= 1
			else:
				return nums[high]
		return nums[0]

print(Solution().findMin([3]))
