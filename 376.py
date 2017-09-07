#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def wiggleMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return nums
		up, down = [1], [1]
		for i in range(1,len(nums)):
			if nums[i] > nums[i-1]:
				up.append(down[-1]+1)
				down.append(down[-1])
			elif nums[i] < nums[i-1]:
				up.append(up[-1])
				down.append(up[-1]+1)
			else:
				up.append(up[-1])
				down.append(down[-1])
		return max(up[-1], down[-1])

