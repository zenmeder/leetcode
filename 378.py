#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import heapq


class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		# use heapq
		# if not matrix:
		# 	return 0
		# hq = []
		# for i in range(len(matrix)):
		# 	for j in range(len(matrix[0])):
		# 		heapq.heappush(hq, matrix[i][j])
		# i = 0
		# while i < k-1:
		# 	heapq.heappop(hq)
		# 	i += 1
		# return heapq.heappop(hq)
		position = [0] * len(matrix)
		i = 0

		while i < k:
			minPosition, minValue = 0, float('inf')
			for j in range(len(position)):
				if position[j] == len(matrix[0]):
					continue
				if matrix[j][position[j]] < minValue:
					minValue = matrix[j][position[j]]
					minPosition = j
			position[minPosition] += 1
			i += 1

		return minValue
print(Solution().kthSmallest([
	[1, 5, 9],
	[10, 11, 13],
	[12, 13, 15]
], 6))
