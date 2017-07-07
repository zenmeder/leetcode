#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math


class Solution(object):
	def arrangeCoins(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return math.floor((math.sqrt(1+8*n)-1)/2)

solution = Solution()
print(solution.arrangeCoins(8))