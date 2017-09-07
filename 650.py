#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def minSteps(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0,0]
		for i in range(2, n+1):
			times = 0x7FFFFFFF
			for j in range(1, i):
				if i%j == 0:
					times = min(times, dp[j]+i/j)
			dp.append(times)
		return int(dp[-1])

print(Solution().minSteps(1))