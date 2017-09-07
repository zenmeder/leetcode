#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"


class Solution(object):
	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		if not M or not M[0]:
			return 0
		circles = []
		for i in range(len(M)):
			flag = 0
			for j in range(i):
				if not M[i][j]:
					continue
				flag = 1
				if not circles:
					circles.append(set([i, j]))
					continue
				for k in range(len(circles)):
					if j in circles[k]:
						circles[k].add(i)
						break
				else:
					circles.append(set([i]))
			if not flag:
				circles.append(set([i]))
			count = len(circles)
			for i in range(len(circles) - 1):
				for j in range(i + 1, len(circles)):
					if not circles[i] & circles[j]:
						count += 1
		return count


print(Solution().findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
