#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		dp = [[0 for i in range(len(triangle[j]))] for j in range(len(triangle))]
		dp[0][0] = triangle[0][0]
		for i in range(1, len(triangle)):
			for j in range(len(triangle[i])):
				if j == 0:
					dp[i][j] = dp[i-1][j]+triangle[i][j]
				elif j==len(triangle[i])-1:
					dp[i][j] = dp[i-1][j-1]+triangle[i][j]
				else:
					dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
		return min(dp[-1])

tr = [[-1],
	  # [2,3],
	  # [1,-1,-1]]
	  ]
print(Solution().minimumTotal(tr))