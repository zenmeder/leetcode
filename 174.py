#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def calculateMinimumHP(self, dungeon):
		"""
		:type dungeon: List[List[int]]
		:rtype: int
		"""
		if not dungeon or not dungeon[0]:
			return -1
		m = [[0 for j in range(len(dungeon[i]))] for i in range(len(dungeon))]
		n = [[0 for j in range(len(dungeon[i]))] for i in range(len(dungeon))]
		for i in range(len(dungeon)):
			for j in range(len(dungeon[i])):
				if i == 0 and j == 0:
					m[i][j] = max(1 - dungeon[i][j], 1)
					n[i][j] = m[i][j] + dungeon[i][j]
				elif i == 0 and j != 0:
					m[i][j] = max(m[i][j-1]+1-n[i][j-1]-dungeon[i][j],m[i][j-1])
					n[i][j] = m[i][j] - m[i][j - 1] + n[i][j - 1] + dungeon[i][j]
				elif j == 0 and i != 0:
					m[i][j] = max(m[i-1][j]+1-n[i-1][j]-dungeon[i][j],m[i-1][j])
					n[i][j] = m[i][j] - m[i-1][j] + n[i-1][j] + dungeon[i][j]
				elif max(m[i-1][j]+1-n[i-1][j]-dungeon[i][j],m[i-1][j]) < max(m[i][j-1]+1-n[i][j-1]-dungeon[i][j],m[i][j-1]):
					m[i][j] = max(m[i-1][j]+1-n[i-1][j]-dungeon[i][j],m[i-1][j])
					n[i][j] = m[i][j] - m[i-1][j] + n[i-1][j] + dungeon[i][j]
				else:
					m[i][j] = max(m[i][j-1]+1-n[i][j-1]-dungeon[i][j],m[i][j-1])
					n[i][j] = m[i][j] - m[i][j - 1] + n[i][j - 1] + dungeon[i][j]
		return m,n

print(Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))
