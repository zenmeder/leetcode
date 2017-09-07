#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from math import sqrt,ceil
class Solution(object):
	def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""
		l =	int(ceil(sqrt(area)))
		while l < area:
			if not area % l:
				return [l, area//l]
			l += 1
		return [area, 1]
print(Solution().constructRectangle(1))