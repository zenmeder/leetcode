#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def lastRemaining(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		nums = [i for i in range(1, n+1)]
		orientation = 1
		while len(nums) > 1:
			if orientation:
				orientation = 0
				for i in range(len(nums))[::-1]:
					if not i%2:
						del nums[i]
			else:
				orientation = 1
				length = len(nums)
				for i in range(len(nums))[::-1]:
					if (length-i) % 2:
						del nums[i]
		return nums[0]

print(Solution().lastRemaining(5305))