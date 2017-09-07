#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		res, i = 0, 1
		while 5 ** i <= n:
			res += n//(5**i)
			i += 1
		return res
print(Solution().trailingZeroes(25))

