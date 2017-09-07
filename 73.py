#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		rows = [0] * len(matrix)
		columns = [0] * len(matrix[0])
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 0:
					rows[i], columns[j] = 1, 1
		print(rows, columns)
		for i, row in enumerate(rows):
			if row:
				matrix[i] = [0] * len(matrix[0])

		for j, column in enumerate(columns):
			if column:
				for i in range(len(matrix)):
					matrix[i][j] = 0
		print(matrix)

Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
