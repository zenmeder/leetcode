#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def missingNumber(self, nums):
		n = len(nums)
		return int(n * (n + 1) / 2 - sum(nums))


print(Solution().missingNumber([2, 0]))
