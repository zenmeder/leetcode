#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		if numRows == 0:
			return []
		dp = [[1]]
		row = 1
		while row < numRows:
			above = dp[-1]
			print(dp)
			l = []
			l.append(above[0])
			if len(above) > 1:
				for i in range(len(above)-1):
					l.append(above[i]+above[i+1])
			l.append(above[-1])
			dp.append(l)
			row += 1
		return dp
print(Solution().generate(5))
