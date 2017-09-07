#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def integerReplacement(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 3:
			return n - 1
		times = 0
		while n != 2:
			if n == 3:
				times+=1
				break
			elif n % 2 == 0:
				n = n / 2
				times += 1
			elif n % 4 == 1:
				n = n - 1
				times += 1
			else:
				n = n + 1
				times += 1
		return times + 1


print(Solution().integerReplacement(65535))
