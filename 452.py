#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

#label: 贪心算法
class Solution(object):
	def findMinArrowShots(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		points = sorted(points, key = lambda x: x[1])
		count = 0
		pend = None
		for point in points:
			if pend == None:
				pend = point[1]
				count += 1
			elif point[0] > pend:
				pend = point[1]
				count += 1
		return count

print(Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))