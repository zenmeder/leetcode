#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		row = column = 0
		m = len(matrix)
		if m == 0:
			return False
		n = len(matrix[0])
		if n == 0:
			return False
		print(m, n)
		while row < m and column < n:
			if matrix[row][column] == target:
				return True
			if row == m - 1 and column == n - 1:
				return False
			p = row
			q = column
			while q < n:
				if matrix[p][q] == target:
					return True
				q += 1

			q = column
			while p < m:
				if matrix[p][q] == target:
					return True
				p += 1
			if row + 1 < m:
				row += 1
			if column + 1 < n:
				column += 1


solution = Solution()
print(solution.searchMatrix([[1, 1]
							 ], 0))
