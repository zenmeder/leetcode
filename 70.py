#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def climbStairs(self, n):
		dp = [0 for i in range(n+1)]
		for i in range(n+1):
			if i==0 or i==1:
				dp[i] = 1
			else:
				dp[i] = dp[i-1]+dp[i-2]
		return dp[-1]
print(Solution().climbStairs(3))

