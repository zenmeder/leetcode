#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		res = [1]
		for i in range(0, rowIndex//2):
			res.append(int(res[-1]*(rowIndex-i)/(i+1)))
		if rowIndex%2:
			res = res + res[::-1]
		else:
			res = res + res[:-1][::-1]

		return res

print(Solution().getRow(100))