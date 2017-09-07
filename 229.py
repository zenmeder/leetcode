#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return []
		count = {}
		result = []
		for num in nums:
			if num in count:
				if count[num] < 0:
					continue
				count[num] += 1
			else:
				count[num] = 1
			if count[num] > int(len(nums) / 3):
				result.append(num)
				count[num] = - count[num]
		return result