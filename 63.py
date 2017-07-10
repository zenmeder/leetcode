#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
		for i in range(len(obstacleGrid)):
			for j in range(len(obstacleGrid[0])):
				if obstacleGrid[i][j] == 1:
					dp[i][j] = 0
				elif i>=1 and j>=1:
					dp[i][j] = dp[i-1][j]+dp[i][j-1]
				elif i==0 and j>=1:
					dp[i][j] = dp[i][j-1]
				elif i>=1 and j==0:
					dp[i][j] = dp[i-1][j]
				else:
					dp[0][0] = 1
		return dp[-1][-1]
print(Solution().uniquePathsWithObstacles([
  [0],
  [1],
]))