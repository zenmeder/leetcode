#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

import random
class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		for i in range(len(nums)-1):
			for j in range(i+1, len(nums)):
				if nums[i] > nums[j]:
					nums[i], nums[j] = nums[j], nums[i]
		return nums

print(Solution().sortColors([random.randint(0,2) for i in range(100)]))
