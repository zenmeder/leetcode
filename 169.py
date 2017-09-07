#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = {}
		for num in nums:
			if num in count:
				count[num] += 1
			else:
				count[num] = 1
			if count[num] > int(len(nums) / 2):
				return num

print(Solution().majorityElement([1]))