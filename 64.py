#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid or not grid[0]:
			return 0
		dp = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if i == 0 and j == 0:
					dp[i][j] = grid[0][0]
				elif i == 0 and j != 0:
					dp[i][j] = grid[i][j]+dp[i][j-1]
				elif i != 0 and j == 0:
					dp[i][j] = grid[i][j]+dp[i-1][j]
				else:
					dp[i][j] = grid[i][j]+min(dp[i][j-1], dp[i-1][j])

		return dp[-1][-1]

print(Solution().minPathSum([[1,2,3],[4,5,6]]))