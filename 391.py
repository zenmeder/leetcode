#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isRectangleCover(self, rectangles):
		"""
		:type rectangles: List[List[int]]
		:rtype: bool
		"""
		edges = dict()
		lb, rt = [float('inf'), float('inf')], [float('-inf'), float('-inf')]
		for rectangle in rectangles:
			lb = min(lb, rectangle[:2])
			rt = max(rt, rectangle[-2:])
			for i in range(rectangle[0], rectangle[2] + 1):
				for j in range(rectangle[1], rectangle[3] + 1):
					if i != rectangle[0]:
						if (i - 1, j, i, j) not in edges:
							edges[(i - 1, j, i, j)] = 1
						else:
							return False
					if j != rectangle[1]:
						if (i, j - 1, i, j) not in edges:
							edges[(i, j - 1, i, j)] = 1
						else:
							return False

		for i in range(lb[0], rt[0] + 1):
			for j in range(lb[1], rt[1] + 1):
				if i != lb[0]:
					if (i - 1, j, i, j) not in edges:
						return False
				if j != lb[1]:
					if (i, j - 1, i, j) not in edges:
						return False
		return True


print(Solution().isRectangleCover([
	[1, 1, 3, 3],
	[3, 1, 4, 2],
	[3, 2, 4, 4],
	[1, 3, 2, 4],
	[2, 3, 3, 4]
]))
