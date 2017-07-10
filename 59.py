#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		result = [[0 for i in range(n)] for j in range(n)]
		high = left = 0
		low = n - 1
		left = 0
		right = n - 1
		orientation = 0
		row = column = 0
		for i in range(n ** 2):
			result[row][column] = i + 1
			if orientation == 0:
				column += 1
			elif orientation == 1:
				row += 1
			elif orientation == 2:
				column -= 1
			elif orientation == 3:
				row -= 1
			if orientation == 0 and column == right:
				orientation = 1
				high += 1
			elif orientation == 1 and row == low:
				orientation = 2
				right -= 1
			elif orientation == 2 and column == left:
				orientation = 3
				low -= 1
			elif orientation == 3 and row == high:
				orientation = 0
				left += 1
		return result

solution = Solution()
print(solution.generateMatrix(0))