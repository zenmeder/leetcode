#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def searchMatrix(self, matrix, target):
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		row, column = 0, len(matrix[0]) - 1
		while row < len(matrix) and column >= 0:
			if target == matrix[row][column]:
				return True
			elif target > matrix[row][column]:
				row += 1
			elif target < matrix[row][column]:
				column -= 1
		return False
	def searchMatrix1(self, matrix, target):
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		low = 0
		high = len(matrix) - 1
		while low <= high:
			mid = (low + high) // 2
			if matrix[mid][0] == target:
				return True
			elif matrix[mid][0] > target:
				high = mid - 1
				continue
			elif matrix[mid][0] < target:
				low = mid + 1
				continue
		left = 0
		right = len(matrix[0]) - 1
		while left <= right:
			mid = (left + right) // 2
			if matrix[high][mid] == target:
				return True
			elif matrix[high][mid] < target:
				left = mid + 1
				continue
			elif matrix[high][mid] > target:
				right = mid - 1
				continue
		return False


print(Solution().searchMatrix([
	[1, 3, 5, 7],
	[10, 11, 16, 20],
	[23, 30, 34, 50]
], 22))
