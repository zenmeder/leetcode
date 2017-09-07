#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
		dp = [1] + [float('inf')]*n
		for i in range(n+1):
			for num in nums:
				if num > i: break
				if num == i: dp[i] = 1
				if num <i: dp[i] = min(dp[i], dp[i-num]+1)
		return dp[-1]

print(Solution().numSquares(6052))