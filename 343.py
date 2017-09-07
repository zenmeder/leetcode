#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if not n:
			return 0
		elif n == 2:
			return 1
		elif n == 3:
			return 2
		elif n%3 == 0:
			return int(3**(n/3))
		elif (n-2)%3 == 0:
			return int(2*3**((n-2)/3))
		elif (n-4)%3 == 0:
			return int(4*3**((n-4)/3))

print(Solution().integerBreak(11))