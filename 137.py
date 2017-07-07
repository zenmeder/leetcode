#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# 用dict实现 beat 53%
		length = len(nums)
		d = dict()
		for i in range(length):
			if nums[i] in d:
				d[nums[i]] += 1
			else:
				d[nums[i]] = 1
		for item in d.items():
			if item[1]!=3:
				return item[0]
solution = Solution()
print(solution.singleNumber([1,2,2,2,1,4,1]))