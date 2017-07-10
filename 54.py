#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0:
			return []
		if len(matrix[0]) == 0:
			return []
		if len(matrix[0]) == 1:
			return [matrix[i][0] for i in range(len(matrix))]
		high = 0
		low = len(matrix) - 1
		left = 0
		right = len(matrix[0]) - 1
		orientation = 0
		row = column = 0
		result = []
		while high <= low and left <= right:
			print(row,column,high,low,left,right)
			result.append(matrix[row][column])
			if orientation == 0:
				column += 1
			elif orientation == 1:
				row += 1
			elif orientation == 2:
				column -= 1
			elif orientation == 3:
				row -= 1
			if column == right and orientation == 0:
				orientation = 1
				high += 1
			elif row == low and orientation == 1:
				orientation = 2
				right -= 1
			elif column == left and orientation == 2:
				orientation = 3
				low -= 1
			elif row == high and orientation == 3:
				orientation = 0
				left += 1
		result.append(matrix[row][column])
		return result


solution = Solution()
print(solution.spiralOrder([
	[1],
	[2]
	# [4,5,6],
	# [7, 8, 9]
]))
