#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def uniquePaths(self, m, n):
		# 递归算法
		dp = [[0 for i in range(m)] for j in range(n)]
		for i in range(n):
			for j in range(m):
				if i==0 or j==0:
					dp[i][j] = 1
				else:
					dp[i][j] = dp[i-1][j]+dp[i][j-1]
		return dp[-1][-1]
print(Solution().uniquePaths(2,2))