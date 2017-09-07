#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from math import fabs,sqrt

class Solution(object):
	def computeArea(self, A, B, C, D, E, F, G, H):
		"""
		:type A: int
		:type B: int
		:type C: int
		:type D: int
		:type E: int
		:type F: int
		:type G: int
		:type H: int
		:rtype: int
		"""
		l = []
		for x in [A, C]:
			for y in [B, D]:
				if min(E, G) <= x <= max(E, G) and min(F, H) <= y <= max(F, H):
					l.append([x, y])

		for x in [E,G]:
			for y in [F, H]:
				if min(A, C) <= x <= max(A, C) and min(B, D) <= y <= max(B, D):
					l.append([x, y])
		print(l)
		if len(l) == 2:
			return int(fabs(l[0][0] - l[1][0]) * fabs(l[0][1] - l[1][1]))
		elif len(l) == 8:
			return int(fabs(A-C) * fabs(B-D))
		elif len(l) == 4:
			a = max(fabs(l[0][0] - l[1][0]), fabs(l[0][1] - l[1][1]))
			b = min(self.distance(l[0],l[2]), self.distance(l[0], l[3]))
			return int(a*b)
		else:
			return 0

	def distance(self, x, y):
		return sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2 )


print(Solution().computeArea(-2,-2,2,2,0,-2,3,2))