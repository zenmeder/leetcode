#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def findKthNumber(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: int
		"""
		i , a, flag = 1, 1, True
		while i<k:
			if a * 10 <= n:
				a *= 10
			elif a + 1 <= n:
				a += 1
				while not a%10:
					a = a//10
			else:
				a = a//10+1
			i += 1
		return a

print(Solution().findKthNumber(681692778
,351251360
))
